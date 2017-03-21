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
from . import rtzstm11
from . import rtzstm20

def client_mrn():
    """
    Placeholder for real client mrn service from certificate context
    print(connexion.request.getpeercert(True))
    """
    if not connexion.request.authorization:
        print('Not authorized')
    else:
        print('Great! Authorized')
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
    return 'do some magic!'

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
    with uvids[0].open() as f: data = json.loads(f.read())
    if routeStatus is not None:
        if routeStatus != data['routeStatus']:
            return 'Voyage plan with routeStatus' + routeStatus + ' not found', 404
    if not check_acl(str(uvids[0]).split('/')[1].split('.')[0]):
        return 'Forbidden', 403
    vp = VoyagePlan()
    f = open('export/' + data['route'], 'r')
    vp.route = f.read()
    f.close()
    vps = [ vp ]
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
    p = Path('import')
    if uvid is None:
        vp = 'all'
        ret.body = 'Generic remove subscription sent'
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
    """
    os.remove('import/' + vp + '.rmsubs')
    p = Path('export')
    uvids = list(p.glob('**/*' + vp + '.subs'))
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
    """
    f = open('export/' + vp + '.subs', 'w')
    f.write(json.dumps(data))
    f.close()
    os.remove('import/' + vp + '.subs')

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
    routeStatus = '1'
    RE_XML_ENCODING = re.compile("encoding=\"UTF-8\"", re.IGNORECASE)
    rtz = io.StringIO()
    rtz.write(RE_XML_ENCODING.sub("", voyagePlan, count=1))
    rtz.seek(0)
    doc = etree.parse(rtz)
    root = doc.getroot()
    if root.tag == '{http://www.cirm.org/RTZ/1/0}route':
        if rtz10.xmlschema.validate(doc) == False:
            rtz.close()
            ret.body = rtz10.xmlschema.error_log
            return ret, 400
    else:
        if root.tag == '{http://www.cirm.org/RTZ/1/1}route':
            if rtzstm11.xmlschema.validate(doc) == False:
                rtz.close()
                ret.body = rtzstm11.xmlschema.error_log
                return ret, 400
        else:
            if root.tag == '{http://www.cirm.org/RTZ/2/0}route':
                if rtzstm20.xmlschema.validate(doc) == False:
                    rtz.close()
                    ret.body = rtzstm20.xmlschema.error_log
                    return ret, 400
            else:
                ret.body = 'Unsupported route format'
                return ret, 400
    uvid='parse:from:rtz'
    data = { 'uvid': uvid, 'route': uvid + '.rtz', 'routeStatus': routeStatus }
    f = open('import/' + uvid + '.uvid', 'w')
    f.write(json.dumps(data))
    f.close()
    f = open('import/' + uvid + '.rtz', 'w')
    f.write(voyagePlan)
    f.close()
    if deliveryAckEndPoint is not None:
        f = open('import/' + uvid + '.ack', 'w')
        f.write(deliveryAckEndPoint)
        f.close()

    """
    Now the vessel will need to process the uploaded voyagePlan and send an ack.
    """
    os.remove('import/' + uvid + '.rtz')
    f = open('export/' + uvid + '.rtz', 'w')
    f.write(voyagePlan)
    f.close()
    vp = { 'uvid': uvid, 'route': uvid + '.rtz', 'routeStatus': '1' }
    f = open('export/' + uvid + '.uvid', 'w')
    f.write(json.dumps(vp))
    f.close()
    """
    if deliveryAckEndPoint is not None:
        os.remove('import/' + uvid + '.ack')
        send_ack(deliveryAckEndPoint)
    """

    return 'OK'

