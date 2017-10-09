# coding: utf-8

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
                        print(field[4:])
                        return field[4:]
    return 'urn:mrn:stm:service:instance:furuno:vis2'

def acknowledgement(deliveryAck):
    """
    
    Endpoint for receipt of acknowledgement of uploaded message
    :param deliveryAck: Acknowledgement
    :type deliveryAck: dict | bytes

    :rtype: None
    if connexion.request.is_json:
        deliveryAck = DeliveryAck.from_dict(connexion.request.get_json())
    """
    with open('stm/ackmsg.txt', 'w') as f:
        f.write(json.dumps(deliveryAck))
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
    servicetype, url, name = service.get_service_url(client_mrn())
    id = ''
    if 'id' in deliveryAck:
        id = deliveryAck['id']
    ackResult = ''
    if 'ackResult' in deliveryAck:
        ackResult = deliveryAck['ackResult']
    service.log_event('received ack ' + id, name=ackResult, status = name)
    return 'Thank you for sending the acknowlegement'

