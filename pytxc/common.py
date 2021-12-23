from typing import Optional
from pydantic import BaseModel

from pytxc.txc import Element


class Location(BaseModel):
    id: Optional[str]
    longitude: float
    latitude: float

    @classmethod
    def from_element(cls, element: Element):
        return cls(
            id=element.attrib.get("id"),
            longitude=element.find_text("./txc:Longitude"),
            latitude=element.find_text("./txc:Latitude"),
        )
