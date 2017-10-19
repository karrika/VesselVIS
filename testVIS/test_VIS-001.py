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
import logging
from swagger_server import service

url=service.url
callbackurl=service.callbackurl
newvoyageuvid='urn:mrn:stm:voyage:id:001:001'
vis2_uvid=service.vis2_uvid

voyageplan='''<?xml version="1.0" encoding="UTF-8"?>
<route version="1.1" 
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xmlns:stm="http://stmvalidation.eu/STM/1/0/0"
  xsi:schemaLocation="http://stmvalidation.eu/STM/1/0/0 stm_extensions.xsd"
  xmlns="http://www.cirm.org/RTZ/1/1">
  <routeInfo vesselVoyage="urn:mrn:stm:voyage:id:001:001" routeName="HAN-VIS" validityPeriodStart="2017-02-15T10:00:00Z" validityPeriodStop="2017-02-16T10:00:00Z" optimizationMethod="Time table">
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

voyageplan_in_the_past='''<?xml version="1.0" encoding="UTF-8"?>
<route version="1.1" 
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xmlns:stm="http://stmvalidation.eu/STM/1/0/0"
  xsi:schemaLocation="http://stmvalidation.eu/STM/1/0/0 stm_extensions.xsd"
  xmlns="http://www.cirm.org/RTZ/1/1">
  <routeInfo vesselVoyage="urn:mrn:stm:voyage:id:001:001" routeName="HAN-VIS in the past" validityPeriodStart="2016-02-15T10:00:00Z" validityPeriodStop="2016-02-16T10:00:00Z" optimizationMethod="Time table">
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

voyageplan_in_the_past_and_future='''<?xml version="1.0" encoding="UTF-8"?>
<route version="1.1" 
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xmlns:stm="http://stmvalidation.eu/STM/1/0/0"
  xsi:schemaLocation="http://stmvalidation.eu/STM/1/0/0 stm_extensions.xsd"
  xmlns="http://www.cirm.org/RTZ/1/1">
  <routeInfo vesselVoyage="urn:mrn:stm:voyage:id:001:001" routeName="HAN-VIS in past and future" validityPeriodStart="2016-02-15T10:00:00Z" validityPeriodStop="2030-02-16T10:00:00Z" optimizationMethod="Time table">
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

voyageplan_rtz10='''<?xml version="1.0"?>
<route version="1.0" 
  xmlns:xsd="http://www.w3.org/2001/XMLSchema"
  xmlns="http://www.cirm.org/RTZ/1/0">
  <routeInfo routeStatus="7" vesselVoyage="urn:mrn:stm:voyage:id:001:001" routeName="HAN-VIS rtz1.0" validityPeriodStart="2116-02-15T10:00:00Z" validityPeriodStop="2116-02-16T10:00:00Z" optimizationMethod="Time table">
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
        <sheduleElement etd="2116-02-15T10:00:00Z" waypointId="1"/>
        <sheduleElement eta="2116-02-15T10:35:00Z" waypointId="2" speed="7.000000"/>
      </calculated>
    </schedule>
  </schedules>
</route>
'''

voyageplan_in_the_future='''<?xml version="1.0" encoding="UTF-8"?>
<route version="1.1" 
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xmlns:stm="http://stmvalidation.eu/STM/1/0/0"
  xsi:schemaLocation="http://stmvalidation.eu/STM/1/0/0 stm_extensions.xsd"
  xmlns="http://www.cirm.org/RTZ/1/1">
  <routeInfo vesselVoyage="urn:mrn:stm:voyage:id:001:001" routeName="HAN-VIS 1.1" validityPeriodStart="2030-02-15T10:00:00Z" validityPeriodStop="2030-02-16T10:00:00Z" optimizationMethod="Time table">
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

voyageplan_incorrect_xml='''<?xml version="1.0" encoding="UTF-8"?>
<route version="1.1" 
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xmlns:stm="http://stmvalidation.eu/STM/1/0/0"
  xsi:schemaLocation="http://stmvalidation.eu/STM/1/0/0 stm_extensions.xsd"
  xmlns="http://www.cirm.org/RTZ/1/1">
  <routeInfo vesselVoyage="urn:mrn:stm:voyage:id:001:001" routeName="HAN-VIS incorrect xml" validityPeriodStart="2017-02-15T10:00:00Z" validityPeriodStop="2017-02-16T10:00:00Z" optimizationMethod="Time table">
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

voyageplan_incorrect_schema='''<?xml version="1.0" encoding="UTF-8"?>
<route version="1.1" 
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xmlns:stm="http://stmvalidation.eu/STM/1/0/0"
  xsi:schemaLocation="http://stmvalidation.eu/STM/1/0/0 stm_extensions.xsd"
  xmlns="http://www.cirm.org/RTZ/3/9">
  <routeInfo vesselVoyage="urn:mrn:stm:voyage:id:001:001" routeName="HAN-VIS incorrect schema" validityPeriodStart="2017-02-15T10:00:00Z" validityPeriodStop="2017-02-16T10:00:00Z" optimizationMethod="Time table">
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

voyageplan_missing_vesselVoyage='''<?xml version="1.0" encoding="UTF-8"?>
<route version="1.1" 
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xmlns:stm="http://stmvalidation.eu/STM/1/0/0"
  xsi:schemaLocation="http://stmvalidation.eu/STM/1/0/0 stm_extensions.xsd"
  xmlns="http://www.cirm.org/RTZ/1/1">
  <routeInfo routeName="HAN-VIS missing vesselVoyage" validityPeriodStart="2017-02-15T10:00:00Z" validityPeriodStop="2017-02-16T10:00:00Z" optimizationMethod="Time table">
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

voyageplan_wrong_syntax_vesselVoyage='''<?xml version="1.0" encoding="UTF-8"?>
<route version="1.1" 
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xmlns:stm="http://stmvalidation.eu/STM/1/0/0"
  xsi:schemaLocation="http://stmvalidation.eu/STM/1/0/0 stm_extensions.xsd"
  xmlns="http://www.cirm.org/RTZ/1/1">
  <routeInfo vesselVoyage="Free text" routeName="HAN-VIS wrong syntax vesselVoyage" validityPeriodStart="2017-02-15T10:00:00Z" validityPeriodStop="2017-02-16T10:00:00Z" optimizationMethod="Time table">
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

voyageplan_missing_routeStatusEnum='''<?xml version="1.0" encoding="UTF-8"?>
<route version="1.1" 
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xmlns:stm="http://stmvalidation.eu/STM/1/0/0"
  xsi:schemaLocation="http://stmvalidation.eu/STM/1/0/0 stm_extensions.xsd"
  xmlns="http://www.cirm.org/RTZ/1/1">
  <routeInfo vesselVoyage="urn:mrn:stm:voyage:id:001:001" routeName="HAN-VIS missing routeStatusEnum" validityPeriodStart="2017-02-15T10:00:00Z" validityPeriodStop="2017-02-16T10:00:00Z" optimizationMethod="Time table">
    <extensions>
      <extension xsi:type="stm:RouteInfoExtension"
        manufacturer="STM" name="routeInfoEx" version="1.0.0"
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

voyageplan_wrong_syntax_routeStatusEnum='''<?xml version="1.0" encoding="UTF-8"?>
<route version="1.1" 
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xmlns:stm="http://stmvalidation.eu/STM/1/0/0"
  xsi:schemaLocation="http://stmvalidation.eu/STM/1/0/0 stm_extensions.xsd"
  xmlns="http://www.cirm.org/RTZ/1/1">
  <routeInfo vesselVoyage="urn:mrn:stm:voyage:id:001:001" routeName="HAN-VIS wrong syntax routeStatusEnum" validityPeriodStart="2017-02-15T10:00:00Z" validityPeriodStop="2017-02-16T10:00:00Z" optimizationMethod="Time table">
    <extensions>
      <extension xsi:type="stm:RouteInfoExtension"
        manufacturer="STM" name="routeInfoEx" version="1.0.0"
        routeStatusEnum="Free text"
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

class TestVIS_001(BaseTestCase):
    """ VIS-001 tests """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_VIS_001_00(self):
        """
        VIS-001-0 - Preparation: No voyage plan published with chosen UVID in VIS-1

        
        """
        service.rm_acl()
        service.rm_alternate()

        service.reportrow('VIS001sheet', 'VIS_001_00_row', 'VIS_001_00_col')
        pass

    def test_VIS_001_01(self):
        """
        VIS-001-1 - VIS-3: Request (get) voyage plan with chosen UVID from VIS-1

        
        """
        response=service.get_voyageplan(url, newvoyageuvid)
        service.reportrow('VIS001sheet', 'VIS_001_01_row', 'VIS_001_01_col',
            response.status_code == 403, response.reason)
        self.assert403(response, "Response body is : " + response.text)

    def test_VIS_001_02(self):
        """
        VIS-001-2 - VIS-3: Subscribe to voyage plan with chosen UVID from VIS-1

        
        """
        response=service.subscribe_voyageplan(url, callbackurl, newvoyageuvid)
        service.reportrow('VIS001sheet', 'VIS_001_02_row', 'VIS_001_02_col',
            response.status_code == 403, response.reason)
        self.assert403(response, "Response body is : " + response.text)

    def test_VIS_001_03(self):
        """
        VIS-001-3 - Publish voyage plan to VIS-1 with chosen UVID

        
        """
        response=service.post_voyageplan(url, voyageplan)
        service.reportrow('VIS001sheet', 'VIS_001_03_row', 'VIS_001_03_col',
            response.status_code == 200, response.reason)
        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_001_04(self):
        """
        VIS-001-4 - VIS-3: Request voyage plan with chosen UVID from VIS-1

        
        """
        response=service.get_voyageplan(url, newvoyageuvid)
        service.reportrow('VIS001sheet', 'VIS_001_04_row', 'VIS_001_04_col',
            response.status_code == 403, response.reason)
        self.assert403(response, "Response body is : " + response.text)

    def test_VIS_001_05(self):
        """
        VIS-001-5 - VIS-2: Subscribe to voyage plan with chosen UVID from VIS-1

        
        """
        response=service.subscribe_voyageplan(url, callbackurl, newvoyageuvid)
        service.reportrow('VIS001sheet', 'VIS_001_05_row', 'VIS_001_05_col',
            response.status_code == 403, response.reason)
        self.assert403(response, "Response body is : " + response.text)

    def test_VIS_001_06(self):
        """
        VIS-001-6 - VIS-1: Authorize organisation for VIS-2 to chosen UVID in VIS-1

        
        """
        service.set_acl(vis2_uvid, newvoyageuvid)
        service.reportrow('VIS001sheet', 'VIS_001_06_row', 'VIS_001_06_col')
        pass

    def test_VIS_001_07(self):
        """
        VIS-001-7 - VIS-2: Request voyage plan with chosen UVID from VIS-1

        
        """
        response=service.get_voyageplan(url, newvoyageuvid)
        service.reportrow('VIS001sheet', 'VIS_001_07_row', 'VIS_001_07_col',
            response.status_code == 200, response.reason)
        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_001_08(self):
        """
        VIS-001-8 - VIS-2: Subscribe to voyage plan with chosen UVID from VIS-1

        
        """
        response=service.subscribe_voyageplan(url, callbackurl, newvoyageuvid)
        service.reportrow('VIS001sheet', 'VIS_001_08_row', 'VIS_001_08_col',
            response.status_code == 200, response.reason)
        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_001_09(self):
        """
        VIS-001-9 - VIS-1: Remove authorization to organisation for VIS-2 to chosen UVID

        
        """
        service.rm_acl()
        service.reportrow('VIS001sheet', 'VIS_001_09_row', 'VIS_001_09_col')
        pass

    def test_VIS_001_10(self):
        """
        VIS-001-10 - VIS-2: Request voyage plan with chosen UVID from VIS-1

        
        """
        response=service.get_voyageplan(url, newvoyageuvid)
        service.reportrow('VIS001sheet', 'VIS_001_10_row', 'VIS_001_10_col',
            response.status_code == 403, response.reason)
        self.assert403(response, "Response body is : " + response.text)

    def test_VIS_001_11(self):
        """
        VIS-001-11 - VIS-2: Subscribe to voyage plan with chosen UVID from VIS-1

        
        """
        response=service.subscribe_voyageplan(url, callbackurl, newvoyageuvid)
        service.reportrow('VIS001sheet', 'VIS_001_11_row', 'VIS_001_11_col',
            response.status_code == 403, response.reason)
        self.assert403(response, "Response body is : " + response.text)

    def test_VIS_001_12_3_1(self):
        """
        VIS-001-3-1 - Select VP with validityPeriodStart and validityPeriodStop in past and publish to VIS-1


        """
        response=service.post_voyageplan(url, voyageplan_in_the_past)
        service.reportrow('VIS001sheet', 'VIS_001_12_3_1_row', 'VIS_001_12_3_1_col',
            response.status_code == 200, response.reason)
        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_001_12_3_2(self):
        """
        VIS-001-3-2 - Change validityPeriodStop to future and publish to VIS-1


        """
        response=service.post_voyageplan(url, voyageplan_in_the_past_and_future)
        service.reportrow('VIS001sheet', 'VIS_001_12_3_2_row', 'VIS_001_12_3_2_col',
            response.status_code == 200, response.reason)
        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_001_12_3_3(self):
        """
        VIS-001-3-3 - Change validityPeriodStart to future and publish to VIS-1


        """
        response=service.post_voyageplan(url, voyageplan_in_the_future)
        service.reportrow('VIS001sheet', 'VIS_001_12_3_3_row', 'VIS_001_12_3_3_col',
            response.status_code == 200, response.reason)
        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_001_12_4_1(self):
        """
        VIS-001-4-1 - Select VP according to schema RTZ 1.0 and publish to VIS-1


        """
        response=service.post_voyageplan(url, voyageplan_rtz10)
        service.reportrow('VIS001sheet', 'VIS_001_12_4_1_row', 'VIS_001_12_4_1_col',
            response.status_code == 200, response.reason)
        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_001_12_4_2(self):
        """
        VIS-001-4-2 - Select VP according to schema RTZ 1.1 and publish to VIS-1


        """
        response=service.post_voyageplan(url, voyageplan_in_the_future)
        service.reportrow('VIS001sheet', 'VIS_001_12_4_2_row', 'VIS_001_12_4_2_col',
            response.status_code == 200, response.reason)
        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_001_12_4_3(self):
        """
        VIS-001-4-3 - Select VP according to schema RTZ 2.0 and publish to VIS-1


        """
        response=service.post_voyageplan(url, voyageplan_in_the_future)
        service.reportrow('VIS001sheet', 'VIS_001_12_4_3_row', 'VIS_001_12_4_3_col',
            response.status_code == 200, response.reason)
        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_001_12_5_1(self):
        """
        VIS-001-5-1 - Select VP in incorrect XML and publish to VIS-1 


        """
        response=service.post_voyageplan(url, voyageplan_incorrect_xml)
        service.reportrow('VIS001sheet', 'VIS_001_12_5_1_row', 'VIS_001_12_5_1_col',
            response.status_code == 500, response.reason)
        self.assert500(response, "Response body is : " + response.text)

    def test_VIS_001_12_5_2(self):
        """
        VIS-001-5-2 - Select VP not following schema RTZ  and publish to VIS-1 


        """
        response=service.post_voyageplan(url, voyageplan_incorrect_schema)
        service.reportrow('VIS001sheet', 'VIS_001_12_5_2_row', 'VIS_001_12_5_2_col',
            response.status_code == 400, response.reason)
        self.assert400(response, "Response body is : " + response.text)

    def test_VIS_001_12_6_1(self):
        """
        VIS-001-6-1 - Select VP for another ship and publish to subscribers


        """
        response=service.post_voyageplan(url, voyageplan)
        service.reportrow('VIS001sheet', 'VIS_001_12_6_1_row', 'VIS_001_12_6_1_col',
            response.status_code == 200, response.reason)
        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_001_12_7_1(self):
        """
        VIS-001-7-1 - Select voyage plan with missing vesselVoyage and publish to subscribers


        """
        response=service.post_voyageplan(url, voyageplan_missing_vesselVoyage)
        service.reportrow('VIS001sheet', 'VIS_001_12_7_1_row', 'VIS_001_12_7_1_col',
            response.status_code == 404, response.reason)
        self.assert404(response, "Response body is : " + response.text)

    def test_VIS_001_12_7_2(self):
        """
        VIS-001-7-2 - Select voyage plan with incorrect syntax of  vesselVoyage and publish to subscribers


        """
        response=service.post_voyageplan(url, voyageplan_wrong_syntax_vesselVoyage)
        service.reportrow('VIS001sheet', 'VIS_001_12_7_2_row', 'VIS_001_12_7_2_col',
            response.status_code == 400, response.reason)
        self.assert400(response, "Response body is : " + response.text)

    def test_VIS_001_12_7_3(self):
        """
        VIS-001-7-3 - Select voyage plan with missing routeStatus and publish to subscribers


        """
        response=service.post_voyageplan(url, voyageplan_missing_routeStatusEnum)
        service.reportrow('VIS001sheet', 'VIS_001_12_7_3_row', 'VIS_001_12_7_3_col',
            response.status_code == 404, response.reason)
        self.assert404(response, "Response body is : " + response.text)

    def test_VIS_001_12_7_4(self):
        """
        VIS-001-7-4 - Select voyage plan with incorrect syntax of  routeStatus and publish to subscribers


        """
        response=service.post_voyageplan(url, voyageplan_wrong_syntax_routeStatusEnum)
        service.reportrow('VIS001sheet', 'VIS_001_12_7_4_row', 'VIS_001_12_7_4_col',
            response.status_code == 400, response.reason)
        self.assert400(response, "Response body is : " + response.text)

    def test_VIS_001_12_7_5(self):
        """
        VIS-001-7-5 - Test cleanup


        
        """
        def remove(file):
            if os.path.exists(file):
                os.remove(file)

        remove('import/parse:from:rtz.rtz')
        remove('export/parse:from:rtz.rtz')
        remove('export/urn:mrn:stm:voyage:id:001:001.uvid')
        remove('export/HAN-VIS.rtz')
        remove('export/HAN-VIS in the past.rtz')
        remove('export/HAN-VIS in past and future.rtz')
        remove('export/HAN-VIS rtz1.0.rtz')
        remove('export/HAN-VIS 1.1.rtz')
        pass

if __name__ == '__main__':
    unittest.main()


