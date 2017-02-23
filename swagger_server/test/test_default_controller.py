# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.delivery_ack import DeliveryAck
from swagger_server.models.error_model import ErrorModel
from swagger_server.models.get_vp_response_object import GetVPResponseObject
from swagger_server.models.response_obj import ResponseObj
from swagger_server.models.s124_data_set import S124DataSet
from swagger_server.models.text_message_object import TextMessageObject
from swagger_server.models.voyage_plan import VoyagePlan
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestDefaultController(BaseTestCase):
    """ DefaultController integration test stubs """

    def test_acknowledgement(self):
        """
        Test case for acknowledgement

        
        """
        deliveryAck = DeliveryAck()
        response = self.client.open('/V1/acknowledgement',
                                    method='POST',
                                    data=json.dumps(deliveryAck),
                                    content_type='application/json;charset=UTF-8')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_get_voyage_plans(self):
        """
        Test case for get_voyage_plans

        
        """
        query_string = [('uvid', 'uvid_example'),
                        ('routeStatus', 'routeStatus_example')]
        response = self.client.open('/V1/voyagePlans',
                                    method='GET',
                                    content_type='application/json;charset=UTF-8',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_remove_voyage_plan_subscription(self):
        """
        Test case for remove_voyage_plan_subscription

        
        """
        query_string = [('callbackEndpoint', 'callbackEndpoint_example'),
                        ('uvid', 'uvid_example')]
        response = self.client.open('/V1/voyagePlans/subscription',
                                    method='DELETE',
                                    content_type='application/json;charset=UTF-8',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_subscribe_to_voyage_plan(self):
        """
        Test case for subscribe_to_voyage_plan

        
        """
        query_string = [('callbackEndpoint', 'callbackEndpoint_example'),
                        ('uvid', 'uvid_example')]
        response = self.client.open('/V1/voyagePlans/subscription',
                                    method='POST',
                                    content_type='application/json;charset=UTF-8',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_upload_area(self):
        """
        Test case for upload_area

        
        """
        area = S124DataSet()
        query_string = [('deliveryAckEndPoint', 'deliveryAckEndPoint_example')]
        response = self.client.open('/V1/area',
                                    method='POST',
                                    data=json.dumps(area),
                                    content_type='application/json;charset=UTF-8',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_upload_text_message(self):
        """
        Test case for upload_text_message

        
        """
        textMessageObject = TextMessageObject()
        query_string = [('deliveryAckEndPoint', 'deliveryAckEndPoint_example')]
        response = self.client.open('/V1/textMessage',
                                    method='POST',
                                    data=json.dumps(textMessageObject),
                                    content_type='application/json;charset=UTF-8',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_upload_voyage_plan(self):
        """
        Test case for upload_voyage_plan

        
        """
        voyagePlan = VoyagePlan()
        query_string = [('uvid', 'uvid_example'),
                        ('deliveryAckEndPoint', 'deliveryAckEndPoint_example')]
        response = self.client.open('/V1/voyagePlans',
                                    method='POST',
                                    data=json.dumps(voyagePlan),
                                    content_type='application/json;charset=UTF-8',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
