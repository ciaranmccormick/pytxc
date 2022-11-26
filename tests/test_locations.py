from lxml import etree

from pytxc.locations import Track
from tests.constants import NSPACE


def test_parsing_track(snapshot):
    """Can we parse a track with a mapping structure."""
    xml = f"""
        <Track {NSPACE}>
          <Mapping>
            <Location id="L1">
              <Longitude>-1.312878</Longitude>
              <Latitude>54.562472</Latitude>
            </Location>
            <Location id="L2">
              <Longitude>-1.312975</Longitude>
              <Latitude>54.562465</Latitude>
            </Location>
            <Location id="L3">
              <Longitude>-1.312974</Longitude>
              <Latitude>54.562492</Latitude>
            </Location>
            <Location id="L4">
              <Longitude>-1.312970</Longitude>
              <Latitude>54.562599</Latitude>
            </Location>
          </Mapping>
        </Track>
    """
    element = etree.fromstring(xml)
    track = Track.from_txc(element)
    snapshot.assert_match(track.json())
