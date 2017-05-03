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
ackurl=hostsettings.callbackurl
voyageuvid='urn:mrn:stm:voyage:id:004:001'
vis2_uvid=hostsettings.vis2_uvid

area='''<?xml version="1.0" encoding="UTF-8"?>
<S124:DataSet xmlns:S124="http://www.iho.int/S124/gml/1.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:gml="http://www.opengis.net/gml/3.2" xmlns:S100="http://www.iho.int/s100gml/1.0" xmlns:xlink="http://www.w3.org/1999/xlink" gml:id="I.001.16">
  <gml:boundedBy>
    <gml:Envelope srsName="EPSG:4326">
      <gml:lowerCorner>55.0000 20.0000</gml:lowerCorner>
      <gml:upperCorner>85.0000 60.0000</gml:upperCorner>
    </gml:Envelope>
  </gml:boundedBy>
  <S100:Surface gml:id="s.NW.I.001.16.1" srsName="EPSG:4326">
    <gml:patches>
      <gml:PolygonPatch>
        <gml:exterior>
          <gml:LinearRing>
            <gml:posList>59.803000 23.836666 59.873917 23.833745 59.902731 24.095344 59.902560 24.370768 59.965007 24.637580 60.047886 25.015368 60.137687 25.402824 60.173118 25.814394 60.033779 25.714923 59.873677 24.903480 59.831262 24.384379</gml:posList>
          </gml:LinearRing>
        </gml:exterior>
      </gml:PolygonPatch>
    </gml:patches>
  </S100:Surface>
  <imember>
    <S124:NWPreamble gml:id="PR.I.001.16">
      <messageSeriesIdentifier>
        <navOrMetArea>NAVAREA I</navOrMetArea>
        <typeOfWarning>sub-area</typeOfWarning>
        <warningNumber>23</warningNumber>
        <year>2016</year>
        <productionAgency>
          <language>eng</language>
          <text>XXX</text>
        </productionAgency>
      </messageSeriesIdentifier>
	  <generalArea>
				<text>Baltic sea</text>
	  </generalArea>
      <locality>
				<text>gulf of Finland</text>
	  </locality>
      <sourceDate>2016-07-15</sourceDate>
      <generalCategory>SailRaceEvent</generalCategory>

      <!--<generalCategory>Sail Race Event</generalCategory>-->
      <!--<locality>gulf of Finland</locality>-->
      <!--<S100:informationAssociation gml:id='ia001' xlink:href='#NW.I.001.16.1' xlink:role='http://www.iho.int/S-124/gml/1.0/roles/theWarningPart'/>-->
    </S124:NWPreamble>
  </imember>
  <member>
    <S124:NavigationalWarningPart gml:id="NW.I.001.16.1">
      <S100:informationAssociation gml:id="iaINV001" xlink:href="#PR.I.001.16" xlink:role="http://www.iho.int/S-124/gml/1.0/roles/header"/>
      <S100:informationAssociation gml:id="ia002" xlink:href="#NW.I.001.16.2" xlink:role="http://www.iho.int/S-124/gml/1.0/roles/theReferences"/>
      <information>
        <text>Annual Sail Race is held on the 16th of July near Helsinki</text>
      </information>
      <fixedDateRange>
        <timeStart>12:00:00</timeStart>
        <timeEnd>17:00:00</timeEnd>
        <dateStart>
          <!--gDay>16</gDay-->
          <date>2016-07-16</date>
        </dateStart>
        <dateEnd>
          <!---gDay>16</gDay>
				<gMonth>07</gMonth>
				<gYear>2016</gYear-->
          <date>2016-07-17</date>
        </dateEnd>
      </fixedDateRange>
      <referenceUVID>urn:mrn:stm:metallica:12356</referenceUVID>
      <header/>
    </S124:NavigationalWarningPart>
  </member>
  <imember>
    <S124:References gml:id="NW.I.001.16.2">
      <S100:invInformationAssociation gml:id="iaINV0002" xlink:href="#NW.I.001.16.1" xlink:role="http://www.iho.int/S-124/gml/1.0/roles/theWarning"/>
      <referenceType>source reference</referenceType>
      <sourceIndication>
        <categoryOfAuthority>maritime</categoryOfAuthority>
        <country>Sweden</country>
        <featureName>
          <displayName>true</displayName>
          <language>SWE</language>
          <name>SMA</name>
        </featureName>
        <source>
          <language>SWE</language>
          <text>name of organization that carries out these competitions</text>
        </source>
      </sourceIndication>
    </S124:References>
  </imember>
</S124:DataSet>
'''

class TestVIS_007(BaseTestCase):
    """ VIS-007 tests """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def vessel_connects(self):
        hostsettings.vessel_connects()
        pass

    def test_VIS_007_00(self):
        """
        VIS-007-0 - VIS-1:0 allow access

        
        """
        hostsettings.set_acl(vis2_uvid, None)
        pass

    def test_VIS_007_01(self):
        """
        VIS-007-1 - VIS-2;  Select S124 message and send (upload) to VIS-1 with ACKendpoint

        
        """
        response=hostsettings.post_area(url, area, ackurl)
        hostsettings.reportrow('VIS007sheet', 'VIS_007_01_row', 'VIS_007_01_col',
            response.status_code == 200, response.reason)
        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_007_02(self):
        """
        VIS-007-2 - STM Module retrieves messages from VIS-1

        
        """
        logged = hostsettings.check_event('area')
        hostsettings.reportrow('VIS007sheet', 'VIS_007_02_row', 'VIS_007_02_col',
            logged, '')
        self.assertTrue(logged)

    def test_VIS_007_1_1(self):
        """
        VIS-007-1-1 - In VIS-2, select S124 message and send (upload) to VIS-1 with ACKendpoint

        
        """
        response=hostsettings.post_area(url, area, ackurl)
        hostsettings.reportrow('VIS007sheet', 'VIS_007_1_1_row', 'VIS_007_1_1_col',
            response.status_code == 200, response.reason)
        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_007_1_2(self):
        """
        VIS-007-1-2 - No private application retrieves the message

        
        """
        logged = hostsettings.check_event('area')
        hostsettings.reportrow('VIS007sheet', 'VIS_007_1_2_row', 'VIS_007_1_2_col',
            not logged, '')
        self.assertFalse(logged)

if __name__ == '__main__':
    unittest.main()


