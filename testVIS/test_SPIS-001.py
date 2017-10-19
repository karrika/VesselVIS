# coding: utf-8

"""
    STM Sea Port Information Service SeaSWIM Test cases
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
from swagger_server import service
import logging

pcmdata='''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<portCallMessage xmlns="urn:x-mrn:stm:schema:port-call-message:0.0.16">
   <vesselId>urn:mrn:stm:service:instance:furuno:vis2</vesselId>
   <messageId>urn:mrn:stm:service:instance:furuno:vis2:1</messageId>
   <locationState>
        <referenceObject>VESSEL</referenceObject>
        <time>2017-05-07T16:00:00Z</time>
        <timeType>TARGET</timeType>
        <arrivalLocation>
           <to>           
             <locationType>PILOT_BOARDING_AREA</locationType>
             <name>Pilot Boarding Position 3</name>
           </to>
        </arrivalLocation>
   </locationState>
</portCallMessage>
'''

class TestSPIS_001(BaseTestCase):
    """ SPIS-001 tests """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_SPIS_001_01(self):
        """
        SPIS-001-1 - Find keyword ROS

        
        """
        response = service.sendpcm(pcmdata)
        service.reportrow('SPIS001sheet', 'SPIS_001_01_row', 'SPIS_001_01_col',
            response.status_code == 200, response.reason)
        self.assert200(response, "Response body is : " + response.text)

    def test_SPIS_001_02(self):
        """
        SPIS-001-2 - Find keyword ROS+SSPA

        
        """
        response = service.sendpcm(pcmdata)
        service.reportrow('SPIS001sheet', 'SPIS_001_02_row', 'SPIS_001_02_col',
            response.status_code == 200, response.reason)
        self.assert200(response, "Response body is : " + response.text)

    def test_SPIS_001_03(self):
        """
        SPIS-001-3 - Find keyword RO

        
        """
        response = service.sendpcm(pcmdata)
        service.reportrow('SPIS001sheet', 'SPIS_001_03_row', 'SPIS_001_03_col',
            response.status_code == 200, response.reason)
        self.assert200(response, "Response body is : " + response.text)

    def test_SPIS_001_04(self):
        """
        SPIS-001-4 - Find keyword ros

        
        """
        response = service.sendpcm(pcmdata)
        service.reportrow('SPIS001sheet', 'SPIS_001_04_row', 'SPIS_001_04_col',
            response.status_code == 200, response.reason)
        self.assert200(response, "Response body is : " + response.text)

    def test_SPIS_001_05(self):
        """
        SPIS-001-5 - Find keyword voyage

        
        """
        response = service.sendpcm(pcmdata)
        service.reportrow('SPIS001sheet', 'SPIS_001_05_row', 'SPIS_001_05_col',
            response.status_code == 200, response.reason)
        self.assert200(response, "Response body is : " + response.text)

    def test_SPIS_001_06(self):
        """
        SPIS-001-6 - Find keyword service

        
        """
        response = service.sendpcm(pcmdata)
        service.reportrow('SPIS001sheet', 'SPIS_001_06_row', 'SPIS_001_06_col',
            response.status_code == 200, response.reason)
        self.assert200(response, "Response body is : " + response.text)

    def test_SPIS_001_07(self):
        """
        SPIS-001-7 - Find IMO 8719188

        
        """
        response = service.sendpcm(pcmdata)
        service.reportrow('SPIS001sheet', 'SPIS_001_07_row', 'SPIS_001_07_col',
            response.status_code == 200, response.reason)
        self.assert200(response, "Response body is : " + response.text)


if __name__ == '__main__':
    unittest.main()


