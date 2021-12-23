from typing import List, Optional

from pydantic import BaseModel, Field

from .stops import AnnotatedStopPointRef, FIND_BY_REF
from .common import Location
from .txc import Element

FROM_STOP_REF = "./txc:From/txc:StopPointRef"
TO_STOP_REF = "./txc:To/txc:StopPointRef"
ROUTE_LINK = "./txc:RouteLink"
ROUTE_SECTION_REF = "./txc:RouteSectionRef"
FIND_SECTION_BY_REF = "./txc:RouteSections/txc:RouteSection[@id='{ref}']"


class Track(BaseModel):
    mapping: List[Location]

    @classmethod
    def from_element(cls, element: Element):
        path = "./txc:Mapping/txc:Location"
        locations = [Location.from_element(el) for el in element.find_all(path)]
        return cls(mapping=locations)


class RouteLink(BaseModel):
    id: str
    from_stop: AnnotatedStopPointRef
    to_stop: AnnotatedStopPointRef
    distance: Optional[int]
    track: Optional[Track] = Field(repr=False)

    @classmethod
    def from_element(cls, element: Element):
        txc = element.get_root()

        from_ref = element.find_text(FROM_STOP_REF)
        from_ = txc.find(FIND_BY_REF.format(ref=from_ref))
        if from_ is not None:
            from_ = AnnotatedStopPointRef.from_element(from_)

        to_ref = element.find_text(TO_STOP_REF)
        to = txc.find(FIND_BY_REF.format(ref=to_ref))
        if to is not None:
            to = AnnotatedStopPointRef.from_element(to)

        track = element.find("./txc:Track")
        if track is not None:
            track = Track.from_element(track)

        return cls(
            id=element.attrib.get("id"),
            from_stop=from_,
            to_stop=to,
            distance=element.find_text("./txc:Distance"),
            track=track,
        )


class RouteSection(BaseModel):
    id: str
    route_links: List[RouteLink]

    @classmethod
    def from_element(cls, element: Element):
        links = [RouteLink.from_element(el) for el in element.iter_find(ROUTE_LINK)]
        return cls(id=element.attrib.get("id"), route_links=links)


class Route(BaseModel):
    id: str
    description: str
    route_sections: List[RouteSection]

    @classmethod
    def from_element(cls, element: Element):
        refs = element.iter_find(ROUTE_SECTION_REF)
        route_sections = []
        txc = element.get_root()
        for ref in refs:
            route_section = txc.find(FIND_SECTION_BY_REF.format(ref=ref.text))
            if route_section is not None:
                route_sections.append(RouteSection.from_element(route_section))

        return cls(
            id=element.attrib.get("id"),
            description=element.find_text("./txc:Description"),
            route_sections=route_sections,
        )
