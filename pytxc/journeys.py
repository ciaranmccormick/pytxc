"""journeys.py."""
from typing import List

from pytxc.elements import BaseElement
from pytxc.links import From, To


class JourneyPatternTimingLink(BaseElement):
    """Class representing a JourneyPatternTimingLink."""

    from_: From
    to_: To
    route_link_ref: str
    run_time: str

    class Config:
        fields = {"from_": "from"}


class JourneyPatternSection(BaseElement):
    """Class representing a JourneyPatternSection."""

    journey_pattern_timing_link: List[JourneyPatternTimingLink]


class JourneyPattern(BaseElement):
    """Class representing a JourneyPattern."""

    destination_display: str
    direction: str
    operator_ref: str
    route_ref: str
    journey_pattern_section_refs: str
