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
