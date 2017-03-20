# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.delivery_ack import DeliveryAck
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestAcknowledgementController(BaseTestCase):
    """ AcknowledgementController integration test stubs """

    def test_acknowledgement(self):
        """
        Test case for acknowledgement

        
        """
        deliveryAck = DeliveryAck()
        response = self.client.open('/acknowledgement',
                                    method='POST',
                                    data=json.dumps(deliveryAck),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
