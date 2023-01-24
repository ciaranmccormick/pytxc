"""operational.py"""


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
    """A class for representing BankHolidays."""

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
    """A class representing BankHolidayOperations."""

    days_of_operation: List[BankHoliday] = []
    days_of_non_operation: List[BankHoliday] = []


class DayOfWeek(BaseEnum):
    """A class representing DayOfWeek."""

    monday = "Monday"
    tuesday = "Tuesday"
    wednesday = "Wednesday"
    thursday = "Thursday"
    friday = "Friday"
    saturday = "Saturday"
    sunday = "Sunday"


class RegularDayType(BaseElement):
    """A class representing a RegularDayType."""

    days_of_week: List[DayOfWeek] = []
    holidays_only: bool = False


class OperatingProfile(BaseElement):
    """A class representing a TransXChange OperatingProfile."""

    regular_day_type: RegularDayType
    bank_holiday_operation: Optional[BankHolidayOperation]
