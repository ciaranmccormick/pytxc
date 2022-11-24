"""vehicles.py"""
from datetime import time
from typing import List, Optional

from pytxc.elements import BaseElement, BaseEnum


class Block(BaseElement):
    """A class representing a Block node."""

    description: str
    block_number: str


class TicketMachine(BaseElement):
    """A class representing a TicketMachine."""

    journey_code: str


class Operational(BaseElement):
    """A class representing a TransXChange Operational node."""

    ticket_machine: TicketMachine
    block: Optional[Block]


class BankHoliday(BaseEnum):
    boxing_day = "BoxingDay"
    boxing_day_holiday = "BoxingDayHoliday"
    christmas_day = "ChristmasDay"
    christmas_day_holiday = "ChristmasDayHoliday"
    christmas_eve = "ChristmasEve"
    easter_monday = "EasterMonday"
    good_friday = "GoodFriday"
    late_summer_bank_holiday = "LateSummerBankHoliday"
    late_summer_bank_holiday_not_scotland = "LateSummerBankHolidayNotScotland"
    may_day = "MayDay"
    new_years_day = "NewYearsDay"
    new_years_day_holiday = "NewYearsDayHoliday"
    new_years_eve = "NewYearsEve"
    spring_bank = "SpringBank"


class BankHolidayOperation(BaseElement):
    days_of_operation: List[BankHoliday] = []
    days_of_non_operation: List[BankHoliday] = []


class DayOfWeek(BaseEnum):
    monday = "Monday"
    tuesday = "Tuesday"
    wednesday = "Wednesday"
    thursday = "Thursday"
    friday = "Friday"
    saturday = "Saturday"
    sunday = "Sunday"


class RegularDayType(BaseElement):
    days_of_week: List[DayOfWeek] = []
    holidays_only: bool = False


class OperatingProfile(BaseElement):
    """A class representing a TransXChange OperatingProfile."""

    regular_day_type: RegularDayType
    bank_holiday_operation: Optional[BankHolidayOperation]


class VehicleJourneyTimingLink(BaseElement):
    """A class representing a TransXChange VehicleJourneyTimingLink."""

    journey_pattern_timing_link_ref: str
    run_time: str


class VehicleJourney(BaseElement):
    """A class representing a VehicleJourney node."""

    departure_time: time
    direction: str
    operating_profile: OperatingProfile
    operational: Operational
    private_code: Optional[str]
    vehicle_journey_code: str
    vehicle_journey_timing_link: List[VehicleJourneyTimingLink]
    service_ref: str
    line_ref: str
    journey_pattern_ref: str
    operator_ref: str
