# coding: utf-8
from io import StringIO
from lxml import etree
import re

schema_str = '''<?xml version="1.0" encoding="utf-8"?>
<!--
  
  Text Message Exchange Format

  XML schema

  Revision 1.3
    Edition 2   Removed mininclusive in pattern for dateTimeUTC
	Edition 3   Adjusted pattern textMessageURN for textMessageId
	Edition 4	Adjusted minExclusive for radius and type positiveDouble
  Source: STM
-->
<xs:schema xmlns="http://stmvalidation.eu/schemas/textMessageSchema_1_3.xsd" xmlns:xs="http://www.w3.org/2001/XMLSchema" targetNamespace="http://stmvalidation.eu/schemas/textMessageSchema_1_3.xsd" elementFormDefault="qualified" id="textMessageSchema">
	<xs:annotation>
		<xs:documentation>A STM Text message type schema</xs:documentation>
	</xs:annotation>
	<xs:element name="textMessage">
		<xs:complexType>
			<xs:sequence>
				<xs:element name="textMessageId" type="textMessageURN" minOccurs="1" maxOccurs="1">
					<xs:annotation>
						<xs:documentation>Identifier of the text message, mandatory.</xs:documentation>
					</xs:annotation>
				</xs:element>
				<xs:element name="informationObjectReferenceId" type="xs:string" minOccurs="0" maxOccurs="1">
					<xs:annotation>
						<xs:documentation>A reference to an information object, optional.</xs:documentation>
					</xs:annotation>
				</xs:element>
				<xs:element name="informationObjectReferenceType" type="informationObjectTypeEnum" minOccurs="0" maxOccurs="1">
					<xs:annotation>
						<xs:documentation>STM payload format reference, optional.</xs:documentation>
					</xs:annotation>
				</xs:element>
				<xs:element name="validityPeriodStart" type="DateTimeUTC" minOccurs="0" maxOccurs="1">
					<xs:annotation>
						<xs:documentation>
              Start of validity period in ISO 8601 format, optional.
            </xs:documentation>
					</xs:annotation>
				</xs:element>
				<xs:element name="validityPeriodStop" type="DateTimeUTC" minOccurs="0" maxOccurs="1">
					<xs:annotation>
						<xs:documentation>
              Stop of validity period in ISO 8601 format, optional.
            </xs:documentation>
					</xs:annotation>
				</xs:element>
				<xs:element name="author" type="xs:string" maxOccurs="1">
					<xs:annotation>
						<xs:documentation>The message author, mandatory.</xs:documentation>
					</xs:annotation>
				</xs:element>
				<xs:element name="from" type="xs:string" maxOccurs="1">
					<xs:annotation>
						<xs:documentation>The sending actor, mandatory.</xs:documentation>
					</xs:annotation>
				</xs:element>
				<xs:element name="serviceType" type="xs:string" minOccurs="0" maxOccurs="1">
					<xs:annotation>
						<xs:documentation>The service type of the sender, optional.</xs:documentation>
					</xs:annotation>
				</xs:element>
				<xs:element name="createdAt" type="DateTimeUTC">
					<xs:annotation>
						<xs:documentation>The message creation dateTime, mandatory.</xs:documentation>
					</xs:annotation>
				</xs:element>
				<xs:element name="subject" type="xs:string">
					<xs:annotation>
						<xs:documentation>The message subject, mandatory.</xs:documentation>
					</xs:annotation>
				</xs:element>
				<xs:element name="body" type="xs:string">
					<xs:annotation>
						<xs:documentation>The message body,mandatory.</xs:documentation>
					</xs:annotation>
				</xs:element>
				<xs:element name="position" type="GM_Point" minOccurs="0" maxOccurs="1">
					<xs:annotation>
						<xs:documentation>Geographic point, optional.</xs:documentation>
					</xs:annotation>
				</xs:element>
				<xs:element name="area" type="GM_Surface" minOccurs="0" maxOccurs="1">
					<xs:annotation>
						<xs:documentation>Geographic area, optional.</xs:documentation>
					</xs:annotation>
				</xs:element>
			</xs:sequence>
		</xs:complexType>
	</xs:element>
	<xs:simpleType name="textMessageURN">
		<xs:annotation>
			<xs:documentation>
        Text message Id in STM URN format.
      </xs:documentation>
		</xs:annotation>
		<xs:restriction base="xs:string">
			<xs:maxLength value="120"/>
			<xs:pattern value="urn:mrn:stm:txt:[0-9a-zA-Z:+_-]+"/>
		</xs:restriction>
	</xs:simpleType>
	<xs:simpleType name="informationObjectTypeEnum">
		<xs:restriction base="xs:string">
			<xs:enumeration value="RTZ"/>
			<xs:enumeration value="S124"/>
			<xs:enumeration value="TXT"/>
		</xs:restriction>
	</xs:simpleType>
	<xs:simpleType name="DateTimeUTC">
		<xs:annotation>
			<xs:documentation>UTC time.</xs:documentation>
		</xs:annotation>
		<xs:restriction base="xs:dateTime">
			<xs:pattern value=".*Z"/>
		</xs:restriction>
	</xs:simpleType>
	<xs:complexType name="GM_Point">
		<xs:attribute name="lat" type="LatitudeType" use="required">
			<xs:annotation>
				<xs:documentation>Latitude in degrees.</xs:documentation>
			</xs:annotation>
		</xs:attribute>
		<xs:attribute name="lon" type="LongitudeType" use="required">
			<xs:annotation>
				<xs:documentation>Longitude in degrees.</xs:documentation>
			</xs:annotation>
		</xs:attribute>
	</xs:complexType>
	<xs:simpleType name="LatitudeType">
		<xs:annotation>
			<xs:documentation>
        The latitude of the point. Decimal degrees, WGS84 datum.
      </xs:documentation>
		</xs:annotation>
		<xs:restriction base="xs:decimal">
			<xs:minInclusive value="-90.0"/>
			<xs:maxInclusive value="90.0"/>
		</xs:restriction>
	</xs:simpleType>
	<xs:simpleType name="LongitudeType">
		<xs:annotation>
			<xs:documentation>
        The longitude of the point. Decimal degrees, WGS84 datum.
      </xs:documentation>
		</xs:annotation>
		<xs:restriction base="xs:decimal">
			<xs:minInclusive value="-180.0"/>
			<xs:maxInclusive value="180.0"/>
		</xs:restriction>
	</xs:simpleType>
	<xs:simpleType name="BearingType">
		<xs:restriction base="xs:decimal">
			<xs:fractionDigits value="1"/>
			<xs:minInclusive value="0.0"/>
			<xs:maxInclusive value="360.0"/>
		</xs:restriction>
	</xs:simpleType>
	<xs:simpleType name="positiveDouble">
		<xs:restriction base="xs:double">
			<xs:minExclusive value="0"/>
		</xs:restriction>
	</xs:simpleType>
	<xs:complexType name="S100_CircleByCenterPointType">
		<xs:annotation>
			<xs:documentation>Type for S-100 arc by center point geometry using interpolation circularArcCenterPointWithRadius</xs:documentation>
		</xs:annotation>
		<xs:sequence>
			<xs:element name="position" type="GM_Point"/>
			<xs:element name="radius" type="positiveDouble" >
				<xs:annotation>
					<xs:documentation>The radius is a double greater than zero and its unit is assumed to be nautical miles (nm).</xs:documentation>
				</xs:annotation>
			</xs:element>
		</xs:sequence>
		<xs:attribute name="id" type="xs:string">
			<xs:annotation>
				<xs:documentation>
          The attribute gml:id supports provision of a handle for the XML element
          representing a GML Object. Its use is optional for all GML objects.
        </xs:documentation>
			</xs:annotation>
		</xs:attribute>
	</xs:complexType>
	<xs:complexType name="GM_Surface">
		<xs:sequence>
			<xs:element name="Polygon" minOccurs="0">
				<xs:complexType>
					<xs:sequence>
						<xs:element name="posList" type="xs:string">
							<xs:annotation>
								<xs:documentation>
                  posList instances (and other instances with the content model specified
                  by DirectPositionListType) hold the coordinates for a sequence of direct positions
                  within the same coordinate reference system (CRS). if no srsName attribute is given,
                  the CRS shall be specified as part of the larger context this geometry element is
                  part of, typically a geometric object like a point, curve, etc. The optional
                  attribute count specifies the number of direct positions in the list. If the
                  attribute count is present then the attribute srsDimension shall be present, too.
                  The number of entries in the list is equal to the product of the dimensionality of
                  the coordinate reference system (i.e. it is a derived value of the coordinate
                  reference system definition) and the number of direct positions.
                </xs:documentation>
							</xs:annotation>
						</xs:element>
					</xs:sequence>
					<xs:attribute name="id" type="xs:string">
						<xs:annotation>
							<xs:documentation>
                The attribute gml:id supports provision of a handle for the XML element
                representing a GML Object. Its use is optional for all GML objects.
              </xs:documentation>
						</xs:annotation>
					</xs:attribute>
					<xs:attribute name="count" type="xs:unsignedInt">
						<xs:annotation>
							<xs:documentation>
                The number of direct positions in the list
              </xs:documentation>
						</xs:annotation>
					</xs:attribute>
					<xs:attribute name="srsDimension" type="xs:unsignedShort" default="2">
						<xs:annotation>
							<xs:documentation>
                Positive integer
              </xs:documentation>
						</xs:annotation>
					</xs:attribute>
					<xs:attribute name="srsName" type="xs:string">
						<xs:annotation>
							<xs:documentation>
                Any URI
              </xs:documentation>
						</xs:annotation>
					</xs:attribute>
				</xs:complexType>
			</xs:element>
			<xs:element name="Circle" type="S100_CircleByCenterPointType" minOccurs="0"/>
		</xs:sequence>
	</xs:complexType>
</xs:schema>
'''

RE_XML_ENCODING = re.compile("encoding=\"UTF-8\"", re.IGNORECASE)
schema = StringIO(RE_XML_ENCODING.sub("", schema_str, count=1))
schematxt_doc = etree.parse(schema)
xmlschema = etree.XMLSchema(schematxt_doc)

