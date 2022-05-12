from datetime import time

from lxml import etree

from pytxc import Timetable
from pytxc.journeys import JourneyPatternTimingLink
from pytxc.vehicles import VehicleJourney


def test_journey_pattern_sections(txc_file):
    timetable = Timetable.from_file(txc_file)
    first_section = timetable.journey_pattern_sections[0]
    assert len(first_section.timing_links) == 30
    assert len(first_section.get_children()) == 30
    first_link = first_section.timing_links[0]
    assert first_link.to is not None
    assert first_link.to.sequence_number == 22
    assert first_link.from_ is not None
    assert first_link.from_.sequence_number == 21
    assert first_link.from_.activity == "pickUpAndSetDown"
    assert first_link.from_.dynamic_destination_display == "Stockton"
    assert first_link.from_.timing_status == "principalTimingPoint"
    assert first_link.from_.stop_point_ref == "077072584A"
    assert first_link.run_time == "PT0M0S"

    route_link_ref = first_link.route_link_ref
    assert route_link_ref is not None
    assert route_link_ref.text == "RL51"
    route_link = route_link_ref.resolve()
    assert route_link is not None
    from_ = route_link.from_
    assert from_ is not None
    assert from_.stop_point_ref == "077072584A"


def test_journey_patterns(txc_file):
    timetable = Timetable.from_file(txc_file)
    services = timetable.services
    standard = services[0].standard_services[0]
    assert len(standard.journey_patterns) == 3
    pattern = standard.journey_patterns[0]
    assert pattern.direction == "outbound"
    assert pattern.destination_display == "Stockton High Street Stand J"
    route_ref = pattern.route_ref
    assert route_ref is not None
    assert route_ref.text == "RT40"


def test_vehicle_journeys(txc_file):
    timetable = Timetable.from_file(txc_file)
    vehicle_journeys = timetable.vehicle_journeys
    assert len(vehicle_journeys) == 93
    journey = vehicle_journeys[0]

    private_code = journey.private_code
    assert private_code is not None
    assert private_code == "35st:I:0:663:fCSbfB3l85w="

    direction = journey.direction
    assert direction is not None
    assert direction == "outbound"

    operator_ref = journey.operator_ref
    assert operator_ref is not None
    assert operator_ref.text == "1"

    operator = operator_ref.resolve()
    assert operator is not None
    assert operator.national_operator_code == "SCTE"
    assert operator.operator_short_name == "Stagecoach"

    vehicle_journey_code = journey.vehicle_journey_code
    assert vehicle_journey_code is not None
    assert vehicle_journey_code == "VJ1290"
    assert journey.departure_time == time(7, 52, 0)

    service_ref = journey.service_ref
    assert service_ref is not None
    assert service_ref.text == "PB0001987:221"

    line_ref = journey.line_ref
    assert line_ref is not None
    assert line_ref.text == "SCTE:PB0001987:221:35:"

    journey_pattern_ref = journey.journey_pattern_ref
    assert journey_pattern_ref is not None
    assert journey_pattern_ref.text == "JP1"

    timing_links = journey.timing_links
    assert len(timing_links) == 30
    timing_link = timing_links[0]
    assert timing_link.run_time == "PT1M0S"

    jp_timing_link_ref = timing_link.journey_pattern_timing_link_ref
    assert jp_timing_link_ref is not None
    assert jp_timing_link_ref.text == "JPTL1"

    jp_timing_link = jp_timing_link_ref.resolve()
    assert jp_timing_link is not None
    from_ = jp_timing_link.from_
    assert from_ is not None
    assert from_.stop_point_ref == "077072584A"
    assert from_.timing_status == "principalTimingPoint"

    operational = journey.operational
    assert operational is not None
    ticket_machine = operational.ticket_machine
    assert ticket_machine is not None
    assert ticket_machine.journey_code == "7"
    block = operational.block
    assert block is None

    operating_profile = journey.operating_profile
    assert operating_profile is not None
    assert operating_profile.holidays_only


def test_journey_pattern_timing_link_none():
    jp_timing_link_str = """
    <JourneyPatternTimingLink id="JPTL1" xmlns="http://www.transxchange.org.uk/">
        <RouteLinkRef>RL1</RouteLinkRef>
        <RunTime>PT0M0S</RunTime>
    </JourneyPatternTimingLink>
    """
    element = etree.fromstring(jp_timing_link_str)
    jp_timing_link = JourneyPatternTimingLink(element)
    assert jp_timing_link.from_ is None
    assert jp_timing_link.to is None


def test_operational_structure():
    vj_str = """
    <VehicleJourney xmlns="http://www.transxchange.org.uk/">
        <PrivateCode>ECYO005SU:ektqN3RDaUYzRDQ9</PrivateCode>
        <OperatorRef>O1</OperatorRef>
        <Direction>outbound</Direction>
        <Operational>
            <Block>
                <Description>7053</Description>
                <BlockNumber>7053</BlockNumber>
            </Block>
        </Operational>
    </VehicleJourney>
    """
    element = etree.fromstring(vj_str)
    vehicle_journey = VehicleJourney(element)
    operational = vehicle_journey.operational

    assert operational is not None
    block = operational.block
    assert block is not None
    assert block.description == "7053"
    assert block.block_number == "7053"
    ticket_machine = operational.ticket_machine
    assert ticket_machine is None


def test_vehicle_journey_none_children():
    vj_str = """
    <VehicleJourney xmlns="http://www.transxchange.org.uk/">
        <PrivateCode>ECYO005SU:ektqN3RDaUYzRDQ9</PrivateCode>
        <OperatorRef>O1</OperatorRef>
        <Direction>outbound</Direction>
    </VehicleJourney>
    """
    element = etree.fromstring(vj_str)
    vehicle_journey = VehicleJourney(element)

    assert vehicle_journey.operational is None
    assert vehicle_journey.departure_time is None


def test_operating_profile_none():
    vehicle_journey_str = """
    <VehicleJourney xmlns="http://www.transxchange.org.uk/">
        <OperatingProphet>
            <RegularDayType>
              <HolidaysOnly/>
            </RegularDayType>
        </OperatingProphet>
    </VehicleJourney>
    """
    element = etree.fromstring(vehicle_journey_str)
    vehicle_journey = VehicleJourney(element)
    operating_profile = vehicle_journey.operating_profile
    assert operating_profile is None
