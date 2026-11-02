# Copyright (c) 2017 pandas-gbq Authors All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

import collections
from unittest import mock

import google.cloud.bigquery

from pandas_gbq.core import biglake, resource_references


def test_get_table_metadata(mock_bigquery_client):
    reference = resource_references.BigLakeTableId(
        "my-project", "my-catalog", ("my-schema",), "my-table"
    )
    schema = [
        google.cloud.bigquery.SchemaField("col1", "STRING"),
    ]
    job_mock = mock.create_autospec(google.cloud.bigquery.QueryJob)
    job_mock.schema = schema
    mock_bigquery_client.query.return_value = job_mock
    Row = collections.namedtuple("Row", ["total_rows"])
    mock_bigquery_client.query_and_wait.return_value = [Row(total_rows=123)]

    metadata = biglake.get_table_metadata(
        reference=reference, bqclient=mock_bigquery_client
    )

    assert metadata.schema == schema
    assert metadata.num_rows == 123
    mock_bigquery_client.query.assert_called_once()
    mock_bigquery_client.query_and_wait.assert_called_once()


def test_get_table_metadata_no_schema(mock_bigquery_client):
    reference = resource_references.BigLakeTableId(
        "my-project", "my-catalog", ("my-schema",), "my-table"
    )
    job_mock = mock.create_autospec(google.cloud.bigquery.QueryJob)
    job_mock.schema = None
    mock_bigquery_client.query.return_value = job_mock
    Row = collections.namedtuple("Row", ["total_rows"])
    mock_bigquery_client.query_and_wait.return_value = [Row(total_rows=456)]

    metadata = biglake.get_table_metadata(
        reference=reference, bqclient=mock_bigquery_client
    )

    assert metadata.schema == []
    assert metadata.num_rows == 456
    mock_bigquery_client.query.assert_called_once()
    mock_bigquery_client.query_and_wait.assert_called_once()
