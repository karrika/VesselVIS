import connexion
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


def upload_text_message(textMessageObject, deliveryAckEndPoint=None):
    """
    
    Upload text message to VIS from other services i.e. Route Optimization service.
    :param textMessageObject: Uploaded Text message to consumer
    :type textMessageObject: str
    :param deliveryAckEndPoint: Acknowledgement expected. Base URL for VIS as in Service Registry. An ack is send back to this url when the private application retrieve the message from the VIS 
    :type deliveryAckEndPoint: str

    :rtype: None
    """
    f = open('import/' + client_mrn() + ':1' + '.txt', 'w')
    f.write(textMessageObject)
    f.close()
    if deliveryAckEndPoint is not None:
        f = open('import/' + client_mrn() + ':1' + '.ack', 'w')
        f.write(deliveryAckEndPoint)
        f.close()
    return 'OK'
