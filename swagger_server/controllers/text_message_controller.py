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
    try:
        result = txt13.xmlschema.validate(doc)
        if not result:
            txt.close()
            ret = str(txt13.xmlschema.error_log)
            return ret, 400
    except:
        result = False
    if not result:
        txt.close()
        return ret, 400
    tag='{http://stmvalidation.eu/schemas/textMessageSchema_1_3.xsd}'
    messageId = root.find(tag + 'textMessageId')
    referenceId = root.find(tag + 'informationObjectReferenceId')
    subject = root.find(tag + 'subject')
    if subject is None:
        subj = ''
    else:
        subj = subject.text
    body = root.find(tag + 'body')
    if body is None:
        bod = ''
    else:
        bod = body.text
    position = root.find(tag + 'position')
    area = root.find(tag + 'area')
    if (area is None) and (position is None):
        graphics = False
    else:
        graphics = True
    uvid = messageId.text
    with open('import/' + uvid + '.xml', 'w', encoding='utf-8') as f:
        f.write(txtmsg)
    data = { 'uvid': uvid, 'msg': uvid + '.xml', 'from': client_mrn(), 'subject': subj, 'body': bod, 'graphics': graphics }
    with open('import/' + uvid + '.uvid', 'w') as f:
        f.write(json.dumps(data))
    servicetype, url, name = service.get_service_url(client_mrn())
    if deliveryAckEndPoint is not None:
        data = collections.OrderedDict()
        data['endpoint'] = deliveryAckEndPoint
        data['id'] = uvid
        data['fromName'] = name
        data['fromId'] = client_mrn()
        data['time'] = datetime.utcnow().replace(microsecond=0).isoformat() + 'Z'
        if not (referenceId is None):
            data['referenceId'] = referenceId.text
        if not service.conf is None:
            data['toId'] = service.conf['id']
            data['toName'] = service.conf['name']

        with open('import/' + messageId.text + '.ack', 'w') as f:
            f.write(json.dumps(data))
    
    service.log_event('received ' + subject.text, name=body.text, status = name)
    return 'OK'

