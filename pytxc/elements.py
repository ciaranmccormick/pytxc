from typing import Dict, List, Optional, Type, TypeVar, Union

from lxml.etree import _Element


class Element:
    def __init__(self, element: Union["Element", _Element]):

        if isinstance(element, _Element):
            self._element = element
        else:
            self._element = element._element
        self.nsmap = {None: "http://www.transxchange.org.uk/"}

    def __repr__(self):
        return self._element.__repr__()

    @property
    def id(self) -> str:
        return self.attributes.get("id", "")

    @property
    def text(self) -> Optional[str]:
        text = self._element.text
        if text is not None:
            return text.strip()
        return None

    @property
    def attributes(self) -> Dict[str, str]:
        return {str(key): str(value) for key, value in self._element.attrib.items()}

    def _create_ref(self, path: str, element_class):
        element = self.find(path)
        if element is not None:
            return element_class(element)
        return None

    def find(self, path: str) -> Optional["Element"]:
        kwargs = {"namespaces": self.nsmap}
        element = self._element.find(path, **kwargs)  # type: ignore
        if element is not None:
            return Element(element)
        return None

    def find_all(self, path: str) -> List["Element"]:
        kwargs = {"namespaces": self.nsmap}
        return [
            Element(element)
            for element in self._element.findall(path, **kwargs)  # type: ignore
        ]

    def find_text(self, path: str) -> Optional[str]:
        kwargs = {"namespaces": self.nsmap}
        return self._element.findtext(path, **kwargs)  # type: ignore

    def get_parent(self) -> Optional["Element"]:
        parent = self._element.getparent()
        if parent is not None:
            return Element(parent)
        return None

    def get_children(self) -> List["Element"]:
        return [Element(element) for element in self._element.iterchildren()]

    def get_root(self) -> "Element":
        return Element(self._element.getroottree().getroot())


T = TypeVar("T", bound=Element)


class Ref(Element):
    element_class: Type[Element]
    path: str = ""

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(text={self.text})"

    def resolve(self) -> Element:
        ref = self.text
        root = self.get_root()
        element = root.find(self.path + f"[@id='{ref}']")
        if self.element_class is None:
            raise NotImplementedError("No 'element_class' set.")
        if element is not None:
            return self.element_class(element)
        raise NotImplementedError("Not implemented")
