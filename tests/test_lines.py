from pytxc.services import Line
from tests.constants import NSPACE


def test_line(snapshot):
    string = f"""
    <Line id="ADER:PC1116467:8:1A" {NSPACE}>
        <LineName>1A</LineName>
        <OutboundDescription>
            <Description>Derby to Alvaston</Description>
        </OutboundDescription>
        <InboundDescription>
            <Description>Alvaston to Derby</Description>
        </InboundDescription>
    </Line>
    """
    line = Line.from_string(string)
    snapshot.assert_match(line.json(indent=2))
