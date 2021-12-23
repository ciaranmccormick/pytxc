from pydantic import BaseModel

from .txc import Element


class Operator(BaseModel):
    id: str
    national_operator_code: str
    operator_code: str
    operator_short_name: str
    licence_number: str

    @classmethod
    def from_element(cls, element: Element):
        return cls(
            id=element.attrib.get("id"),
            national_operator_code=element.find_text("./txc:NationalOperatorCode"),
            operator_code=element.find_text("./txc:OperatorCode"),
            operator_short_name=element.find_text("./txc:OperatorShortName"),
            licence_number=element.find_text("./txc:LicenceNumber"),
        )
