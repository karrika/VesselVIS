import connexion
from swagger_server.models.delivery_ack import DeliveryAck
from swagger_server.models.error_model import ErrorModel
from swagger_server.models.get_vp_response_object import GetVPResponseObject
from swagger_server.models.response_obj import ResponseObj
from swagger_server.models.s124_data_set import S124DataSet
from swagger_server.models.text_message_object import TextMessageObject
from swagger_server.models.voyage_plan import VoyagePlan
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime
import json
from pathlib import Path
import os


def acknowledgement(deliveryAck):
    """
    acknowledgement
    Endpoint for receipt of acknowledgements
    :param deliveryAck: Acknowledgement 
    :type deliveryAck: dict | bytes

    :rtype: ResponseObj
    """
    ret = ResponseObj()
    if connexion.request.is_json:
        deliveryAck = DeliveryAck.from_dict(connexion.request.get_json())
    """
    So, what an earth am I going to do about acknowledgements?
        self.swagger_types = {
            'id': str,
            'reference_id': str,
            'time_of_delivery': datetime,
            'from_id': str,
            'from_name': str,
            'to_id': str,
            'to_name': str,
            'ack_result': str
        }
    """
    ret.body = 'Thank you for sending the acknowlegement'
    return ret


def get_voyage_plans(uvid=None, routeStatus=None):
    """
    get_voyage_plans
    Returns active VoyagePlans found in the ./export directory.
    This is the directory containing data coming from the vessel.
    :param uvid: Unique identity (URN) of a voyageplan
    :type uvid: str
    :param routeStatus: Status of a route for a voyageplan: 1-Original   2-Planned_for_voyage    3-Optimized 4-Cross_Checked 5-Safety_Checked    6-Approved  7-Used_for_monitoring   8-Inactive
    :type routeStatus: str

    :rtype: GetVPResponseObject
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
    f.close()
    ret = GetVPResponseObject()
    vp = VoyagePlan()
    f = open('export/' + data['route'], 'r')
    vp.route = f.read()
    f.close()
    vps = [ vp ]
    ret.voyage_plan = vps
    return ret


def remove_voyage_plan_subscription(callbackEndpoint, uvid=None):
    """
    remove_voyage_plan_subscription
    Remove subscription for active Voyage Plan from other services i.e. Enhanced Monitoring
    :param callbackEndpoint: An endpoint (URI) specifying the address where the subscribed data is to be posted
    :type callbackEndpoint: str
    :param uvid: Unique identity (URN) of a voyageplan
    :type uvid: str

    :rtype: ResponseObj
    """
    ret = ResponseObj()
    me = { 'uid': 'urn:mrn:me', 'url': callbackEndpoint}
    p = Path('import')
    if uvid is None:
        vp = 'all'
        ret.body = 'Generic remove subscription sent'
    else:
        vp = uvid
        ret.body = 'Remove subscription for ' + uvid + ' sent'
    uvids = list(p.glob('**/*' + vp + '.rmsubs'))
    if len(uvids) > 0:
        with uvids[0].open() as f: data = json.loads(f.read())
        f.close()
        if me in data:
            ret.body = 'Remove subscription already sent'
        else:
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
    return ret


def subscribe_to_voyage_plan(callbackEndpoint, uvid=None):
    """
    subscribe_to_voyage_plan
    Request subscription for active Voyage Plan from other services i.e. Enhanced Monitoring
    The subscription goes to the import directory. It will be sent to the vessel for acceptancce.
    As we have no vessel out there the code will accept the sender automatically.
    :param callbackEndpoint: An endpoint (URI) specifying the address where the subscribed data is to be posted
    :type callbackEndpoint: str
    :param uvid: Unique identity (URN) of a voyageplan
    :type uvid: str

    :rtype: ResponseObj
    """
    ret = ResponseObj()
    me = { 'uid': 'urn:mrn:me', 'url': callbackEndpoint}
    p = Path('import')
    if uvid is None:
        vp = 'all'
        ret.body = 'Generic subscription sent'
    else:
        vp = uvid
        ret.body = 'Subscription for ' + uvid + ' sent'
    uvids = list(p.glob('**/*' + vp + '.subs'))
    if len(uvids) > 0:
        with uvids[0].open() as f: data = json.loads(f.read())
        f.close()
        if me in data:
            print('Already subscribed')
        else:
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
    return ret


def upload_area(area, deliveryAckEndPoint=None):
    """
    upload_area
    Upload area message to VIS from other services i.e. Route Check service as an informational message
    :param area: Area message to add to VIS message db for delivery to STM Onboard system as additional information
    :type area: dict | bytes
    :param deliveryAckEndPoint: Acknowledgement required, optionally an URL could be provided to send acknowledgment.
    :type deliveryAckEndPoint: str

    :rtype: ResponseObj
    """
    if connexion.request.is_json:
        area = S124DataSet.from_dict(connexion.request.get_json())
    return ResponseObj()


def upload_text_message(textMessageObject, deliveryAckEndPoint=None):
    """
    upload_text_message
    Upload text message to VIS from other services i.e. Route Optimization service.
    :param textMessageObject: Text message to add to VIS message db for delivery to STM Onboard system
    :type textMessageObject: dict | bytes
    :param deliveryAckEndPoint: Acknowledgement required, optionally an URL could be provided to send acknowledgment.
    :type deliveryAckEndPoint: str

    :rtype: ResponseObj
    """
    if connexion.request.is_json:
        textMessageObject = TextMessageObject.from_dict(connexion.request.get_json())
    return '-- MAGIC--'


def upload_voyage_plan(uvid, voyagePlan, deliveryAckEndPoint=None):
    """
    upload_voyage_plan
    Upload VoyagePlan to VIS from other services i.e. Route Optimization service.
    :param uvid: UVID of VoyagePlan to upload.
    :type uvid: str
    :param voyagePlan: Voyage Plan to add to VIS message db
    :type voyagePlan: dict | bytes
    :param deliveryAckEndPoint: Acknowledgement required, optionally an URL could be provided to send acknowledgment.
    :type deliveryAckEndPoint: str

    :rtype: ResponseObj
    """
    if connexion.request.is_json:
        voyagePlan = VoyagePlan.from_dict(connexion.request.get_json())
    return '-- MAGIC--'

