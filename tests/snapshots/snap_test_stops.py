# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot

snapshots = Snapshot()

snapshots[
    "test_loading_annotated_stop_point_refs 1"
] = """{
  "attributes": null,
  "common_name": "High Street Stand S",
  "stop_point_ref": "077072002S",
  "location": null
}"""

snapshots[
    "test_no_common_name 1"
] = """{
  "attributes": null,
  "common_name": null,
  "stop_point_ref": "077072002S",
  "location": null
}"""

snapshots[
    "test_stops_with_location 1"
] = """{
  "attributes": null,
  "common_name": "Roundhouse Road",
  "stop_point_ref": "109000009362",
  "location": {
    "attributes": null,
    "longitude": -1.458709,
    "latitude": 52.916994
  }
}"""
