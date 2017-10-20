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

simulate_vessel = False

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
        conf['stmport'] = data['stmport']
        conf['id'] = data['id']
        length = len(data['id'])
        conf['imo'] = data['id'][length-7:length]
        conf['name'] = data['name']
        conf['open_to_all'] = data['open_to_all']
        conf['simulate_vessel'] = data['simulate_vessel']
        simulate_vessel = data['simulate_vessel']
vis_cert = list(p.glob('**/Certificate_*.pem'))
if len(vis_cert) == 0:
    print('Error: no Certificate_*.pem found')
else:
    vesselName = str(vis_cert[0])
    vesselName = vesselName[12:len(vesselName)-4]
vis_key = list(p.glob('**/PrivateKey_*.pem'))
if len(vis_key) == 0:
    print('Error: no PrivateKey_*.pem found')
vis_trust = list(p.glob('**/mc-ca-chain.pem'))
if len(vis_trust) == 0:
    print('Error: no mc-ca-chain.pem found')

vis_cert=(str(vis_cert[0]), str(vis_key[0]))
trustchain=str(vis_trust[0])

url="https://localhost:8001"
callbackurl=conf['host'] + ':' + str(conf['stmport'])
vis2_uvid='urn:mrn:stm:service:instance:furuno:vis2'

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

def log_event(eventname, name = None, callback = None, uvid = None, routeStatus = None, ack = None, url = None, status = None, client = None):
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
    with open('import/event.log', 'a') as f:
        json.dump(data, f, ensure_ascii=True)
        f.write('\n')

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
Unit tests only
'''
def rm_acl():
    fname = 'export/all.acl'
    if os.path.isfile(fname):
        os.remove(fname)
    fname = 'export/monitored.subs'
    if os.path.isfile(fname):
        os.remove(fname)
    fname = 'export/alternate.subs'
    if os.path.isfile(fname):
        os.remove(fname)

def set_acl(id, uvid=None):
    rm_acl()
    data=[ id ]
    fname = 'export/all.acl'
    with open(fname, 'w') as f:
        f.write(json.dumps(data))

def rm_alternate():
    fname = 'export/alternate.uvid'
    if os.path.isfile(fname):
        with open(fname) as f:
            data = json.loads(f.read())
            if 'route' in data:
                route = 'export/' + data['route']
                if os.path.isfile(route):
                    os.remove(route)
        os.remove(fname)

def uvid_exists(uvid):
    p = Path('export')
    uvids = list(p.glob('**/' + uvid + '.uvid'))
    return len(uvids) > 0

def rtz_exists(uvid):
    p = Path('export')
    uvids = list(p.glob('**/' + uvid + '.rtz'))
    return len(uvids) > 0

def subs_exists(uvid):
    p = Path('export')
    if uvid is None:
        uvids = list(p.glob('**/all.subs'))
    else:
        uvids = list(p.glob('**/' + uvid + '.subs'))
    return len(uvids) > 0

def acl_exists(uvid):
    p = Path('export')
    if uvid is None:
        uvids = list(p.glob('**/all.acl'))
    else:
        uvids = list(p.glob('**/' + uvid + '.acl'))
    return len(uvids) > 0

def acl_allowed(uvid):
    p = Path('export')
    all = list(p.glob('**/all.acl'))
    if len(all) > 0:
        with open(str(all[0]), 'r') as f:
            data = json.loads(f.read())
        if uvid in data:
            return True
    return False

def rm_subs(id, uvid=None):
    if uvid is None:
        if subs_exists(None):
            os.remove('export/all.subs') 
    else:
        if subs_exists(uvid):
            os.remove('export/' + uvid + '.subs') 

def rm_uvid(uvid):
    if uvid is None:
        if subs_exists(None):
            os.remove('export/all.subs') 
        if acl_exists(uvid):
            os.remove('export/all.acl') 
    else:
        if uvid_exists(uvid):
            os.remove('export/' + uvid + '.uvid') 
        if rtz_exists(uvid):
            os.remove('export/' + uvid + '.rtz') 
        if subs_exists(uvid):
            os.remove('export/' + uvid + '.subs') 
        if acl_exists(uvid):
            os.remove('export/' + uvid + '.acl') 

def get_voyageplan(url, uvid = None, routeStatus = None, name = None):
    parameters = {
    }
    sub='/voyagePlans'
    if not (uvid is None):
        parameters['uvid'] = uvid
    if not (routeStatus is None):
        parameters['routeStatus'] = routeStatus
    try:
        status = requests.get(url + sub, params = parameters, cert=vis_cert, verify=trustchain, timeout = 15)
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
    log_event('get voyageplan', name=name, status = status.text, url=url)
    return status

def subscribe_voyageplan(url, callback, uvid = None, name = None):
    sub='/voyagePlans/subscription'
    if uvid is None:
        parameters={
            'callbackEndpoint': callback
        }
        status = requests.post(url + sub, params=parameters, cert=vis_cert, verify=trustchain)
        log_event('subscribe', name=name, status = status.text)
        return status
    parameters={
        'callbackEndpoint': callback,
        'uvid': uvid
    }
    status = requests.post(url + sub, params=parameters, cert=vis_cert, verify=trustchain)
    log_event('subscribe', name=name, status = status.text)
    return status

def get_subscriptions(url, callback, name=None):
    sub='/voyagePlans/subscription'
    parameters={
        'callbackEndpoint': callback
    }
    status = requests.get(url + sub, params=parameters, cert=vis_cert, verify=trustchain)
    log_event('get subscriptions', name=name, status = status.text)
    return status

def unsubscribe_voyageplan(url, callback, uvid = None, name = None):
    sub='/voyagePlans/subscription'
    if uvid is None:
        parameters={
            'callbackEndpoint': callback
        }
        status = requests.delete(url + sub, params=parameters, cert=vis_cert, verify=trustchain)
        log_event('delete subscription', name=name, status = status.text)
        return status
    parameters={
        'callbackEndpoint': callback,
        'uvid': uvid
    }
    status = requests.delete(url + sub, params=parameters, cert=vis_cert, verify=trustchain)
    log_event('delete subscription', name=name, status = status.text)
    return status

def post_voyageplan(url, voyageplan, deliveryAckEndPoint = None, callbackEndpoint = callbackurl, uvid = None, name = '', routeName = ''):
    headers = {
        'Content-Type': 'text/xml'
    }
    parameters = {
    }
    if not (deliveryAckEndPoint is None):
        parameters['deliveryAckEndPoint'] = deliveryAckEndPoint
    if not (callbackEndpoint is None):
        parameters['callbackEndpoint'] = callbackEndpoint
    sub='/voyagePlans'
    try:
        status = requests.post(url + sub, data=voyageplan.encode('utf-8'), params = parameters, headers = headers, cert=vis_cert, verify=trustchain, timeout = 15)
    except requests.exceptions.Timeout:
        status = requests.Response
        status.text = "Timeout"
    log_event('sent ' + routeName, name=name, status = status.text)
    return status

def post_area(url, area, deliveryAckEndPoint = None):
    headers = {
        'Content-Type': 'text/xml'
    }
    sub='/area'
    parameters = {
    }
    if not (deliveryAckEndPoint is None):
        parameters['deliveryAckEndPoint'] = deliveryAckEndPoint
    log_event('post_area', None)
    return requests.post(url + sub, data=area.encode('utf-8'), headers=headers, cert=vis_cert, verify=trustchain)

def post_text(url, text, deliveryAckEndPoint = None):
    headers = {
        'Content-Type': 'text/xml'
    }
    sub='/textMessage'
    parameters = {
    }
    if not (deliveryAckEndPoint is None):
        parameters['deliveryAckEndPoint'] = deliveryAckEndPoint
    try:
        status = requests.post(url + sub, data=text.encode('utf-8'), params=parameters, headers=headers, cert=vis_cert, verify=trustchain, timeout = 15)
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
    log_event('post_text', url=url, ack=deliveryAckEndPoint, status=status.text)
    return status

def post_pcm(url, msg, name=None, subj = None):
    sub='/amss/state-update'
    headers={
        'Content-Type' : 'application/xml'
    }
    status = requests.post(url + sub, headers=headers, data=msg, cert=vis_cert, verify=trustchain)
    log_event('sent ' + subj, name=name, status = status.text)
    return status

def get_service_url(xml):
    instanceId = os.path.splitext(os.path.basename(xml))[0]
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
                    return ('VIS', item['endpointUri'], item['name'])
    if os.path.exists('import/vessels.dat'):
        with open('import/vessels.dat') as f:
            data=json.loads(f.read())
            for item in data:
                if item['instanceId'] == instanceId:
                    return ('VIS', item['endpointUri'], item['name'])
    return ('None', 'None', 'None')

def subscribe_all(instanceId):
    servicetype, url, name = get_service_url(instanceId)
    if servicetype == 'VIS':
        return subscribe_voyageplan(url, callbackurl, name=name)

def unsubscribe_all(instanceId):
    servicetype, url, name = get_service_url(instanceId)
    if servicetype == 'VIS':
        return unsubscribe_voyageplan(url, callbackurl, name=name)

def upload_xml(xml):
    servicetype, url, name = get_service_url(xml)
    if servicetype == 'PortCDM':
        with open(xml) as f:
            text = f.read()
            tree = ET.parse(xml)
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
        shutil.copyfile(xml, 'import/xmls.sent')
    if servicetype == 'VIS':
        with open(xml) as f:
            text = f.read()
        post_text(url, text)
        shutil.copyfile(xml, 'import/xmls.sent')

def upload_text(to, msg):
    servicetype, url, name = get_service_url(to)
    if servicetype == 'VIS':
        post_text(url, msg)

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

def upload_alternate_to_all():
    '''
    Upload alternate to all subscribers
    '''
    if os.path.isfile('export/alternate.subs'):
        with open('export/alternate.subs') as f:
            subs = json.loads(f.read())
        for sub in subs:
            upload_monitored(sub)
        if os.path.isfile('export/alternate.uvid'):
            shutil.copyfile('export/alternate.uvid', 'import/alternate.sent')

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
                upload_alternate(sub['url'])
        shutil.copyfile('export/alternate.uvid', 'import/alternate.sent')

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
            unsubscribe_all(preitem)
            shutil.copyfile('export/request.subs', 'import/request.subs')
    for curitem in current:
        if not (curitem in prev):
            subscribe_all(curitem)
            shutil.copyfile('export/request.subs', 'import/request.subs')

def post_ack(data):
    servicetype, url, name = get_service_url(data['fromId'])
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
    try:
        status=requests.post(url + sub, json=payload, cert=vis_cert, verify=trustchain)
    except ValueError:
        status = requests.Response
        response.text = 'Fail'
    log_event('sent ack', name=name, status = status.text)

def search(query, params = None):
    url="https://sr-staging.maritimecloud.net"
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

def searchgeometry(query = None, params = None):
    url="https://sr-staging.maritimecloud.net"
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

def sendpcm(body):
    url="https://sandbox-2.portcdm.eu:8443"
    sub='/amss/state-update'
    headers={
        'Content-Type' : 'application/xml'
    }
    return requests.post(url + sub, headers=headers, data=body, cert=vis_cert, verify=trustchain)

pcmfilter='''[
  {
    "type": "VESSEL",
    "element": "urn:x-mrn:stm:vessel:IMO:7917551"
  }
]'''

pcmnofilter='''[
]'''

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
                        return requests.get(url + sub, headers=headers, cert=vis_cert, verify=trustchain)
    res = requests.Response
    res.status_code = 500
    res.text = ""
    return res

def createallqueues():
    fname = 'import/ports.dat'
    if os.path.isfile(fname):
        with open(fname) as f:
            queue = json.loads(f.read())
            for srv in queue:
                createpcmqueue(srv['instanceId'])

def parse_portcdm(msg):
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

def pollallqueues():
    fname = 'import/queue.dat'
    if os.path.isfile(fname):
        with open(fname) as f:
            queue = json.loads(f.read())
            for srv in queue:
                res = pollpcmqueue(srv['instanceId'])
                if not (res is None):
                    if (res.status_code == 200) and (res.text != 'ConnectionError'):
                        msgs = json.loads(res.text)
                        for msg in msgs:
                            messageId = msg['messageId']
                            parse_portcdm(msg)
                            with open('import/' + messageId + '.uvid', 'w') as f:
                                f.write(json.dumps(msg))

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
    pollallqueues()

def service():
    createallqueues()
    while True:
        time.sleep(20)
        vessel_connects()


