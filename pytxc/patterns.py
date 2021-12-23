from typing import Iterable, Optional

from lxml.etree import _Element
from pydantic import BaseModel

from pytxc.constants import NAMESPACES


class TimingLink(BaseModel):
    activity: Optional[str]
    sequence_number: int
    stop_point_ref: str
    timing_status: Optional[str]

    @classmethod
    def from_element(cls, element: _Element):
        return cls(
            activity=element.findtext("./txc:Activity", namespaces=NAMESPACES),
            sequence_number=element.attrib.get("SequenceNumber"),
            stop_point_ref=element.findtext(
                "./txc:StopPointRef", namespaces=NAMESPACES
            ),
            timing_status=element.findtext("./txc:TimingStatus", namespaces=NAMESPACES),
        )


class JourneyPatternTimingLink(BaseModel):
    from_: TimingLink
    id: str
    route_link_ref: str
    run_time: str
    to: TimingLink

    @classmethod
    def from_element(cls, element: _Element):
        id_ = element.attrib.get("id")
        run_time = element.findtext("./txc:RunTime", namespaces=NAMESPACES)
        route_link_ref = element.findtext("./txc:RouteLinkRef", namespaces=NAMESPACES)

        from_ = element.find("./txc:From", namespaces=NAMESPACES)
        if from_ is not None:
            from_ = TimingLink.from_element(from_)

        to = element.find("./txc:To", namespaces=NAMESPACES)
        if to is not None:
            to = TimingLink.from_element(to)

        return cls(
            from_=from_,
            id=id_,
            route_link_ref=route_link_ref,
            run_time=run_time,
            to=to,
        )


class JourneyPatternSection(BaseModel):
    id: str
    timing_links: Iterable[JourneyPatternTimingLink]

    @classmethod
    def from_element(cls, element: _Element):
        id_ = element.attrib.get("id")
        timing_links = (
            JourneyPatternTimingLink.from_element(el)
            for el in element.iterfind(
                "./txc:JourneyPatternTimingLink", namespaces=NAMESPACES  # type: ignore
            )
        )
        return cls(id=id_, timing_links=timing_links)
