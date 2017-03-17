#!/bin/bash

python3 init_xlsx_report_sheet.py
./setup_VIS-1.sh
./setup_VIS-2.sh
./launch_VIS-1.sh
./launch_VIS-2.sh
cd VIS-1
tox
cd ../VIS-2
tox
rm -f ../stdout.log ../stderr.log
cd ../VIS-1
nosetests -v testVIS/test_VIS-001.py:TestVIS_001.test_VIS_001_00 > >(tee -a ../stdout.log) 2> >(tee -a ../stderr.log >&2)
cd ../VIS-2
nosetests -v testVIS/test_VIS-001.py:TestVIS_001.test_VIS_001_01 > >(tee -a ../stdout.log) 2> >(tee -a ../stderr.log >&2)
nosetests -v testVIS/test_VIS-001.py:TestVIS_001.test_VIS_001_02 > >(tee -a ../stdout.log) 2> >(tee -a ../stderr.log >&2)
nosetests -v testVIS/test_VIS-001.py:TestVIS_001.test_VIS_001_03 > >(tee -a ../stdout.log) 2> >(tee -a ../stderr.log >&2)
cd ../VIS-1
nosetests -v testVIS/test_VIS-001.py:TestVIS_001.vessel_connects > >(tee -a ../stdout.log) 2> >(tee -a ../stderr.log >&2)
cd ../VIS-2
nosetests -v testVIS/test_VIS-001.py:TestVIS_001.test_VIS_001_04 > >(tee -a ../stdout.log) 2> >(tee -a ../stderr.log >&2)
nosetests -v testVIS/test_VIS-001.py:TestVIS_001.test_VIS_001_05 > >(tee -a ../stdout.log) 2> >(tee -a ../stderr.log >&2)
cd ../VIS-1
nosetests -v testVIS/test_VIS-001.py:TestVIS_001.test_VIS_001_06 > >(tee -a ../stdout.log) 2> >(tee -a ../stderr.log >&2)
cd ../VIS-2
nosetests -v testVIS/test_VIS-001.py:TestVIS_001.test_VIS_001_07 > >(tee -a ../stdout.log) 2> >(tee -a ../stderr.log >&2)
nosetests -v testVIS/test_VIS-001.py:TestVIS_001.test_VIS_001_08 > >(tee -a ../stdout.log) 2> >(tee -a ../stderr.log >&2)
cd ../VIS-1
nosetests -v testVIS/test_VIS-001.py:TestVIS_001.test_VIS_001_09 > >(tee -a ../stdout.log) 2> >(tee -a ../stderr.log >&2)
cd ../VIS-2
nosetests -v testVIS/test_VIS-001.py:TestVIS_001.test_VIS_001_10 > >(tee -a ../stdout.log) 2> >(tee -a ../stderr.log >&2)
nosetests -v testVIS/test_VIS-001.py:TestVIS_001.test_VIS_001_11 > >(tee -a ../stdout.log) 2> >(tee -a ../stderr.log >&2)
nosetests -v testVIS/test_VIS-001.py:TestVIS_001.test_VIS_001_12_3_1 > >(tee -a ../stdout.log) 2> >(tee -a ../stderr.log >&2)
nosetests -v testVIS/test_VIS-001.py:TestVIS_001.test_VIS_001_12_3_2 > >(tee -a ../stdout.log) 2> >(tee -a ../stderr.log >&2)
nosetests -v testVIS/test_VIS-001.py:TestVIS_001.test_VIS_001_12_3_3 > >(tee -a ../stdout.log) 2> >(tee -a ../stderr.log >&2)
nosetests -v testVIS/test_VIS-001.py:TestVIS_001.test_VIS_001_12_4_1 > >(tee -a ../stdout.log) 2> >(tee -a ../stderr.log >&2)
nosetests -v testVIS/test_VIS-001.py:TestVIS_001.test_VIS_001_12_4_2 > >(tee -a ../stdout.log) 2> >(tee -a ../stderr.log >&2)
nosetests -v testVIS/test_VIS-001.py:TestVIS_001.test_VIS_001_12_4_3 > >(tee -a ../stdout.log) 2> >(tee -a ../stderr.log >&2)
nosetests -v testVIS/test_VIS-001.py:TestVIS_001.test_VIS_001_12_5_1 > >(tee -a ../stdout.log) 2> >(tee -a ../stderr.log >&2)
nosetests -v testVIS/test_VIS-001.py:TestVIS_001.test_VIS_001_12_5_2 > >(tee -a ../stdout.log) 2> >(tee -a ../stderr.log >&2)
nosetests -v testVIS/test_VIS-001.py:TestVIS_001.test_VIS_001_12_6_1 > >(tee -a ../stdout.log) 2> >(tee -a ../stderr.log >&2)
nosetests -v testVIS/test_VIS-001.py:TestVIS_001.test_VIS_001_12_7_1 > >(tee -a ../stdout.log) 2> >(tee -a ../stderr.log >&2)
nosetests -v testVIS/test_VIS-001.py:TestVIS_001.test_VIS_001_12_7_2 > >(tee -a ../stdout.log) 2> >(tee -a ../stderr.log >&2)
nosetests -v testVIS/test_VIS-001.py:TestVIS_001.test_VIS_001_12_7_3 > >(tee -a ../stdout.log) 2> >(tee -a ../stderr.log >&2)
nosetests -v testVIS/test_VIS-001.py:TestVIS_001.test_VIS_001_12_7_4 > >(tee -a ../stdout.log) 2> >(tee -a ../stderr.log >&2)

cd ../VIS-1
nosetests -v testVIS/test_VIS-002.py:TestVIS_002.test_VIS_002_00 > >(tee -a ../stdout.log) 2> >(tee -a ../stderr.log >&2)
cd ../VIS-2
nosetests -v testVIS/test_VIS-002.py:TestVIS_002.test_VIS_002_01 > >(tee -a ../stdout.log) 2> >(tee -a ../stderr.log >&2)
nosetests -v testVIS/test_VIS-002.py:TestVIS_002.test_VIS_002_02 > >(tee -a ../stdout.log) 2> >(tee -a ../stderr.log >&2)
nosetests -v testVIS/test_VIS-002.py:TestVIS_002.test_VIS_002_03 > >(tee -a ../stdout.log) 2> >(tee -a ../stderr.log >&2)
nosetests -v testVIS/test_VIS-002.py:TestVIS_002.test_VIS_002_04 > >(tee -a ../stdout.log) 2> >(tee -a ../stderr.log >&2)
nosetests -v testVIS/test_VIS-002.py:TestVIS_002.test_VIS_002_05 > >(tee -a ../stdout.log) 2> >(tee -a ../stderr.log >&2)
nosetests -v testVIS/test_VIS-002.py:TestVIS_002.test_VIS_002_06 > >(tee -a ../stdout.log) 2> >(tee -a ../stderr.log >&2)
nosetests -v testVIS/test_VIS-002.py:TestVIS_002.test_VIS_002_07 > >(tee -a ../stdout.log) 2> >(tee -a ../stderr.log >&2)
nosetests -v testVIS/test_VIS-002.py:TestVIS_002.test_VIS_002_08 > >(tee -a ../stdout.log) 2> >(tee -a ../stderr.log >&2)
cd ../VIS-1
nosetests -v testVIS/test_VIS-002.py:TestVIS_002.test_VIS_002_9_0 > >(tee -a ../stdout.log) 2> >(tee -a ../stderr.log >&2)
cd ../VIS-2
nosetests -v testVIS/test_VIS-002.py:TestVIS_002.test_VIS_002_9_1 > >(tee -a ../stdout.log) 2> >(tee -a ../stderr.log >&2)
cd ../VIS-1
nosetests -v testVIS/test_VIS-002.py:TestVIS_002.vessel_connects > >(tee -a ../stdout.log) 2> >(tee -a ../stderr.log >&2)
cd ../VIS-2
nosetests -v testVIS/test_VIS-002.py:TestVIS_002.test_VIS_002_9_2 > >(tee -a ../stdout.log) 2> >(tee -a ../stderr.log >&2)
nosetests -v testVIS/test_VIS-002.py:TestVIS_002.test_VIS_002_9_3 > >(tee -a ../stdout.log) 2> >(tee -a ../stderr.log >&2)
nosetests -v testVIS/test_VIS-002.py:TestVIS_002.test_VIS_002_9_4 > >(tee -a ../stdout.log) 2> >(tee -a ../stderr.log >&2)
nosetests -v testVIS/test_VIS-002.py:TestVIS_002.test_VIS_002_9_5 > >(tee -a ../stdout.log) 2> >(tee -a ../stderr.log >&2)
cd ../VIS-1
nosetests -v testVIS/test_VIS-002.py:TestVIS_002.vessel_connects > >(tee -a ../stdout.log) 2> >(tee -a ../stderr.log >&2)
cd ../VIS-2
nosetests -v testVIS/test_VIS-002.py:TestVIS_002.test_VIS_002_9_6 > >(tee -a ../stdout.log) 2> >(tee -a ../stderr.log >&2)
nosetests -v testVIS/test_VIS-002.py:TestVIS_002.test_VIS_002_9_7 > >(tee -a ../stdout.log) 2> >(tee -a ../stderr.log >&2)
cd ../VIS-1
nosetests -v testVIS/test_VIS-002.py:TestVIS_002.test_VIS_002_9_8 > >(tee -a ../stdout.log) 2> >(tee -a ../stderr.log >&2)
cd ../VIS-2
nosetests -v testVIS/test_VIS-003.py > >(tee -a ../stdout.log) 2> >(tee -a ../stderr.log >&2)

nosetests -v testVIS/test_VIS-004.py:TestVIS_004.test_VIS_004_01 > >(tee -a ../stdout.log) 2> >(tee -a ../stderr.log >&2)
nosetests -v testVIS/test_VIS-004.py:TestVIS_004.test_VIS_004_02 > >(tee -a ../stdout.log) 2> >(tee -a ../stderr.log >&2)
cd ../VIS-1
nosetests -v testVIS/test_VIS-004.py:TestVIS_004.vessel_connects > >(tee -a ../stdout.log) 2> >(tee -a ../stderr.log >&2)
cd ../VIS-2
nosetests -v testVIS/test_VIS-004.py:TestVIS_004.test_VIS_004_03 > >(tee -a ../stdout.log) 2> >(tee -a ../stderr.log >&2)
nosetests -v testVIS/test_VIS-004.py:TestVIS_004.test_VIS_004_04 > >(tee -a ../stdout.log) 2> >(tee -a ../stderr.log >&2)
nosetests -v testVIS/test_VIS-004.py:TestVIS_004.test_VIS_004_05 > >(tee -a ../stdout.log) 2> >(tee -a ../stderr.log >&2)
cd ../VIS-1
nosetests -v testVIS/test_VIS-005.py:TestVIS_005.test_VIS_005_0_1 > >(tee -a ../stdout.log) 2> >(tee -a ../stderr.log >&2)
cd ../VIS-2
nosetests -v testVIS/test_VIS-005.py:TestVIS_005.test_VIS_005_0_2 > >(tee -a ../stdout.log) 2> >(tee -a ../stderr.log >&2)
cd ../VIS-1
nosetests -v testVIS/test_VIS-005.py:TestVIS_005.test_VIS_005_0_3 > >(tee -a ../stdout.log) 2> >(tee -a ../stderr.log >&2)
nosetests -v testVIS/test_VIS-005.py:TestVIS_005.test_VIS_005_1_1 > >(tee -a ../stdout.log) 2> >(tee -a ../stderr.log >&2)
nosetests -v testVIS/test_VIS-005.py:TestVIS_005.test_VIS_005_1_2 > >(tee -a ../stdout.log) 2> >(tee -a ../stderr.log >&2)
cd ../VIS-1
nosetests -v testVIS/test_VIS-005.py:TestVIS_005.test_VIS_005_1_3 > >(tee -a ../stdout.log) 2> >(tee -a ../stderr.log >&2)
cd ../VIS-2
nosetests -v testVIS/test_VIS-005.py:TestVIS_005.test_VIS_005_2_1 > >(tee -a ../stdout.log) 2> >(tee -a ../stderr.log >&2)
nosetests -v testVIS/test_VIS-005.py:TestVIS_005.test_VIS_005_2_2 > >(tee -a ../stdout.log) 2> >(tee -a ../stderr.log >&2)
cd ..
python3 close_xlsx_report_sheet.py
python3 create_worksheet.py
