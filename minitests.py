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
import uuid
from pathlib import Path
from swagger_server import service

voyageplan='''<?xml version="1.0" encoding="UTF-8"?>
<!--route node-->
<route version="1.1" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:stm="http://stmvalidation.eu/STM/1/0/0" xsi:schemaLocation="http://stmvalidation.eu/STM/1/0/0 stm_extensions.xsd" xmlns="http://www.cirm.org/RTZ/1/1">
  <!--routeInfo node-->
  <routeInfo routeName="FROMFFOY" vesselName="FURUNO KOEAJO" vesselMMSI="230031001" vesselIMO="0000000" vesselVoyage="urn:mrn:stm:voyage:id:furuno:19700101000000-11-FROMFFOY" optimizationMethod="MAX speed">
    <extensions>
      <extension xsi:type="stm:RouteInfoExtension" manufacturer="STM" name="routeInfoEx" version="1.0.0" routeStatusEnum="7" depPort="SEGOT" arrPort="SEUME">
        <stm:routeChanges>
          <stm:historyItem dateTime="2017-08-23T06:46:20Z" author="Karri" reason="Space characters break uvid"/>
        </stm:routeChanges>
      </extension>
      <extension manufacturer="Furuno" name="AdditionalRouteInfo" version="1.0">
        <property income="0" channelLimitMode="0" safetyContour="30" ukcLimit="30.000000"/>
      </extension>
    </extensions>
  </routeInfo>
  <!--waypoints node-->
  <waypoints>
    <!--No.1 waypoint-->
    <waypoint id="1" name="" radius="0.800000">
      <position lat="60.166333" lon="24.706517"/>
    </waypoint>
    <!--No.2 waypoint-->
    <waypoint id="2" name="" radius="0.800000">
      <position lat="60.163017" lon="24.695300"/>
      <leg portsideXTD="0.099892" starboardXTD="0.099892" safetyContour="30" geometryType="Loxodrome" speedMax="22.100000" draughtForward="10.000000" draughtAft="10.000000" staticUKC="30.000000"/>
      <extensions>
        <extension manufacturer="Furuno" name="AdditionalLegInfo" version="1.0">
          <property margin="40.000000" parallelLine1="0.000000" parallelLine2="0.000000"/>
        </extension>
      </extensions>
    </waypoint>
    <!--No.3 waypoint-->
    <waypoint id="3" name="" radius="0.380000">
      <position lat="60.161833" lon="24.681733"/>
      <leg portsideXTD="0.099892" starboardXTD="0.099892" safetyContour="30" geometryType="Loxodrome" speedMax="22.100000" draughtForward="10.000000" draughtAft="10.000000" staticUKC="30.000000"/>
      <extensions>
        <extension manufacturer="Furuno" name="AdditionalLegInfo" version="1.0">
          <property margin="40.000000" parallelLine1="0.000000" parallelLine2="0.000000"/>
        </extension>
      </extensions>
    </waypoint>
    <!--No.4 waypoint-->
    <waypoint id="4" name="" radius="0.330000">
      <position lat="60.157633" lon="24.670733"/>
      <leg portsideXTD="0.099892" starboardXTD="0.099892" safetyContour="30" geometryType="Loxodrome" speedMax="22.100000" draughtForward="10.000000" draughtAft="10.000000" staticUKC="30.000000"/>
      <extensions>
        <extension manufacturer="Furuno" name="AdditionalLegInfo" version="1.0">
          <property margin="40.000000" parallelLine1="0.000000" parallelLine2="0.000000"/>
        </extension>
      </extensions>
    </waypoint>
    <!--No.5 waypoint-->
    <waypoint id="5" name="" radius="0.390000">
      <position lat="60.155667" lon="24.657350"/>
      <leg portsideXTD="0.099892" starboardXTD="0.099892" safetyContour="30" geometryType="Loxodrome" speedMax="22.100000" draughtForward="10.000000" draughtAft="10.000000" staticUKC="30.000000"/>
      <extensions>
        <extension manufacturer="Furuno" name="AdditionalLegInfo" version="1.0">
          <property margin="40.000000" parallelLine1="0.000000" parallelLine2="0.000000"/>
        </extension>
      </extensions>
    </waypoint>
    <!--No.6 waypoint-->
    <waypoint id="6" name="" radius="0.470000">
      <position lat="60.152633" lon="24.648317"/>
      <leg portsideXTD="0.099892" starboardXTD="0.099892" safetyContour="30" geometryType="Loxodrome" speedMax="22.100000" draughtForward="10.000000" draughtAft="10.000000" staticUKC="30.000000"/>
      <extensions>
        <extension manufacturer="Furuno" name="AdditionalLegInfo" version="1.0">
          <property margin="40.000000" parallelLine1="0.000000" parallelLine2="0.000000"/>
        </extension>
      </extensions>
    </waypoint>
    <!--No.7 waypoint-->
    <waypoint id="7" name="" radius="0.800000">
      <position lat="60.149017" lon="24.626483"/>
      <leg portsideXTD="0.099892" starboardXTD="0.099892" safetyContour="30" geometryType="Loxodrome" speedMax="22.100000" draughtForward="10.000000" draughtAft="10.000000" staticUKC="30.000000"/>
      <extensions>
        <extension manufacturer="Furuno" name="AdditionalLegInfo" version="1.0">
          <property margin="40.000000" parallelLine1="0.000000" parallelLine2="0.000000"/>
        </extension>
      </extensions>
    </waypoint>
    <!--No.8 waypoint-->
    <waypoint id="8" name="" radius="0.800000">
      <position lat="60.148183" lon="24.612033"/>
      <leg portsideXTD="0.099892" starboardXTD="0.099892" safetyContour="30" geometryType="Loxodrome" speedMax="22.100000" draughtForward="10.000000" draughtAft="10.000000" staticUKC="30.000000"/>
      <extensions>
        <extension manufacturer="Furuno" name="AdditionalLegInfo" version="1.0">
          <property margin="40.000000" parallelLine1="0.000000" parallelLine2="0.000000"/>
        </extension>
      </extensions>
    </waypoint>
  </waypoints>
  <!--schedules node-->
  <schedules/>
</route>
'''

voyageplan2='''<?xml version="1.0" encoding="UTF-8"?>
<!--route node-->
<route version="1.1" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:stm="http://stmvalidation.eu/STM/1/0/0" xsi:schemaLocation="http://stmvalidation.eu/STM/1/0/0 stm_extensions.xsd" xmlns="http://www.cirm.org/RTZ/1/1">
  <!--routeInfo node-->
  <routeInfo routeName="Barcelona-Gothenborg" vesselName="FURUNO KOEAJO" vesselMMSI="230031001" vesselIMO="0000000" vesselVoyage="urn:mrn:stm:voyage:id:furuno:19700101000000-2-Barcelona-Gothenborg" optimizationMethod="MAX speed">
    <extensions>
      <extension xsi:type="stm:RouteInfoExtension" manufacturer="STM" name="routeInfoEx" version="1.0.0" routeStatusEnum="1" depPort="SEGOT" arrPort="SEUME" />
      <extension manufacturer="Furuno" name="AdditionalRouteInfo" version="1.0">
        <property income="0" channelLimitMode="1" safetyContour="30" ukcLimit="30.000000"/>
      </extension>
    </extensions>
  </routeInfo>
  <!--waypoints node-->
  <waypoints>
    <!--No.1 waypoint-->
    <waypoint id="1" name="Barcelona Port" radius="1.000000">
      <position lat="41.302357" lon="2.168808"/>
    </waypoint>
    <!--No.2 waypoint-->
    <waypoint id="2" name="" radius="1.000000">
      <position lat="41.246190" lon="2.192564"/>
      <leg portsideXTD="0.539957" starboardXTD="0.539957" safetyContour="30" geometryType="Loxodrome" speedMax="22.100000" draughtForward="10.000000" draughtAft="10.000000" staticUKC="30.000000"/>
      <extensions>
        <extension manufacturer="Furuno" name="AdditionalLegInfo" version="1.0">
          <property margin="0.000000" parallelLine1="0.000000" parallelLine2="0.000000"/>
        </extension>
      </extensions>
    </waypoint>
    <!--No.3 waypoint-->
    <waypoint id="3" name="Cabo de la Nao" radius="1.000000">
      <position lat="38.731918" lon="0.369609"/>
      <leg portsideXTD="0.539957" starboardXTD="0.539957" safetyContour="30" geometryType="Loxodrome" speedMax="22.100000" draughtForward="10.000000" draughtAft="10.000000" staticUKC="30.000000"/>
      <extensions>
        <extension manufacturer="Furuno" name="AdditionalLegInfo" version="1.0">
          <property margin="0.000000" parallelLine1="0.000000" parallelLine2="0.000000"/>
        </extension>
      </extensions>
    </waypoint>
    <!--No.4 waypoint-->
    <waypoint id="4" name="Cabo de Palos" radius="1.000000">
      <position lat="37.560518" lon="-0.567099"/>
      <leg portsideXTD="0.539957" starboardXTD="0.539957" safetyContour="30" geometryType="Loxodrome" speedMax="22.100000" draughtForward="10.000000" draughtAft="10.000000" staticUKC="30.000000"/>
      <extensions>
        <extension manufacturer="Furuno" name="AdditionalLegInfo" version="1.0">
          <property margin="0.000000" parallelLine1="0.000000" parallelLine2="0.000000"/>
        </extension>
      </extensions>
    </waypoint>
    <!--No.5 waypoint-->
    <waypoint id="5" name="Cabo de Gata" radius="1.000000">
      <position lat="36.422830" lon="-2.192519"/>
      <leg portsideXTD="0.539957" starboardXTD="0.539957" safetyContour="30" geometryType="Loxodrome" speedMax="22.100000" draughtForward="10.000000" draughtAft="10.000000" staticUKC="30.000000"/>
      <extensions>
        <extension manufacturer="Furuno" name="AdditionalLegInfo" version="1.0">
          <property margin="0.000000" parallelLine1="0.000000" parallelLine2="0.000000"/>
        </extension>
      </extensions>
    </waypoint>
    <!--No.6 waypoint-->
    <waypoint id="6" name="Algeciras" radius="1.000000">
      <position lat="36.043494" lon="-5.295780"/>
      <leg portsideXTD="0.539957" starboardXTD="0.539957" safetyContour="30" geometryType="Loxodrome" speedMax="22.100000" draughtForward="10.000000" draughtAft="10.000000" staticUKC="30.000000"/>
      <extensions>
        <extension manufacturer="Furuno" name="AdditionalLegInfo" version="1.0">
          <property margin="0.000000" parallelLine1="0.000000" parallelLine2="0.000000"/>
        </extension>
      </extensions>
    </waypoint>
    <!--No.7 waypoint-->
    <waypoint id="7" name="Gibraltar Street" radius="1.000000">
      <position lat="35.951721" lon="-5.626583"/>
      <leg portsideXTD="0.539957" starboardXTD="0.539957" safetyContour="30" geometryType="Loxodrome" speedMax="22.100000" draughtForward="10.000000" draughtAft="10.000000" staticUKC="30.000000"/>
      <extensions>
        <extension manufacturer="Furuno" name="AdditionalLegInfo" version="1.0">
          <property margin="0.000000" parallelLine1="0.000000" parallelLine2="0.000000"/>
        </extension>
      </extensions>
    </waypoint>
    <!--No.8 waypoint-->
    <waypoint id="8" name="Cabo Trafalgar" radius="1.000000">
      <position lat="35.950510" lon="-6.196057"/>
      <leg portsideXTD="0.539957" starboardXTD="0.539957" safetyContour="30" geometryType="Loxodrome" speedMax="22.100000" draughtForward="10.000000" draughtAft="10.000000" staticUKC="30.000000"/>
      <extensions>
        <extension manufacturer="Furuno" name="AdditionalLegInfo" version="1.0">
          <property margin="0.000000" parallelLine1="0.000000" parallelLine2="0.000000"/>
        </extension>
      </extensions>
    </waypoint>
    <!--No.9 waypoint-->
    <waypoint id="9" name="Cabo Vicente" radius="1.000000">
      <position lat="36.747495" lon="-9.136054"/>
      <leg portsideXTD="0.539957" starboardXTD="0.539957" safetyContour="30" geometryType="Loxodrome" speedMax="22.100000" draughtForward="10.000000" draughtAft="10.000000" staticUKC="30.000000"/>
      <extensions>
        <extension manufacturer="Furuno" name="AdditionalLegInfo" version="1.0">
          <property margin="0.000000" parallelLine1="0.000000" parallelLine2="0.000000"/>
        </extension>
      </extensions>
    </waypoint>
    <!--No.10 waypoint-->
    <waypoint id="10" name="COPREB Report" radius="1.000000">
      <position lat="36.915920" lon="-9.344751"/>
      <leg portsideXTD="0.539957" starboardXTD="0.539957" safetyContour="30" geometryType="Loxodrome" speedMax="22.100000" draughtForward="10.000000" draughtAft="10.000000" staticUKC="30.000000"/>
      <extensions>
        <extension manufacturer="Furuno" name="AdditionalLegInfo" version="1.0">
          <property margin="0.000000" parallelLine1="0.000000" parallelLine2="0.000000"/>
        </extension>
      </extensions>
    </waypoint>
    <!--No.11 waypoint-->
    <waypoint id="11" name="Cabo de Roca" radius="1.000000">
      <position lat="38.746829" lon="-9.853093"/>
      <leg portsideXTD="0.539957" starboardXTD="0.539957" safetyContour="30" geometryType="Loxodrome" speedMax="22.100000" draughtForward="10.000000" draughtAft="10.000000" staticUKC="30.000000"/>
      <extensions>
        <extension manufacturer="Furuno" name="AdditionalLegInfo" version="1.0">
          <property margin="0.000000" parallelLine1="0.000000" parallelLine2="0.000000"/>
        </extension>
      </extensions>
    </waypoint>
    <!--No.12 waypoint-->
    <waypoint id="12" name="Cabo Torinana" radius="1.000000">
      <position lat="43.192115" lon="-9.791491"/>
      <leg portsideXTD="0.539957" starboardXTD="0.539957" safetyContour="30" geometryType="Loxodrome" speedMax="22.100000" draughtForward="10.000000" draughtAft="10.000000" staticUKC="30.000000"/>
      <extensions>
        <extension manufacturer="Furuno" name="AdditionalLegInfo" version="1.0">
          <property margin="0.000000" parallelLine1="0.000000" parallelLine2="0.000000"/>
        </extension>
      </extensions>
    </waypoint>
    <!--No.13 waypoint-->
    <waypoint id="13" name="Aton 992276301" radius="1.000000">
      <position lat="48.783177" lon="-5.601301"/>
      <leg portsideXTD="0.539957" starboardXTD="0.539957" safetyContour="30" geometryType="Loxodrome" speedMax="22.100000" draughtForward="10.000000" draughtAft="10.000000" staticUKC="30.000000"/>
      <extensions>
        <extension manufacturer="Furuno" name="AdditionalLegInfo" version="1.0">
          <property margin="0.000000" parallelLine1="0.000000" parallelLine2="0.000000"/>
        </extension>
      </extensions>
    </waypoint>
    <!--No.14 waypoint-->
    <waypoint id="14" name="Guernsey" radius="1.000000">
      <position lat="49.807189" lon="-2.950814"/>
      <leg portsideXTD="0.539957" starboardXTD="0.539957" safetyContour="30" geometryType="Loxodrome" speedMax="22.100000" draughtForward="10.000000" draughtAft="10.000000" staticUKC="30.000000"/>
      <extensions>
        <extension manufacturer="Furuno" name="AdditionalLegInfo" version="1.0">
          <property margin="0.000000" parallelLine1="0.000000" parallelLine2="0.000000"/>
        </extension>
      </extensions>
    </waypoint>
    <!--No.15 waypoint-->
    <waypoint id="15" name="Bassurelle" radius="1.000000">
      <position lat="50.516720" lon="1.042536"/>
      <leg portsideXTD="0.539957" starboardXTD="0.539957" safetyContour="30" geometryType="Loxodrome" speedMax="22.100000" draughtForward="10.000000" draughtAft="10.000000" staticUKC="30.000000"/>
      <extensions>
        <extension manufacturer="Furuno" name="AdditionalLegInfo" version="1.0">
          <property margin="0.000000" parallelLine1="0.000000" parallelLine2="0.000000"/>
        </extension>
      </extensions>
    </waypoint>
    <!--No.16 waypoint-->
    <waypoint id="16" name="Verguyer" radius="1.000000">
      <position lat="50.565360" lon="1.154182"/>
      <leg portsideXTD="0.539957" starboardXTD="0.539957" safetyContour="30" geometryType="Loxodrome" speedMax="22.100000" draughtForward="10.000000" draughtAft="10.000000" staticUKC="30.000000"/>
      <extensions>
        <extension manufacturer="Furuno" name="AdditionalLegInfo" version="1.0">
          <property margin="0.000000" parallelLine1="0.000000" parallelLine2="0.000000"/>
        </extension>
      </extensions>
    </waypoint>
    <!--No.17 waypoint-->
    <waypoint id="17" name="" radius="1.000000">
      <position lat="50.698134" lon="1.342688"/>
      <leg portsideXTD="0.539957" starboardXTD="0.539957" safetyContour="30" geometryType="Loxodrome" speedMax="22.100000" draughtForward="10.000000" draughtAft="10.000000" staticUKC="30.000000"/>
      <extensions>
        <extension manufacturer="Furuno" name="AdditionalLegInfo" version="1.0">
          <property margin="0.000000" parallelLine1="0.000000" parallelLine2="0.000000"/>
        </extension>
      </extensions>
    </waypoint>
    <!--No.18 waypoint-->
    <waypoint id="18" name="ZC2" radius="1.000000">
      <position lat="50.900059" lon="1.430883"/>
      <leg portsideXTD="0.539957" starboardXTD="0.539957" safetyContour="30" geometryType="Loxodrome" speedMax="22.100000" draughtForward="10.000000" draughtAft="10.000000" staticUKC="30.000000"/>
      <extensions>
        <extension manufacturer="Furuno" name="AdditionalLegInfo" version="1.0">
          <property margin="0.000000" parallelLine1="0.000000" parallelLine2="0.000000"/>
        </extension>
      </extensions>
    </waypoint>
    <!--No.19 waypoint-->
    <waypoint id="19" name="Ruytingen" radius="1.000000">
      <position lat="51.088722" lon="1.695638"/>
      <leg portsideXTD="0.539957" starboardXTD="0.539957" safetyContour="30" geometryType="Loxodrome" speedMax="22.100000" draughtForward="10.000000" draughtAft="10.000000" staticUKC="30.000000"/>
      <extensions>
        <extension manufacturer="Furuno" name="AdditionalLegInfo" version="1.0">
          <property margin="0.000000" parallelLine1="0.000000" parallelLine2="0.000000"/>
        </extension>
      </extensions>
    </waypoint>
    <!--No.20 waypoint-->
    <waypoint id="20" name="Sandettie" radius="1.000000">
      <position lat="51.220618" lon="1.829956"/>
      <leg portsideXTD="0.539957" starboardXTD="0.539957" safetyContour="30" geometryType="Loxodrome" speedMax="22.100000" draughtForward="10.000000" draughtAft="10.000000" staticUKC="30.000000"/>
      <extensions>
        <extension manufacturer="Furuno" name="AdditionalLegInfo" version="1.0">
          <property margin="0.000000" parallelLine1="0.000000" parallelLine2="0.000000"/>
        </extension>
      </extensions>
    </waypoint>
    <!--No.21 waypoint-->
    <waypoint id="21" name="Euro W" radius="1.000000">
      <position lat="51.840607" lon="2.681310"/>
      <leg portsideXTD="0.539957" starboardXTD="0.539957" safetyContour="30" geometryType="Loxodrome" speedMax="22.100000" draughtForward="10.000000" draughtAft="10.000000" staticUKC="30.000000"/>
      <extensions>
        <extension manufacturer="Furuno" name="AdditionalLegInfo" version="1.0">
          <property margin="0.000000" parallelLine1="0.000000" parallelLine2="0.000000"/>
        </extension>
      </extensions>
    </waypoint>
    <!--No.22 waypoint-->
    <waypoint id="22" name="" radius="1.000000">
      <position lat="52.186862" lon="2.690256"/>
      <leg portsideXTD="0.539957" starboardXTD="0.539957" safetyContour="30" geometryType="Loxodrome" speedMax="22.100000" draughtForward="10.000000" draughtAft="10.000000" staticUKC="30.000000"/>
      <extensions>
        <extension manufacturer="Furuno" name="AdditionalLegInfo" version="1.0">
          <property margin="0.000000" parallelLine1="0.000000" parallelLine2="0.000000"/>
        </extension>
      </extensions>
    </waypoint>
    <!--No.23 waypoint-->
    <waypoint id="23" name="BP 7" radius="1.000000">
      <position lat="52.915876" lon="3.338244"/>
      <leg portsideXTD="0.539957" starboardXTD="0.539957" safetyContour="30" geometryType="Loxodrome" speedMax="22.100000" draughtForward="10.000000" draughtAft="10.000000" staticUKC="30.000000"/>
      <extensions>
        <extension manufacturer="Furuno" name="AdditionalLegInfo" version="1.0">
          <property margin="0.000000" parallelLine1="0.000000" parallelLine2="0.000000"/>
        </extension>
      </extensions>
    </waypoint>
    <!--No.24 waypoint-->
    <waypoint id="24" name="PEN 10" radius="1.000000">
      <position lat="53.509584" lon="3.764843"/>
      <leg portsideXTD="0.539957" starboardXTD="0.539957" safetyContour="30" geometryType="Loxodrome" speedMax="22.100000" draughtForward="10.000000" draughtAft="10.000000" staticUKC="30.000000"/>
      <extensions>
        <extension manufacturer="Furuno" name="AdditionalLegInfo" version="1.0">
          <property margin="0.000000" parallelLine1="0.000000" parallelLine2="0.000000"/>
        </extension>
      </extensions>
    </waypoint>
    <!--No.25 waypoint-->
    <waypoint id="25" name="Ensco 122" radius="1.000000">
      <position lat="53.913259" lon="4.574409"/>
      <leg portsideXTD="0.539957" starboardXTD="0.539957" safetyContour="30" geometryType="Loxodrome" speedMax="22.100000" draughtForward="10.000000" draughtAft="10.000000" staticUKC="30.000000"/>
      <extensions>
        <extension manufacturer="Furuno" name="AdditionalLegInfo" version="1.0">
          <property margin="0.000000" parallelLine1="0.000000" parallelLine2="0.000000"/>
        </extension>
      </extensions>
    </waypoint>
    <!--No.26 waypoint-->
    <waypoint id="26" name="Prod F15" radius="1.000000">
      <position lat="54.241353" lon="4.782000"/>
      <leg portsideXTD="0.539957" starboardXTD="0.539957" safetyContour="30" geometryType="Loxodrome" speedMax="22.100000" draughtForward="10.000000" draughtAft="10.000000" staticUKC="30.000000"/>
      <extensions>
        <extension manufacturer="Furuno" name="AdditionalLegInfo" version="1.0">
          <property margin="0.000000" parallelLine1="0.000000" parallelLine2="0.000000"/>
        </extension>
      </extensions>
    </waypoint>
    <!--No.27 waypoint-->
    <waypoint id="27" name="Jammerbugt" radius="1.000000">
      <position lat="57.470533" lon="8.368660"/>
      <leg portsideXTD="0.539957" starboardXTD="0.539957" safetyContour="30" geometryType="Loxodrome" speedMax="22.100000" draughtForward="10.000000" draughtAft="10.000000" staticUKC="30.000000"/>
      <extensions>
        <extension manufacturer="Furuno" name="AdditionalLegInfo" version="1.0">
          <property margin="0.000000" parallelLine1="0.000000" parallelLine2="0.000000"/>
        </extension>
      </extensions>
    </waypoint>
    <!--No.28 waypoint-->
    <waypoint id="28" name="Hirtshals" radius="1.000000">
      <position lat="58.087575" lon="9.994499"/>
      <leg portsideXTD="0.539957" starboardXTD="0.539957" safetyContour="30" geometryType="Loxodrome" speedMax="22.100000" draughtForward="10.000000" draughtAft="10.000000" staticUKC="30.000000"/>
      <extensions>
        <extension manufacturer="Furuno" name="AdditionalLegInfo" version="1.0">
          <property margin="0.000000" parallelLine1="0.000000" parallelLine2="0.000000"/>
        </extension>
      </extensions>
    </waypoint>
    <!--No.29 waypoint-->
    <waypoint id="29" name="Djupa Rennan" radius="1.000000">
      <position lat="57.889380" lon="11.239638"/>
      <leg portsideXTD="0.539957" starboardXTD="0.539957" safetyContour="30" geometryType="Loxodrome" speedMax="22.100000" draughtForward="10.000000" draughtAft="10.000000" staticUKC="30.000000"/>
      <extensions>
        <extension manufacturer="Furuno" name="AdditionalLegInfo" version="1.0">
          <property margin="0.000000" parallelLine1="0.000000" parallelLine2="0.000000"/>
        </extension>
      </extensions>
    </waypoint>
    <!--No.30 waypoint-->
    <waypoint id="30" name="Gothenborg Approach" radius="1.000000">
      <position lat="57.587848" lon="11.446772"/>
      <leg portsideXTD="0.539957" starboardXTD="0.539957" safetyContour="30" geometryType="Loxodrome" speedMax="22.100000" draughtForward="10.000000" draughtAft="10.000000" staticUKC="30.000000"/>
      <extensions>
        <extension manufacturer="Furuno" name="AdditionalLegInfo" version="1.0">
          <property margin="0.000000" parallelLine1="0.000000" parallelLine2="0.000000"/>
        </extension>
      </extensions>
    </waypoint>
    <!--No.31 waypoint-->
    <waypoint id="31" name="" radius="1.000000">
      <position lat="57.544325" lon="11.549589"/>
      <leg portsideXTD="0.539957" starboardXTD="0.539957" safetyContour="30" geometryType="Loxodrome" speedMax="22.100000" draughtForward="10.000000" draughtAft="10.000000" staticUKC="30.000000"/>
      <extensions>
        <extension manufacturer="Furuno" name="AdditionalLegInfo" version="1.0">
          <property margin="0.000000" parallelLine1="0.000000" parallelLine2="0.000000"/>
        </extension>
      </extensions>
    </waypoint>
    <!--No.32 waypoint-->
    <waypoint id="32" name="Traffic Separation" radius="1.000000">
      <position lat="57.571454" lon="11.653254"/>
      <leg portsideXTD="0.539957" starboardXTD="0.539957" safetyContour="30" geometryType="Loxodrome" speedMax="22.100000" draughtForward="10.000000" draughtAft="10.000000" staticUKC="30.000000"/>
      <extensions>
        <extension manufacturer="Furuno" name="AdditionalLegInfo" version="1.0">
          <property margin="0.000000" parallelLine1="0.000000" parallelLine2="0.000000"/>
        </extension>
      </extensions>
    </waypoint>
    <!--No.33 waypoint-->
    <waypoint id="33" name="" radius="1.000000">
      <position lat="57.607042" lon="11.666901"/>
      <leg portsideXTD="0.539957" starboardXTD="0.539957" safetyContour="30" geometryType="Loxodrome" speedMax="22.100000" draughtForward="10.000000" draughtAft="10.000000" staticUKC="30.000000"/>
      <extensions>
        <extension manufacturer="Furuno" name="AdditionalLegInfo" version="1.0">
          <property margin="0.000000" parallelLine1="0.000000" parallelLine2="0.000000"/>
        </extension>
      </extensions>
    </waypoint>
    <!--No.34 waypoint-->
    <waypoint id="34" name="" radius="1.000000">
      <position lat="57.630624" lon="11.695992"/>
      <leg portsideXTD="0.539957" starboardXTD="0.539957" safetyContour="30" geometryType="Loxodrome" speedMax="22.100000" draughtForward="10.000000" draughtAft="10.000000" staticUKC="30.000000"/>
      <extensions>
        <extension manufacturer="Furuno" name="AdditionalLegInfo" version="1.0">
          <property margin="0.000000" parallelLine1="0.000000" parallelLine2="0.000000"/>
        </extension>
      </extensions>
    </waypoint>
    <!--No.35 waypoint-->
    <waypoint id="35" name="" radius="1.000000">
      <position lat="57.647444" lon="11.697822"/>
      <leg portsideXTD="0.539957" starboardXTD="0.539957" safetyContour="30" geometryType="Loxodrome" speedMax="22.100000" draughtForward="10.000000" draughtAft="10.000000" staticUKC="30.000000"/>
      <extensions>
        <extension manufacturer="Furuno" name="AdditionalLegInfo" version="1.0">
          <property margin="0.000000" parallelLine1="0.000000" parallelLine2="0.000000"/>
        </extension>
      </extensions>
    </waypoint>
    <!--No.36 waypoint-->
    <waypoint id="36" name="" radius="1.000000">
      <position lat="57.660052" lon="11.774033"/>
      <leg portsideXTD="0.539957" starboardXTD="0.539957" safetyContour="30" geometryType="Loxodrome" speedMax="22.100000" draughtForward="10.000000" draughtAft="10.000000" staticUKC="30.000000"/>
      <extensions>
        <extension manufacturer="Furuno" name="AdditionalLegInfo" version="1.0">
          <property margin="0.000000" parallelLine1="0.000000" parallelLine2="0.000000"/>
        </extension>
      </extensions>
    </waypoint>
    <!--No.37 waypoint-->
    <waypoint id="37" name="" radius="1.000000">
      <position lat="57.678211" lon="11.809310"/>
      <leg portsideXTD="0.539957" starboardXTD="0.539957" safetyContour="30" geometryType="Loxodrome" speedMax="22.100000" draughtForward="10.000000" draughtAft="10.000000" staticUKC="30.000000"/>
      <extensions>
        <extension manufacturer="Furuno" name="AdditionalLegInfo" version="1.0">
          <property margin="0.000000" parallelLine1="0.000000" parallelLine2="0.000000"/>
        </extension>
      </extensions>
    </waypoint>
    <!--No.38 waypoint-->
    <waypoint id="38" name="Gotheborg Port" radius="1.000000">
      <position lat="57.683965" lon="11.853938"/>
      <leg portsideXTD="0.539957" starboardXTD="0.539957" safetyContour="30" geometryType="Loxodrome" speedMax="22.100000" draughtForward="10.000000" draughtAft="10.000000" staticUKC="30.000000"/>
      <extensions>
        <extension manufacturer="Furuno" name="AdditionalLegInfo" version="1.0">
          <property margin="0.000000" parallelLine1="0.000000" parallelLine2="0.000000"/>
        </extension>
      </extensions>
    </waypoint>
  </waypoints>
  <!--schedules node-->
  <schedules/>
</route>
'''

voyageplanorig='''<?xml version="1.0" encoding="UTF-8"?>
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

textmessage2='''<?xml version="1.0" encoding="utf-8"?>
<textMessage
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xmlns="http://stmvalidation.eu/schemas/textMessageSchema_1_3.xsd">
  <textMessageId>urn:mrn:stm:txt:sma:20170510104400-1</textMessageId>
  <informationObjectReferenceId>urn:mrn:stm:voyage:id:furuno:19700101000000-2-Barcelona-Gothenborg</informationObjectReferenceId>
  <informationObjectReferenceType>RTZ</informationObjectReferenceType>
  <validityPeriodStart>2017-05-01T01:00:00Z</validityPeriodStart>
  <validityPeriodStop>2017-06-10T01:00:00Z</validityPeriodStop>
  <author>urn:mrn:stm:user:sma:mikolo</author>
  <from>urn:mrn:stm:org:sma</from>
  <serviceType>SHIP-VIS</serviceType>
  <createdAt>2017-05-10T01:00:00Z</createdAt>
  <subject>Test message</subject>
  <body>Kliffaa hei</body>
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

textmessage='''<?xml version="1.0" encoding="utf-8"?>
<textMessage
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xmlns="http://stmvalidation.eu/schemas/textMessageSchema_1_3.xsd">
  <textMessageId>urn:mrn:stm:txt:furuno:20170510104400-7</textMessageId>
  <author>urn:mrn:stm:user:sma:mikolo</author>
  <from>urn:mrn:stm:org:sma</from>
  <serviceType>SHIP-VIS</serviceType>
  <createdAt>2017-10-21T01:00:00Z</createdAt>
  <subject>Medea</subject>
  <body>Testing msg from Medea</body>
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

ackmsg = {
  "endpoint": service.url,
  "id": "urn:mrn:s124:NW.SE.local.100.17.P",
  "fromName": service.vis2_name,
  "fromId": service.vis2_uvid,
  "time": "2017-10-24T06:08:44Z",
  "toId": service.conf['id'],
  "toName": service.conf['name']
}

pcmdata1='''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<portCallMessage xmlns="urn:x-mrn:stm:schema:port-call-message:0.0.16">
   <vesselId>urn:x-mrn:stm:vessel:IMO:8016550</vesselId>
   <messageId>urn:mrn:stm:portcdm:message:'''

pcmdata2='''</messageId>
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

pcmfilter='''[
  {
    "type": "VESSEL",
    "element": "urn:x-mrn:stm:vessel:IMO:8016550"
  }
]'''

pcmnofilter='''[
]'''

url=service.url
ackurl=service.callbackurl
vis_cert=service.vis_cert
trustchain=service.trustchain
print('Endpoint: ', url)
print()

print('POST voyageplan')
response=service.post_voyageplan(url, voyageplan, callbackEndpoint = ackurl, deliveryAckEndPoint = ackurl)
print(response.status_code, response.text)
print('POST textmessage')
response=service.post_text(url, textmessage, ackurl)
print(response.status_code, response.text)
print('POST area message')
response=service.post_area(url, area, ackurl)
print(response.status_code, response.text)
print('GET voyage plans')
response=service.get_voyageplan(url)
print(response.status_code, response.text)
print()
print('SUBSCRIBE voyage plans')
response=service.subscribe_voyageplan(service.vis2_uvid)
print(response.status_code, response.text)
print()
print('UNSUBSCRIBE voyage plans')
response=service.unsubscribe_voyageplan(service.vis2_uvid)
print(response.status_code, response.text)
print()
print('POST acknowledgement')
response=service.post_ack(ackmsg)
print(response.status_code, response.text)
print()
#print('POST PCM message')
#msg=pcmdata1 + str(uuid.uuid4()) + pcmdata2
#print(msg)
#response=service.sendpcm(msg)
#print(response.status_code, response.text)


#print('PortCDM create queue')
#response=service.createpcmqueue(pcmnofilter)
#print(response.status_code, response.text)
#with open('pcmqueue.dat','w') as f:
#    f.write(response.text)
#print()

#print(service.createpcmmsg(TTAmsg))

#print('POST PCM message')
#response=service.sendpcm(pcmoldmsg)
#print(response.status_code, response.text)
#print()

#print('POST PCM message')
#response=service.sendpcm(pcmnewmsg)
#print(response.status_code, response.text)
#print()

#print('PortCDM poll queue')
#with open('pcmqueue.dat') as f:
#    guid=f.read()
#response=service.pollpcmqueue(guid)
#print(response.status_code, response.text)

