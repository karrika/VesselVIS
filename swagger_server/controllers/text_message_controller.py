# coding: utf-8

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
from . import txt13
import codecs

def log_event(name, ackendpoint = None, textId = None, refId = None):
    data = collections.OrderedDict()
    data['time'] = datetime.utcnow().replace(microsecond=0).isoformat() + 'Z'
    data['client'] = client_mrn()
    data['event'] = name
    if not (ackendpoint is None):
        data['ack'] = ackendpoint
    if not (textId is None):
        data['id'] = textId
    if not (refId is None):
        data['refid'] = refId
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
    with open('import/parse.txt', 'wb') as f:
        f.write(textMessageObject)
    try:
        with codecs.open('import/parse.txt', 'r', encoding = 'utf-8') as f:
            txtmsg = f.read()
    except ValueError:
        print('Not utf-8')
        try:
            with codecs.open('import/parse.txt', 'r', encoding = 'windows-1252') as f:
                txtmsg = f.read()
        except ValueError:
            print('Not windows-1252 either')

    RE_XML_ENCODING = re.compile("encoding=\"UTF-8\"", re.IGNORECASE)
    txt = io.StringIO()
    txt.write(RE_XML_ENCODING.sub("", txtmsg, count=1))
    txt.seek(0)
    doc = etree.parse(txt)
    root = doc.getroot()
    if txt13.xmlschema.validate(doc) == False:
        txt.close()
        ret = txt13.xmlschema.error_log
        return ret, 400
    tag='{http://stmvalidation.eu/schemas/textMessageSchema_1_3.xsd}'
    messageId = root.find(tag + 'textMessageId').text
    referenceId = root.find(tag + 'informationObjectReferenceId').text
    with open('import/' + messageId + '.xml', 'w', encoding='utf-8') as f:
        f.write(txtmsg)
    if deliveryAckEndPoint is not None:
        data = collections.OrderedDict()
        data['endpoint'] = deliveryAckEndPoint
        data['textMessageId'] = 'placeholder'
        data['client'] = client_mrn()
        data['time'] = datetime.utcnow().replace(microsecond=0).isoformat() + 'Z'
        if not (referenceId is None):
            data['referenceId'] = referenceId
        with open('import/' + messageId + '.ack', 'w') as f:
            f.write(json.dumps(data))
    
    log_event('text', ackendpoint = deliveryAckEndPoint, textId = messageId, refId = referenceId)
    return 'OK'

