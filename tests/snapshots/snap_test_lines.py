# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot

snapshots = Snapshot()

snapshots[
    "test_line 1"
] = """{
  "attributes": {
    "id": "ADER:PC1116467:8:1A",
    "file_name": null,
    "sequence_number": null,
    "creation_date_time": null,
    "modification_date_time": null,
    "modification": null,
    "revision_number": null,
    "schema_version": null
  },
  "line_name": "1A",
  "outbound_description": {
    "attributes": null,
    "origin": null,
    "destination": null,
    "description": "Derby to Alvaston"
  },
  "inbound_description": {
    "attributes": null,
    "origin": null,
    "destination": null,
    "description": "Alvaston to Derby"
  }
}"""
