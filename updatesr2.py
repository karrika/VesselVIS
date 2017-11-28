import json
from swagger_server import service
import collections
from operator import methodcaller
import os
from datetime import datetime
import time
import uuid

'''
Here we try to check the validity of the services
'''

''' Read current valid services '''
dataold = []
fname = 'import/vts.dat'
if os.path.isfile(fname):
    with open(fname) as f:
        dataold = json.loads(f.read())

''' Read all services '''
fname = 'import/vtsnew.dat'
with open(fname) as f:
    data = json.loads(f.read())
os.remove(fname)
''' Set all services to valid for the check '''
fname = 'import/vts.dat'
with open(fname,'w') as f:
    f.write(json.dumps(data))
''' Set the set to include only new or unvalid services '''
for item in dataold:
    if item in data:
        data.remove(item)
''' Check the set of new or unvalid services '''
for srv in data:
    ret = service.get_voyageplan(srv['endpointUri'])
    if (ret.status_code == 500) and (ret.text == 'SSLError'):
        print(srv['name'])
    else:
        dataold.append(srv)
''' Save the modified set of valid services '''
with open(fname,'w') as f:
    f.write(json.dumps(dataold))

''' Read current valid services '''
dataold = []
fname = 'import/services.dat'
if os.path.isfile(fname):
    with open(fname) as f:
        dataold = json.loads(f.read())

''' Read all services '''
fname = 'import/servicesnew.dat'
with open(fname) as f:
    data = json.loads(f.read())
os.remove(fname)
''' Set all services to valid for the check '''
fname = 'import/services.dat'
with open(fname,'w') as f:
    f.write(json.dumps(data))
''' Set the set to include only new or unvalid services '''
for item in dataold:
    if item in data:
        data.remove(item)
''' Check the set of new or unvalid services '''
for srv in data:
    ret = service.get_voyageplan(srv['endpointUri'])
    if (ret.status_code == 500) and (ret.text == 'SSLError'):
        print(srv['name'])
    else:
        dataold.append(srv)
''' Save the modified set of valid services '''
with open(fname,'w') as f:
    f.write(json.dumps(dataold))

''' Read current valid services '''
dataold = []
fname = 'import/vessels.dat'
if os.path.isfile(fname):
    with open(fname) as f:
        dataold = json.loads(f.read())

''' Read all services '''
fname = 'import/vesselsnew.dat'
with open(fname) as f:
    data = json.loads(f.read())
os.remove(fname)
''' Set all services to valid for the check '''
fname = 'import/vessels.dat'
with open(fname,'w') as f:
    f.write(json.dumps(data))
''' Set the set to include only new or unvalid services '''
for item in dataold:
    if item in data:
        data.remove(item)
''' Check the set of new or unvalid services '''
for srv in data:
    ret = service.get_voyageplan(srv['endpointUri'])
    if (ret.status_code == 500) and (ret.text == 'SSLError'):
        print(srv['name'])
    else:
        dataold.append(srv)
''' Save the modified set of valid services '''
with open(fname,'w') as f:
    f.write(json.dumps(dataold))

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
        dataold.append(srv)
''' Save the modified set of valid services '''
with open(fname,'w') as f:
    f.write(json.dumps(dataold))

''' Read current valid services '''
dataold = []
fname = 'import/ports.dat'
if os.path.isfile(fname):
    with open(fname) as f:
        dataold = json.loads(f.read())

''' Read all services '''
fname = 'import/portsnew.dat'
with open(fname) as f:
    data = json.loads(f.read())
os.remove(fname)
''' Set all services to valid for the check '''
fname = 'import/ports.dat'
with open(fname,'w') as f:
    f.write(json.dumps(data))
''' Set the set to include only new or unvalid services '''
for item in dataold:
    if item in data:
        data.remove(item)
''' Check the set of new or unvalid services '''
for srv in data:
    ret = service.createpcmqueue(srv['instanceId'])
    if ret.status_code == 200:
        dataold.append(srv)
    else:
        print(srv['unlocode'], ret.status_code, ret.text)
''' Save the modified set of valid services '''
with open(fname,'w') as f:
    f.write(json.dumps(dataold))


