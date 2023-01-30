# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot

snapshots = Snapshot()

snapshots[
    "test_parase_route_section 1"
] = """{
  "attributes": {
    "id": "RS1",
    "file_name": null,
    "sequence_number": null,
    "creation_date_time": null,
    "modification_date_time": null,
    "modification": null,
    "revision_number": null,
    "schema_version": null
  },
  "route_link": [
    {
      "attributes": {
        "id": "RL113",
        "file_name": null,
        "sequence_number": null,
        "creation_date_time": "2020-11-22T11:00:00",
        "modification_date_time": "2021-12-17T11:08:35",
        "modification": "revise",
        "revision_number": 159,
        "schema_version": null
      },
      "from_": {
        "attributes": null,
        "stop_point_ref": "077072746A",
        "activity": null,
        "dynamic_destination_display": null,
        "timing_status": null,
        "fare_stage_number": null
      },
      "to": {
        "attributes": null,
        "stop_point_ref": "077072574B",
        "activity": null,
        "dynamic_destination_display": null,
        "timing_status": null,
        "fare_stage_number": null
      },
      "distance": 696,
      "track": null
    },
    {
      "attributes": {
        "id": "RL2",
        "file_name": null,
        "sequence_number": null,
        "creation_date_time": "2020-11-22T11:00:00",
        "modification_date_time": "2021-12-17T11:08:35",
        "modification": "revise",
        "revision_number": 159,
        "schema_version": null
      },
      "from_": {
        "attributes": null,
        "stop_point_ref": "077072001X",
        "activity": null,
        "dynamic_destination_display": null,
        "timing_status": null,
        "fare_stage_number": null
      },
      "to": {
        "attributes": null,
        "stop_point_ref": "077072405B",
        "activity": null,
        "dynamic_destination_display": null,
        "timing_status": null,
        "fare_stage_number": null
      },
      "distance": 172,
      "track": null
    }
  ]
}"""

snapshots[
    "test_parse_route 1"
] = """{
  "attributes": {
    "id": "RT39",
    "file_name": null,
    "sequence_number": null,
    "creation_date_time": "2020-11-22T11:00:00",
    "modification_date_time": "2021-12-17T11:08:35",
    "modification": "revise",
    "revision_number": 159,
    "schema_version": null
  },
  "private_code": "35st-39",
  "description": "Stockton - Wolviston Court",
  "route_section_ref": "RS1"
}"""

snapshots[
    "test_parse_route_link_no_mapping 1"
] = """{
  "attributes": {
    "id": "RL113",
    "file_name": null,
    "sequence_number": null,
    "creation_date_time": "2020-11-22T11:00:00",
    "modification_date_time": "2021-12-17T11:08:35",
    "modification": "revise",
    "revision_number": 159,
    "schema_version": null
  },
  "from_": {
    "attributes": null,
    "stop_point_ref": "077072746A",
    "activity": null,
    "dynamic_destination_display": null,
    "timing_status": null,
    "fare_stage_number": null
  },
  "to": {
    "attributes": null,
    "stop_point_ref": "077072574B",
    "activity": null,
    "dynamic_destination_display": null,
    "timing_status": null,
    "fare_stage_number": null
  },
  "distance": 696,
  "track": null
}"""

snapshots[
    "test_parse_route_no_description 1"
] = """{
  "attributes": {
    "id": "RT39",
    "file_name": null,
    "sequence_number": null,
    "creation_date_time": "2020-11-22T11:00:00",
    "modification_date_time": "2021-12-17T11:08:35",
    "modification": "revise",
    "revision_number": 159,
    "schema_version": null
  },
  "private_code": "35st-39",
  "description": null,
  "route_section_ref": "RS1"
}"""
