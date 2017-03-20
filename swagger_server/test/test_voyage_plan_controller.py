# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.get_subscription_response import GetSubscriptionResponse
from swagger_server.models.get_voyage_plan_response import GetVoyagePlanResponse
from . import BaseTestCase
from six import BytesIO
from flask import json

voyageuvid='urn:mrn:stm:voyage:id:8320767:2017021010'
vis_uvid='urn:mrn:stm:service:instance:furuno:'

f = open('export/' + voyageuvid + '.acl', 'w')
data=[ vis_uvid ]
f.write(json.dumps(data))
f.close()

f = open('export/all.acl', 'w')
data=[ vis_uvid ]
f.write(json.dumps(data))
f.close()


class TestVoyagePlanController(BaseTestCase):
    """ VoyagePlanController integration test stubs """

    def test_get_subscription_to_voyage_plans(self):
        """
        Test case for get_subscription_to_voyage_plans

        
        """
        query_string = [('callbackEndpoint', 'callbackEndpoint_example')]
        response = self.client.open('/voyagePlans/subscription',
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_get_voyage_plans(self):
        """
        Test case for get_voyage_plans

        
        """
        query_string = [('uvid', 'uvid_example'),
                        ('routeStatus', 'routeStatus_example')]
        response = self.client.open('/voyagePlans',
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_remove_voyage_plan_subscription(self):
        """
        Test case for remove_voyage_plan_subscription

        
        """
        query_string = [('callbackEndpoint', 'callbackEndpoint_example'),
                        ('uvid', 'uvid_example')]
        response = self.client.open('/voyagePlans/subscription',
                                    method='DELETE',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_subscribe_to_voyage_plan(self):
        """
        Test case for subscribe_to_voyage_plan

        
        """
        query_string = [('callbackEndpoint', 'callbackEndpoint_example'),
                        ('uvid', 'uvid_example')]
        response = self.client.open('/voyagePlans/subscription',
                                    method='POST',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_upload_voyage_plan(self):
        """
        Test case for upload_voyage_plan

        
        """
        voyagePlan = 'voyagePlan_example'
        query_string = [('deliveryAckEndPoint', 'deliveryAckEndPoint_example'),
                        ('callbackEndpoint', 'callbackEndpoint_example')]
        response = self.client.open('/voyagePlans',
                                    method='POST',
                                    data=json.dumps(voyagePlan),
                                    content_type='text/xml',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
