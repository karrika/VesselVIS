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


def acknowledgement(deliveryAck):
    """
    acknowledgement
    Endpoint for receipt of acknowledgements
    :param deliveryAck: Acknowledgement 
    :type deliveryAck: dict | bytes

    :rtype: ResponseObj
    """
    if connexion.request.is_json:
        deliveryAck = DeliveryAck.from_dict(connexion.request.get_json())
    return 'Hello World!'


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
            return 'No voyage plans found'
        else:
            return 'Voyage plan ' + uvid + ' not found'
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
    return ResponseObj()


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
    me = { 'uid': 'urn:mrn:me', 'url': callbackEndpoint}
    p = Path('import')
    if uvid is None:
        vp = 'all'
    else:
        vp = uvid
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
    Copy the requests directly to the export directory. All requests approved.
    """
    f = open('export/' + vp + '.subs', 'w')
    f.write(json.dumps(data))
    f.close()
    return ResponseObj()


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

