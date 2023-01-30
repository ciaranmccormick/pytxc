# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot

snapshots = Snapshot()

snapshots[
    "test_vehicle_journey 1"
] = """{
  "attributes": null,
  "departure_time": "05:12:00",
  "direction": null,
  "private_code": null,
  "vehicle_journey_code": "1001",
  "vehicle_journey_timing_link": null,
  "service_ref": "PC1116467:8",
  "line_ref": "ADER:PC1116467:8:1A",
  "journey_pattern_ref": "jp_1",
  "operator_ref": "tkt_oid"
}"""
