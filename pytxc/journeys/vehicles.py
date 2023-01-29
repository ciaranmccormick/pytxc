"""vehicles.py"""
from datetime import time
from typing import List, Optional

from pytxc.base import BaseTxCElement


class VehicleJourneyTimingLink(BaseTxCElement):
    """A class representing a TransXChange VehicleJourneyTimingLink."""

    journey_pattern_timing_link_ref: str
    run_time: str


class VehicleJourney(BaseTxCElement):
    """A class representing a VehicleJourney node."""

    departure_time: time
    direction: Optional[str]
    private_code: Optional[str]
    vehicle_journey_code: str
    vehicle_journey_timing_link: Optional[List[VehicleJourneyTimingLink]]
    service_ref: str
    line_ref: str
    journey_pattern_ref: str
    operator_ref: str
