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

url=hostsettings.url
callbackurl=hostsettings.callbackurl
voyageuvid=hostsettings.voyageuvid
newvoyageuvid='urn:mrn:stm:voyage:id:003:001'
vis2_uvid=hostsettings.vis2_uvid

voyageplan='''<?xml version="1.0" encoding="UTF-8"?>
<route version="1.1" 
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xmlns:stm="http://stmvalidation.eu/STM/1/0/0"
  xsi:schemaLocation="http://stmvalidation.eu/STM/1/0/0 stm_extensions.xsd"
  xmlns="http://www.cirm.org/RTZ/1/1">
  <routeInfo vesselVoyage="urn:mrn:stm:voyage:id:003:001" routeName="HAN-VIS" validityPeriodStart="2017-02-15T10:00:00Z" validityPeriodStop="2017-02-16T10:00:00Z" optimizationMethod="Time table">
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

class TestVIS_003(BaseTestCase):
    """ VIS-003 tests """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def vessel_connects(self):
        hostsettings.vessel_connects()
        pass

    def test_VIS_003_00(self):
        hostsettings.set_acl(vis2_uvid, newvoyageuvid)
        hostsettings.set_acl(vis2_uvid, None)
        response=hostsettings.post_voyageplan(url, voyageplan)
        pass

    def test_VIS_003_01(self):
        """
        VIS-003-1 - VIS-2: Request subscription on VIS-1

        
        """
        response=hostsettings.subscribe_voyageplan(url, callbackurl)
        hostsettings.reportrow('VIS003sheet', 'VIS_003_01_row', 'VIS_003_01_col',
            response.status_code == 200, response.reason)
        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_003_02(self):
        """
        VIS-003-2 - VIS-2 logs event

        
        """
        logged = hostsettings.check_event('post_subscription', callbackurl)
        hostsettings.reportrow('VIS003sheet', 'VIS_003_02_row', 'VIS_003_02_col',
            logged, '')
        self.assertTrue(logged)

    def test_VIS_003_03(self):
        """
        VIS-003-3 - VIS-1 gets a POST subscription request

        
        """
        logged = hostsettings.check_event('subscribe', callbackurl)
        hostsettings.reportrow('VIS003sheet', 'VIS_003_03_row', 'VIS_003_03_col',
            logged, '')
        self.assertTrue(logged)

    def test_VIS_003_04(self):
        """
        VIS-003-4 - VIS-1 logs event

        
        """
        logged = hostsettings.check_event('subscribe', callbackurl)
        hostsettings.reportrow('VIS003sheet', 'VIS_003_04_row', 'VIS_003_04_col',
            logged, '')
        self.assertTrue(logged)

    def test_VIS_003_05(self):
        """
        VIS-003-5 - VIS-1 checks against ACL and get OK

        
        """
        allowed = hostsettings.acl_allowed(vis2_uvid)
        hostsettings.reportrow('VIS003sheet', 'VIS_003_05_row', 'VIS_003_05_col',
            allowed, '')
        self.assertTrue(allowed)

    def test_VIS_003_06(self):
        """
        VIS-003-6 - VIS-1 returns the latest published voyage plan for each UVID with routeStatus<8

        
        """
        logged = hostsettings.check_event('post_voyage')
        hostsettings.reportrow('VIS003sheet', 'VIS_003_06_row', 'VIS_003_06_col',
            logged, '')
        self.assertTrue(logged)

    def test_VIS_003_07(self):
        """
        VIS-003-7 - VIS-1 returns the latest published voyage plan for each UVID with routeStatus<8

        
        """
        response=hostsettings.post_voyageplan(url, voyageplan)
        hostsettings.reportrow('VIS003sheet', 'VIS_003_07_row', 'VIS_003_07_col',
            response.status_code == 200, response.reason)
        self.assert200(response, "Response body is : " + response.text)


    def test_VIS_003_1_1(self):
        """
        VIS-003-1-1 - In VIS-2, request subscription on voyage plans from VIS-1 

        
        """
        response=hostsettings.subscribe_voyageplan(url, 'https://localhost:8001', newvoyageuvid)
        hostsettings.reportrow('VIS003sheet', 'VIS_003_1_1_row', 'VIS_003_1_1_col',
            response.status_code == 200, response.reason)
        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_003_1_2(self):
        """
        VIS-003-1-2 - Publish voyage plan to VIS-1

        
        """
        response=hostsettings.post_voyageplan(url, voyageplan)
        hostsettings.reportrow('VIS003sheet', 'VIS_003_1_2_row', 'VIS_003_1_2_col',
            response.status_code == 200, response.reason)
        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_003_2_1(self):
        """
        VIS-003-2-1 - In VIS-2, request subscription on voyage plans from VIS-1, but with incorrect UVID

        
        """
        response=hostsettings.subscribe_voyageplan(url, callbackurl, 'urn:mrn:stm:voyage:id:not:existing')
        hostsettings.reportrow('VIS003sheet', 'VIS_003_2_1_row', 'VIS_003_2_1_col',
            response.status_code == 404, response.reason)
        self.assert404(response, "Response body is : " + response.text)

    def test_VIS_003_2_2(self):
        """
        VIS-003-2-2 - Publish voyage plan to VIS 1 instance

        
        """
        hostsettings.reportrow('VIS003sheet', 'VIS_003_2_2_row', 'VIS_003_2_2_col')
        pass


    def test_VIS_003_3_1(self):
        """
        VIS-003-3-1 - VIS-2: Request subscription from VIS-1

        
        """
        response=hostsettings.subscribe_voyageplan(url, callbackurl)
        hostsettings.reportrow('VIS003sheet', 'VIS_003_3_1_row', 'VIS_003_3_1_col',
            response.status_code == 200, response.reason)
        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_003_3_2(self):
        """
        VIS-003-3-2 - VIS-2: Request subscription from VIS-1

        
        """
        response=hostsettings.subscribe_voyageplan(url, callbackurl)
        hostsettings.reportrow('VIS003sheet', 'VIS_003_3_2_row', 'VIS_003_3_2_col',
            response.status_code == 200, response.reason)
        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_003_3_3(self):
        """
        VIS-003-3-3 - VIS-2: Request subscription from VIS-1

        
        """
        response=hostsettings.subscribe_voyageplan(url, callbackurl, newvoyageuvid)
        hostsettings.reportrow('VIS003sheet', 'VIS_003_3_3_row', 'VIS_003_3_3_col',
            response.status_code == 200, response.reason)
        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_003_3_4(self):
        """
        VIS-003-3-4 - VIS-2: Request subscription from VIS-1

        
        """
        response=hostsettings.subscribe_voyageplan(url, callbackurl, newvoyageuvid)
        hostsettings.reportrow('VIS003sheet', 'VIS_003_3_4_row', 'VIS_003_3_4_col',
            response.status_code == 200, response.reason)
        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_003_3_5(self):
        """
        VIS-003-3-5 - Test cleanup


        
        """
        response=hostsettings.subscribe_voyageplan(url, 'delete', newvoyageuvid)
        hostsettings.rm_acl(vis2_uvid, newvoyageuvid)
        hostsettings.rm_acl(vis2_uvid)
        hostsettings.rm_subs(vis2_uvid)
        p = Path('import')
        files = list(p.glob('**/' + voyageuvid + '.*'))
        for item in files:
            os.remove(str(item))
        files = list(p.glob('**/' + newvoyageuvid + '.*'))
        for item in files:
            os.remove(str(item))
        files = list(p.glob('**/' + vis2_uvid + '*'))
        for item in files:
            os.remove(str(item))
        files = list(p.glob('**/parse*'))
        for item in files:
            os.remove(str(item))

        p = Path('export')
        files = list(p.glob('**/' + newvoyageuvid + '.*'))
        for item in files:
            os.remove(str(item))
        files = list(p.glob('**/' + vis2_uvid + '*'))
        for item in files:
            os.remove(str(item))
        files = list(p.glob('**/parse*'))
        for item in files:
            os.remove(str(item))
        pass

if __name__ == '__main__':
    unittest.main()


