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


class TestVIS_002(BaseTestCase):
    """ VIS-002 tests """

    def setUp(self):
        pass

    def tearDown(self):
        pass


    def test_VIS_002_00(self):
        """
        VIS-002-0 - Preparation:Organisation for VIS-2 authorized to exactly one published voyage plan with routestatus=7 and chosen UVID

        
        """
        f = open('../VIS-1/export/' + voyageuvid + '.acl', 'w')
        data=[ vis_uvid ]
        f.write(json.dumps(data))
        f.close()
        f = open('../VIS-1/export/all.acl', 'w')
        data=[ vis_uvid ]
        f.write(json.dumps(data))
        f.close()

        report='''
VIS002sheet.write(VIS_002_00_row, VIS_002_00_col, "PASS", boldcenter)
'''
        f = open('../create_worksheet.py', 'a')
        f.write(report)
        f.close()
        pass

    def test_VIS_002_1(self):
        """
        VIS-002-1 - VIS-2 request voyage plan from VIS-1, no specific UVID or status, hence no parameters given

        
        """
        sub='/voyagePlans'
        response=requests.get(url + sub, cert=vis_cert, verify=trustchain)

        if response.status_code == 200:
            report='''
VIS002sheet.write(VIS_002_01_row, VIS_002_01_col, "PASS", boldcenter)
'''
        else:
            report='''
VIS002sheet.write(VIS_002_01_row, VIS_002_01_col, "FAIL", boldcenter)
'''
        f = open('../create_worksheet.py', 'a')
        f.write(report)
        f.close()

        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_002_2(self):
        """
        VIS-002-2 - VIS-2 request voyage plan with chosen UVID from VIS-1, no specific status

        
        """
        sub='/voyagePlans'
        parameters={
            'uvid': voyageuvid
        }
        response=requests.get(url + sub, params=parameters, cert=vis_cert, verify=trustchain)

        if response.status_code == 200:
            report='''
VIS002sheet.write(VIS_002_02_row, VIS_002_02_col, "PASS", boldcenter)
'''
        else:
            report='''
VIS002sheet.write(VIS_002_02_row, VIS_002_02_col, "FAIL", boldcenter)
'''
        f = open('../create_worksheet.py', 'a')
        f.write(report)
        f.close()

        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_002_3(self):
        """
        VIS-002-3 - VIS-2 request voyage plan with routeStatus= 7 from VIS-1, no specific UVID

        
        """
        sub='/voyagePlans'
        parameters={
            'routeStatus': '7'
        }
        response=requests.get(url + sub, params=parameters, cert=vis_cert, verify=trustchain)

        if response.status_code == 200:
            report='''
VIS002sheet.write(VIS_002_03_row, VIS_002_03_col, "PASS", boldcenter)
'''
        else:
            report='''
VIS002sheet.write(VIS_002_03_row, VIS_002_03_col, "FAIL", boldcenter)
'''
        f = open('../create_worksheet.py', 'a')
        f.write(report)
        f.close()

        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_002_4(self):
        """
        VIS-002-4 - VIS-2 request voyage plan with chosen UVID and routeStatus=7 from VIS-1

        
        """
        sub='/voyagePlans'
        parameters={
            'uvid': voyageuvid,
            'routeStatus': '7'
        }
        response=requests.get(url + sub, params=parameters, cert=vis_cert, verify=trustchain)

        if response.status_code == 200:
            report='''
VIS002sheet.write(VIS_002_04_row, VIS_002_04_col, "PASS", boldcenter)
'''
        else:
            report='''
VIS002sheet.write(VIS_002_04_row, VIS_002_04_col, "FAIL", boldcenter)
'''
        f = open('../create_worksheet.py', 'a')
        f.write(report)
        f.close()

        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_002_5(self):
        """
        VIS-002-5 - VIS-2 request voyage plan with another (non published) UVID and routeStatus=7 from VIS-1

        
        """
        sub='/voyagePlans'
        parameters={
            'uvid': 'urn:mrn:stm:voyage:id:not:found',
            'routeStatus': '7'
        }
        response=requests.get(url + sub, params=parameters, cert=vis_cert, verify=trustchain)

        if response.status_code == 404:
            report='''
VIS002sheet.write(VIS_002_05_row, VIS_002_05_col, "PASS", boldcenter)
'''
        else:
            report='''
VIS002sheet.write(VIS_002_05_row, VIS_002_05_col, "FAIL", boldcenter)
'''
        f = open('../create_worksheet.py', 'a')
        f.write(report)
        f.close()

        self.assert404(response, "Response body is : " + response.text)

    def test_VIS_002_6(self):
        """
        VIS-002-6 - VIS-2 request voyage plan with chosen UVID and routeStatus=6 from VIS-1

        
        """
        sub='/voyagePlans'
        parameters={
            'uvid': voyageuvid,
            'routeStatus': '6'
        }
        response=requests.get(url + sub, params=parameters, cert=vis_cert, verify=trustchain)

        if response.status_code == 404:
            report='''
VIS002sheet.write(VIS_002_06_row, VIS_002_06_col, "PASS", boldcenter)
'''
        else:
            report='''
VIS002sheet.write(VIS_002_06_row, VIS_002_06_col, "FAIL", boldcenter)
'''
        f = open('../create_worksheet.py', 'a')
        f.write(report)
        f.close()

        self.assert404(response, "Response body is : " + response.text)

    def test_VIS_002_7(self):
        """
        VIS-002-7 - VIS-2 request voyage plan with another (non published) UVID from VIS-1, no specific status

        
        """
        sub='/voyagePlans'
        parameters={
            'uvid': 'urn:mrn:stm:voyage:id:not:found'
        }
        response=requests.get(url + sub, params=parameters, cert=vis_cert, verify=trustchain)

        if response.status_code == 404:
            report='''
VIS002sheet.write(VIS_002_07_row, VIS_002_07_col, "PASS", boldcenter)
'''
        else:
            report='''
VIS002sheet.write(VIS_002_07_row, VIS_002_07_col, "FAIL", boldcenter)
'''
        f = open('../create_worksheet.py', 'a')
        f.write(report)
        f.close()

        self.assert404(response, "Response body is : " + response.text)

    def test_VIS_002_8(self):
        """
        VIS-002-8 - VIS-2 request voyage plan with routeStatus= 6 (non published)  from VIS-1, no specific UVID

        
        """
        sub='/voyagePlans'
        parameters={
            'routeStatus': '6'
        }
        response=requests.get(url + sub, params=parameters, cert=vis_cert, verify=trustchain)

        if response.status_code == 404:
            report='''
VIS002sheet.write(VIS_002_08_row, VIS_002_08_col, "PASS", boldcenter)
'''
        else:
            report='''
VIS002sheet.write(VIS_002_08_row, VIS_002_08_col, "FAIL", boldcenter)
'''
        f = open('../create_worksheet.py', 'a')
        f.write(report)
        f.close()

        self.assert404(response, "Response body is : " + response.text)


if __name__ == '__main__':
    unittest.main()


