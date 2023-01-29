"""journeys.py."""
from typing import List

from pytxc.base import BaseTxCElement
from pytxc.links import From, To


class JourneyPatternTimingLink(BaseTxCElement):
    """Class representing a JourneyPatternTimingLink."""

    from_: From
    to: To
    route_link_ref: str
    run_time: str

    class Config:
        fields = {"from_": "from"}


class JourneyPatternSection(BaseTxCElement):
    """Class representing a JourneyPatternSection."""

    journey_pattern_timing_link: List[JourneyPatternTimingLink]


class JourneyPattern(BaseTxCElement):
    """Class representing a JourneyPattern."""

    destination_display: str
    direction: str
    operator_ref: str
    route_ref: str
    journey_pattern_section_refs: str
