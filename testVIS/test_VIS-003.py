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
newvoyageuvid=hostsettings.newvoyageuvid
newvoyageuvid2=hostsettings.newvoyageuvid2
vis_uvid=hostsettings.vis_uvid

voyageplan='\
<?xml version="1.0" encoding="UTF-8"?>\
<route version="1.0" xmlns="http://www.cirm.org/RTZ/1/0">\
    <routeInfo routeName="Test-Mini-1" routeStatus="7"/>\
        <waypoints>\
                <waypoint id="1">\
                        <position lat="53.5123" lon="8.11998"/>\
                </waypoint>\
                <waypoint id="15">\
                        <position lat="53.0492" lon="8.87731"/>\
                </waypoint>\
        </waypoints>\
</route>\
'


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
        hostsettings.set_acl(vis_uvid, voyageuvid)
        hostsettings.set_acl(vis_uvid, None)
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
        hostsettings.log_event('subscribe', callbackurl)
        logged = hostsettings.check_event('subscribe', callbackurl)
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
        allowed = hostsettings.acl_allowed(vis_uvid)
        hostsettings.reportrow('VIS003sheet', 'VIS_003_05_row', 'VIS_003_05_col',
            allowed, '')
        self.assertTrue(allowed)

    def test_VIS_003_06(self):
        """
        VIS-003-6 - VIS-1 returns the latest published voyage plan for each UVID with routeStatus<8

        
        """
        logged = hostsettings.check_event('post_voyageplan', callbackurl)
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
        response=hostsettings.subscribe_voyageplan(url, 'https://localhost:99', voyageuvid)
        hostsettings.reportrow('VIS003sheet', 'VIS_003_1_1_row', 'VIS_003_1_1_col',
            response.status_code == 400, response.reason)
        self.assert400(response, "Response body is : " + response.text)

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
        response=hostsettings.subscribe_voyageplan(url, callbackurl, voyageuvid)
        hostsettings.reportrow('VIS003sheet', 'VIS_003_3_3_row', 'VIS_003_3_3_col',
            response.status_code == 200, response.reason)
        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_003_3_4(self):
        """
        VIS-003-3-4 - VIS-2: Request subscription from VIS-1

        
        """
        response=hostsettings.subscribe_voyageplan(url, callbackurl, voyageuvid)
        hostsettings.reportrow('VIS003sheet', 'VIS_003_3_4_row', 'VIS_003_3_4_col',
            response.status_code == 200, response.reason)
        self.assert200(response, "Response body is : " + response.text)



if __name__ == '__main__':
    unittest.main()


