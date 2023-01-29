"""routes.py."""
from typing import List, Optional

from pytxc.base import BaseTxCElement
from pytxc.links import From, To
from pytxc.locations import Track


class Route(BaseTxCElement):
    """A class representing a TransXChange Route."""

    private_code: Optional[str]
    description: Optional[str]
    route_section_ref: str


class RouteLink(BaseTxCElement):
    """A class representing a TransXChange RouteLink."""

    from_: From
    to: To
    distance: Optional[int]
    track: Optional[Track]

    class Config:
        fields = {"from_": "from"}


class RouteSection(BaseTxCElement):
    """A class representing a TransXChange RouteSection."""

    route_link: List[RouteLink]
