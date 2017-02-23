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
    return 'do some magic!'


def get_voyage_plans(uvid=None, routeStatus=None):
    """
    get_voyage_plans
    Returns active VoyagePlans
    :param uvid: Unique identity (URN) of a voyageplan
    :type uvid: str
    :param routeStatus: Status of a route for a voyageplan: 1-Original   2-Planned_for_voyage    3-Optimized 4-Cross_Checked 5-Safety_Checked    6-Approved  7-Used_for_monitoring   8-Inactive
    :type routeStatus: str

    :rtype: GetVPResponseObject
    """
    return 'do some magic!'


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
    return 'do some magic!'


def subscribe_to_voyage_plan(callbackEndpoint, uvid=None):
    """
    subscribe_to_voyage_plan
    Request subscription for active Voyage Plan from other services i.e. Enhanced Monitoring
    :param callbackEndpoint: An endpoint (URI) specifying the address where the subscribed data is to be posted
    :type callbackEndpoint: str
    :param uvid: Unique identity (URN) of a voyageplan
    :type uvid: str

    :rtype: ResponseObj
    """
    return 'do some magic!'


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
    return 'do some magic!'


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
    return 'do some magic!'


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
    return 'do some magic!'
