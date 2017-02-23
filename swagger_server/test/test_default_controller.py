# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.delivery_ack import DeliveryAck
from swagger_server.models.error_model import ErrorModel
from swagger_server.models.get_vp_response_object import GetVPResponseObject
from swagger_server.models.response_obj import ResponseObj
from swagger_server.models.s124_data_set import S124DataSet
from swagger_server.models.text_message import TextMessage
from swagger_server.models.voyage_plan import VoyagePlan
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestDefaultController(BaseTestCase):
    """ DefaultController integration test stubs """

    def test_acknowledment(self):
        """
        Test case for acknowledment

        
        """
        deliveryAck = DeliveryAck()
        response = self.client.open('/8320767/acknowledgement',
                                    method='POST',
                                    data=json.dumps(deliveryAck),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_get_voyage_plan(self):
        """
        Test case for get_voyage_plan

        
        """
        query_string = [('uvid', 'uvid_example'),
                        ('routeStatus', 'routeStatus_example')]
        response = self.client.open('/8320767/voyagePlan',
                                    method='GET',
                                    content_type='application/json',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_remove_voyage_plan_subscription(self):
        """
        Test case for remove_voyage_plan_subscription

        
        """
        query_string = [('callBackendpoint', 'callBackendpoint_example'),
                        ('uvid', 'uvid_example')]
        response = self.client.open('/8320767/voyagePlan/subscribe',
                                    method='DELETE',
                                    content_type='application/json',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_subscribe_to_voyage_plan(self):
        """
        Test case for subscribe_to_voyage_plan

        
        """
        query_string = [('callBackendpoint', 'callBackendpoint_example'),
                        ('uvid', 'uvid_example')]
        response = self.client.open('/8320767/voyagePlan/subscribe',
                                    method='POST',
                                    content_type='application/json',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_upload_area(self):
        """
        Test case for upload_area

        
        """
        area = S124DataSet()
        query_string = [('deliveryAckEndpoint', 'deliveryAckEndpoint_example')]
        response = self.client.open('/8320767/area',
                                    method='POST',
                                    data=json.dumps(area),
                                    content_type='application/json',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_upload_text_message(self):
        """
        Test case for upload_text_message

        
        """
        textMessage = TextMessage()
        query_string = [('deliveryAckEndpoint', 'deliveryAckEndpoint_example')]
        response = self.client.open('/8320767/textMessage',
                                    method='POST',
                                    data=json.dumps(textMessage),
                                    content_type='application/json',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_upload_voyage_plan(self):
        """
        Test case for upload_voyage_plan

        
        """
        voyagePlan = VoyagePlan()
        query_string = [('uvid', 'uvid_example'),
                        ('deliveryAckEndpoint', 'deliveryAckEndpoint_example')]
        response = self.client.open('/8320767/voyagePlan',
                                    method='POST',
                                    data=json.dumps(voyagePlan),
                                    content_type='application/json',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
