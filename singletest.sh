#!/bin/bash

SERVICE=$1

cd testVIS
rm hostsettings.py
ln -s $1_hostsettings.py hostsettings.py
cd ..
python3 minitests.py
