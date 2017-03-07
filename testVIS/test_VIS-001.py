# coding: utf-8

"""
    STM Voyage Information Service SeaSWIM Test cases
"""

from __future__ import absolute_import

import os
import sys
import unittest
from . import BaseTestCase
import swagger_client
from swagger_client.rest import ApiException
import requests
import shutil
import sys
import json
from pathlib import Path
from . import hostsettings

vis_cert=hostsettings.vis_cert
trustchain=hostsettings.trustchain

url=hostsettings.url
callbackurl=hostsettings.callbackurl
voyageuvid=hostsettings.voyageuvid
vis_uvid=hostsettings.vis_uvid

voyageplan='\
<?xml version="1.0" encoding="UTF-8"?>\
<route version="1.0" xmlns="http://www.cirm.org/RTZ/1/0">\
    <routeInfo routeName="Test-Mini-1"/>\
        <waypoints>\
                <waypoint id="1">\
                        <position lat="53.5123" lon="8.11998"/>\
                </waypoint>\
                <waypoint id="15">\
                        <position lat="53.0492" lon="8.87731"/>\
                </waypoint>\
        </waypoints>\
</route>\
'

voyageplan_in_the_past='\
<?xml version="1.0" encoding="UTF-8"?>\
<route version="1.0" xmlns="http://www.cirm.org/RTZ/1/0">\
    <routeInfo routeName="Test-Mini-1" validityPeriodStart="2016-12-22T13:00:00Z" validityPeriodStop="2016-12-23T13:00:00Z"/>\
        <waypoints>\
                <waypoint id="1">\
                        <position lat="53.5123" lon="8.11998"/>\
                </waypoint>\
                <waypoint id="15">\
                        <position lat="53.0492" lon="8.87731"/>\
                </waypoint>\
        </waypoints>\
</route>\
'

voyageplan_in_the_past_and_future='\
<?xml version="1.0" encoding="UTF-8"?>\
<route version="1.0" xmlns="http://www.cirm.org/RTZ/1/0">\
    <routeInfo routeName="Test-Mini-1" validityPeriodStart="2016-12-22T13:00:00Z" validityPeriodStop="2100-12-23T13:00:00Z"/>\
        <waypoints>\
                <waypoint id="1">\
                        <position lat="53.5123" lon="8.11998"/>\
                </waypoint>\
                <waypoint id="15">\
                        <position lat="53.0492" lon="8.87731"/>\
                </waypoint>\
        </waypoints>\
</route>\
'

voyageplan_in_the_future10='\
<?xml version="1.0" encoding="UTF-8"?>\
<route version="1.0" xmlns="http://www.cirm.org/RTZ/1/0">\
    <routeInfo routeName="Test-Mini-1" validityPeriodStart="2100-12-22T13:00:00Z" validityPeriodStop="2100-12-23T13:00:00Z"/>\
        <waypoints>\
                <waypoint id="1">\
                        <position lat="53.5123" lon="8.11998"/>\
                </waypoint>\
                <waypoint id="15">\
                        <position lat="53.0492" lon="8.87731"/>\
                </waypoint>\
        </waypoints>\
</route>\
'

voyageplan_in_the_future11='\
<?xml version="1.0" encoding="UTF-8"?>\
<route version="1.0" xmlns="http://www.cirm.org/RTZ/1/1">\
    <routeInfo routeName="Test-Mini-1" validityPeriodStart="2100-12-22T13:00:00Z" validityPeriodStop="2100-12-23T13:00:00Z"/>\
        <waypoints>\
                <waypoint id="1">\
                        <position lat="53.5123" lon="8.11998"/>\
                </waypoint>\
                <waypoint id="15">\
                        <position lat="53.0492" lon="8.87731"/>\
                </waypoint>\
        </waypoints>\
</route>\
'

voyageplan_in_the_future20='\
<?xml version="1.0" encoding="UTF-8"?>\
<route version="1.0" xmlns="http://www.cirm.org/RTZ/2/0">\
    <routeInfo routeName="Test-Mini-1" validityPeriodStart="2100-12-22T13:00:00Z" validityPeriodStop="2100-12-23T13:00:00Z"/>\
        <waypoints>\
                <waypoint id="1">\
                        <position lat="53.5123" lon="8.11998"/>\
                </waypoint>\
                <waypoint id="15">\
                        <position lat="53.0492" lon="8.87731"/>\
                </waypoint>\
        </waypoints>\
</route>\
'

voyageplan_in_the_future_stm20='\
<?xml version="1.0" encoding="UTF-8"?>\
<route version="1.0" xmlns="http://www.cirm.org/RTZ/2/0">\
    <routeInfo routeName="Test-Mini-1" validityPeriodStart="2100-12-22T13:00:00Z" validityPeriodStop="2100-12-23T13:00:00Z"/>\
        <waypoints>\
                <waypoint id="1">\
                        <position lat="53.5123" lon="8.11998"/>\
                </waypoint>\
                <waypoint id="15">\
                        <position lat="53.0492" lon="8.87731"/>\
                </waypoint>\
        </waypoints>\
</route>\
'

voyageplan_incorrect_xml='\
<?xml version="1.0" encoding="UTF-8"?>\
<route version="1.0" xmlns="http://www.cirm.org/RTZ/1/0">\
        <waypoints>\
                <waypoint id="1">\
                        <position lat="53.5123" lon="8.11998"/>\
                </waypoint>\
                <waypoint id="15">\
                        <position lat="53.0492" lon="8.87731"/>\
                </waypoint>\
        </waypoints>\
'

voyageplan_incorrect_schema='\
<?xml version="1.0" encoding="UTF-8"?>\
<route version="1.0" xmlns="http://www.cirm.org/RTZ/1/0">\
    <elephant routeName="Test-Mini-1" validityPeriodStart="2100-12-22T13:00:00Z" validityPeriodStop="2100-12-23T13:00:00Z"/>\
        <waypoints>\
                <waypoint id="1">\
                        <position lat="53.5123" lon="8.11998"/>\
                </waypoint>\
                <waypoint id="15">\
                        <position lat="53.0492" lon="8.87731"/>\
                </waypoint>\
        </waypoints>\
</route>\
'


class TestVIS_001(BaseTestCase):
    """ VIS-001 tests """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_VIS_001_01(self):
        """
        VIS-001-1 - VIS-2: Request (get) voyage plan with chosen UVID from VIS-1

        
        """
        f = open('export/all.acl', 'w')
        data=[ ]
        f.write(json.dumps(data))
        f.close()
        f = open('export/' + voyageuvid + '.acl', 'w')
        data=[ ]
        f.write(json.dumps(data))
        f.close()

        sub='/voyagePlans'
        parameters={
            'uvid': 'urn:mrn:stm:voyage:id:not:found'
        }
        response=requests.get(url + sub, params=parameters, cert=vis_cert, verify=trustchain)
        self.assert404(response, "Response body is : " + response.text)

    def test_VIS_001_02(self):
        """
        VIS-001-2 - VIS-2: Subscribe to voyage plan with chosen UVID from VIS-1

        
        """
        sub='/voyagePlans/subscription'
        parameters={
            'callbackEndpoint': callbackurl + '/voyagePlans',
            'uvid': 'urn:mrn:stm:voyage:id:not:found'
        }
        payload={}
        response=requests.post(url + sub, params=parameters, json=payload, cert=vis_cert, verify=trustchain)
        self.assert403(response, "Response body is : " + response.text)

    def test_VIS_001_03(self):
        """
        VIS-001-3 - Publish voyage plan to VIS-1 with chosen UVID

        
        """
        sub='/voyagePlans'
        parameters={
            'uvid': 'urn:mrn:stm:voyage:id:new:plan'
        }
        payload={'route': voyageplan}
        response=requests.post(url + sub, params=parameters, json=payload, cert=vis_cert, verify=trustchain)
        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_001_03_1(self):
        """
        VIS-001-3-1 - Select VP with validityPeriodStart and validityPeriodStop in past and publish to VIS-1


        """
        sub='/voyagePlans'
        parameters={
            'uvid': 'urn:mrn:stm:voyage:id:new:plan'
        }
        payload={'route': voyageplan_in_the_past}
        response=requests.post(url + sub, params=parameters, json=payload, cert=vis_cert, verify=trustchain)
        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_001_03_2(self):
        """
        VIS-001-3-2 - Change validityPeriodStop to future and publish to VIS-1


        """
        sub='/voyagePlans'
        parameters={
            'uvid': 'urn:mrn:stm:voyage:id:new:plan'
        }
        payload={'route': voyageplan_in_the_past_and_future}
        response=requests.post(url + sub, params=parameters, json=payload, cert=vis_cert, verify=trustchain)
        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_001_03_3(self):
        """
        VIS-001-3-3 - Change validityPeriodStart to future and publish to VIS-1


        """
        sub='/voyagePlans'
        parameters={
            'uvid': 'urn:mrn:stm:voyage:id:new:plan'
        }
        payload={'route': voyageplan_in_the_future10}
        response=requests.post(url + sub, params=parameters, json=payload, cert=vis_cert, verify=trustchain)
        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_001_04_1(self):
        """
        VIS-001-4-1 - Select VP according to schema RTZ 1.0 and publish to VIS-1


        """
        sub='/voyagePlans'
        parameters={
            'uvid': 'urn:mrn:stm:voyage:id:new:plan'
        }
        payload={'route': voyageplan_in_the_future10}
        response=requests.post(url + sub, params=parameters, json=payload, cert=vis_cert, verify=trustchain)
        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_001_04_2(self):
        """
        VIS-001-4-2 - Select VP according to schema RTZ 1.1 and publish to VIS-1


        """
        sub='/voyagePlans'
        parameters={
            'uvid': 'urn:mrn:stm:voyage:id:new:plan'
        }
        payload={'route': voyageplan_in_the_future11}
        response=requests.post(url + sub, params=parameters, json=payload, cert=vis_cert, verify=trustchain)
        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_001_04_3(self):
        """
        VIS-001-4-3 - Select VP according to schema RTZ 2.0 and publish to VIS-1


        """
        sub='/voyagePlans'
        parameters={
            'uvid': 'urn:mrn:stm:voyage:id:new:plan'
        }
        payload={'route': voyageplan_in_the_future20}
        response=requests.post(url + sub, params=parameters, json=payload, cert=vis_cert, verify=trustchain)
        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_001_04_4(self):
        """
        VIS-001-4-4 - Select VP according to schema RTZ STM 2.0 and publish to VIS-1 


        """
        sub='/voyagePlans'
        parameters={
            'uvid': 'urn:mrn:stm:voyage:id:new:plan'
        }
        payload={'route': voyageplan_in_the_future_stm20}
        response=requests.post(url + sub, params=parameters, json=payload, cert=vis_cert, verify=trustchain)
        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_001_05_1(self):
        """
        VIS-001-5-1 - Select VP in incorrect XML and publish to VIS-1 


        """
        sub='/voyagePlans'
        parameters={
            'uvid': 'urn:mrn:stm:voyage:id:new:plan'
        }
        payload={'route': voyageplan_incorrect_xml}
        response=requests.post(url + sub, params=parameters, json=payload, cert=vis_cert, verify=trustchain)
        self.assert400(response, "Response body is : " + response.text)

    def test_VIS_001_05_2(self):
        """
        VIS-001-5-2 - Select VP not following schema RTZ  and publish to VIS-1 


        """
        sub='/voyagePlans'
        parameters={
            'uvid': 'urn:mrn:stm:voyage:id:new:plan'
        }
        payload={'route': voyageplan_incorrect_schema}
        response=requests.post(url + sub, params=parameters, json=payload, cert=vis_cert, verify=trustchain)
        self.assert400(response, "Response body is : " + response.text)

    def test_VIS_001_04(self):
        """
        VIS-001-4 - VIS-2: Request voyage plan with chosen UVID from VIS-1

        
        """
        f = open('export/' + voyageuvid + '.acl', 'w')
        data=[ ]
        f.write(json.dumps(data))
        f.close()
        sub='/voyagePlans'
        parameters={
            'uvid': 'urn:mrn:stm:voyage:id:8320767'
        }
        response=requests.get(url + sub, params=parameters, cert=vis_cert, verify=trustchain)
        self.assert403(response, "Response body is : " + response.text)

    def test_VIS_001_05(self):
        """
        VIS-001-5 - VIS-2: Subscribe to voyage plan with chosen UVID from VIS-1

        
        """
        f = open('export/' + voyageuvid + '.acl', 'w')
        data=[ ]
        f.write(json.dumps(data))
        f.close()
        sub='/voyagePlans/subscription'
        parameters={
            'callbackEndpoint': callbackurl + '/voyagePlans',
            'uvid': 'urn:mrn:stm:voyage:id:8320767'
        }
        payload={}
        response=requests.post(url + sub, params=parameters, json=payload, cert=vis_cert, verify=trustchain)
        self.assert403(response, "Response body is : " + response.text)

    def test_VIS_001_06(self):
        """
        VIS-001-6 - VIS-1: Authorize organisation for VIS-2 to chosen UVID in VIS-1

        
        """
        f = open('export/' + voyageuvid + '.acl', 'w')
        data=[ vis_uvid ]
        f.write(json.dumps(data))
        f.close()
        pass

    def test_VIS_001_07(self):
        """
        VIS-001-7 - VIS-2: Request voyage plan with chosen UVID from VIS-1

        
        """
        sub='/voyagePlans'
        parameters={
            'uvid': 'urn:mrn:stm:voyage:id:8320767'
        }
        response=requests.get(url + sub, params=parameters, cert=vis_cert, verify=trustchain)
        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_001_08(self):
        """
        VIS-001-8 - VIS-2: Subscribe to voyage plan with chosen UVID from VIS-1

        
        """
        sub='/voyagePlans/subscription'
        parameters={
            'callbackEndpoint': callbackurl + '/voyagePlans',
            'uvid': 'urn:mrn:stm:voyage:id:8320767'
        }
        payload={}
        response=requests.post(url + sub, params=parameters, json=payload, cert=vis_cert, verify=trustchain)
        self.assert200(response, "Response body is : " + response.text)

    def test_VIS_001_09(self):
        """
        VIS-001-9 - VIS-1: Remove authorization to organisation for VIS-2 to chosen UVID

        
        """
        f = open('export/' + voyageuvid + '.acl', 'w')
        data=[ ]
        f.write(json.dumps(data))
        f.close()
        pass

    def test_VIS_001_10(self):
        """
        VIS-001-10 - VIS-2: Request voyage plan with chosen UVID from VIS-1

        
        """
        sub='/voyagePlans'
        parameters={
            'uvid': 'urn:mrn:stm:voyage:id:8320767'
        }
        response=requests.get(url + sub, params=parameters, cert=vis_cert, verify=trustchain)
        self.assert403(response, "Response body is : " + response.text)

    def test_VIS_001_11(self):
        """
        VIS-001-11 - VIS-2: Subscribe to voyage plan with chosen UVID from VIS-1

        
        """
        sub='/voyagePlans/subscription'
        parameters={
            'callbackEndpoint': callbackurl + '/voyagePlans',
            'uvid': 'urn:mrn:stm:voyage:id:8320767'
        }
        payload={}
        response=requests.post(url + sub, params=parameters, json=payload, cert=vis_cert, verify=trustchain)
        self.assert403(response, "Response body is : " + response.text)


if __name__ == '__main__':
    unittest.main()


