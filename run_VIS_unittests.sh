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
nosetests -v testVIS/test_VIS-001.py > >(tee -a ../stdout.log) 2> >(tee -a ../stderr.log >&2)
nosetests -v testVIS/test_VIS-002.py > >(tee -a ../stdout.log) 2> >(tee -a ../stderr.log >&2)
nosetests -v testVIS/test_VIS-002-1.py:TestVIS_002_1.test_VIS_002_9_0 > >(tee -a ../stdout.log) 2> >(tee -a ../stderr.log >&2)
nosetests -v testVIS/test_VIS-002-1.py:TestVIS_002_1.test_VIS_002_9_1 > >(tee -a ../stdout.log) 2> >(tee -a ../stderr.log >&2)
cd ../VIS-1
nosetests -v testVIS/test_VIS-002-1.py:TestVIS_002_1.vessel_connects > >(tee -a ../stdout.log) 2> >(tee -a ../stderr.log >&2)
cd ../VIS-2
nosetests -v testVIS/test_VIS-002-1.py:TestVIS_002_1.test_VIS_002_9_2 > >(tee -a ../stdout.log) 2> >(tee -a ../stderr.log >&2)
nosetests -v testVIS/test_VIS-002-1.py:TestVIS_002_1.test_VIS_002_9_3 > >(tee -a ../stdout.log) 2> >(tee -a ../stderr.log >&2)
nosetests -v testVIS/test_VIS-002-1.py:TestVIS_002_1.test_VIS_002_9_4 > >(tee -a ../stdout.log) 2> >(tee -a ../stderr.log >&2)
nosetests -v testVIS/test_VIS-002-1.py:TestVIS_002_1.test_VIS_002_9_5 > >(tee -a ../stdout.log) 2> >(tee -a ../stderr.log >&2)
cd ../VIS-1
nosetests -v testVIS/test_VIS-002-1.py:TestVIS_002_1.vessel_connects > >(tee -a ../stdout.log) 2> >(tee -a ../stderr.log >&2)
cd ../VIS-2
nosetests -v testVIS/test_VIS-002-1.py:TestVIS_002_1.test_VIS_002_9_6 > >(tee -a ../stdout.log) 2> >(tee -a ../stderr.log >&2)
nosetests -v testVIS/test_VIS-002-1.py:TestVIS_002_1.test_VIS_002_9_7 > >(tee -a ../stdout.log) 2> >(tee -a ../stderr.log >&2)
cd ../VIS-1
nosetests -v testVIS/test_VIS-002-1.py:TestVIS_002_1.test_VIS_002_9_8 > >(tee -a ../stdout.log) 2> >(tee -a ../stderr.log >&2)
cd ../VIS-2
nosetests -v testVIS/test_VIS-003.py > >(tee -a ../stdout.log) 2> >(tee -a ../stderr.log >&2)
#nosetests -v testVIS/test_VIS-004.py > >(tee -a ../stdout.log) 2> >(tee -a ../stderr.log >&2)
#cd ../VIS-1
#nosetests -v testVIS/test_VIS-005.py:TestVIS_005.test_VIS_005_0_1 > >(tee -a ../stdout.log) 2> >(tee -a ../stderr.log >&2)
#cd ../VIS-2
#nosetests -v testVIS/test_VIS-005.py:TestVIS_005.test_VIS_005_0_2 > >(tee -a ../stdout.log) 2> >(tee -a ../stderr.log >&2)
#cd ../VIS-1
#nosetests -v testVIS/test_VIS-005.py:TestVIS_005.test_VIS_005_0_3 > >(tee -a ../stdout.log) 2> >(tee -a ../stderr.log >&2)
#nosetests -v testVIS/test_VIS-005.py:TestVIS_005.test_VIS_005_1_1 > >(tee -a ../stdout.log) 2> >(tee -a ../stderr.log >&2)
#nosetests -v testVIS/test_VIS-005.py:TestVIS_005.test_VIS_005_1_2 > >(tee -a ../stdout.log) 2> >(tee -a ../stderr.log >&2)
#cd ../VIS-1
#nosetests -v testVIS/test_VIS-005.py:TestVIS_005.test_VIS_005_1_3 > >(tee -a ../stdout.log) 2> >(tee -a ../stderr.log >&2)
#cd ../VIS-2
#nosetests -v testVIS/test_VIS-005.py:TestVIS_005.test_VIS_005_2_1 > >(tee -a ../stdout.log) 2> >(tee -a ../stderr.log >&2)
#nosetests -v testVIS/test_VIS-005.py:TestVIS_005.test_VIS_005_2_2 > >(tee -a ../stdout.log) 2> >(tee -a ../stderr.log >&2)
cd ..
python3 close_xlsx_report_sheet.py
python3 create_worksheet.py
