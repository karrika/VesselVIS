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


class TestVIS_005(BaseTestCase):
    """ VIS-005 tests """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_VIS_005_0_1(self):
        """
        VIS-005-1 - Prepare VIS-1 for test

        
        """
        hostsettings.rm_uvid(newvoyageuvid)
        pass

    def test_VIS_005_0_2(self):
        """
        VIS-005-2 - Select voyage plan in VIS-2 and send (upload) the voyage plan to VIS-1,
                    no ACK requested, no callback expected

        
        """
        sub='/voyagePlans'
        parameters={
            'uvid': newvoyageuvid,
            'routeStatus': '7'
        }
        payload={'route': voyageplan}
        response=requests.post(url + sub, params=parameters, json=payload, cert=vis_cert, verify=trustchain)
        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_005_0_3(self):
        """
        VIS-005-3 - STM Module retrieves messages from VIS-1

        
        """
        self.assertTrue(hostsettings.uvid_exists(newvoyageuvid))

    def test_VIS_005_1(self):
        """
        VIS-005-1 - STM Module retrieves messages from VIS-1 with ack

        
        """
        sub='/voyagePlans'
        parameters={
            'uvid': newvoyageuvid,
            'routeStatus': '7'
        }
        payload={'route': voyageplan}
        response=requests.post(url + sub, params=parameters, json=payload, cert=vis_cert, verify=trustchain)
        self.assert200(response, "Response body is : " + response.text)

    @unittest.skip('Implementing check for received payload is still missing.')
    def test_VIS_005_4(self):
        """
        VIS-005-4 - STM Module retrieves messages from VIS-1 with ack timeout?

        
        """
        sub='/voyagePlans'
        parameters={
            'uvid': newvoyageuvid,
            'routeStatus': '7'
        }
        payload={'route': voyageplan}
        response=requests.post(url + sub, params=parameters, json=payload, cert=vis_cert, verify=trustchain)
        self.assert200(response, "Response body is : " + response.text)



if __name__ == '__main__':
    unittest.main()


