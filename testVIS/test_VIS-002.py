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
voyageuvid=hostsettings.voyageuvid
newvoyageuvid='urn:mrn:stm:voyage:id:002:001'
newvoyageuvid2='urn:mrn:stm:voyage:id:002:002'
vis2_uvid=hostsettings.vis2_uvid

voyageplan='''<?xml version="1.0" encoding="UTF-8"?>
<route version="1.1" 
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xmlns:stm="http://stmvalidation.eu/STM/1/0/0"
  xsi:schemaLocation="http://stmvalidation.eu/STM/1/0/0 stm_extensions.xsd"
  xmlns="http://www.cirm.org/RTZ/1/1">
  <routeInfo vesselVoyage="urn:mrn:stm:voyage:id:002:001" routeName="HAN-VIS" validityPeriodStart="2017-02-15T10:00:00Z" validityPeriodStop="2017-02-16T10:00:00Z" optimizationMethod="Time table">
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

voyageplan2='''<?xml version="1.0" encoding="UTF-8"?>
<route version="1.1" 
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xmlns:stm="http://stmvalidation.eu/STM/1/0/0"
  xsi:schemaLocation="http://stmvalidation.eu/STM/1/0/0 stm_extensions.xsd"
  xmlns="http://www.cirm.org/RTZ/1/1">
  <routeInfo vesselVoyage="urn:mrn:stm:voyage:id:002:002" routeName="HAN-VIS" validityPeriodStart="2017-02-15T10:00:00Z" validityPeriodStop="2017-02-16T10:00:00Z" optimizationMethod="Time table">
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


class TestVIS_002(BaseTestCase):
    """ VIS-002 tests """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def vessel_connects(self):
        hostsettings.vessel_connects()
        pass


    def test_VIS_002_00(self):
        """
        VIS-002-0 - Preparation:Organisation for VIS-2 authorized to exactly one published voyage plan with routestatus=7 and chosen UVID

        
        """
        hostsettings.set_acl(vis2_uvid, voyageuvid)
        hostsettings.set_acl(vis2_uvid, newvoyageuvid)
        hostsettings.set_acl(vis2_uvid, newvoyageuvid2)
        hostsettings.reportrow('VIS002sheet', 'VIS_002_00_row', 'VIS_002_00_col',
            True, '')
        pass

    def test_VIS_002_01(self):
        """
        VIS-002-1 - VIS-2 request voyage plan from VIS-1, no specific UVID or status, hence no parameters given

        
        """
        response=hostsettings.get_voyageplan(url)
        hostsettings.reportrow('VIS002sheet', 'VIS_002_01_row', 'VIS_002_01_col',
            response.status_code == 200, response.reason)
        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_002_02(self):
        """
        VIS-002-2 - VIS-2 request voyage plan with chosen UVID from VIS-1, no specific status

        
        """
        response=hostsettings.get_voyageplan(url, voyageuvid)
        hostsettings.reportrow('VIS002sheet', 'VIS_002_02_row', 'VIS_002_02_col',
            response.status_code == 200, response.reason)
        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_002_03(self):
        """
        VIS-002-3 - VIS-2 request voyage plan with routeStatus= 7 from VIS-1, no specific UVID

        
        """
        response=hostsettings.get_voyageplan(url, routeStatus = '7')
        hostsettings.reportrow('VIS002sheet', 'VIS_002_03_row', 'VIS_002_03_col',
            response.status_code == 200, response.reason)
        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_002_04(self):
        """
        VIS-002-4 - VIS-2 request voyage plan with chosen UVID and routeStatus=7 from VIS-1

        
        """
        response=hostsettings.get_voyageplan(url, uvid=voyageuvid, routeStatus = '7')
        hostsettings.reportrow('VIS002sheet', 'VIS_002_04_row', 'VIS_002_04_col',
            response.status_code == 200, response.reason)
        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_002_05(self):
        """
        VIS-002-5 - VIS-2 request voyage plan with another (non published) UVID and routeStatus=7 from VIS-1

        
        """
        response=hostsettings.get_voyageplan(url, uvid='urn:mrn:stm:voyage:id:not:found', routeStatus = '7')
        hostsettings.reportrow('VIS002sheet', 'VIS_002_05_row', 'VIS_002_05_col',
            response.status_code == 404, response.reason)
        self.assert404(response, "Response body is : " + response.text)

    def test_VIS_002_06(self):
        """
        VIS-002-6 - VIS-2 request voyage plan with chosen UVID and routeStatus=6 from VIS-1

        
        """
        response=hostsettings.get_voyageplan(url, uvid=voyageuvid, routeStatus = '6')
        hostsettings.reportrow('VIS002sheet', 'VIS_002_06_row', 'VIS_002_06_col',
            response.status_code == 404, response.reason)
        self.assert404(response, "Response body is : " + response.text)

    def test_VIS_002_07(self):
        """
        VIS-002-7 - VIS-2 request voyage plan with another (non published) UVID from VIS-1, no specific status

        
        """
        response=hostsettings.get_voyageplan(url, uvid='urn:mrn:stm:voyage:id:not:found')
        hostsettings.reportrow('VIS002sheet', 'VIS_002_07_row', 'VIS_002_07_col',
            response.status_code == 404, response.reason)
        self.assert404(response, "Response body is : " + response.text)

    def test_VIS_002_08(self):
        """
        VIS-002-8 - VIS-2 request voyage plan with routeStatus= 6 (non published)  from VIS-1, no specific UVID

        
        """
        response=hostsettings.get_voyageplan(url, routeStatus='6')
        hostsettings.reportrow('VIS002sheet', 'VIS_002_08_row', 'VIS_002_08_col',
            response.status_code == 404, response.reason)
        self.assert404(response, "Response body is : " + response.text)

    def test_VIS_002_9_0(self):
        """
        VIS-002-1-0 - Preparation Organisation for VIS-2 authorized to chosen UVID

        
        """
        hostsettings.rm_uvid(newvoyageuvid)
        hostsettings.set_acl(vis2_uvid, newvoyageuvid)
        hostsettings.set_acl(vis2_uvid, newvoyageuvid2)
        hostsettings.reportrow('VIS002sheet', 'VIS_002_1_0_row', 'VIS_002_1_0_col',
            True, '')
        pass

    def test_VIS_002_9_1(self):
        """
        VIS-002-1-1 - VIS-1 : Publish voyage plan with chosen UVID and routeStatus=7


        """
        response=hostsettings.post_voyageplan(url, voyageplan)
        hostsettings.reportrow('VIS002sheet', 'VIS_002_1_1_row', 'VIS_002_1_1_col',
            response.status_code == 200, response.reason)
        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_002_9_2(self):
        """
        VIS-002-1-2 - VIS-2 : Request voyage plans from VIS-1

        
        """
        response=hostsettings.get_voyageplan(url)
        hostsettings.reportrow('VIS002sheet', 'VIS_002_1_2_row', 'VIS_002_1_2_col',
            response.status_code == 200, response.reason)
        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_002_9_3(self):
        """
        VIS-002-1-3 - VIS-1 : Publish voyage plan with chosen UVID and routeStatus=7


        """
        response=hostsettings.post_voyageplan(url, voyageplan)
        hostsettings.reportrow('VIS002sheet', 'VIS_002_1_3_row', 'VIS_002_1_3_col',
            response.status_code == 200, response.reason)
        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_002_9_4(self):
        """
        VIS-002-1-4 - VIS-2 : Request voyage plans from VIS-1

        
        """
        response=hostsettings.get_voyageplan(url)
        hostsettings.reportrow('VIS002sheet', 'VIS_002_1_4_row', 'VIS_002_1_4_col',
            response.status_code == 200, response.reason)
        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_002_9_5(self):
        """
        VIS-002-1-5 - VIS-1 : Publish voyage plan with new UVID for the same ship and routeStatus=7


        """
        response=hostsettings.post_voyageplan(url, voyageplan)
        hostsettings.reportrow('VIS002sheet', 'VIS_002_1_5_row', 'VIS_002_1_5_col',
            response.status_code == 200, response.reason)
        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_002_9_6(self):
        """
        VIS-002-1-6 - VIS-2 : Request voyage plans from VIS-1

        
        """
        response=hostsettings.get_voyageplan(url)
        hostsettings.reportrow('VIS002sheet', 'VIS_002_1_6_row', 'VIS_002_1_6_col',
            response.status_code == 200, response.reason)
        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_002_9_7(self):
        """
        VIS-002-1-7 - VIS-1 : Publish voyage plan with new UVID for another ship and routeStatus=7


        """
        response=hostsettings.post_voyageplan(url, voyageplan)
        hostsettings.reportrow('VIS002sheet', 'VIS_002_1_7_row', 'VIS_002_1_7_col',
            response.status_code == 200, response.reason)
        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_002_9_8(self):
        """
        VIS-002-1-8 - VIS-2 : Request voyage plans from VIS-1

        
        """
        response=hostsettings.get_voyageplan(url)
        hostsettings.reportrow('VIS002sheet', 'VIS_002_1_8_row', 'VIS_002_1_8_col',
            response.status_code == 200, response.reason)
        self.assert200(response, "Response body is : " + response.text)


if __name__ == '__main__':
    unittest.main()


