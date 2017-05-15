#!/bin/bash

cp MCtest/mc-ca-chain.pem VIS-1
tar cf - encoder.py export import requirements.txt setup.py swagger_client swagger_server testVIS | (cd VIS-1; tar xfBp -)
sed -i '/^host:/c\host: "localhost:8001"' VIS-1/swagger_server/swagger/swagger.yaml
sed -i "/app.run/c\        app.run(host='localhost', port=8001, ssl_context=context)" VIS-1/swagger_server/__main__.py


