"""vehicles.py"""
from datetime import time
from typing import List, Optional

from pytxc.elements import BaseElement
from pytxc.journeys.operations import OperatingProfile, Operational


class VehicleJourneyTimingLink(BaseElement):
    """A class representing a TransXChange VehicleJourneyTimingLink."""

    journey_pattern_timing_link_ref: str
    run_time: str


class VehicleJourney(BaseElement):
    """A class representing a VehicleJourney node."""

    departure_time: time
    direction: Optional[str]
    operating_profile: Optional[OperatingProfile]
    operational: Optional[Operational]
    private_code: Optional[str]
    vehicle_journey_code: str
    vehicle_journey_timing_link: Optional[List[VehicleJourneyTimingLink]]
    service_ref: str
    line_ref: str
    journey_pattern_ref: str
    operator_ref: str
