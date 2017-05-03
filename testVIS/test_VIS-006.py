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
from . import hostsettings
import logging

vis_cert=hostsettings.vis_cert
trustchain=hostsettings.trustchain

url=hostsettings.url
ackurl=hostsettings.callbackurl
callbackurl=hostsettings.callbackurl
voyageuvid='urn:mrn:stm:voyage:id:004:001'
vis2_uvid=hostsettings.vis2_uvid

textmessage='''<?xml version="1.0" encoding="utf-8"?>
<textMessage xmlns="http://tempuri.org/textMessageSchema.xsd">
  <textMessageId>urn:mrn:stm:txt:sma:20161222104700-1</textMessageId>
  <informationObjectReferenceId>urn:mrn:stm:voyage:id:sma:test-1</informationObjectReferenceId>
  <author>Mikael</author>
  <from>urn:mrn:stm:org:sma</from>
  <createdAt>2016-12-22T11:09:47</createdAt>
  <subject>Subject</subject>
  <body>Body</body>
</textMessage>
'''

class TestVIS_006(BaseTestCase):
    """ VIS-006 tests """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def vessel_connects(self):
        hostsettings.vessel_connects()
        pass

    def test_VIS_006_00(self):
        """
        VIS-006-0 - VIS-1:0 allow access

        
        """
        hostsettings.set_acl(vis2_uvid, None)
        pass

    def test_VIS_006_01(self):
        """
        VIS-006-1 - VIS-2: Select TXT message and send (upload) the TXT message to VIS-1

        
        """
        response=hostsettings.post_text(url, textmessage, ackurl)
        hostsettings.reportrow('VIS006sheet', 'VIS_006_01_row', 'VIS_006_01_col',
            response.status_code == 200, response.reason)
        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_006_02(self):
        """
        VIS-006-2 - STM Module receives the uplodaded txt message. VIS-1 sends ACK to VIS-2

        
        """
        logged = hostsettings.check_event('text')
        hostsettings.reportrow('VIS006sheet', 'VIS_006_02_row', 'VIS_006_02_col',
            logged, '')
        self.assertTrue(logged)

    def test_VIS_006_03(self):
        """
        VIS-006-3 - VIS-2 receives ACK. VIS-2 logs ACK event

        
        """
        logged = hostsettings.check_event('ack')
        hostsettings.reportrow('VIS006sheet', 'VIS_006_03_row', 'VIS_006_03_col',
            logged, '')
        self.assertTrue(logged)

    def test_VIS_006_1_1(self):
        """
        VIS-006-1-1 - In VIS-2, select TXT message and send (upload) to VIS-1 with ACKendpoint

        
        """
        response=hostsettings.post_text(url, textmessage, ackurl)
        hostsettings.reportrow('VIS006sheet', 'VIS_006_1_1_row', 'VIS_006_1_1_col',
            response.status_code == 200, response.reason)
        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_006_1_2(self):
        """
        VIS-006-1-2 - Retrieve/receive the uploaded message in private application of VIS-1

        
        """
        logged = hostsettings.check_event('text')
        hostsettings.reportrow('VIS006sheet', 'VIS_006_1_2_row', 'VIS_006_1_2_col',
            logged, '')
        self.assertTrue(logged)


    def test_VIS_006_2_1(self):
        """
        VIS-006-2-1 - In VIS-2, select TXT message and send (upload) to VIS-1 with ACKendpoint

        
        """
        response=hostsettings.post_text(url, textmessage, ackurl)
        hostsettings.reportrow('VIS006sheet', 'VIS_006_2_1_row', 'VIS_006_2_1_col',
            response.status_code == 200, response.reason)
        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_006_2_2(self):
        """
        VIS-006-2-2 - No private application retrieves/receives the message

        
        """
        logged = hostsettings.check_event('text')
        hostsettings.reportrow('VIS006sheet', 'VIS_006_2_2_row', 'VIS_006_2_2_col',
            logged, '')
        self.assertTrue(logged)

if __name__ == '__main__':
    unittest.main()


