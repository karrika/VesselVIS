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
vis1_uvid=hostsettings.vis1_uvid
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

    @unittest.skip('The service registry search is not implemented yet.')
    def test_VIS_005_1_1(self):
        """
        VIS-005-1-1 - In VIS-2, search for VIS with MMSI=12345678

        
        """

    def test_VIS_005_1_2(self):
        """
        VIS-005-1-2 - In VIS-2, select voyage plan and send (upload) the voyage plan to VIS-1 with ACKendpoint

        
        """
        sub='/voyagePlans'
        parameters={
            'uvid': newvoyageuvid,
            'routeStatus': '1',
            'deliveryAckEndPoint': 'https://localhost:8002'
        }
        payload={'route': voyageplan}
        response=requests.post(url + sub, params=parameters, json=payload, cert=vis_cert, verify=trustchain)
        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_005_1_3(self):
        """
        VIS-005-1-3 - STM Module retrieves messages from VIS-1

        
        """
        sub='/acknowledgement'
        deliveryAckEndPoint = 'https://localhost:8002'
        payload={
            'ackResult': 'Ok',
            'fromId': vis1_uvid,
            'fromName': 'VIS-1',
            'id': newvoyageuvid + ':ack',
            'referenceId': newvoyageuvid,
            'timeOfDelivery': '2017-01-27T12:00:00Z',
            'toId': vis2_uvid,
            'toName': 'VIS-2'
        }
        response=requests.post(deliveryAckEndPoint + sub, json=payload, cert=vis_cert, verify=trustchain)
        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_005_2_1(self):
        """
        VIS-005-2-2 - In VIS-2, select voyage plan and send (upload) the voyage plan to VIS-1 with ACKendpoint that does not respond

        
        """
        sub='/voyagePlans'
        parameters={
            'uvid': newvoyageuvid,
            'routeStatus': '1',
            'deliveryAckEndPoint': 'https://localhost'
        }
        payload={'route': voyageplan}
        response=requests.post(url + sub, params=parameters, json=payload, cert=vis_cert, verify=trustchain)
        self.assert200(response, "Response body is : " + response.text)

    @unittest.skip('Implement user timeout nagging feature when ack is missing')
    def test_VIS_005_2_2(self):
        """
        VIS-005-1-3 - STM Module retrieves messages from VIS-1

        
        """
        pass



if __name__ == '__main__':
    unittest.main()


