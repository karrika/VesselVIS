#!/usr/bin/env python3

import connexion
from .encoder import JSONEncoder
import ssl


if __name__ == '__main__':
    context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    context.load_cert_chain('Certificate_VIS-IMO8320767.pem',\
                            'PrivateKey_VIS-IMO8320767.pem')
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'Voyage Information Service API facing SeaSWIM through SSC exposing interfaces to SeaSWIM stakeholders'})
    app.run(port=8002)
