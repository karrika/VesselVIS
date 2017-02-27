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
        deliveryAck.id = 'urn:mrn:'
        deliveryAck.reference_id = 'urn:mrn:'
        deliveryAck.time_of_delivery = '2017-01-27T12:00:00Z'
        deliveryAck.from_id = 'urn:mrn:'
        deliveryAck.from_name = 'Who cares'
        deliveryAck.to_id = 'urn:mrn:'
        deliveryAck.to_name = 'Who cares'
        deliveryAck.ack_result = 'Who cares'
        response = self.client.open('/8320767/acknowledgement',
                                    method='POST',
                                    data=json.dumps(deliveryAck),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_get_voyage_plans_current(self):
        """
        Test case for get_voyage_plans
        In this case we have no uvid or routeStatus.
        We want to retrieve the latest, current plan.
        
        """
        query_string = []
        response = self.client.open('/8320767/voyagePlans',
                                    method='GET',
                                    content_type='application/json',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_get_voyage_plans_found(self):
        """
        Test case for get_voyage_plans

        
        """
        query_string = [('uvid', 'urn:mrn:stm:voyage:id:8320767'),
                        ('routeStatus', '1')]
        response = self.client.open('/8320767/voyagePlans',
                                    method='GET',
                                    content_type='application/json',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_get_voyage_plans_not_found(self):
        """
        Test case for get_voyage_plans

        
        """
        query_string = [('uvid', 'urn:mrn:stm:voyage:id:not:existing'),
                        ('routeStatus', '1')]
        response = self.client.open('/8320767/voyagePlans',
                                    method='GET',
                                    content_type='application/json',
                                    query_string=query_string)
        self.assert404(response, "Response body is : " + response.data.decode('utf-8'))

    def test_remove_voyage_plan_subscription(self):
        """
        Test case for remove_voyage_plan_subscription

        
        """
        query_string = [('callbackEndpoint', 'http://localhost:8002'),
                        ('uvid', 'urn:mrn:stm:voyage:id:8320767')]
        response = self.client.open('/8320767/voyagePlans/subscription',
                                    method='DELETE',
                                    content_type='application/json',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_subscribe_to_generic_voyage_plan(self):
        """
        Test case for subscribe_to_voyage_plan
        Here we have no uvid. This is a generic request.
        
        """
        query_string = [('callbackEndpoint', 'http://localhost:8002')]
        response = self.client.open('/8320767/voyagePlans/subscription',
                                    method='POST',
                                    content_type='application/json',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_subscribe_to_voyage_plan_found(self):
        """
        Test case for subscribe_to_voyage_plan
        A voyage with this uid exists.
        
        """
        query_string = [('callbackEndpoint', 'http://localhost:8002'),
                        ('uvid', 'urn:mrn:stm:voyage:id:8320767')]
        response = self.client.open('/8320767/voyagePlans/subscription',
                                    method='POST',
                                    content_type='application/json',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_subscribe_to_voyage_plan_not_found(self):
        """
        Test case for subscribe_to_voyage_plan
        A voyage with this uvid does not exist.
        
        """
        query_string = [('callbackEndpoint', 'http://localhost:8002'),
                        ('uvid', 'urn:mrn:stm:voyage:id:not:existing')]
        response = self.client.open('/8320767/voyagePlans/subscription',
                                    method='POST',
                                    content_type='application/json',
                                    query_string=query_string)
        self.assert404(response, "Response body is : " + response.data.decode('utf-8'))

    def test_upload_area(self):
        """
        Test case for upload_area

        
        """
        area = S124DataSet()
        area.data_set = 'who cares'
        query_string = [('deliveryAckEndPoint', 'http://localhost:8002')]
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
        textMessageObject = TextMessageObject()
        textMessageObject.text_message = 'Hi there'
        query_string = [('deliveryAckEndPoint', 'http://localhost:8002')]
        response = self.client.open('/8320767/textMessage',
                                    method='POST',
                                    data=json.dumps(textMessageObject),
                                    content_type='application/json',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_upload_voyage_plan(self):
        """
        Test case for upload_voyage_plan

        
        """
        voyagePlan = VoyagePlan()
        voyagePlan.route = '<route />'
        query_string = [('uvid', 'urn:mrn:stm:voyage:id:vis1:0001'),
                        ('deliveryAckEndPoint', 'http://localhost:8002')]
        response = self.client.open('/8320767/voyagePlans',
                                    method='POST',
                                    data=json.dumps(voyagePlan),
                                    content_type='application/json',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
