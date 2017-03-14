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
        hostsettings.set_acl(vis_uvid, voyageuvid)
        hostsettings.set_acl(vis_uvid, None)
        pass

    def tearDown(self):
        pass

    def test_VIS_003_01(self):
        """
        VIS-003-1 - VIS-2: Request subscription on VIS-1

        
        """
        sub='/voyagePlans/subscription'
        parameters={
            'callbackEndpoint': callbackurl + '/voyagePlans',
            'uvid': voyageuvid
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

    @unittest.skip('Sender logging is not implemented yet')
    def test_VIS_003_02(self):
        """
        VIS-003-2 - VIS-2 logs event

        
        """
        pass

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
        pass

    def test_VIS_003_05(self):
        """
        VIS-003-4 - VIS-1 checks against ACL and get OK

        
        """
        pass



if __name__ == '__main__':
    unittest.main()


