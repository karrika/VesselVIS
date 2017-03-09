#!/bin/bash

./setup_VIS-1.sh
./setup_VIS-2.sh
./launch_VIS-1.sh
./launch_VIS-2.sh
cd VIS-2
tox
nosetests -v testVIS &> huu

