# Copyright (c) 2017 pandas-gbq Authors All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

"""System tests for read_gbq using the BigQuery Storage API."""

import functools
import uuid

import pytest

pytest.importorskip("google.cloud.bigquery", minversion="1.24.0")


@pytest.fixture
def method_under_test(project_id, credentials):
    import pandas_gbq

    return functools.partial(
        pandas_gbq.read_gbq, project_id=project_id, credentials=credentials
    )


@pytest.mark.parametrize(
    "query_string",
    (
        ("SELECT * FROM (SELECT 1) WHERE TRUE = FALSE;"),
        (
            "SELECT * FROM (SELECT TIMESTAMP('2020-02-11 16:33:32-06:00')) WHERE TRUE = FALSE;"
        ),
    ),
)
def test_empty_results(method_under_test, query_string):
    """Test with an empty dataframe.

    See: https://github.com/pydata/pandas-gbq/issues/299
    """
    df = method_under_test(
        query_string,
        use_bqstorage_api=True,
    )
    assert len(df.index) == 0


def test_large_results(random_dataset, method_under_test):
    df = method_under_test(
        """
        SELECT
          total_amount,
          passenger_count,
          trip_distance
        FROM `bigquery-public-data.new_york.tlc_green_trips_2014`
        -- Select non-null rows for no-copy conversion from Arrow to pandas.
        WHERE total_amount IS NOT NULL
          AND passenger_count IS NOT NULL
          AND trip_distance IS NOT NULL
        LIMIT 10000000
        """,
        use_bqstorage_api=True,
        configuration={
            "query": {
                "destinationTable": {
                    "projectId": random_dataset.project,
                    "datasetId": random_dataset.dataset_id,
                    "tableId": "".join(
                        [
                            "test_read_gbq_w_bqstorage_api_",
                            str(uuid.uuid4()).replace("-", "_"),
                        ]
                    ),
                },
                "writeDisposition": "WRITE_TRUNCATE",
            }
        },
    )
    assert len(df) == 10000000
