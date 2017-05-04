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
ackurl=hostsettings.callbackurl
voyageuvid='urn:mrn:stm:voyage:id:004:001'
vis2_uvid=hostsettings.vis2_uvid

voyageplan='''<?xml version="1.0" encoding="UTF-8"?>
<route version="1.1" 
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xmlns:stm="http://stmvalidation.eu/STM/1/0/0"
  xsi:schemaLocation="http://stmvalidation.eu/STM/1/0/0 stm_extensions.xsd"
  xmlns="http://www.cirm.org/RTZ/1/1">
  <routeInfo vesselVoyage="urn:mrn:stm:voyage:id:004:001" routeName="HAN-VIS" validityPeriodStart="2017-02-15T10:00:00Z" validityPeriodStop="2017-02-16T10:00:00Z" optimizationMethod="Time table">
    <extensions>
      <extension xsi:type="stm:RouteInfoExtension"
        manufacturer="STM" name="routeInfoEx" version="1.0.0"
        routeStatusEnum="7"
        depPort="FIHAN"
        arrPort="SEVIS"
        depPortCallId="urn:mrn:stm:portcdm:port_call:FIHAN:20170421"
        arrPortCallId="urn:mrn:stm:portcdm:port_call:SEVIS:20170421"
        startSeaPassage="PILOT_BOARDING_AREA:WP1"
        endSeaPassage="PILOT_BOARDING_AREA:WP2">
        <stm:routeChanges>
            <stm:historyItem dateTime="2016-10-20T11:14:41Z" author="1st mate"
              reason="initial creation"/>
        </stm:routeChanges>
      </extension>
    </extensions>
  </routeInfo>
  <waypoints>
    <waypoint id="1" name="Hango" radius="0.800000">
      <position lat="59.811700" lon="22.935567"/>
    </waypoint>
    <waypoint id="2" radius="0.800000">
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

textmessage='''<?xml version="1.0" encoding="utf-8"?>
<textMessage xmlns="http://tempuri.org/textMessageSchema.xsd">
  <textMessageId>urn:mrn:stm:txt:sma:20161222104700-1</textMessageId>
  <informationObjectReferenceId>urn:mrn:stm:voyage:id:sma:test-1</informationObjectReferenceId>
  <author>Mikael</author>
  <from>urn:mrn:stm:org:sma</from>
  <createdAt>2016-12-22T11:09:47</createdAt>
  <subject>Subject</subject>
  <body>Body</body>
</textMessage>
'''

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

class TestVIS_009(BaseTestCase):
    """ VIS-009 tests """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def vessel_connects(self):
        hostsettings.vessel_connects()
        pass

    def test_VIS_009_00(self):
        """
        VIS-009-0 - VIS-1:0 allow access

        
        """
        hostsettings.set_acl(vis2_uvid, None)
        pass

    def test_VIS_009_01(self):
        """
        VIS-009-1 - Open log and check events and data

        
        """
        hostsettings.reportrow('VIS009sheet', 'VIS_009_01_row', 'VIS_009_01_col')
        pass

    def test_VIS_009_02(self):
        """
        VIS-009-2 - Request voyage plan from VIS

        
        """
        response=hostsettings.get_voyageplan(url)
        hostsettings.reportrow('VIS009sheet', 'VIS_009_02_row', 'VIS_009_02_col',
            response.status_code == 200, response.reason)
        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_009_03(self):
        """
        VIS-009-3 - Request subscription from VIS

        
        """
        response=hostsettings.subscribe_voyageplan(url, callbackurl)
        hostsettings.reportrow('VIS009sheet', 'VIS_009_03_row', 'VIS_009_03_col',
            response.status_code == 200, response.reason)
        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_009_04(self):
        """
        VIS-009-4 - Remove subscription

        
        """
        response=hostsettings.unsubscribe_voyageplan(url, callbackurl)
        hostsettings.reportrow('VIS009sheet', 'VIS_009_04_row', 'VIS_009_04_col',
            response.status_code == 200, response.reason)
        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_009_05(self):
        """
        VIS-009-5 - Upload voyage plan

        
        """
        response=hostsettings.post_voyageplan(url, voyageplan)
        hostsettings.reportrow('VIS009sheet', 'VIS_009_05_row', 'VIS_009_05_col',
            response.status_code == 200, response.reason)
        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_009_06(self):
        """
        VIS-009-6 - Upload text message

        
        """
        response=hostsettings.post_text(url, textmessage, ackurl)
        hostsettings.reportrow('VIS009sheet', 'VIS_009_06_row', 'VIS_009_06_col',
            response.status_code == 200, response.reason)
        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_009_07(self):
        """
        VIS-009-7 - Upload area message

        
        """
        response=hostsettings.post_area(url, area, ackurl)
        hostsettings.reportrow('VIS009sheet', 'VIS_009_07_row', 'VIS_009_07_col',
            response.status_code == 200, response.reason)
        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_009_08(self):
        """
        VIS-009-8 - Receive Acknowledgement

        
        """
        sub='/voyagePlans/subscription'
        parameters={
            'callbackEndpoint': callbackurl
        }
        payload={}
        response=requests.post(url + sub, params=parameters, json=payload, cert=vis_cert, verify=trustchain)
        hostsettings.reportrow('VIS009sheet', 'VIS_009_08_row', 'VIS_009_08_col',
            response.status_code == 200, response.reason)
        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_009_09(self):
        """
        VIS-009-9 - Send voyage plan to subscribers

        
        """
        sub='/voyagePlans/subscription'
        parameters={
            'callbackEndpoint': callbackurl
        }
        payload={}
        response=requests.post(url + sub, params=parameters, json=payload, cert=vis_cert, verify=trustchain)
        hostsettings.reportrow('VIS009sheet', 'VIS_009_09_row', 'VIS_009_09_col',
            response.status_code == 200, response.reason)
        self.assert200(response, "Response body is : " + response.text)

    @unittest.skip('Not applicable as we have no SSC')
    def test_VIS_009_10(self):
        """
        VIS-009-10 - findServices

        
        """
        pass

    @unittest.skip('Not applicable as we have no SSC')
    def test_VIS_009_11(self):
        """
        VIS-009-11 - callService

        
        """
        pass

    @unittest.skip('Not applicable as we have no SSC')
    def test_VIS_009_12(self):
        """
        VIS-009-12 - findIdentities

        
        """
        pass

    def test_VIS_009_13(self):
        """
        VIS-009-13 - Test both successful calls and erroneous calls

        
        """
        sub='/voyagePlans/subscription'
        parameters={
            'callbackEndpoint': callbackurl
        }
        payload={}
        response=requests.post(url + sub, params=parameters, json=payload, cert=vis_cert, verify=trustchain)
        hostsettings.reportrow('VIS009sheet', 'VIS_009_13_row', 'VIS_009_13_col',
            response.status_code == 200, response.reason)
        self.assert200(response, "Response body is : " + response.text)

if __name__ == '__main__':
    unittest.main()


