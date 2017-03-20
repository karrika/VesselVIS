# coding: utf-8

from __future__ import absolute_import

from . import BaseTestCase
from six import BytesIO
from flask import json


class TestAreaController(BaseTestCase):
    """ AreaController integration test stubs """

    def test_upload_area(self):
        """
        Test case for upload_area

        
        """
        area = 'area_example'
        query_string = [('deliveryAckEndPoint', 'deliveryAckEndPoint_example')]
        response = self.client.open('/area',
                                    method='POST',
                                    data=json.dumps(area),
                                    content_type='text/xml',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
