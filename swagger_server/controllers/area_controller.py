# coding: utf-8

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
import collections
from . import S124
import codecs

def log_event(name ,areaname, ackendpoint = None):
    data = collections.OrderedDict()
    data['time'] = datetime.utcnow().replace(microsecond=0).isoformat() + 'Z'
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
    with open('import/parse_area.txt', 'wb') as f:
        f.write(area)
    try:
        with codecs.open('import/parse_area.txt', 'r', encoding = 'utf-8') as f:
            areamsg = f.read()
    except ValueError:
        print('Not utf-8')
        try:
            with codecs.open('import/parse_area.txt', 'r', encoding = 'windows-1252') as f:
                areamsg = f.read()
        except ValueError:
            print('Not windows-1252 either')
            pass

    RE_XML_ENCODING = re.compile("encoding=\"UTF-8\"", re.IGNORECASE)
    areastr = io.StringIO()
    areastr.write(RE_XML_ENCODING.sub("", areamsg, count=1))
    areastr.seek(0)
    doc = etree.parse(areastr)
    root = doc.getroot()
    try:
        result = S124.xmlschema.validate(doc)
        if not result:
            areastr.close()
            ret = str(S124.xmlschema.error_log)
            return ret, 400
    except:
        result = False
    if not result:
        areastr.close()
        return ret, 400
    tag='{http://www.iho.int/S124/gml/1.0}'
    areaname = 'karri'
    if deliveryAckEndPoint is not None:
        data = collections.OrderedDict()
        data['endpoint'] = deliveryAckEndPoint
        data['id'] = areaname
        data['client'] = client_mrn()
        data['fromId'] = client_mrn()
        data['time'] = datetime.utcnow().replace(microsecond=0).isoformat() + 'Z'
        with open('import/' + areaname + '.ack', 'w') as f:
            f.write(json.dumps(data))
    log_event('area', areaname, deliveryAckEndPoint)
    return 'OK'
