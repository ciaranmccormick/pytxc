"""services.py."""
from datetime import date
from typing import List, Optional

from pytxc.elements import BaseElement
from pytxc.journeys import JourneyPattern


class OutboundDescription(BaseElement):
    """A class representing an OutboundDescription node."""

    origin: str
    destination: str
    description: str


class OperatingPeriod(BaseElement):
    """A class representing an OperatingPeriod."""

    start_date: date
    end_date: Optional[date]


class Line(BaseElement):
    """A class representing a TransXChange Line."""

    line_name: str
    outbound_description: Optional[OutboundDescription]


class StandardService(BaseElement):
    """A class representing a StandardService."""

    origin: str
    destination: str
    use_all_stop_points: Optional[bool]
    journey_pattern: List[JourneyPattern] = []
    vias: List[str] = []


class Service(BaseElement):
    """A class representing a Service."""

    service_code: str
    lines: List[Line]
    operating_period: OperatingPeriod
    ticket_machine_service_code: Optional[str]
    registered_operator_ref: str
    public_use: bool
    standard_service: StandardService


"""
class DayOfWeek(Enum):
    monday = "Monday"
    tuesday = "Tuesday"
    wednesday = "Wednesday"
    thursday = "Thursday"
    friday = "Friday"
    saturday = "Saturday"
    sunday = "Sunday"

    @classmethod
    def from_weekday_int(cls, weekday: int) -> "DayOfWeek":
        map = {
            0: cls.monday,
            1: cls.tuesday,
            2: cls.wednesday,
            3: cls.thursday,
            4: cls.friday,
            5: cls.saturday,
            6: cls.sunday
        }
        return map[weekday]


class OperatingProfile(Element):
    def __repr__(self) -> str:
        if self.holidays_only:
            return "OperatingProfile(holidays only)"
        days_of_week = self.days_of_week
        if len(days_of_week) == 0:
            return "OperatingProfile(none)"
        return f"OperatingProfile({' '.join([d.value for d in days_of_week])})"

    @property
    def holidays_only(self) -> bool:
        path = "RegularDayType/HolidaysOnly"
        elem = self.find(path)
        return elem is not None

    @property
    def days_of_week(self) -> List[DayOfWeek]:
        path = "RegularDayType/DaysOfWeek"
        days_of_week_elem = self.find(path)
        applicable_days = []
        if days_of_week_elem is not None:
            for day in DayOfWeek:
                if days_of_week_elem.find(day.value) is not None:
                    applicable_days.append(day)
        return applicable_days


class Service(Element):
    @property
    def operating_profile(self) -> Optional[OperatingProfile]:
        path = "OperatingProfile"
        element = self.find(path)
        if element is not None:
            return OperatingProfile(element)
        return None
"""
