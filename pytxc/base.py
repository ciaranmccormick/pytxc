import re
from datetime import date, datetime, time
from typing import Any, Dict, Optional, Type, TypeVar, Union

from lxml.etree import fromstring, tostring
from pydantic import BaseModel
from pydantic.fields import SHAPE_LIST, ModelField

HANDLERS = {
    str: lambda text: str(text),
    int: lambda text: int(text),
    float: lambda text: float(text),
    bool: lambda text: bool(text),
    time: lambda text: time.fromisoformat(text),
    datetime: lambda text: datetime.fromisoformat(text),
    date: lambda text: date.fromisoformat(text),
}


RESERVED_WORDS = ["from"]


def is_pseudo_array(model_field: ModelField):
    """Return True if field is a pseduo-array.

    In TransXChange there are elements that hold list of child elements with
    a similar name,
    e.g
    <Operators>
        <Operator></Operator>
        <Operator></Operator>
    </Operators>

    But there are also elements that hold a list child elements with different names,
    e.g.
    <RouteSection>
        <RouteLink></RouteLink>
        <RouteLink></RouteLink>
        <RouteLink></RouteLink>
    </RouteSection>

    These 2 scenarios are handled separately since in our Models
    operators: List[Operator] and route_section: List[RouteLink]

    """
    return pascal_to_snake(model_field.type_.__name__) == model_field.name


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
    attributes: Optional[Attributes]

    @staticmethod
    def _populate_attributes(element) -> Optional[Attributes]:
        attrs = {}
        if element.attrib:
            attrs = {
                pascal_to_snake(attrib_key): attrib_value
                for attrib_key, attrib_value in element.attrib.items()
            }
            return Attributes.parse_obj(attrs)
        else:
            return None

    @classmethod
    def from_string(cls: Type[T], string: str) -> T:
        element = fromstring(string)
        fields: Dict[str, Any] = {}

        for child in element.getchildren():  # type: ignore
            name = pascal_to_snake(remove_namespace(child.tag))

            if name in RESERVED_WORDS:
                model_field = cls.__fields__.get(f"{name}_")
            else:
                model_field = cls.__fields__.get(name)

            if not model_field:
                continue

            if model_field.shape == SHAPE_LIST and is_pseudo_array(model_field):
                items = fields.get(name, [])
                items.append(model_field.type_.from_string(tostring(child)))
                fields[name] = items
            elif model_field.shape == SHAPE_LIST and not is_pseudo_array(model_field):
                type_ = model_field.type_
                fields[name] = [
                    type_.from_string(tostring(el)) for el in child.iterchildren()
                ]
            elif model_field.is_complex():
                # complex type i.e. <Operator>...</Operator>
                fields[name] = model_field.type_.from_string(tostring(child))
            else:
                # int, string, datetime, float
                type_ = model_field.type_
                func = HANDLERS[type_]
                fields[name] = func(child.text.strip())  # type: ignore

        attributes = cls._populate_attributes(element)
        if attributes:
            fields["attributes"] = attributes

        return cls.parse_obj(fields)
