from datetime import datetime
from pathlib import Path
from typing import Iterable, List, Optional

from lxml import etree
from lxml.etree import _Attrib, _Element
from pydantic import BaseModel

from .constants import (
    NAMESPACES,
    creation_date_time_key,
    file_name_key,
    modification_date_time_key,
    modification_key,
    revision_number_key,
    schema_version_key,
)


class TXCAttributes(BaseModel):
    schema_version: str
    creation_date_time: datetime
    modification_date_time: datetime
    modification: str
    revision_number: int
    file_name: str

    @classmethod
    def from_attrib(cls, attrib: _Attrib):
        return cls(
            schema_version=attrib.get(schema_version_key),
            creation_date_time=attrib.get(creation_date_time_key),
            modification_date_time=attrib.get(modification_date_time_key),
            modification=attrib.get(modification_key),
            revision_number=attrib.get(revision_number_key),
            file_name=attrib.get(file_name_key),
        )


class Element:
    def __init__(self, element: _Element):
        self.namespaces = NAMESPACES
        self._element = element

    @property
    def text(self) -> Optional[str]:
        return self._element.text

    @property
    def attrib(self) -> _Attrib:
        return self._element.attrib

    @property
    def tag(self) -> str:
        return self._element.tag

    @classmethod
    def from_path(cls, path: Path):
        with path.open("r") as f:
            return cls(etree.parse(f).getroot())

    def find(self, path: str) -> Optional["Element"]:
        element = self._element.find(path, namespaces=self.namespaces)
        if element is not None:
            return Element(element)
        return None

    def find_all(self, path: str) -> List["Element"]:
        return [
            Element(el)
            for el in self._element.findall(path, namespaces=self.namespaces)
        ]

    def find_text(self, path: str) -> Optional[str]:
        return self._element.findtext(path, namespaces=self.namespaces)

    def get_root(self) -> "Element":
        return Element(self._element.getroottree().getroot())

    def iter_find(self, path: str) -> Iterable["Element"]:
        elements = self._element.iterfind(
            path,
            namespaces=self.namespaces,  # type: ignore
        )
        return (Element(el) for el in elements)
