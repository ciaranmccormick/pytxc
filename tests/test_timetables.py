from pathlib import Path

from lxml import etree

from pytxc.txc import TransXChange


def test_no_header_attrs(snapshot):
    transxchange_str = """
    <TransXChange xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xmlns="http://www.transxchange.org.uk/"
    RegistrationDocument="false"
    xsi:schemaLocation="http://www.transxchange.org.uk/
    http://www.transxchange.org.uk/schema/2.4/TransXChange_general.xsd">
    </TransXChange>
    """
    element = etree.fromstring(transxchange_str)
    timetable = TransXChange.from_txc(element)
    snapshot.assert_match(timetable.json())


def test_timetable_from_file_path(snapshot):
    data_dir = Path(__file__).parent / "data"
    stockton = data_dir / "stockton_35.xml"
    timetable = TransXChange.from_file_path(stockton)
    snapshot.assert_match(timetable.json())
