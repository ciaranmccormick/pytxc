# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot

snapshots = Snapshot()

snapshots[
    "test_journey_pattern 1"
] = '{"attributes": {"id": "JP1", "file_name": null, "sequence_number": null, "creation_date_time": "2020-11-22T11:00:00", "modification_date_time": "2021-12-17T11:08:35", "modification": "revise", "revision_number": 159, "schema_version": null}, "destination_display": "Stockton High Street Stand J", "direction": "outbound", "operator_ref": "1", "route_ref": "RT40", "journey_pattern_section_refs": "JPS94"}'

snapshots[
    "test_parse_journey_pattern_timing_link 1"
] = '{"attributes": {"id": "JPTL32", "file_name": null, "sequence_number": null, "creation_date_time": null, "modification_date_time": null, "modification": null, "revision_number": null, "schema_version": null}, "from_": {"attributes": {"id": "JPSU63", "file_name": null, "sequence_number": 2, "creation_date_time": null, "modification_date_time": null, "modification": null, "revision_number": null, "schema_version": null}, "stop_point_ref": "077072001X", "activity": "pickUpAndSetDown", "dynamic_destination_display": "Stockton", "timing_status": "principalTimingPoint", "fare_stage_number": null}, "to": {"attributes": {"id": "JPSU64", "file_name": null, "sequence_number": 3, "creation_date_time": null, "modification_date_time": null, "modification": null, "revision_number": null, "schema_version": null}, "stop_point_ref": "077072405B", "activity": "pickUpAndSetDown", "dynamic_destination_display": "Stockton", "timing_status": "otherPoint", "fare_stage_number": null}, "route_link_ref": "RL2", "run_time": "PT0M0S"}'

snapshots[
    "test_parsing_journey_pattern_sections 1"
] = '{"attributes": {"id": "JPS95", "file_name": null, "sequence_number": null, "creation_date_time": null, "modification_date_time": null, "modification": null, "revision_number": null, "schema_version": null}, "journey_pattern_timing_link": [{"attributes": {"id": "JPTL31", "file_name": null, "sequence_number": null, "creation_date_time": null, "modification_date_time": null, "modification": null, "revision_number": null, "schema_version": null}, "from_": {"attributes": {"id": "JPSU61", "file_name": null, "sequence_number": 1, "creation_date_time": null, "modification_date_time": null, "modification": null, "revision_number": null, "schema_version": null}, "stop_point_ref": "077072002S", "activity": "pickUpAndSetDown", "dynamic_destination_display": "Stockton", "timing_status": "principalTimingPoint", "fare_stage_number": 112}, "to": {"attributes": {"id": "JPSU62", "file_name": null, "sequence_number": 2, "creation_date_time": null, "modification_date_time": null, "modification": null, "revision_number": null, "schema_version": null}, "stop_point_ref": "077072001X", "activity": "pickUpAndSetDown", "dynamic_destination_display": "Stockton", "timing_status": "principalTimingPoint", "fare_stage_number": null}, "route_link_ref": "RL1", "run_time": "PT0M0S"}]}'
