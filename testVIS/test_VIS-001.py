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

CERTPATH='/home/karri/VesselVIS/'
url="https://ec2-35-157-50-165.eu-central-1.compute.amazonaws.com"

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
        uvid='urn%3Amrn%3Astm%3Avoyage%3Aid%3Anot%3Afound'
        sub='/voyagePlans?uvid=' + uvid
        payload={}
        response=requests.get(url + sub, json=payload, cert=(CERTPATH + 'Certificate_VIS-Falstaff.pem', CERTPATH + 'PrivateKey_VIS-Falstaff.pem'), verify=CERTPATH + 'mc-ca-chain.pem')
        self.assert404(response, "Response body is : " + response.text)

    def test_VIS_001_2(self):
        """
        VIS-001-2 - VIS-2: Subscribe to voyage plan with chosen UVID from VIS-1

        
        """
        sub='/voyagePlans/subscription?callbackEndpoint=http%3A%2F%2Flocalhost%2FvoyagePlans&uvid=urn%3Amrn%3Astm%3Avoyage%3Aid%3Anot%3Afound'
        payload={}
        response=requests.post(url + sub, json=payload, cert=(CERTPATH + 'Certificate_VIS-Falstaff.pem', CERTPATH + 'PrivateKey_VIS-Falstaff.pem'), verify=CERTPATH + 'mc-ca-chain.pem')
        self.assert404(response, "Response body is : " + response.text)

    def test_VIS_001_3(self):
        """
        VIS-001-3 - Publish voyage plan to VIS-1 with chosen UVID

        
        """
        sub='/voyagePlans?uvid=urn%3Amrn%3Astm%3Avoyage%3Aid%3Anot%3Afound'
        payload={'route': '<route />'}
        response=requests.post(url + sub, json=payload, cert=(CERTPATH + 'Certificate_VIS-Falstaff.pem', CERTPATH + 'PrivateKey_VIS-Falstaff.pem'), verify=CERTPATH + 'mc-ca-chain.pem')
        self.assert200(response, "Response body is : " + response.text)


if __name__ == '__main__':
    unittest.main()


