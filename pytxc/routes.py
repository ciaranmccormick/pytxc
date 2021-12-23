from typing import List, Optional

from lxml.etree import _Element
from pydantic import BaseModel, Field

from .constants import NAMESPACES
from .stops import AnnotatedStopPointRef, FIND_BY_REF
from .common import Location

FROM_STOP_REF = "./txc:From/txc:StopPointRef"
TO_STOP_REF = "./txc:To/txc:StopPointRef"
ROUTE_LINK = "./txc:RouteLink"
ROUTE_SECTION_REF = "./txc:RouteSectionRef"
FIND_SECTION_BY_REF = "./txc:RouteSections/txc:RouteSection[@id='{ref}']"


class Track(BaseModel):
    mapping: List[Location]

    @classmethod
    def from_element(cls, element: _Element):
        path = "./txc:Mapping/txc:Location"
        locations = [
            Location.from_element(el) for el in element.findall(path, namespaces=NAMESPACES)
        ]
        return cls(mapping=locations)


class RouteLink(BaseModel):
    id: str
    from_stop: AnnotatedStopPointRef
    to_stop: AnnotatedStopPointRef
    distance: Optional[int]
    track: Optional[Track] = Field(repr=False)

    @classmethod
    def from_element(cls, element: _Element):
        txc = element.getroottree().getroot()

        from_ref = element.findtext(FROM_STOP_REF, namespaces=NAMESPACES)
        from_ = txc.find(FIND_BY_REF.format(ref=from_ref), namespaces=NAMESPACES)
        if from_ is not None:
            from_ = AnnotatedStopPointRef.from_element(from_)

        to_ref = element.findtext(TO_STOP_REF, namespaces=NAMESPACES)
        to = txc.find(FIND_BY_REF.format(ref=to_ref), namespaces=NAMESPACES)
        if to is not None:
            to = AnnotatedStopPointRef.from_element(to)

        track = element.find("./txc:Track", namespaces=NAMESPACES)
        if track is not None:
            track = Track.from_element(track)

        return cls(
            id=element.attrib.get("id"),
            from_stop=from_,
            to_stop=to,
            distance=element.findtext("./txc:Distance", namespaces=NAMESPACES),
            track=track,
        )


class RouteSection(BaseModel):
    id: str
    route_links: List[RouteLink]

    @classmethod
    def from_element(cls, element: _Element):
        links = [
            RouteLink.from_element(el)
            for el in element.iterfind(ROUTE_LINK, namespaces=NAMESPACES)  # type: ignore
        ]
        return cls(id=element.attrib.get("id"), route_links=links)


class Route(BaseModel):
    id: str
    description: str
    route_sections: List[RouteSection]

    @classmethod
    def from_element(cls, element: _Element):
        refs = element.iterfind(ROUTE_SECTION_REF, namespaces=NAMESPACES)  # type: ignore
        route_sections = []
        txc = element.getroottree().getroot()
        for ref in refs:
            route_section = txc.find(
                FIND_SECTION_BY_REF.format(ref=ref.text), namespaces=NAMESPACES
            )
            if route_section is not None:
                route_sections.append(RouteSection.from_element(route_section))

        return cls(
            id=element.attrib.get("id"),
            description=element.findtext("./txc:Description", namespaces=NAMESPACES),
            route_sections=route_sections,
        )
