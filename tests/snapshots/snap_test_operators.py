# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot

snapshots = Snapshot()

snapshots[
    "test_parsing_operators 1"
] = '{"attributes": {"id": "1", "file_name": null, "sequence_number": null, "creation_date_time": "2020-11-22T11:00:00", "modification_date_time": "2021-12-17T11:08:35", "modification": "revise", "revision_number": 159, "schema_version": null}, "national_operator_code": "SCTE", "operator_code": "SOT", "operator_short_name": "Stagecoach", "operator_name_on_licence": "Cleveland Transit Ltd", "trading_name": "Stagecoach North East", "licence_number": "PB0001987", "garages": [{"attributes": null, "garage_code": "NEBY", "garage_name": "Byker Depot", "location": {"attributes": {"id": "L1975", "file_name": null, "sequence_number": null, "creation_date_time": null, "modification_date_time": null, "modification": null, "revision_number": null, "schema_version": null}, "longitude": -1.563148, "latitude": 54.983598}}, {"attributes": null, "garage_code": "NESU", "garage_name": "Sunderland Depot", "location": {"attributes": {"id": "L1980", "file_name": null, "sequence_number": null, "creation_date_time": null, "modification_date_time": null, "modification": null, "revision_number": null, "schema_version": null}, "longitude": -1.381518, "latitude": 54.913485}}]}'

snapshots["test_parsing_operators2 1"] = {
    "attributes": {
        "creation_date_time": GenericRepr("datetime.datetime(2020, 11, 22, 11, 0)"),
        "file_name": None,
        "id": "1",
        "modification": "revise",
        "modification_date_time": GenericRepr(
            "datetime.datetime(2021, 12, 17, 11, 8, 35)"
        ),
        "revision_number": 159,
        "schema_version": None,
        "sequence_number": None,
    },
    "garages": [
        {
            "attributes": None,
            "garage_code": "NEBY",
            "garage_name": "Byker Depot",
            "location": {
                "attributes": {
                    "creation_date_time": None,
                    "file_name": None,
                    "id": "L1975",
                    "modification": None,
                    "modification_date_time": None,
                    "revision_number": None,
                    "schema_version": None,
                    "sequence_number": None,
                },
                "latitude": 54.983598,
                "longitude": -1.563148,
            },
        },
        {
            "attributes": None,
            "garage_code": "NEHA",
            "garage_name": "Hartlepool Depot",
            "location": {
                "attributes": {
                    "creation_date_time": None,
                    "file_name": None,
                    "id": "L1976",
                    "modification": None,
                    "modification_date_time": None,
                    "revision_number": None,
                    "schema_version": None,
                    "sequence_number": None,
                },
                "latitude": 54.666442,
                "longitude": -1.211364,
            },
        },
        {
            "attributes": None,
            "garage_code": "NESL",
            "garage_name": "Slatyford Depot",
            "location": {
                "attributes": {
                    "creation_date_time": None,
                    "file_name": None,
                    "id": "L1977",
                    "modification": None,
                    "modification_date_time": None,
                    "revision_number": None,
                    "schema_version": None,
                    "sequence_number": None,
                },
                "latitude": 54.989526,
                "longitude": -1.671841,
            },
        },
        {
            "attributes": None,
            "garage_code": "NESO",
            "garage_name": "South Shields Depot",
            "location": {
                "attributes": {
                    "creation_date_time": None,
                    "file_name": None,
                    "id": "L1978",
                    "modification": None,
                    "modification_date_time": None,
                    "revision_number": None,
                    "schema_version": None,
                    "sequence_number": None,
                },
                "latitude": 54.985716,
                "longitude": -1.432579,
            },
        },
        {
            "attributes": None,
            "garage_code": "NEST",
            "garage_name": "Stockton Depot",
            "location": {
                "attributes": {
                    "creation_date_time": None,
                    "file_name": None,
                    "id": "L1979",
                    "modification": None,
                    "modification_date_time": None,
                    "revision_number": None,
                    "schema_version": None,
                    "sequence_number": None,
                },
                "latitude": 54.570652,
                "longitude": -1.302515,
            },
        },
        {
            "attributes": None,
            "garage_code": "NESU",
            "garage_name": "Sunderland Depot",
            "location": {
                "attributes": {
                    "creation_date_time": None,
                    "file_name": None,
                    "id": "L1980",
                    "modification": None,
                    "modification_date_time": None,
                    "revision_number": None,
                    "schema_version": None,
                    "sequence_number": None,
                },
                "latitude": 54.913485,
                "longitude": -1.381518,
            },
        },
    ],
    "licence_number": "PB0001987",
    "national_operator_code": "SCTE",
    "operator_code": "SOT",
    "operator_name_on_licence": "Cleveland Transit Ltd",
    "operator_short_name": "Stagecoach",
    "trading_name": "Stagecoach North East",
}

snapshots[
    "test_parsing_operators_missing_elements 1"
] = '{"attributes": {"id": "1", "file_name": null, "sequence_number": null, "creation_date_time": "2020-11-22T11:00:00", "modification_date_time": "2021-12-17T11:08:35", "modification": "revise", "revision_number": 159, "schema_version": null}, "national_operator_code": "SCTE", "operator_code": null, "operator_short_name": "Stagecoach", "operator_name_on_licence": null, "trading_name": null, "licence_number": "PB0001987", "garages": []}'
