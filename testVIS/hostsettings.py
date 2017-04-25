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

def log_event(name, callback, uvid = None):
    data = { }
    if not (client_mrn() is None):
        data['client'] = client_mrn()
    if not (name is None):
        data['event'] = name
    if not (callback is None):
        data['callback'] = callback
    if not (uvid is None):
        data['uvid'] = uvid
    with open('event.log', 'a') as f:
        json.dump(data, f, ensure_ascii=True)
        f.write('\n')

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
    Also send the plans further is an active subscription exists.
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
            response=requests.post(data['endpoint'] + sub, json=payload, cert=vis_cert, verify=trustchain)
