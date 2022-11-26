"""routes.py."""
from typing import List, Optional

from pytxc.elements import BaseElement
from pytxc.links import From, To
from pytxc.locations import Track


class Route(BaseElement):
    """A class representing a TransXChange Route."""

    private_code: str
    description: Optional[str]
    route_section_ref: str


class RouteLink(BaseElement):
    """A class representing a TransXChange RouteLink."""

    from_: From
    to: To
    distance: Optional[int]
    track: Optional[Track]

    class Config:
        fields = {"from_": "from"}


class RouteSection(BaseElement):
    """A class representing a TransXChange RouteSection."""

    route_link: List[RouteLink]
