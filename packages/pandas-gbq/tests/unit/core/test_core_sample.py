# Copyright (c) 2026 pandas-gbq Authors All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from typing import Sequence
from unittest import mock

import google.cloud.bigquery
import google.cloud.bigquery.table
import pytest

import pandas_gbq.constants
import pandas_gbq.core.sample


@pytest.mark.parametrize(
    "schema, expected_size",
    [
        pytest.param(
            [
                google.cloud.bigquery.SchemaField("id", "INT64"),  # 8
                google.cloud.bigquery.SchemaField("is_valid", "BOOL"),  # 1
                google.cloud.bigquery.SchemaField("price", "NUMERIC"),  # 16
                google.cloud.bigquery.SchemaField("big_value", "BIGNUMERIC"),  # 32
            ],
            8 + 1 + 16 + 32,  # 57
            id="Fixed_Size_Types",
        ),
        pytest.param(
            [
                google.cloud.bigquery.SchemaField(
                    "coords",
                    "RECORD",
                    fields=[
                        google.cloud.bigquery.SchemaField("lat", "FLOAT64"),  # 8
                        google.cloud.bigquery.SchemaField("lon", "FLOAT64"),  # 8
                    ],
                ),
            ],
            16,  # 8 + 8
            id="Simple_Struct",
        ),
        pytest.param(
            [
                google.cloud.bigquery.SchemaField(
                    "history", "TIMESTAMP", mode="REPEATED"
                ),  # 5 * 8
            ],
            pandas_gbq.core.sample._ARRAY_LENGTH_ESTIMATE * 8,  # 40
            id="Simple_Array",
        ),
        pytest.param(
            [
                google.cloud.bigquery.SchemaField(
                    "addresses",
                    "RECORD",
                    mode="REPEATED",
                    fields=[
                        google.cloud.bigquery.SchemaField("street", "STRING"),  # 1KIB
                        google.cloud.bigquery.SchemaField("zip", "INT64"),  # 8
                    ],
                ),
            ],
            pandas_gbq.core.sample._ARRAY_LENGTH_ESTIMATE
            * (pandas_gbq.constants.BYTES_IN_KIB + 8),
            id="Repeated_Struct",
        ),
        pytest.param(
            [
                google.cloud.bigquery.SchemaField(
                    "empty_struct", "RECORD", fields=[]
                ),  # 0
                google.cloud.bigquery.SchemaField("simple_int", "INT64"),  # 8
            ],
            9,  # 1 + 8
            id="empty-struct",
        ),
        # Case 8: Complex Mix (Combining multiple cases)
        pytest.param(
            [
                google.cloud.bigquery.SchemaField("key", "INT64"),  # 8
                google.cloud.bigquery.SchemaField("notes", "STRING"),  # 1KIB
                google.cloud.bigquery.SchemaField(
                    "history", "TIMESTAMP", mode="REPEATED"
                ),  # 40
                google.cloud.bigquery.SchemaField(
                    "details",
                    "RECORD",
                    fields=[
                        google.cloud.bigquery.SchemaField("d1", "NUMERIC"),  # 16
                        google.cloud.bigquery.SchemaField("d2", "BYTES"),  # 1MB
                    ],
                ),
            ],
            8
            + pandas_gbq.constants.BYTES_IN_KIB
            + 40
            + (16 + pandas_gbq.constants.BYTES_IN_MIB),
            id="Complex_Mix",
        ),
    ],
)
def test_estimate_row_size_parametrized(
    schema: Sequence[google.cloud.bigquery.SchemaField], expected_size: int
):
    actual_size = pandas_gbq.core.sample._estimate_row_bytes(schema)
    assert actual_size == expected_size


def test_calculate_target_bytes_with_target_mb():
    target_mb = 200
    expected_bytes = target_mb * pandas_gbq.constants.BYTES_IN_MIB
    actual_bytes = pandas_gbq.core.sample._calculate_target_bytes(target_mb)
    assert actual_bytes == expected_bytes


@mock.patch("psutil.virtual_memory")
def test_calculate_target_bytes_with_available_memory(mock_virtual_memory):
    # Mock psutil.virtual_memory to return a mock object with an 'available' attribute.
    available_memory = 2 * pandas_gbq.constants.BYTES_IN_GIB  # 2 GB
    mock_virtual_memory.return_value = mock.Mock(available=available_memory)

    # Expected bytes is available memory / 4.
    expected_bytes = available_memory // 4
    actual_bytes = pandas_gbq.core.sample._calculate_target_bytes(None)
    assert actual_bytes == expected_bytes


@mock.patch("psutil.virtual_memory")
def test_calculate_target_bytes_low_memory(mock_virtual_memory):
    # Mock psutil.virtual_memory to return a mock object with an 'available' attribute.
    # Set available memory to a low value.
    available_memory = 100  # 100 bytes
    mock_virtual_memory.return_value = mock.Mock(available=available_memory)

    # Expected bytes should be low value // 4.
    expected_bytes = 25
    actual_bytes = pandas_gbq.core.sample._calculate_target_bytes(None)
    assert actual_bytes == expected_bytes


@mock.patch("psutil.virtual_memory")
def test_calculate_target_bytes_caps_at_max_auto_target_bytes(mock_virtual_memory):
    # Mock psutil.virtual_memory to return a mock object with an 'available' attribute.
    # Set available memory to a high value (e.g., 8 GB) so that available // 4 > _MAX_AUTO_TARGET_BYTES.
    available_memory = 8 * pandas_gbq.constants.BYTES_IN_GIB  # 8 GB
    mock_virtual_memory.return_value = mock.Mock(available=available_memory)

    # Expected bytes should be _MAX_AUTO_TARGET_BYTES (1 GiB) because available // 4 (2 GiB) is capped.
    expected_bytes = pandas_gbq.core.sample._MAX_AUTO_TARGET_BYTES
    actual_bytes = pandas_gbq.core.sample._calculate_target_bytes(None)
    assert actual_bytes == expected_bytes


@pytest.mark.parametrize(
    "target_bytes, table_bytes, table_rows, fields, expected_limit",
    [
        # With table_bytes and table_rows, should use proportion
        pytest.param(
            1000, 10000, 100, [], 10, id="with-stats-simple"
        ),  # 100 * (1000/10000)
        pytest.param(1, 10000, 100, [], 1, id="with-stats-min-1"),  # min is 1
        # Without stats, should estimate from schema
        pytest.param(
            1000,
            None,
            None,
            [google.cloud.bigquery.SchemaField("col1", "INT64")],  # 8 bytes
            125,  # 1000 // 8
            id="no-stats-simple",
        ),
        pytest.param(
            10,
            None,
            None,
            [google.cloud.bigquery.SchemaField("col1", "NUMERIC")],  # 16 bytes
            1,  # max(1, 10 // 16)
            id="no-stats-min-1",
        ),
        # Edge case: row_bytes_estimate is 0
        pytest.param(
            1000,
            None,
            None,
            [],
            1000,
            id="no-stats-zero-row-size",  # empty schema -> 0 bytes
        ),
    ],
)
def test_estimate_limit(target_bytes, table_bytes, table_rows, fields, expected_limit):
    limit = pandas_gbq.core.sample._estimate_limit(
        target_bytes=target_bytes,
        table_bytes=table_bytes,
        table_rows=table_rows,
        fields=fields,
    )
    assert limit == expected_limit


@mock.patch("pandas_gbq.core.read.download_results")
def test_download_results_in_parallel_with_table(
    mock_download_results, mock_bigquery_client
):
    rows = mock.Mock(spec=google.cloud.bigquery.table.RowIterator)
    rows._table = "table"
    rows._schema = "schema"
    pandas_gbq.core.sample._download_results_in_parallel(
        rows, bqclient=mock_bigquery_client
    )
    mock_bigquery_client.list_rows.assert_called_once_with(
        "table", selected_fields="schema"
    )
    mock_download_results.assert_called_once()


@mock.patch("pandas_gbq.core.read.download_results")
def test_download_results_in_parallel_no_table(
    mock_download_results, mock_bigquery_client
):
    rows = mock.Mock(spec=google.cloud.bigquery.table.RowIterator)
    rows._table = None
    rows._schema = None
    pandas_gbq.core.sample._download_results_in_parallel(
        rows, bqclient=mock_bigquery_client
    )
    mock_bigquery_client.list_rows.assert_not_called()
    mock_download_results.assert_called_once_with(
        rows,
        bqclient=mock_bigquery_client,
        progress_bar_type=None,
        warn_on_large_results=False,
        max_results=None,
        user_dtypes=None,
        use_bqstorage_api=True,
    )


@mock.patch("pandas_gbq.core.sample._download_results_in_parallel")
def test_sample_with_tablesample(
    mock_download_results_in_parallel, mock_bigquery_client
):
    proportion = 0.1
    target_row_count = 100

    pandas_gbq.core.sample._sample_with_tablesample(
        "test-project.test_dataset.test_table",
        bqclient=mock_bigquery_client,
        proportion=proportion,
        target_row_count=target_row_count,
    )

    mock_bigquery_client.query_and_wait.assert_called_once()
    query = mock_bigquery_client.query_and_wait.call_args[0][0]
    assert "TABLESAMPLE SYSTEM (10 PERCENT)" in query
    assert "LIMIT 100" in query
    assert "FROM `test-project.test_dataset.test_table`" in query

    # The mock for query_and_wait returns a mock RowIterator, which is then
    # passed to _download_results_in_parallel.
    mock_results = mock_bigquery_client.query_and_wait.return_value
    mock_download_results_in_parallel.assert_called_with(
        mock_results,
        bqclient=mock_bigquery_client,
        progress_bar_type=None,
        use_bqstorage_api=True,
    )


@mock.patch("pandas_gbq.core.sample._download_results_in_parallel")
def test_sample_with_limit(mock_download_results_in_parallel, mock_bigquery_client):
    target_row_count = 200

    pandas_gbq.core.sample._sample_with_limit(
        "test-project.test_dataset.test_table",
        bqclient=mock_bigquery_client,
        target_row_count=target_row_count,
    )

    mock_bigquery_client.query_and_wait.assert_called_once()
    query = mock_bigquery_client.query_and_wait.call_args[0][0]
    assert "TABLESAMPLE" not in query
    assert "LIMIT 200" in query
    assert "FROM `test-project.test_dataset.test_table`" in query

    # The mock for query_and_wait returns a mock RowIterator, which is then
    # passed to _download_results_in_parallel.
    mock_results = mock_bigquery_client.query_and_wait.return_value
    mock_download_results_in_parallel.assert_called_with(
        mock_results,
        bqclient=mock_bigquery_client,
        progress_bar_type=None,
        use_bqstorage_api=True,
    )


@pytest.fixture
def mock_gbq_connector(mock_bigquery_client):
    with mock.patch("pandas_gbq.gbq_connector.GbqConnector") as mock_connector_class:
        mock_connector = mock_connector_class.return_value
        mock_connector.get_client.return_value = mock_bigquery_client
        mock_connector.credentials = mock.Mock()
        yield mock_connector


@mock.patch("pandas_gbq.core.biglake.get_table_metadata")
@mock.patch("pandas_gbq.core.sample._sample_with_tablesample")
def test_sample_biglake_table(
    mock_sample_with_tablesample,
    mock_get_table_metadata,
    mock_gbq_connector,
    mock_bigquery_client,
):
    mock_metadata = mock.Mock()
    mock_metadata.num_rows = 1000
    mock_metadata.schema = [google.cloud.bigquery.SchemaField("col1", "INT64")]
    mock_get_table_metadata.return_value = mock_metadata
    table_id = "p.c.d.t"

    with mock.patch(
        "pandas_gbq.core.sample._calculate_target_bytes", return_value=1000
    ):
        pandas_gbq.core.sample.sample(table_id, billing_project_id="p")

    mock_sample_with_tablesample.assert_called_once()
    # 1000 target bytes / 8 bytes/row in schema = 125 target_row_count
    # 125 / 1000 rows = 0.125 proportion.
    # min(100, max(1, 0.125 * 100)) = 12.5 -> 12
    # So proportion should be about 0.125
    # Let's check the args
    args, kwargs = mock_sample_with_tablesample.call_args
    assert kwargs["proportion"] > 0.1
    assert kwargs["target_row_count"] == 125


@mock.patch("pandas_gbq.core.biglake.get_table_metadata")
@mock.patch("pandas_gbq.core.sample._sample_with_tablesample")
def test_sample_biglake_table_zero_rows(
    mock_sample_with_tablesample,
    mock_get_table_metadata,
    mock_gbq_connector,
    mock_bigquery_client,
):
    mock_metadata = mock.Mock()
    mock_metadata.num_rows = 0
    mock_metadata.schema = [google.cloud.bigquery.SchemaField("col1", "INT64")]
    mock_get_table_metadata.return_value = mock_metadata
    table_id = "p.c.d.t"

    with mock.patch(
        "pandas_gbq.core.sample._calculate_target_bytes", return_value=1000
    ):
        pandas_gbq.core.sample.sample(table_id, billing_project_id="p")

    mock_sample_with_tablesample.assert_called_once()
    args, kwargs = mock_sample_with_tablesample.call_args
    # Avoid division by zero
    assert kwargs["proportion"] > 0.0


@mock.patch("pandas_gbq.core.read.download_results")
def test_sample_small_table_downloads_all(
    mock_download_results, mock_gbq_connector, mock_bigquery_client
):
    mock_table = mock.Mock(spec=google.cloud.bigquery.Table)
    type(mock_table).table_type = "TABLE"
    type(mock_table).num_bytes = 1000
    type(mock_table).num_rows = 10
    type(mock_table).schema = []
    mock_bigquery_client.get_table.return_value = mock_table

    with mock.patch(
        "pandas_gbq.core.sample._calculate_target_bytes", return_value=2000
    ):
        pandas_gbq.core.sample.sample("my-project.my_dataset.my_table")

    mock_bigquery_client.list_rows.assert_called_once_with(mock_table)
    mock_download_results.assert_called_once()
    # Check that we didn't try to run a query for sampling
    mock_bigquery_client.query_and_wait.assert_not_called()


@mock.patch("pandas_gbq.core.sample._sample_with_tablesample")
def test_sample_uses_tablesample(
    mock_sample_with_tablesample, mock_gbq_connector, mock_bigquery_client
):
    mock_table = mock.Mock(spec=google.cloud.bigquery.Table)
    type(mock_table).project = "my-project"
    type(mock_table).dataset_id = "my_dataset"
    type(mock_table).table_id = "my_table"
    type(mock_table).table_type = "TABLE"
    type(mock_table).num_bytes = 1_000_000_000_000
    type(mock_table).num_rows = 1_000
    type(mock_table).schema = [google.cloud.bigquery.SchemaField("col1", "INT64")]
    mock_bigquery_client.get_table.return_value = mock_table

    pandas_gbq.core.sample.sample("my-project.my_dataset.my_table", target_mb=1)

    mock_sample_with_tablesample.assert_called_once()


@mock.patch("pandas_gbq.core.sample._sample_with_limit")
def test_sample_uses_limit_fallback(
    mock_sample_with_limit, mock_gbq_connector, mock_bigquery_client
):
    mock_table = mock.Mock(spec=google.cloud.bigquery.Table)
    mock_table.project = "my-project"
    mock_table.dataset_id = "my_dataset"
    mock_table.table_id = "my_table"
    mock_table.num_bytes = 10000
    mock_table.num_rows = 100
    mock_table.table_type = "VIEW"  # Not eligible for TABLESAMPLE
    mock_table.schema = [google.cloud.bigquery.SchemaField("col1", "INT64")]
    mock_bigquery_client.get_table.return_value = mock_table

    with mock.patch(
        "pandas_gbq.core.sample._calculate_target_bytes", return_value=1000
    ):
        pandas_gbq.core.sample.sample("my-project.my_dataset.my_table")

    mock_sample_with_limit.assert_called_once()


@mock.patch("pandas_gbq.core.sample._sample_with_limit")
def test_sample_uses_limit_fallback_no_bytes(
    mock_sample_with_limit, mock_gbq_connector, mock_bigquery_client
):
    mock_table = mock.Mock(spec=google.cloud.bigquery.Table)
    mock_table.project = "my-project"
    mock_table.dataset_id = "my_dataset"
    mock_table.table_id = "my_table"
    mock_table.num_bytes = None  # num_bytes can be None
    mock_table.num_rows = 100
    mock_table.table_type = "TABLE"
    mock_table.schema = [google.cloud.bigquery.SchemaField("col1", "INT64")]
    mock_bigquery_client.get_table.return_value = mock_table

    with mock.patch(
        "pandas_gbq.core.sample._calculate_target_bytes", return_value=1000
    ):
        pandas_gbq.core.sample.sample("my-project.my_dataset.my_table")

    mock_sample_with_limit.assert_called_once()
