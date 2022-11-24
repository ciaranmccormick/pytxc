"""stops.py."""
from pytxc.elements import BaseElement


class AnnotatedStopPointRef(BaseElement):
    """A class representing an AnnotatedStopPointRef."""

    common_name: str
    stop_point_ref: str
