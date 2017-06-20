# coding: utf-8

"""
    STM Voyage Information Service SeaSWIM Test cases
"""

from __future__ import absolute_import

import os
import sys
import requests
import shutil
import sys
import json
from pathlib import Path
from testVIS import hostsettings

voyageplan='''<?xml version="1.0" encoding="UTF-8"?>
<route version="1.1" 
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xmlns:stm="http://stmvalidation.eu/STM/1/0/0"
  xsi:schemaLocation="http://stmvalidation.eu/STM/1/0/0 stm_extensions.xsd"
  xmlns="http://www.cirm.org/RTZ/1/1">
  <routeInfo vesselVoyage="urn:mrn:stm:voyage:id:mini:001" routeName="HAN-VIS" validityPeriodStart="2017-02-15T10:00:00Z" validityPeriodStop="2017-02-16T10:00:00Z" optimizationMethod="Time table">
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
<textMessage
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xmlns="http://stmvalidation.eu/schemas/textMessageSchema_1_3.xsd">
  <textMessageId>urn:mrn:stm:txt:sma:20170510104400-1</textMessageId>
  <informationObjectReferenceId>urn:mrn:stm:voyage:id:003:001</informationObjectReferenceId>
  <informationObjectReferenceType>RTZ</informationObjectReferenceType>
  <validityPeriodStart>2017-05-01T01:00:00Z</validityPeriodStart>
  <validityPeriodStop>2017-06-10T01:00:00Z</validityPeriodStop>
  <author>urn:mrn:stm:user:sma:mikolo</author>
  <from>urn:mrn:stm:org:sma</from>
  <serviceType>SHIP-VIS</serviceType>
  <createdAt>2017-05-10T01:00:00Z</createdAt>
  <subject>Test message</subject>
  <body>Test message Hanoebukten</body>
  <position lat="55.50668" lon="14.29825"/>
  <area>
    <Polygon>
      <posList>55.452 14.405 55.465 14.151 56.006 14.301 55.563 14.437 55.452 14.405</posList>
    </Polygon>
    <Circle>
      <position lat="55.50668" lon="14.29825"/>
      <radius>1</radius>
    </Circle>
  </area>
</textMessage>
'''

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


url=hostsettings.url
ackurl='https://stm.furuno.fi:8001'
vis_cert=hostsettings.vis_cert
trustchain=hostsettings.trustchain
print('Endpoint: ', url)
print()

print('POST voyageplan')
response=hostsettings.post_voyageplan(url, voyageplan, callbackEndpoint = ackurl, deliveryAckEndPoint = ackurl)
print(response.text)
#print('POST textmessage')
#response=hostsettings.post_text(url, textmessage, ackurl)
#print(response.text)
#print('POST area message')
#response=hostsettings.post_area(url, area, ackurl)
#print(response.text)
#print('GET voyage plans')
#response=hostsettings.get_voyageplan(url)
#print(response.text)
#print()
#print('SUBSCRIBE voyage plans')
#response=hostsettings.subscribe_voyageplan(url, ackurl)
#print(response.text)
#print()
#print('UNSUBSCRIBE voyage plans')
#response=hostsettings.unsubscribe_voyageplan(url, ackurl)
#print(response.text)
#print()
#print('POST acknowledgement')
#response=hostsettings.send_ack(url)
#print(response.text)


