#!/usr/bin/env python3

import connexion
from .encoder import JSONEncoder
import ssl
from pathlib import Path
from pathlib import PurePath
import os


if __name__ == '__main__':
    p = Path('.')
    vis_cert = list(p.glob('**/Certificate_VIS*.pem'))
    if len(vis_cert) == 0:
        print('Error: no Certificate_VIS*.pem found')
    vis_key = list(p.glob('**/PrivateKey_VIS*.pem'))
    if len(vis_key) == 0:
        print('Error: no PrivateKey_VIS*.pem found')
    context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    context.load_cert_chain(str(vis_cert[0]), str(vis_key[0]))
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'Voyage Information Service API facing SeaSWIM through SSC exposing interfaces to SeaSWIM stakeholders'})
    app.run(host='ec2-35-157-50-165.eu-central-1.compute.amazonaws.com', port=443, ssl_context=context)
