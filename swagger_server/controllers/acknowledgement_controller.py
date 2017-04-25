import connexion
from swagger_server.models.delivery_ack import DeliveryAck
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
import collections

def log_event(name):
    data = collections.OrderedDict()
    data['time'] = datetime.utcnow().replace(microsecond=0).isoformat() + 'Z'
    data['client'] = client_mrn()
    data['event'] = name
    with open('event.log', 'a') as f:
        json.dump(data, f, ensure_ascii=True)
        f.write('\n')

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

def acknowledgement(deliveryAck):
    """
    
    Endpoint for receipt of acknowledgement of uploaded message
    :param deliveryAck: Acknowledgement
    :type deliveryAck: dict | bytes

    :rtype: None
    """
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
    log_event('ack')
    return 'Thank you for sending the acknowlegement'

