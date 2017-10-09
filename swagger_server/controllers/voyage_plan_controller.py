# coding: utf-8

import connexion
from swagger_server.models.get_subscription_response import GetSubscriptionResponse
from swagger_server.models.get_voyage_plan_response import GetVoyagePlanResponse
from swagger_server.models.voyage_plan import VoyagePlan
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime

import json
from pathlib import Path
import os
import requests
import xml.etree.ElementTree as ET
import io
import re
from . import rtz10
from . import rtz11
from . import rtzstm11
import sys
from datetime import datetime
import collections
from swagger_server import service

def log_event(name, callback, uvid = None):
    data = collections.OrderedDict()
    data['time'] = datetime.utcnow().replace(microsecond=0).isoformat() + 'Z'
    if not (client_mrn() is None):
        data['client'] = client_mrn()
    if not (name is None):
        data['event'] = name
    if not (uvid is None):
        data['uvid'] = uvid
    if not (callback is None):
        data['callback'] = callback
    with open('import/event.log', 'a') as f:
        json.dump(data, f, ensure_ascii=True)
        f.write('\n')

def client_mrn():
    """
    Get the real DN name of the requestor
    or return the testing requestor
    """
    for hdr in connexion.request.headers:
        if hdr[0] == 'Ssl-Dn':
            for field in hdr[1].split('/'):
                if len(field) > 5:
                    if field[0:4] == 'UID=':
                        print(field[4:])
                        return field[4:]
    return 'urn:mrn:stm:service:instance:furuno:vis2'

def check_acl():
    """
    Check if client is authorized in the access list of the voyage
    """
    fname = 'export/all.acl'
    if os.path.isfile(fname):
        with open(fname) as f:
            data = json.loads(f.read())
            if client_mrn() in data:
                return True

    fname = 'export/monitored.subs'
    if os.path.isfile(fname):
        with open(fname) as f:
            data = json.loads(f.read())
            if client_mrn() in data:
                return True

    fname = 'export/alternate.subs'
    if os.path.isfile(fname):
        with open(fname) as f:
            data = json.loads(f.read())
            if client_mrn() in data:
                return True

    if not service.conf is None:
        if service.conf['open_to_all']:
            return True
    return False

def getuvid(routename):
    fname = 'export/' + routename
    if os.path.isfile(fname):
        tree = ET.parse(fname)
        root = tree.getroot()
        tag='{http://www.cirm.org/RTZ/1/1}'
        routeInfo = root.find(tag + 'routeInfo')
        return(routeInfo.get('vesselVoyage'))

def get_subscription_to_voyage_plans(callbackEndpoint):
    """
    
    Retrieve a list of subcribed UVID for the callBackEndPoint and Organization
    :param callbackEndpoint: Callback expected. Base url of the vis instance as in the Service Registry. The callback response will be sended to the voyagePlans endPoint of the instance
    :type callbackEndpoint: str

    :rtype: List[GetSubscriptionResponse]
    """
    subsl = []
    fname = 'export/monitored.subs'
    if os.path.isfile(fname):
        with open(fname) as f:
            data = json.loads(f.read())
            if client_mrn() in data:
                subsl.append(getuvid('monitored.rtz'))

    fname = 'export/alternate.subs'
    if os.path.isfile(fname):
        with open(fname) as f:
            data = json.loads(f.read())
            if client_mrn() in data:
                subsl.append(getuvid('alternate.rtz'))

    log_event('get_subscriptions', callbackEndpoint)
    return subsl

def get_voyage_plans(uvid=None, routeStatus=None):
    """
    
    Returns active VoyagePlans
    :param uvid: Unique identity (URN) of a voyageplan
    :type uvid: str
    :param routeStatus: Status of a route for a voyageplan: 1-Original   2-Planned_for_voyage    3-Optimized 4-Cross_Checked 5-Safety_Checked    6-Approved  7-Used_for_monitoring   8-Inactive
    :type routeStatus: str

    :rtype: GetVoyagePlanResponse
    """
    if not check_acl():
        return 'Forbidden', 403
    vps = []
    fname = 'export/monitored.rtz'
    if os.path.isfile(fname):
        filterOK = True
        if not (uvid is None):
            if uvid == getuvid('monitored.rtz'):
                filterOK = False
        if not (routeStatus is None):
            if int(routeStatus) != 7:
                filterOK = False
        if filterOK:
            with open(fname) as f:
                vp = VoyagePlan()
                vp.route = f.read()
                vps.append(vp)
    fname = 'export/alternate.rtz'
    if os.path.isfile(fname):
        filterOK = True
        if not (uvid is None):
            if uvid == getuvid('alternate.rtz'):
                filterOK = False
        if not (routeStatus is None):
            if int(routeStatus) == 7:
                filterOK = False
        if filterOK:
            with open(fname) as f:
                vp = VoyagePlan()
                vp.route = f.read()
                vps.append(vp)
    if len(vps) == 0:
        return 'No voyage plans found', 404
    if os.path.exists('export/last_interaction_time'):
        with open('export/last_interaction_time', 'r') as f:
            timestamp = f.read()
    else:
        timestamp = datetime.utcnow().replace(microsecond=0).isoformat() + 'Z'
    log_event('get_voyage', None)
    return GetVoyagePlanResponse(last_interaction_time=timestamp, voyage_plans=vps)

def remove_voyage_plan_subscription(callbackEndpoint, uvid=None):
    """
    
    Remove subscription for active Voyage Plan from other services i.e. Enhanced Monitoring
    :param callbackEndpoint: Callback expected. Base url of the vis instance as in the Service Registry. The callback response will be sended to the voyagePlans endPoint of the instance
    :type callbackEndpoint: str
    :param uvid: Unique identity (URN) of a voyageplan
    :type uvid: str

    :rtype: None
    """
    me = { 'uid': client_mrn(), 'url': callbackEndpoint}
    meacl = client_mrn()
    p = Path('import')
    if uvid is None:
        vp = 'all'
    else:
        vp = uvid
    uvids = list(p.glob('**/' + vp + '.rmsubs'))
    if len(uvids) > 0:
        with uvids[0].open() as f: data = json.loads(f.read())
        f.close()
        if not check_acl():
            return 'Forbidden', 403
        if not (me in data):
            data.append(me)
    else:
        data = [ me ]
    f = open('import/' + vp + '.rmsubs', 'w')
    f.write(json.dumps(data))
    f.close()
    log_event('remove_subscription', callbackEndpoint, uvid)
    return 'OK'


def subscribe_to_voyage_plan(callbackEndpoint, uvid=None):
    """
    
    Request subscription for active Voyage Plan from other services i.e. Enhanced Monitoring
    :param callbackEndpoint: Callback expected. Base url of the vis instance as in the Service Registry. The callback response will be sended to the voyagePlans endPoint of the instance
    :type callbackEndpoint: str
    :param uvid: Unique identity (URN) of a voyageplan. If no uvid is provided, the subcription is to all the active uvid that your organization has access to
    :type uvid: str

    :rtype: None
    """
    meacl = client_mrn()
    if uvid is None:
        vp1 = 'all'
    else:
        vp1 = uvid
    p = Path('export')
    if callbackEndpoint == 'allow':
        acls = list(p.glob('**/*' + vp1 + '.acl'))
        if len(acls) > 0:
            with acls[0].open() as f: data = json.loads(f.read())
            f.close()
            if not (meacl in data):
                data.append(meacl)
        else:
            data = [ meacl ]
        f = open('export/' + vp1 + '.acl', 'w')
        f.write(json.dumps(data))
        f.close()
        return 'OK'
    elif callbackEndpoint == 'deny':
        acls = list(p.glob('**/*' + vp1 + '.acl'))
        if len(acls) > 0:
            with acls[0].open() as f: data = json.loads(f.read())
            f.close()
            if meacl in data:
                data.remove(meacl)
            if len(data) == 0:
                os.remove('export/' + vp1 + '.acl')
            else:
                f = open('export/' + vp1 + '.acl', 'w')
                f.write(json.dumps(data))
                f.close()
        return 'OK'
    elif callbackEndpoint == 'delete':
        uvids = list(p.glob('**/*' + vp1 + '.uvid'))
        if len(uvids) > 0:
            os.remove('export/' + vp1 + '.uvid')
            os.remove('export/' + vp1 + '.rtz')
        uvids = list(p.glob('**/*' + vp1 + '.subs'))
        if len(uvids) > 0:
            os.remove('export/' + vp1 + '.subs')
        uvids = list(p.glob('**/*' + vp1 + '.acl'))
        if len(uvids) > 0:
            os.remove('export/' + vp1 + '.acl')
        return 'OK'

    me = { 'uid': client_mrn(), 'url': callbackEndpoint}
    allowed=True
    p = Path('import')
    if uvid is None:
        vp = 'all'
    else:
        vp = uvid
        p2 = Path('export')
        uvids = list(p2.glob('**/' + uvid + '.uvid'))
        if len(uvids) == 0:
            return 'Voyage plan ' + uvid + ' not found', 404
        if not check_acl():
            allowed = False
    uvids = list(p.glob('**/*' + vp + '.subs'))
    if len(uvids) > 0:
        with uvids[0].open() as f: data = json.loads(f.read())
        f.close()
        if not (me in data):
            data.append(me)
    else:
        data = [ me ]
    if allowed:
        f = open('import/' + vp + '.subs', 'w')
        f.write(json.dumps(data))
        f.close()
        log_event('subscribe', callbackEndpoint, uvid)
        return 'OK'
    return 'Forbidden', 403


def upload_voyage_plan(voyagePlan, deliveryAckEndPoint=None, callbackEndpoint=None):
    """
    
    Upload VoyagePlan to VIS from other services i.e. Route Optimization service.
    :param voyagePlan: Voyage Plan in RTZ format
    :type voyagePlan: str
    :param deliveryAckEndPoint: Acknowledgement expected. Base URL for VIS as in Service Registry. An ack is send back to this url when the private application retrieve the message from the VIS 
    :type deliveryAckEndPoint: str
    :param callbackEndpoint: Callback expected. Base url of the vis instance as in the Service Registry. The callback response will be sended to the voyagePlans endPoint of the instance
    :type callbackEndpoint: str

    :rtype: None
    """
    uvid='parse:from:rtz'
    f = open('import/' + uvid + '.rtz', 'wb')
    f.write(voyagePlan)
    f.close()
    f = open('import/' + uvid + '.rtz', 'r')
    vp = f.read()
    f.close()
    RE_XML_ENCODING = re.compile("encoding=\"UTF-8\"", re.IGNORECASE)
    rtz = io.StringIO()
    rtz.write(RE_XML_ENCODING.sub("", vp, count=1))
    rtz.seek(0)
    doc = ET.parse(rtz)
    root = doc.getroot()
    if root.tag == '{http://www.cirm.org/RTZ/1/0}route':
        '''
        if rtz10.xmlschema.validate(doc) == False:
            rtz.close()
            ret = rtz10.xmlschema.error_log
            return ret, 400
        '''
        result = True
        tag='{http://www.cirm.org/RTZ/1/0}'
    else:
        if root.tag == '{http://www.cirm.org/RTZ/1/1}route':
            try:
                result = rtzstm11.xmlschema.validate(doc)
                if result == False:
                    rtz.close()
                    ret = str(rtzstm11.xmlschema.error_log)
                    return ret, 400
            except:
                result = False
            tag='{http://www.cirm.org/RTZ/1/1}'
        else:
            rtz.close()
            ret = 'Unsupported route format'
            return ret, 400
    if result == False:
        rtz.close()
        return ret, 400
    routeInfo = doc.find(tag + 'routeInfo')
    uvid = routeInfo.get('vesselVoyage')
    if uvid is None:
        return 'Missing vesselVoyage', 404
    routeName = routeInfo.get('routeName')
    if routeName is None:
        return 'Missing routeName', 404
    if not ('urn:mrn:stm:voyage:id' in uvid):
        return 'Wrong vesselVoyage format', 400
    if tag == '{http://www.cirm.org/RTZ/1/1}':
        routeInfo = doc.find(tag + 'routeInfo')
        extensions = routeInfo.find(tag + 'extensions')
        if extensions is None:
            return 'Missing routeInfo/extensions', 404
        extension = extensions.find(tag + 'extension')
        if extension is None:
            return 'Missing routeInfo/extensions/extension', 404
        routeStatus = extension.get('routeStatusEnum')
        if routeStatus is None:
            return 'Missing routeInfo/extensions/extension/routeStatusEnum', 404
    else:
        routeStatus = routeInfo.get('routeStatus')
    if not (routeStatus in '12345678'):
        return 'Wrong routeStatus format', 400
    f = open('import/' + routeName + '.rtz', 'wb')
    f.write(voyagePlan)
    f.close()
    data = { 'uvid': uvid, 'route': routeName + '.rtz', 'routeStatus': routeStatus, 'from': client_mrn() }
    f = open('import/' + uvid + '.uvid', 'w')
    f.write(json.dumps(data))
    f.close()
    servicetype, url, name = service.get_service_url(client_mrn())
    if deliveryAckEndPoint is not None:
        data = collections.OrderedDict()
        data['endpoint'] = deliveryAckEndPoint
        data['id'] = uvid
        data['fromName'] = name
        data['fromId'] = client_mrn()
        data['time'] = datetime.utcnow().replace(microsecond=0).isoformat() + 'Z'
        if not service.conf is None:
            data['toId'] = service.conf['id']
            data['toName'] = service.conf['name']

        with open('import/' + uvid + '.ack', 'w') as f:
            f.write(json.dumps(data))
    service.log_event('received voyageplan', name=routeName, status = name)
    return 'OK'

