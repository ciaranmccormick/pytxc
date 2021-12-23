from pathlib import Path
from typing import Iterable, List, TextIO

from lxml import etree
from .journeys import VehicleJourney
from .operators import Operator
from .patterns import JourneyPatternSection
from .routes import Route, RouteSection
from .services import Service
from .stops import AnnotatedStopPointRef
from .txc import Element, TXCAttributes

__all__ = [
    "AnnotatedStopPointRef",
    "JourneyPatternSection",
    "Operator",
    "Route",
    "RouteSection",
    "Service",
    "TransXChange",
    "VehicleJourney",
]


class TransXChange:
    def __init__(self, element: Element):
        self.element = element

    @property
    def attributes(self) -> TXCAttributes:
        return TXCAttributes.from_attrib(self.element.attrib)

    @property
    def iter_stop_points(self) -> Iterable[AnnotatedStopPointRef]:
        path = "./txc:StopPoints/txc:AnnotatedStopPointRef"
        return (
            AnnotatedStopPointRef.from_element(el)
            for el in self.element.iter_find(path)
        )

    @property
    def stops_points(self) -> List[AnnotatedStopPointRef]:
        return list(self.iter_stop_points)

    @property
    def iter_routes(self) -> Iterable[Route]:
        path = "./txc:Routes/txc:Route"
        return (Route.from_element(el) for el in self.element.iter_find(path))

    @property
    def routes(self) -> List[Route]:
        return list(self.iter_routes)

    @property
    def iter_route_sections(self) -> Iterable[RouteSection]:
        path = "./txc:RouteSections/txc:RouteSection"
        return (RouteSection.from_element(el) for el in self.element.iter_find(path))

    @property
    def route_sections(self) -> List[RouteSection]:
        return list(self.iter_route_sections)

    @property
    def iter_operators(self) -> Iterable[Operator]:
        path = "./txc:Operators/txc:Operator"
        return (Operator.from_element(el) for el in self.element.iter_find(path))

    @property
    def operators(self) -> List[Operator]:
        return list(self.iter_operators)

    @property
    def iter_services(self) -> Iterable[Service]:
        path = "./txc:Services/txc:Service"
        return (Service.from_element(el) for el in self.element.iter_find(path))

    @property
    def services(self) -> List[Service]:
        return list(self.iter_services)

    @property
    def iter_journey_pattern_sections(self) -> Iterable[JourneyPatternSection]:
        path = "./txc:JourneyPatternSections/txc:JourneyPatternSection"
        return (
            JourneyPatternSection.from_element(el)
            for el in self.element.iter_find(path)
        )

    @property
    def journey_pattern_sections(self) -> List[JourneyPatternSection]:
        return list(self.iter_journey_pattern_sections)

    @property
    def iter_vehicle_journeys(self) -> Iterable[VehicleJourney]:
        path = "./txc:VehicleJourneys/txc:VehicleJourney"
        return (VehicleJourney.from_element(el) for el in self.element.iter_find(path))

    @property
    def vehicle_journeys(self) -> List[VehicleJourney]:
        return list(self.iter_vehicle_journeys)

    @classmethod
    def from_filepath(cls, path: Path):
        with path.open("r") as f:
            return cls(Element(etree.parse(f).getroot()))

    @classmethod
    def from_filepath_str(cls, path: str):
        return cls.from_filepath(Path(path))

    @classmethod
    def from_file(cls, file: TextIO):
        return cls(Element(etree.parse(file).getroot()))
