# Copyright (c) 2025 pandas-gbq Authors All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

import google.cloud.bigquery
import google.oauth2.credentials

import pandas_gbq


def test_sample_small_table(
    project_id: str,
    credentials: google.oauth2.credentials.Credentials,
    bigquery_client: google.cloud.bigquery.Client,
):
    # Arrange
    table_id = "bigquery-public-data.ml_datasets.penguins"
    table = bigquery_client.get_table(table_id)
    num_bytes = table.num_bytes
    num_rows = table.num_rows

    # Act
    df = pandas_gbq.sample(
        table_id,
        target_mb=1_000,
        credentials=credentials,
        billing_project_id=project_id,
    )

    # Assert
    assert num_bytes is not None and num_bytes > 0
    assert num_rows is not None and num_rows > 0
    assert df is not None and len(df.index) == num_rows


def test_sample_large_table(
    project_id: str,
    credentials: google.oauth2.credentials.Credentials,
    bigquery_client: google.cloud.bigquery.Client,
):
    # Arrange
    table_id = "bigquery-public-data.chicago_taxi_trips.taxi_trips"
    table = bigquery_client.get_table(table_id)
    num_bytes = table.num_bytes
    num_rows = table.num_rows

    # Act
    df = pandas_gbq.sample(
        table_id, target_mb=10, credentials=credentials, billing_project_id=project_id
    )

    # Assert
    assert num_bytes is not None and num_bytes > 0
    assert num_rows is not None and num_rows > 0
    assert df is not None
    rows_downloaded = len(df.index)
    assert rows_downloaded > 0
    assert rows_downloaded < num_rows
    bytes_downloaded = df.memory_usage().sum()
    assert bytes_downloaded < num_bytes


def test_sample_small_external_table(
    project_id: str,
    credentials: google.oauth2.credentials.Credentials,
    external_table: str,
):
    # Act
    df = pandas_gbq.sample(
        external_table,
        target_mb=1_000,
        credentials=credentials,
        billing_project_id=project_id,
    )

    # Assert
    assert df is not None
    rows_downloaded = len(df.index)
    assert rows_downloaded > 0


def test_sample_view(
    project_id: str,
    credentials: google.oauth2.credentials.Credentials,
):
    # Arrange
    table_id = "bigquery-public-data.ethereum_blockchain.live_contracts"

    # Act
    df = pandas_gbq.sample(
        table_id, target_mb=10, credentials=credentials, billing_project_id=project_id
    )

    # Assert
    assert df is not None
    rows_downloaded = len(df.index)
    assert rows_downloaded > 0
