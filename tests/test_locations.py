from pytxc.locations import Mapping, Track
from tests.constants import NSPACE


def test_parsing_track(snapshot):
    """Can we parse a track with a mapping structure."""
    string = f"""
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
    track = Track.from_string(string)
    snapshot.assert_match(track.json(indent=2))


def test_mapping_to_geojson(snapshot):
    """Can we parse a Mapping object and export to geojson?"""
    string = f"""
          <Mapping {NSPACE}>
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
    """
    mapping = Mapping.from_string(string)
    snapshot.assert_match(mapping.to_geojson())
