"""locations.py."""
from typing import List

from pytxc.elements import BaseElement


class Location(BaseElement):
    """A class representing a TransXChange Location."""

    longitude: float
    latitude: float

    def to_list(self) -> List[float]:
        """Return a location as a list of floats [long, lat]."""
        return [self.longitude, self.latitude]
