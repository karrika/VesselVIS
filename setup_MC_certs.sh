#!/bin/bash

sudo mkdir -p /usr/share/ca-certificates/MCproduction
sudo cp MCproduction/mc-ca-chain.pem /usr/share/ca-certificates/MCproduction
HASHPROD=`openssl x509 -hash -in MCproduction/mc-ca-chain.pem -noout`.0
sudo mkdir -p /usr/share/ca-certificates/MCstaging
sudo cp MCstaging/mc-ca-chain.pem /usr/share/ca-certificates/MCstaging
HASHTEST=`openssl x509 -hash -in MCstaging/mc-ca-chain.pem -noout`.0
sudo rm -f /usr/lib/ssl/certs/$HASHPROD
sudo ln -s /usr/share/ca-certificates/MCproduction/mc-ca-chain.pem /usr/lib/ssl/certs/$HASHPROD
HASHTEST=70b4092a.0
sudo rm -f /usr/lib/ssl/certs/$HASHTEST
sudo ln -s /usr/share/ca-certificates/MCstaging/mc-ca-chain.pem /usr/lib/ssl/certs/$HASHTEST
HASHTEST=83dd6dbc.0
sudo rm -f /usr/lib/ssl/certs/$HASHTEST
sudo ln -s /usr/share/ca-certificates/MCstaging/mc-ca-chain.pem /usr/lib/ssl/certs/$HASHTEST
HASHTEST=a6566d95.0
sudo rm -f /usr/lib/ssl/certs/$HASHTEST
sudo ln -s /usr/share/ca-certificates/MCstaging/mc-ca-chain.pem /usr/lib/ssl/certs/$HASHTEST
HASHTEST=dfa402ab.0
sudo rm -f /usr/lib/ssl/certs/$HASHTEST
sudo ln -s /usr/share/ca-certificates/MCstaging/mc-ca-chain.pem /usr/lib/ssl/certs/$HASHTEST
