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

    def test_VIS_003_00(self):
        hostsettings.set_acl(vis_uvid, voyageuvid)
        hostsettings.set_acl(vis_uvid, None)
        pass

    def test_VIS_003_01(self):
        """
        VIS-003-1 - VIS-2: Request subscription on VIS-1

        
        """
        sub='/voyagePlans/subscription'
        parameters={
            'callbackEndpoint': callbackurl
        }
        payload={}
        response=requests.post(url + sub, params=parameters, json=payload, cert=vis_cert, verify=trustchain)

        if response.status_code == 200:
            report='''
VIS003sheet.write(VIS_003_01_row, VIS_003_01_col, "PASS", boldcenter)
'''
        else:
            report='''
VIS003sheet.write(VIS_003_01_row, VIS_003_01_col, "FAIL", boldcenter)
VIS003sheet.write(VIS_003_01_row, VIS_003_01_col - 1, "''' + response.reason + '", normal)'
        f = open('../create_worksheet.py', 'a')
        f.write(report)
        f.close()

        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_003_02(self):
        """
        VIS-003-2 - VIS-2 logs event

        
        """
        logged = hostsettings.check_event('subscribe', callbackurl)
        if logged:
            report='''
VIS003sheet.write(VIS_003_02_row, VIS_003_02_col, "PASS", boldcenter)
'''
        else:
            report='''
VIS003sheet.write(VIS_003_02_row, VIS_003_02_col, "FAIL", boldcenter)
VIS003sheet.write(VIS_003_02_row, VIS_003_02_col - 1, "''' + '", normal)'
        f = open('../create_worksheet.py', 'a')
        f.write(report)
        f.close()
        self.assertTrue(logged)

    def test_VIS_003_03(self):
        """
        VIS-003-3 - VIS-1 gets a POST subscription request

        
        """
        report='''
VIS003sheet.write(VIS_003_03_row, VIS_003_03_col, "PASS", boldcenter)
'''
        f = open('../create_worksheet.py', 'a')
        f.write(report)
        f.close()
        pass

    def test_VIS_003_04(self):
        """
        VIS-003-4 - VIS-1 logs event

        
        """
        report='''
VIS003sheet.write(VIS_003_04_row, VIS_003_04_col, "PASS", boldcenter)
'''
        f = open('../create_worksheet.py', 'a')
        f.write(report)
        f.close()
        pass

    def test_VIS_003_05(self):
        """
        VIS-003-5 - VIS-1 checks against ACL and get OK

        
        """
        report='''
VIS003sheet.write(VIS_003_05_row, VIS_003_05_col, "PASS", boldcenter)
'''
        f = open('../create_worksheet.py', 'a')
        f.write(report)
        f.close()
        pass

    @unittest.skip('Check for existence of voyage plan in VIS-2')
    def test_VIS_003_06(self):
        """
        VIS-003-6 - VIS-1 returns the latest published voyage plan for each UVID with routeStatus<8

        
        """
        pass

    @unittest.skip('Publish voyage plan to VIS-1. The plan will then be posted to VIS-2 also.')
    def test_VIS_003_07(self):
        """
        VIS-003-7 - VIS-1 returns the latest published voyage plan for each UVID with routeStatus<8

        
        """
        pass


    def test_VIS_003_1_1(self):
        """
        VIS-003-1-1 - In VIS-2, request subscription on voyage plans from VIS-1 

        
        """
        sub='/voyagePlans/subscription'
        parameters={
            'callbackEndpoint': 'https://localhost:99',
            'uvid': voyageuvid
        }
        payload={}
        response=requests.post(url + sub, params=parameters, json=payload, cert=vis_cert, verify=trustchain)

        if response.status_code == 200:
            report='''
VIS003sheet.write(VIS_003_1_1_row, VIS_003_1_1_col, "PASS", boldcenter)
VIS003sheet.write(VIS_003_1_1_row, VIS_003_1_1_col - 1, "''' + response.reason + '", normal)'
        else:
            report='''
VIS003sheet.write(VIS_003_1_1_row, VIS_003_1_1_col, "FAIL", boldcenter)
VIS003sheet.write(VIS_003_1_1_row, VIS_003_1_1_col - 1, "''' + response.reason + '", normal)'
        f = open('../create_worksheet.py', 'a')
        f.write(report)
        f.close()

        self.assert400(response, "Response body is : " + response.text)

    def test_VIS_003_2_1(self):
        """
        VIS-003-2-1 - In VIS-2, request subscription on voyage plans from VIS-1, but with incorrect UVID

        
        """
        sub='/voyagePlans/subscription'
        parameters={
            'callbackEndpoint': callbackurl,
            'uvid': 'urn:mrn:stm:voyage:id:not:existing'
        }
        payload={}
        response=requests.post(url + sub, params=parameters, json=payload, cert=vis_cert, verify=trustchain)

        if response.status_code == 404:
            report='''
VIS003sheet.write(VIS_003_2_1_row, VIS_003_2_1_col, "PASS", boldcenter)
VIS003sheet.write(VIS_003_2_1_row, VIS_003_2_1_col - 1, "''' + response.reason + '", normal)'
        else:
            report='''
VIS003sheet.write(VIS_003_2_1_row, VIS_003_2_1_col, "FAIL", boldcenter)
VIS003sheet.write(VIS_003_2_1_row, VIS_003_2_1_col - 1, "''' + response.reason + '", normal)'
        f = open('../create_worksheet.py', 'a')
        f.write(report)
        f.close()

        self.assert404(response, "Response body is : " + response.text)

    def test_VIS_003_2_2(self):
        """
        VIS-003-2-2 - Publish voyage plan to VIS 1 instance

        
        """
        report='''
VIS003sheet.write(VIS_003_2_2_row, VIS_003_2_2_col, "PASS", boldcenter)
'''
        f = open('../create_worksheet.py', 'a')
        f.write(report)
        f.close()
        pass


    def test_VIS_003_3_1(self):
        """
        VIS-003-3-1 - VIS-2: Request subscription from VIS-1

        
        """
        sub='/voyagePlans/subscription'
        parameters={
            'callbackEndpoint': callbackurl
        }
        payload={}
        response=requests.post(url + sub, params=parameters, json=payload, cert=vis_cert, verify=trustchain)

        if response.status_code == 200:
            report='''
VIS003sheet.write(VIS_003_3_1_row, VIS_003_3_1_col, "PASS", boldcenter)
VIS003sheet.write(VIS_003_3_1_row, VIS_003_3_1_col - 1, "''' + response.reason + '", normal)'
        else:
            report='''
VIS003sheet.write(VIS_003_3_1_row, VIS_003_3_1_col, "FAIL", boldcenter)
VIS003sheet.write(VIS_003_3_1_row, VIS_003_3_1_col - 1, "''' + response.reason + '", normal)'
        f = open('../create_worksheet.py', 'a')
        f.write(report)
        f.close()

        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_003_3_2(self):
        """
        VIS-003-3-2 - VIS-2: Request subscription from VIS-1

        
        """
        sub='/voyagePlans/subscription'
        parameters={
            'callbackEndpoint': callbackurl
        }
        payload={}
        response=requests.post(url + sub, params=parameters, json=payload, cert=vis_cert, verify=trustchain)

        if response.status_code == 200:
            report='''
VIS003sheet.write(VIS_003_3_2_row, VIS_003_3_2_col, "PASS", boldcenter)
VIS003sheet.write(VIS_003_3_2_row, VIS_003_3_2_col - 1, "''' + response.reason + '", normal)'
        else:
            report='''
VIS003sheet.write(VIS_003_3_2_row, VIS_003_3_2_col, "FAIL", boldcenter)
VIS003sheet.write(VIS_003_3_2_row, VIS_003_3_2_col - 1, "''' + response.reason + '", normal)'
        f = open('../create_worksheet.py', 'a')
        f.write(report)
        f.close()

        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_003_3_3(self):
        """
        VIS-003-3-3 - VIS-2: Request subscription from VIS-1

        
        """
        sub='/voyagePlans/subscription'
        parameters={
            'callbackEndpoint': callbackurl,
            'uvid': voyageuvid
        }
        payload={}
        response=requests.post(url + sub, params=parameters, json=payload, cert=vis_cert, verify=trustchain)

        if response.status_code == 200:
            report='''
VIS003sheet.write(VIS_003_3_3_row, VIS_003_3_3_col, "PASS", boldcenter)
VIS003sheet.write(VIS_003_3_3_row, VIS_003_3_3_col - 1, "''' + response.reason + '", normal)'
        else:
            report='''
VIS003sheet.write(VIS_003_3_3_row, VIS_003_3_3_col, "FAIL", boldcenter)
VIS003sheet.write(VIS_003_3_3_row, VIS_003_3_3_col - 1, "''' + response.reason + '", normal)'
        f = open('../create_worksheet.py', 'a')
        f.write(report)
        f.close()

        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_003_3_4(self):
        """
        VIS-003-3-4 - VIS-2: Request subscription from VIS-1

        
        """
        sub='/voyagePlans/subscription'
        parameters={
            'callbackEndpoint': callbackurl,
            'uvid': voyageuvid
        }
        payload={}
        response=requests.post(url + sub, params=parameters, json=payload, cert=vis_cert, verify=trustchain)

        if response.status_code == 200:
            report='''
VIS003sheet.write(VIS_003_3_4_row, VIS_003_3_4_col, "PASS", boldcenter)
VIS003sheet.write(VIS_003_3_4_row, VIS_003_3_4_col - 1, "''' + response.reason + '", normal)'
        else:
            report='''
VIS003sheet.write(VIS_003_3_4_row, VIS_003_3_4_col, "FAIL", boldcenter)
VIS003sheet.write(VIS_003_3_4_row, VIS_003_3_4_col - 1, "''' + response.reason + '", normal)'
        f = open('../create_worksheet.py', 'a')
        f.write(report)
        f.close()

        self.assert200(response, "Response body is : " + response.text)



if __name__ == '__main__':
    unittest.main()


