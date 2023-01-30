"""services.py."""
from datetime import date
from typing import List, Optional

from pytxc.base import BaseTxCElement
from pytxc.journeys.patterns import JourneyPattern


class OutboundDescription(BaseTxCElement):
    """A class representing an OutboundDescription node."""

    origin: Optional[str]
    destination: Optional[str]
    description: str


class InboundDescription(BaseTxCElement):
    """A class representing an OutboundDescription node."""

    origin: Optional[str]
    destination: Optional[str]
    description: str


class OperatingPeriod(BaseTxCElement):
    """A class representing an OperatingPeriod."""

    start_date: date
    end_date: Optional[date]


class Line(BaseTxCElement):
    """A class representing a TransXChange Line."""

    line_name: str
    outbound_description: Optional[OutboundDescription]
    inbound_description: Optional[InboundDescription]


class StandardService(BaseTxCElement):
    """A class representing a StandardService."""

    origin: str
    destination: str
    use_all_stop_points: Optional[bool]
    journey_pattern: List[JourneyPattern] = []
    vias: List[str] = []


class Service(BaseTxCElement):
    """A class representing a Service."""

    service_code: str
    lines: List[Line]
    operating_period: OperatingPeriod
    ticket_machine_service_code: Optional[str]
    registered_operator_ref: str
    public_use: bool
    standard_service: StandardService
