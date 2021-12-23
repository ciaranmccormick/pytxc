from typing import Optional

from pydantic import BaseModel

from .common import Location
from .txc import Element

FIND_BY_REF = "./txc:StopPoints/txc:AnnotatedStopPointRef[txc:StopPointRef='{ref}']"


class AnnotatedStopPointRef(BaseModel):
    stop_point_ref: str
    common_name: str
    location: Optional[Location]

    @classmethod
    def from_element(cls, element: Element):
        location = element.find("./txc:Location")
        if location is not None:
            location = Location.from_element(location)
        return cls(
            stop_point_ref=element.find_text("./txc:StopPointRef"),
            common_name=element.find_text("./txc:CommonName"),
            location=location,
        )
