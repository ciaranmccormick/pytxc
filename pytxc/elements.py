"""elements.py."""
import re
from datetime import datetime
from enum import Enum
from pathlib import Path
from typing import IO, AnyStr, List, Optional, Type, Union

from lxml import etree
from lxml.etree import _Element
from pydantic import BaseModel
from pydantic.fields import ModelField

NAMESPACES = {None: "http://www.transxchange.org.uk/"}
_BASIC_TYPES = [str, int, bool]


def snake_to_pascal(snake: str) -> str:
    """Return a pascal case formatted string from a snake case string."""
    return "".join(s.capitalize() for s in snake.split("_"))


def pascal_to_snake(pascal: str) -> str:
    """Return a snake case formatted string a pascal case string."""
    return "_".join(p.lower() for p in re.split("(?<=.)(?=[A-Z])", pascal))


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


class TransXChangeBuilder:
    def __init__(self, kls: Type, node: _Element):
        self.kls = kls
        self.node = node
        self.attrs = {}
        self._aliases = {}
        self._properties = kls.schema()["properties"]

    @property
    def fields(self) -> List[str]:
        """Return a list of the fields in the kls."""
        names = []
        for model in self.kls.__fields__.values():
            if model.alias:
                self._aliases[model.alias] = model.name
                names.append(model.alias)
            else:
                names.append(model.name)
        return names

    def init_attrs(self):
        if self.node.attrib:
            element_attrib = {
                pascal_to_snake(attrib_key): attrib_value  # type: ignore
                for attrib_key, attrib_value in self.node.attrib.items()
            }
            self.attrs["attributes"] = Attributes.parse_obj(element_attrib)

    def get_model_field(self, field: str) -> ModelField:
        """Return the ModelField for this field."""
        field_name = self._aliases.get(field, field)
        return self.kls.__fields__[field_name]

    def get_model_class(self, field: str) -> Type["BaseElement"]:
        """Return the type of the fields model."""
        return self.get_model_field(field).type_

    def get_property_type(self, field: str) -> Optional[str]:
        """Return the type as defined by Pydantic properties dict."""
        return self._properties.get(field, {}).get("type")

    def get_next_nodes(self, field: str) -> List[_Element]:
        """Return all the nodes with Pascal."""
        node_name = snake_to_pascal(field)
        return self.node.findall(node_name, namespaces=NAMESPACES)  # type: ignore

    def is_pseudo_array(self, field: str) -> bool:
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
        return snake_to_pascal(field) == self.get_model_class(field).__name__

    def add_basic_type(self, field: str) -> None:
        """Adds the field and value to the attrs dict."""
        next_nodes = self.get_next_nodes(field)
        if next_nodes:
            self.attrs[field] = next_nodes[0].text

    def add_boolen_type(self, field: str) -> None:
        """Adds a boolean type to the attrs dict."""
        next_nodes = self.get_next_nodes(field)
        if next_nodes:
            node = next_nodes[0]
            if node.text is None:
                # presence of the node but no text is treated as truthy
                self.attrs[field] = True
            else:
                # process text if it exists
                self.attrs[field] = node.text

    def add_array_type(self, field: str) -> None:
        """Create and add array/list types to the parent object."""
        next_nodes = self.get_next_nodes(field)
        if not next_nodes:
            return

        model = self.get_model_class(field)
        if model in _BASIC_TYPES:
            self.attrs[field] = [child.text for child in next_nodes[0].iterchildren()]
            return

        if issubclass(model, BaseEnum):
            self.attrs[field] = [
                model.from_lxml(child) for child in next_nodes[0].iterchildren()
            ]
            return

        if self.is_pseudo_array(field):
            # A TransXChange single list-like element e.g. RouteSection
            self.attrs[field] = [
                TransXChangeBuilder(model, n).build() for n in next_nodes
            ]
        else:
            # A TransXChange list element e.g. Operators, Services, RouteSections
            self.attrs[field] = [
                TransXChangeBuilder(model, n).build()
                for n in next_nodes[0].iterchildren()
            ]

    def add_complex_type(self, field: str):
        """Adds a complex value to the attrs dict."""
        next_nodes = self.get_next_nodes(field)
        if next_nodes:
            model = self.get_model_class(field)
            self.attrs[field] = TransXChangeBuilder(model, next_nodes[0]).build()

    def build(self):
        self.init_attrs()

        for field in self.fields:
            type_ = self.get_property_type(field)
            if type_ in ["integer", "string", "number"]:
                self.add_basic_type(field)
                continue

            if type_ == "boolean":
                self.add_boolen_type(field)
                continue

            if type_ == "array":
                self.add_array_type(field)
                continue

            self.add_complex_type(field)

        return self.kls.parse_obj(self.attrs)


class BaseEnum(str, Enum):
    """An Enum class for TransXChange elements."""

    @classmethod
    def from_lxml(cls, element):
        return cls(element.xpath("name()"))


class BaseElement(BaseModel):
    """A base class for TransXChange objects."""

    attributes: Optional[Attributes]

    @classmethod
    def from_txc(cls, node: _Element) -> "BaseElement":
        """Return a BaseElement object from an lxml element."""
        return TransXChangeBuilder(cls, node).build()

    @classmethod
    def from_file_path(cls, path: Path) -> "BaseElement":
        """Return a BaseElement from a path."""
        with path.open("r") as txc_file:
            return cls.from_file(txc_file)

    @classmethod
    def from_file(cls, file: Union[IO[AnyStr], IO[bytes]]) -> "BaseElement":
        """Return a BaseElement from a file."""
        element = etree.parse(file).getroot()
        return cls.from_txc(element)

    @classmethod
    def from_string(cls, xml: str) -> "BaseElement":
        """Return a BaseElement from a string."""
        element = etree.fromstring(xml)
        return cls.from_txc(element)
