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
vis2_uvid=hostsettings.vis2_uvid

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

class TestVIS_004(BaseTestCase):
    """ VIS-004 tests """

    def setUp(self):
        hostsettings.set_acl(vis2_uvid, voyageuvid)
        hostsettings.set_acl(vis2_uvid, None)
        pass

    def tearDown(self):
        pass

    def vessel_connects(self):
        hostsettings.vessel_connects()
        pass

    def test_VIS_004_01(self):
        """
        VIS-004-1 - VIS-2: Request subscription on VIS-1

        
        """
        sub='/voyagePlans/subscription'
        parameters={
            'callbackEndpoint': callbackurl,
            'uvid': voyageuvid
        }
        payload={}
        response=requests.delete(url + sub, params=parameters, json=payload, cert=vis_cert, verify=trustchain)

        if response.status_code == 200:
            report='''
VIS004sheet.write(VIS_004_01_row, VIS_004_01_col, "PASS", boldcenter)
VIS004sheet.write(VIS_004_01_row, VIS_004_01_col - 1, "''' + response.reason + '", normal)'
        else:
            report='''
VIS004sheet.write(VIS_004_01_row, VIS_004_01_col, "FAIL", boldcenter)
VIS004sheet.write(VIS_004_01_row, VIS_004_01_col - 1, "''' + response.reason + '", normal)'
        f = open('../create_worksheet.py', 'a')
        f.write(report)
        f.close()

        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_004_02(self):
        """
        VIS-004-2 - Publish voyage plan to VIS-1 with chosen UVID

        
        """
        sub='/voyagePlans'
        parameters={
            'uvid': newvoyageuvid
        }
        payload={'route': voyageplan}
        response=requests.post(url + sub, params=parameters, json=payload, cert=vis_cert, verify=trustchain)

        if response.status_code == 900:
            report='''
VIS004sheet.write(VIS_004_02_row, VIS_004_02_col, "PASS", boldcenter)
VIS004sheet.write(VIS_004_02_row, VIS_004_02_col - 1, "''' + response.reason + '", normal)'
        else:
            report='''
VIS004sheet.write(VIS_004_02_row, VIS_004_02_col, "FAIL", boldcenter)
VIS004sheet.write(VIS_004_02_row, VIS_004_02_col - 1, "''' + response.reason + '", normal)'
        f = open('../create_worksheet.py', 'a')
        f.write(report)
        f.close()

        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_004_03(self):
        """
        VIS-004-4 - VIS-2: Request remove of subscription to voyage plan from VIS-1

        
        """
        sub='/voyagePlans/subscription'
        parameters={
            'callbackEndpoint': callbackurl,
            'uvid': voyageuvid
        }
        payload={}
        response=requests.delete(url + sub, params=parameters, json=payload, cert=vis_cert, verify=trustchain)

        if response.status_code == 200:
            report='''
VIS004sheet.write(VIS_004_03_row, VIS_004_03_col, "PASS", boldcenter)
VIS004sheet.write(VIS_004_03_row, VIS_004_03_col - 1, "''' + response.reason + '", normal)'
        else:
            report='''
VIS004sheet.write(VIS_004_03_row, VIS_004_03_col, "FAIL", boldcenter)
VIS004sheet.write(VIS_004_03_row, VIS_004_03_col - 1, "''' + response.reason + '", normal)'
        f = open('../create_worksheet.py', 'a')
        f.write(report)
        f.close()

        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_004_04(self):
        """
        VIS-004-4 - Publish voyage plan to VIS-1 with chosen UVID

        
        """
        sub='/voyagePlans'
        parameters={
            'uvid': newvoyageuvid
        }
        payload={'route': voyageplan}
        response=requests.post(url + sub, params=parameters, json=payload, cert=vis_cert, verify=trustchain)

        if response.status_code == 900:
            report='''
VIS004sheet.write(VIS_004_04_row, VIS_004_04_col, "PASS", boldcenter)
VIS004sheet.write(VIS_004_04_row, VIS_004_04_col - 1, "''' + response.reason + '", normal)'
        else:
            report='''
VIS004sheet.write(VIS_004_04_row, VIS_004_04_col, "FAIL", boldcenter)
VIS004sheet.write(VIS_004_04_row, VIS_004_04_col - 1, "''' + response.reason + '", normal)'
        f = open('../create_worksheet.py', 'a')
        f.write(report)
        f.close()

        self.assert200(response, "Response body is : " + response.text)


if __name__ == '__main__':
    unittest.main()


