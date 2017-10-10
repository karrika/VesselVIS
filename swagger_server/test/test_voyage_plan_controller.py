# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.get_subscription_response import GetSubscriptionResponse
from swagger_server.models.get_voyage_plan_response import GetVoyagePlanResponse
from swagger_server.models.voyage_plan import VoyagePlan
from . import BaseTestCase
from six import BytesIO
from flask import json
from pathlib import Path
import os
import unittest

voyageuvid='urn:mrn:stm:voyage:id:8320767:2017021010'
vis_uvid='urn:mrn:stm:service:instance:furuno:vis2'
newplan='urn:mrn:stm:voyage:id:new:plan'
callbackEndpoint='http://localhost:8002'

f = open('export/all.acl', 'w')
data=[ vis_uvid ]
f.write(json.dumps(data))
f.close()

voyageplan='''<?xml version="1.0" encoding="UTF-8"?>
<!--route node-->
<route version="1.1" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:stm="http://stmvalidation.eu/STM/1/0/0" xsi:schemaLocation="http://stmvalidation.eu/STM/1/0/0 stm_extensions.xsd" xmlns="http://www.cirm.org/RTZ/1/1">
  <!--routeInfo node-->
  <routeInfo routeName="HELUME" validityPeriodStart="2017-10-09T12:00:00Z" validityPeriodStop="2017-10-10T19:00:00Z" vesselName="FURUNO KOEAJO" vesselMMSI="230031001" vesselIMO="7917551" vesselVoyage="urn:mrn:stm:voyage:id:Furuno:20171006132651-15-HELUME" optimizationMethod="Time table">
    <extensions>
      <extension xsi:type="stm:RouteInfoExtension" manufacturer="STM" name="routeInfoEx" version="1.0.0" routeStatusEnum="7" depPort="SEGOT" arrPort="SEUME">
        <stm:routeChanges/>
      </extension>
      <extension manufacturer="Furuno" name="AdditionalRouteInfo" version="1.0">
        <property income="0" channelLimitMode="0" safetyContour="10" ukcLimit="30.000000"/>
      </extension>
    </extensions>
  </routeInfo>
  <!--waypoints node-->
  <waypoints>
    <!--No.1 waypoint-->
    <waypoint id="1" name="" radius="0.800000">
      <position lat="60.163433" lon="24.708550"/>
    </waypoint>
    <!--No.2 waypoint-->
    <waypoint id="2" name="" radius="0.800000">
      <position lat="59.794683" lon="24.523083"/>
      <leg portsideXTD="0.099892" starboardXTD="0.099892" safetyContour="10" geometryType="Loxodrome" speedMax="22.100000" draughtForward="10.000000" draughtAft="10.000000" staticUKC="30.000000"/>
      <extensions>
        <extension manufacturer="Furuno" name="AdditionalLegInfo" version="1.0">
          <property margin="40.000000" parallelLine1="0.000000" parallelLine2="0.000000"/>
        </extension>
      </extensions>
    </waypoint>
    <!--No.3 waypoint-->
    <waypoint id="3" name="" radius="0.800000">
      <position lat="59.498433" lon="20.900950"/>
      <leg portsideXTD="0.099892" starboardXTD="0.099892" safetyContour="10" geometryType="Loxodrome" speedMax="22.100000" draughtForward="10.000000" draughtAft="10.000000" staticUKC="30.000000"/>
      <extensions>
        <extension manufacturer="Furuno" name="AdditionalLegInfo" version="1.0">
          <property margin="40.000000" parallelLine1="0.000000" parallelLine2="0.000000"/>
        </extension>
      </extensions>
    </waypoint>
    <!--No.4 waypoint-->
    <waypoint id="4" name="" radius="0.800000">
      <position lat="60.191217" lon="19.091933"/>
      <leg portsideXTD="0.099892" starboardXTD="0.099892" safetyContour="10" geometryType="Loxodrome" speedMax="22.100000" draughtForward="10.000000" draughtAft="10.000000" staticUKC="30.000000"/>
      <extensions>
        <extension manufacturer="Furuno" name="AdditionalLegInfo" version="1.0">
          <property margin="40.000000" parallelLine1="0.000000" parallelLine2="0.000000"/>
        </extension>
      </extensions>
    </waypoint>
    <!--No.5 waypoint-->
    <waypoint id="5" name="" radius="0.800000">
      <position lat="60.773083" lon="19.052767"/>
      <leg portsideXTD="0.099892" starboardXTD="0.099892" safetyContour="10" geometryType="Loxodrome" speedMax="22.100000" draughtForward="10.000000" draughtAft="10.000000" staticUKC="30.000000"/>
      <extensions>
        <extension manufacturer="Furuno" name="AdditionalLegInfo" version="1.0">
          <property margin="40.000000" parallelLine1="0.000000" parallelLine2="0.000000"/>
        </extension>
      </extensions>
    </waypoint>
    <!--No.6 waypoint-->
    <waypoint id="6" name="" radius="0.800000">
      <position lat="62.689833" lon="19.531500"/>
      <leg portsideXTD="0.099892" starboardXTD="0.099892" safetyContour="10" geometryType="Loxodrome" speedMax="22.100000" draughtForward="10.000000" draughtAft="10.000000" staticUKC="30.000000"/>
      <extensions>
        <extension manufacturer="Furuno" name="AdditionalLegInfo" version="1.0">
          <property margin="40.000000" parallelLine1="0.000000" parallelLine2="0.000000"/>
        </extension>
      </extensions>
    </waypoint>
    <!--No.7 waypoint-->
    <waypoint id="7" name="" radius="0.800000">
      <position lat="63.470867" lon="20.710450"/>
      <leg portsideXTD="0.099892" starboardXTD="0.099892" safetyContour="10" geometryType="Loxodrome" speedMax="22.100000" draughtForward="10.000000" draughtAft="10.000000" staticUKC="30.000000"/>
      <extensions>
        <extension manufacturer="Furuno" name="AdditionalLegInfo" version="1.0">
          <property margin="40.000000" parallelLine1="0.000000" parallelLine2="0.000000"/>
        </extension>
      </extensions>
    </waypoint>
    <!--No.8 waypoint-->
    <waypoint id="8" name="" radius="0.800000">
      <position lat="63.638017" lon="20.374267"/>
      <leg portsideXTD="0.099892" starboardXTD="0.099892" safetyContour="10" geometryType="Loxodrome" speedMax="22.100000" draughtForward="10.000000" draughtAft="10.000000" staticUKC="30.000000"/>
      <extensions>
        <extension manufacturer="Furuno" name="AdditionalLegInfo" version="1.0">
          <property margin="40.000000" parallelLine1="0.000000" parallelLine2="0.000000"/>
        </extension>
      </extensions>
    </waypoint>
    <!--No.9 waypoint-->
    <waypoint id="9" name="" radius="0.800000">
      <position lat="63.654767" lon="20.340667"/>
      <leg portsideXTD="0.099892" starboardXTD="0.099892" safetyContour="10" geometryType="Loxodrome" speedMax="22.100000" draughtForward="10.000000" draughtAft="10.000000" staticUKC="30.000000"/>
      <extensions>
        <extension manufacturer="Furuno" name="AdditionalLegInfo" version="1.0">
          <property margin="40.000000" parallelLine1="0.000000" parallelLine2="0.000000"/>
        </extension>
      </extensions>
    </waypoint>
  </waypoints>
  <!--schedules node-->
  <schedules>
    <schedule id="1">
      <calculated>
        <scheduleElement etd="2017-10-09T12:00:00Z" waypointId="1"/>
        <scheduleElement eta="2017-10-09T13:41:00Z" waypointId="2" speed="13.700000"/>
        <scheduleElement eta="2017-10-09T21:48:00Z" waypointId="3" speed="13.700000"/>
        <scheduleElement eta="2017-10-10T02:48:00Z" waypointId="4" speed="13.700000"/>
        <scheduleElement eta="2017-10-10T05:20:00Z" waypointId="5" speed="13.700000"/>
        <scheduleElement eta="2017-10-10T13:48:00Z" waypointId="6" speed="13.700000"/>
        <scheduleElement eta="2017-10-10T17:57:00Z" waypointId="7" speed="13.700000"/>
        <scheduleElement eta="2017-10-10T18:54:00Z" waypointId="8" speed="13.700000"/>
        <scheduleElement eta="2017-10-10T19:00:00Z" waypointId="9" speed="13.700000"/>
      </calculated>
    </schedule>
  </schedules>
</route>
'''

class TestVoyagePlanController(BaseTestCase):
    """ VoyagePlanController integration test stubs """

    def test_1_upload_voyage_plan(self):
        """
        Test case for upload_voyage_plan

        
        """
        query_string = [('callbackEndpoint', 'http://localhost:8002')]
        response = self.client.open('/voyagePlans',
                                    method='POST',
                                    data=voyageplan.encode('utf-8'),
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_2_subscribe_to_voyage_plan_found(self):
        """
        Test case for subscribe_to_voyage_plan
        A voyage with this uid exists.
        
        """
        query_string = [('callbackEndpoint', 'http://localhost:8002'),
                        ('uvid', 'urn:mrn:stm:voyage:id:8320767:2017021010')]
        response = self.client.open('/voyagePlans/subscription',
                                    method='POST',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_3_get_subscription_to_voyage_plans(self):
        """
        Test case for get_subscription_to_voyage_plans

        
        """
        query_string = [('callbackEndpoint', callbackEndpoint)]
        response = self.client.open('/voyagePlans/subscription',
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_4_get_voyage_plans(self):
        """
        Test case for get_voyage_plans

        
        """
        query_string = []
        response = self.client.open('/voyagePlans',
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_5_remove_voyage_plan_subscription(self):
        """
        Test case for remove_voyage_plan_subscription

        
        """
        query_string = [('callbackEndpoint', callbackEndpoint),
                        ('uvid', voyageuvid)]
        response = self.client.open('/voyagePlans/subscription',
                                    method='DELETE',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_upload_voyage_plan_cleanup(self):
        """
        Test case for upload_voyage_plan cleanup

        
        """
        '''
        vis2_uvid='urn:mrn:stm:service:instance:furuno:vis2'
        p = Path('import')
        files = list(p.glob('**/' + voyageuvid + '.acl'))
        for item in files:
            os.remove(str(item))
        files = list(p.glob('**/' + voyageuvid + '.subs'))
        for item in files:
            os.remove(str(item))
        files = list(p.glob('**/' + vis2_uvid + '*'))
        for item in files:
            os.remove(str(item))
        files = list(p.glob('**/parse*'))
        for item in files:
            os.remove(str(item))
        files = list(p.glob('**/' + newplan + '*'))
        for item in files:
            os.remove(str(item))

        p = Path('export')
        files = list(p.glob('**/' + voyageuvid + '.acl'))
        for item in files:
            os.remove(str(item))
        files = list(p.glob('**/' + voyageuvid + '.subs'))
        for item in files:
            os.remove(str(item))
        files = list(p.glob('**/' + vis2_uvid + '*'))
        for item in files:
            os.remove(str(item))
        files = list(p.glob('**/parse*'))
        for item in files:
            os.remove(str(item))
        files = list(p.glob('**/' + newplan + '*'))
        for item in files:
            os.remove(str(item))
        '''
        pass

if __name__ == '__main__':
    import unittest
    unittest.main()
