"""routes.py."""
from typing import Dict, List, Tuple, Union

from shapely.geometry import LineString, mapping

from pytxc.elements import BaseElement
from pytxc.links import From, To
from pytxc.locations import Location

Coordinates = Tuple[Tuple[float]]
GeoValue = Union[str, Coordinates]


class Route(BaseElement):
    """A class representing a TransXChange Route."""

    private_code: str
    description: str
    route_section_ref: str


class Mapping(BaseElement):
    """A class representing a TransXChange Mapping node."""

    location: List[Location]

    def to_geojson(self) -> Dict[str, GeoValue]:
        """Return a geojson feature."""
        return mapping(LineString(self.to_list()))

    def to_list(self) -> List[List[float]]:
        """Return a list of locations represented as a list of floats."""
        return [location.to_list() for location in self.location]


class Track(BaseElement):
    """A class representing a TransXChange Track node."""

    mapping: Mapping


class RouteLink(BaseElement):
    """A class representing a TransXChange RouteLink."""

    from_: From
    to: To
    distance: int
    track: Track

    class Config:
        fields = {"from_": "from"}


class RouteSection(BaseElement):
    """A class representing a TransXChange RouteSection."""

    route_link: List[RouteLink]
