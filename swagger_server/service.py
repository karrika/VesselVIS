# coding: utf-8

"""
    STM Voyage Information Service Service logic

    This part takes care of automatic client tasks sending out data
"""

from __future__ import absolute_import
from __future__ import print_function

import os
import sys
import requests
from requests.exceptions import SSLError, ConnectionError, Timeout
import shutil
import sys
import json
from pathlib import Path
from swagger_server.models.delivery_ack import DeliveryAck
import collections
from datetime import datetime
import time
from subprocess import call
import xml.etree.ElementTree as ET
from lxml import etree
from io import BytesIO
import uuid
import csv

simulate_vessel = False
staging = False

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

portcdm_version='0.0.16'
'''
portcdm_version='0.6'
'''

conf={}
p = Path('.')
conffile = list(p.glob('**/vessel.conf'))
if len(conffile) > 0:
    with conffile[0].open() as f:
        data = json.loads(f.read())
        conf['host'] = data['host']
        conf['port'] = data['port']
        conf['stmhost'] = data['stmhost']
        conf['stmport'] = data['stmport']
        conf['id'] = data['id']
        length = len(data['id'])
        conf['imo'] = data['id'][length-7:length]
        conf['mmsi'] = data['mmsi']
        conf['name'] = data['name']
        conf['open_to_all'] = data['open_to_all']
        conf['simulate_vessel'] = data['simulate_vessel']
        simulate_vessel = data['simulate_vessel']
        if 'staging' in data:
            staging = True
vis_cert = list(p.glob('**/Certificate_*.pem'))
if len(vis_cert) == 0:
    print('Error: no Certificate_*.pem found')
else:
    vesselName = str(vis_cert[0])
    vesselName = vesselName[12:len(vesselName)-4]
vis_key = list(p.glob('**/PrivateKey_*.pem'))
if len(vis_key) == 0:
    print('Error: no PrivateKey_*.pem found')
vis_cert=(str(vis_cert[0]), str(vis_key[0]))
if staging:
    trustchain = '/usr/share/ca-certificates/MCstaging/mc-ca-chain.pem'
else:
    trustchain = '/usr/share/ca-certificates/MCproduction/mc-ca-chain.pem'

url="https://localhost:8001"
vis2_uvid='urn:mrn:stm:service:instance:furuno:vis2'
vis2_name='VIS-2'

p = Path('.')
conffile = list(p.glob('**/target.conf'))
if len(conffile) > 0:
    with conffile[0].open() as f:
        data = json.loads(f.read())
        url = data['endpointUri']
        vis2_uvid = data['instanceId']
        vis2_name = data['name']

callbackurl=conf['stmhost'] + ':' + str(conf['stmport'])

def st(status):
    return str(status.status_code) + " " + status.text

def reportrow(sheet, row, col, state = True, reason = ''):
    if state:
        report=sheet + '.write(' + row + ', ' + col + ''', "PASS", boldcenter)
''' + sheet + '.write(' + row + ', ' + col + ' - 1, "' + reason + '''", normal)
'''
    else:
        report=sheet + '.write(' + row + ', ' + col + ''', "FAIL", boldcenter)
''' + sheet + '.write(' + row + ', ' + col + ' - 1, "' + reason + '''", normal)
'''
    with open('../create_worksheet.py', 'a') as f:
        f.write(report)

'''
Skip trustchain check for Microsoft Azure servers
Due to Transas that refuse to use certificates properly
and STM that does not enforce proper security
'''
def skip_trustchain(url):
    if 'azure' in url:
        return True
    if 'transas' in url:
        return True
    return False

'''
Check that the partner to talk with is in the service registry
For staging we allow anything, for production it needs to be in all.dat
'''
def released(id):
    fname = 'import/all.dat'
    with open(fname) as f:
        data = json.loads(f.read())
    for item in data:
        if item['instanceId'] == id:
            return True
    return False

def log_stm_event(eventNumber, eventType, externalOrgId, externalEntityId, eventParameters, eventDataType, eventData):
    data = collections.OrderedDict()
    data['UID'] = str(uuid.uuid4())
    data['time'] = datetime.utcnow().replace(microsecond=0).isoformat() + 'Z'
    data['serviceInstanceId'] = conf['id']
    data['eventNumber'] = eventNumber
    data['eventType'] = eventType
    data['externalOrgId'] = externalOrgId
    data['externalEntityId'] = externalEntityId
    data['eventParameters'] = eventParameters
    data['eventDataType'] = eventDataType
    data['eventData'] = eventData
    with open(str(data['time'])[0:10] + '.log', 'a') as f:
        spamwriter = csv.writer(f, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow([ data['UID'], data['time'], data['serviceInstanceId'], data['eventNumber'], data['eventType'], data['externalOrgId'], data['externalEntityId'], data['eventParameters'], data['eventDataType'], data['eventData'] ])

def log_event(eventname, name = None, callback = None, uvid = None, routeStatus = None, ack = None, url = None, status = None, client = None, eventNumber = '', eventType = '', externalOrgId = '', eventParameters = '', eventDataType = '', eventData = '' ):
    data = collections.OrderedDict()
    data['time'] = datetime.utcnow().replace(microsecond=0).isoformat() + 'Z'
    if not (eventname is None):
        data['event'] = eventname
    if not (client is None):
        data['client'] = client
    if not (name is None):
        data['name'] = name.replace('"','').replace('{','').replace('}','')
    if not (ack is None):
        data['ack'] = ack
    if not (callback is None):
        data['callback'] = callback
    if not (uvid is None):
        data['uvid'] = uvid
    if not (url is None):
        data['url'] = url
    if not (routeStatus is None):
        data['routeStatus'] = routeStatus
    if not (status is None):
        data['status'] = status.replace('"','').replace('{','').replace('}','')
        if len(data['status']) > 80:
            tmp = data['status']
            data['status'] = tmp[0:79]
    with open('import/event.log', 'a') as f:
        json.dump(data, f, ensure_ascii=True)
        f.write('\n')
    log_stm_event(eventNumber, eventType, externalOrgId, client, eventParameters, eventDataType, eventData)

def check_event(name, callback = None, uvid = None):
    with open('import/event.log', 'r') as f:
        log = f.readlines()
        length = len(log)
        if length > 0:
            data = json.loads(log[length-1])
            if data['event'] == name:
                if not (callback is None):
                    if data['callback'] == callback:
                        if not (uvid is None):
                            if data['uvid'] == uvid:
                                return True
    return False

'''
Get uvid from monitored.rtz or alternate.rtz
'''
def getuvid(routename):
    fname = 'export/' + routename
    if os.path.isfile(fname):
        tree = etree.parse(fname)
        root = tree.getroot()
        tag='{http://www.cirm.org/RTZ/1/1}'
        routeInfo = root.find(tag + 'routeInfo')
        return(routeInfo.get('vesselVoyage'))

def get_alternate_uvid():
    return getuvid('alternate.rtz')

def get_monitored_uvid():
    return getuvid('monitored.rtz')

'''
Generic ACL methods for testing only
The acl will also follow the subscriptions
'''
def rm_acl(id = None):
    if simulate_vessel:
        fname = 'export/all.acl'
        if os.path.isfile(fname):
            if id is None:
                os.remove(fname)
            else:
                with open(fname) as f:
                    acl = json.loads(f.read())
                    if id in acl:
                        acl.remove(id)
                        with open(fname,'w') as g:
                            g.write(acl)

def add_acl(id):
    if simulate_vessel:
        fname = 'export/all.acl'
        acl = []
        if os.path.isfile(fname):
            with open(fname) as f:
                acl = json.loads(f.read())
        if not (id in acl):
            acl.append(id)
            with open(fname, 'w') as f:
                f.write(json.dumps(acl))

'''
Alternate route methods for testing only
'''
def rm_alternate():
    if simulate_vessel:
        fname = 'export/alternate.uvid'
        if os.path.isfile(fname):
            with open(fname) as f:
                data = json.loads(f.read())
                if 'route' in data:
                    route = 'export/' + data['route']
                    if os.path.isfile(route):
                        os.remove(route)
            os.remove(fname)

'''
Monitored route methods for testing only
'''
def rm_monitored():
    if simulate_vessel:
        fname = 'export/monitored.uvid'
        if os.path.isfile(fname):
            with open(fname) as f:
                data = json.loads(f.read())
                if 'route' in data:
                    route = 'export/' + data['route']
                    if os.path.isfile(route):
                        os.remove(route)
            os.remove(fname)

'''
Extract url and name based on intanceId
'''
def get_service_url(instanceId):
    instanceId = os.path.splitext(os.path.basename(instanceId))[0]
    if os.path.exists('import/ports.dat'):
        with open('import/ports.dat') as f:
            data=json.loads(f.read())
            for item in data:
                if item['instanceId'] == instanceId:
                    return ('PortCDM', item['endpointUri'], item['unlocode'])
    if os.path.exists('import/vts.dat'):
        with open('import/vts.dat') as f:
            data=json.loads(f.read())
            for item in data:
                if item['instanceId'] == instanceId:
                    return ('VIS', item['endpointUri'], item['name'])
    if os.path.exists('import/services.dat'):
        with open('import/services.dat') as f:
            data=json.loads(f.read())
            for item in data:
                if item['instanceId'] == instanceId:
                    if instanceId == 'urn:mrn:mcl:service:instance:dmi:METOC_SejlRute-service':
                        return ('MCL', item['endpointUri'], item['name'])
                    else:
                        return ('VIS', item['endpointUri'], item['name'])
    if os.path.exists('import/vessels.dat'):
        with open('import/vessels.dat') as f:
            data=json.loads(f.read())
            for item in data:
                if item['instanceId'] == instanceId:
                    return ('VIS', item['endpointUri'], item['name'])
    return ('None', 'None', 'None')

'''
GET voyagePlans method
'''
def get_voyageplan(url, uvid = None, routeStatus = None, name = None, client = conf['id']):
    parameters = {
    }
    sub='/voyagePlans'
    evtype = 1
    evpar = ''
    if not (uvid is None):
        parameters['uvid'] = uvid
        evpar = 'uvid:' + str(uvid)
    if not (routeStatus is None):
        parameters['routeStatus'] = routeStatus
        evpar = evpar + ' routeStatus:' + str(routeStatus)
    try:
        if skip_trustchain(url):
            status = requests.get(url + sub, params = parameters, cert=vis_cert, timeout = 15)
        else:
            status = requests.get(url + sub, params = parameters, cert=vis_cert, verify=trustchain, timeout = 15)
    except Timeout as e:
        print(e)
        status = requests.Response
        status.text = "Timeout"
        status.status_code = 500
        evtype = 4
    except SSLError as e:
        print(e)
        status = requests.Response
        status.text = "SSLError"
        status.status_code = 500
        evtype = 6
    except ConnectionError as e:
        print(e)
        status = requests.Response
        status.text = "ConnectionError"
        status.status_code = 500
        evtype = 4
    log_event('voyageplan', url=url, name=name, uvid=uvid, routeStatus=routeStatus, status=st(status), client = client, eventNumber = 2, eventType = evtype, eventDataType = 1, eventParameters = evpar)
    return status

'''
POST voyagePlans/subscription method
'''
def post_subscription(url, callback, uvid = None, name = None, client = conf['id']):
    sub='/voyagePlans/subscription'
    evtype = 1
    evpar = 'callbackEndpoint:' + str(callback)
    if uvid is None:
        parameters={
            'callbackEndpoint': callback
        }
        try:
            if skip_trustchain(url):
                status = requests.post(url + sub, params=parameters, cert=vis_cert)
            else:
                status = requests.post(url + sub, params=parameters, cert=vis_cert, verify=trustchain)
        except Timeout as e:
            print(e)
            status = requests.Response
            status.text = "Timeout"
            status.status_code = 500
            evtype = 4
        except SSLError as e:
            print(e)
            status = requests.Response
            status.text = "SSLError"
            status.status_code = 500
            evtype = 6
        except ConnectionError as e:
            print(e)
            status = requests.Response
            status.text = "ConnectionError"
            status.status_code = 500
            evtype = 4
        log_event('subscribe', url=url, name=name, status=st(status), client = client, eventNumber = 10, eventType = evtype, eventDataType = 1, eventParameters = evpar)
        return status
    evpar = evpar + 'uvid:' + str(uvid)
    parameters={
        'callbackEndpoint': callback,
        'uvid': uvid
    }
    try:
        if skip_trustchain(url):
            status = requests.post(url + sub, params=parameters, cert=vis_cert)
        else:
            status = requests.post(url + sub, params=parameters, cert=vis_cert, verify=trustchain)
    except Timeout as e:
        print(e)
        status = requests.Response
        status.text = "Timeout"
        status.status_code = 500
        evtype = 4
    except SSLError as e:
        print(e)
        status = requests.Response
        status.text = "SSLError"
        status.status_code = 500
        evtype = 6
    except ConnectionError as e:
        print(e)
        status = requests.Response
        status.text = "ConnectionError"
        status.status_code = 500
        evtype = 4
    log_event('subscribe', url=url, name=name, uvid=uvid, status=st(status), client = client, eventNumber = 10, eventType = evtype, eventDataType = 1, eventParameters = evpar)
    return status

def subscribe_voyageplan(instanceId):
    servicetype, url, name = get_service_url(instanceId)
    if servicetype == 'VIS':
        return post_subscription(url, callbackurl, name=name)

'''
GET voyagePlans/subscription method
'''
def get_subscriptions(url, callback, name=None, client = conf['id']):
    sub='/voyagePlans/subscription'
    evtype = 1
    evpar = 'callbackEndpoint:' + str(callback)
    parameters={
        'callbackEndpoint': callback
    }
    try:
        if skip_trustchain(url):
            status = requests.get(url + sub, params=parameters, cert=vis_cert)
        else:
            status = requests.get(url + sub, params=parameters, cert=vis_cert, verify=trustchain)
    except Timeout as e:
        print(e)
        status = requests.Response
        status.text = "Timeout"
        status.status_code = 500
        evtype = 4
    except SSLError as e:
        print(e)
        status = requests.Response
        status.text = "SSLError"
        status.status_code = 500
        evtype = 6
    except ConnectionError as e:
        print(e)
        status = requests.Response
        status.text = "ConnectionError"
        status.status_code = 500
        evtype = 4
    log_event('subscriptions', url=url, name=name, status=st(status), client = client, eventNumber = 30, eventType = evtype, eventDataType = 1, eventParameters = evpar)
    return status

'''
DELETE voyagePlans/subscription method
'''
def delete_subscription(url, callback, uvid = None, name = None, client = conf['id']):
    sub='/voyagePlans/subscription'
    evtype = 1
    evpar = 'callbackEndpoint:' + callback
    if uvid is None:
        parameters={
            'callbackEndpoint': callback
        }
        try:
            if skip_trustchain(url):
                status = requests.delete(url + sub, params=parameters, cert=vis_cert)
            else:
                status = requests.delete(url + sub, params=parameters, cert=vis_cert, verify=trustchain)
        except Timeout as e:
            print(e)
            status = requests.Response
            status.text = "Timeout"
            status.status_code = 500
            evtype = 4
        except SSLError as e:
            print(e)
            status = requests.Response
            status.text = "SSLError"
            status.status_code = 500
            evtype = 6
        except ConnectionError as e:
            print(e)
            status = requests.Response
            status.text = "ConnectionError"
            status.status_code = 500
            evtype = 4
        log_event('unsubscribe', url=url, name=name, status=st(status), client = client, eventNumber = 12, eventType = evtype, eventDataType = 1, eventParameters = evpar)
        return status
    parameters={
        'callbackEndpoint': callback,
        'uvid': uvid
    }
    evpar = evpar + 'uvid:' + str(uvid)
    try:
        if skip_trustchain(url):
            status = requests.delete(url + sub, params=parameters, cert=vis_cert)
        else:
            status = requests.delete(url + sub, params=parameters, cert=vis_cert, verify=trustchain)
    except Timeout as e:
        print(e)
        status = requests.Response
        status.text = "Timeout"
        status.status_code = 500
        evtype = 4
    except SSLError as e:
        print(e)
        status = requests.Response
        status.text = "SSLError"
        status.status_code = 500
        evtype = 6
    except ConnectionError as e:
        print(e)
        status = requests.Response
        status.text = "ConnectionError"
        status.status_code = 500
        evtype = 4
    log_event('unsubscribe', url=url, name=name, status=st(status), uvid=uvid, client = client, eventNumber = 12, eventType = evtype, eventDataType = 1, eventParameters = evpar)
    return status

def unsubscribe_voyageplan(instanceId):
    servicetype, url, name = get_service_url(instanceId)
    if servicetype == 'VIS':
        return delete_subscription(url, callbackurl, name=name)

def upload_subscriptions_to_all():
    prev = []
    fname = 'import/request.subs'
    if os.path.isfile(fname):
        with open(fname) as f:
            prev = json.loads(f.read())
    current = []
    fname = 'export/request.subs'
    if os.path.isfile(fname):
        with open(fname) as f:
            current = json.loads(f.read())
    for preitem in prev:
        if not (preitem in current):
            unsubscribe_voyageplan(preitem)
            shutil.copyfile('export/request.subs', 'import/request.subs')
    for curitem in current:
        if not (curitem in prev):
            subscribe_voyageplan(curitem)
            shutil.copyfile('export/request.subs', 'import/request.subs')

'''
POST voyagePlans method
'''
def post_voyageplan(url, voyageplan, deliveryAckEndPoint = None, callbackEndpoint = callbackurl, uvid = None, name = '', routeName = '', client = conf['id']):
    headers = {
        'Content-Type': 'text/xml'
    }
    parameters = {
    }
    evtype = 1
    evpar = ''
    if not (deliveryAckEndPoint is None):
        parameters['deliveryAckEndPoint'] = deliveryAckEndPoint
        evpar = 'deliveryAckEndPoint:' + str(deliveryAckEndPoint)
    if not (callbackEndpoint is None):
        parameters['callbackEndpoint'] = callbackEndpoint
        evpar = evpar + ' callbackEndpoint:' + str(callbackEndpoint)
    sub='/voyagePlans'
    try:
        if skip_trustchain(url):
            status = requests.post(url + sub, data=voyageplan.encode('utf-8'), params = parameters, headers = headers, cert=vis_cert, timeout = 30)
        else:
            status = requests.post(url + sub, data=voyageplan.encode('utf-8'), params = parameters, headers = headers, cert=vis_cert, verify=trustchain, timeout = 30)
    except Timeout as e:
        print(e)
        status = requests.Response
        status.text = "Timeout"
        status.status_code = 500
        evtype = 4
    except SSLError as e:
        print(e)
        status = requests.Response
        status.text = "SSLError"
        status.status_code = 500
        evtype = 6
    except ConnectionError as e:
        print(e)
        status = requests.Response
        status.text = "ConnectionError"
        status.status_code = 500
        evtype = 4
    log_event('sent ' + routeName, url=url, name=name, ack=deliveryAckEndPoint, status=st(status), client = client, eventNumber = 4, eventType = evtype, eventDataType = 1, eventParameters = evpar)
    return status

def upload_monitored(subscriber):
    '''
    Upload monitored route to subscriber
    '''
    servicetype, url, name = get_service_url(subscriber)
    if servicetype == 'VIS':
        fname = 'export/monitored.uvid'
        if os.path.exists(fname):
            with open(fname, 'r') as f:
                data = json.loads(f.read())
                routeFile = 'export/' + data['route']
                if os.path.exists(routeFile):
                    with open(routeFile) as f:
                        route = f.read()
                        tree = ET.parse(routeFile)
                        root = tree.getroot()
                        routeInfo = root.find('{http://www.cirm.org/RTZ/1/1}routeInfo')
                        if not (routeInfo is None):
                            routeName = routeInfo.get('routeName')
                        else:
                            routeName = data['route']
                        post_voyageplan(url, route, uvid=data['uvid'], name=name, routeName=routeName)
    if servicetype == 'MCL':
        fname = 'export/monitored.uvid'
        if os.path.exists(fname):
            with open(fname, 'r') as f:
                data = json.loads(f.read())
                routeFile = 'export/' + data['route']
                if os.path.exists(routeFile):
                    with open(routeFile) as f:
                        route = f.read()
                        tree = ET.parse(routeFile)
                        root = tree.getroot()
                        routeInfo = root.find('{http://www.cirm.org/RTZ/1/1}routeInfo')
                        if not (routeInfo is None):
                            routeName = routeInfo.get('routeName')
                        else:
                            routeName = data['route']
                        post_dmi(url, route, uvid=data['uvid'], name=name, routeName=routeName)

def upload_alternate(subscriber):
    '''
    Upload alternate route to subscriber
    '''
    servicetype, url, name = get_service_url(subscriber)
    if servicetype == 'VIS':
        fname = 'export/alternate.uvid'
        if os.path.exists(fname):
            with open(fname, 'r') as f:
                data = json.loads(f.read())
                routeFile = 'export/' + data['route']
                if os.path.exists(routeFile):
                    with open(routeFile) as f:
                        route = f.read()
                        tree = ET.parse(routeFile)
                        root = tree.getroot()
                        routeInfo = root.find('{http://www.cirm.org/RTZ/1/1}routeInfo')
                        if not (routeInfo is None):
                            routeName = routeInfo.get('routeName')
                        else:
                            routeName = data['route']
                        post_voyageplan(url, route, uvid=data['uvid'], name=name, routeName=routeName)
    if servicetype == 'MCL':
        fname = 'export/alternate.uvid'
        if os.path.exists(fname):
            with open(fname, 'r') as f:
                data = json.loads(f.read())
                routeFile = 'export/' + data['route']
                if os.path.exists(routeFile):
                    with open(routeFile) as f:
                        route = f.read()
                        tree = ET.parse(routeFile)
                        root = tree.getroot()
                        routeInfo = root.find('{http://www.cirm.org/RTZ/1/1}routeInfo')
                        if not (routeInfo is None):
                            routeName = routeInfo.get('routeName')
                        else:
                            routeName = data['route']
                        post_dmi(url, route, uvid=data['uvid'], name=name, routeName=routeName)

def upload_monitored_to_all():
    '''
    Upload monitored to all subscribers
    '''
    if os.path.isfile('export/monitored.subs'):
        with open('export/monitored.subs') as f:
            subs = json.loads(f.read())
        for sub in subs:
            upload_monitored(sub)
        if os.path.isfile('export/monitored.uvid'):
            shutil.copyfile('export/monitored.uvid', 'import/monitored.sent')

def upload_alternate_to_all():
    '''
    Upload alternate to all subscribers
    '''
    if os.path.isfile('export/alternate.uvid'):
        fname = 'export/alternate.subs'
        if os.path.isfile(fname):
            with open(fname) as f:
                subs = json.loads(f.read())
            for sub in subs:
                upload_alternate(sub)
        shutil.copyfile('export/alternate.uvid', 'import/alternate.sent')

'''
POST area method
'''
def post_area(url, area, deliveryAckEndPoint = None, name = None, areaName = 'area', client = conf['id']):
    headers = {
        'Content-Type': 'text/xml'
    }
    sub='/area'
    parameters = {
    }
    evtype = 1
    evpar = ''
    if not (deliveryAckEndPoint is None):
        parameters['deliveryAckEndPoint'] = deliveryAckEndPoint
        evpar = 'deliveryAckEndPoint:' + deliveryAckEndPoint
    try:
        if skip_trustchain(url):
            status = requests.post(url + sub, data=area.encode('utf-8'), params=parameters, headers=headers, cert=vis_cert)
        else:
            status = requests.post(url + sub, data=area.encode('utf-8'), params=parameters, headers=headers, cert=vis_cert, verify=trustchain)
    except Timeout as e:
        print(e)
        status = requests.Response
        status.text = "Timeout"
        status.status_code = 500
        evtype = 4
    except SSLError as e:
        print(e)
        status = requests.Response
        status.text = "SSLError"
        status.status_code = 500
        evtype = 6
    except ConnectionError as e:
        print(e)
        status = requests.Response
        status.text = "ConnectionError"
        status.status_code = 500
        evtype = 4
    log_event('post_area', url=url, name=name, ack=deliveryAckEndPoint, status=st(status), client = client, eventNumber = 8, eventType = evtype, eventDataType = 4, eventParameters = evpar)
    return status

def upload_area(to, msg):
    servicetype, url, name = get_service_url(to)
    if servicetype == 'VIS':
        post_area(url, msg, name = name)

'''
POST textMessage method
'''
def post_text(url, text, deliveryAckEndPoint = None, name = None, textName = 'text', client = conf['id']):
    headers = {
        'Content-Type': 'text/xml'
    }
    sub='/textMessage'
    parameters = {
    }
    evtype = 1
    evpar = ''
    if not (deliveryAckEndPoint is None):
        parameters['deliveryAckEndPoint'] = deliveryAckEndPoint
        evpar = 'deliveryAckEndPoint:' + deliveryAckEndPoint
    try:
        if skip_trustchain(url):
            status = requests.post(url + sub, data=text.encode('utf-8'), params=parameters, headers=headers, cert=vis_cert, timeout = 15)
        else:
            status = requests.post(url + sub, data=text.encode('utf-8'), params=parameters, headers=headers, cert=vis_cert, verify=trustchain, timeout = 15)
    except Timeout as e:
        print(e)
        status = requests.Response
        status.text = "Timeout"
        status.status_code = 500
        evtype = 4
    except SSLError as e:
        print(e)
        status = requests.Response
        status.text = "SSLError"
        status.status_code = 500
        evtype = 6
    except ConnectionError as e:
        print(e)
        status = requests.Response
        status.text = "ConnectionError"
        status.status_code = 500
        evtype = 4
    log_event('post_text', url=url, ack=deliveryAckEndPoint, status=st(status), client = client, eventNumber = 6, eventType = evtype, eventDataType = 2, eventParameters = evpar)
    return status

def upload_text(to, msg):
    servicetype, url, name = get_service_url(to)
    if servicetype == 'VIS':
        post_text(url, msg, name = name, client = to)

'''
POST acknowledgement method
'''
def post_ack(data):
    servicetype, url, name = get_service_url(data['fromId'])
    if url == 'None':
        status = requests.Response
        status.text = 'No url'
        status.status_code = 400
        return
    payload = collections.OrderedDict()
    
    if 'id' in data:
        payload['id'] = data['id']
    else:
        payload['id'] = 'urn:mrn:stm:id:missing'
    if 'referenceId' in data:
        payload['referenceId'] = data['referenceId']
    else:
        payload['referenceId'] = 'urn:mrn:stm:referenceid:missing'
    if 'time' in data:
        payload['timeOfDelivery'] = data['time']
    else:
        payload['timeOfDelivery'] = datetime.utcnow().replace(microsecond=0).isoformat() + 'Z'
    if 'fromId' in data:
        payload['fromId'] = data['fromId']
    else:
        payload['fromId'] = 'urn:mrn:stm:fromid:missing'
    if 'fromName' in data:
        payload['fromName'] = data['fromName']
    else:
        payload['fromName'] = 'Unknown sender'
    if 'toId' in data:
        payload['toId'] = data['toId']
    else:
        payload['toId'] = 'urn:mrn:stm:toid:missing'
    if 'toName' in data:
        payload['toName'] = data['toName']
    else:
        payload['toName'] = 'Unknown receiver'
    if 'ackResult' in data:
        payload['ackResult'] = data['ackResult']
    else:
        payload['ackResult'] = 'OK'
    sub='/acknowledgement'
    evtype = 1
    try:
        if skip_trustchain(url):
            status=requests.post(url + sub, json=payload, cert=vis_cert)
        else:
            status=requests.post(url + sub, json=payload, cert=vis_cert, verify=trustchain)
    except ValueError:
        status = requests.Response
        response.text = 'Fail'
        evtype = 4
    log_event('sent ack', name=name, status = st(status), client = data['fromId'], eventNumber = 14, eventType = evtype, eventDataType = 8)
    return status

'''
Extract waypoints and schedules
'''
def extract_waypoints(route):
    wps = []
    calculated = []
    bytestream = BytesIO(route.encode('utf-8'))
    bytestream.readline()
    bytestream.readline()
    tree = ET.parse(bytestream)
    root = tree.getroot()
    tag = root.tag[0:len(root.tag)-5]
    routeInfo = root.find(tag + 'routeInfo')
    if routeInfo:
        routeuvid = routeInfo.get('vesselVoyage')
    schedules = root.find(tag + 'schedules')
    if schedules:
        schedule = schedules.find(tag + 'schedule')
        if schedule:
            calculated = schedule.find(tag + 'calculated')
    waypoints = root.find(tag + 'waypoints')
    if waypoints:
        for wp in waypoints:
            a = wp.attrib
            if 'id' in a:
                wpnr = a['id']
                eta = ''
                pos = wp[0]
                for el in calculated:
                    if el.attrib['waypointId'] == wpnr:
                        if 'eta' in el.attrib:
                            eta = el.attrib['eta']
                        if 'etd' in el.attrib:
                            eta = el.attrib['etd']
                etalen = len(eta)
                eta = eta[0:etalen-1] + '.000+0000'
                wps.append({'eta': eta, 'lat': float(pos.attrib['lat']), 'lon': float(pos.attrib['lon']), 'heading': 'RL'})
    return routeuvid, wps

'''
POST forecast text messages
'''
def post_meteo_textmessage(forecast, i, validStart, validStop, routeuvid):
    routeReferenceId=routeuvid
    createTime=validStart
    if 'time' in forecast:
        createTime = forecast['time']
    createTime = createTime[:16]
    if not ('wind-dir' in forecast):
        return
    if not ('wind-speed' in forecast):
        return
    textMessageId='urn:mrn:stm:txt:dmi:' + createTime + ':' + str(i)
    userId='urn:mrn:mcl:service:instance:dmi:METOC_SejlRute-service'
    fromId='urn:mrn:mcl:service:instance:dmi:METOC_SejlRute-service'
    subject=createTime
    if 'lat' in forecast:
        lat = str(round(forecast['lat'],5))
    if 'lon' in forecast:
        lon = str(round(forecast['lon'],5))
    textmessage='''<?xml version="1.0" encoding="utf-8"?>
<textMessage
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xmlns="http://stmvalidation.eu/schemas/textMessageSchema_1_3.xsd">
  <textMessageId>''' + textMessageId + '''</textMessageId>
  <informationObjectReferenceId>''' + routeReferenceId + '''</informationObjectReferenceId>
  <informationObjectReferenceType>RTZ</informationObjectReferenceType>
  <validityPeriodStart>''' + validStart + '''</validityPeriodStart>
  <validityPeriodStop>''' + validStop + '''</validityPeriodStop>
  <author>DMI</author>
  <from>''' + fromId + '''</from>
  <serviceType>SHORE-MCL</serviceType>
  <createdAt>''' + createTime + '''</createdAt>
  <subject>''' + subject + '''</subject>
  <metoc/>
  <wind_direction>''' + str(round(forecast['wind-dir']['forecast'],1)) + '''</wind_direction>
  <wind_speed>''' + str(round(forecast['wind-speed']['forecast'],1)) + '''</wind_speed>
  <body>'''
    minibody = ''
    if 'time' in forecast:
        line = '    time ' + createTime
        textmessage = textmessage + line + '\n'
    if 'wind-dir' in forecast or 'wind-speed' in forecast:
        line = '    wind '
        if 'wind-dir' in forecast:
            line = line + str(round(forecast['wind-dir']['forecast'],1)) + ' degrees '
        if 'wind-speed' in forecast:
            line = line + str(round(forecast['wind-speed']['forecast'],1)) + ' m/s'
        minibody = textmessage + line
        textmessage = textmessage + line + '\n'
    if 'temperature' in forecast:
        line = '    temperature ' + str(round(forecast['temperature']['forecast'],1)) + ' degC'
        textmessage = textmessage + line + '\n'
    if 'current-dir' in forecast or 'current-speed' in forecast:
        line = '    current '
        if 'current-dir' in forecast:
            line = line + str(round(forecast['current-dir']['forecast'],1)) + ' degrees '
        if 'current-speed' in forecast:
            line = line + str(round(forecast['current-speed']['forecast'] * 3600 / 1852,1)) + ' kts'
        textmessage = textmessage + line + '\n'
    if 'wave-dir' in forecast or 'wave-height' in forecast or 'wave-period' in forecast:
        line = '    wave '
        if 'wave-dir' in forecast:
            line = line + str(round(forecast['wave-dir']['forecast'],1)) + ' degrees '
        if 'wave-height' in forecast:
            line = line + str(round(forecast['wave-height']['forecast'],1)) + ' m '
        if 'wave-period' in forecast:
            line = line + str(round(forecast['wave-period']['forecast'],1)) + ' s'
        textmessage = textmessage + line + '\n'
    if 'sealevel' in forecast:
        line = '    sealevel ' + str(round(forecast['sealevel']['forecast'],1)) + ' m'
        textmessage = textmessage + line + '\n'
    if 'sea-temperature' in forecast:
        line = '    sea-temperature ' + str(round(forecast['sealevel']['forecast'],1)) + ' degC'
        textmessage = textmessage + line + '\n'
    if 'salinity' in forecast:
        line = '    salinity ' + str(round(forecast['salinity']['forecast'],1)) + ' g/kg'
        textmessage = textmessage + line + '\n'
    if 'sea-ice-thickness' in forecast:
        line = '    sea-ice-thickness ' + str(round(forecast['sea-ice-thickness']['forecast'],1)) + ' m'
        textmessage = textmessage + line + '\n'
    if 'sea-ice-cover' in forecast:
        line = '    sea-ice-cover ' + str(round(forecast['sea-ice-cover']['forecast'],1)) + ' fraction: 0-1'
        textmessage = textmessage + line + '\n'
    if 'sea-ice-drift-dir' in forecast or 'sea-ice-drift-speed' in forecast:
        line = '    sea-ice-drift '
        if 'sea-ice-drift-dir' in forecast:
            line = line + str(round(forecast['sea-ice-drift-dir']['forecast'],1)) + ' degrees '
        if 'sea-ice-drift-speed' in forecast:
            line = line + str(round(forecast['sea-ice-drift-speed']['forecast'],1)) + ' m/s'
        textmessage = textmessage + line + '\n'
    textmessage = textmessage + '''  </body>
  <position lat="''' + lat + '" lon="' + lon + '''"/>
</textMessage>
''' 
    fname = 'import/' + textMessageId + '.xml'
    with open(fname, 'w') as f:
        f.write(textmessage)
    data = {
        "msg": textMessageId + '.xml',
        "from": fromId,
        "uvid": textMessageId,
        "subject": subject,
        "body": minibody,
        "graphics": True
    }
    fname = 'import/' + textMessageId + '.uvid'
    with open(fname, 'w') as f:
        f.write(json.dumps(data))


'''
POST meteorological query
'''
def post_dmi(url='http://sejlrute.dmi.dk/SejlRute/SR', route=None, uvid='', name='', routeName=''):
    headers={
        'Accept' : 'application/json',
        'Content-Type' : 'application/json'
    }
    wps = [
    {
      "heading":"GC",
      "lat":60.163433,
      "eta":"2018-03-27T12:00:00.000+0000",
      "lon":24.708550},
    {
      "eta":"2018-03-27T13:41:00.000+0000",
      "heading":"GC",
      "lat":59.794683,
      "lon":24.523083},
    {
      "eta":"2018-03-27T21:48:00.000+0000",
      "heading":"RL",
      "lat":59.498433,
      "lon":20.900950}
        ]
    routeuvid, wps = extract_waypoints(route)
    payload = collections.OrderedDict()
    payload['mssi'] = conf['mmsi']
    payload['datatypes'] = ["sealevel","current","wave","wind","sea-ice","sea-ice-drift","sea-temperature","salinity","temperature"]
    payload['dt'] = 360
    payload['waypoints'] = wps
    parameters={
        'req' : json.dumps(payload)
    }
    status = requests.post(url, params=parameters)
    if status.status_code == 200:
        data = json.loads(status.text)
        if 'metocForecast' in data:
            metocForecast = data['metocForecast']
            if metocForecast:
                if 'forecasts' in metocForecast:
                    forecasts = metocForecast['forecasts']
                    timefirst = ''
                    timelast = ''
                    i = 0
                    for forecast in forecasts:
                        if i == 0:
                            timefirst = str(forecast['time'])
                        timelast = str(forecast['time'])
                    i = 1
                    for forecast in forecasts:
                        post_meteo_textmessage(forecast, i, timefirst[:16], timelast[:16], routeuvid)
                        i = i+1
    return status

'''
POST PortCDM locationState method
'''
def post_pcm(url, msg, name=None, subj = None):
    sub='/amss/state_update'
    headers={
        'Content-Type' : 'application/xml'
    }
    if skip_trustchain(url):
        status = requests.post(url + sub, headers=headers, data=msg, cert=vis_cert)
    else:
        status = requests.post(url + sub, headers=headers, data=msg, cert=vis_cert, verify=trustchain)
    log_event('sent ' + subj, name=name, status = st(status))
    return status

def upload_pcm(to, msg):
    servicetype, url, name = get_service_url(to)
    if servicetype == 'PortCDM':
        fname = 'export/' + msg
        with open(fname) as f:
            text = f.read()
            tree = ET.parse(fname)
            root = tree.getroot()
            locationState = root.find('{urn:x-mrn:stm:schema:port-call-message:0.0.16}locationState')
            if not (locationState is None):
                timeval = locationState.find('{urn:x-mrn:stm:schema:port-call-message:0.0.16}time')
                subj = timeval.text
                arrivalLocation = locationState.find('{urn:x-mrn:stm:schema:port-call-message:0.0.16}arrivalLocation')
                if not (arrivalLocation is None):
                    to = arrivalLocation.find('{urn:x-mrn:stm:schema:port-call-message:0.0.16}to')
                    if not (to is None):
                        locationType = to.find('{urn:x-mrn:stm:schema:port-call-message:0.0.16}locationType')
                        subj = subj + ' ' + locationType.text
            else:
                subj = None
        post_pcm(url, text, name = name, subj = subj)
        shutil.copyfile(fname, 'import/portcdm.sent')

'''
Define PortCDM message queue filter to only receive material for my vessel
'''
pcmfilter='''[
  {
    "type": "VESSEL",
    "element": "urn:x-mrn:stm:vessel:IMO:''' + conf['imo'] + '''"
  }
]'''

'''
Define PortCDM message queue to capture everythin at the port
'''
pcmnofilter='''[
]'''

'''
Create message queue in a specified STM Port
'''
def createpcmqueue(instanceId, fil = pcmfilter):
    servicetype, url, name = get_service_url(instanceId)
    if servicetype == 'PortCDM':
        if portcdm_version == '0.0.16':
            sub='/mqs_legacy/mb/mqs'
        else:
            sub='/mb/mqs'
        headers={
            'Accept' : 'application/json',
            'Content-Type' : 'application/json'
        }
        try:
            if skip_trustchain(url):
                status = requests.post(url + sub, headers=headers, data=fil, cert=vis_cert, timeout = 15)
            else:
                status = requests.post(url + sub, headers=headers, data=fil, cert=vis_cert, verify=trustchain, timeout = 15)
        except Timeout as e:
            print(e)
            status = requests.Response
            status.text = "Timeout"
            status.status_code = 500
        except SSLError as e:
            print(e)
            status = requests.Response
            status.text = "SSLError"
            status.status_code = 500
        except ConnectionError as e:
            print(e)
            status = requests.Response
            status.text = "ConnectionError"
            status.status_code = 500
        if status.status_code == 200:
            queueId = status.text
            fname = 'import/queue.dat'
            queue = []
            if os.path.isfile(fname):
                with open(fname) as f:
                    queue = json.loads(f.read())
            found = False
            for srv in queue:
                if srv['instanceId'] == instanceId:
                    srv['queueId'] = queueId
                    found = True
            if not found:
                queue.append({'instanceId': instanceId, 'queueId': queueId})
            with open(fname,'w') as f:
                f.write(json.dumps(queue))
        return status
    status = requests.Response
    status.text = "Unknown"
    status.status_code = 500
    return status
            
'''
Create message queues for all STM Ports
'''
def createallqueues():
    fname = 'import/ports.dat'
    if os.path.isfile(fname):
        with open(fname) as f:
            queue = json.loads(f.read())
            for srv in queue:
                createpcmqueue(srv['instanceId'])

'''
Parse a PortCDM message
'''
def parse_portcdm(msg):
    body = ''
    if 'reportedAt' in msg:
        reportedAt = msg['reportedAt']
        messageId = msg['messageId']
        if not (msg['serviceState'] is None):
            serviceState = msg['serviceState']
            timeSequence = serviceState['timeSequence']
            timeval = serviceState['time']
            serviceObject = serviceState['serviceObject']
            if serviceObject:
                body = serviceObject + ' '
            else:
                body = ''
            if timeSequence:
                body = body + ' ' + timeSequence
            if timeval:
                t = datetime.utcfromtimestamp(timeval / 1000)
                body = body + ' at ' + t.strftime('%Y-%m-%dT%H:%MZ')
            if 'between' in serviceState:
                between = serviceState['between']
                if between:
                    fr = serviceState['between']['from']
                    if fr:
                        body = body + ' from '
                        name = fr['name']
                        if name:
                            body = body + name
                        frtyp = fr['locationType']
                        if frtyp:
                            body = body + ' (' + frtyp + ')'
                    to = serviceState['between']['to']
                    if to:
                        body = body + ' to '
                        name = to['name']
                        if name:
                            body = body + name
                        totyp = to['locationType']
                        if totyp:
                            body = body + ' (' + totyp + ')'
                with open('import/' + messageId + '.msg', 'w') as f:
                    f.write(body)
        elif not (msg['locationState'] is None):
            locationState = msg['locationState']
            timeType = locationState['timeType']
            timeval = locationState['time']
            t = datetime.utcfromtimestamp(timeval / 1000)
            body = timeType + ' ' + t.strftime('%Y-%m-%dT%H:%MZ')
            if not (locationState['arrivalLocation'] is None):
                to = locationState['arrivalLocation']['to']
                fr = locationState['arrivalLocation']['from']
            if not (locationState['departureLocation'] is None):
                to = locationState['departureLocation']['to']
                fr = locationState['departureLocation']['from']
            if not (fr is None):
                body = body + ' from '
                frtyp = fr['locationType']
                if not (fr['name'] is None):
                    body = body + fr['name'] + ' (' + frtyp + ')'
                else:
                    body = body + frtyp
            if not (to is None):
                body = body + ' to '
                totyp = to['locationType']
                if not (to['name'] is None):
                    body = body + to['name'] + ' (' + totyp + ')'
                else:
                    body = body + totyp
            with open('import/' + messageId + '.msg', 'w') as f:
                f.write(body)
    return body

'''
Poll for messages on a STM Port
'''
def pollpcmqueue(instanceId):
    servicetype, url, name = get_service_url(instanceId)
    if servicetype == 'PortCDM':
        fname = 'import/queue.dat'
        if os.path.isfile(fname):
            with open(fname) as f:
                queue = json.loads(f.read())
                for srv in queue:
                    if srv['instanceId'] == instanceId:
                        queueId = srv['queueId']
                        if portcdm_version == '0.0.16':
                            sub='/mqs_legacy/mb/mqs/' + queueId
                        else:
                            sub='/mb/mqs/' + queueId
                        headers={
                            'Accept' : 'application/json',
                            'Content-Type' : 'application/json'
                        }
                        if skip_trustchain(url):
                            res = requests.get(url + sub, headers=headers, cert=vis_cert)
                        else:
                            res = requests.get(url + sub, headers=headers, cert=vis_cert, verify=trustchain)
                        if not (res is None):
                            if (res.status_code == 200) and (res.text != 'ConnectionError'):
                                try:
                                    msgs = json.loads(res.text)
                                    for msg in msgs:
                                        messageId = msg['messageId']
                                        body = parse_portcdm(msg)
                                        log_event('msg ' + body, name=name, status = st(res))
                                        with open('import/' + messageId + '.uvid', 'w') as f:
                                            f.write(json.dumps(msg))
                                except:
                                    pass
                        return res
    res = requests.Response
    res.status_code = 500
    res.text = ""
    return res

'''
Poll messages on all STM Port message queues
'''
def pollallqueues():
    fname = 'import/queue.dat'
    if os.path.isfile(fname):
        with open(fname) as f:
            queue = json.loads(f.read())
            for srv in queue:
                res = pollpcmqueue(srv['instanceId'])
                if not (res is None):
                    if (res.status_code == 200) and (res.text != 'ConnectionError'):
                        try:
                            msgs = json.loads(res.text)
                            for msg in msgs:
                                messageId = msg['messageId']
                                parse_portcdm(msg)
                                with open('import/' + messageId + '.uvid', 'w') as f:
                                    f.write(json.dumps(msg))
                        except:
                            fname = 'import/queue.dat'

'''
Search Service Registry method
'''
def search(query, params = None):
    if staging:
        url="https://sr-staging.maritimecloud.net"
    else:
        url="https://sr.maritimecloud.net"
    sub='/api/_search/serviceInstance'
    headers={
        'Accept' : 'application/json'
    }
    parameters={
        'query' : query,
        'size' : 1000
    }
    if params is None:
        return requests.get(url + sub, headers=headers, params=parameters)
    else:
        if not (query is None):
            params['query'] = query;
        return requests.get(url + sub, headers=headers, params=params)

'''
Search Service Registry by geometry method
'''
def searchgeometry(query = None, params = None):
    if staging:
        url="https://sr-staging.maritimecloud.net"
    else:
        url="https://sr.maritimecloud.net"
    sub='/api/_searchGeometryWKT/serviceInstance'
    headers={
        'Accept' : 'application/json'
    }
    parameters={
        'query' : query,
        'size' : 1000
    }
    if params is None:
        return requests.get(url + sub, headers=headers, params=parameters)
    else:
        if not (query is None):
            params['query'] = query;
        return requests.get(url + sub, headers=headers, params=params)

usepcm = False

def vessel_connects():
    '''
    Check the possible new subsciptions and handle it if is allowed in acl.
    '''
    p = Path('import')
    subs = list(p.glob('**/all.subs'))
    if len(subs) > 0:
        for sub in subs:
            with sub.open() as f:
                new_subs = json.loads(f.read())
                if acl_allowed(new_subs[0]['uid']):
                    send_uvid_to = new_subs
                    q = Path('export')
                    q = q / sub.parts[1]
                    if q.exists():
                        with q.open() as f:
                            old_subs = json.loads(f.read())
                        for subscriber in old_subs:
                            if not ( subscriber in new_subs ):
                                new_subs.append(subscriber)
                    with open(str(q), 'w') as f:
                        f.write(json.dumps(new_subs))
                    for subscriber in send_uvid_to:
                        '''
                        Send monitored voyage to new subscribers
                        '''
                        upload_monitored(subscriber['url'])
                    os.remove(str(sub))
    '''
    Check the remaining non-allowed subscriptions and send them to the vessel
    '''
    if simulate_vessel:
        p = Path('import')
        subs = list(p.glob('**/*.subs'))
        if len(subs) > 0:
            for sub in subs:
                shutil.copyfile(str(sub), 'stm/' + sub.parts[1])
                os.remove(str(sub))
    '''
    Check the possible new subsciption removals and take care of them.
    '''
    if simulate_vessel:
        p = Path('import')
        rmsubs = list(p.glob('**/*.rmsubs'))
        if len(rmsubs) > 0:
            for rmsub in rmsubs:
                with rmsub.open() as f:
                    new_rmsubs = json.loads(f.read())
                os.remove(str(rmsub))
                sub = str(rmsub.parts[1]).split('.')[0] + '.subs'
                q = Path('export')
                q = q / sub
                if q.exists():
                    with q.open() as f:
                        old_subs = json.loads(f.read())
                    for subscriber in new_rmsubs:
                        if subscriber in old_subs:
                            old_subs.remove(subscriber)
                    if len(old_subs) == 0:
                        os.remove(str(q))
                    else:
                        with open(str(q), 'w') as f:
                            f.write(json.dumps(old_subs))
    '''
    Check for new voyage plans being uploaded and send ack if required.
    Also send the plans further if an active subscription exists.
    '''
    if simulate_vessel:
        p = Path('import')
        uvids = list(p.glob('**/urn:mrn:stm:voyage:id:*.uvid'))
        for item in uvids:
            rm_alternate()
            shutil.copyfile(str(item), 'export/alternate.uvid')
            os.remove(str(item))
            with open('export/alternate.uvid') as f:
                data = json.loads(f.read())
                if 'route' in data:
                    fname = 'import/' + data['route']
                    if os.path.isfile(fname):
                        shutil.move(fname, 'export/' + data['route'])
    '''
    Check for new areas being uploaded.
    '''
    if simulate_vessel:
        p = Path('import')
        areas = list(p.glob('**/*.S124'))
        if len(areas) > 0:
            for area in areas:
                shutil.copyfile(str(area), 'stm/' + area.parts[1])
                os.remove(str(area))
    '''
    Check for new text messages being uploaded.
    '''
    if simulate_vessel:
        p = Path('import')
        texts = list(p.glob('**/*.xml'))
        for text in texts:
            shutil.copyfile(str(text), 'stm/' + text.parts[1])
            os.remove(str(text)) 
    '''
    Check for new text messages to be sent.
    '''
    p = Path('export')
    msgs = list(p.glob('**/urn:mrn:stm:txt:imo:*.uvid'))
    if len(msgs) > 0:
        if os.path.isfile('import/textmsg.sent'):
            lastSentTime = os.path.getmtime('import/textmsg.sent')
        else:
            lastSentTime = None
        for msg in msgs:
            msg_already_sent = False
            if not (lastSentTime is None):
                if os.path.getmtime(str(msg)) < lastSentTime:
                    msg_already_sent = True
            if msg_already_sent == False:
                with msg.open() as f:
                    envel = json.loads(f.read())
                    fname = 'export/' + envel['msg']
                    if os.path.isfile(fname):
                        with open(fname) as g:
                            data = g.read()
                            upload_text(envel['to'], data)
                            shutil.copyfile(str(msg), 'import/textmsg.sent')
    '''
    Check for ack requests.
    '''
    p = Path('export')
    acks = list(p.glob('**/*.ack'))
    if len(acks) > 0:
        for ack in acks:
            fname = str(ack).lstrip('export/')
            if os.path.isfile('import/' + fname):
                os.remove('import/' + fname)
                with open(str(ack)) as f:
                    content = f.read()
                    try:
                        data = json.loads(content)
                    except ValueError:
                        data = { 'endpoint' : content }
                post_ack(data)
    '''
    Check for monitored route being changed.
    '''
    if os.path.isfile('export/monitored.uvid'):
        if os.path.isfile('import/monitored.sent'):
            if os.path.getmtime('export/monitored.uvid') > os.path.getmtime('import/monitored.sent'):
                upload_monitored_to_all()
        else:
            upload_monitored_to_all()
    '''
    Check for alternate route being changed.
    '''
    if os.path.isfile('export/alternate.uvid'):
        if os.path.isfile('import/alternate.sent'):
            if os.path.getmtime('export/alternate.uvid') > os.path.getmtime('import/alternate.sent'):
                upload_alternate_to_all()
        else:
            upload_alternate_to_all()
    '''
    Check for request changes.
    '''
    if os.path.isfile('export/request.subs'):
        if os.path.isfile('import/request.subs'):
            if os.path.getmtime('export/request.subs') > os.path.getmtime('import/request.subs'):
                upload_subscriptions_to_all()
        else:
            upload_subscriptions_to_all()
    '''
    Check for PortCDM messages to be sent.
    '''
    if usepcm:
        p = Path('export')
        uvids = list(p.glob('**/urn:x-mrn:stm:portcdm:message:*.uvid'))
        if len(uvids) > 0:
            for item in uvids:
                if os.path.isfile('import/portcdm.sent'):
                    if os.path.getmtime(str(item)) > os.path.getmtime('import/portcdm.sent'):
                        with item.open() as f:
                            data = json.loads(f.read())
                            upload_pcm(data['to'], data['msg'])
                else:
                    with item.open() as f:
                        data = json.loads(f.read())
                        upload_pcm(data['to'], data['msg'])
    '''
    Check for PortCDM messages to be received.
    '''
    if usepcm:
        pollallqueues()

def service():
    if usepcm:
        createallqueues()
    while True:
        time.sleep(20)
        vessel_connects()


