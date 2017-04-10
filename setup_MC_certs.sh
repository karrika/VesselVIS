#!/bin/bash

sudo mkdir -p /usr/share/ca-certificates/MCproduction
sudo cp MCproduction/mc-ca-chain.pem /usr/share/ca-certificates/MCproduction
HASHPROD=`openssl x509 -hash -in MCproduction/mc-ca-chain.pem -noout`.0
sudo mkdir -p /usr/share/ca-certificates/MCtest
sudo cp MCtest/mc-ca-chain.pem /usr/share/ca-certificates/MCtest
HASHTEST=`openssl x509 -hash -in MCtest/mc-ca-chain.pem -noout`.0
sudo ln -s /usr/share/ca-certificates/MCproduction/mc-ca-chain.pem /usr/lib/ssl/certs/$HASHPROD
sudo ln -s /usr/share/ca-certificates/MCproduction/mc-ca-chain.pem /usr/lib/ssl/certs/$HASHTEST
