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
import sys

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

def check_acl(uvid):
    """
    Check if client is authorized in the access list of the voyage
    """
    p = Path('export')
    acl = list(p.glob('**/all.acl'))
    if len(acl) > 0:
        with acl[0].open() as f: data = json.loads(f.read())
        f.close()
        if client_mrn() in data:
            return True

    if uvid is not None:
        acl = list(p.glob('**/' + uvid + '.acl'))
        if len(acl) > 0:
            with acl[0].open() as f: data = json.loads(f.read())
            f.close()
            if client_mrn() in data:
                return True
    return False


def get_subscription_to_voyage_plans(callbackEndpoint):
    """
    
    Retrieve a list of subcribed UVID for the callBackEndPoint and Organization
    :param callbackEndpoint: Callback expected. Base url of the vis instance as in the Service Registry. The callback response will be sended to the voyagePlans endPoint of the instance
    :type callbackEndpoint: str

    :rtype: List[GetSubscriptionResponse]
    """
    me = { 'uid': client_mrn(), 'url': callbackEndpoint}
    p = Path('export')
    subsl = [] 
    uvids = list(p.glob('**/*.subs'))
    if len(uvids) > 0:
        with uvids[0].open() as f: data = json.loads(f.read())
        f.close()
        if me in data:
            sr = GetSubscriptionResponse(str(uvids[0]))
            subsl.append(sr)
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
    p = Path('export')
    if uvid is None:
        uvids = list(p.glob('**/*.uvid'))
    else:
        uvids = list(p.glob('**/' + uvid + '.uvid'))
    if len(uvids) == 0:
        if uvid is None:
            return 'No voyage plans found', 404
        else:
            return 'Voyage plan ' + uvid + ' not found', 404
    if routeStatus is None:
        routeStatus = '7'
    vps = []
    for voyage in uvids:
        with voyage.open() as f: data = json.loads(f.read())
        if routeStatus == data['routeStatus']:
            if not check_acl(str(voyage).split('/')[1].split('.')[0]):
                return 'Forbidden', 403
            vp = VoyagePlan()
            f = open('export/' + data['route'], 'r')
            vp.route = f.read()
            f.close()
            vps.append(vp)
    if len(vps) == 0:
        return 'Voyage plan with routeStatus ' + routeStatus + ' not found', 404
    timestamp = '2017-02-15T10:35:00Z'
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
        if not check_acl(vp):
            return 'Forbidden', 403
        if not (me in data):
            data.append(me)
    else:
        data = [ me ]
    f = open('import/' + vp + '.rmsubs', 'w')
    f.write(json.dumps(data))
    f.close()

    """
    Now the vessel will get the request to remove a subscription. As we have no vessel we have to simulate it here.
    At this time we also remove the client from the acl.
    As there is no way to clean up garbage we re-use this method to delete old stuff as well.
    """
    os.remove('import/' + vp + '.rmsubs')
    p = Path('export')
    uvids = list(p.glob('**/*' + vp + '.subs'))
    data = []
    if len(uvids) > 0:
        with uvids[0].open() as f: data = json.loads(f.read())
        f.close()
        if me in data:
            data.remove(me)
    if len(data) == 0:
        os.remove('export/' + vp + '.subs')
    else:
        f = open('export/' + vp + '.subs', 'w')
        f.write(json.dumps(data))
        f.close()

    acls = list(p.glob('**/*' + vp + '.acl'))
    if len(acls) > 0:
        with acls[0].open() as f: data = json.loads(f.read())
        f.close()
        if meacl in data:
            data.remove(meacl)
        if len(data) == 0:
            os.remove('export/' + vp + '.acl')
        else:
            f = open('export/' + vp + '.acl', 'w')
            f.write(json.dumps(data))
            f.close()

    uvids = list(p.glob('**/*' + vp + '.uvid'))
    if len(uvids) > 0:
        os.remove('export/' + vp + '.uvid')
        os.remove('export/' + vp + '.rtz')

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
    me = { 'uid': client_mrn(), 'url': callbackEndpoint}
    meacl = client_mrn()
    p = Path('import')
    if uvid is None:
        vp = 'all'
    else:
        vp = uvid
        p2 = Path('export')
        uvids = list(p2.glob('**/' + uvid + '.uvid'))
        if len(uvids) == 0:
            return 'Voyage plan ' + uvid + ' not found', 404
        if not check_acl(uvid):
            return 'Forbidden', 403
    uvids = list(p.glob('**/*' + vp + '.subs'))
    if len(uvids) > 0:
        with uvids[0].open() as f: data = json.loads(f.read())
        f.close()
        if not (me in data):
            data.append(me)
    else:
        data = [ me ]
    f = open('import/' + vp + '.subs', 'w')
    f.write(json.dumps(data))
    f.close()

    """
    Now the vessel will get the request to subscribe. As we have no vessel we have to simulate it here.
    Also add the client_mrn to the access list.
    """
    f = open('export/' + vp + '.subs', 'w')
    f.write(json.dumps(data))
    f.close()
    os.remove('import/' + vp + '.subs')

    acls = list(p.glob('**/*' + vp + '.acl'))
    if len(acls) > 0:
        with acls[0].open() as f: data = json.loads(f.read())
        f.close()
        if not (meacl in data):
            data.append(meacl)
    else:
        data = [ meacl ]
    f = open('export/' + vp + '.acl', 'w')
    f.write(json.dumps(data))
    f.close()

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
    doc = etree.parse(rtz)
    root = doc.getroot()
    if root.tag == '{http://www.cirm.org/RTZ/1/0}route':
        if rtz10.xmlschema.validate(doc) == False:
            rtz.close()
            ret = rtz10.xmlschema.error_log
            return ret, 400
        tag='{http://www.cirm.org/RTZ/1/0}'
    else:
        if root.tag == '{http://www.cirm.org/RTZ/1/1}route':
            if rtz11.xmlschema.validate(doc) == False:
                rtz.close()
                ret = rtz11.xmlschema.error_log
                return ret, 400
            tag='{http://www.cirm.org/RTZ/1/1}'
        else:
            ret = 'Unsupported route format'
            return ret, 400
    routeInfo = doc.find(tag + 'routeInfo')
    uvid = routeInfo.get('vesselVoyage')
    if uvid is None:
        return 'Missing vesselVoyage', 404
    if not ('urn:mrn:stm:voyage:id' in uvid):
        return 'Wrong vesselVoyage format', 400
    routeStatus = routeInfo.get('routeStatus')
    if routeStatus is None:
        return 'Missing routeStatus', 404
    if not (routeStatus in '12345678'):
        return 'Wrong routeStatus format', 400
    f = open('import/' + uvid + '.rtz', 'wb')
    f.write(voyagePlan)
    f.close()
    data = { 'uvid': uvid, 'route': uvid + '.rtz', 'routeStatus': routeStatus }
    f = open('import/' + uvid + '.uvid', 'w')
    f.write(json.dumps(data))
    f.close()
    if deliveryAckEndPoint is not None:
        f = open('import/' + uvid + '.ack', 'w')
        f.write(deliveryAckEndPoint)
        f.close()

    """
    Now the vessel will need to process the uploaded voyagePlan and send an ack.
    """
    os.remove('import/' + uvid + '.rtz')
    f = open('export/' + uvid + '.rtz', 'wb')
    f.write(voyagePlan)
    f.close()
    vp = { 'uvid': uvid, 'route': uvid + '.rtz', 'routeStatus': routeStatus }
    f = open('export/' + uvid + '.uvid', 'w')
    f.write(json.dumps(vp))
    f.close()
    """
    if deliveryAckEndPoint is not None:
        os.remove('import/' + uvid + '.ack')
        send_ack(deliveryAckEndPoint)
    """
    return 'OK'

