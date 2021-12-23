from datetime import date
from typing import Iterable, Optional

from lxml.etree import _Element
from pydantic import BaseModel

from .constants import NAMESPACES


class OperatingPeriod(BaseModel):
    end_date: date
    start_date: date

    @classmethod
    def from_element(cls, element: _Element):
        return cls(
            end_date=element.findtext("./txc:EndDate", namespaces=NAMESPACES),
            start_date=element.findtext("./txc:StartDate", namespaces=NAMESPACES),
        )


class Line(BaseModel):
    id: str
    inbound_description: str
    line_name: str
    outbound_description: str

    @classmethod
    def from_element(cls, element: _Element):
        id_ = element.attrib.get("id")
        line_name = element.findtext("./txc:LineName", namespaces=NAMESPACES)
        outbound_description = element.findtext(
            "./txc:OutboundDescription/txc:Description", namespaces=NAMESPACES
        )
        inbound_description = element.findtext(
            "./txc:InboundDescription/txc:Description", namespaces=NAMESPACES
        )
        return cls(
            id=id_,
            inbound_description=inbound_description,
            line_name=line_name,
            outbound_description=outbound_description,
        )


class JourneyPattern(BaseModel):
    destination_display: Optional[str]
    direction: str
    id: str
    journey_pattern_section_refs: str
    operator_ref: str
    route_ref: str

    @classmethod
    def from_element(cls, element: _Element):
        journey_pattern_section_refs = element.findtext(
            "./txc:JourneyPatternSectionRefs", namespaces=NAMESPACES
        )
        destination_display = element.findtext(
            "./txc:DestinationDisplay", namespaces=NAMESPACES
        )
        return cls(
            destination_display=destination_display,
            direction=element.findtext("./txc:Direction", namespaces=NAMESPACES),
            id=element.attrib.get("id"),
            journey_pattern_section_refs=journey_pattern_section_refs,
            operator_ref=element.findtext("./txc:OperatorRef", namespaces=NAMESPACES),
            route_ref=element.findtext("./txc:RouteRef", namespaces=NAMESPACES),
        )


class StandardService(BaseModel):
    destination: str
    journey_patterns: Iterable[JourneyPattern]
    origin: str

    @classmethod
    def from_element(cls, element: _Element):
        journey_patterns = (
            JourneyPattern.from_element(el)
            for el in element.iterfind("./txc:JourneyPattern", namespaces=NAMESPACES)  # type: ignore
        )
        return cls(
            destination=element.findtext("./txc:Destination", namespaces=NAMESPACES),
            journey_patterns=journey_patterns,
            origin=element.findtext("./txc:Origin", namespaces=NAMESPACES),
        )


class Service(BaseModel):
    lines: Iterable[Line]
    operating_period: OperatingPeriod
    public_use: bool = True
    service_code: str
    standard_service: Optional[StandardService]

    @classmethod
    def from_element(cls, element: _Element):
        service_code = element.findtext("./txc:ServiceCode", namespaces=NAMESPACES)
        operating_period = element.find("./txc:OperatingPeriod", namespaces=NAMESPACES)
        if operating_period is not None:
            operating_period = OperatingPeriod.from_element(operating_period)

        standard_service = element.find("./txc:StandardService", namespaces=NAMESPACES)
        if standard_service is not None:
            standard_service = StandardService.from_element(standard_service)
        lines = (
            Line.from_element(el)
            for el in element.iterfind("./txc:Lines/txc:Line", namespaces=NAMESPACES)  # type: ignore
        )
        public_use = element.findtext("./txc:PublicUse", namespaces=NAMESPACES)
        return cls(
            lines=lines,
            operating_period=operating_period,
            public_use=public_use,
            service_code=service_code,
            standard_service=standard_service,
        )
