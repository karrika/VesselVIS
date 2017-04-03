# coding: utf-8
from io import StringIO
from lxml import etree
import re

schema_str = '''<?xml version="1.0" encoding="utf-8"?>
<!--
  
  STM Extension RouteInfo for Route Exchange Format (RTZ)

  XML schema

  Revision 1.0.0

  Source: STM Developer Forum
-->
<xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns="http://www.cirm.org/RTZ/1/1" targetNamespace="http://www.cirm.org/RTZ/1/1" elementFormDefault="unqualified">
  <!--                                         -->
  <!-- STM routeInfo extension type definition -->
  <!--                                         -->
  <xsd:complexType name="RouteInfoExtensionSTM">
    <xsd:sequence>
      <xsd:element name="routeChanges" type="RouteChanges"
        minOccurs="0" maxOccurs="1">
        <xsd:annotation>
          <xsd:documentation>Route changes history.</xsd:documentation>
        </xsd:annotation>
      </xsd:element>
    </xsd:sequence>
    <xsd:attribute name="manufacturer" type="xsd:string"
      use="required" fixed="STM">
      <xsd:annotation>
        <xsd:documentation>Manufacturer of the extension.</xsd:documentation>
      </xsd:annotation>
    </xsd:attribute>
    <xsd:attribute name="name" type="xsd:string"
      use="required" fixed="routeInfoEx">
      <xsd:annotation>
        <xsd:documentation>Manufacturer of the extension.</xsd:documentation>
      </xsd:annotation>
    </xsd:attribute>
    <xsd:attribute name="version" type="xsd:string" fixed="1.0.0">
      <xsd:annotation>
        <xsd:documentation>Version of the extension.</xsd:documentation>
      </xsd:annotation>
    </xsd:attribute>
    <xsd:attribute name="routeStatusEnum" type="RouteStatusType">
      <xsd:annotation>
        <xsd:documentation>Route status number.</xsd:documentation>
      </xsd:annotation>
    </xsd:attribute>
    <xsd:attribute name="routeVersion" type="xsd:string">
      <xsd:annotation>
        <xsd:documentation>Version of the route.</xsd:documentation>
      </xsd:annotation>
    </xsd:attribute>
    <xsd:attribute name="personsOnBoard" type="xsd:nonNegativeInteger">
      <xsd:annotation>
        <xsd:documentation>
          Ship’s passengers including crew.
        </xsd:documentation>
      </xsd:annotation>
    </xsd:attribute>
    <xsd:attribute name="depPort" type="UNLOCODE">
      <xsd:annotation>
        <xsd:documentation>Departure port.</xsd:documentation>
      </xsd:annotation>
    </xsd:attribute>
    <xsd:attribute name="arrPort" type="UNLOCODE">
      <xsd:annotation>
        <xsd:documentation>Arrival port.</xsd:documentation>
      </xsd:annotation>
    </xsd:attribute>
    <xsd:attribute name="depPortCallId" type="PortCallIdentifier">
      <xsd:annotation>
        <xsd:documentation>
          Port call identifier for departure port.
        </xsd:documentation>
      </xsd:annotation>
    </xsd:attribute>
    <xsd:attribute name="arrPortCallId" type="PortCallIdentifier">
      <xsd:annotation>
        <xsd:documentation>
          Port call identifier for arrival port.
        </xsd:documentation>
      </xsd:annotation>
    </xsd:attribute>
    <xsd:attribute name="startSeaPassage" type="xsd:string">
      <xsd:annotation>
        <xsd:documentation>
          WP and its type, where sea passage starts.
        </xsd:documentation>
      </xsd:annotation>
    </xsd:attribute>
    <xsd:attribute name="endSeaPassage" type="xsd:string">
      <xsd:annotation>
        <xsd:documentation>
          WP and its type, where sea passage ends.
        </xsd:documentation>
      </xsd:annotation>
    </xsd:attribute>
  </xsd:complexType>
  <!--                              -->
  <!--"RouteStatus" type definition -->
  <!--                              -->
  <xsd:simpleType name="RouteStatusType">
    <xsd:annotation>
      <xsd:documentation>Route status value.</xsd:documentation>
    </xsd:annotation>
    <xsd:restriction base="xsd:integer">
      <xsd:minInclusive value="1"/>
    </xsd:restriction>
  </xsd:simpleType>
  <!--                                    -->
  <!-- RouteChangeHistory type definition -->
  <!--                                    -->
  <xsd:complexType name="RouteChanges">
    <xsd:annotation>
      <xsd:documentation>
        Data for route changes history.
      </xsd:documentation>
    </xsd:annotation>
    <xsd:sequence>
      <xsd:element name="historyItem" type="HistoryItem"
        minOccurs="0" maxOccurs="unbounded">
        <xsd:annotation>
          <xsd:documentation>History item details.</xsd:documentation>
        </xsd:annotation>
      </xsd:element>
    </xsd:sequence>
  </xsd:complexType>
  <!--                             -->
  <!-- HistoryItem type definition -->
  <!--                             -->
  <xsd:complexType name="HistoryItem">
    <xsd:annotation>
      <xsd:documentation>
        Route change history item.
      </xsd:documentation>
    </xsd:annotation>
    <xsd:attribute name="dateTime" type="DateTimeUTC" use="required">
      <xsd:annotation>
        <xsd:documentation>Date and time of change.</xsd:documentation>
      </xsd:annotation>
    </xsd:attribute>
    <xsd:attribute name="author" type="NonEmptyString" use="required">
      <xsd:annotation>
        <xsd:documentation>Author of change.</xsd:documentation>
      </xsd:annotation>
    </xsd:attribute>
    <xsd:attribute name="reason" type="NonEmptyString" use="required">
      <xsd:annotation>
        <xsd:documentation>Reason of change.</xsd:documentation>
      </xsd:annotation>
    </xsd:attribute>
  </xsd:complexType>
  <!--                                    -->
  <!-- PortCallIdentifier type definition -->
  <!--                                    -->
  <xsd:simpleType name="PortCallIdentifier">
    <xsd:annotation>
      <xsd:documentation>
        Port call identifier, based on MRN.
        First element of the NSS should be the UN/Locode of the port.
      </xsd:documentation>
    </xsd:annotation>
    <xsd:restriction base="xsd:string">
      <xsd:maxLength value="120"/>
      <xsd:pattern value=
        "urn:mrn:stm:portcdm:port_call:[A-Za-z]{5}:[A-Za-z0-9()+,\-.:=@;$_!*'%/?#]+"
      />
    </xsd:restriction>
  </xsd:simpleType>
  <!--                          -->
  <!-- UNLOCODE type definition -->
  <!--                          -->
  <xsd:simpleType name="UNLOCODE">
    <xsd:annotation>
      <xsd:documentation>UNLocode</xsd:documentation>
    </xsd:annotation>
    <xsd:restriction base="xsd:string">
      <xsd:maxLength value="5"/>
      <xsd:pattern value="[A-Za-z]{5}"/>
    </xsd:restriction>
  </xsd:simpleType>
  <!--                                               -->
  <!-- STM scheduleElement extension type definition -->
  <!--                                               -->
  <xsd:complexType name="ScheduleElementExtensionSTM">
    <xsd:attribute name="manufacturer" type="NonEmptyString"
      use="required" fixed="STM">
      <xsd:annotation>
        <xsd:documentation>Unique vendor identifier.</xsd:documentation>
      </xsd:annotation>
    </xsd:attribute>
    <xsd:attribute name="name" type="NonEmptyString"
      use="required" fixed="ScheduleElementEx">
      <xsd:annotation>
        <xsd:documentation>Extension name.</xsd:documentation>
      </xsd:annotation>
    </xsd:attribute>
    <xsd:attribute name="version" type="NonEmptyString" fixed="1.0.0">
      <xsd:annotation>
        <xsd:documentation>Extension version.</xsd:documentation>
      </xsd:annotation>
    </xsd:attribute>
    <xsd:attribute name="waveHeight">
      <xsd:annotation>
        <xsd:documentation>Height of waves in metres.</xsd:documentation>
      </xsd:annotation>
      <xsd:simpleType>
        <xsd:restriction base="xsd:decimal">
          <xsd:minInclusive value="0.0"/>
        </xsd:restriction>
      </xsd:simpleType>
    </xsd:attribute>
    <xsd:attribute name="waveDirection">
      <xsd:annotation>
        <xsd:documentation>Wave direction in degrees.</xsd:documentation>
      </xsd:annotation>
      <xsd:simpleType>
        <xsd:restriction base="xsd:decimal">
          <xsd:minInclusive value="0.0"/>
          <xsd:maxExclusive value="360.0"/>
        </xsd:restriction>
      </xsd:simpleType>
    </xsd:attribute>
  </xsd:complexType>
  <!--                                -->
  <!-- NonEmptyString type definition -->
  <!--                                -->
  <xsd:simpleType name="NonEmptyString">
    <xsd:annotation>
      <xsd:documentation>Non-empty string.</xsd:documentation>
    </xsd:annotation>
    <xsd:restriction base="xsd:string">
      <xsd:minLength value="1"/>
      <xsd:pattern value=".*[0-9a-zA-Z].*"/>
    </xsd:restriction>
  </xsd:simpleType>
  <!--                                     -->
  <!-- DateTimeUTC element type definition -->
  <!--                                     -->
  <xsd:simpleType name="DateTimeUTC">
    <xsd:annotation>
      <xsd:documentation>Length type.</xsd:documentation>
    </xsd:annotation>
    <xsd:restriction base="xsd:dateTime">
      <xsd:pattern value=".*Z"/>
    </xsd:restriction>
  </xsd:simpleType>
</xsd:schema>
'''

RE_XML_ENCODING = re.compile("encoding=\"UTF-8\"", re.IGNORECASE)
schema = StringIO(RE_XML_ENCODING.sub("", schema_str, count=1))
schema11_doc = etree.parse(schema)
xmlschema = etree.XMLSchema(schema11_doc)


