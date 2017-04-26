import connexion
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from swagger_server.util import deserialize_date, deserialize_datetime
import json
from pathlib import Path
import os
import requests
from lxml import etree
import io
import re
import collections

def log_event(name, ackendpoint = None):
    data = collections.OrderedDict()
    data['time'] = datetime.utcnow().replace(microsecond=0).isoformat() + 'Z'
    data['client'] = client_mrn()
    data['event'] = name
    if not (ackendpoint is None):
        data['ack'] = ackendpoint
    with open('event.log', 'a') as f:
        json.dump(data, f, ensure_ascii=True)
        f.write('\n')

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

def upload_text_message(textMessageObject, deliveryAckEndPoint=None):
    """
    
    Upload text message to VIS from other services i.e. Route Optimization service.
    :param textMessageObject: Uploaded Text message to consumer
    :type textMessageObject: str
    :param deliveryAckEndPoint: Acknowledgement expected. Base URL for VIS as in Service Registry. An ack is send back to this url when the private application retrieve the message from the VIS 
    :type deliveryAckEndPoint: str

    :rtype: None
    """
    with open('import/' + client_mrn() + ':1' + '.txt', 'wb') as f:
        f.write(textMessageObject)
    if deliveryAckEndPoint is not None:
        with open('import/' + client_mrn() + ':1' + '.ack', 'w') as f:
            f.write(deliveryAckEndPoint)
    log_event('txt', deliveryAckEndPoint)
    return 'OK'

