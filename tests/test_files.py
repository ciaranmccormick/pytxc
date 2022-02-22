"""
test_files.py
Tests of the parser against various "flavours" of TransXChange files.
"""
from datetime import datetime
from pathlib import Path

import pytest

from pytxc import Timetable

DATA_DIR = Path(__file__).parent / "data"


class TestStagecoachCheseterLine1:
    @pytest.fixture()
    def timetable(self):
        file_path = DATA_DIR / "1-None--STCR-CZ-2021-10-03-TXC_CZ20211003-BODS_V1_1.xml"
        timetable = Timetable.from_file_path(file_path)
        yield timetable

    def test_header_details(self, timetable: Timetable):
        """
        CreationDateTime -> 2020-11-22T11:00:00
        FileName -> 1-None--STCR-CZ-2021-10-03-TXC_CZ20211003-BODS_V1_1.xml
        Modification -> revise
        ModificationDateTime -> 2021-10-19T13:27:51
        RevisionNumber -> 72
        SchemaVersion -> 2.4
        """
        assert timetable.header.creation_date_time == datetime(2020, 11, 22, 11, 0, 0)
        assert timetable.header.file_name == (
            "1-None--STCR-CZ-2021-10-03-TXC_CZ20211003-BODS_V1_1.xml"
        )
        assert timetable.header.modification == "revise"
        assert timetable.header.modification_date_time == datetime(
            2021, 10, 19, 13, 27, 51
        )
        assert timetable.header.revision_number == 72
        assert timetable.header.schema_version == "2.4"

    def test_stop_points(self, timetable: Timetable):
        """
        66 AnnotatedStopPointRefs
        i=0 AnnotatedStopPointRef  -> 0610CH19049, Chester Bus Interchange
        i=14 AnnotatedStopPointRef -> 0610CH2491, High School
        i=-1 AnnotatedStopPointRef -> 0610CH2397, Canal Bridge
        """
        assert len(timetable.stop_points) == 66

        stop = timetable.stop_points[0]
        ref = stop.stop_point_ref
        assert ref is not None
        assert ref.text == "0610CH19049"
        assert stop.common_name == "Chester Bus Interchange"

        stop = timetable.stop_points[14]
        ref = stop.stop_point_ref
        assert ref is not None
        assert ref.text == "0610CH2491"
        assert stop.common_name == "High School"

        stop = timetable.stop_points[-1]
        ref = stop.stop_point_ref
        assert ref is not None
        assert ref.text == "0610CH2397"
        assert stop.common_name == "Canal Bridge"

    def test_operators(self, timetable: Timetable):
        """
        id -> 4
        NationalOperatorCode -> STCR
        OperatorCode -> STCR
        OperatorShortName -> Stagecoach
        OperatorNameOnLicence -> Ribble Motor Services Ltd
        TradingName -> Stagecoach Merseyside and South Lancashire
        LicenceNumber -> PC1033334
        """
        assert len(timetable.operators) == 1
        operator = timetable.operators[0]

        assert operator.national_operator_code == "STCR"
        assert operator.operator_code == "STCR"
        assert operator.operator_short_name == "Stagecoach"
        assert operator.operator_name_on_licence == "Ribble Motor Services Ltd"
        assert operator.trading_name == "Stagecoach Merseyside and South Lancashire"
        assert operator.licence_number == "PC1033334"

    def test_routes(self, timetable: Timetable):
        """
        5 Routes -> RT1 - RT5
        i = 0 Route  -> 1_1-1, Chester - Blacon Parade, RouteSectionRef=RS1
        i = -1 Route -> 1_1A-5, Chester - Blacon Parade, RouteSectionRef=RS5
        """
        assert len(timetable.routes) == 5

        route = timetable.routes[0]
        assert route.private_code == "1_1-1"
        assert route.description == "Chester - Blacon Parade"
        assert len(route.route_section_refs) == 1
        section_ref = route.route_section_refs[0]
        assert section_ref.text == "RS1"

        route = timetable.routes[4]
        assert route.private_code == "1_1A-5"
        assert route.description == "Chester - Blacon Parade"
        assert len(route.route_section_refs) == 1
        section_ref = route.route_section_refs[0]
        assert section_ref.text == "RS5"

    def test_route_sections(self, timetable: Timetable):
        """
        5 Route Sections
        RS1 -> 31 route links
        """
        assert len(timetable.route_sections) == 5

        section = timetable.route_sections[0]
        assert section.id == "RS1"
        assert len(section.route_links) == 31

        link = section.route_links[0]
        assert link.id == "RL1"
        assert link.distance == 262
        from_ = link.from_
        assert from_ is not None
        assert from_.stop_point_ref == "0610CH19049"
        to = link.to
        assert to is not None
        assert to.stop_point_ref == "0610CH1056"
        track = link.track
        assert track is not None
        assert len(track.mapping) == 11
        location = track.mapping[5]
        assert location.id == "L6"
        assert location.longitude == -2.889986
        assert location.latitude == 53.194497

    def test_services(self, timetable: Timetable):
        assert len(timetable.services) == 1
        service = timetable.services[0]
        assert len(service.lines) == 2
        line1 = service.lines[0]
        line2 = service.lines[1]
        assert len(service.standard_services) == 1
        standard = service.standard_services[0]

        assert service.service_code == "PC1033334:197"
        assert line1.line_name == "1"
        assert line1.id == "STCR:PC1033334:197:1:"
        assert line2.line_name == "1A"
        assert line2.id == "STCR:PC1033334:197:1A:"

        assert standard.origin == "Chester"
        assert standard.destination == "Blacon Parade"
        assert standard.use_all_stop_points

        assert len(standard.journey_patterns) == 5
        pattern = standard.journey_patterns[3]
        assert pattern.id == "JP4"
        assert pattern.destination_display == "Chester Chester Bus Interchange"
        assert pattern.direction == "inbound"
        route_ref = pattern.route_ref
        assert route_ref is not None
        assert route_ref.text == "RT4"
        operator_ref = pattern.operator_ref
        assert operator_ref is not None
        assert operator_ref.text == "4"

        section_refs = pattern.journey_pattern_section_refs
        assert len(section_refs) == 1
        section_ref = section_refs[0]
        assert section_ref.text == "JPS4"

        section = section_ref.resolve()
        assert section is not None
        assert section.id == "JPS4"
        assert len(section.timing_links) == 33
