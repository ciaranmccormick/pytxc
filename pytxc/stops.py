"""stops.py."""
from typing import Optional

from pytxc.elements import BaseElement


class AnnotatedStopPointRef(BaseElement):
    """A class representing an AnnotatedStopPointRef."""

    common_name: Optional[str] = None
    stop_point_ref: str
