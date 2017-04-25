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

class TestVIS_009(BaseTestCase):
    """ VIS-009 tests """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def vessel_connects(self):
        hostsettings.vessel_connects()
        pass

    def test_VIS_009_00(self):
        """
        VIS-009-0 - VIS-1:0 allow access

        
        """
        hostsettings.set_acl(vis2_uvid, None)
        pass

    def test_VIS_009_01(self):
        """
        VIS-009-1 - Open log and check events and data

        
        """
        sub='/voyagePlans/subscription'
        parameters={
            'callbackEndpoint': callbackurl
        }
        payload={}
        response=requests.post(url + sub, params=parameters, json=payload, cert=vis_cert, verify=trustchain)

        if response.status_code == 200:
            report='''
VIS009sheet.write(VIS_009_01_row, VIS_009_01_col, "PASS", boldcenter)
VIS009sheet.write(VIS_009_01_row, VIS_009_01_col - 1, "''' + response.reason + '", normal)'
        else:
            report='''
VIS009sheet.write(VIS_009_01_row, VIS_009_01_col, "FAIL", boldcenter)
VIS009sheet.write(VIS_009_01_row, VIS_009_01_col - 1, "''' + response.reason + '", normal)'
        f = open('../create_worksheet.py', 'a')
        f.write(report)
        f.close()

        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_009_02(self):
        """
        VIS-009-2 - Request voyage plan from VIS

        
        """
        sub='/voyagePlans/subscription'
        parameters={
            'callbackEndpoint': callbackurl
        }
        payload={}
        response=requests.post(url + sub, params=parameters, json=payload, cert=vis_cert, verify=trustchain)

        if response.status_code == 200:
            report='''
VIS009sheet.write(VIS_009_02_row, VIS_009_02_col, "PASS", boldcenter)
VIS009sheet.write(VIS_009_02_row, VIS_009_02_col - 1, "''' + response.reason + '", normal)'
        else:
            report='''
VIS009sheet.write(VIS_009_02_row, VIS_009_02_col, "FAIL", boldcenter)
VIS009sheet.write(VIS_009_02_row, VIS_009_02_col - 1, "''' + response.reason + '", normal)'
        f = open('../create_worksheet.py', 'a')
        f.write(report)
        f.close()

        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_009_03(self):
        """
        VIS-009-3 - Request subscription from VIS

        
        """
        sub='/voyagePlans/subscription'
        parameters={
            'callbackEndpoint': callbackurl
        }
        payload={}
        response=requests.post(url + sub, params=parameters, json=payload, cert=vis_cert, verify=trustchain)

        if response.status_code == 200:
            report='''
VIS009sheet.write(VIS_009_03_row, VIS_009_03_col, "PASS", boldcenter)
VIS009sheet.write(VIS_009_03_row, VIS_009_03_col - 1, "''' + response.reason + '", normal)'
        else:
            report='''
VIS009sheet.write(VIS_009_03_row, VIS_009_03_col, "FAIL", boldcenter)
VIS009sheet.write(VIS_009_03_row, VIS_009_03_col - 1, "''' + response.reason + '", normal)'
        f = open('../create_worksheet.py', 'a')
        f.write(report)
        f.close()

        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_009_04(self):
        """
        VIS-009-4 - Remove subscription

        
        """
        sub='/voyagePlans/subscription'
        parameters={
            'callbackEndpoint': callbackurl
        }
        payload={}
        response=requests.post(url + sub, params=parameters, json=payload, cert=vis_cert, verify=trustchain)

        if response.status_code == 200:
            report='''
VIS009sheet.write(VIS_009_04_row, VIS_009_04_col, "PASS", boldcenter)
VIS009sheet.write(VIS_009_04_row, VIS_009_04_col - 1, "''' + response.reason + '", normal)'
        else:
            report='''
VIS009sheet.write(VIS_009_04_row, VIS_009_04_col, "FAIL", boldcenter)
VIS009sheet.write(VIS_009_04_row, VIS_009_04_col - 1, "''' + response.reason + '", normal)'
        f = open('../create_worksheet.py', 'a')
        f.write(report)
        f.close()

        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_009_05(self):
        """
        VIS-009-5 - Upload voyage plan

        
        """
        sub='/voyagePlans/subscription'
        parameters={
            'callbackEndpoint': callbackurl
        }
        payload={}
        response=requests.post(url + sub, params=parameters, json=payload, cert=vis_cert, verify=trustchain)

        if response.status_code == 200:
            report='''
VIS009sheet.write(VIS_009_05_row, VIS_009_05_col, "PASS", boldcenter)
VIS009sheet.write(VIS_009_05_row, VIS_009_05_col - 1, "''' + response.reason + '", normal)'
        else:
            report='''
VIS009sheet.write(VIS_009_05_row, VIS_009_05_col, "FAIL", boldcenter)
VIS009sheet.write(VIS_009_05_row, VIS_009_05_col - 1, "''' + response.reason + '", normal)'
        f = open('../create_worksheet.py', 'a')
        f.write(report)
        f.close()

        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_009_06(self):
        """
        VIS-009-6 - Upload text message

        
        """
        sub='/voyagePlans/subscription'
        parameters={
            'callbackEndpoint': callbackurl
        }
        payload={}
        response=requests.post(url + sub, params=parameters, json=payload, cert=vis_cert, verify=trustchain)

        if response.status_code == 200:
            report='''
VIS009sheet.write(VIS_009_06_row, VIS_009_06_col, "PASS", boldcenter)
VIS009sheet.write(VIS_009_06_row, VIS_009_06_col - 1, "''' + response.reason + '", normal)'
        else:
            report='''
VIS009sheet.write(VIS_009_06_row, VIS_009_06_col, "FAIL", boldcenter)
VIS009sheet.write(VIS_009_06_row, VIS_009_06_col - 1, "''' + response.reason + '", normal)'
        f = open('../create_worksheet.py', 'a')
        f.write(report)
        f.close()

        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_009_07(self):
        """
        VIS-009-7 - Upload area message

        
        """
        sub='/voyagePlans/subscription'
        parameters={
            'callbackEndpoint': callbackurl
        }
        payload={}
        response=requests.post(url + sub, params=parameters, json=payload, cert=vis_cert, verify=trustchain)

        if response.status_code == 200:
            report='''
VIS009sheet.write(VIS_009_07_row, VIS_009_07_col, "PASS", boldcenter)
VIS009sheet.write(VIS_009_07_row, VIS_009_07_col - 1, "''' + response.reason + '", normal)'
        else:
            report='''
VIS009sheet.write(VIS_009_07_row, VIS_009_07_col, "FAIL", boldcenter)
VIS009sheet.write(VIS_009_07_row, VIS_009_07_col - 1, "''' + response.reason + '", normal)'
        f = open('../create_worksheet.py', 'a')
        f.write(report)
        f.close()

        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_009_08(self):
        """
        VIS-009-8 - Receive Acknowledgement

        
        """
        sub='/voyagePlans/subscription'
        parameters={
            'callbackEndpoint': callbackurl
        }
        payload={}
        response=requests.post(url + sub, params=parameters, json=payload, cert=vis_cert, verify=trustchain)

        if response.status_code == 200:
            report='''
VIS009sheet.write(VIS_009_08_row, VIS_009_08_col, "PASS", boldcenter)
VIS009sheet.write(VIS_009_08_row, VIS_009_08_col - 1, "''' + response.reason + '", normal)'
        else:
            report='''
VIS009sheet.write(VIS_009_08_row, VIS_009_08_col, "FAIL", boldcenter)
VIS009sheet.write(VIS_009_08_row, VIS_009_08_col - 1, "''' + response.reason + '", normal)'
        f = open('../create_worksheet.py', 'a')
        f.write(report)
        f.close()

        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_009_09(self):
        """
        VIS-009-9 - Send voyage plan to subscribers

        
        """
        sub='/voyagePlans/subscription'
        parameters={
            'callbackEndpoint': callbackurl
        }
        payload={}
        response=requests.post(url + sub, params=parameters, json=payload, cert=vis_cert, verify=trustchain)

        if response.status_code == 200:
            report='''
VIS009sheet.write(VIS_009_09_row, VIS_009_09_col, "PASS", boldcenter)
VIS009sheet.write(VIS_009_09_row, VIS_009_09_col - 1, "''' + response.reason + '", normal)'
        else:
            report='''
VIS009sheet.write(VIS_009_09_row, VIS_009_09_col, "FAIL", boldcenter)
VIS009sheet.write(VIS_009_09_row, VIS_009_09_col - 1, "''' + response.reason + '", normal)'
        f = open('../create_worksheet.py', 'a')
        f.write(report)
        f.close()

        self.assert200(response, "Response body is : " + response.text)

    @unittest.skip('Not applicable as we have no SSC')
    def test_VIS_009_10(self):
        """
        VIS-009-10 - findServices

        
        """
        sub='/voyagePlans/subscription'
        parameters={
            'callbackEndpoint': callbackurl
        }
        payload={}
        response=requests.post(url + sub, params=parameters, json=payload, cert=vis_cert, verify=trustchain)

        if response.status_code == 200:
            report='''
VIS009sheet.write(VIS_009_10_row, VIS_009_10_col, "PASS", boldcenter)
VIS009sheet.write(VIS_009_10_row, VIS_009_10_col - 1, "''' + response.reason + '", normal)'
        else:
            report='''
VIS009sheet.write(VIS_009_10_row, VIS_009_10_col, "FAIL", boldcenter)
VIS009sheet.write(VIS_009_10_row, VIS_009_10_col - 1, "''' + response.reason + '", normal)'
        f = open('../create_worksheet.py', 'a')
        f.write(report)
        f.close()

        self.assert200(response, "Response body is : " + response.text)

    @unittest.skip('Not applicable as we have no SSC')
    def test_VIS_009_11(self):
        """
        VIS-009-11 - callService

        
        """
        sub='/voyagePlans/subscription'
        parameters={
            'callbackEndpoint': callbackurl
        }
        payload={}
        response=requests.post(url + sub, params=parameters, json=payload, cert=vis_cert, verify=trustchain)

        if response.status_code == 200:
            report='''
VIS009sheet.write(VIS_009_11_row, VIS_009_11_col, "PASS", boldcenter)
VIS009sheet.write(VIS_009_11_row, VIS_009_11_col - 1, "''' + response.reason + '", normal)'
        else:
            report='''
VIS009sheet.write(VIS_009_11_row, VIS_009_11_col, "FAIL", boldcenter)
VIS009sheet.write(VIS_009_11_row, VIS_009_11_col - 1, "''' + response.reason + '", normal)'
        f = open('../create_worksheet.py', 'a')
        f.write(report)
        f.close()

        self.assert200(response, "Response body is : " + response.text)

    @unittest.skip('Not applicable as we have no SSC')
    def test_VIS_009_12(self):
        """
        VIS-009-12 - findIdentities

        
        """
        sub='/voyagePlans/subscription'
        parameters={
            'callbackEndpoint': callbackurl
        }
        payload={}
        response=requests.post(url + sub, params=parameters, json=payload, cert=vis_cert, verify=trustchain)

        if response.status_code == 200:
            report='''
VIS009sheet.write(VIS_009_12_row, VIS_009_12_col, "PASS", boldcenter)
VIS009sheet.write(VIS_009_12_row, VIS_009_12_col - 1, "''' + response.reason + '", normal)'
        else:
            report='''
VIS009sheet.write(VIS_009_12_row, VIS_009_12_col, "FAIL", boldcenter)
VIS009sheet.write(VIS_009_12_row, VIS_009_12_col - 1, "''' + response.reason + '", normal)'
        f = open('../create_worksheet.py', 'a')
        f.write(report)
        f.close()

        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_009_13(self):
        """
        VIS-009-13 - Test both successful calls and erroneous calls

        
        """
        sub='/voyagePlans/subscription'
        parameters={
            'callbackEndpoint': callbackurl
        }
        payload={}
        response=requests.post(url + sub, params=parameters, json=payload, cert=vis_cert, verify=trustchain)

        if response.status_code == 200:
            report='''
VIS009sheet.write(VIS_009_13_row, VIS_009_13_col, "PASS", boldcenter)
VIS009sheet.write(VIS_009_13_row, VIS_009_13_col - 1, "''' + response.reason + '", normal)'
        else:
            report='''
VIS009sheet.write(VIS_009_13_row, VIS_009_13_col, "FAIL", boldcenter)
VIS009sheet.write(VIS_009_13_row, VIS_009_13_col - 1, "''' + response.reason + '", normal)'
        f = open('../create_worksheet.py', 'a')
        f.write(report)
        f.close()

        self.assert200(response, "Response body is : " + response.text)

if __name__ == '__main__':
    unittest.main()


