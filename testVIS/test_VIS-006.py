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
from swagger_server import service
import logging

vis_cert=service.vis_cert
trustchain=service.trustchain

url=service.url
ackurl=service.callbackurl
callbackurl=service.callbackurl
voyageuvid='urn:mrn:stm:voyage:id:004:001'
vis2_uvid=service.vis2_uvid

textmessage='''<?xml version="1.0" encoding="utf-8"?>
<textMessage
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xmlns="http://stmvalidation.eu/schemas/textMessageSchema_1_3.xsd">
  <textMessageId>urn:mrn:stm:txt:sma:20170510104400-1</textMessageId>
  <informationObjectReferenceId>urn:mrn:stm:voyage:id:test:100</informationObjectReferenceId>
  <informationObjectReferenceType>RTZ</informationObjectReferenceType>
  <validityPeriodStart>2017-05-01T01:00:00Z</validityPeriodStart>
  <validityPeriodStop>2017-06-10T01:00:00Z</validityPeriodStop>
  <author>urn:mrn:stm:user:sma:mikolo</author>
  <from>urn:mrn:stm:org:sma</from>
  <serviceType>SHIP-VIS</serviceType>
  <createdAt>2017-05-10T01:00:00Z</createdAt>
  <subject>Test message</subject>
  <body>Test message Hanöbukten</body>
  <position lat="55.50668" lon="14.29825"/>
  <area>
    <Polygon>
      <posList>55.452 14.405 55.465 14.151 56.006 14.301 55.563 14.437 55.452 14.405</posList>
    </Polygon>
    <Circle>
      <position lat="55.50668" lon="14.29825"/>
      <radius>1</radius>
    </Circle>
  </area>
</textMessage>
'''

class TestVIS_006(BaseTestCase):
    """ VIS-006 tests """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_VIS_006_00(self):
        """
        VIS-006-0 - VIS-1:0 allow access

        
        """
        service.set_acl(vis2_uvid, None)
        pass

    def test_VIS_006_01(self):
        """
        VIS-006-1 - VIS-2: Select TXT message and send (upload) the TXT message to VIS-1

        
        """
        response=service.post_text(url, textmessage, ackurl)
        service.reportrow('VIS006sheet', 'VIS_006_01_row', 'VIS_006_01_col',
            response.status_code == 200, response.reason)
        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_006_02(self):
        """
        VIS-006-2 - STM Module receives the uplodaded txt message. VIS-1 sends ACK to VIS-2

        
        """
        logged = service.check_event('text')
        service.reportrow('VIS006sheet', 'VIS_006_02_row', 'VIS_006_02_col',
            logged, '')
        self.assertTrue(logged)

    def test_VIS_006_03(self):
        """
        VIS-006-3 - VIS-2 receives ACK. VIS-2 logs ACK event

        
        """
        logged = service.check_event('ack')
        service.reportrow('VIS006sheet', 'VIS_006_03_row', 'VIS_006_03_col',
            logged, '')
        self.assertTrue(logged)

    def test_VIS_006_1_1(self):
        """
        VIS-006-1-1 - In VIS-2, select TXT message and send (upload) to VIS-1 with ACKendpoint

        
        """
        response=service.post_text(url, textmessage, ackurl)
        service.reportrow('VIS006sheet', 'VIS_006_1_1_row', 'VIS_006_1_1_col',
            response.status_code == 200, response.reason)
        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_006_1_2(self):
        """
        VIS-006-1-2 - Retrieve/receive the uploaded message in private application of VIS-1

        
        """
        logged = service.check_event('text')
        service.reportrow('VIS006sheet', 'VIS_006_1_2_row', 'VIS_006_1_2_col',
            logged, '')
        self.assertTrue(logged)


    def test_VIS_006_2_1(self):
        """
        VIS-006-2-1 - In VIS-2, select TXT message and send (upload) to VIS-1 with ACKendpoint

        
        """
        response=service.post_text(url, textmessage, ackurl)
        service.reportrow('VIS006sheet', 'VIS_006_2_1_row', 'VIS_006_2_1_col',
            response.status_code == 200, response.reason)
        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_006_2_2(self):
        """
        VIS-006-2-2 - No private application retrieves/receives the message

        
        """
        logged = service.check_event('text')
        service.reportrow('VIS006sheet', 'VIS_006_2_2_row', 'VIS_006_2_2_col',
            logged, '')
        self.assertTrue(logged)

if __name__ == '__main__':
    unittest.main()


