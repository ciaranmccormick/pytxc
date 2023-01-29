import pytest

from pytxc.journeys.operations import OperatingProfile, Operational
from tests.constants import NSPACE


def test_operational(snapshot):
    """Can we parse an Operational string."""
    string = f"""
      <Operational {NSPACE}>
        <TicketMachine>
          <JourneyCode>7</JourneyCode>
        </TicketMachine>
      </Operational>
    """
    operational = Operational.from_string(string)
    snapshot.assert_match(operational.json(indent=2))


@pytest.mark.skip("Haven't implemented enums yet")
def test_parsing_operating_period(snapshot):
    """Can we parse an OperatingPeriod."""
    string = f"""
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
    operational = OperatingProfile.from_string(string)
    snapshot.assert_match(operational.json())
