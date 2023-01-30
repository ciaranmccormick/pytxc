from pytxc.stops import AnnotatedStopPointRef

NSPACE = 'xmlns="http://www.transxchange.org.uk/"'


def test_loading_annotated_stop_point_refs(snapshot):
    """Verify that well structured stops are parsed correctly."""
    string = f"""
    <AnnotatedStopPointRef {NSPACE}>
      <StopPointRef>077072002S</StopPointRef>
      <CommonName>High Street Stand S</CommonName>
    </AnnotatedStopPointRef>
    """
    stop = AnnotatedStopPointRef.from_string(string)
    snapshot.assert_match(stop.json(indent=2))


def test_no_common_name(snapshot):
    """XML should still be parsed even if CommonName is missing."""
    string = f"""
    <AnnotatedStopPointRef {NSPACE}>
      <StopPointRef>077072002S</StopPointRef>
    </AnnotatedStopPointRef>
    """
    stop = AnnotatedStopPointRef.from_string(string)
    snapshot.assert_match(stop.json(indent=2))


def test_stops_with_location(snapshot):
    """Can we parse an AnnotatedStopPointRef with a location?"""
    string = f"""
    <AnnotatedStopPointRef {NSPACE}>
        <StopPointRef>109000009362</StopPointRef>
        <CommonName>Roundhouse Road</CommonName>
        <Location>
            <Longitude>-1.458709</Longitude>
            <Latitude>52.916994</Latitude>
        </Location>
    </AnnotatedStopPointRef>
    """
    stop = AnnotatedStopPointRef.from_string(string)
    snapshot.assert_match(stop.json(indent=2))
