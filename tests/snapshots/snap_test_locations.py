# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot

snapshots = Snapshot()

snapshots["test_mapping_to_geojson 1"] = {
    "coordinates": (
        (-1.312878, 54.562472),
        (-1.312975, 54.562465),
        (-1.312974, 54.562492),
        (-1.31297, 54.562599),
    ),
    "type": "LineString",
}

snapshots[
    "test_parsing_track 1"
] = """{
  "attributes": null,
  "mapping": {
    "attributes": null,
    "location": [
      {
        "attributes": {
          "id": "L1",
          "file_name": null,
          "sequence_number": null,
          "creation_date_time": null,
          "modification_date_time": null,
          "modification": null,
          "revision_number": null,
          "schema_version": null
        },
        "longitude": -1.312878,
        "latitude": 54.562472
      },
      {
        "attributes": {
          "id": "L2",
          "file_name": null,
          "sequence_number": null,
          "creation_date_time": null,
          "modification_date_time": null,
          "modification": null,
          "revision_number": null,
          "schema_version": null
        },
        "longitude": -1.312975,
        "latitude": 54.562465
      },
      {
        "attributes": {
          "id": "L3",
          "file_name": null,
          "sequence_number": null,
          "creation_date_time": null,
          "modification_date_time": null,
          "modification": null,
          "revision_number": null,
          "schema_version": null
        },
        "longitude": -1.312974,
        "latitude": 54.562492
      },
      {
        "attributes": {
          "id": "L4",
          "file_name": null,
          "sequence_number": null,
          "creation_date_time": null,
          "modification_date_time": null,
          "modification": null,
          "revision_number": null,
          "schema_version": null
        },
        "longitude": -1.31297,
        "latitude": 54.562599
      }
    ]
  }
}"""
