# Copyright (c) 2025 pandas-gbq Authors All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from unittest import mock

import pandas
import pandas.testing
from google.cloud import bigquery

from pandas_gbq import dry_runs


def test_get_query_stats():
    mock_query_job = mock.create_autospec(bigquery.QueryJob)
    total_bytes_processed = 15
    mock_query_job._properties = {
        "kind": "bigquery#job",
        "etag": "e-tag",
        "id": "id",
        "selfLink": "self-link",
        "user_email": "user-emial",
        "configuration": {
            "query": {
                "query": "SELECT * FROM `test_table`",
                "destinationTable": {
                    "projectId": "project-id",
                    "datasetId": "dataset-id",
                    "tableId": "table-id",
                },
                "writeDisposition": "WRITE_TRUNCATE",
                "priority": "INTERACTIVE",
                "useLegacySql": False,
            },
            "jobType": "QUERY",
        },
        "jobReference": {
            "projectId": "project-id",
            "jobId": "job-id",
            "location": "US",
        },
        "statistics": {
            "creationTime": 1767037135155.0,
            "startTime": 1767037135238.0,
            "endTime": 1767037135353.0,
            "totalBytesProcessed": f"{total_bytes_processed}",
            "query": {
                "totalBytesProcessed": f"{total_bytes_processed}",
                "totalBytesBilled": "0",
                "cacheHit": True,
                "statementType": "SELECT",
            },
            "reservation_id": "reservation_id",
            "edition": "ENTERPRISE",
            "reservationGroupPath": [""],
        },
        "status": {"state": "DONE"},
        "principal_subject": "principal_subject",
        "jobCreationReason": {"code": "REQUESTED"},
    }
    expected_index = pandas.Index(
        [
            "bigquerySchema",
            "projectId",
            "jobId",
            "location",
            "jobType",
            "dispatchedSql",
            "destinationTable",
            "useLegacySql",
            "referencedTables",
            "totalBytesProcessed",
            "cacheHit",
            "statementType",
            "creationTime",
        ]
    )

    result = dry_runs.get_query_stats(mock_query_job)

    assert isinstance(result, pandas.Series)
    pandas.testing.assert_index_equal(expected_index, result.index)
    assert result["totalBytesProcessed"] == total_bytes_processed


def test_get_query_stats_missing_bytes_use_zero():
    mock_query_job = mock.create_autospec(bigquery.QueryJob)
    mock_query_job._properties = {
        "kind": "bigquery#job",
        "etag": "e-tag",
        "id": "id",
        "selfLink": "self-link",
        "user_email": "user-emial",
        "configuration": {
            "query": {
                "query": "SELECT * FROM `test_table`",
                "destinationTable": {
                    "projectId": "project-id",
                    "datasetId": "dataset-id",
                    "tableId": "table-id",
                },
                "writeDisposition": "WRITE_TRUNCATE",
                "priority": "INTERACTIVE",
                "useLegacySql": False,
            },
            "jobType": "QUERY",
        },
        "jobReference": {
            "projectId": "project-id",
            "jobId": "job-id",
            "location": "US",
        },
        "statistics": {
            "creationTime": 1767037135155.0,
            "startTime": 1767037135238.0,
            "endTime": 1767037135353.0,
            "query": {
                "cacheHit": True,
                "statementType": "SELECT",
            },
            "reservation_id": "reservation_id",
            "edition": "ENTERPRISE",
            "reservationGroupPath": [""],
        },
        "status": {"state": "DONE"},
        "principal_subject": "principal_subject",
        "jobCreationReason": {"code": "REQUESTED"},
    }
    expected_index = pandas.Index(
        [
            "bigquerySchema",
            "projectId",
            "jobId",
            "location",
            "jobType",
            "dispatchedSql",
            "destinationTable",
            "useLegacySql",
            "referencedTables",
            "totalBytesProcessed",
            "cacheHit",
            "statementType",
            "creationTime",
        ]
    )

    result = dry_runs.get_query_stats(mock_query_job)

    assert isinstance(result, pandas.Series)
    pandas.testing.assert_index_equal(expected_index, result.index)
    assert result["totalBytesProcessed"] == 0
