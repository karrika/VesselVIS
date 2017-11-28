import json
from swagger_server import service
import collections
from operator import methodcaller
import os
from datetime import datetime
import time
import uuid

textmessage='''<?xml version="1.0" encoding="utf-8"?>
<textMessage
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xmlns="http://stmvalidation.eu/schemas/textMessageSchema_1_3.xsd">
  <textMessageId>urn:mrn:stm:txt:furuno:''' + str(uuid.uuid4()) + '''</textMessageId>
  <author>Test robot</author>
  <from>urn:mrn:stm:org:sma</from>
  <serviceType>SHIP-VIS</serviceType>
  <createdAt>''' + datetime.utcnow().replace(microsecond=0).isoformat() + 'Z' + '''</createdAt>
  <subject>Automatic test message</subject>
  <body>This message is sent in order to test if text messages can be sent to this VIS instance</body>
</textMessage>
'''

''' Read current valid services '''
dataold = []
fname = 'import/text.dat'
if os.path.isfile(fname):
    with open(fname) as f:
        dataold = json.loads(f.read())

''' Read all services '''
fname = 'import/textnew.dat'
with open(fname) as f:
    data = json.loads(f.read())
os.remove(fname)
''' Set all services to valid for the check '''
fname = 'import/text.dat'
with open(fname,'w') as f:
    f.write(json.dumps(data))
''' Set the set to include only new or unvalid services '''
for item in dataold:
    if item in data:
        data.remove(item)
''' Check the set of new or unvalid services '''
for srv in data:
    ret = service.post_text(srv['endpointUri'], textmessage)
    if ret.status_code == 405 or ret.status_code == 500 or ret.status_code == 501:
        print(srv['name'])
    else:
        print(srv['name'], 'OK')
        dataold.append(srv)
mapping_set = []
for item in sorted(dataold, key=methodcaller('get', 'name', None)):
    mapping_data=collections.OrderedDict()
    mapping_data['name'] = item['name']
    mapping_data['endpointUri'] = item['endpointUri']
    mapping_data['instanceId'] = item['instanceId']
    mapping_set.append(mapping_data)
''' Save the modified set of valid services '''
with open(fname,'w') as f:
    f.write(json.dumps(mapping_set))
