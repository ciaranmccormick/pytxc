# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot

snapshots = Snapshot()

snapshots["test_journey_pattern 1"] = {
    "attributes": {
        "creation_date_time": GenericRepr("datetime.datetime(2020, 11, 22, 11, 0)"),
        "file_name": None,
        "id": "JP1",
        "modification": "revise",
        "modification_date_time": GenericRepr(
            "datetime.datetime(2021, 12, 17, 11, 8, 35)"
        ),
        "revision_number": 159,
        "schema_version": None,
        "sequence_number": None,
    },
    "destination_display": "Stockton High Street Stand J",
    "direction": "outbound",
    "journey_pattern_section_refs": "JPS94",
    "operator_ref": "1",
    "route_ref": "RT40",
}

snapshots[
    "test_parse_journey_pattern_timing_link 1"
] = '{"attributes": {"id": "JPTL32", "file_name": null, "sequence_number": null, "creation_date_time": null, "modification_date_time": null, "modification": null, "revision_number": null, "schema_version": null}, "from_": {"attributes": {"id": "JPSU63", "file_name": null, "sequence_number": 2, "creation_date_time": null, "modification_date_time": null, "modification": null, "revision_number": null, "schema_version": null}, "stop_point_ref": "077072001X", "activity": "pickUpAndSetDown", "dynamic_destination_display": "Stockton", "timing_status": "principalTimingPoint", "fare_stage_number": null}, "to_": {"attributes": {"id": "JPSU64", "file_name": null, "sequence_number": 3, "creation_date_time": null, "modification_date_time": null, "modification": null, "revision_number": null, "schema_version": null}, "stop_point_ref": "077072405B", "activity": "pickUpAndSetDown", "dynamic_destination_display": "Stockton", "timing_status": "otherPoint", "fare_stage_number": null}, "route_link_ref": "RL2", "run_time": "PT0M0S"}'

snapshots["test_parsing_journey_pattern_sections 1"] = {
    "attributes": {
        "creation_date_time": None,
        "file_name": None,
        "id": "JPS95",
        "modification": None,
        "modification_date_time": None,
        "revision_number": None,
        "schema_version": None,
        "sequence_number": None,
    },
    "journey_pattern_timing_link": [
        {
            "attributes": {
                "creation_date_time": None,
                "file_name": None,
                "id": "JPTL31",
                "modification": None,
                "modification_date_time": None,
                "revision_number": None,
                "schema_version": None,
                "sequence_number": None,
            },
            "from_": {
                "activity": "pickUpAndSetDown",
                "attributes": {
                    "creation_date_time": None,
                    "file_name": None,
                    "id": "JPSU61",
                    "modification": None,
                    "modification_date_time": None,
                    "revision_number": None,
                    "schema_version": None,
                    "sequence_number": 1,
                },
                "dynamic_destination_display": "Stockton",
                "fare_stage_number": 112,
                "stop_point_ref": "077072002S",
                "timing_status": "principalTimingPoint",
            },
            "route_link_ref": "RL1",
            "run_time": "PT0M0S",
            "to_": {
                "activity": "pickUpAndSetDown",
                "attributes": {
                    "creation_date_time": None,
                    "file_name": None,
                    "id": "JPSU62",
                    "modification": None,
                    "modification_date_time": None,
                    "revision_number": None,
                    "schema_version": None,
                    "sequence_number": 2,
                },
                "dynamic_destination_display": "Stockton",
                "fare_stage_number": None,
                "stop_point_ref": "077072001X",
                "timing_status": "principalTimingPoint",
            },
        }
    ],
}
