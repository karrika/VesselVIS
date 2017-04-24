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

f = open('export/' + voyageuvid + '.acl', 'w')
data=[ vis_uvid ]
f.write(json.dumps(data))
f.close()

class TestVoyagePlanController(BaseTestCase):
    """ VoyagePlanController integration test stubs """

    def test_1_upload_voyage_plan(self):
        """
        Test case for upload_voyage_plan

        
        """
        voyagePlan = VoyagePlan()
        voyagePlan='''<?xml version="1.0" encoding="UTF-8"?>
<route version="1.1" 
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xmlns:stm="http://stmvalidation.eu/STM/1/0/0"
  xsi:schemaLocation="http://stmvalidation.eu/STM/1/0/0 stm_extensions.xsd"
  xmlns="http://www.cirm.org/RTZ/1/1">
  <routeInfo vesselVoyage="urn:mrn:stm:voyage:id:new:plan" routeName="HAN-VIS" validityPeriodStart="2017-02-15T10:00:00Z" validityPeriodStop="2017-02-16T10:00:00Z" optimizationMethod="Time table">
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
        query_string = [('deliveryAckEndPoint', 'http://localhost:8002'),
                        ('callbackEndpoint', 'http://localhost:8002')]
        response = self.client.open('/voyagePlans',
                                    method='POST',
                                    data=voyagePlan,
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
        query_string = [('uvid', voyageuvid),
                        ('routeStatus', '7')]
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
        pass

if __name__ == '__main__':
    import unittest
    unittest.main()
