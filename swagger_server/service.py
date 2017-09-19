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
import shutil
import sys
import json
from pathlib import Path
from swagger_server.models.delivery_ack import DeliveryAck
import collections
from datetime import datetime
import time
from subprocess import call

simulate_vessel = False

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

conf={}
p = Path('.')
conffile = list(p.glob('**/vessel.conf'))
if len(conffile) > 0:
    with conffile[0].open() as f:
        data = json.loads(f.read())
        conf['host'] = data['host']
        conf['port'] = data['port']
        conf['id'] = data['id']
        conf['name'] = data['name']
        conf['open_to_all'] = data['open_to_all']
        conf['simulate_vessel'] = data['simulate_vessel']
        simulate_vessel = data['simulate_vessel']
vis_cert = list(p.glob('**/Certificate_VIS*.pem'))
if len(vis_cert) == 0:
    print('Error: no Certificate_VIS*.pem found')
else:
    vesselName = str(vis_cert[0])
    vesselName = vesselName[12:len(vesselName)-4]
vis_key = list(p.glob('**/PrivateKey_VIS*.pem'))
if len(vis_key) == 0:
    print('Error: no PrivateKey_VIS*.pem found')
vis_trust = list(p.glob('**/mc-ca-chain.pem'))
if len(vis_trust) == 0:
    print('Error: no mc-ca-chain.pem found')

vis_cert=(str(vis_cert[0]), str(vis_key[0]))
trustchain=str(vis_trust[0])

url="https://localhost:8001"
callbackurl="https://stm.furuno.fi:8000"

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

def log_event(name, callback = None, uvid = None, routeStatus = None, ack = None, url = None, status = None):
    data = collections.OrderedDict()
    data['time'] = datetime.utcnow().replace(microsecond=0).isoformat() + 'Z'
    if not (name is None):
        data['event'] = name
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
        data['status'] = status
    with open('import/event.log', 'a') as f:
        json.dump(data, f, ensure_ascii=True)
        f.write('\n')

def check_event(name, callback = None, uvid = None):
    with open('event.log', 'r') as f:
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

def set_acl(id, uvid=None):
    if uvid is None: 
        f = open('export/all.acl', 'w')
    else:
        f = open('export/' + uvid + '.acl', 'w')
    data=[ id ]
    f.write(json.dumps(data))
    f.close()

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

def rm_acl(id, uvid=None):
    if uvid is None:
        if acl_exists(None):
            os.remove('export/all.acl') 
    else:
        if acl_exists(uvid):
            os.remove('export/' + uvid + '.acl') 

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

def get_voyageplan(url, uvid = None, routeStatus = None):
    parameters = {
    }
    sub='/voyagePlans'
    if not (uvid is None):
        parameters['uvid'] = uvid
    if not (routeStatus is None):
        parameters['routeStatus'] = routeStatus
    log_event('get_voyage', uvid=uvid, routeStatus=routeStatus)
    return requests.get(url + sub, params=parameters, cert=vis_cert, verify=trustchain)

def subscribe_voyageplan(url, callback, uvid = None):
    sub='/voyagePlans/subscription'
    if uvid is None:
        parameters={
            'callbackEndpoint': callback
        }
        log_event('post_subscription', callback = callback)
        return requests.post(url + sub, params=parameters, cert=vis_cert, verify=trustchain)
    parameters={
        'callbackEndpoint': callback,
        'uvid': uvid
    }
    log_event('post_subscription', callback = callback, uvid = uvid)
    return requests.post(url + sub, params=parameters, cert=vis_cert, verify=trustchain)

def unsubscribe_voyageplan(url, callback, uvid = None):
    sub='/voyagePlans/subscription'
    if uvid is None:
        parameters={
            'callbackEndpoint': callback
        }
        return requests.delete(url + sub, params=parameters, cert=vis_cert, verify=trustchain)
    parameters={
        'callbackEndpoint': callback,
        'uvid': uvid
    }
    return requests.delete(url + sub, params=parameters, cert=vis_cert, verify=trustchain)

def post_voyageplan(url, voyageplan, deliveryAckEndPoint = None, callbackEndpoint = None, uvid = None):
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
    status = requests.post(url + sub, data=voyageplan.encode('utf-8'), params = parameters, headers = headers, cert=vis_cert, verify=trustchain)
    log_event('post_voyage', url=url, uvid=uvid, status=status.text)
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
    status = requests.post(url + sub, data=text.encode('utf-8'), params=parameters, headers=headers, cert=vis_cert, verify=trustchain)
    log_event('post_text', url=url, ack=deliveryAckEndPoint, status=status.text)
    return status

def post_pcm(url, msg):
    sub='/amss/state-update'
    headers={
        'Content-Type' : 'application/xml'
    }
    status = requests.post(url + sub, headers=headers, data=msg, cert=vis_cert, verify=trustchain)
    log_event('post_pcm', url=url, status=status.text)
    return status

def get_service_url(xml):
    fname = os.path.basename(xml)
    if os.path.exists('import/ports.dat'):
        with open('import/ports.dat') as f:
            data=json.loads(f.read())
            for item in data:
                if (item['instanceId'] + '.xml') == fname:
                    return ('PortCDM', item['endpointUri'])
    if os.path.exists('import/vts.dat'):
        with open('import/vts.dat') as f:
            data=json.loads(f.read())
            for item in data:
                if (item['instanceId'] + '.xml') == fname:
                    return ('VIS', item['endpointUri'])
    if os.path.exists('import/ros.dat'):
        with open('import/ros.dat') as f:
            data=json.loads(f.read())
            for item in data:
                if (item['instanceId'] + '.xml') == fname:
                    return ('VIS', item['endpointUri'])
    if os.path.exists('import/rcs.dat'):
        with open('import/rcs.dat') as f:
            data=json.loads(f.read())
            for item in data:
                if (item['instanceId'] + '.xml') == fname:
                    return ('VIS', item['endpointUri'])
    if os.path.exists('import/ems.dat'):
        with open('import/ems.dat') as f:
            data=json.loads(f.read())
            for item in data:
                if (item['instanceId'] + '.xml') == fname:
                    return ('VIS', item['endpointUri'])
    if os.path.exists('import/shore.dat'):
        with open('import/shore.dat') as f:
            data=json.loads(f.read())
            for item in data:
                if (item['instanceId'] + '.xml') == fname:
                    return ('VIS', item['endpointUri'])
    if os.path.exists('import/vessels.dat'):
        with open('import/vessels.dat') as f:
            data=json.loads(f.read())
            for item in data:
                if (item['instanceId'] + '.xml') == fname:
                    return ('VIS', item['endpointUri'])
    return ('None', 'None')

def upload_xml(xml):
    servicetype, url = get_service_url(xml)
    if servicetype == 'PortCDM':
        with open(xml) as f:
            text = f.read()
        post_pcm(url, text)
        shutil.copyfile(xml, 'import/xmls.sent')
    if servicetype == 'VIS':
        with open(xml) as f:
            text = f.read()
        post_text(url, text)
        shutil.copyfile(xml, 'import/xmls.sent')

def upload_monitored(subscriber):
    '''
    Upload monitored route to subscriber
    '''
    p = Path('export')
    uvids = list(p.glob('**/*.uvid'))
    for uvid in uvids:
        with open(str(uvid), 'r') as f:
            data = json.loads(f.read())
        if data['routeStatus'] == '7':
            '''
            Send this uvid to subscriber
            '''
            rtzs = list(p.glob('**/' + str(data['route'])))
            for rtz in rtzs:
                with rtz.open() as f:
                    route = f.read()
                post_voyageplan(subscriber, route, uvid=data['uvid'])

def upload_monitored_to_all():
    '''
    Upload monitored to all subscribers
    '''
    if os.path.isfile('export/monitored.uvid'):
        with open('export/all.subs') as f:
            subs = json.loads(f.read())
        for sub in subs:
            upload_monitored(sub['url'])
        shutil.copyfile('export/monitored.uvid', 'import/monitored.sent')

def upload_alternate(subscriber):
    '''
    Upload alternate route to subscriber
    '''
    p = Path('export')
    uvids = list(p.glob('**/*.uvid'))
    for uvid in uvids:
        with open(str(uvid), 'r') as f:
            data = json.loads(f.read())
        if data['routeStatus'] != '7':
            '''
            Send this uvid to subscriber
            '''
            rtzs = list(p.glob('**/' + str(data['route'])))
            for rtz in rtzs:
                with rtz.open() as f:
                    route = f.read()
                post_voyageplan(subscriber, route, uvid=data['uvid'])

def upload_alternate_to_all():
    '''
    Upload alternate to all subscribers
    '''
    if os.path.isfile('export/alternate.uvid'):
        with open('export/all.subs') as f:
            subs = json.loads(f.read())
        for sub in subs:
            upload_alternate(sub['url'])
        shutil.copyfile('export/alternate.uvid', 'import/alternate.sent')

def post_ack(data):
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
    if 'endpoint' in data:
        url = data['endpoint']
        sub='/acknowledgement'
        log_event('post_ack', callback=url)
        try:
            response=requests.post(url + sub, json=payload, cert=vis_cert, verify=trustchain)
        except ValueError:
            printf('Fail')

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

def sendpcm(body):
    url="https://sandbox-2.portcdm.eu:8443"
    sub='/amss/state-update'
    headers={
        'Content-Type' : 'application/xml'
    }
    return requests.post(url + sub, headers=headers, data=body, cert=vis_cert, verify=trustchain)

def vessel_connects():
    '''
    Check the possible new subsciptions and handle it if is allowed in acl.
    '''
    p = Path('import')
    subs = list(p.glob('**/*.subs'))
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
        uvids = list(p.glob('**/*.uvid'))
        for item in uvids:
            shutil.copyfile(str(item), 'stm/' + item.parts[1])
            shutil.copyfile(str(item), 'export/' + item.parts[1])
            os.remove(str(item)) 
        rtzs = list(p.glob('**/*.rtz'))
        for item in rtzs:
            shutil.copyfile(str(item), 'stm/' + item.parts[1])
            shutil.copyfile(str(item), 'export/' + item.parts[1])
            os.remove(str(item))
        
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
    Check for ack requests.
    '''
    p = Path('import')
    acks = list(p.glob('**/*.ack'))
    if len(acks) > 0:
        for ack in acks:
            with open(str(ack)) as f:
                content = f.read()
                try:
                    data = json.loads(content)
                except ValueError:
                    data = { 'endpoint' : content }
            os.remove(str(ack))
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
    Check for text and PortCDM messages to be sent.
    '''
    p = Path('export')
    xmls = list(p.glob('**/urn*.xml'))
    if len(xmls) > 0:
        for xml in xmls:
            if os.path.isfile('import/xmls.sent'):
                if os.path.getmtime(str(xml)) > os.path.getmtime('import/xmls.sent'):
                    upload_xml(str(xml))
                    '''os.remove(str(xml))'''
            else:
                upload_xml(str(xml))
                '''os.remove(str(xml))'''

def service():
    while True:
        time.sleep(20)
        vessel_connects()


