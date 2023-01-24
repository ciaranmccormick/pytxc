from lxml import etree

from pytxc.journeys.operations import OperatingProfile, Operational
from tests.constants import NSPACE


def test_operational(snapshot):
    """Can we parse an Operational element."""
    xml = f"""
      <Operational {NSPACE}>
        <TicketMachine>
          <JourneyCode>7</JourneyCode>
        </TicketMachine>
      </Operational>
    """
    element = etree.fromstring(xml)
    operational = Operational.from_txc(element)
    snapshot.assert_match(operational.json(indent=2))


def test_parsing_operating_period(snapshot):
    """Can we parse an OperatingPeriod."""
    xml = f"""
      <OperatingProfile {NSPACE}>
        <RegularDayType>
          <HolidaysOnly />
        </RegularDayType>
        <BankHolidayOperation>
          <DaysOfOperation>
            <ChristmasEve />
            <NewYearsEve />
          </DaysOfOperation>
          <DaysOfNonOperation>
            <ChristmasDay />
            <BoxingDay />
            <GoodFriday />
            <NewYearsDay />
            <LateSummerBankHolidayNotScotland />
            <MayDay />
            <EasterMonday />
            <SpringBank />
            <ChristmasDayHoliday />
            <BoxingDayHoliday />
            <NewYearsDayHoliday />
          </DaysOfNonOperation>
        </BankHolidayOperation>
      </OperatingProfile>
    """
    element = etree.fromstring(xml)
    operational = OperatingProfile.from_txc(element)
    snapshot.assert_match(operational.json())
