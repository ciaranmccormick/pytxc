# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot

snapshots = Snapshot()

snapshots[
    "test_standard_service 1"
] = """{
  "attributes": null,
  "origin": "Derby",
  "destination": "Alvaston",
  "use_all_stop_points": null,
  "journey_pattern": [
    {
      "attributes": {
        "id": "jp_1",
        "file_name": null,
        "sequence_number": null,
        "creation_date_time": null,
        "modification_date_time": null,
        "modification": null,
        "revision_number": null,
        "schema_version": null
      },
      "destination_display": "Morledge",
      "direction": "outbound",
      "operator_ref": "tkt_oid",
      "route_ref": "rt_0000",
      "journey_pattern_section_refs": "js_1"
    }
  ],
  "vias": []
}"""
