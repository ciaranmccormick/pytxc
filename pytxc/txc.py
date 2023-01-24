"""txc.py."""
from typing import List

from pytxc.elements import BaseElement
from pytxc.journeys.patterns import JourneyPatternSection
from pytxc.journeys.vehicles import VehicleJourney
from pytxc.operators import Operator
from pytxc.routes import Route, RouteSection
from pytxc.services import Service
from pytxc.stops import AnnotatedStopPointRef


class TransXChange(BaseElement):
    """A class representing a TransXChange document."""

    stop_points: List[AnnotatedStopPointRef] = []
    route_sections: List[RouteSection] = []
    routes: List[Route] = []
    journey_pattern_sections: List[JourneyPatternSection] = []
    operators: List[Operator] = []
    services: List[Service] = []
    vehicle_journeys: List[VehicleJourney] = []
