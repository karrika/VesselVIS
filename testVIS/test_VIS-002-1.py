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


class TestVIS_002_1(BaseTestCase):
    """ VIS-002 tests """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def vessel_connects(self):
        hostsettings.vessel_connects()
        pass


    def test_VIS_002_9_0(self):
        """
        VIS-002-1-0 - Preparation Organisation for VIS-2 authorized to chosen UVID

        
        """
        hostsettings.rm_uvid(newvoyageuvid)
        hostsettings.set_acl(vis2_uvid, newvoyageuvid)
        hostsettings.set_acl(vis2_uvid, newvoyageuvid2)

        report='''
VIS002sheet.write(VIS_002_1_0_row, VIS_002_08_col, "PASS", boldcenter)
'''
        f = open('../create_worksheet.py', 'a')
        f.write(report)
        f.close()

        pass

    def test_VIS_002_9_1(self):
        """
        VIS-002-1-1 - VIS-1 : Publish voyage plan with chosen UVID and routeStatus=7


        """
        sub='/voyagePlans'
        parameters={
            'uvid': newvoyageuvid,
            'routeStatus': '7'
        }
        payload={'route': voyageplan}
        response=requests.post(url + sub, params=parameters, json=payload, cert=vis_cert, verify=trustchain)

        if response.status_code == 200:
            report='''
VIS002sheet.write(VIS_002_1_1_row, VIS_002_1_1_col, "PASS", boldcenter)
'''
        else:
            report='''
VIS002sheet.write(VIS_002_1_1_row, VIS_002_1_1_col, "FAIL", boldcenter)
VIS002sheet.write(VIS_002_1_1_row, VIS_002_1_1_col - 1, "''' + response.reason + '", normal)'
        f = open('../create_worksheet.py', 'a')
        f.write(report)
        f.close()

        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_002_9_2(self):
        """
        VIS-002-1-2 - VIS-2 : Request voyage plans from VIS-1

        
        """
        sub='/voyagePlans'
        parameters={
            'uvid': newvoyageuvid
        }
        response=requests.get(url + sub, params=parameters, cert=vis_cert, verify=trustchain)

        if response.status_code == 200:
            report='''
VIS002sheet.write(VIS_002_1_2_row, VIS_002_1_2_col, "PASS", boldcenter)
'''
        else:
            report='''
VIS002sheet.write(VIS_002_1_2_row, VIS_002_1_2_col, "FAIL", boldcenter)
VIS002sheet.write(VIS_002_1_2_row, VIS_002_1_2_col - 1, "''' + response.reason + '", normal)'
        f = open('../create_worksheet.py', 'a')
        f.write(report)
        f.close()

        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_002_9_3(self):
        """
        VIS-002-1-3 - VIS-1 : Publish voyage plan with chosen UVID and routeStatus=7


        """
        sub='/voyagePlans'
        parameters={
            'uvid': newvoyageuvid,
            'routeStatus': '7'
        }
        payload={'route': voyageplan}
        response=requests.post(url + sub, params=parameters, json=payload, cert=vis_cert, verify=trustchain)

        if response.status_code == 200:
            report='''
VIS002sheet.write(VIS_002_1_3_row, VIS_002_1_3_col, "PASS", boldcenter)
'''
        else:
            report='''
VIS002sheet.write(VIS_002_1_3_row, VIS_002_1_3_col, "FAIL", boldcenter)
VIS002sheet.write(VIS_002_1_3_row, VIS_002_1_3_col - 1, "''' + response.reason + '", normal)'
        f = open('../create_worksheet.py', 'a')
        f.write(report)
        f.close()

        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_002_9_4(self):
        """
        VIS-002-1-4 - VIS-2 : Request voyage plans from VIS-1

        
        """
        sub='/voyagePlans'
        parameters={
            'uvid': newvoyageuvid
        }
        response=requests.get(url + sub, params=parameters, cert=vis_cert, verify=trustchain)

        if response.status_code == 200:
            report='''
VIS002sheet.write(VIS_002_1_4_row, VIS_002_1_4_col, "PASS", boldcenter)
'''
        else:
            report='''
VIS002sheet.write(VIS_002_1_4_row, VIS_002_1_4_col, "FAIL", boldcenter)
VIS002sheet.write(VIS_002_1_4_row, VIS_002_1_4_col - 1, "''' + response.reason + '", normal)'
        f = open('../create_worksheet.py', 'a')
        f.write(report)
        f.close()

        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_002_9_5(self):
        """
        VIS-002-1-5 - VIS-1 : Publish voyage plan with new UVID for the same ship and routeStatus=7


        """
        sub='/voyagePlans'
        parameters={
            'uvid': newvoyageuvid2,
            'routeStatus': '7'
        }
        payload={'route': voyageplan}
        response=requests.post(url + sub, params=parameters, json=payload, cert=vis_cert, verify=trustchain)

        if response.status_code == 200:
            report='''
VIS002sheet.write(VIS_002_1_5_row, VIS_002_1_5_col, "PASS", boldcenter)
'''
        else:
            report='''
VIS002sheet.write(VIS_002_1_5_row, VIS_002_1_5_col, "FAIL", boldcenter)
VIS002sheet.write(VIS_002_1_5_row, VIS_002_1_5_col - 1, "''' + response.reason + '", normal)'
        f = open('../create_worksheet.py', 'a')
        f.write(report)
        f.close()

        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_002_9_6(self):
        """
        VIS-002-1-6 - VIS-2 : Request voyage plans from VIS-1

        
        """
        sub='/voyagePlans'
        parameters={
            'uvid': newvoyageuvid2
        }
        response=requests.get(url + sub, params=parameters, cert=vis_cert, verify=trustchain)

        if response.status_code == 200:
            report='''
VIS002sheet.write(VIS_002_1_6_row, VIS_002_1_6_col, "PASS", boldcenter)
'''
        else:
            report='''
VIS002sheet.write(VIS_002_1_6_row, VIS_002_1_6_col, "FAIL", boldcenter)
VIS002sheet.write(VIS_002_1_6_row, VIS_002_1_6_col - 1, "''' + response.reason + '", normal)'
        f = open('../create_worksheet.py', 'a')
        f.write(report)
        f.close()

        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_002_9_7(self):
        """
        VIS-002-1-7 - VIS-1 : Publish voyage plan with new UVID for another ship and routeStatus=7


        """
        sub='/voyagePlans'
        parameters={
            'uvid': newvoyageuvid2,
            'routeStatus': '7'
        }
        payload={'route': voyageplan}
        response=requests.post(url + sub, params=parameters, json=payload, cert=vis_cert, verify=trustchain)

        if response.status_code == 200:
            report='''
VIS002sheet.write(VIS_002_1_7_row, VIS_002_1_7_col, "PASS", boldcenter)
'''
        else:
            report='''
VIS002sheet.write(VIS_002_1_7_row, VIS_002_1_7_col, "FAIL", boldcenter)
VIS002sheet.write(VIS_002_1_7_row, VIS_002_1_7_col - 1, "''' + response.reason + '", normal)'
        f = open('../create_worksheet.py', 'a')
        f.write(report)
        f.close()

        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_002_9_8(self):
        """
        VIS-002-1-8 - VIS-2 : Request voyage plans from VIS-1

        
        """
        sub='/voyagePlans'
        response=requests.get(url + sub, cert=vis_cert, verify=trustchain)

        if response.status_code == 400:
            report='''
VIS002sheet.write(VIS_002_1_8_row, VIS_002_1_8_col, "PASS", boldcenter)
'''
        else:
            report='''
VIS002sheet.write(VIS_002_1_8_row, VIS_002_1_8_col, "FAIL", boldcenter)
VIS002sheet.write(VIS_002_1_8_row, VIS_002_1_8_col - 1, "''' + response.reason + '", normal)'
        f = open('../create_worksheet.py', 'a')
        f.write(report)
        f.close()

        self.assert200(response, "Response body is : " + response.text)


if __name__ == '__main__':
    unittest.main()


