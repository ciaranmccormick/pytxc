from datetime import datetime
from pathlib import Path

from lxml import etree

from pytxc import AnnotatedStopPointRef, Timetable


def test_txc_header(txc_file):
    timetable = Timetable.from_file(txc_file)
    expected_filename = (
        "35st-None--SCTE-ST-2021-12-12-TXC_SOT_PB_ALL_20211121-BODS_V1_1.xml"
    )
    assert timetable.header.schema_version == "2.4"
    assert timetable.header.revision_number == 159
    assert timetable.header.modification == "revise"
    assert timetable.header.creation_date_time == datetime(2020, 11, 22, 11, 0, 0)
    assert timetable.header.modification_date_time == datetime(2021, 12, 17, 11, 8, 35)
    assert timetable.header.file_name == expected_filename
    assert timetable.get_parent() is None


def test_get_annotated_stop_point_refs(txc_file):
    timetable = Timetable.from_file(txc_file)
    stop_points = timetable.stop_points
    assert len(stop_points) == 48
    first_stop = stop_points[0]
    assert first_stop.stop_point_ref is not None
    assert first_stop.stop_point_ref.text == "077072002S"
    assert first_stop.common_name == "High Street Stand S"
    last_stop = stop_points[-1]
    assert last_stop.stop_point_ref is not None
    assert last_stop.stop_point_ref.text == "077072002J"
    assert last_stop.common_name == "High Street Stand J"


def test_stop_point_ref_is_none():
    annotated_stop_point_ref = """
    <AnnotatedStopPointRef xmlns="http://www.transxchange.org.uk/">
        <CommonName>Great Yarmouth,Market Gates</CommonName>
    </AnnotatedStopPointRef>
    """
    test_element = etree.fromstring(annotated_stop_point_ref)
    stop = AnnotatedStopPointRef(test_element)
    assert stop.stop_point_ref is None


def test_operators(txc_file):
    timetable = Timetable.from_file(txc_file)
    operators = timetable.operators
    assert len(operators) == 1
    operator = operators[0]
    assert operator.national_operator_code == "SCTE"
    assert operator.operator_code == "SOT"
    assert operator.operator_short_name == "Stagecoach"
    assert operator.operator_name_on_licence == "Cleveland Transit Ltd"
    assert operator.trading_name == "Stagecoach North East"
    assert operator.licence_number == "PB0001987"


def test_no_header_attrs():
    transxchange_str = """
    <TransXChange xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xmlns="http://www.transxchange.org.uk/"
    RegistrationDocument="false"
    xsi:schemaLocation="http://www.transxchange.org.uk/
    http://www.transxchange.org.uk/schema/2.4/TransXChange_general.xsd">
    </TransXChange>
    """
    element = etree.fromstring(transxchange_str)
    timetable = Timetable(element=element)

    assert timetable.header.creation_date_time is None
    assert timetable.header.file_name == ""
    assert timetable.header.modification == ""
    assert timetable.header.modification_date_time is None
    assert timetable.header.revision_number is None
    assert timetable.header.schema_version == ""


def test_timetable_from_file_path():
    data_dir = Path(__file__).parent / "data"
    stockton = data_dir / "stockton_35.xml"
    timetable = Timetable.from_file_path(stockton)
    assert timetable.header.schema_version == "2.4"
