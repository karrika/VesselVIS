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
voyageuvid='urn:mrn:stm:voyage:id:8320767'
newvoyageuvid='urn:mrn:stm:voyage:id:new:plan'
newvoyageuvid2='urn:mrn:stm:voyage:id:new:plan2'
vis_uvid='urn:mrn:stm:service:instance:furuno:imo8320767'

def set_acl(id, uvid=None):
    if uvid is None: 
        f = open('export/all.acl', 'w')
    else:
        f = open('export/' + voyageuvid + '.acl', 'w')
    data=[ id ]
    f.write(json.dumps(data))
    f.close()

