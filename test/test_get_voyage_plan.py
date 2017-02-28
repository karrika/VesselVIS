# coding: utf-8

"""
    STM Voyage Information Service SeaSWIM API

    Voyage Information Service API facing SeaSWIM through SSC exposing interfaces to SeaSWIM stakeholders

    OpenAPI spec version: 1.0.0
    Contact: per.lofbom@sjofartsverket.se
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest
import requests

import swagger_client
from swagger_client.rest import ApiException
from swagger_client.models.voyage_plan import VoyagePlan


class TestGetVoyagePlan(unittest.TestCase):
    """ Post VoyagePlan unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testGetVoyagePlan(self):
        """
        Test VoyagePlan
        """
        VIS_CERT='/home/karri/VesselVIS/Certificate_VIS-IMO8320767.pem'
        VIS_KEY='/home/karri/VesselVIS/PrivateKeye_VIS-IMO8320767.pem'
        endPoint='http://localhost:8002/8320767/voyagePlans'
        payload='{}'
        r=requests.get(endPoint, json=payload)
        #r=requests.post(endPoint, json=payload, cert=('/home/karri/VesselVIS/Certificate_VIS-IMO8320767.pem','/home/karri/VesselVIS/PrivateKey_VIS-IMO8320767.pem'))
        if r.status_code == 200:
            pass
        print(r.status_code, r.reason)


if __name__ == '__main__':
    unittest.main()
