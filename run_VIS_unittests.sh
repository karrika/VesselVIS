#!/bin/bash

./setup_VIS-1.sh
./setup_VIS-2.sh
./launch_VIS-1.sh
./launch_VIS-2.sh
cd VIS-1
tox
cd ../VIS-2
tox
nosetests -v testVIS/test_VIS-001.py &> huu
nosetests -v testVIS/test_VIS-002.py:TestVIS_002.test_VIS_002_1 &>> huu
nosetests -v testVIS/test_VIS-002.py:TestVIS_002.test_VIS_002_2 &>> huu
nosetests -v testVIS/test_VIS-002.py:TestVIS_002.test_VIS_002_3 &>> huu
nosetests -v testVIS/test_VIS-002.py:TestVIS_002.test_VIS_002_4 &>> huu
nosetests -v testVIS/test_VIS-002.py:TestVIS_002.test_VIS_002_5 &>> huu
nosetests -v testVIS/test_VIS-002.py:TestVIS_002.test_VIS_002_6 &>> huu
nosetests -v testVIS/test_VIS-002.py:TestVIS_002.test_VIS_002_7 &>> huu
nosetests -v testVIS/test_VIS-002.py:TestVIS_002.test_VIS_002_8 &>> huu
nosetests -v testVIS/test_VIS-002.py:TestVIS_002.test_VIS_002_9_1 &>> huu
nosetests -v testVIS/test_VIS-002.py:TestVIS_002.test_VIS_002_9_2 &>> huu
nosetests -v testVIS/test_VIS-002.py:TestVIS_002.test_VIS_002_9_3 &>> huu

