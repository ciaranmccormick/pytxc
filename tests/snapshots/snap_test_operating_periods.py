# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot

snapshots = Snapshot()

snapshots[
    "test_operating_period 1"
] = """{
  "attributes": null,
  "start_date": "2023-01-03",
  "end_date": null
}"""
