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
voyageuvid='urn:mrn:stm:voyage:id:005:001'

voyageplan='''<?xml version="1.0" encoding="UTF-8"?>
<route version="1.1" 
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xmlns:stm="http://stmvalidation.eu/STM/1/0/0"
  xsi:schemaLocation="http://stmvalidation.eu/STM/1/0/0 stm_extensions.xsd"
  xmlns="http://www.cirm.org/RTZ/1/1">
  <routeInfo vesselVoyage="urn:mrn:stm:voyage:id:005:001" routeName="HAN-VIS" validityPeriodStart="2017-02-15T10:00:00Z" validityPeriodStop="2017-02-16T10:00:00Z" optimizationMethod="Time table">
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

class TestVIS_005(BaseTestCase):
    """ VIS-005 tests """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_VIS_005_01(self):
        """
        VIS-005-1 - VIS-2: Select voyage plan and send (upload) the voyage plan to VIS-1, no ACK requested, no callback expected

        
        """
        response=service.post_voyageplan(url, voyageplan)
        service.reportrow('VIS005sheet', 'VIS_005_01_row', 'VIS_005_01_col',
            response.status_code == 200, response.reason)
        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_005_02(self):
        """
        VIS-005-2 - Select voyage plan in VIS-2 and send (upload) the voyage plan to VIS-1,
                    no ACK requested, no callback expected

        
        """
        response=service.post_voyageplan(url, voyageplan)
        service.reportrow('VIS005sheet', 'VIS_005_02_row', 'VIS_005_02_col',
            response.status_code == 200, response.reason)
        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_005_03(self):
        """
        VIS-005-3 - STM Module retrieves messages from VIS-1

        
        """
        self.assertTrue(service.uvid_exists(voyageuvid))

    def test_VIS_005_1_1(self):
        """
        VIS-005-1-1 - In VIS-2, search for VIS with MMSI=12345678

        
        """
        response = service.search('mmsi:12345678')
        service.reportrow('VIS005sheet', 'VIS_005_1_1_row', 'VIS_005_1_1_col',
            response.status_code == 200, response.reason)
        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_005_1_2(self):
        """
        VIS-005-1-2 - In VIS-2, select voyage plan and send (upload) the voyage plan to VIS-1 with ACKendpoint

        
        """
        response=service.post_voyageplan(url, voyageplan, deliveryAckEndPoint = 'https://localhost:8002')
        service.reportrow('VIS005sheet', 'VIS_005_1_2_row', 'VIS_005_1_2_col',
            response.status_code == 200, response.reason)
        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_005_1_3(self):
        """
        VIS-005-1-3 - STM Module retrieves messages from VIS-1

        
        """
        logged = service.check_event('upload')
        service.reportrow('VIS005sheet', 'VIS_005_1_3_row', 'VIS_005_1_3_col',
            logged, '')
        self.assertTrue(logged)

    def test_VIS_005_2_1(self):
        """
        VIS-005-2-2 - In VIS-2, select voyage plan and send (upload) the voyage plan to VIS-1 with ACKendpoint that does not respond

        
        """
        response=service.post_voyageplan(url, voyageplan, deliveryAckEndPoint = 'https://localhost:8001')
        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_005_2_2(self):
        """
        VIS-005-1-3 - STM Module retrieves messages from VIS-1

        
        """
        logged = service.check_event('upload')
        service.reportrow('VIS005sheet', 'VIS_005_2_2_row', 'VIS_005_2_2_col',
            logged, '')
        self.assertTrue(logged)



if __name__ == '__main__':
    unittest.main()


