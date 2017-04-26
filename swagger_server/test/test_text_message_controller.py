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
        textMessageObject = '''<?xml version="1.0" encoding="utf-8"?>
<textMessage xmlns="http://tempuri.org/textMessageSchema.xsd">
  <textMessageId>urn:mrn:stm:txt:sma:20161222104700-1</textMessageId>
  <informationObjectReferenceId>urn:mrn:stm:voyage:id:sma:test-1</informationObjectReferenceId>
  <author>Mikael</author>
  <from>urn:mrn:stm:org:sma</from>
  <createdAt>2016-12-22T11:09:47</createdAt>
  <subject>Subject</subject>
  <body>Body</body>
</textMessage>
'''

        query_string = [('deliveryAckEndPoint', 'https://localhost:8002')]
        response = self.client.open('/textMessage',
                                    method='POST',
                                    data=textMessageObject,
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
