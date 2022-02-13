from lxml import etree

from pytxc import Timetable
from pytxc.routes import Location, RouteLink


def test_route_links(txc_file):
    timetable = Timetable.from_file(txc_file)
    sections = timetable.route_sections
    assert len(sections) > 0
    links = sections[0].route_links
    assert len(links) == 49
    track = links[0].track
    assert track is not None
    assert len(track.mapping) == 32
    first_location = track.mapping[0]
    last_location = track.mapping[-1]
    assert first_location.longitude == -1.312878
    assert first_location.latitude == 54.562472
    assert last_location.longitude == -1.313024
    assert last_location.latitude == 54.567029


def test_route_sections(txc_file):
    timetable = Timetable.from_file(txc_file)
    route_sections = timetable.route_sections
    assert len(route_sections) == 3
    first_section = route_sections[0]
    assert len(first_section.route_links) == 49
    first_link = first_section.route_links[0]
    from_ = first_link.from_
    assert from_ is not None
    assert from_.stop_point_ref == "077072002S"
    to = first_link.to
    assert to is not None
    assert to.stop_point_ref == "077072001X"
    assert first_link.distance == 516


def test_route(txc_file):
    timetable = Timetable.from_file(txc_file)
    routes = timetable.routes
    route = routes[0]
    assert route.private_code == "35st-39"
    assert route.id == "RT39"
    assert route.description == "Stockton - Wolviston Court"
    ref = route.route_section_refs[0]
    assert ref.text == "RS1"
    route_section = ref.resolve()
    assert route_section is not None
    assert route_section.id == "RS1"
    assert route_section.route_links[0].id == "RL1"
    assert route_section.route_links[0].get_parent().id == route_section.id


def test_location_none_children():
    location_str = """
    <Location id="L1" xmlns="http://www.transxchange.org.uk/">
    </Location>
    """
    element = etree.fromstring(location_str)
    location = Location(element)
    assert location.longitude is None
    assert location.latitude is None


def test_route_link_none():
    route_link_str = """
    <RouteLink id="RL1" xmlns="http://www.transxchange.org.uk/">
    </RouteLink>
    """
    element = etree.fromstring(route_link_str)
    route_link = RouteLink(element=element)
    assert route_link.from_ is None
    assert route_link.to is None
    assert route_link.distance is None
    assert route_link.track is None
    assert route_link
