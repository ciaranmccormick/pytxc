"""operators.py."""
from typing import List, Optional

from pytxc.elements import BaseElement
from pytxc.locations import Location


class Garage(BaseElement):
    """A class representing a TransXChange Garage."""

    garage_code: str
    garage_name: str
    location: Location


class Operator(BaseElement):
    """A class representing a TransXChange Operator."""

    national_operator_code: str
    operator_code: Optional[str]
    operator_short_name: str
    operator_name_on_licence: Optional[str]
    trading_name: Optional[str]
    licence_number: str
    garages: List[Garage] = []
