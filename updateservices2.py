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
    if srv['name'] == 'DMI Route METOC service':
        dataold.append(srv)
    else:
        ret = service.get_voyageplan(srv['endpointUri'])
        if (ret.status_code == 500) and (ret.text == 'SSLError'):
            print(srv['name'])
        else:
            dataold.append(srv)
''' Sort the list alphabetically '''
mapping_set = []
for item in sorted(dataold, key=methodcaller('get', 'name', None)):
    if 'status' in item:
        if item['status'] != 'released':
            print(item['name'])
        else:
            mapping_data=collections.OrderedDict()
            mapping_data['name'] = item['name']
            mapping_data['endpointUri'] = item['endpointUri'].rstrip('/')
            mapping_data['instanceId'] = item['instanceId']
            mapping_set.append(mapping_data)
    else:
        print(item)
''' Save the modified set of valid services '''
with open(fname,'w') as f:
    f.write(json.dumps(mapping_set))
