# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot

snapshots = Snapshot()

snapshots[
    "test_no_header_attrs 1"
] = '{"attributes": {"id": null, "file_name": null, "sequence_number": null, "creation_date_time": null, "modification_date_time": null, "modification": null, "revision_number": null, "schema_version": null}, "stop_points": [], "route_sections": [], "routes": [], "journey_pattern_sections": [], "operators": [], "services": [], "vehicle_journeys": []}'

snapshots[
    "test_timetable_from_file_path 1"