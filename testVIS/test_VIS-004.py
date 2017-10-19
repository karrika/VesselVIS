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
callbackurl=service.callbackurl
voyageuvid='urn:mrn:stm:voyage:id:004:001'
vis2_uvid=service.vis2_uvid

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

class TestVIS_004(BaseTestCase):
    """ VIS-004 tests """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_VIS_004_00(self):
        """
        VIS-004-0 - VIS-1:0 allow access

        
        """
        service.set_acl(vis2_uvid, None)
        pass

    def test_VIS_004_01(self):
        """
        VIS-004-1 - VIS-2: Request subscription on VIS-1

        
        """
        response=service.subscribe_voyageplan(url, callbackurl)
        service.reportrow('VIS004sheet', 'VIS_004_01_row', 'VIS_004_01_col',
            response.status_code == 200, response.reason)
        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_004_02(self):
        """
        VIS-004-2 - Publish voyage plan to VIS-1 with chosen UVID

        
        """
        response=service.post_voyageplan(url, voyageplan)
        service.reportrow('VIS004sheet', 'VIS_004_02_row', 'VIS_004_02_col',
            response.status_code == 200, response.reason)
        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_004_03(self):
        """
        VIS-004-3 - VIS-2: Request remove of subscription to voyage plan from VIS-1

        
        """
        response=service.unsubscribe_voyageplan(url, callbackurl)
        service.reportrow('VIS004sheet', 'VIS_004_03_row', 'VIS_004_03_col',
            response.status_code == 200, response.reason)
        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_004_04(self):
        """
        VIS-004-4 - Publish voyage plan to VIS-1 with chosen UVID

        
        """
        response=service.post_voyageplan(url, voyageplan)
        service.reportrow('VIS004sheet', 'VIS_004_04_row', 'VIS_004_04_col',
            response.status_code == 200, response.reason)
        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_004_1_1(self):
        """
        VIS-004-1-1 - VIS-2: Request subscription on VIS-1

        
        """
        response=service.subscribe_voyageplan(url, callbackurl)
        service.reportrow('VIS004sheet', 'VIS_004_1_1_row', 'VIS_004_1_1_col',
            response.status_code == 200, response.reason)
        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_004_1_2(self):
        """
        VIS-004-1-2 - Publish voyage plan to VIS-1 with chosen UVID

        
        """
        response=service.post_voyageplan(url, voyageplan)
        service.reportrow('VIS004sheet', 'VIS_004_1_2_row', 'VIS_004_1_2_col',
            response.status_code == 200, response.reason)
        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_004_1_3(self):
        """
        VIS-004-1-3 - VIS-2: Request remove of subscription to voyage plan from VIS-1

        
        """
        response=service.unsubscribe_voyageplan(url, 'https://localhost:99')
        service.reportrow('VIS004sheet', 'VIS_004_1_3_row', 'VIS_004_1_3_col',
            response.status_code == 200, response.reason)
        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_004_1_4(self):
        """
        VIS-004-1-4 - Publish voyage plan to VIS-1 with chosen UVID

        
        """
        response=service.post_voyageplan(url, voyageplan)
        service.reportrow('VIS004sheet', 'VIS_004_1_4_row', 'VIS_004_1_4_col',
            response.status_code == 200, response.reason)
        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_004_1_5(self):
        """
        VIS-004-1-5 - Publish voyage plan to VIS-1 with chosen UVID

        
        """
        response=service.post_voyageplan(url, voyageplan)
        service.reportrow('VIS004sheet', 'VIS_004_1_5_row', 'VIS_004_1_5_col',
            response.status_code == 200, response.reason)
        self.assert200(response, "Response body is : " + response.text)


if __name__ == '__main__':
    unittest.main()


