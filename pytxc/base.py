import re
from datetime import datetime
from typing import Optional, Type, TypeVar, Union

from lxml.etree import fromstring, tostring
from pydantic import BaseModel

HANDLERS = {
    str: lambda el: str(el.text),
    int: lambda el: int(el.text),
    float: lambda el: float(el.text),
    bool: lambda el: bool(el.text),
}


def remove_namespace(string: str) -> str:
    end = string.find("}") + 1
    return string[end:]


def snake_to_pascal(snake: str) -> str:
    """Return a pascal case formatted string from a snake case string."""
    return "".join(s.capitalize() for s in snake.split("_"))


def pascal_to_snake(pascal: Union[str, bytes]) -> str:
    """Return a snake case formatted string a pascal case string."""
    if isinstance(pascal, bytes):
        pascal_str = pascal.decode("utf-8")
    else:
        pascal_str = pascal
    return "_".join(p.lower() for p in re.split("(?<=.)(?=[A-Z])", pascal_str))


T = TypeVar("T", bound="BaseTxCElement")


class Attributes(BaseModel):
    """Class representing all the key/value items in the attrib."""

    id: Optional[str]
    file_name: Optional[str]
    sequence_number: Optional[int]
    creation_date_time: Optional[datetime]
    modification_date_time: Optional[datetime]
    modification: Optional[str]
    revision_number: Optional[int]
    schema_version: Optional[str]


class BaseTxCElement(BaseModel):
    attributes: Attributes

    @staticmethod
    def _populate_attributes(element) -> Attributes:
        attrs = {}
        if element.attrib:
            attrs = {
                pascal_to_snake(attrib_key): attrib_value
                for attrib_key, attrib_value in element.attrib.items()
            }
        return Attributes.parse_obj(attrs)

    @classmethod
    def from_string(cls: Type[T], string: str) -> T:
        element = fromstring(string)
        attrs = {"attributes": cls._populate_attributes(element)}
        for child in element.getchildren():
            name = pascal_to_snake(remove_namespace(child.tag))
            model_field = cls.__fields__[name]

            if model_field.is_complex():
                attrs[name] = model_field.type_.from_string(tostring(child))
            else:
                type_ = model_field.type_
                attrs[name] = type_(child.text.strip())
        return cls.parse_obj(attrs)
