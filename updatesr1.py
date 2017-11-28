import json
from swagger_server import service
import collections
from operator import methodcaller
import os
from datetime import datetime
import time
import uuid

all_data = []

parameters={
    'query' : 'designID="urn:mrn:stm:service:design:sma:vis-rest-2.2" +VTS -SHIP',
    'size' : 1000,
    'sort' : 'name,desc',
    'sort' : 'id'
}
ret=service.search(None, params=parameters)
data=json.loads(ret.text)
shore_set = []
for item in sorted(data, key=methodcaller('get', 'name', None)):
    if item['status'] == 'noprovisional':
        print('Provisional: ', item['name'])
    else:
        shore_data=collections.OrderedDict()
        shore_data['name'] = item['name']
        shore_data['endpointUri'] = item['endpointUri'].rstrip('/')
        shore_data['instanceId'] = item['instanceId']
        shore_set.append(shore_data)
        all_data.append(item)
        print('VTS', item['name'])
with open('import/vtsnew.dat','w') as f:
    f.write(json.dumps(shore_set))

ret=service.search('designID="urn:mrn:stm:service:design:sma:vis-rest-2.2" -VTS -SHIP')
data=json.loads(ret.text)
shore_set = []
for item in sorted(data, key=methodcaller('get', 'name', None)):
    if item['status'] == 'noprovisional':
        print('Provisional: ', item['name'])
    else:
        shore_data=collections.OrderedDict()
        shore_data['name'] = item['name']
        shore_data['endpointUri'] = item['endpointUri'].rstrip('/')
        shore_data['instanceId'] = item['instanceId']
        shore_set.append(shore_data)
        if not ('instanceId' in all_data):
            all_data.append(item)
        print('Services', item['name'], 'keywords:', item['keywords'])
with open('import/servicesnew.dat','w') as f:
    f.write(json.dumps(shore_set))

ret=service.search('designID="urn:mrn:stm:service:design:sma:vis-rest-2.2" +SHIP')
data=json.loads(ret.text)
vessels_set = []
for item in sorted(data, key=methodcaller('get', 'name', None)):
    if item['status'] == 'noprovisional':
        print('Provisional: ', item['name'])
    else:
        vessels_data=collections.OrderedDict()
        vessels_data['name'] = item['name']
        vessels_data['imo'] = item['imo']
        vessels_data['mmsi'] = item['mmsi']
        vessels_data['endpointUri'] = item['endpointUri'].rstrip('/')
        vessels_data['instanceId'] = item['instanceId']
        vessels_set.append(vessels_data)
        if not ('instanceId' in all_data):
            all_data.append(item)
        print('Ship', item['imo' ], item['mmsi'], item['name'], 'keywords:', item['keywords'])
with open('import/vesselsnew.dat','w') as f:
    f.write(json.dumps(vessels_set))

ret=service.search('designID="urn:mrn:stm:service:design:viktoria:amss"')
data=json.loads(ret.text)
ports_set = []
for item in sorted(data, key=methodcaller('get', 'unlocode', None)):
    if item['status'] == 'noprovisional':
        print('Provisional: ', item['name'])
    else:
        ports_data=collections.OrderedDict()
        ports_data['unlocode'] = item['unlocode']
        ports_data['endpointUri'] = item['endpointUri'].rstrip('/')
        ports_data['instanceId'] = item['instanceId']
        ports_set.append(ports_data)
        item['name'] = item['unlocode']
        all_data.append(item)
        print('Port', item['unlocode'], item['instanceId'], 'keywords:', item['keywords'])
with open('import/portsnew.dat','w') as f:
    f.write(json.dumps(ports_set))

mapping_set = []
for item in sorted(all_data, key=methodcaller('get', 'name', None)):
    if item['status'] == 'noprovisional':
        print('Provisional: ', item['name'])
    else:
        mapping_data=collections.OrderedDict()
        mapping_data['name'] = item['name']
        mapping_data['endpointUri'] = item['endpointUri'].rstrip('/')
        mapping_data['instanceId'] = item['instanceId']
        mapping_set.append(mapping_data)
        print('All', item['name'], item['instanceId'])
with open('import/all.dat','w') as f:
    f.write(json.dumps(mapping_set))
with open('import/textnew.dat','w') as f:
    f.write(json.dumps(mapping_set))

