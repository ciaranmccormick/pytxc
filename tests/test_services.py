from datetime import datetime
from typing import cast

from lxml import etree

from pytxc import TransXChange
from pytxc.journeys.operations import OperatingProfile
from pytxc.services import (  # DayOfWeek,; OperatingPeriod,; OperatingProfile,; Service,
    StandardService,
)


def test_services(snapshot, txc_file):
    timetable = cast(TransXChange, TransXChange.from_file(txc_file))
    snapshot.assert_match(timetable.json())

    services = timetable.services
    assert len(services) == 1
    service = services[0]
    assert service.service_code == "PB0001987:221"
    lines = service.lines
    assert len(lines) == 1
    line = lines[0]
    assert line.line_name == "35"

    operating_period = service.operating_period
    assert operating_period is not None
    assert operating_period.start_date == datetime(2021, 11, 21).date()
    assert operating_period.end_date == datetime(2022, 1, 3).date()


def test_standard_service(snapshot, txc_root):
    timetable = cast(TransXChange, TransXChange.from_txc(txc_root))
    snapshot.assert_match(timetable.json())

    services = timetable.services
    assert len(services) == 1
    standard_service = services[0].standard_service
    assert standard_service
    standard = standard_service
    assert standard.origin == "Stockton High Street"
    assert standard.destination == "Billingham High Grange"
    assert standard.use_all_stop_points


def test_standard_service_none_use_all_stop_points(snapshot):
    standard_service_str = """
    <StandardService xmlns="http://www.transxchange.org.uk/">
        <Origin>Great Yarmouth</Origin>
        <Destination>Burgh Castle</Destination>
        <Vias>
            <Via>Bradwell</Via>
        </Vias>
    </StandardService>
    """
    element = etree.fromstring(standard_service_str)
    standard_service = cast(StandardService, StandardService.from_txc(element))
    assert standard_service.use_all_stop_points is None
    snapshot.assert_match(standard_service.json())


def test_operating_profile(snapshot):
    xml = """
    <OperatingProfile xmlns="http://www.transxchange.org.uk/">
        <RegularDayType>
            <HolidaysOnly/>
        </RegularDayType>
        <BankHolidayOperation>
            <DaysOfOperation>
                <GoodFriday/>
                <LateSummerBankHolidayNotScotland/>
                <MayDay/>
                <EasterMonday/>
                <SpringBank/>
            </DaysOfOperation>
            <DaysOfNonOperation>
                <ChristmasDay/>
                <BoxingDay/>
                <NewYearsDay/>
                <ChristmasDayHoliday/>
                <BoxingDayHoliday/>
                <NewYearsDayHoliday/>
                <ChristmasEve/>
                <NewYearsEve/>
            </DaysOfNonOperation>
        </BankHolidayOperation>
    </OperatingProfile>
    """
    element = etree.fromstring(xml)
    profile = OperatingProfile.from_txc(element)
    snapshot.assert_match(profile.json())


def test_days_of_operation(snapshot):
    xml = """
    <OperatingProfile xmlns="http://www.transxchange.org.uk/">
        <RegularDayType>
            <DaysOfWeek>
                <Monday/>
                <Tuesday/>
                <Wednesday/>
                <Thursday/>
                <Friday/>
            </DaysOfWeek>
        </RegularDayType>
    </OperatingProfile>
    """
    element = etree.fromstring(xml)
    profile = OperatingProfile.from_txc(element)
    snapshot.assert_match(profile.json())


# def test_operating_profile_holidays_only():
#     operating_profile_str = """
#     <OperatingProfile xmlns="http://www.transxchange.org.uk/">
#         <RegularDayType>
#             <HolidaysOnly/>
#         </RegularDayType>
#     </OperatingProfile>
#     """
#     element = etree.fromstring(operating_profile_str)
#     operating_profile = OperatingProfile(element)
#     assert operating_profile.holidays_only is True


# def test_operating_profile_week_days():
#     operating_profile_str = """
#     <OperatingProfile xmlns="http://www.transxchange.org.uk/">
#         <RegularDayType>
#             <DaysOfWeek>
#                 <Monday/>
#                 <Tuesday/>
#                 <Wednesday/>
#                 <Thursday/>
#                 <Friday/>
#             </DaysOfWeek>
#         </RegularDayType>
#     </OperatingProfile>
#     """
#     element = etree.fromstring(operating_profile_str)
#     operating_profile = OperatingProfile(element)
#     days_of_week = operating_profile.days_of_week
#     assert len(days_of_week) == 5
#     assert DayOfWeek.monday in days_of_week
#     assert DayOfWeek.tuesday in days_of_week
#     assert DayOfWeek.wednesday in days_of_week
#     assert DayOfWeek.thursday in days_of_week
#     assert DayOfWeek.friday in days_of_week
#     assert operating_profile.holidays_only is False


# def test_day_of_week_from_int():
#     day = DayOfWeek.from_weekday_int(0)
#     assert day == DayOfWeek.monday
#     day = DayOfWeek.from_weekday_int(6)
#     assert day == DayOfWeek.sunday
