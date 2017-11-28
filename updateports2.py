import json
from swagger_server import service
import collections
from operator import methodcaller
import os
from datetime import datetime
import time
import uuid

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


