"""locations.py."""
from typing import Dict, List, Tuple, Union

from shapely.geometry import LineString, mapping

from pytxc.base import BaseTxCElement

Coordinates = Tuple[Tuple[float]]
GeoValue = Union[str, Coordinates]


class Location(BaseTxCElement):
    """A class representing a TransXChange Location."""

    longitude: float
    latitude: float

    def to_list(self) -> List[float]:
        """Return a location as a list of floats [long, lat]."""
        return [self.longitude, self.latitude]


class Mapping(BaseTxCElement):
    """A class representing a TransXChange Mapping node."""

    location: List[Location]

    def to_geojson(self) -> Dict[str, GeoValue]:
        """Return a geojson feature."""
        return mapping(LineString(self.to_list()))

    def to_list(self) -> List[List[float]]:
        """Return a list of locations represented as a list of floats."""
        return [location.to_list() for location in self.location]


class Track(BaseTxCElement):
    """A class representing a TransXChange Track node."""

    mapping: Mapping
