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
newvoyageuvid='urn:mrn:stm:voyage:id:001:001'
newvoyageuvid2='urn:mrn:stm:voyage:id:001:002'
vis2_uvid=hostsettings.vis2_uvid

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

voyageplan_in_the_past='''<?xml version="1.0"?>
<route version="1.1" 
  xmlns:xsd="http://www.w3.org/2001/XMLSchema"
  xmlns="http://www.cirm.org/RTZ/1/1">
  <routeInfo routeStatus="7" vesselVoyage="urn:mrn:stm:voyage:id:001:002" routeName="HAN-VIS" validityPeriodStart="2016-02-15T10:00:00Z" validityPeriodStop="2016-02-16T10:00:00Z" optimizationMethod="Time table">
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
        <scheduleElement etd="2016-02-15T10:00:00Z" waypointId="1"/>
        <scheduleElement eta="2016-02-15T10:35:00Z" waypointId="2" speed="7.000000"/>
      </calculated>
    </schedule>
  </schedules>
</route>
'''

voyageplan_in_the_past_and_future='''<?xml version="1.0"?>
<route version="1.1" 
  xmlns:xsd="http://www.w3.org/2001/XMLSchema"
  xmlns="http://www.cirm.org/RTZ/1/1">
  <routeInfo routeStatus="7" vesselVoyage="urn:mrn:stm:voyage:id:001:001" routeName="HAN-VIS" validityPeriodStart="2016-02-15T10:00:00Z" validityPeriodStop="2116-02-16T10:00:00Z" optimizationMethod="Time table">
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
        <scheduleElement etd="2016-02-15T10:00:00Z" waypointId="1"/>
        <scheduleElement eta="2116-02-15T10:35:00Z" waypointId="2" speed="7.000000"/>
      </calculated>
    </schedule>
  </schedules>
</route>
'''

voyageplan_in_the_future10='''<?xml version="1.0"?>
<route version="1.0" 
  xmlns:xsd="http://www.w3.org/2001/XMLSchema"
  xmlns="http://www.cirm.org/RTZ/1/0">
  <routeInfo routeStatus="7" vesselVoyage="urn:mrn:stm:voyage:id:001:001" routeName="HAN-VIS" validityPeriodStart="2116-02-15T10:00:00Z" validityPeriodStop="2116-02-16T10:00:00Z" optimizationMethod="Time table">
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

voyageplan_in_the_future11='''<?xml version="1.0"?>
<route version="1.1" 
  xmlns:xsd="http://www.w3.org/2001/XMLSchema"
  xmlns="http://www.cirm.org/RTZ/1/1">
  <routeInfo routeStatus="7" vesselVoyage="urn:mrn:stm:voyage:id:001:001" routeName="HAN-VIS" validityPeriodStart="2116-02-15T10:00:00Z" validityPeriodStop="2116-02-16T10:00:00Z" optimizationMethod="Time table">
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
        <scheduleElement etd="2116-02-15T10:00:00Z" waypointId="1"/>
        <scheduleElement eta="2116-02-15T10:35:00Z" waypointId="2" speed="7.000000"/>
      </calculated>
    </schedule>
  </schedules>
</route>
'''

voyageplan_in_the_futurestm20='''<?xml version="1.0"?>
<route version="1.1" 
  xmlns:xsd="http://www.w3.org/2001/XMLSchema"
  xmlns="http://www.cirm.org/RTZ/1/1">
  <routeInfo routeStatus="7" vesselVoyage="urn:mrn:stm:voyage:id:001:001" routeName="HAN-VIS" validityPeriodStart="2116-02-15T10:00:00Z" validityPeriodStop="2116-02-16T10:00:00Z" optimizationMethod="Time table">
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
        <scheduleElement etd="2116-02-15T10:00:00Z" waypointId="1"/>
        <scheduleElement eta="2116-02-15T10:35:00Z" waypointId="2" speed="7.000000"/>
      </calculated>
    </schedule>
  </schedules>
</route>
'''

voyageplan_incorrect_xml='\
<?xml version="1.0" encoding="UTF-8"?>\
<route version="1.0" xmlns="http://www.cirm.org/RTZ/1/0">\
        <waypoints>\
                <waypoint id="1">\
                        <position lat="53.5123" lon="8.11998"/>\
                </waypoint>\
                <waypoint id="15">\
                        <position lat="53.0492" lon="8.87731"/>\
                </waypoint>\
        </waypoints>\
'

voyageplan_incorrect_schema='\
<?xml version="1.0" encoding="UTF-8"?>\
<route version="1.0" xmlns="http://www.cirm.org/RTZ/3/0">\
    <routeInfo routeStatus="7" vesselVoyage="urn:mrn:stm:voyage:id:001:001" routeName="Test-Mini-1" validityPeriodStart="2100-12-22T13:00:00Z" validityPeriodStop="2100-12-23T13:00:00Z"/>\
        <waypoints>\
                <waypoint id="1">\
                        <position lat="53.5123" lon="8.11998"/>\
                </waypoint>\
                <waypoint id="15">\
                        <position lat="53.0492" lon="8.87731"/>\
                </waypoint>\
        </waypoints>\
</route>\
'

voyageplan_missing_vesselVoyage='''<?xml version="1.0"?>
<route version="1.1" 
  xmlns:xsd="http://www.w3.org/2001/XMLSchema"
  xmlns="http://www.cirm.org/RTZ/1/1">
  <routeInfo routeStatus="7" routeName="HAN-VIS" validityPeriodStart="2017-02-15T10:00:00Z" validityPeriodStop="2017-02-16T10:00:00Z" optimizationMethod="Time table">
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

voyageplan_wrong_syntax_vesselVoyage='''<?xml version="1.0"?>
<route version="1.1" 
  xmlns:xsd="http://www.w3.org/2001/XMLSchema"
  xmlns="http://www.cirm.org/RTZ/1/1">
  <routeInfo routeStatus="7" vesselVoyage="Free text" routeName="HAN-VIS" validityPeriodStart="2017-02-15T10:00:00Z" validityPeriodStop="2017-02-16T10:00:00Z" optimizationMethod="Time table">
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

voyageplan_missing_routeStatus='''<?xml version="1.0"?>
<route version="1.1" 
  xmlns:xsd="http://www.w3.org/2001/XMLSchema"
  xmlns="http://www.cirm.org/RTZ/1/1">
  <routeInfo vesselVoyage="urn:mrn:stm:voyage:id:001:001" routeName="HAN-VIS" validityPeriodStart="2017-02-15T10:00:00Z" validityPeriodStop="2017-02-16T10:00:00Z" optimizationMethod="Time table">
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

voyageplan_wrong_syntax_routeStatus='''<?xml version="1.0"?>
<route version="1.1" 
  xmlns:xsd="http://www.w3.org/2001/XMLSchema"
  xmlns="http://www.cirm.org/RTZ/1/1">
  <routeInfo routeStatus="Free text" vesselVoyage="urn:mrn:stm:voyage:id:001:001" routeName="HAN-VIS" validityPeriodStart="2017-02-15T10:00:00Z" validityPeriodStop="2017-02-16T10:00:00Z" optimizationMethod="Time table">
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

    def vessel_connects(self):
        hostsettings.vessel_connects()
        pass

    def test_VIS_001_00(self):
        """
        VIS-001-0 - Preparation: No voyage plan published with chosen UVID in VIS-1

        
        """
        hostsettings.rm_uvid(newvoyageuvid)
        hostsettings.rm_acl(vis2_uvid)
        hostsettings.rm_subs(vis2_uvid)
        sub='/voyagePlans/subscription'
        parameters={
            'callbackEndpoint': 'delete',
            'uvid': newvoyageuvid
        }
        payload={}
        response=requests.post(url + sub, params=parameters, json=payload, cert=vis_cert, verify=trustchain)

        sub='/voyagePlans/subscription'
        parameters={
            'callbackEndpoint': 'deny',
            'uvid': newvoyageuvid
        }
        payload={}
        response=requests.post(url + sub, params=parameters, json=payload, cert=vis_cert, verify=trustchain)

        parameters={
            'callbackEndpoint': 'deny'
        }
        payload={}
        response=requests.post(url + sub, params=parameters, json=payload, cert=vis_cert, verify=trustchain)

        report='''
VIS001sheet.write(VIS_001_00_row, VIS_001_00_col, "PASS", boldcenter)
'''
        f = open('../create_worksheet.py', 'a')
        f.write(report)
        f.close()
        pass

    def test_VIS_001_01(self):
        """
        VIS-001-1 - VIS-3: Request (get) voyage plan with chosen UVID from VIS-1

        
        """
        sub='/voyagePlans'
        parameters={
            'uvid': newvoyageuvid
        }
        response=requests.get(url + sub, params=parameters, cert=vis_cert, verify=trustchain)

        if response.status_code == 404:
            report='''
VIS001sheet.write(VIS_001_01_row, VIS_001_01_col, "PASS", boldcenter)
VIS001sheet.write(VIS_001_01_row, VIS_001_01_col - 1, "''' + response.reason + '", normal)'
        else:
            report='''
VIS001sheet.write(VIS_001_01_row, VIS_001_01_col, "FAIL", boldcenter)
VIS001sheet.write(VIS_001_01_row, VIS_001_01_col - 1, "''' + response.reason + '", normal)'
        f = open('../create_worksheet.py', 'a')
        f.write(report)
        f.close()

        self.assert404(response, "Response body is : " + response.text)

    def test_VIS_001_02(self):
        """
        VIS-001-2 - VIS-3: Subscribe to voyage plan with chosen UVID from VIS-1

        
        """
        sub='/voyagePlans/subscription'
        parameters={
            'callbackEndpoint': callbackurl,
            'uvid': newvoyageuvid
        }
        payload={}
        response=requests.post(url + sub, params=parameters, json=payload, cert=vis_cert, verify=trustchain)

        if response.status_code == 404:
            report='''
VIS001sheet.write(VIS_001_02_row, VIS_001_02_col, "PASS", boldcenter)
VIS001sheet.write(VIS_001_02_row, VIS_001_02_col - 1, "''' + response.reason + '", normal)'
        else:
            report='''
VIS001sheet.write(VIS_001_02_row, VIS_001_02_col, "FAIL", boldcenter)
VIS001sheet.write(VIS_001_02_row, VIS_001_02_col - 1, "''' + response.reason + '", normal)'
        f = open('../create_worksheet.py', 'a')
        f.write(report)
        f.close()

        self.assert404(response, "Response body is : " + response.text)

    def test_VIS_001_03(self):
        """
        VIS-001-3 - Publish voyage plan to VIS-1 with chosen UVID

        
        """
        sub='/voyagePlans'
        payload=voyageplan
        response=requests.post(url + sub, data=payload, cert=vis_cert, verify=trustchain)

        if response.status_code == 200:
            report='''
VIS001sheet.write(VIS_001_03_row, VIS_001_03_col, "PASS", boldcenter)
VIS001sheet.write(VIS_001_03_row, VIS_001_03_col - 1, "''' + response.reason + '", normal)'
        else:
            report='''
VIS001sheet.write(VIS_001_03_row, VIS_001_03_col, "FAIL", boldcenter)
VIS001sheet.write(VIS_001_03_row, VIS_001_03_col - 1, "''' + response.reason + '", normal)'
        f = open('../create_worksheet.py', 'a')
        f.write(report)
        f.close()
        print(response.text)

        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_001_04(self):
        """
        VIS-001-4 - VIS-3: Request voyage plan with chosen UVID from VIS-1

        
        """
        sub='/voyagePlans'
        parameters={
            'uvid': newvoyageuvid
        }
        response=requests.get(url + sub, params=parameters, cert=vis_cert, verify=trustchain)

        if response.status_code == 403:
            report='''
VIS001sheet.write(VIS_001_04_row, VIS_001_04_col, "PASS", boldcenter)
VIS001sheet.write(VIS_001_04_row, VIS_001_04_col - 1, "''' + response.reason + '", normal)'
        else:
            report='''
VIS001sheet.write(VIS_001_04_row, VIS_001_04_col, "FAIL", boldcenter)
VIS001sheet.write(VIS_001_04_row, VIS_001_04_col - 1, "''' + response.reason + '", normal)'
        f = open('../create_worksheet.py', 'a')
        f.write(report)
        f.close()

        self.assert403(response, "Response body is : " + response.text)

    def test_VIS_001_05(self):
        """
        VIS-001-5 - VIS-2: Subscribe to voyage plan with chosen UVID from VIS-1

        
        """
        sub='/voyagePlans/subscription'
        parameters={
            'callbackEndpoint': callbackurl,
            'uvid': newvoyageuvid
        }
        payload={}
        response=requests.post(url + sub, params=parameters, json=payload, cert=vis_cert, verify=trustchain)

        if response.status_code == 403:
            report='''
VIS001sheet.write(VIS_001_05_row, VIS_001_05_col, "PASS", boldcenter)
VIS001sheet.write(VIS_001_05_row, VIS_001_05_col - 1, "''' + response.reason + '", normal)'
        else:
            report='''
VIS001sheet.write(VIS_001_05_row, VIS_001_05_col, "FAIL", boldcenter)
VIS001sheet.write(VIS_001_05_row, VIS_001_05_col - 1, "''' + response.reason + '", normal)'
        f = open('../create_worksheet.py', 'a')
        f.write(report)
        f.close()

        self.assert403(response, "Response body is : " + response.text)

    def test_VIS_001_06(self):
        """
        VIS-001-6 - VIS-1: Authorize organisation for VIS-2 to chosen UVID in VIS-1

        
        """
        hostsettings.set_acl(vis2_uvid, newvoyageuvid)
        sub='/voyagePlans/subscription'
        parameters={
            'callbackEndpoint': 'allow',
            'uvid': newvoyageuvid
        }
        payload={}
        response=requests.post(url + sub, params=parameters, json=payload, cert=vis_cert, verify=trustchain)

        report='''
VIS001sheet.write(VIS_001_06_row, VIS_001_06_col, "PASS", boldcenter)
'''
        f = open('../create_worksheet.py', 'a')
        f.write(report)
        f.close()

        pass

    def test_VIS_001_07(self):
        """
        VIS-001-7 - VIS-2: Request voyage plan with chosen UVID from VIS-1

        
        """
        sub='/voyagePlans'
        parameters={
            'uvid': newvoyageuvid
        }
        response=requests.get(url + sub, params=parameters, cert=vis_cert, verify=trustchain)

        if response.status_code == 200:
            report='''
VIS001sheet.write(VIS_001_07_row, VIS_001_07_col, "PASS", boldcenter)
VIS001sheet.write(VIS_001_07_row, VIS_001_07_col - 1, "''' + response.reason + '", normal)'
        else:
            report='''
VIS001sheet.write(VIS_001_07_row, VIS_001_07_col, "FAIL", boldcenter)
VIS001sheet.write(VIS_001_07_row, VIS_001_07_col - 1, "''' + response.reason + '", normal)'
        f = open('../create_worksheet.py', 'a')
        f.write(report)
        f.close()

        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_001_08(self):
        """
        VIS-001-8 - VIS-2: Subscribe to voyage plan with chosen UVID from VIS-1

        
        """
        sub='/voyagePlans/subscription'
        parameters={
            'callbackEndpoint': callbackurl,
            'uvid': newvoyageuvid
        }
        payload={}
        response=requests.post(url + sub, params=parameters, json=payload, cert=vis_cert, verify=trustchain)

        if response.status_code == 200:
            report='''
VIS001sheet.write(VIS_001_08_row, VIS_001_08_col, "PASS", boldcenter)
VIS001sheet.write(VIS_001_08_row, VIS_001_08_col - 1, "''' + response.reason + '", normal)'
        else:
            report='''
VIS001sheet.write(VIS_001_08_row, VIS_001_08_col, "FAIL", boldcenter)
VIS001sheet.write(VIS_001_08_row, VIS_001_08_col - 1, "''' + response.reason + '", normal)'
        f = open('../create_worksheet.py', 'a')
        f.write(report)
        f.close()

        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_001_09(self):
        """
        VIS-001-9 - VIS-1: Remove authorization to organisation for VIS-2 to chosen UVID

        
        """
        hostsettings.rm_acl(vis2_uvid, newvoyageuvid)
        sub='/voyagePlans/subscription'
        parameters={
            'callbackEndpoint': 'deny',
            'uvid': newvoyageuvid
        }
        payload={}
        response=requests.post(url + sub, params=parameters, json=payload, cert=vis_cert, verify=trustchain)

        report='''
VIS001sheet.write(VIS_001_09_row, VIS_001_09_col, "PASS", boldcenter)
'''
        f = open('../create_worksheet.py', 'a')
        f.write(report)
        f.close()

        pass

    def test_VIS_001_10(self):
        """
        VIS-001-10 - VIS-2: Request voyage plan with chosen UVID from VIS-1

        
        """
        sub='/voyagePlans'
        parameters={
            'uvid': newvoyageuvid
        }
        response=requests.get(url + sub, params=parameters, cert=vis_cert, verify=trustchain)

        if response.status_code == 403:
            report='''
VIS001sheet.write(VIS_001_10_row, VIS_001_10_col, "PASS", boldcenter)
VIS001sheet.write(VIS_001_10_row, VIS_001_10_col - 1, "''' + response.reason + '", normal)'
        else:
            report='''
VIS001sheet.write(VIS_001_10_row, VIS_001_10_col, "FAIL", boldcenter)
VIS001sheet.write(VIS_001_10_row, VIS_001_10_col - 1, "''' + response.reason + '", normal)'
        f = open('../create_worksheet.py', 'a')
        f.write(report)
        f.close()

        self.assert403(response, "Response body is : " + response.text)

    def test_VIS_001_11(self):
        """
        VIS-001-11 - VIS-2: Subscribe to voyage plan with chosen UVID from VIS-1

        
        """
        sub='/voyagePlans/subscription'
        parameters={
            'callbackEndpoint': callbackurl,
            'uvid': newvoyageuvid
        }
        payload={}
        response=requests.post(url + sub, params=parameters, json=payload, cert=vis_cert, verify=trustchain)

        if response.status_code == 403:
            report='''
VIS001sheet.write(VIS_001_11_row, VIS_001_11_col, "PASS", boldcenter)
VIS001sheet.write(VIS_001_11_row, VIS_001_11_col - 1, "''' + response.reason + '", normal)'
        else:
            report='''
VIS001sheet.write(VIS_001_11_row, VIS_001_11_col, "FAIL", boldcenter)
VIS001sheet.write(VIS_001_11_row, VIS_001_11_col - 1, "''' + response.reason + '", normal)'
        f = open('../create_worksheet.py', 'a')
        f.write(report)
        f.close()

        self.assert403(response, "Response body is : " + response.text)

    def test_VIS_001_12_3_1(self):
        """
        VIS-001-3-1 - Select VP with validityPeriodStart and validityPeriodStop in past and publish to VIS-1


        """
        sub='/voyagePlans'
        payload=voyageplan_in_the_past
        response=requests.post(url + sub, data=payload, cert=vis_cert, verify=trustchain)

        if response.status_code == 200:
            report='''
VIS001sheet.write(VIS_001_12_3_1_row, VIS_001_12_3_1_col, "PASS", boldcenter)
VIS001sheet.write(VIS_001_12_3_1_row, VIS_001_12_3_1_col - 1, "''' + response.reason + '", normal)'
        else:
            report='''
VIS001sheet.write(VIS_001_12_3_1_row, VIS_001_12_3_1_col, "FAIL", boldcenter)
VIS001sheet.write(VIS_001_12_3_1_row, VIS_001_12_3_1_col - 1, "''' + response.reason + '", normal)'
        f = open('../create_worksheet.py', 'a')
        f.write(report)
        f.close()

        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_001_12_3_2(self):
        """
        VIS-001-3-2 - Change validityPeriodStop to future and publish to VIS-1


        """
        sub='/voyagePlans'
        payload=voyageplan_in_the_past_and_future
        response=requests.post(url + sub, data=payload, cert=vis_cert, verify=trustchain)

        if response.status_code == 200:
            report='''
VIS001sheet.write(VIS_001_12_3_2_row, VIS_001_12_3_2_col, "PASS", boldcenter)
VIS001sheet.write(VIS_001_12_3_2_row, VIS_001_12_3_2_col - 1, "''' + response.reason + '", normal)'
        else:
            report='''
VIS001sheet.write(VIS_001_12_3_2_row, VIS_001_12_3_2_col, "FAIL", boldcenter)
VIS001sheet.write(VIS_001_12_3_2_row, VIS_001_12_3_2_col - 1, "''' + response.reason + '", normal)'
        f = open('../create_worksheet.py', 'a')
        f.write(report)
        f.close()

        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_001_12_3_3(self):
        """
        VIS-001-3-3 - Change validityPeriodStart to future and publish to VIS-1


        """
        sub='/voyagePlans'
        payload=voyageplan_in_the_future11
        response=requests.post(url + sub, data=payload, cert=vis_cert, verify=trustchain)

        if response.status_code == 200:
            report='''
VIS001sheet.write(VIS_001_12_3_3_row, VIS_001_12_3_3_col, "PASS", boldcenter)
VIS001sheet.write(VIS_001_12_3_3_row, VIS_001_12_3_3_col - 1, "''' + response.reason + '", normal)'
        else:
            report='''
VIS001sheet.write(VIS_001_12_3_3_row, VIS_001_12_3_3_col, "FAIL", boldcenter)
VIS001sheet.write(VIS_001_12_3_3_row, VIS_001_12_3_3_col - 1, "''' + response.reason + '", normal)'
        f = open('../create_worksheet.py', 'a')
        f.write(report)
        f.close()

        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_001_12_4_1(self):
        """
        VIS-001-4-1 - Select VP according to schema RTZ 1.0 and publish to VIS-1


        """
        sub='/voyagePlans'
        payload=voyageplan_in_the_future10
        response=requests.post(url + sub, data=payload, cert=vis_cert, verify=trustchain)

        if response.status_code == 200:
            report='''
VIS001sheet.write(VIS_001_12_4_1_row, VIS_001_12_4_1_col, "PASS", boldcenter)
VIS001sheet.write(VIS_001_12_4_1_row, VIS_001_12_4_1_col - 1, "''' + response.reason + '", normal)'
        else:
            report='''
VIS001sheet.write(VIS_001_12_4_1_row, VIS_001_12_4_1_col, "FAIL", boldcenter)
VIS001sheet.write(VIS_001_12_4_1_row, VIS_001_12_4_1_col - 1, "''' + response.reason + '", normal)'
        f = open('../create_worksheet.py', 'a')
        f.write(report)
        f.close()

        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_001_12_4_2(self):
        """
        VIS-001-4-2 - Select VP according to schema RTZ 1.1 and publish to VIS-1


        """
        sub='/voyagePlans'
        payload=voyageplan_in_the_future11
        response=requests.post(url + sub, data=payload, cert=vis_cert, verify=trustchain)

        if response.status_code == 200:
            report='''
VIS001sheet.write(VIS_001_12_4_2_row, VIS_001_12_4_2_col, "PASS", boldcenter)
VIS001sheet.write(VIS_001_12_4_2_row, VIS_001_12_4_2_col - 1, "''' + response.reason + '", normal)'
        else:
            report='''
VIS001sheet.write(VIS_001_12_4_2_row, VIS_001_12_4_2_col, "FAIL", boldcenter)
VIS001sheet.write(VIS_001_12_4_2_row, VIS_001_12_4_2_col - 1, "''' + response.reason + '", normal)'
        f = open('../create_worksheet.py', 'a')
        f.write(report)
        f.close()

        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_001_12_4_3(self):
        """
        VIS-001-4-3 - Select VP according to schema RTZ 2.0 and publish to VIS-1


        """
        sub='/voyagePlans'
        payload=voyageplan_in_the_futurestm20
        response=requests.post(url + sub, data=payload, cert=vis_cert, verify=trustchain)

        if response.status_code == 200:
            report='''
VIS001sheet.write(VIS_001_12_4_3_row, VIS_001_12_4_3_col, "PASS", boldcenter)
VIS001sheet.write(VIS_001_12_4_3_row, VIS_001_12_4_3_col - 1, "''' + response.reason + '", normal)'
        else:
            report='''
VIS001sheet.write(VIS_001_12_4_3_row, VIS_001_12_4_3_col, "FAIL", boldcenter)
VIS001sheet.write(VIS_001_12_4_3_row, VIS_001_12_4_3_col - 1, "''' + response.reason + '", normal)'
        f = open('../create_worksheet.py', 'a')
        f.write(report)
        f.close()

        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_001_12_5_1(self):
        """
        VIS-001-5-1 - Select VP in incorrect XML and publish to VIS-1 


        """
        sub='/voyagePlans'
        payload=voyageplan_incorrect_xml
        response=requests.post(url + sub, data=payload, cert=vis_cert, verify=trustchain)

        if response.status_code == 500:
            report='''
VIS001sheet.write(VIS_001_12_5_1_row, VIS_001_12_5_1_col, "PASS", boldcenter)
VIS001sheet.write(VIS_001_12_5_1_row, VIS_001_12_5_1_col - 1, "''' + response.reason + '", normal)'
        else:
            report='''
VIS001sheet.write(VIS_001_12_5_1_row, VIS_001_12_5_1_col, "FAIL", boldcenter)
VIS001sheet.write(VIS_001_12_5_1_row, VIS_001_12_5_1_col - 1, "''' + response.reason + '", normal)'
        f = open('../create_worksheet.py', 'a')
        f.write(report)
        f.close()

        self.assert500(response, "Response body is : " + response.text)

    def test_VIS_001_12_5_2(self):
        """
        VIS-001-5-2 - Select VP not following schema RTZ  and publish to VIS-1 


        """
        sub='/voyagePlans'
        payload=voyageplan_incorrect_schema
        response=requests.post(url + sub, data=payload, cert=vis_cert, verify=trustchain)

        if response.status_code == 400:
            report='''
VIS001sheet.write(VIS_001_12_5_2_row, VIS_001_12_5_2_col, "PASS", boldcenter)
VIS001sheet.write(VIS_001_12_5_2_row, VIS_001_12_5_2_col - 1, "''' + response.reason + '", normal)'
        else:
            report='''
VIS001sheet.write(VIS_001_12_5_2_row, VIS_001_12_5_2_col, "FAIL", boldcenter)
VIS001sheet.write(VIS_001_12_5_2_row, VIS_001_12_5_2_col - 1, "''' + response.reason + '", normal)'
        f = open('../create_worksheet.py', 'a')
        f.write(report)
        f.close()

        self.assert400(response, "Response body is : " + response.text)

    def test_VIS_001_12_6_1(self):
        """
        VIS-001-6-1 - Select VP for another ship and publish to subscribers


        """
        sub='/voyagePlans'
        payload=voyageplan
        response=requests.post(url + sub, data=payload, cert=vis_cert, verify=trustchain)

        if response.status_code == 200:
            report='''
VIS001sheet.write(VIS_001_12_6_1_row, VIS_001_12_6_1_col, "PASS", boldcenter)
VIS001sheet.write(VIS_001_12_6_1_row, VIS_001_12_6_1_col - 1, "''' + response.reason + '", normal)'
        else:
            report='''
VIS001sheet.write(VIS_001_12_6_1_row, VIS_001_12_6_1_col, "FAIL", boldcenter)
VIS001sheet.write(VIS_001_12_6_1_row, VIS_001_12_6_1_col - 1, "''' + response.reason + '", normal)'
        f = open('../create_worksheet.py', 'a')
        f.write(report)
        f.close()

        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_001_12_7_1(self):
        """
        VIS-001-7-1 - Select voyage plan with missing vesselVoyage and publish to subscribers


        """
        sub='/voyagePlans'
        payload=voyageplan_missing_vesselVoyage
        response=requests.post(url + sub, data=payload, cert=vis_cert, verify=trustchain)

        if response.status_code == 404:
            report='''
VIS001sheet.write(VIS_001_12_7_1_row, VIS_001_12_7_1_col, "PASS", boldcenter)
VIS001sheet.write(VIS_001_12_7_1_row, VIS_001_12_7_1_col - 1, "''' + response.reason + '", normal)'
        else:
            report='''
VIS001sheet.write(VIS_001_12_7_1_row, VIS_001_12_7_1_col, "FAIL", boldcenter)
VIS001sheet.write(VIS_001_12_7_1_row, VIS_001_12_7_1_col - 1, "''' + response.reason + '", normal)'
        f = open('../create_worksheet.py', 'a')
        f.write(report)
        f.close()

        self.assert404(response, "Response body is : " + response.text)

    def test_VIS_001_12_7_2(self):
        """
        VIS-001-7-2 - Select voyage plan with incorrect syntax of  vesselVoyage and publish to subscribers


        """
        sub='/voyagePlans'
        payload=voyageplan_wrong_syntax_vesselVoyage
        response=requests.post(url + sub, data=payload, cert=vis_cert, verify=trustchain)

        if response.status_code == 400:
            report='''
VIS001sheet.write(VIS_001_12_7_2_row, VIS_001_12_7_2_col, "PASS", boldcenter)
VIS001sheet.write(VIS_001_12_7_2_row, VIS_001_12_7_2_col - 1, "''' + response.reason + '", normal)'
        else:
            report='''
VIS001sheet.write(VIS_001_12_7_2_row, VIS_001_12_7_2_col, "FAIL", boldcenter)
VIS001sheet.write(VIS_001_12_7_2_row, VIS_001_12_7_2_col - 1, "''' + response.reason + '", normal)'
        f = open('../create_worksheet.py', 'a')
        f.write(report)
        f.close()

        self.assert400(response, "Response body is : " + response.text)

    def test_VIS_001_12_7_3(self):
        """
        VIS-001-7-3 - Select voyage plan with missing routeStatus and publish to subscribers


        """
        sub='/voyagePlans'
        payload=voyageplan_missing_routeStatus
        response=requests.post(url + sub, data=payload, cert=vis_cert, verify=trustchain)

        if response.status_code == 404:
            report='''
VIS001sheet.write(VIS_001_12_7_3_row, VIS_001_12_7_3_col, "PASS", boldcenter)
VIS001sheet.write(VIS_001_12_7_3_row, VIS_001_12_7_3_col - 1, "''' + response.reason + '", normal)'
        else:
            report='''
VIS001sheet.write(VIS_001_12_7_3_row, VIS_001_12_7_3_col, "FAIL", boldcenter)
VIS001sheet.write(VIS_001_12_7_3_row, VIS_001_12_7_3_col - 1, "''' + response.reason + '", normal)'
        f = open('../create_worksheet.py', 'a')
        f.write(report)
        f.close()

        self.assert404(response, "Response body is : " + response.text)

    def test_VIS_001_12_7_4(self):
        """
        VIS-001-7-4 - Select voyage plan with incorrect syntax of  routeStatus and publish to subscribers


        """
        sub='/voyagePlans'
        payload=voyageplan_wrong_syntax_routeStatus
        response=requests.post(url + sub, data=payload, cert=vis_cert, verify=trustchain)

        if response.status_code == 400:
            report='''
VIS001sheet.write(VIS_001_12_7_4_row, VIS_001_12_7_4_col, "PASS", boldcenter)
VIS001sheet.write(VIS_001_12_7_4_row, VIS_001_12_7_4_col - 1, "''' + response.reason + '", normal)'
        else:
            report='''
VIS001sheet.write(VIS_001_12_7_4_row, VIS_001_12_7_4_col, "FAIL", boldcenter)
VIS001sheet.write(VIS_001_12_7_4_row, VIS_001_12_7_4_col - 1, "''' + response.reason + '", normal)'
        f = open('../create_worksheet.py', 'a')
        f.write(report)
        f.close()

        self.assert400(response, "Response body is : " + response.text)

    def test_VIS_001_12_7_5(self):
        """
        VIS-001-7-5 - Test cleanup


        
        """
        sub='/voyagePlans/subscription'
        parameters={
            'callbackEndpoint': 'delete',
            'uvid': newvoyageuvid
        }
        payload={}
        response=requests.post(url + sub, params=parameters, json=payload, cert=vis_cert, verify=trustchain)
        sub='/voyagePlans/subscription'
        parameters={
            'callbackEndpoint': 'delete',
            'uvid': newvoyageuvid2
        }
        payload={}
        response=requests.post(url + sub, params=parameters, json=payload, cert=vis_cert, verify=trustchain)
        sub='/voyagePlans/subscription'
        parameters={
            'callbackEndpoint': callbackurl,
            'uvid': newvoyageuvid
        }
        payload={}
        response=requests.delete(url + sub, params=parameters, json=payload, cert=vis_cert, verify=trustchain)
        vis2_uvid='urn:mrn:stm:service:instance:furuno:vis2'
        p = Path('import')
        files = list(p.glob('**/' + newvoyageuvid + '.*'))
        for item in files:
            os.remove(str(item))
        files = list(p.glob('**/' + newvoyageuvid2 + '.*'))
        for item in files:
            os.remove(str(item))
        files = list(p.glob('**/' + vis2_uvid + '*'))
        for item in files:
            os.remove(str(item))
        files = list(p.glob('**/parse*'))
        for item in files:
            os.remove(str(item))

        p = Path('export')
        files = list(p.glob('**/' + newvoyageuvid + '.*'))
        for item in files:
            os.remove(str(item))
        files = list(p.glob('**/' + newvoyageuvid2 + '.*'))
        for item in files:
            os.remove(str(item))
        files = list(p.glob('**/' + vis2_uvid + '*'))
        for item in files:
            os.remove(str(item))
        files = list(p.glob('**/parse*'))
        for item in files:
            os.remove(str(item))
        pass

if __name__ == '__main__':
    unittest.main()


