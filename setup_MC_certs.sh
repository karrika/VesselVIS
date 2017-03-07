#!/bin/bash

sudo mkdir -p /usr/share/ca-certificates/MCproduction
sudo cp MCproduction/mc-ca-chain.pem /usr/share/ca-certificates/MCproduction
sudo mkdir -p /usr/share/ca-certificates/MCtest
sudo cp MCtest/mc-ca-chain.pem /usr/share/ca-certificates/MCtest
sudo ln -s /usr/share/ca-certificates/MCproduction/mc-ca-chain.pem /usr/lib/ssl/certs/24fc69e9.0
sudo ln -s /usr/share/ca-certificates/MCtest/mc-ca-chain.pem /usr/lib/ssl/certs/dfa402ab.0
