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
<S124:DataSet xmlns:S124="http://www.iho.int/S124/gml/1.0"
	xsi:schemaLocation="http://www.iho.int/S124/gml/1.0 ../../schemas/0.5/S124.xsd" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xmlns:gml="http://www.opengis.net/gml/3.2"
	xmlns:S100="http://www.iho.int/s100gml/1.0"
	xmlns:xlink="http://www.w3.org/1999/xlink" gml:id="SE.local.100.17">
	<gml:boundedBy><gml:Envelope srsName="EPSG:4326">
			<gml:lowerCorner>-6.0000 30.0000</gml:lowerCorner>
			<gml:upperCorner>45.0000 47.0000</gml:upperCorner>
		</gml:Envelope></gml:boundedBy>
<imember>
	<S124:S124_NWPreamble gml:id="PR.SE.local.100.17">
	<id>urn:mrn:s124:NW.SE.local.100.17.P</id>
		<messageSeriesIdentifier>
				<NameOfSeries>Oregrund VTS</NameOfSeries>
				<typeOfWarning>local</typeOfWarning>
				<warningNumber>100</warningNumber>
				<year>17</year>
				<productionAgency>
					<language>eng</language>
					<text>SWEDISH MARITIME AUTHORITY</text>
				</productionAgency>
				<country>SE</country>
		</messageSeriesIdentifier>
		<sourceDate>2017-05-08</sourceDate>
		<generalArea>Sea of Åland and Archipelago Sea</generalArea>
		<locality><text>west of island Orskar</text></locality>
		<title><text>Small craft with 5 crew members is in a drift</text></title>
		<theWarningPart xlink:href="#NW.SE.local.100.17.1"/>
		</S124:S124_NWPreamble>
</imember>
<member>
	<S124:S124_NavigationalWarningPart gml:id="NW.SE.local.100.17.1">
		<id>urn:mrn:s124:NW.SE.local.100.17.1</id>
		<geometry>
		<S100:surfaceProperty>
		<gml:Polygon gml:id="s.NW.SE.local.100.17.1" srsName="EPSG:4326">
			<gml:exterior>
				<gml:LinearRing>
					<gml:posList>
						60.53 18.307
						60.53 18.35
						60.50 18.35
						60.50 18.307
						</gml:posList>
					</gml:LinearRing>
				</gml:exterior>
			</gml:Polygon>
		</S100:surfaceProperty>
		</geometry>  
		<header xlink:href="#PR.SE.local.100.17"/>
	</S124:S124_NavigationalWarningPart>
</member>
</S124:DataSet>
'''

class TestVIS_007(BaseTestCase):
    """ VIS-007 tests """

    def setUp(self):
        pass

    def tearDown(self):
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


