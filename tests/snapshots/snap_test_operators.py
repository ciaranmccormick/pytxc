# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot

snapshots = Snapshot()

snapshots[
    "test_parsing_operators 1"
] = """{
  "attributes": {
    "id": "1",
    "file_name": null,
    "sequence_number": null,
    "creation_date_time": "2020-11-22T11:00:00",
    "modification_date_time": "2021-12-17T11:08:35",
    "modification": "revise",
    "revision_number": 159,
    "schema_version": null
  },
  "national_operator_code": "SCTE",
  "operator_code": "SOT",
  "operator_short_name": "Stagecoach",
  "operator_name_on_licence": "Cleveland Transit Ltd",
  "trading_name": "Stagecoach North East",
  "licence_number": "PB0001987",
  "garages": [
    {
      "attributes": null,
      "garage_code": "NEBY",
      "garage_name": "Byker Depot",
      "location": {
        "attributes": {
          "id": "L1975",
          "file_name": null,
          "sequence_number": null,
          "creation_date_time": null,
          "modification_date_time": null,
          "modification": null,
          "revision_number": null,
          "schema_version": null
        },
        "longitude": -1.563148,
        "latitude": 54.983598
      }
    },
    {
      "attributes": null,
      "garage_code": "NESU",
      "garage_name": "Sunderland Depot",
      "location": {
        "attributes": {
          "id": "L1980",
          "file_name": null,
          "sequence_number": null,
          "creation_date_time": null,
          "modification_date_time": null,
          "modification": null,
          "revision_number": null,
          "schema_version": null
        },
        "longitude": -1.381518,
        "latitude": 54.913485
      }
    }
  ]
}"""

snapshots[
    "test_parsing_operators_missing_elements 1"
] = """{
  "attributes": {
    "id": "1",
    "file_name": null,
    "sequence_number": null,
    "creation_date_time": "2020-11-22T11:00:00",
    "modification_date_time": "2021-12-17T11:08:35",
    "modification": "revise",
    "revision_number": 159,
    "schema_version": null
  },
  "national_operator_code": "SCTE",
  "operator_code": null,
  "operator_short_name": "Stagecoach",
  "operator_name_on_licence": null,
  "trading_name": null,
  "licence_number": "PB0001987",
  "garages": []
}"""
