# Copyright (c) 2017 pandas-gbq Authors All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

# -*- coding: utf-8 -*-

from unittest import mock

import google.cloud.bigquery
import google.cloud.bigquery.table
import packaging.version
import pytest


@pytest.fixture(autouse=True)
def default_bigquery_client(mock_bigquery_client):
    mock_query = mock.create_autospec(google.cloud.bigquery.QueryJob)
    mock_query.job_id = "some-random-id"
    mock_query.state = "DONE"
    mock_rows = mock.create_autospec(google.cloud.bigquery.table.RowIterator)
    mock_rows.total_rows = 1
    mock_rows.__iter__.return_value = [(1,)]
    mock_query.result.return_value = mock_rows
    mock_bigquery_client.list_rows.return_value = mock_rows
    mock_bigquery_client.query.return_value = mock_query
    return mock_bigquery_client


@pytest.fixture(autouse=True)
def mock_get_credentials(monkeypatch):
    import google.auth.credentials

    from pandas_gbq import auth

    mock_credentials = mock.MagicMock(google.auth.credentials.Credentials)
    mock_get_credentials = mock.Mock()
    mock_get_credentials.return_value = (mock_credentials, "my-project")

    monkeypatch.setattr(auth, "get_credentials", mock_get_credentials)
    return mock_get_credentials


def test_read_gbq_should_save_credentials(mock_get_credentials):
    import pandas_gbq

    assert pandas_gbq.context.credentials is None
    assert pandas_gbq.context.project is None

    pandas_gbq.read_gbq("SELECT 1", dialect="standard")

    assert mock_get_credentials.call_count == 1
    mock_get_credentials.reset_mock()
    assert pandas_gbq.context.credentials is not None
    assert pandas_gbq.context.project is not None

    pandas_gbq.read_gbq("SELECT 1", dialect="standard")
    mock_get_credentials.assert_not_called()


def test_read_gbq_should_use_dialect_with_query(monkeypatch, mock_bigquery_client):
    import pandas_gbq
    import pandas_gbq.features

    monkeypatch.setattr(
        pandas_gbq.features.FEATURES,
        "_bigquery_installed_version",
        packaging.version.parse(pandas_gbq.features.BIGQUERY_MINIMUM_VERSION),
    )

    assert pandas_gbq.context.dialect is None
    pandas_gbq.context.dialect = "legacy"
    pandas_gbq.read_gbq("SELECT 1")

    _, kwargs = mock_bigquery_client.query.call_args
    assert kwargs["job_config"].use_legacy_sql

    pandas_gbq.context.dialect = "standard"
    pandas_gbq.read_gbq("SELECT 1")

    _, kwargs = mock_bigquery_client.query.call_args
    assert not kwargs["job_config"].use_legacy_sql
    pandas_gbq.context.dialect = None  # Reset the global state.


def test_read_gbq_should_use_dialect_with_query_and_wait(
    monkeypatch, mock_bigquery_client
):
    if not hasattr(mock_bigquery_client, "query_and_wait"):
        pytest.skip(
            f"google-cloud-bigquery {google.cloud.bigquery.__version__} does not have query_and_wait"
        )

    import pandas_gbq
    import pandas_gbq.features

    monkeypatch.setattr(
        pandas_gbq.features.FEATURES,
        "_bigquery_installed_version",
        packaging.version.parse(pandas_gbq.features.BIGQUERY_QUERY_AND_WAIT_VERSION),
    )

    assert pandas_gbq.context.dialect is None
    pandas_gbq.context.dialect = "legacy"
    pandas_gbq.read_gbq("SELECT 1")

    _, kwargs = mock_bigquery_client.query_and_wait.call_args
    assert kwargs["job_config"].use_legacy_sql

    pandas_gbq.context.dialect = "standard"
    pandas_gbq.read_gbq("SELECT 1")

    _, kwargs = mock_bigquery_client.query_and_wait.call_args
    assert not kwargs["job_config"].use_legacy_sql
    pandas_gbq.context.dialect = None  # Reset the global state.
