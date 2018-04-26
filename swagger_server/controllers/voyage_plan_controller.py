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
from lxml import etree
import io
import re
from . import rtz10
from . import rtz11
from . import rtzstm11
import sys
from datetime import datetime
import collections
from swagger_server import service

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
                        print(field[4:], 'RTZ')
                        return field[4:]
    return 'urn:mrn:stm:service:instance:furuno:vis2'

def check_acl(mrn):
    """
    Check if client is authorized in the access list of the voyage
    """
    fname = 'export/all.acl'
    if os.path.isfile(fname):
        with open(fname) as f:
            data = json.loads(f.read())
            if mrn in data:
                return True

    fname = 'export/monitored.subs'
    if os.path.isfile(fname):
        with open(fname) as f:
            data = json.loads(f.read())
            if mrn in data:
                return True

    fname = 'export/alternate.subs'
    if os.path.isfile(fname):
        with open(fname) as f:
            data = json.loads(f.read())
            if mrn in data:
                return True

    if not service.conf is None:
        if service.conf['open_to_all']:
            return True
    return False

def getuvid(routename):
    fname = 'export/' + routename
    if os.path.isfile(fname):
        tree = etree.parse(fname)
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
    mrn = client_mrn()
    if not service.released(mrn):
        service.log_event('RTZ from not released service', client = mrn, eventNumber = 29, eventType = 6, eventDataType = 1)
        return 'We only talk with released services', 403

    if not check_acl(mrn):
        service.log_event('RTZ not allowed', client = mrn, eventNumber = 29, eventType = 6, eventDataType = 1)
        return 'Forbidden', 403

    subsl = []
    fname = 'export/monitored.subs'
    if os.path.isfile(fname):
        with open(fname) as f:
            data = json.loads(f.read())
            if mrn in data:
                subsl.append(getuvid('monitored.rtz'))

    fname = 'export/alternate.subs'
    if os.path.isfile(fname):
        with open(fname) as f:
            data = json.loads(f.read())
            if mrn in data:
                subsl.append(getuvid('alternate.rtz'))

    evpar = 'callbackEndpoint:' + callbackEndpoint
    service.log_event('get_subscriptions', client=mrn, callback=callbackEndpoint, eventNumber = 29, eventType = 1, eventDataType = 1, eventParameters = evpar)
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
    mrn = client_mrn()
    if not service.released(mrn):
        service.log_event('RTZ from not released service', client = mrn, eventNumber = 1, eventType = 6, eventDataType = 1)
        return 'We only talk with released services', 403

    if not check_acl(mrn):
        service.log_event('RTZ not allowed', client = mrn, eventNumber = 1, eventType = 6, eventDataType = 1)
        return 'Forbidden', 403

    vps = []
    fname = 'export/monitored.uvid'
    if os.path.isfile(fname):
        filterOK = True
        with open(fname) as f:
            data = json.loads(f.read())
            if 'route' in data:
                if not (uvid is None):
                    if uvid != getuvid(data['route']):
                        filterOK = False
        if not (routeStatus is None):
            if int(routeStatus) != 7:
                filterOK = False
        if filterOK:
            fname = 'export/' + data['route']
            with open(fname) as f:
                vp = VoyagePlan()
                vp.route = f.read()
                vps.append(vp)
    fname = 'export/alternate.uvid'
    if os.path.isfile(fname):
        filterOK = True
        with open(fname) as f:
            data = json.loads(f.read())
            if 'route' in data:
                if not (uvid is None):
                    if uvid != getuvid(data['route']):
                        filterOK = False
        if not (routeStatus is None):
            if int(routeStatus) == 7:
                filterOK = False
        if filterOK:
            fname = 'export/' + data['route']
            with open(fname) as f:
                vp = VoyagePlan()
                vp.route = f.read()
                vps.append(vp)
    evpar = 'uvid:' + str(uvid) + ' routeStatus:' + str(routeStatus)
    if len(vps) == 0:
        service.log_event('get_subscriptions', client=mrn, eventNumber = 1, eventType = 1, eventDataType = 1, eventParameters = evpar)
        return 'No voyage plans found', 404
    if os.path.exists('export/last_interaction_time'):
        with open('export/last_interaction_time', 'r') as f:
            timestamp = f.read()
    else:
        timestamp = datetime.utcnow().replace(microsecond=0).isoformat() + 'Z'
    service.log_event('get_subscriptions', client=mrn, eventNumber = 1, eventType = 1, eventDataType = 1, eventParameters = evpar)
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
    mrn = client_mrn()
    if not service.released(mrn):
        service.log_event('RTZ from not released service', client = mrn, eventNumber = 11, eventType = 6, eventDataType = 1)
        return 'We only talk with released services', 403

    if not check_acl(mrn):
        service.log_event('RTZ not allowed', client = mrn, eventNumber = 11, eventType = 6, eventDataType = 1)
        return 'Forbidden', 403

    fname = 'export/monitored.subs'
    if os.path.isfile(fname):
        with open(fname) as f:
            subs = json.loads(f.read())
            if mrn in subs:
                filterOK = True
                if not (uvid is None):
                    if uvid == getuvid('monitored.rtz'):
                        filterOK = False
                if filterOK:
                    rmsubsname = 'import/monitored.rmsubs'
                    data = []
                    if os.path.isfile(rmsubsname):
                        with open(rmsubsname) as g:
                            data = json.loads(g.read())
                    data.append(mrn)
                    with open(rmsubsname, 'w') as g:
                        g.write(json.dumps(data))

    fname = 'export/alternate.subs'
    if os.path.isfile(fname):
        with open(fname) as f:
            subs = json.loads(f.read())
            if mrn in subs:
                filterOK = True
                if not (uvid is None):
                    if uvid == getuvid('alternate.rtz'):
                        filterOK = False
                if filterOK:
                    rmsubsname = 'import/alternate.rmsubs'
                    data = []
                    if os.path.isfile(rmsubsname):
                        with open(rmsubsname) as g:
                            data = json.loads(g.read())
                    data.append(mrn)
                    with open(rmsubsname, 'w') as g:
                        g.write(json.dumps(data))

    evpar = 'uvid:' + str(uvid) + ' callbackEndpoint:' + str(callbackEndpoint)
    service.log_event('remove_subscription', client=mrn, callback=callbackEndpoint, uvid=uvid, eventNumber = 11, eventType = 1, eventDataType = 1, eventParameters = evpar)
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

    mrn = client_mrn()
    '''
    This section is for stand-alone unit testing only
    '''
    acl = []
    fname = 'export/all.acl'
    if os.path.isfile(fname):
        with open(fname) as f:
            acl = json.loads(f.read())
    if callbackEndpoint == 'allow':
        if not (mrn in acl):
            acl.append(mrn)
            with open(fname, 'w') as g:
                g.write(acl)
        return 'OK'
    elif callbackEndpoint == 'deny':
        if mrn in acl:
            acl.remove(mrn)
            with open(fname, 'w') as g:
                g.write(acl)
        return 'OK'
    elif callbackEndpoint == 'delete':
        if os.path.isfile(fname):
            os.remove(fname)
        return 'OK'

    if not service.released(mrn):
        service.log_event('RTZ from not released service', client = mrn, eventNumber = 9, eventType = 6, eventDataType = 1)
        return 'We only talk with released services', 403

    if not check_acl(mrn):
        service.log_event('RTZ not allowed', client = mrn, eventNumber = 9, eventType = 6, eventDataType = 1)
        return 'Forbidden', 403

    subs1 = []
    fname = 'export/monitored.subs'
    if os.path.isfile(fname):
        with open(fname) as f:
            subs1 = json.loads(f.read())
    filterOK = True
    if not (uvid is None):
        if os.path.isfile('export/monitored.rtz'):
            if uvid == getuvid('monitored.rtz'):
                filterOK = False
    if not mrn in subs1:
        subs1.append(mrn)
    with open(fname, 'w') as f:
        f.write(json.dumps(subs1))

    subs2 = []
    fname = 'export/alternate.subs'
    if os.path.isfile(fname):
        with open(fname) as f:
            subs2 = json.loads(f.read())
    filterOK = True
    if not (uvid is None):
        if os.path.isfile('export/alternate.rtz'):
            if uvid == getuvid('alternate.rtz'):
                filterOK = False
    if not mrn in subs2:
        subs2.append(mrn)
    with open(fname, 'w') as f:
        f.write(json.dumps(subs2))

    evpar = 'uvid:' + str(uvid) + ' callbackEndpoint:' + str(callbackEndpoint)
    if (len(subs1) == 0) and (len(subs2) == 0):
        service.log_event('subscribe', client=mrn, callback=callbackEndpoint, uvid=uvid, eventNumber = 9, eventType = 1, eventDataType = 1, eventParameters = evpar)
        return 'No voyage plans found', 404
    service.log_event('subscribe', client=mrn, callback=callbackEndpoint, uvid=uvid, eventNumber = 9, eventType = 1, eventDataType = 1, eventParameters = evpar)
    return 'OK'


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
    mrn = client_mrn()
    if not service.released(mrn):
        service.log_event('RTZ from not released service', client = mrn, eventNumber = 3, eventType = 6, eventDataType = 1)
        return 'We only talk with released services', 403

    evpar = 'deliveryAckEndPoint:' + str(deliveryAckEndPoint) + ' callbackEndpoint:' + str(callbackEndpoint)
    uvid='parse:from:rtz'
    f = open('import/' + uvid + '.rtz', 'wb')
    f.write(voyagePlan)
    f.close()
    f = open('import/' + uvid + '.rtz', 'r')
    vp = f.read()
    f.close()
    RE2_XML_ENCODING = re.compile("encoding='UTF-8'", re.IGNORECASE)
    vp2 = RE2_XML_ENCODING.sub("", vp, count=1)
    RE_XML_ENCODING = re.compile("encoding=\"UTF-8\"", re.IGNORECASE)
    rtz = io.StringIO()
    rtz.write(RE_XML_ENCODING.sub("", vp2, count=1))
    rtz.seek(0)
    doc = etree.parse(rtz)
    root = doc.getroot()
    result = True
    ret = ''
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
                    service.log_event('Error in RTZ schema', client = mrn, eventNumber = 3, eventType = 2, eventDataType = 1)
                    return ret, 400
            except:
                ret = 'Schema validation exception'
                result = False
            tag='{http://www.cirm.org/RTZ/1/1}'
        else:
            rtz.close()
            ret = 'Unsupported route format'
            service.log_event('Error in RTZ schema', client = mrn, eventNumber = 3, eventType = 2, eventDataType = 1)
            return ret, 400
    if result == False:
        rtz.close()
        service.log_event('Error in RTZ schema', client = mrn, eventNumber = 3, eventType = 2, eventDataType = 1)
        return ret, 400
    routeInfo = doc.find(tag + 'routeInfo')
    uvid = routeInfo.get('vesselVoyage')
    if uvid is None:
        service.log_event('Error in RTZ schema', client = mrn, eventNumber = 3, eventType = 2, eventDataType = 1)
        return 'Missing vesselVoyage', 404
    routeName = routeInfo.get('routeName')
    if routeName is None:
        service.log_event('Error in RTZ schema', client = mrn, eventNumber = 3, eventType = 2, eventDataType = 1)
        return 'Missing routeName', 404
    if not ('urn:mrn:stm:voyage:id' in uvid):
        service.log_event('Error in RTZ schema', client = mrn, eventNumber = 3, eventType = 2, eventDataType = 1)
        return 'Wrong vesselVoyage format', 400
    if tag == '{http://www.cirm.org/RTZ/1/1}':
        routeInfo = doc.find(tag + 'routeInfo')
        extensions = routeInfo.find(tag + 'extensions')
        if extensions is None:
            service.log_event('Error in RTZ schema', client = mrn, eventNumber = 3, eventType = 2, eventDataType = 1)
            return 'Missing routeInfo/extensions', 404
        extension = extensions.find(tag + 'extension')
        if extension is None:
            service.log_event('Error in RTZ schema', client = mrn, eventNumber = 3, eventType = 2, eventDataType = 1)
            return 'Missing routeInfo/extensions/extension', 404
        routeStatus = extension.get('routeStatusEnum')
        if routeStatus is None:
            service.log_event('Error in RTZ schema', client = mrn, eventNumber = 3, eventType = 2, eventDataType = 1)
            return 'Missing routeInfo/extensions/extension/routeStatusEnum', 404
    else:
        routeStatus = routeInfo.get('routeStatus')
    if not (routeStatus in '12345678'):
        service.log_event('Error in RTZ schema', client = mrn, eventNumber = 3, eventType = 2, eventDataType = 1)
        return 'Wrong routeStatus format', 400
    f = open('import/' + routeName + '.rtz', 'wb')
    f.write(voyagePlan)
    f.close()
    data = { 'uvid': uvid, 'route': routeName + '.rtz', 'routeStatus': routeStatus, 'from': mrn }
    f = open('import/' + uvid + '.uvid', 'w')
    f.write(json.dumps(data))
    f.close()
    servicetype, url, name = service.get_service_url(mrn)
    if deliveryAckEndPoint is not None:
        data = collections.OrderedDict()
        data['endpoint'] = deliveryAckEndPoint
        data['id'] = uvid
        data['fromName'] = name
        data['fromId'] = mrn
        data['time'] = datetime.utcnow().replace(microsecond=0).isoformat() + 'Z'
        if not service.conf is None:
            data['toId'] = service.conf['id']
            data['toName'] = service.conf['name']

        with open('import/' + uvid + '.ack', 'w') as f:
            f.write(json.dumps(data))
    service.log_event('received voyageplan', client=mrn, name=routeName, status = name, callback=callbackEndpoint, eventNumber = 3, eventType = 1, eventDataType = 1, eventParameters = evpar)
    return 'OK'

