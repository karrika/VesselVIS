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

CERTPATH='/home/karri/VesselVIS/'
vis_cert=(CERTPATH + 'Certificate_VIS-Falstaff.pem', CERTPATH + 'PrivateKey_VIS-Falstaff.pem')
trustchain=CERTPATH + 'mc-ca-chain.pem'

url="https://ec2-35-157-50-165.eu-central-1.compute.amazonaws.com"
url="http://localhost:8002"
callbackurl="http://localhost:8002"

voyageplan='\
<?xml version="1.0" encoding="UTF-8"?>\
<route version="1.0" xmlns="http://www.cirm.org/RTZ/1/0">\
    <routeInfo routeName="Test-Mini-1"/>\
        <waypoints>\
                <waypoint id="1">\
                        <position lat="53.5123" lon="8.11998"/>\
                </waypoint>\
                <waypoint id="15">\
                        <position lat="53.0492" lon="8.87731"/>\
                </waypoint>\
        </waypoints>\
</route>\
'

voyageuvid='urn:mrn:stm:voyage:id:8320767'
vis_uvid='urn:mrn:stm:service:instance:furuno:imo8320767'

class TestVIS_001(BaseTestCase):
    """ VIS-001 tests """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_VIS_001_1(self):
        """
        VIS-001-1 - VIS-2: Request (get) voyage plan with chosen UVID from VIS-1

        
        """
        sub='/voyagePlans'
        parameters={
            'uvid': 'urn:mrn:stm:voyage:id:not:found'
        }
        response=requests.get(url + sub, params=parameters, cert=vis_cert, verify=trustchain)
        self.assert403(response, "Response body is : " + response.text)

    def test_VIS_001_2(self):
        """
        VIS-001-2 - VIS-2: Subscribe to voyage plan with chosen UVID from VIS-1

        
        """
        sub='/voyagePlans/subscription'
        parameters={
            'callbackEndpoint': callbackurl + '/voyagePlans',
            'uvid': 'urn:mrn:stm:voyage:id:not:found'
        }
        payload={}
        response=requests.post(url + sub, params=parameters, json=payload, cert=vis_cert, verify=trustchain)
        self.assert403(response, "Response body is : " + response.text)

    def test_VIS_001_3(self):
        """
        VIS-001-3 - Publish voyage plan to VIS-1 with chosen UVID

        
        """
        sub='/voyagePlans'
        parameters={
            'uvid': 'urn:mrn:stm:voyage:id:new:plan'
        }
        payload={'route': voyageplan}
        response=requests.post(url + sub, params=parameters, json=payload, cert=vis_cert, verify=trustchain)
        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_001_4(self):
        """
        VIS-001-4 - VIS-2: Request voyage plan with chosen UVID from VIS-1

        
        """
        f = open('export/' + voyageuvid + '.acl', 'w')
        data=[ ]
        f.write(json.dumps(data))
        f.close()
        sub='/voyagePlans'
        parameters={
            'uvid': 'urn:mrn:stm:voyage:id:8320767'
        }
        response=requests.get(url + sub, params=parameters, cert=vis_cert, verify=trustchain)
        self.assert403(response, "Response body is : " + response.text)


if __name__ == '__main__':
    unittest.main()


