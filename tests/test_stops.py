from lxml import etree

from pytxc.stops import AnnotatedStopPointRef

NSPACE = 'xmlns="http://www.transxchange.org.uk/"'


def test_loading_annotated_stop_point_refs(snapshot):
    """Verify that well structured stops are parsed correctly."""
    xml = f"""
    <AnnotatedStopPointRef {NSPACE}>
      <StopPointRef>077072002S</StopPointRef>
      <CommonName>High Street Stand S</CommonName>
    </AnnotatedStopPointRef>
    """
    element = etree.fromstring(xml)
    stop = AnnotatedStopPointRef.from_txc(element)
    snapshot.assert_match(stop.json())


def test_no_common_name(snapshot):
    """XML should still be parsed even if CommonName is missing."""
    xml = f"""
    <AnnotatedStopPointRef {NSPACE}>
      <StopPointRef>077072002S</StopPointRef>
    </AnnotatedStopPointRef>
    """
    element = etree.fromstring(xml)
    stop = AnnotatedStopPointRef.from_txc(element)
    snapshot.assert_match(stop.json())
