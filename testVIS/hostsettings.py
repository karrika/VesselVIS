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
callbackurl="https://localhost:8001"
voyageuvid='urn:mrn:stm:voyage:id:8320767:2017021010'
newvoyageuvid='urn:mrn:stm:voyage:id:new:plan'
newvoyageuvid2='urn:mrn:stm:voyage:id:new:plan2'
vis_uvid='urn:mrn:stm:service:instance:furuno:imo8320767'
vis1_uvid='urn:mrn:stm:service:instance:furuno:vis1'
vis2_uvid='urn:mrn:stm:service:instance:furuno:vis2'
vis3_uvid='urn:mrn:stm:service:instance:furuno:vis3'

def reportrow(sheet, row, col, state, reason):
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

def log_event(name, callback = None, uvid = None, routeStatus = None):
    data = { }
    if not (name is None):
        data['event'] = name
    if not (callback is None):
        data['callback'] = callback
    if not (uvid is None):
        data['uvid'] = uvid
    if not (routeStatus is None):
        data['routeStatus'] = routeStatus
    with open('event.log', 'a') as f:
        json.dump(data, f, ensure_ascii=True)
        f.write('\n')

def check_event(name, callback, uvid = None):
    with open('event.log', 'r') as f:
        log = f.readlines()
    length = len(log)
    if length > 0:
        data = json.loads(log[length-1])
        if data['event'] != name:
            return False
        if data['callback'] != callback:
            return False
        if not (uvid is None):
            if data['uvid'] != uvid:
                return False
        return True
    return False

def set_acl(id, uvid=None):
    if uvid is None: 
        f = open('export/all.acl', 'w')
    else:
        f = open('export/' + uvid + '.acl', 'w')
    data=[ id ]
    f.write(json.dumps(data))
    f.close()

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
    if uvid is None:
        if acl_exists(None):
            os.remove('export/all.acl') 
    else:
        if acl_exists(uvid):
            os.remove('export/' + uvid + '.acl') 

def acl_allowed(uvid):
    p = Path('export')
    all = list(p.glob('**/all.acl'))
    if len(all) > 0:
        with open('all[0]', 'r') as f:
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

def get_voyageplan(url, uvid = None, routeStatus = None):
    parameters = {
    }
    sub='/voyagePlans'
    if not (uvid is None):
        parameters['uvid'] = uvid
    if not (routeStatus is None):
        parameters['routeStatus'] = routeStatus
    log_event('get_voyage', uvid=uvid, routeStatus=routeStatus)
    return requests.get(url + sub, params=parameters, cert=vis_cert, verify=trustchain)

def subscribe_voyageplan(url, callback, uvid = None):
        sub='/voyagePlans/subscription'
        if uvid is None:
            parameters={
                'callbackEndpoint': callback
            }
            return requests.post(url + sub, params=parameters, cert=vis_cert, verify=trustchain)
        parameters={
            'callbackEndpoint': callback,
            'uvid': uvid
        }
        return requests.post(url + sub, params=parameters, cert=vis_cert, verify=trustchain)

def unsubscribe_voyageplan(url, callback, uvid = None):
        sub='/voyagePlans/subscription'
        if uvid is None:
            parameters={
                'callbackEndpoint': callback
            }
            return requests.delete(url + sub, params=parameters, cert=vis_cert, verify=trustchain)
        parameters={
            'callbackEndpoint': callback,
            'uvid': uvid
        }
        return requests.delete(url + sub, params=parameters, cert=vis_cert, verify=trustchain)

def post_voyageplan(url, voyageplan):
        sub='/voyagePlans'
        log_event('post_voyage', None)
        return requests.post(url + sub, data=voyageplan, cert=vis_cert, verify=trustchain)

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

def send_ack(endpoint):
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
    response=requests.post(endpoint + sub, json=payload, cert=vis_cert, verify=trustchain)

def vessel_connects():
    '''
    Check the possible new subsciptions and merge them with existing ones.
    '''
    p = Path('import')
    subs = list(p.glob('**/*.subs'))
    if len(subs) > 0:
        for sub in subs:
            with sub.open() as f:
                new_subs = json.loads(f.read())
                send_uvid_to = new_subs
            os.remove(str(sub))
            q = Path('export')
            q = q / sub.parts[1]
            if q.exists():
                with q.open() as f:
                    old_subs = json.loads(f.read())
                for subscriber in old_subs:
                    if not ( subscriber in new_subs ):
                        new_subs.append(subscriber)
            with open(str(q), 'w') as f:
                f.write(json.dumps(new_subs))
            for subscriber in send_uvid_to:
                '''
                Send monitored voyage to new subscribers
                '''
                upload_monitored(subscriber)
    '''
    Check the possible new subsciption removals and take care of them.
    '''
    p = Path('import')
    rmsubs = list(p.glob('**/*.rmsubs'))
    if len(rmsubs) > 0:
        for rmsub in rmsubs:
            with rmsub.open() as f:
                new_rmsubs = json.loads(f.read())
            os.remove(str(rmsub))
            sub = str(rmsub.parts[1]).split('.')[0] + '.subs'
            q = Path('export')
            q = q / sub
            if q.exists():
                with q.open() as f:
                    old_subs = json.loads(f.read())
                for subscriber in new_rmsubs:
                    if subscriber in old_subs:
                        old_subs.remove(subscriber)
                if len(old_subs) == 0:
                    os.remove(str(q))
                else:
                    with open(str(q), 'w') as f:
                        f.write(json.dumps(old_subs))
    '''
    Check for new voyage plans being uploaded and send ack if required.
    Also send the plans further if an active subscription exists.
    '''
    p = Path('import')
    uvids = list(p.glob('**/*.uvid'))
    for item in uvids:
        shutil.copyfile(str(item), 'export/' + item.parts[1])
        os.remove(str(item)) 
    rtzs = list(p.glob('**/*.rtz'))
    for item in rtzs:
        shutil.copyfile(str(item), 'export/' + item.parts[1])
        os.remove(str(item))
        
    '''
    Check for new areas being uploaded.
    '''
    p = Path('import')
    areas = list(p.glob('**/*.S124'))
    if len(areas) > 0:
        for area in areas:
            os.remove(str(area))
    '''
    Check for new text messages being uploaded.
    '''
    '''
    Check for ack requests.
    '''
    p = Path('import')
    acks = list(p.glob('**/*.ack'))
    if len(acks) > 0:
        for ack in acks:
            with open(str(ack)) as f:
                data = json.loads(f.read())
            os.remove(str(ack))
            send_ack(data['endpoint'])

