# coding: utf-8
from io import StringIO
from lxml import etree

schema = StringIO('''<?xml version="1.0"?>
<!--
  
  Route Exchange Format (RTZ)

  XML schema

  Revision 1.0

  Source: IEC 61174 Ed 4.0:2015
-->

<xsd:schema
  xmlns:xsd="http://www.w3.org/2001/XMLSchema"
  xmlns="http://www.cirm.org/RTZ/1/0"
  targetNamespace="http://www.cirm.org/RTZ/1/0"
  elementFormDefault="qualified">

  <xsd:annotation>
    <xsd:documentation>
      RTZ schema version 1.1. For more information on RTZ and this schema,
      visit http://www.cirm.org/RTZ.

      RTZ uses the following conventions: all coordinates are relative to the WGS84
      datum.

      All measurements are in nautical miles unless otherwise specified.
    </xsd:documentation>
  </xsd:annotation>

  <!--              -->
  <!-- Root element -->
  <!--              -->
  <xsd:element name="route" type="Route">
    <xsd:annotation>
      <xsd:documentation>
        Route is the root element in the XML RTZ file.
      </xsd:documentation>
    </xsd:annotation>
  </xsd:element>

  <!--                              -->
  <!-- Root element type definition -->
  <!--                              -->
  <xsd:complexType name="Route">
    <xsd:annotation>
      <xsd:documentation>
        RTZ files contain a number of waypoints, followed with auxiliary schedules.
        You can add your own elements to the extension section of the RTZ document.
      </xsd:documentation>
    </xsd:annotation>
    <xsd:sequence>
      <xsd:element name="routeInfo" type="RouteInfo" minOccurs="1" maxOccurs="1">
        <xsd:annotation>
          <xsd:documentation>
            Generic route information.
          </xsd:documentation>
        </xsd:annotation>
      </xsd:element>
      <xsd:element name="waypoints" type="Waypoints" minOccurs="1" maxOccurs="1">
        <xsd:annotation>
          <xsd:documentation>
            A list of waypoints.
          </xsd:documentation>
        </xsd:annotation>
      </xsd:element>
      <xsd:element name="schedules" type="Schedules" minOccurs="0" maxOccurs="1">
        <xsd:annotation>
          <xsd:documentation>
            Optional list of schedules.
          </xsd:documentation>
        </xsd:annotation>
      </xsd:element>
      <xsd:element name="extensions" type="Extensions" minOccurs="0" maxOccurs="1">
        <xsd:annotation>
          <xsd:documentation>
            You can add extend RTZ by adding your own elements from another schema
            here.
          </xsd:documentation>
        </xsd:annotation>
      </xsd:element>
    </xsd:sequence>
    <xsd:attribute name="version" type="xsd:string" use="required" fixed="1.0">
      <xsd:annotation>
        <xsd:documentation>
          Format version (currently "1.0").
        </xsd:documentation>
      </xsd:annotation>
    </xsd:attribute>
  </xsd:complexType>

  <!--                                      -->
  <!-- "RouteInfo" element type definition  -->
  <!--                                      -->
  <xsd:complexType name="RouteInfo">
    <xsd:sequence>
      <xsd:element name="extensions" type="Extensions" minOccurs="0" maxOccurs="1">
        <xsd:annotation>
          <xsd:documentation>
            You can add extend RTZ by adding your own elements from another schema
            here.
          </xsd:documentation>
        </xsd:annotation>
      </xsd:element>
    </xsd:sequence>
    <xsd:attribute name="routeName" type="xsd:string" use="required">
      <xsd:annotation>
        <xsd:documentation>The name of the route.</xsd:documentation>
      </xsd:annotation>
    </xsd:attribute>
    <xsd:attribute name="routeAuthor" type="xsd:string">
      <xsd:annotation>
        <xsd:documentation>The author of route.</xsd:documentation>
      </xsd:annotation>
    </xsd:attribute>
    <xsd:attribute name="routeStatus" type="xsd:string">
      <xsd:annotation>
        <xsd:documentation>Status of route.</xsd:documentation>
      </xsd:annotation>
    </xsd:attribute>
    <xsd:attribute name="validityPeriodStart" type="xsd:dateTime">
      <xsd:annotation>
        <xsd:documentation>
          Start of validity period in ISO 8601 format.
        </xsd:documentation>
      </xsd:annotation>
    </xsd:attribute>
    <xsd:attribute name="validityPeriodStop" type="xsd:dateTime">
      <xsd:annotation>
        <xsd:documentation>
          Stop of validity period in ISO 8601 format.
        </xsd:documentation>
      </xsd:annotation>
    </xsd:attribute>
    <xsd:attribute name="vesselName" type="xsd:string">
      <xsd:annotation>
        <xsd:documentation>The name of ship.</xsd:documentation>
      </xsd:annotation>
    </xsd:attribute>
    <xsd:attribute name="vesselMMSI" type="xsd:nonNegativeInteger">
      <xsd:annotation>
        <xsd:documentation>MMSI of ship.</xsd:documentation>
      </xsd:annotation>
    </xsd:attribute>
    <xsd:attribute name="vesselIMO" type="xsd:nonNegativeInteger">
      <xsd:annotation>
        <xsd:documentation>IMO number of ship.</xsd:documentation>
      </xsd:annotation>
    </xsd:attribute>
    <xsd:attribute name="vesselVoyage" type="xsd:string">
      <xsd:annotation>
        <xsd:documentation>Number of the voyage.</xsd:documentation>
      </xsd:annotation>
    </xsd:attribute>
    <xsd:attribute name="vesselDisplacement" type="xsd:nonNegativeInteger">
      <xsd:annotation>
        <xsd:documentation>Displacement of ship in tons.</xsd:documentation>
      </xsd:annotation>
    </xsd:attribute>
    <xsd:attribute name="vesselCargo" type="xsd:nonNegativeInteger">
      <xsd:annotation>
        <xsd:documentation>Cargo of ship in tons.</xsd:documentation>
      </xsd:annotation>
    </xsd:attribute>
    <xsd:attribute name="vesselGM" type="LengthType">
      <xsd:annotation>
        <xsd:documentation>Metacentric height in metres.</xsd:documentation>
      </xsd:annotation>
    </xsd:attribute>
    <xsd:attribute name="optimizationMethod" type="xsd:string">
      <xsd:annotation>
        <xsd:documentation>Route is optimized to meet KPI.</xsd:documentation>
      </xsd:annotation>
    </xsd:attribute>
    <xsd:attribute name="vesselMaxRoll" type="xsd:nonNegativeInteger">
      <xsd:annotation>
        <xsd:documentation>
          Max roll angle of ship allowed in degrees.
        </xsd:documentation>
      </xsd:annotation>
    </xsd:attribute>
    <xsd:attribute name="vesselMaxWave" type="LengthType">
      <xsd:annotation>
        <xsd:documentation>
          Ship significant wave height limit in metres.
        </xsd:documentation>
      </xsd:annotation>
    </xsd:attribute>
    <xsd:attribute name="vesselMaxWind" type="xsd:decimal">
      <xsd:annotation>
        <xsd:documentation>
          Max wind speed limit of ship in metres per second.
        </xsd:documentation>
      </xsd:annotation>
    </xsd:attribute>
    <xsd:attribute name="vesselSpeedMax" type="SpeedType">
      <xsd:annotation>
        <xsd:documentation>Max speed of ship in knots.</xsd:documentation>
      </xsd:annotation>
    </xsd:attribute>
    <xsd:attribute name="vesselServiceMin" type="SpeedType">
      <xsd:annotation>
        <xsd:documentation>
          Preferred service speed window minimum in knots.
        </xsd:documentation>
      </xsd:annotation>
    </xsd:attribute>
    <xsd:attribute name="vesselServiceMax" type="SpeedType">
      <xsd:annotation>
        <xsd:documentation>
          Preferred service speed window maximum in knots.
        </xsd:documentation>
      </xsd:annotation>
    </xsd:attribute>
    <xsd:attribute name="routeChangesHistory" type="SpeedType">
      <xsd:annotation>
        <xsd:documentation>
          Cause of route change, originator and reason.
        </xsd:documentation>
      </xsd:annotation>
    </xsd:attribute>
  </xsd:complexType>
  
  <!--                                      -->
  <!-- "LengthType" element type definition -->
  <!--                                      -->
  <xsd:simpleType name="LengthType">
    <xsd:annotation>
      <xsd:documentation>Length type.</xsd:documentation>
    </xsd:annotation>
    <xsd:restriction base="xsd:decimal">
      <xsd:minInclusive value="0.0"/>
    </xsd:restriction>
  </xsd:simpleType>

  <!--                                     -->
  <!-- "SpeedType" element type definition -->
  <!--                                     -->
  <xsd:simpleType name="SpeedType">
    <xsd:annotation>
      <xsd:documentation>Speed type.</xsd:documentation>
    </xsd:annotation>
    <xsd:restriction base="xsd:decimal">
      <xsd:minInclusive value="0.0"/>
    </xsd:restriction>
  </xsd:simpleType>
  
  <!--                                 -->
  <!-- Extension point type definition -->
  <!--                                 -->
  <xsd:complexType name="Extensions">
    <xsd:annotation>
      <xsd:documentation>
        You can add extend GPX by adding your own elements from another schema here.
      </xsd:documentation>
    </xsd:annotation>
    <xsd:sequence>
      <xsd:any namespace="##any" processContents="skip"
               minOccurs="0" maxOccurs="unbounded">
        <xsd:annotation>
          <xsd:documentation>
            You can add extend GPX by adding your own elements from another schema
            here.
          </xsd:documentation>
        </xsd:annotation>
      </xsd:any>
    </xsd:sequence>
  </xsd:complexType>

  <!--                                      -->
  <!-- "Waypoints" element type definition  -->
  <!--                                      -->
  <xsd:complexType name="Waypoints">
    <xsd:sequence>
      <xsd:element name="defaultWaypoint" type="DefaultWaypoint" minOccurs="0"
        maxOccurs="1">
        <xsd:annotation>
          <xsd:documentation>Waypoint defaults.</xsd:documentation>
        </xsd:annotation>
      </xsd:element>
      <xsd:element name="waypoint" type="Waypoint" minOccurs="2" maxOccurs="unbounded">
        <xsd:annotation>
          <xsd:documentation>Waypoint details.</xsd:documentation>
        </xsd:annotation>
      </xsd:element>
      <xsd:element name="extensions"  type="Extensions" minOccurs="0" maxOccurs="1">
        <xsd:annotation>
          <xsd:documentation>
            You can add extend RTZ by adding your own elements from another schema
            here.
          </xsd:documentation>
        </xsd:annotation>
      </xsd:element>
    </xsd:sequence>
  </xsd:complexType>

  <!--                                           -->
  <!-- "DefaultWaypoint" element type definition -->
  <!--                                           -->
  <xsd:complexType name="DefaultWaypoint">
    <xsd:sequence>
      <xsd:element name="leg" type="Leg" minOccurs="0" maxOccurs="1">
        <xsd:annotation>
          <xsd:documentation>Leg attributes.</xsd:documentation>
        </xsd:annotation>
      </xsd:element>
      <xsd:element name="extensions" type="Extensions" minOccurs="0" maxOccurs="1">
        <xsd:annotation>
          <xsd:documentation>
            You can add extend RTZ by adding your own elements from another schema
            here.
          </xsd:documentation>
        </xsd:annotation>
      </xsd:element>
    </xsd:sequence>
    <xsd:attribute name="radius" type="RadiusType">
      <xsd:annotation>
        <xsd:documentation>Turn radius in NM.</xsd:documentation>
      </xsd:annotation>
    </xsd:attribute>
  </xsd:complexType>

  <!--                                      -->
  <!-- "RadiusType" element type definition -->
  <!--                                      -->
  <xsd:simpleType name="RadiusType">
    <xsd:annotation>
      <xsd:documentation>Radius type.</xsd:documentation>
    </xsd:annotation>
    <xsd:restriction base="xsd:decimal">
      <xsd:minInclusive value="0.0"/>
      <xsd:maxExclusive value="10.0"/>
    </xsd:restriction>
  </xsd:simpleType>

  <!--                                    -->
  <!-- "Waypoint" element type definition -->
  <!--                                    -->
  <xsd:complexType name="Waypoint">
    <xsd:sequence>
      <xsd:element name="position" type="GM_Point" minOccurs="1" maxOccurs="1">
        <xsd:annotation>
          <xsd:documentation>Geographic point.</xsd:documentation>
        </xsd:annotation>
      </xsd:element>
      <xsd:element name="leg" type="Leg" minOccurs="0" maxOccurs="1">
        <xsd:annotation>
          <xsd:documentation>Leg attributes.</xsd:documentation>
        </xsd:annotation>
      </xsd:element>
      <xsd:element name="extensions"  type="Extensions" minOccurs="0" maxOccurs="1">
        <xsd:annotation>
          <xsd:documentation>
            You can add extend RTZ by adding your own elements from another schema
            here.
          </xsd:documentation>
        </xsd:annotation>
      </xsd:element>
    </xsd:sequence>
    <xsd:attribute name="id" type="xsd:nonNegativeInteger" use="required">
      <xsd:annotation>
        <xsd:documentation>
          Unique waypoint identifier.
        </xsd:documentation>
      </xsd:annotation>
    </xsd:attribute>
    <xsd:attribute name="revision" type="xsd:nonNegativeInteger">
      <xsd:annotation>
        <xsd:documentation>
          Waypoint revision. Increased on every change.
        </xsd:documentation>
      </xsd:annotation>
    </xsd:attribute>
    <xsd:attribute name="name" type="xsd:string">
      <xsd:annotation>
        <xsd:documentation>
          Waypoint name.
        </xsd:documentation>
      </xsd:annotation>
    </xsd:attribute>
    <xsd:attribute name="radius" type="RadiusType">
      <xsd:annotation>
        <xsd:documentation>
          Turn radius in NM.
        </xsd:documentation>
      </xsd:annotation>
    </xsd:attribute>
  </xsd:complexType>

  <!--                               -->
  <!-- "Leg" element type definition -->
  <!--                               -->
  <xsd:complexType name="Leg">
    <xsd:attribute name="starboardXTD" type="XtdType">
      <xsd:annotation>
        <xsd:documentation>Starboard XTD in NM.</xsd:documentation>
      </xsd:annotation>
    </xsd:attribute>
    <xsd:attribute name="portsideXTD" type="XtdType">
      <xsd:annotation>
        <xsd:documentation>Port XTD in NM.</xsd:documentation>
      </xsd:annotation>
    </xsd:attribute>
    <xsd:attribute name="safetyContour" type="LengthType">
      <xsd:annotation>
        <xsd:documentation>Safety contour in metres.</xsd:documentation>
      </xsd:annotation>
    </xsd:attribute>
    <xsd:attribute name="safetyDepth" type="LengthType">
      <xsd:annotation>
        <xsd:documentation>Safety depth in metres.</xsd:documentation>
      </xsd:annotation>
    </xsd:attribute>
    <xsd:attribute name="geometryType" type="GeometryType">
      <xsd:annotation>
        <xsd:documentation>Geometry type of leg.</xsd:documentation>
      </xsd:annotation>
    </xsd:attribute>
    <xsd:attribute name="speedMin" type="SpeedType">
      <xsd:annotation>
        <xsd:documentation>Lowest cruising speed in knots.</xsd:documentation>
      </xsd:annotation>
    </xsd:attribute>
    <xsd:attribute name="speedMax" type="SpeedType">
      <xsd:annotation>
        <xsd:documentation>Highest allowed speed in knots.</xsd:documentation>
      </xsd:annotation>
    </xsd:attribute>
    <xsd:attribute name="draughtForward" type="LengthType">
      <xsd:annotation>
        <xsd:documentation>Static draught forward in metres.</xsd:documentation>
      </xsd:annotation>
    </xsd:attribute>
    <xsd:attribute name="draughtAft" type="LengthType">
      <xsd:annotation>
        <xsd:documentation>Static draught aft in metres.</xsd:documentation>
      </xsd:annotation>
    </xsd:attribute>
    <xsd:attribute name="staticUKC" type="LengthType">
      <xsd:annotation>
        <xsd:documentation>Minimum UKC on the leg.</xsd:documentation>
      </xsd:annotation>
    </xsd:attribute>
    <xsd:attribute name="dynamicUKC" type="LengthType">
      <xsd:annotation>
        <xsd:documentation>Minimum dynamic UKC on the leg.</xsd:documentation>
      </xsd:annotation>
    </xsd:attribute>
    <xsd:attribute name="masthead" type="LengthType">
      <xsd:annotation>
        <xsd:documentation>Height of masthead.</xsd:documentation>
      </xsd:annotation>
    </xsd:attribute>
    <xsd:attribute name="legReport" type="xsd:string">
      <xsd:annotation>
        <xsd:documentation>Reporting information.</xsd:documentation>
      </xsd:annotation>
    </xsd:attribute>
    <xsd:attribute name="legInfo" type="xsd:string">
      <xsd:annotation>
        <xsd:documentation>Nice to know.</xsd:documentation>
      </xsd:annotation>
    </xsd:attribute>
    <xsd:attribute name="legNote1" type="xsd:string">
      <xsd:annotation>
        <xsd:documentation>Notes regarding the ETD/ETA.</xsd:documentation>
      </xsd:annotation>
    </xsd:attribute>
    <xsd:attribute name="legNote2" type="xsd:string">
      <xsd:annotation>
        <xsd:documentation>Local remarks.</xsd:documentation>
      </xsd:annotation>
    </xsd:attribute>
  </xsd:complexType>

  <!--                     -->
  <!-- XTD type definition -->
  <!--                     -->
  <xsd:simpleType name="XtdType">
    <xsd:annotation>
      <xsd:documentation>
        XTD of the point. Nautical miles.
      </xsd:documentation>
    </xsd:annotation>
    <xsd:restriction base="xsd:decimal">
      <xsd:minInclusive value="0.0"/>
      <xsd:maxExclusive value="10.0"/>
    </xsd:restriction>
  </xsd:simpleType>

  <!--                                             -->
  <!-- "geometry/geopoint" element type definition -->
  <!--                                             -->
  <xsd:complexType name="GM_Point">
    <xsd:attribute name="lat" type="LatitudeType" use="required">
      <xsd:annotation>
        <xsd:documentation>Latitude in degrees.</xsd:documentation>
      </xsd:annotation>
    </xsd:attribute>
    <xsd:attribute name="lon" type="LongitudeType" use="required">
      <xsd:annotation>
        <xsd:documentation>Longitude in degrees.</xsd:documentation>
      </xsd:annotation>
    </xsd:attribute>
  </xsd:complexType>

  <!--                                 -->
  <!-- RL/GC indicator type definition -->
  <!--                                 -->
  <xsd:simpleType name="GeometryType">
    <xsd:annotation>
      <xsd:documentation>RL/GC indicator.</xsd:documentation>
    </xsd:annotation>
    <xsd:restriction base="xsd:string">
      <xsd:enumeration value="Loxodrome"/>
      <xsd:enumeration value="Orthodrome"/>
    </xsd:restriction>
  </xsd:simpleType>

  <!--                                       -->
  <!-- Geographical latitude type definition -->
  <!--                                       -->
  <xsd:simpleType name="LatitudeType">
    <xsd:annotation>
      <xsd:documentation>
        The latitude of the point. Decimal degrees, WGS84 datum.
      </xsd:documentation>
    </xsd:annotation>
    <xsd:restriction base="xsd:decimal">
      <xsd:minInclusive value="-90.0"/>
      <xsd:maxInclusive value="90.0"/>
    </xsd:restriction>
  </xsd:simpleType>

  <!--                                        -->
  <!-- Geographical longitude type definition -->
  <!--                                        -->
  <xsd:simpleType name="LongitudeType">
    <xsd:annotation>
      <xsd:documentation>
        The longitude of the point. Decimal degrees, WGS84 datum.
      </xsd:documentation>
    </xsd:annotation>
    <xsd:restriction base="xsd:decimal">
      <xsd:minInclusive value="-180.0"/>
      <xsd:maxExclusive value="180.0"/>
    </xsd:restriction>
  </xsd:simpleType>

  <!--                                     -->
  <!-- "Schedules" element type definition -->
  <!--                                     -->
  <xsd:complexType name="Schedules">
    <xsd:sequence>
      <xsd:element name="schedule" type="Schedule" minOccurs="0" maxOccurs="unbounded">
        <xsd:annotation>
          <xsd:documentation>Schedule definition.</xsd:documentation>
        </xsd:annotation>
      </xsd:element>
      <xsd:element name="extensions"  type="Extensions" minOccurs="0" maxOccurs="1">
        <xsd:annotation>
          <xsd:documentation>
            You can add extend RTZ by adding your own elements from another schema
            here.
          </xsd:documentation>
        </xsd:annotation>
      </xsd:element>
    </xsd:sequence>
  </xsd:complexType>

  <!--                                              -->
  <!-- "schedules/schedule" element type definition -->
  <!--                                              -->
  <xsd:complexType name="Schedule">
    <xsd:annotation>
      <xsd:documentation>
        Schedule definition.
      </xsd:documentation>
    </xsd:annotation>
    <xsd:sequence>
      <xsd:element name="manual" type="Manual" minOccurs="0" maxOccurs="1">
        <xsd:annotation>
          <xsd:documentation>
            Manual schedule values definition.
          </xsd:documentation>
        </xsd:annotation>
      </xsd:element>
      <xsd:element name="calculated" type="Calculated" minOccurs="0" maxOccurs="1">
        <xsd:annotation>
          <xsd:documentation>
            Calculated schedules.
          </xsd:documentation>
        </xsd:annotation>
      </xsd:element>
      <xsd:element name="extensions"  type="Extensions" minOccurs="0" maxOccurs="1">
        <xsd:annotation>
          <xsd:documentation>
            You can add extend RTZ by adding your own elements from another schema
            here.
          </xsd:documentation>
        </xsd:annotation>
      </xsd:element>
    </xsd:sequence>
    <xsd:attribute name="id" type="xsd:nonNegativeInteger" use="required">
      <xsd:annotation>
        <xsd:documentation>
          Schedule name.
        </xsd:documentation>
      </xsd:annotation>
    </xsd:attribute>
    <xsd:attribute name="name" type="xsd:string">
      <xsd:annotation>
        <xsd:documentation>
          Schedule name.
        </xsd:documentation>
      </xsd:annotation>
    </xsd:attribute>
  </xsd:complexType>

  <!--                                  -->
  <!-- "Manual" element type definition -->
  <!--                                  -->
  <xsd:complexType name="Manual">
    <xsd:annotation>
      <xsd:documentation>User defined schedule parameters.</xsd:documentation>
    </xsd:annotation>
    <xsd:sequence>
      <xsd:element name="sheduleElement" type="ScheduleElement"
        minOccurs="1" maxOccurs="unbounded">
        <xsd:annotation>
          <xsd:documentation>
            Manual schedule leg definition.
          </xsd:documentation>
        </xsd:annotation>
      </xsd:element>
      <xsd:element name="extensions" type="Extensions" minOccurs="0" maxOccurs="1">
        <xsd:annotation>
          <xsd:documentation>
            You can add extend RTZ by adding your own elements
            from another schema here.
          </xsd:documentation>
        </xsd:annotation>
      </xsd:element>
    </xsd:sequence>
  </xsd:complexType>

  <!--                                      -->
  <!-- "Calculated" element type definition -->
  <!--                                      -->
  <xsd:complexType name="Calculated">
    <xsd:annotation>
      <xsd:documentation>
        Calculated schedule parameters.
      </xsd:documentation>
    </xsd:annotation>
    <xsd:sequence>
      <xsd:element name="sheduleElement" type="ScheduleElement"
        minOccurs="0" maxOccurs="unbounded">
        <xsd:annotation>
          <xsd:documentation>
            Calculated schedule waypoint parameters.
          </xsd:documentation>
        </xsd:annotation>
      </xsd:element>
      <xsd:element name="extensions" type="Extensions" minOccurs="0" maxOccurs="1">
        <xsd:annotation>
          <xsd:documentation>
            You can add extend RTZ by adding your own elements
            from another schema here.
          </xsd:documentation>
        </xsd:annotation>
      </xsd:element>
    </xsd:sequence>
  </xsd:complexType>

  <!--                                           -->
  <!-- "ScheduleElement" element type definition -->
  <!--                                           -->
  <xsd:complexType name="ScheduleElement">
    <xsd:sequence>
      <xsd:element name="extensions" type="Extensions" minOccurs="0" maxOccurs="1">
        <xsd:annotation>
          <xsd:documentation>
            You can add extend RTZ by adding your own elements from another schema
            here.
          </xsd:documentation>
        </xsd:annotation>
      </xsd:element>
    </xsd:sequence>
    <xsd:attribute name="waypointId" type="xsd:nonNegativeInteger" use="required">
      <xsd:annotation>
        <xsd:documentation>Unique waypoint identifier.</xsd:documentation>
      </xsd:annotation>
    </xsd:attribute>
    <xsd:attribute name="etd" type="xsd:dateTime">
      <xsd:annotation>
        <xsd:documentation>
          UTC estimated departure time in ISO 8601 format.
        </xsd:documentation>
      </xsd:annotation>
    </xsd:attribute>
    <xsd:attribute name="etdWindowBefore" type="xsd:time">
      <xsd:annotation>
        <xsd:documentation>
          Describes the uncertainty of the predicted ETD after optimization.
        </xsd:documentation>
      </xsd:annotation>
    </xsd:attribute>
    <xsd:attribute name="etdWindowAfter" type="xsd:time">
      <xsd:annotation>
        <xsd:documentation>
          Describes the uncertainty of the predicted ETD after optimization.
        </xsd:documentation>
      </xsd:annotation>
    </xsd:attribute>
    <xsd:attribute name="eta" type="xsd:dateTime">
      <xsd:annotation>
        <xsd:documentation>
          UTC estimated arrival time in ISO 8601 format.
        </xsd:documentation>
      </xsd:annotation>
    </xsd:attribute>
    <xsd:attribute name="etaWindowBefore" type="xsd:time">
      <xsd:annotation>
        <xsd:documentation>
          Describes the uncertainty of the predicted ETA after optimization.
        </xsd:documentation>
      </xsd:annotation>
    </xsd:attribute>
    <xsd:attribute name="etaWindowAfter" type="xsd:time">
      <xsd:annotation>
        <xsd:documentation>
          Describes the uncertainty of the predicted ETA after optimization.
        </xsd:documentation>
      </xsd:annotation>
    </xsd:attribute>
    <xsd:attribute name="stay" type="xsd:time">
      <xsd:annotation>
        <xsd:documentation>Stay time on WP.</xsd:documentation>
      </xsd:annotation>
    </xsd:attribute>
    <xsd:attribute name="speed" type="SpeedType">
      <xsd:annotation>
        <xsd:documentation>True speed in knots.</xsd:documentation>
      </xsd:annotation>
    </xsd:attribute>
    <xsd:attribute name="speedWindow" type="xsd:decimal">
      <xsd:annotation>
        <xsd:documentation>
          Describes the uncertainty of the predicted speed after optimization in knots.
        </xsd:documentation>
      </xsd:annotation>
    </xsd:attribute>
    <xsd:attribute name="windSpeed" type="SpeedType">
      <xsd:annotation>
        <xsd:documentation>True wind speed in metres per second.</xsd:documentation>
      </xsd:annotation>
    </xsd:attribute>
    <xsd:attribute name="windDirection" type="CourseType">
      <xsd:annotation>
        <xsd:documentation>True wind direction in degrees.</xsd:documentation>
      </xsd:annotation>
    </xsd:attribute>
    <xsd:attribute name="currentSpeed" type="SpeedType">
      <xsd:annotation>
        <xsd:documentation>Current speed in knots.</xsd:documentation>
      </xsd:annotation>
    </xsd:attribute>
    <xsd:attribute name="currentDirection" type="CourseType">
      <xsd:annotation>
        <xsd:documentation>Current direction in degrees.</xsd:documentation>
      </xsd:annotation>
    </xsd:attribute>
    <xsd:attribute name="windLoss" type="SpeedType">
      <xsd:annotation>
        <xsd:documentation>Speed loss caused by wind in knots.</xsd:documentation>
      </xsd:annotation>
    </xsd:attribute>
    <xsd:attribute name="waveLoss" type="SpeedType">
      <xsd:annotation>
        <xsd:documentation>Speed loss caused by wave.</xsd:documentation>
      </xsd:annotation>
    </xsd:attribute>
    <xsd:attribute name="totalLoss" type="SpeedType">
      <xsd:annotation>
        <xsd:documentation>Total speed loss.</xsd:documentation>
      </xsd:annotation>
    </xsd:attribute>
    <xsd:attribute name="rpm" type="xsd:nonNegativeInteger">
      <xsd:annotation>
        <xsd:documentation>Advised Engine RPM.</xsd:documentation>
      </xsd:annotation>
    </xsd:attribute>
    <xsd:attribute name="pitch" type="xsd:integer">
      <xsd:annotation>
        <xsd:documentation>Advised Engine Pitch.</xsd:documentation>
      </xsd:annotation>
    </xsd:attribute>
    <xsd:attribute name="fuel" type="xsd:decimal">
      <xsd:annotation>
        <xsd:documentation>Predicted fuel consumption on leg.</xsd:documentation>
      </xsd:annotation>
    </xsd:attribute>
    <xsd:attribute name="relFuelSave" type="xsd:decimal">
      <xsd:annotation>
        <xsd:documentation>
          Relative fuel saving after optimization in percent.
        </xsd:documentation>
      </xsd:annotation>
    </xsd:attribute>
    <xsd:attribute name="absFuelSave" type="xsd:decimal">
      <xsd:annotation>
        <xsd:documentation>
          Absolute fuel saving after optimization.
        </xsd:documentation>
      </xsd:annotation>
    </xsd:attribute>
    <xsd:attribute name="Note" type="xsd:string">
    </xsd:attribute>
  </xsd:complexType>

  <!--                        -->
  <!-- Course type definition -->
  <!--                        -->
  <xsd:simpleType name="CourseType">
    <xsd:annotation>
      <xsd:documentation>Course type in degrees.</xsd:documentation>
    </xsd:annotation>
    <xsd:restriction base="xsd:decimal">
      <xsd:minInclusive value="0.0"/>
      <xsd:maxExclusive value="360.0"/>
    </xsd:restriction>
  </xsd:simpleType>

</xsd:schema>
''')

schema10_doc = etree.parse(schema)
xmlschema = etree.XMLSchema(schema10_doc)

