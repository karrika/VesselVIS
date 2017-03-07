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

CERTPATH=''
vis_cert=(CERTPATH + str(vis_cert[0]), CERTPATH + str(vis_key[0]))
trustchain=CERTPATH + str(vis_trust[0])

url="https://ec2-35-157-50-165.eu-central-1.compute.amazonaws.com"
url="http://localhost:8002"
callbackurl="http://localhost:8002"
voyageuvid='urn:mrn:stm:voyage:id:8320767'
newvoyageuvid='urn:mrn:stm:voyage:id:new:plan'
vis_uvid='urn:mrn:stm:service:instance:furuno:imo8320767'


