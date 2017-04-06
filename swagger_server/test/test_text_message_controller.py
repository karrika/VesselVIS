# coding: utf-8

from __future__ import absolute_import

from . import BaseTestCase
from six import BytesIO
from flask import json
from pathlib import Path
import os


class TestTextMessageController(BaseTestCase):
    """ TextMessageController integration test stubs """

    def test_upload_text_message(self):
        """
        Test case for upload_text_message

        
        """
        textMessageObject = 'Hello World!'
        query_string = [('deliveryAckEndPoint', 'https://localhost:8002')]
        response = self.client.open('/textMessage',
                                    method='POST',
                                    data=json.dumps(textMessageObject),
                                    content_type='application/json',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_upload_text_message_cleanup(self):
        """
        Test case for upload_text_message cleanup

        
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
