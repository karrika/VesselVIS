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
            f = open(str(q), 'w')
            f.write(json.dumps(new_subs))
            f.close()
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
                    f = open(str(q), 'w')
                    f.write(json.dumps(old_subs))
                    f.close()
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
    Check for new areas being uploaded and send ack if required.
    '''
    '''
    Check for new text messages being uploaded and send ack if required.
    '''

