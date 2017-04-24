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

url="https://sr-test.maritimecloud.net"
callbackurl=hostsettings.callbackurl
vis_uvid=hostsettings.vis_uvid
vis1_uvid=hostsettings.vis1_uvid
vis2_uvid=hostsettings.vis2_uvid
with open('accesstoken', 'r') as f:
    ACCESSTOKEN = f.read()

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
        sub='/api/_searchKeywords/serviceInstance'
        headers={
            'Authorization' : 'Bearer ' + ACCESSTOKEN[0:len(ACCESSTOKEN)-1],
            'Accept' : 'application/json'
        }
        parameters={
            'query' : 'ROS'
        }
        response=requests.get(url + sub, headers=headers, params=parameters, cert=vis_cert)
        print(response.text)

        if response.status_code == 200:
            report='''
VIS010sheet.write(VIS_010_01_row, VIS_010_01_col, "PASS", boldcenter)
VIS010sheet.write(VIS_010_01_row, VIS_010_01_col - 1, "''' + response.reason + '", normal)'
        else:
            report='''
VIS010sheet.write(VIS_010_01_row, VIS_010_01_col, "FAIL", boldcenter)
VIS010sheet.write(VIS_010_01_row, VIS_010_01_col - 1, "''' + response.reason + '", normal)'
        f = open('../create_worksheet.py', 'a')
        f.write(report)
        f.close()

        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_010_0_02(self):
        """
        VIS-010-2 - Find keyword ROS+SSPA

        
        """
        sub='/api/_searchKeywords/serviceInstance'
        headers={
            'Authorization' : 'Bearer ' + ACCESSTOKEN[0:len(ACCESSTOKEN)-1],
            'Accept' : 'application/json'
        }
        parameters={
            'query' : 'ROS+SSPA'
        }
        response=requests.get(url + sub, headers=headers, params=parameters, cert=vis_cert)
        print(response.text)

        if response.status_code == 200:
            report='''
VIS010sheet.write(VIS_010_02_row, VIS_010_02_col, "PASS", boldcenter)
VIS010sheet.write(VIS_010_02_row, VIS_010_02_col - 1, "''' + response.reason + '", normal)'
        else:
            report='''
VIS010sheet.write(VIS_010_02_row, VIS_010_02_col, "FAIL", boldcenter)
VIS010sheet.write(VIS_010_02_row, VIS_010_02_col - 1, "''' + response.reason + '", normal)'
        f = open('../create_worksheet.py', 'a')
        f.write(report)
        f.close()

        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_010_0_03(self):
        """
        VIS-010-3 - Find keyword RO

        
        """
        sub='/api/_searchKeywords/serviceInstance'
        headers={
            'Authorization' : 'Bearer ' + ACCESSTOKEN[0:len(ACCESSTOKEN)-1],
            'Accept' : 'application/json'
        }
        parameters={
            'query' : 'RO'
        }
        response=requests.get(url + sub, headers=headers, params=parameters, cert=vis_cert)
        print(response.text)

        if response.status_code == 200:
            report='''
VIS010sheet.write(VIS_010_03_row, VIS_010_03_col, "PASS", boldcenter)
VIS010sheet.write(VIS_010_03_row, VIS_010_03_col - 1, "''' + response.reason + '", normal)'
        else:
            report='''
VIS010sheet.write(VIS_010_03_row, VIS_010_03_col, "FAIL", boldcenter)
VIS010sheet.write(VIS_010_03_row, VIS_010_03_col - 1, "''' + response.reason + '", normal)'
        f = open('../create_worksheet.py', 'a')
        f.write(report)
        f.close()

        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_010_0_04(self):
        """
        VIS-010-4 - Find keyword ros

        
        """
        sub='/api/_searchKeywords/serviceInstance'
        headers={
            'Authorization' : 'Bearer ' + ACCESSTOKEN[0:len(ACCESSTOKEN)-1],
            'Accept' : 'application/json'
        }
        parameters={
            'query' : 'ros'
        }
        response=requests.get(url + sub, headers=headers, params=parameters, cert=vis_cert)
        print(response.text)

        if response.status_code == 200:
            report='''
VIS010sheet.write(VIS_010_04_row, VIS_010_04_col, "PASS", boldcenter)
VIS010sheet.write(VIS_010_04_row, VIS_010_04_col - 1, "''' + response.reason + '", normal)'
        else:
            report='''
VIS010sheet.write(VIS_010_04_row, VIS_010_04_col, "FAIL", boldcenter)
VIS010sheet.write(VIS_010_04_row, VIS_010_04_col - 1, "''' + response.reason + '", normal)'
        f = open('../create_worksheet.py', 'a')
        f.write(report)
        f.close()

        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_010_0_05(self):
        """
        VIS-010-5 - Find keyword voyage

        
        """
        sub='/api/_searchKeywords/serviceInstance'
        headers={
            'Authorization' : 'Bearer ' + ACCESSTOKEN[0:len(ACCESSTOKEN)-1],
            'Accept' : 'application/json'
        }
        parameters={
            'query' : 'voyage'
        }
        response=requests.get(url + sub, headers=headers, params=parameters, cert=vis_cert)
        print(response.text)

        if response.status_code == 200:
            report='''
VIS010sheet.write(VIS_010_05_row, VIS_010_05_col, "PASS", boldcenter)
VIS010sheet.write(VIS_010_05_row, VIS_010_05_col - 1, "''' + response.reason + '", normal)'
        else:
            report='''
VIS010sheet.write(VIS_010_05_row, VIS_010_05_col, "FAIL", boldcenter)
VIS010sheet.write(VIS_010_05_row, VIS_010_05_col - 1, "''' + response.reason + '", normal)'
        f = open('../create_worksheet.py', 'a')
        f.write(report)
        f.close()

        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_010_0_06(self):
        """
        VIS-010-6 - Find keyword service

        
        """
        sub='/api/_searchKeywords/serviceInstance'
        headers={
            'Authorization' : 'Bearer ' + ACCESSTOKEN[0:len(ACCESSTOKEN)-1],
            'Accept' : 'application/json'
        }
        parameters={
            'query' : 'service'
        }
        response=requests.get(url + sub, headers=headers, params=parameters, cert=vis_cert)
        print(response.text)

        if response.status_code == 200:
            report='''
VIS010sheet.write(VIS_010_06_row, VIS_010_06_col, "PASS", boldcenter)
VIS010sheet.write(VIS_010_06_row, VIS_010_06_col - 1, "''' + response.reason + '", normal)'
        else:
            report='''
VIS010sheet.write(VIS_010_06_row, VIS_010_06_col, "FAIL", boldcenter)
VIS010sheet.write(VIS_010_06_row, VIS_010_06_col - 1, "''' + response.reason + '", normal)'
        f = open('../create_worksheet.py', 'a')
        f.write(report)
        f.close()

        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_010_0_07(self):
        """
        VIS-010-7 - Find IMO 8719188

        
        """
        sub='/api/_search/serviceInstance'
        headers={
            'Authorization' : 'Bearer ' + ACCESSTOKEN[0:len(ACCESSTOKEN)-1],
            'Accept' : 'application/json'
        }
        parameters={
            'query' : '+IMO +8719188'
        }
        response=requests.get(url + sub, headers=headers, params=parameters, cert=vis_cert)
        print(response.text)

        if response.status_code == 200:
            report='''
VIS010sheet.write(VIS_010_07_row, VIS_010_07_col, "PASS", boldcenter)
VIS010sheet.write(VIS_010_07_row, VIS_010_07_col - 1, "''' + response.reason + '", normal)'
        else:
            report='''
VIS010sheet.write(VIS_010_07_row, VIS_010_07_col, "FAIL", boldcenter)
VIS010sheet.write(VIS_010_07_row, VIS_010_07_col - 1, "''' + response.reason + '", normal)'
        f = open('../create_worksheet.py', 'a')
        f.write(report)
        f.close()

        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_010_0_08(self):
        """
        VIS-010-8 - Find ship by MMSI

        
        """
        sub='/api/_search/serviceInstance'
        headers={
            'Authorization' : 'Bearer ' + ACCESSTOKEN[0:len(ACCESSTOKEN)-1],
            'Accept' : 'application/json'
        }
        parameters={
            'query' : '+MMSI'
        }
        response=requests.get(url + sub, headers=headers, params=parameters, cert=vis_cert)
        print(response.text)

        if response.status_code == 200:
            report='''
VIS010sheet.write(VIS_010_08_row, VIS_010_08_col, "PASS", boldcenter)
VIS010sheet.write(VIS_010_08_row, VIS_010_08_col - 1, "''' + response.reason + '", normal)'
        else:
            report='''
VIS010sheet.write(VIS_010_08_row, VIS_010_08_col, "FAIL", boldcenter)
VIS010sheet.write(VIS_010_08_row, VIS_010_08_col - 1, "''' + response.reason + '", normal)'
        f = open('../create_worksheet.py', 'a')
        f.write(report)
        f.close()

        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_010_0_09(self):
        """
        VIS-010-9 - Find ship by serviceType

        
        """
        sub='/api/_search/serviceInstance'
        headers={
            'Authorization' : 'Bearer ' + ACCESSTOKEN[0:len(ACCESSTOKEN)-1],
            'Accept' : 'application/json'
        }
        parameters={
            'query' : '+serviceType'
        }
        response=requests.get(url + sub, headers=headers, params=parameters, cert=vis_cert)
        print(response.text)

        if response.status_code == 200:
            report='''
VIS010sheet.write(VIS_010_09_row, VIS_010_09_col, "PASS", boldcenter)
VIS010sheet.write(VIS_010_09_row, VIS_010_09_col - 1, "''' + response.reason + '", normal)'
        else:
            report='''
VIS010sheet.write(VIS_010_09_row, VIS_010_09_col, "FAIL", boldcenter)
VIS010sheet.write(VIS_010_09_row, VIS_010_09_col - 1, "''' + response.reason + '", normal)'
        f = open('../create_worksheet.py', 'a')
        f.write(report)
        f.close()

        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_010_0_10(self):
        """
        VIS-010-10 - Find IMO 8719188 + Keyword ROS

        
        """
        sub='/api/_search/serviceInstance'
        headers={
            'Authorization' : 'Bearer ' + ACCESSTOKEN[0:len(ACCESSTOKEN)-1],
            'Accept' : 'application/json'
        }
        parameters={
            'query' : '+IMO +8719188 +ROS'
        }
        response=requests.get(url + sub, headers=headers, params=parameters, cert=vis_cert)
        print(response.text)

        if response.status_code == 200:
            report='''
VIS010sheet.write(VIS_010_10_row, VIS_010_10_col, "PASS", boldcenter)
VIS010sheet.write(VIS_010_10_row, VIS_010_10_col - 1, "''' + response.reason + '", normal)'
        else:
            report='''
VIS010sheet.write(VIS_010_08_row, VIS_010_08_col, "FAIL", boldcenter)
VIS010sheet.write(VIS_010_08_row, VIS_010_08_col - 1, "''' + response.reason + '", normal)'
        f = open('../create_worksheet.py', 'a')
        f.write(report)
        f.close()

        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_010_0_11(self):
        """
        VIS-010-11 - Find Route optimisation service to consume

        
        """
        sub='/api/_search/serviceInstance'
        headers={
            'Authorization' : 'Bearer ' + ACCESSTOKEN[0:len(ACCESSTOKEN)-1],
            'Accept' : 'application/json'
        }
        parameters={
            'query' : '+serviceType +ROS'
        }
        response=requests.get(url + sub, headers=headers, params=parameters, cert=vis_cert)
        print(response.text)

        if response.status_code == 200:
            report='''
VIS010sheet.write(VIS_010_11_row, VIS_010_11_col, "PASS", boldcenter)
VIS010sheet.write(VIS_010_11_row, VIS_010_11_col - 1, "''' + response.reason + '", normal)'
        else:
            report='''
VIS010sheet.write(VIS_010_11_row, VIS_010_11_col, "FAIL", boldcenter)
VIS010sheet.write(VIS_010_11_row, VIS_010_11_col - 1, "''' + response.reason + '", normal)'
        f = open('../create_worksheet.py', 'a')
        f.write(report)
        f.close()

        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_010_0_12(self):
        """
        VIS-010-12 - Find Route check service to consume

        
        """
        sub='/api/_search/serviceInstance'
        headers={
            'Authorization' : 'Bearer ' + ACCESSTOKEN[0:len(ACCESSTOKEN)-1],
            'Accept' : 'application/json'
        }
        parameters={
            'query' : '+serviceType +RCS'
        }
        response=requests.get(url + sub, headers=headers, params=parameters, cert=vis_cert)
        print(response.text)

        if response.status_code == 200:
            report='''
VIS010sheet.write(VIS_010_12_row, VIS_010_12_col, "PASS", boldcenter)
VIS010sheet.write(VIS_010_12_row, VIS_010_12_col - 1, "''' + response.reason + '", normal)'
        else:
            report='''
VIS010sheet.write(VIS_010_12_row, VIS_010_12_col, "FAIL", boldcenter)
VIS010sheet.write(VIS_010_12_row, VIS_010_12_col - 1, "''' + response.reason + '", normal)'
        f = open('../create_worksheet.py', 'a')
        f.write(report)
        f.close()

        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_010_0_13(self):
        """
        VIS-010-13 - Find Enhanced monitoring service to consume

        
        """
        sub='/api/_search/serviceInstance'
        headers={
            'Authorization' : 'Bearer ' + ACCESSTOKEN[0:len(ACCESSTOKEN)-1],
            'Accept' : 'application/json'
        }
        parameters={
            'query' : '+serviceType +EMS'
        }
        response=requests.get(url + sub, headers=headers, params=parameters, cert=vis_cert)
        print(response.text)

        if response.status_code == 200:
            report='''
VIS010sheet.write(VIS_010_13_row, VIS_010_13_col, "PASS", boldcenter)
VIS010sheet.write(VIS_010_13_row, VIS_010_13_col - 1, "''' + response.reason + '", normal)'
        else:
            report='''
VIS010sheet.write(VIS_010_13_row, VIS_010_13_col, "FAIL", boldcenter)
VIS010sheet.write(VIS_010_13_row, VIS_010_13_col - 1, "''' + response.reason + '", normal)'
        f = open('../create_worksheet.py', 'a')
        f.write(report)
        f.close()

        self.assert200(response, "Response body is : " + response.text)


if __name__ == '__main__':
    unittest.main()


