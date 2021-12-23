from datetime import date
from typing import Iterable, Optional

from pydantic import BaseModel

from .txc import Element


class OperatingPeriod(BaseModel):
    end_date: date
    start_date: date

    @classmethod
    def from_element(cls, element: Element):
        return cls(
            end_date=element.find_text("./txc:EndDate"),
            start_date=element.find_text("./txc:StartDate"),
        )


class Line(BaseModel):
    id: str
    inbound_description: str
    line_name: str
    outbound_description: str

    @classmethod
    def from_element(cls, element: Element):
        id_ = element.attrib.get("id")
        line_name = element.find_text("./txc:LineName")
        outbound_description = element.find_text(
            "./txc:OutboundDescription/txc:Description"
        )
        inbound_description = element.find_text(
            "./txc:InboundDescription/txc:Description"
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
    def from_element(cls, element: Element):
        journey_pattern_section_refs = element.find_text(
            "./txc:JourneyPatternSectionRefs"
        )
        destination_display = element.find_text("./txc:DestinationDisplay")
        return cls(
            destination_display=destination_display,
            direction=element.find_text("./txc:Direction"),
            id=element.attrib.get("id"),
            journey_pattern_section_refs=journey_pattern_section_refs,
            operator_ref=element.find_text("./txc:OperatorRef"),
            route_ref=element.find_text("./txc:RouteRef"),
        )


class StandardService(BaseModel):
    destination: str
    journey_patterns: Iterable[JourneyPattern]
    origin: str

    @classmethod
    def from_element(cls, element: Element):
        journey_patterns = (
            JourneyPattern.from_element(el)
            for el in element.iter_find("./txc:JourneyPattern")
        )
        return cls(
            destination=element.find_text("./txc:Destination"),
            journey_patterns=journey_patterns,
            origin=element.find_text("./txc:Origin"),
        )


class Service(BaseModel):
    lines: Iterable[Line]
    operating_period: OperatingPeriod
    public_use: bool = True
    service_code: str
    standard_service: Optional[StandardService]

    @classmethod
    def from_element(cls, element: Element):
        service_code = element.find_text("./txc:ServiceCode")
        operating_period = element.find("./txc:OperatingPeriod")
        if operating_period is not None:
            operating_period = OperatingPeriod.from_element(operating_period)

        standard_service = element.find("./txc:StandardService")
        if standard_service is not None:
            standard_service = StandardService.from_element(standard_service)
        lines = (
            Line.from_element(el) for el in element.iter_find("./txc:Lines/txc:Line")
        )
        public_use = element.find_text("./txc:PublicUse")
        return cls(
            lines=lines,
            operating_period=operating_period,
            public_use=public_use,
            service_code=service_code,
            standard_service=standard_service,
        )
