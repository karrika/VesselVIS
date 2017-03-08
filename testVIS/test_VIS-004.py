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


class TestVIS_004(BaseTestCase):
    """ VIS-004 tests """

    def setUp(self):
        hostsettings.set_acl(vis_uvid, voyageuvid)
        hostsettings.set_acl(vis_uvid, None)
        pass

    def tearDown(self):
        pass

    def test_VIS_004_1(self):
        """
        VIS-004-1 - VIS-2: Request subscription on VIS-1

        
        """
        sub='/voyagePlans/subscription'
        parameters={
            'callbackEndpoint': callbackurl + '/voyagePlans',
            'uvid': voyageuvid
        }
        payload={}
        response=requests.delete(url + sub, params=parameters, json=payload, cert=vis_cert, verify=trustchain)
        self.assert200(response, "Response body is : " + response.text)

    @unittest.skip('Testing subscription with receiving the packet requires two instances. Not set up yet.')
    def test_VIS_004_2(self):
        """
        VIS-004-2 - VIS-1: Publish voyage plan to VIS-1 instance

        
        """
        sub='/voyagePlans/subscription'
        parameters={
            'callbackEndpoint': callbackurl + '/voyagePlans',
            'uvid': voyageuvid
        }
        payload={}
        response=requests.delete(url + sub, params=parameters, json=payload, cert=vis_cert, verify=trustchain)
        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_004_3(self):
        """
        VIS-004-3 - VIS-2: Request remove of subscription to voyage plan from VIS-1

        
        """
        sub='/voyagePlans/subscription'
        parameters={
            'callbackEndpoint': callbackurl + '/voyagePlans',
            'uvid': voyageuvid
        }
        payload={}
        response=requests.delete(url + sub, params=parameters, json=payload, cert=vis_cert, verify=trustchain)
        self.assert200(response, "Response body is : " + response.text)

    @unittest.skip('Testing subscription with receiving the packet requires two instances. Not set up yet.')
    def test_VIS_004_4(self):
        """
        VIS-004-4 - VIS-1: Publish voyage plan to VIS-1 instance

        
        """
        sub='/voyagePlans/subscription'
        parameters={
            'callbackEndpoint': callbackurl + '/voyagePlans',
            'uvid': voyageuvid
        }
        payload={}
        response=requests.delete(url + sub, params=parameters, json=payload, cert=vis_cert, verify=trustchain)
        self.assert200(response, "Response body is : " + response.text)


if __name__ == '__main__':
    unittest.main()


