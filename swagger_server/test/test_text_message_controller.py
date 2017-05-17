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
<textMessage
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xmlns="http://stmvalidation.eu/schemas/textMessageSchema_1_3.xsd">
  <textMessageId>urn:mrn:stm:txt:sma:20170510104400-1</textMessageId>
  <informationObjectReferenceId>urn:mrn:stm:voyage:id:test:100</informationObjectReferenceId>
  <informationObjectReferenceType>RTZ</informationObjectReferenceType>
  <validityPeriodStart>2017-05-01T01:00:00Z</validityPeriodStart>
  <validityPeriodStop>2017-06-10T01:00:00Z</validityPeriodStop>
  <author>urn:mrn:stm:user:sma:mikolo</author>
  <from>urn:mrn:stm:org:sma</from>
  <serviceType>SHIP-VIS</serviceType>
  <createdAt>2017-05-10T01:00:00Z</createdAt>
  <subject>Test message</subject>
  <body>Test message Hanöbukten</body>
  <position lat="55.50668" lon="14.29825"/>
  <area>
    <Polygon>
      <posList>55.452 14.405 55.465 14.151 56.006 14.301 55.563 14.437 55.452 14.405</posList>
    </Polygon>
    <Circle>
      <position lat="55.50668" lon="14.29825"/>
      <radius>1</radius>
    </Circle>
  </area>
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
        p = Path('import')
        files = list(p.glob('**/urn:mrn:stm:txt:sma:20170510104400-1*'))
        for item in files:
            print(item)
            os.remove(str(item))
        files = list(p.glob('**/parse.txt'))
        for item in files:
            print(item)
            os.remove(str(item))
        pass


if __name__ == '__main__':
    import unittest
    unittest.main()
