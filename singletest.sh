#!/bin/bash

SERVICE=$1

rm -f target.conf
ln -s $1 target.conf
python3 minitests.py
