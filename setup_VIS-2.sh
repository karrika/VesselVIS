#!/bin/bash

cp MCtest/mc-ca-chain.pem VIS-2
tar cf - encoder.py export import requirements.txt setup.py swagger_client swagger_server testVIS | (cd VIS-2; tar xfBp -)
sed -i '/^host:/c\host: "localhost:8002"' VIS-2/swagger_server/swagger/swagger.yaml
sed -i "/app.run/c\    app.run(host='localhost', port=8002, ssl_context=context)" VIS-2/swagger_server/__main__.py

