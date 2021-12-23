from lxml.etree import _Element
from pydantic import BaseModel

from .constants import NAMESPACES


class Operator(BaseModel):
    id: str
    national_operator_code: str
    operator_code: str
    operator_short_name: str
    licence_number: str

    @classmethod
    def from_element(cls, element: _Element):
        id_ = element.attrib.get("id")
        return cls(
            id=id_,
            national_operator_code=element.findtext(
                "./txc:NationalOperatorCode", namespaces=NAMESPACES
            ),
            operator_code=element.findtext("./txc:OperatorCode", namespaces=NAMESPACES),
            operator_short_name=element.findtext(
                "./txc:OperatorShortName", namespaces=NAMESPACES
            ),
            licence_number=element.findtext(
                "./txc:LicenceNumber", namespaces=NAMESPACES
            ),
        )
