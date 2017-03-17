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

voyageplan='''<?xml version="1.0"?>
<route version="1.1" 
  xmlns:xsd="http://www.w3.org/2001/XMLSchema"
  xmlns="http://www.cirm.org/RTZ/1/1">
  <routeInfo routeStatus="1" vesselVoyage="urn:mrn:stm:voyage:id:new:plan" routeName="HAN-VIS" validityPeriodStart="2017-02-15T10:00:00Z" validityPeriodStop="2017-02-16T10:00:00Z" optimizationMethod="Time table">
  </routeInfo>
  <waypoints>
    <waypoint id="1" name="Hango" radius="0.800000">
      <position lat="59.811700" lon="22.935567"/>
    </waypoint>
    <waypoint id="2" name="" radius="0.800000">
      <position lat="59.758817" lon="23.020267"/>
      <leg portsideXTD="0.099892" starboardXTD="0.099892" safetyContour="30" geometryType="Loxodrome" speedMax="7.000000" draughtForward="10.000000" draughtAft="10.000000" staticUKC="30.000000"/>
    </waypoint>
  </waypoints>
  <schedules>
    <schedule id="1">
      <calculated>
        <scheduleElement etd="2017-02-15T10:00:00Z" waypointId="1"/>
        <scheduleElement eta="2017-02-15T10:35:00Z" waypointId="2" speed="7.000000"/>
      </calculated>
    </schedule>
  </schedules>
</route>
'''

class TestVIS_005(BaseTestCase):
    """ VIS-005 tests """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_VIS_005_0_01(self):
        """
        VIS-005-1 - VIS-2: Select voyage plan and send (upload) the voyage plan to VIS-1, no ACK requested, no callback expected

        
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
VIS005sheet.write(VIS_005_01_row, VIS_005_01_col, "PASS", boldcenter)
VIS005sheet.write(VIS_005_01_row, VIS_005_01_col - 1, "''' + response.reason + '", normal)'
        else:
            report='''
VIS005sheet.write(VIS_005_01_row, VIS_005_01_col, "FAIL", boldcenter)
VIS005sheet.write(VIS_005_01_row, VIS_005_01_col - 1, "''' + response.reason + '", normal)'
        f = open('../create_worksheet.py', 'a')
        f.write(report)
        f.close()

        self.assert200(response, "Response body is : " + response.text)

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

        if response.status_code == 200:
            report='''
VIS005sheet.write(VIS_005_02_row, VIS_005_02_col, "PASS", boldcenter)
VIS005sheet.write(VIS_005_02_row, VIS_005_02_col - 1, "''' + response.reason + '", normal)'
        else:
            report='''
VIS005sheet.write(VIS_005_02_row, VIS_005_02_col, "FAIL", boldcenter)
VIS005sheet.write(VIS_005_02_row, VIS_005_02_col - 1, "''' + response.reason + '", normal)'
        f = open('../create_worksheet.py', 'a')
        f.write(report)
        f.close()

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

        if response.status_code == 200:
            report='''
VIS005sheet.write(VIS_005_1_2_row, VIS_005_1_2_col, "PASS", boldcenter)
VIS005sheet.write(VIS_005_1_2_row, VIS_005_1_2_col - 1, "''' + response.reason + '", normal)'
        else:
            report='''
VIS005sheet.write(VIS_005_1_2_row, VIS_005_1_2_col, "FAIL", boldcenter)
VIS005sheet.write(VIS_005_1_2_row, VIS_005_1_2_col - 1, "''' + response.reason + '", normal)'
        f = open('../create_worksheet.py', 'a')
        f.write(report)
        f.close()

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

        if response.status_code == 200:
            report='''
VIS005sheet.write(VIS_005_1_3_row, VIS_005_1_3_col, "PASS", boldcenter)
VIS005sheet.write(VIS_005_1_3_row, VIS_005_1_3_col - 1, "''' + response.reason + '", normal)'
        else:
            report='''
VIS005sheet.write(VIS_005_1_3_row, VIS_005_1_3_col, "FAIL", boldcenter)
VIS005sheet.write(VIS_005_1_3_row, VIS_005_1_3_col - 1, "''' + response.reason + '", normal)'
        f = open('../create_worksheet.py', 'a')
        f.write(report)
        f.close()

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


