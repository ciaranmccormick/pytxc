from typing import Optional

from lxml.etree import _Element
from pydantic import BaseModel

from .constants import NAMESPACES
from .common import Location

FIND_BY_REF = "./txc:StopPoints/txc:AnnotatedStopPointRef[txc:StopPointRef='{ref}']"


class AnnotatedStopPointRef(BaseModel):
    stop_point_ref: str
    common_name: str
    location: Optional[Location]

    @classmethod
    def from_element(cls, element: _Element):
        if (
            location := element.find("./txc:Location", namespaces=NAMESPACES)
        ) is not None:
            location = Location.from_element(location)
        return cls(
            stop_point_ref=element.findtext(
                "./txc:StopPointRef", namespaces=NAMESPACES
            ),
            common_name=element.findtext("./txc:CommonName", namespaces=NAMESPACES),
            location=location,
        )
