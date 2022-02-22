from lxml import etree

from pytxc import Timetable
from pytxc.elements import Element
from pytxc.routes import RouteRef


def test_create_ref_none(txc_file):
    timetable = Timetable.from_file(txc_file)

    test_path = "Blah"
    test_element_class = RouteRef

    result = timetable._create_ref(test_path, test_element_class)
    assert result is None


def test_text_none():
    element_str = """
    <AnnotatedStopPointRef>
        <StopPointRef>2900Y0378</StopPointRef>
        <CommonName>Great Yarmouth,Market Gates</CommonName>
    </AnnotatedStopPointRef>
    """
    element = etree.fromstring(element_str)
    element.text = None
    assert Element(element).text is None
