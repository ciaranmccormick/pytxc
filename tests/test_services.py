from typing import cast

import pytest
from lxml import etree

from pytxc.journeys.operations import OperatingProfile
from pytxc.services import StandardService
from tests.constants import NSPACE


def test_standard_service(snapshot):
    string = f"""
    <StandardService {NSPACE}>
        <Origin>Derby</Origin>
        <Destination>Alvaston</Destination>
        <JourneyPattern id="jp_1">
            <DestinationDisplay>Morledge</DestinationDisplay>
            <OperatorRef>tkt_oid</OperatorRef>
            <Direction>outbound</Direction>
            <RouteRef>rt_0000</RouteRef>
            <JourneyPatternSectionRefs>js_1</JourneyPatternSectionRefs>
        </JourneyPattern>
    </StandardService>
    """
    standard_service = StandardService.from_string(string)
    snapshot.assert_match(standard_service.json(indent=2))


@pytest.mark.skip("Not ready to test yet")
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


@pytest.mark.skip("Not ready to test yet")
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


@pytest.mark.skip("Not ready to test yet")
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
