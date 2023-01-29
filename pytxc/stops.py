"""stops.py."""
from typing import Optional

from pytxc.base import BaseTxCElement
from pytxc.locations import Location


class AnnotatedStopPointRef(BaseTxCElement):
    """A class representing an AnnotatedStopPointRef."""

    common_name: Optional[str] = None
    stop_point_ref: str
    location: Optional[Location] = None
