# coding: utf-8

from __future__ import absolute_import

from . import BaseTestCase
from six import BytesIO
from flask import json
from pathlib import Path
import os


class TestAreaController(BaseTestCase):
    """ AreaController integration test stubs """

    def test_upload_area(self):
        """
        Test case for upload_area

        
        """
        area = 'Hello World!'
        query_string = [('deliveryAckEndPoint', 'https://localhost:8002')]
        response = self.client.open('/area',
                                    method='POST',
                                    data=json.dumps(area),
                                    content_type='application/json',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_upload_area_cleanup(self):
        """
        Test case for upload_area cleanup

        
        """
        vis2_uvid='urn:mrn:stm:service:instance:furuno:vis2'
        p = Path('import')
        files = list(p.glob('**/' + vis2_uvid + '*'))
        for item in files:
            print(item)
            os.remove(str(item))
        pass

if __name__ == '__main__':
    import unittest
    unittest.main()
