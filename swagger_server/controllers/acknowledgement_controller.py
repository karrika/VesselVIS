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
    return 'Thank you for sending the acknowlegement'

