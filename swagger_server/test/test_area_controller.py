# coding: utf-8

from __future__ import absolute_import

from . import BaseTestCase
from six import BytesIO
from flask import json
from pathlib import Path
import os


areamsg='''<?xml version="1.0" encoding="UTF-8"?>
<S124:DataSet xmlns:S124="http://www.iho.int/S124/gml/1.0"
	xsi:schemaLocation="http://www.iho.int/S124/gml/1.0 ../../schemas/0.5/S124.xsd" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xmlns:gml="http://www.opengis.net/gml/3.2"
	xmlns:S100="http://www.iho.int/s100gml/1.0"
	xmlns:xlink="http://www.w3.org/1999/xlink" gml:id="SE.local.100.17">
	<gml:boundedBy><gml:Envelope srsName="EPSG:4326">
			<gml:lowerCorner>-6.0000 30.0000</gml:lowerCorner>
			<gml:upperCorner>45.0000 47.0000</gml:upperCorner>
		</gml:Envelope></gml:boundedBy>
<imember>
	<S124:S124_NWPreamble gml:id="PR.SE.local.100.17">
	<id>urn:mrn:s124:NW.SE.local.100.17.P</id>
		<messageSeriesIdentifier>
				<NameOfSeries>Oregrund VTS</NameOfSeries>
				<typeOfWarning>local</typeOfWarning>
				<warningNumber>100</warningNumber>
				<year>17</year>
				<productionAgency>
					<language>eng</language>
					<text>SWEDISH MARITIME AUTHORITY</text>
				</productionAgency>
				<country>SE</country>
		</messageSeriesIdentifier>
		<sourceDate>2017-05-08</sourceDate>
		<generalArea>Sea of Åland and Archipelago Sea</generalArea>
		<locality><text>west of island Orskar</text></locality>
		<title><text>Small craft with 5 crew members is in a drift</text></title>
		<theWarningPart xlink:href="#NW.SE.local.100.17.1"/>
		</S124:S124_NWPreamble>
</imember>
<member>
	<S124:S124_NavigationalWarningPart gml:id="NW.SE.local.100.17.1">
		<id>urn:mrn:s124:NW.SE.local.100.17.1</id>
		<geometry>
		<S100:surfaceProperty>
		<gml:Polygon gml:id="s.NW.SE.local.100.17.1" srsName="EPSG:4326">
			<gml:exterior>
				<gml:LinearRing>
					<gml:posList>
						60.53 18.307
						60.53 18.35
						60.50 18.35
						60.50 18.307
						</gml:posList>
					</gml:LinearRing>
				</gml:exterior>
			</gml:Polygon>
		</S100:surfaceProperty>
		</geometry>  
		<header xlink:href="#PR.SE.local.100.17"/>
	</S124:S124_NavigationalWarningPart>
</member>
</S124:DataSet>
'''

class TestAreaController(BaseTestCase):
    """ AreaController integration test stubs """

    def test_upload_area(self):
        """
        Test case for upload_area

        
        """
        area = areamsg
        query_string = [('deliveryAckEndPoint', 'https://localhost:8002')]
        response = self.client.open('/area',
                                    method='POST',
                                    data=area,
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_upload_area_cleanup(self):
        """
        Test case for upload_area cleanup

        
        """
        vis2_uvid='urn:mrn:stm:service:instance:furuno:vis2'
        p = Path('import')
        files = list(p.glob('**/urn:mrn:s124:*'))
        for item in files:
            print(item)
            os.remove(str(item))
        pass

if __name__ == '__main__':
    import unittest
    unittest.main()
