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
callbackurl=hostsettings.callbackurl
voyageuvid='urn:mrn:stm:voyage:id:004:001'
vis2_uvid=hostsettings.vis2_uvid

voyageplan='''<?xml version="1.0" encoding="UTF-8"?>
<route version="1.1" 
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xmlns:stm="http://stmvalidation.eu/STM/1/0/0"
  xsi:schemaLocation="http://stmvalidation.eu/STM/1/0/0 stm_extensions.xsd"
  xmlns="http://www.cirm.org/RTZ/1/1">
  <routeInfo vesselVoyage="urn:mrn:stm:voyage:id:004:001" routeName="HAN-VIS" validityPeriodStart="2017-02-15T10:00:00Z" validityPeriodStop="2017-02-16T10:00:00Z" optimizationMethod="Time table">
    <extensions>
      <extension xsi:type="stm:RouteInfoExtension"
        manufacturer="STM" name="routeInfoEx" version="1.0.0"
        routeStatusEnum="7"
        depPort="FIHAN"
        arrPort="SEVIS"
        depPortCallId="urn:mrn:stm:portcdm:port_call:FIHAN:20170421"
        arrPortCallId="urn:mrn:stm:portcdm:port_call:SEVIS:20170421"
        startSeaPassage="PILOT_BOARDING_AREA:WP1"
        endSeaPassage="PILOT_BOARDING_AREA:WP2">
        <stm:routeChanges>
            <stm:historyItem dateTime="2016-10-20T11:14:41Z" author="1st mate"
              reason="initial creation"/>
        </stm:routeChanges>
      </extension>
    </extensions>
  </routeInfo>
  <waypoints>
    <waypoint id="1" name="Hango" radius="0.800000">
      <position lat="59.811700" lon="22.935567"/>
    </waypoint>
    <waypoint id="2" radius="0.800000">
      <position lat="59.758817" lon="23.020267"/>
      <leg portsideXTD="0.099892" starboardXTD="0.099892" safetyContour="30" geometryType="Loxodrome" speedMax="7.000000" draughtForward="10.000000" draughtAft="10.000000" staticUKC="30.000000"/>
    </waypoint>
  </waypoints>
  <schedules>
    <schedule id="1">
      <calculated>
        <scheduleElement etd="2017-02-15T10:00:00Z" waypointId="1"/>
        <scheduleElement eta="2017-02-15T10:35:00Z" waypointId="2" speed="7.000000"/>
      </calculated>
    </schedule>
  </schedules>
</route>
'''

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
        sub='/voyagePlans/subscription'
        parameters={
            'callbackEndpoint': callbackurl
        }
        payload={}
        response=requests.post(url + sub, params=parameters, json=payload, cert=vis_cert, verify=trustchain)

        if response.status_code == 200:
            report='''
VIS006sheet.write(VIS_006_01_row, VIS_006_01_col, "PASS", boldcenter)
VIS006sheet.write(VIS_006_01_row, VIS_006_01_col - 1, "''' + response.reason + '", normal)'
        else:
            report='''
VIS006sheet.write(VIS_006_01_row, VIS_006_01_col, "FAIL", boldcenter)
VIS006sheet.write(VIS_006_01_row, VIS_006_01_col - 1, "''' + response.reason + '", normal)'
        f = open('../create_worksheet.py', 'a')
        f.write(report)
        f.close()

        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_006_02(self):
        """
        VIS-006-2 - STM Module receives the uplodaded txt message. VIS-1 sends ACK to VIS-2

        
        """
        sub='/voyagePlans/subscription'
        parameters={
            'callbackEndpoint': callbackurl
        }
        payload={}
        response=requests.post(url + sub, params=parameters, json=payload, cert=vis_cert, verify=trustchain)

        if response.status_code == 200:
            report='''
VIS006sheet.write(VIS_006_02_row, VIS_006_02_col, "PASS", boldcenter)
VIS006sheet.write(VIS_006_02_row, VIS_006_02_col - 1, "''' + response.reason + '", normal)'
        else:
            report='''
VIS006sheet.write(VIS_006_02_row, VIS_006_02_col, "FAIL", boldcenter)
VIS006sheet.write(VIS_006_02_row, VIS_006_02_col - 1, "''' + response.reason + '", normal)'
        f = open('../create_worksheet.py', 'a')
        f.write(report)
        f.close()

        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_006_03(self):
        """
        VIS-006-3 - VIS-2 receives ACK. VIS-2 logs ACK event

        
        """
        sub='/voyagePlans/subscription'
        parameters={
            'callbackEndpoint': callbackurl
        }
        payload={}
        response=requests.post(url + sub, params=parameters, json=payload, cert=vis_cert, verify=trustchain)

        if response.status_code == 200:
            report='''
VIS006sheet.write(VIS_006_03_row, VIS_006_03_col, "PASS", boldcenter)
VIS006sheet.write(VIS_006_03_row, VIS_006_03_col - 1, "''' + response.reason + '", normal)'
        else:
            report='''
VIS006sheet.write(VIS_006_03_row, VIS_006_03_col, "FAIL", boldcenter)
VIS006sheet.write(VIS_006_03_row, VIS_006_03_col - 1, "''' + response.reason + '", normal)'
        f = open('../create_worksheet.py', 'a')
        f.write(report)
        f.close()

        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_006_1_1(self):
        """
        VIS-006-1-1 - In VIS-2, select TXT message and send (upload) to VIS-1 with ACKendpoint

        
        """
        sub='/voyagePlans/subscription'
        parameters={
            'callbackEndpoint': callbackurl
        }
        payload={}
        response=requests.post(url + sub, params=parameters, json=payload, cert=vis_cert, verify=trustchain)

        if response.status_code == 200:
            report='''
VIS006sheet.write(VIS_006_1_1_row, VIS_006_1_1_col, "PASS", boldcenter)
VIS006sheet.write(VIS_006_1_1_row, VIS_006_1_1_col - 1, "''' + response.reason + '", normal)'
        else:
            report='''
VIS006sheet.write(VIS_006_1_1_row, VIS_006_1_1_col, "FAIL", boldcenter)
VIS006sheet.write(VIS_006_1_1_row, VIS_006_1_1_col - 1, "''' + response.reason + '", normal)'
        f = open('../create_worksheet.py', 'a')
        f.write(report)
        f.close()

        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_006_1_2(self):
        """
        VIS-006-1-2 - Retrieve/receive the uploaded message in private application of VIS-1

        
        """
        sub='/voyagePlans/subscription'
        parameters={
            'callbackEndpoint': callbackurl
        }
        payload={}
        response=requests.post(url + sub, params=parameters, json=payload, cert=vis_cert, verify=trustchain)

        if response.status_code == 200:
            report='''
VIS006sheet.write(VIS_006_1_2_row, VIS_006_1_2_col, "PASS", boldcenter)
VIS006sheet.write(VIS_006_1_2_row, VIS_006_1_2_col - 1, "''' + response.reason + '", normal)'
        else:
            report='''
VIS006sheet.write(VIS_006_1_2_row, VIS_006_1_2_col, "FAIL", boldcenter)
VIS006sheet.write(VIS_006_1_2_row, VIS_006_1_2_col - 1, "''' + response.reason + '", normal)'
        f = open('../create_worksheet.py', 'a')
        f.write(report)
        f.close()

        self.assert200(response, "Response body is : " + response.text)


    def test_VIS_006_2_1(self):
        """
        VIS-006-2-1 - In VIS-2, select TXT message and send (upload) to VIS-1 with ACKendpoint

        
        """
        sub='/voyagePlans/subscription'
        parameters={
            'callbackEndpoint': callbackurl
        }
        payload={}
        response=requests.post(url + sub, params=parameters, json=payload, cert=vis_cert, verify=trustchain)

        if response.status_code == 200:
            report='''
VIS006sheet.write(VIS_006_2_1_row, VIS_006_2_1_col, "PASS", boldcenter)
VIS006sheet.write(VIS_006_2_1_row, VIS_006_2_1_col - 1, "''' + response.reason + '", normal)'
        else:
            report='''
VIS006sheet.write(VIS_006_2_1_row, VIS_006_2_1_col, "FAIL", boldcenter)
VIS006sheet.write(VIS_006_2_1_row, VIS_006_2_1_col - 1, "''' + response.reason + '", normal)'
        f = open('../create_worksheet.py', 'a')
        f.write(report)
        f.close()

        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_006_2_2(self):
        """
        VIS-006-2-2 - No private application retrieves/receives the message

        
        """
        sub='/voyagePlans/subscription'
        parameters={
            'callbackEndpoint': callbackurl
        }
        payload={}
        response=requests.post(url + sub, params=parameters, json=payload, cert=vis_cert, verify=trustchain)

        if response.status_code == 200:
            report='''
VIS006sheet.write(VIS_006_2_2_row, VIS_006_2_2_col, "PASS", boldcenter)
VIS006sheet.write(VIS_006_2_2_row, VIS_006_2_2_col - 1, "''' + response.reason + '", normal)'
        else:
            report='''
VIS006sheet.write(VIS_006_2_2_row, VIS_006_2_2_col, "FAIL", boldcenter)
VIS006sheet.write(VIS_006_2_2_row, VIS_006_2_2_col - 1, "''' + response.reason + '", normal)'
        f = open('../create_worksheet.py', 'a')
        f.write(report)
        f.close()

        self.assert200(response, "Response body is : " + response.text)

if __name__ == '__main__':
    unittest.main()


