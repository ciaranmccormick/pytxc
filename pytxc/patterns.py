from typing import Iterable, Optional

from pydantic import BaseModel
from .txc import Element


class TimingLink(BaseModel):
    activity: Optional[str]
    sequence_number: int
    stop_point_ref: str
    timing_status: Optional[str]

    @classmethod
    def from_element(cls, element: Element):
        return cls(
            activity=element.find_text("./txc:Activity"),
            sequence_number=element.attrib.get("SequenceNumber"),
            stop_point_ref=element.find_text("./txc:StopPointRef"),
            timing_status=element.find_text("./txc:TimingStatus"),
        )


class JourneyPatternTimingLink(BaseModel):
    from_: TimingLink
    id: str
    route_link_ref: str
    run_time: str
    to: TimingLink

    @classmethod
    def from_element(cls, element: Element):
        id_ = element.attrib.get("id")
        run_time = element.find_text("./txc:RunTime")
        route_link_ref = element.find_text("./txc:RouteLinkRef")

        from_ = element.find("./txc:From")
        if from_ is not None:
            from_ = TimingLink.from_element(from_)

        to = element.find("./txc:To")
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
    def from_element(cls, element: Element):
        id_ = element.attrib.get("id")
        timing_links = (
            JourneyPatternTimingLink.from_element(el)
            for el in element.iter_find("./txc:JourneyPatternTimingLink")
        )
        return cls(id=id_, timing_links=timing_links)
