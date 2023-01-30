from pytxc.services import OperatingPeriod
from tests.constants import NSPACE


def test_operating_period(snapshot):
    string = f"""
    <OperatingPeriod {NSPACE}>
        <StartDate>2023-01-03</StartDate>
    </OperatingPeriod>
    """
    operating_period = OperatingPeriod.from_string(string)
    snapshot.assert_match(operating_period.json(indent=2))
