from typing import Optional
from lxml.etree import _Element
from pydantic import BaseModel

from .constants import NAMESPACES


class Location(BaseModel):
    id: Optional[str]
    longitude: float
    latitude: float

    @classmethod
    def from_element(cls, element: _Element):
        return cls(
            id=element.attrib.get("id"),
            longitude=element.findtext("./txc:Longitude", namespaces=NAMESPACES),
            latitude=element.findtext("./txc:Latitude", namespaces=NAMESPACES),
        )
