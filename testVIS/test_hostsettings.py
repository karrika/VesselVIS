# coding: utf-8

"""
    STM Voyage Information Service SeaSWIM Test cases
"""

from __future__ import absolute_import

import os
import sys
import unittest
from . import BaseTestCase
import swagger_client
from swagger_client.rest import ApiException
import requests
import shutil
import sys
import json
from pathlib import Path
import requests
from swagger_server.models.delivery_ack import DeliveryAck
import collections
from datetime import datetime


p = Path('.')
vis_cert = list(p.glob('**/Certificate_VIS*.pem'))
if len(vis_cert) == 0:
    print('Error: no Certificate_VIS*.pem found')
vis_key = list(p.glob('**/PrivateKey_VIS*.pem'))
if len(vis_key) == 0:
    print('Error: no PrivateKey_VIS*.pem found')
vis_trust = list(p.glob('**/mc-ca-chain.pem'))
if len(vis_trust) == 0:
    print('Error: no mc-ca-chain.pem found')

vis_cert=(str(vis_cert[0]), str(vis_key[0]))
trustchain=str(vis_trust[0])

url="https://localhost:8001"
callbackurl="https://localhost:8002"
voyageuvid='urn:mrn:stm:voyage:id:8320767:2017021010'
newvoyageuvid='urn:mrn:stm:voyage:id:new:plan'
newvoyageuvid2='urn:mrn:stm:voyage:id:new:plan2'
vis1_uvid='urn:mrn:stm:service:instance:furuno:vis1'
vis2_uvid='urn:mrn:stm:service:instance:furuno:vis2'
vis3_uvid='urn:mrn:stm:service:instance:furuno:vis3'

def reportrow(sheet, row, col, state = True, reason = ''):
    if state:
        report=sheet + '.write(' + row + ', ' + col + ''', "PASS", boldcenter)
''' + sheet + '.write(' + row + ', ' + col + ' - 1, "' + reason + '''", normal)
'''
    else:
        report=sheet + '.write(' + row + ', ' + col + ''', "FAIL", boldcenter)
''' + sheet + '.write(' + row + ', ' + col + ' - 1, "' + reason + '''", normal)
'''
    with open('../create_worksheet.py', 'a') as f:
        f.write(report)

def log_event(name, callback = None, uvid = None, routeStatus = None, ack = None):
    data = { }
    if not (name is None):
        data['event'] = name
    if not (ack is None):
        data['ack'] = ack
    if not (callback is None):
        data['callback'] = callback
    if not (uvid is None):
        data['uvid'] = uvid
    if not (routeStatus is None):
        data['routeStatus'] = routeStatus
    with open('event.log', 'a') as f:
        json.dump(data, f, ensure_ascii=True)
        f.write('\n')

def check_event(name, callback = None, uvid = None):
    for log in open('event.log', 'r'):
        match = True
        length = len(log)
        if length > 0:
            data = json.loads(log)
            if ('event' in data) and (data['event'] != name):
                match = False
            if not (callback is None):
                if ('callback' in data) and (data['callback'] != callback):
                    match = False
            if not (uvid is None):
                if ('uvid' in data) and (data['uvid'] != uvid):
                    match = False
            if match:
                return True
    return False

def islocal():
    return (vis2_uvid == 'urn:mrn:stm:service:instance:furuno:vis2')

def set_acl(id, uvid=None):
    if islocal():
        if uvid is None: 
            f = open('export/all.acl', 'w')
        else:
            f = open('export/' + uvid + '.acl', 'w')
        data=[ id ]
        f.write(json.dumps(data))
        f.close()
    else:
        if uvid is None: 
            response=subscribe_voyageplan(url, 'allow')
        else:
            response=subscribe_voyageplan(url, 'allow', uvid)

def uvid_exists(uvid):
    p = Path('export')
    uvids = list(p.glob('**/' + uvid + '.uvid'))
    return len(uvids) > 0

def rtz_exists(uvid):
    p = Path('export')
    uvids = list(p.glob('**/' + uvid + '.rtz'))
    return len(uvids) > 0

def subs_exists(uvid):
    p = Path('export')
    if uvid is None:
        uvids = list(p.glob('**/all.subs'))
    else:
        uvids = list(p.glob('**/' + uvid + '.subs'))
    return len(uvids) > 0

def acl_exists(uvid):
    p = Path('export')
    if uvid is None:
        uvids = list(p.glob('**/all.acl'))
    else:
        uvids = list(p.glob('**/' + uvid + '.acl'))
    return len(uvids) > 0

def rm_acl(id, uvid=None):
    if islocal():
        if uvid is None:
            if acl_exists(None):
                os.remove('export/all.acl') 
        else:
            if acl_exists(uvid):
                os.remove('export/' + uvid + '.acl') 
    else:
        if uvid is None: 
            response=subscribe_voyageplan(url, 'deny')
        else:
            response=subscribe_voyageplan(url, 'deny', uvid)

def acl_allowed(uvid):
    p = Path('export')
    all = list(p.glob('**/all.acl'))
    if len(all) > 0:
        with open(str(all[0]), 'r') as f:
            data = json.loads(f.read())
        if uvid in data:
            return True
    return False

def rm_subs(id, uvid=None):
    if uvid is None:
        if subs_exists(None):
            os.remove('export/all.subs') 
    else:
        if subs_exists(uvid):
            os.remove('export/' + uvid + '.subs') 

def rm_uvid(uvid):
    if islocal():
        if uvid is None:
            if subs_exists(None):
                os.remove('export/all.subs') 
            if acl_exists(uvid):
                os.remove('export/all.acl') 
        else:
            if uvid_exists(uvid):
                os.remove('export/' + uvid + '.uvid') 
            if rtz_exists(uvid):
                os.remove('export/' + uvid + '.rtz') 
            if subs_exists(uvid):
                os.remove('export/' + uvid + '.subs') 
            if acl_exists(uvid):
                os.remove('export/' + uvid + '.acl') 
    else:
        response=subscribe_voyageplan(url, 'delete', uvid)

def get_voyageplan(url, uvid = None, routeStatus = None):
    sub='/voyagePlans'
    headers = {
        'Content-Type': 'application/json'
    }
    parameters = {
    }
    if not (uvid is None):
        parameters['uvid'] = uvid
    if not (routeStatus is None):
        parameters['routeStatus'] = routeStatus
    log_event('get_voyage', uvid=uvid, routeStatus=routeStatus)
    return requests.get(url + sub, params=parameters, headers=headers, cert=vis_cert, verify=trustchain)

def subscribe_voyageplan(url, callback, uvid = None):
    sub='/voyagePlans/subscription'
    headers = {
        'Content-Type': 'application/json'
    }
    if uvid is None:
        parameters={
            'callbackEndpoint': callback
        }
        log_event('post_subscription', callback = callback)
        return requests.post(url + sub, params=parameters, headers=headers, cert=vis_cert, verify=trustchain)
    parameters={
        'callbackEndpoint': callback,
        'uvid': uvid
    }
    log_event('post_subscription', callback = callback, uvid = uvid)
    return requests.post(url + sub, params=parameters, headers=headers, cert=vis_cert, verify=trustchain)

def unsubscribe_voyageplan(url, callback, uvid = None):
    sub='/voyagePlans/subscription'
    headers = {
        'Content-Type': 'application/json'
    }
    if uvid is None:
        parameters={
            'callbackEndpoint': callback
        }
        return requests.delete(url + sub, params=parameters, headers=headers, cert=vis_cert, verify=trustchain)
    parameters={
        'callbackEndpoint': callback,
        'uvid': uvid
    }
    return requests.delete(url + sub, params=parameters, headers=headers, cert=vis_cert, verify=trustchain)

def post_voyageplan(url, voyageplan, deliveryAckEndPoint = None, callbackEndpoint = None):
    parameters = {
    }
    if not (deliveryAckEndPoint is None):
        parameters['deliveryAckEndPoint'] = deliveryAckEndPoint
    if not (callbackEndpoint is None):
        parameters['callbackEndpoint'] = callbackEndpoint
    sub='/voyagePlans'
    log_event('post_voyage', None)
    return requests.post(url + sub, data=voyageplan, params = parameters, cert=vis_cert, verify=trustchain)

def post_area(url, area, deliveryAckEndPoint = None):
    sub='/area'
    parameters = {
    }
    if not (deliveryAckEndPoint is None):
        parameters['deliveryAckEndPoint'] = deliveryAckEndPoint
    log_event('post_area', None)
    return requests.post(url + sub, data=area, cert=vis_cert, verify=trustchain)

def post_text(url, text, deliveryAckEndPoint = None):
    sub='/textMessage'
    parameters = {
    }
    if not (deliveryAckEndPoint is None):
        parameters['deliveryAckEndPoint'] = deliveryAckEndPoint
        log_event('post_text', ack=deliveryAckEndPoint)
    else:
        log_event('post_text', None)
    headers = {
        'Content-Type' : 'charset=utf-8'
    }
    return requests.post(url + sub, data=text, params=parameters, headers=headers, cert=vis_cert, verify=trustchain)

def upload_monitored(subscriber):
    '''
    Upload monitored route to subscriber
    '''
    p = Path('export')
    uvids = list(p.glob('**/*.uvid'))
    for uvid in uvids:
        with open(str(uvid), 'r') as f:
            data = json.loads(f.read())
        if data['routeStatus'] == '7':
            '''
            Send this uvid to subscriber
            '''
            rtzs = list(p.glob('**/' + str(data['route'])))
            for rtz in rtzs:
                with rtz.open() as f:
                    route = f.read()
                post_voyageplan(subscriber, route)

def post_ack(data):
    payload = collections.OrderedDict()
    
    if 'textMessageId' in data:
        payload['id'] = data['textMessageId']
    else:
        payload['id'] = 'urn:mrn:stm:id:missing'
    if 'referenceId' in data:
        payload['referenceId'] = data['referenceId']
    else:
        payload['referenceId'] = 'urn:mrn:stm:referenceid:missing'
    if 'timeOfDelivery' in data:
        payload['timeOfDelivery'] = data['timeOfDelivery']
    else:
        payload['timeOfDelivery'] = datetime.utcnow().replace(microsecond=0).isoformat() + 'Z'
    if 'fromId' in data:
        payload['fromId'] = data['fromId']
    else:
        payload['fromId'] = 'urn:mrn:stm:fromid:missing'
    if 'fromName' in data:
        payload['fromName'] = data['fromName']
    else:
        payload['fromName'] = 'Unknown sender'
    if 'toId' in data:
        payload['toId'] = data['toId']
    else:
        payload['toId'] = 'urn:mrn:stm:toid:missing'
    if 'toName' in data:
        payload['toName'] = data['toName']
    else:
        payload['toName'] = 'Unknown receiver'
    if 'ackResult' in data:
        payload['ackResult'] = data['ackResult']
    else:
        payload['ackResult'] = 'OK'
    if 'endpoint' in data:
        url = data['endpoint']
        sub='/acknowledgement'
        print(payload)
        print(url + sub)
        return requests.post(url + sub, json=payload, cert=vis_cert, verify=trustchain)

def send_ack(endpoint, id = 'urn:mrn:'):
    payload = collections.OrderedDict()
    payload['id'] = 'urn:mrn:'
    payload['referenceId'] = 'urn:mrn:'
    payload['timeOfDelivery'] = datetime.utcnow().replace(microsecond=0).isoformat() + 'Z'
    payload['fromId'] = 'urn:mrn:'
    payload['fromName'] = 'Who cares'
    payload['toId'] = 'urn:mrn:'
    payload['toName'] = 'Who cares'
    payload['ackResult'] = 'Who cares'
    sub='/acknowledgement'
    return requests.post(endpoint + sub, json=payload, cert=vis_cert, verify=trustchain)

def send_ack(endpoint, id = 'urn:mrn:'):
    payload = collections.OrderedDict()
    payload['id'] = 'urn:mrn:'
    payload['referenceId'] = 'urn:mrn:'
    payload['timeOfDelivery'] = datetime.utcnow().replace(microsecond=0).isoformat() + 'Z'
    payload['fromId'] = 'urn:mrn:'
    payload['fromName'] = 'Who cares'
    payload['toId'] = 'urn:mrn:'
    payload['toName'] = 'Who cares'
    payload['ackResult'] = 'Who cares'
    sub='/acknowledgement'
    return requests.post(endpoint + sub, json=payload, cert=vis_cert, verify=trustchain)

def read_accesstoken():
    with open('accesstoken', 'r') as f:
        ACCESSTOKEN = f.read()
    return ACCESSTOKEN

def search(query):
    url="https://sr-test.maritimecloud.net"
    sub='/api/_search/serviceInstance'
    ACCESSTOKEN = read_accesstoken()
    headers={
        'Authorization' : 'Bearer ' + ACCESSTOKEN[0:len(ACCESSTOKEN)-1],
        'Accept' : 'application/json'
    }
    parameters={
        'query' : query
    }
    return requests.get(url + sub, headers=headers, params=parameters, cert=vis_cert)

def sendpcm(body):
    url="https://sandbox-2.portcdm.eu:8443"
    sub='/amss/state_update'
    headers={
        'Content-Type' : 'application/xml'
    }
    return requests.post(url + sub, headers=headers, data=body, cert=vis_cert, verify=trustchain)

