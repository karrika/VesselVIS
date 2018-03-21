#!/usr/bin/env python3

import connexion
from .encoder import JSONEncoder
import ssl
from pathlib import Path
from pathlib import PurePath
import os
from flask import request
from threading import Thread
from . import service

p = Path('.')
if service.staging:
    print('Staging', service.conf)
else:
    print('Production', service.conf)
vis_cert = list(p.glob('**/Certificate_*.pem'))
if len(vis_cert) == 0:
    print('Error: no Certificate_*.pem found')
vis_key = list(p.glob('**/PrivateKey_*.pem'))
if len(vis_key) == 0:
    print('Error: no PrivateKey_*.pem found')
context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
context.load_cert_chain(str(vis_cert[0]), str(vis_key[0]))
app = connexion.App(__name__, specification_dir='./swagger/')
app.app.json_encoder = JSONEncoder
app.add_api('swagger.yaml', arguments={'title': 'Voyage Information Service API facing SeaSWIM through SSC exposing interfaces to SeaSWIM stakeholders'})

if __name__ == '__main__':
    thread = Thread(target = service.service, args = ())
    thread.start()
    if service.conf is None:
        app.run(port=8000, host='127.0.0.1')
    else:
        app.run(port=service.conf['port'], host=service.conf['host'])
    thread.join()

