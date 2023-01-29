from pathlib import Path

from pytxc.txc import TransXChange


def test_no_header_attrs(snapshot):
    string = """
    <TransXChange xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xmlns="http://www.transxchange.org.uk/"
    RegistrationDocument="false"
    xsi:schemaLocation="http://www.transxchange.org.uk/
    http://www.transxchange.org.uk/schema/2.4/TransXChange_general.xsd">
    </TransXChange>
    """
    timetable = TransXChange.from_string(string)
    snapshot.assert_match(timetable.json(indent=2))


def test_timetable_from_file_path(snapshot):
    data_dir = Path(__file__).parent / "data"
    stockton = data_dir / "stockton_35.xml"
    with stockton.open("r", encoding="utf-8") as file_:
        timetable = TransXChange.from_string(file_.read())
    snapshot.assert_match(timetable.json())
