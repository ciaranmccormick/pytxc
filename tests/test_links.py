from lxml import etree

from pytxc.links import From


def test_from_none_sequence():
    from_str = """
    <From id="JPSU3" xmlns="http://www.transxchange.org.uk/">
        <Activity>pickUpAndSetDown</Activity>
        <StopPointRef>2900Y0391</StopPointRef>
        <TimingStatus>otherPoint</TimingStatus>
        <FareStageNumber>206</FareStageNumber>
    </From>
    """
    element = etree.fromstring(from_str)
    from_ = From(element=element)
    assert from_.sequence_number is None
