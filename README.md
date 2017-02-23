# Swagger generated server

## Overview
This server was generated by the [swagger-codegen](https://github.com/swagger-api/swagger-codegen) project. By using the
[OpenAPI-Spec](https://github.com/swagger-api/swagger-core/wiki) from a remote server, you can easily generate a server stub.  This
is an example of building a swagger-enabled Flask server.

This example uses the [Connexion](https://github.com/zalando/connexion) library on top of Flask.

### SSL certification

In order to use SSL certificates you need to add your service instance certificates in the main directory. Have a look at __main__.py for the name of the host, ports and certificates.

To run the server, please execute the following from the root directory:

```
pip3 install -r requirements.txt
python3 -m swagger_server
```

and open your browser to here:

```
https://stm.furuno.fi:8002/8320767/ui/
```

Your Swagger definition lives here:

```
https://stm.furuno.fi:8002/8320767/swagger.json
```

To launch the integration tests, use tox:
```
sudo pip install tox
tox
```
