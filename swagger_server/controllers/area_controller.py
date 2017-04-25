from swagger_server.models.delivery_ack import DeliveryAck
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
import time
import collections

def log_event(name ,areaname, ackendpoint = None):
    data = collections.OrderedDict()
    data['time'] = time.strftime("%Y-%m-%d %H:%M")
    data['client'] = client_mrn()
    data['event'] = name
    data['name'] = areaname
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

def upload_area(area, deliveryAckEndPoint=None):
    """
    
    Upload area message to VIS from other services i.e. Route Check service as an informational message
    :param area: Uploaded area message in S124 format to consumer
    :type area: str
    :param deliveryAckEndPoint: Acknowledgement expected. Base URL for VIS as in Service Registry. An ack is send back to this url when the private application retrieve the message from the VIS 
    :type deliveryAckEndPoint: str

    :rtype: None
    """
    areaname = client_mrn() + ':2'
    with open('import/' + areaname + '.S124', 'wb') as f:
        f.write(area)
    if deliveryAckEndPoint is not None:
        data = collections.OrderedDict()
        data['endpoint'] = deliveryAckEndPoint
        data['client'] = client_mrn()
        data['time'] = time.strftime("%Y-%m-%d %H:%M")
        with open('import/' + areaname + '.ack', 'w') as f:
            f.write(json.dumps(data))
    log_event('area', areaname, deliveryAckEndPoint)
    return 'OK'
