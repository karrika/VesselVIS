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


class TestVIS_002_1(BaseTestCase):
    """ VIS-002 tests """

    def setUp(self):
        f = open('../VIS-1/export/' + voyageuvid + '.acl', 'w')
        data=[ vis_uvid ]
        f.write(json.dumps(data))
        f.close()
        f = open('../VIS-1/export/all.acl', 'w')
        data=[ vis_uvid ]
        f.write(json.dumps(data))
        f.close()
        pass

    def tearDown(self):
        pass

    def test_VIS_002_9_7(self):
        """
        VIS-002-1-7 - VIS-2 : Request voyage plans from VIS-1

        
        """
        sub='/voyagePlans'
        parameters={
            'uvid': newvoyageuvid2
        }
        response=requests.get(url + sub, params=parameters, cert=vis_cert, verify=trustchain)
        self.assert200(response, "Response body is : " + response.text)

    @unittest.skip('Multiple vessels through one instance is not supported.')
    def test_VIS_002_9_8(self):
        """
        VIS-002-1-8 - VIS-1 : Publish voyage plan with new UVID for another ship and routeStatus=7


        """
        sub='/voyagePlans'
        parameters={
            'uvid': newvoyageuvid2,
            'routeStatus': '7'
        }
        payload={'route': voyageplan}
        response=requests.post(url + sub, params=parameters, json=payload, cert=vis_cert, verify=trustchain)
        self.assert200(response, "Response body is : " + response.text)

    @unittest.skip('Multiple vessels through one instance is not supported.')
    def test_VIS_002_9_9(self):
        """
        VIS-002-1-9 - VIS-2 : Request voyage plans from VIS-1

        
        """
        sub='/voyagePlans'
        response=requests.get(url + sub, cert=vis_cert, verify=trustchain)
        self.assert200(response, "Response body is : " + response.text)


if __name__ == '__main__':
    unittest.main()


