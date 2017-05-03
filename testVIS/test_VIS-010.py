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

class TestVIS_010(BaseTestCase):
    """ VIS-010 tests """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_VIS_010_0_01(self):
        """
        VIS-010-1 - Find keyword ROS

        
        """
        response = hostsettings.search('keywords:ROS')
        hostsettings.reportrow('VIS010sheet', 'VIS_010_01_row', 'VIS_010_01_col',
            response.status_code == 200, response.reason)
        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_010_0_02(self):
        """
        VIS-010-2 - Find keyword ROS+SSPA

        
        """
        response = hostsettings.search('keywords:ROS AND keywords:SSPA')
        hostsettings.reportrow('VIS010sheet', 'VIS_010_02_row', 'VIS_010_02_col',
            response.status_code == 200, response.reason)
        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_010_0_03(self):
        """
        VIS-010-3 - Find keyword RO

        
        """
        response = hostsettings.search('keywords:RO')
        hostsettings.reportrow('VIS010sheet', 'VIS_010_03_row', 'VIS_010_03_col',
            response.status_code == 200, response.reason)
        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_010_0_04(self):
        """
        VIS-010-4 - Find keyword ros

        
        """
        response = hostsettings.search('keywords:ros')
        hostsettings.reportrow('VIS010sheet', 'VIS_010_04_row', 'VIS_010_04_col',
            response.status_code == 200, response.reason)
        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_010_0_05(self):
        """
        VIS-010-5 - Find keyword voyage

        
        """
        response = hostsettings.search('keywords:voyage')
        hostsettings.reportrow('VIS010sheet', 'VIS_010_05_row', 'VIS_010_05_col',
            response.status_code == 200, response.reason)
        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_010_0_06(self):
        """
        VIS-010-6 - Find keyword service

        
        """
        response = hostsettings.search('keywords:service')
        hostsettings.reportrow('VIS010sheet', 'VIS_010_06_row', 'VIS_010_06_col',
            response.status_code == 200, response.reason)
        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_010_0_07(self):
        """
        VIS-010-7 - Find IMO 8719188

        
        """
        response = hostsettings.search('imo:8719188')
        hostsettings.reportrow('VIS010sheet', 'VIS_010_07_row', 'VIS_010_07_col',
            response.status_code == 200, response.reason)
        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_010_0_08(self):
        """
        VIS-010-8 - Find ship by MMSI

        
        """
        response = hostsettings.search('mmsi')
        hostsettings.reportrow('VIS010sheet', 'VIS_010_08_row', 'VIS_010_08_col',
            response.status_code == 200, response.reason)
        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_010_0_09(self):
        """
        VIS-010-9 - Find ship by serviceType

        
        """
        response = hostsettings.search('serviceType')
        hostsettings.reportrow('VIS010sheet', 'VIS_010_09_row', 'VIS_010_09_col',
            response.status_code == 200, response.reason)
        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_010_0_10(self):
        """
        VIS-010-10 - Find IMO 8719188 + Keyword ROS

        
        """
        response = hostsettings.search('imo:8719188 AND keywords:ROS')
        hostsettings.reportrow('VIS010sheet', 'VIS_010_10_row', 'VIS_010_10_col',
            response.status_code == 200, response.reason)
        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_010_0_11(self):
        """
        VIS-010-11 - Find Route optimisation service to consume

        
        """
        response = hostsettings.search('serviceType AND ROS')
        hostsettings.reportrow('VIS010sheet', 'VIS_010_11_row', 'VIS_010_11_col',
            response.status_code == 200, response.reason)
        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_010_0_12(self):
        """
        VIS-010-12 - Find Route check service to consume

        
        """
        response = hostsettings.search('serviceType AND RCS')
        hostsettings.reportrow('VIS010sheet', 'VIS_010_12_row', 'VIS_010_12_col',
            response.status_code == 200, response.reason)
        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_010_0_13(self):
        """
        VIS-010-13 - Find Enhanced monitoring service to consume

        
        """
        response = hostsettings.search('serviceType AND EMS')
        hostsettings.reportrow('VIS010sheet', 'VIS_010_13_row', 'VIS_010_13_col',
            response.status_code == 200, response.reason)
        self.assert200(response, "Response body is : " + response.text)


if __name__ == '__main__':
    unittest.main()


