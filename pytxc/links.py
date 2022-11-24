"""links.py"""
from typing import Optional

from pytxc.elements import BaseElement


class Link(BaseElement):
    """A class representing a TransXChange Link node."""

    stop_point_ref: str
    activity: Optional[str]
    dynamic_destination_display: Optional[str]
    timing_status: Optional[str]
    fare_stage_number: Optional[int]


class From(Link):
    """A class representing a From element."""


class To(Link):
    """A class representing a To element."""
