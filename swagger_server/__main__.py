#!/usr/bin/env python3

import connexion
from .encoder import JSONEncoder
import ssl


if __name__ == '__main__':
    context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    context.load_cert_chain('Certificate_VIS-Falstaff.pem',\
                            'PrivateKey_VIS-Falstaff.pem')
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'Voyage Information Service API facing SeaSWIM through SSC exposing interfaces to SeaSWIM stakeholders'})
    app.run(host='ec2-35-157-50-165.eu-central-1.compute.amazonaws.com', port=443, ssl_context=context)
    #app.run(port=8002)
