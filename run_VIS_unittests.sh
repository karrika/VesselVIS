#!/bin/bash

./setup_VIS-1.sh
./setup_VIS-2.sh
./launch_VIS-1.sh
./launch_VIS-2.sh
cd VIS-1
tox
cd ../VIS-2
tox
nosetests -v testVIS/test_VIS-001.py > >(tee -a ../stdout.log) 2> >(tee -a ../stderr.log >&2)
nosetests -v testVIS/test_VIS-002.py 
nosetests -v testVIS/test_VIS-002-1.py:TestVIS_002_1.test_VIS_002_9_7 > >(tee -a ../stdout.log) 2> >(tee -a ../stderr.log >&2)
cd ../VIS-1
nosetests -v testVIS/test_VIS-002-1.py:TestVIS_002_1.test_VIS_002_9_8 > >(tee -a ../stdout.log) 2> >(tee -a ../stderr.log >&2)
cd ../VIS-2
nosetests -v testVIS/test_VIS-002-1.py:TestVIS_002_1.test_VIS_002_9_9 > >(tee -a ../stdout.log) 2> >(tee -a ../stderr.log >&2)

