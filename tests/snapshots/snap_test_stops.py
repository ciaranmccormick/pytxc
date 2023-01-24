# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot

snapshots = Snapshot()

snapshots[
    "test_loading_annotated_stop_point_refs 1"
] = '{"attributes": null, "common_name": "High Street Stand S", "stop_point_ref": "077072002S"}'

snapshots[
    "test_no_common_name 1"
] = '{"attributes": null, "common_name": null, "stop_point_ref": "077072002S"}'
