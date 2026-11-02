# Copyright (c) 2017 pandas-gbq Authors All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from __future__ import annotations

import concurrent.futures
import datetime
from unittest import mock

import freezegun
import google.api_core.exceptions
import google.auth.exceptions
import google.cloud.bigquery
import pytest

import pandas_gbq.exceptions
import pandas_gbq.gbq
import pandas_gbq.query as module_under_test


def _make_connector(project_id: str = "some-project", **kwargs):
    return pandas_gbq.gbq.GbqConnector(project_id, **kwargs)


def test_query_and_wait_via_client_library_apierror_raises_genericgbqexception(
    mock_bigquery_client,
):
    if not hasattr(mock_bigquery_client, "query_and_wait"):
        pytest.skip(
            f"google-cloud-bigquery {google.cloud.bigquery.__version__} does not have query_and_wait"
        )

    connector = _make_connector()
    connector.client = mock_bigquery_client
    mock_bigquery_client.query_and_wait.side_effect = (
        google.api_core.exceptions.GoogleAPIError()
    )

    with pytest.raises(pandas_gbq.exceptions.GenericGBQException):
        module_under_test.query_and_wait_via_client_library(
            connector,
            mock_bigquery_client,
            "SELECT 1",
            job_config=google.cloud.bigquery.QueryJobConfig(),
            location=None,
            project_id=None,
            max_results=None,
            timeout_ms=None,
        )


def test_query_and_wait_via_client_library_refresherror_raises_accessdenied_service_account(
    mock_bigquery_client,
):
    if not hasattr(mock_bigquery_client, "query_and_wait"):
        pytest.skip(
            f"google-cloud-bigquery {google.cloud.bigquery.__version__} does not have query_and_wait"
        )

    connector = _make_connector()
    connector.private_key = "abc"
    connector.client = mock_bigquery_client
    mock_bigquery_client.query_and_wait.side_effect = (
        google.auth.exceptions.RefreshError()
    )

    with pytest.raises(pandas_gbq.exceptions.AccessDenied, match="service account"):
        module_under_test.query_and_wait_via_client_library(
            connector,
            mock_bigquery_client,
            "SELECT 1",
            job_config=google.cloud.bigquery.QueryJobConfig(),
            location=None,
            project_id=None,
            max_results=None,
            timeout_ms=None,
        )


def test_query_and_wait_via_client_library_refresherror_raises_accessdenied_user_credentials(
    mock_bigquery_client,
):
    if not hasattr(mock_bigquery_client, "query_and_wait"):
        pytest.skip(
            f"google-cloud-bigquery {google.cloud.bigquery.__version__} does not have query_and_wait"
        )

    connector = _make_connector()
    connector.client = mock_bigquery_client
    mock_bigquery_client.query_and_wait.side_effect = (
        google.auth.exceptions.RefreshError()
    )

    with pytest.raises(pandas_gbq.exceptions.AccessDenied, match="revoked or expired"):
        module_under_test.query_and_wait_via_client_library(
            connector,
            mock_bigquery_client,
            "SELECT 1",
            job_config=google.cloud.bigquery.QueryJobConfig(),
            location=None,
            project_id=None,
            max_results=None,
            timeout_ms=None,
        )


def test_query_and_wait_via_client_library_timeout_raises_querytimeout(
    mock_bigquery_client,
):
    if not hasattr(mock_bigquery_client, "query_and_wait"):
        pytest.skip(
            f"google-cloud-bigquery {google.cloud.bigquery.__version__} does not have query_and_wait"
        )

    connector = _make_connector()
    connector.client = mock_bigquery_client
    connector.start = datetime.datetime(2020, 1, 1).timestamp()

    mock_bigquery_client.query_and_wait.side_effect = concurrent.futures.TimeoutError(
        "fake timeout"
    )

    with (
        freezegun.freeze_time("2020-01-01 00:00:00", auto_tick_seconds=15),
        pytest.raises(pandas_gbq.exceptions.QueryTimeout),
    ):
        module_under_test.query_and_wait_via_client_library(
            connector,
            mock_bigquery_client,
            "SELECT 1",
            job_config=google.cloud.bigquery.QueryJobConfig(),
            location="EU",
            project_id="test-query-and-wait",
            max_results=123,
            timeout_ms=500,
        )

    mock_bigquery_client.query_and_wait.assert_called_with(
        "SELECT 1",
        job_config=mock.ANY,
        location="EU",
        project="test-query-and-wait",
        max_results=123,
        wait_timeout=0.5,
    )


@pytest.mark.parametrize(
    ["size_in_bytes", "formatted_text"],
    [
        (999, "999.0 B"),
        (1024, "1.0 KB"),
        (1099, "1.1 KB"),
        (1044480, "1020.0 KB"),
        (1048576, "1.0 MB"),
        (1048576000, "1000.0 MB"),
        (1073741824, "1.0 GB"),
        (1.099512e12, "1.0 TB"),
        (1.125900e15, "1.0 PB"),
        (1.152922e18, "1.0 EB"),
        (1.180592e21, "1.0 ZB"),
        (1.208926e24, "1.0 YB"),
        (1.208926e28, "10000.0 YB"),
    ],
)
def test_query_response_bytes(size_in_bytes, formatted_text):
    assert module_under_test.sizeof_fmt(size_in_bytes) == formatted_text


def test__wait_for_query_job_exits_when_done(mock_bigquery_client):
    connector = _make_connector()
    connector.client = mock_bigquery_client

    mock_query = mock.create_autospec(google.cloud.bigquery.QueryJob)
    type(mock_query).state = mock.PropertyMock(side_effect=("RUNNING", "DONE"))
    mock_query.result.side_effect = concurrent.futures.TimeoutError("fake timeout")

    frozen_time = datetime.datetime(2020, 1, 1)
    with freezegun.freeze_time(frozen_time, tick=False):
        # Set start time inside frozen context to ensure elapsed time is 0
        connector.start = frozen_time.timestamp()
        # Mock get_elapsed_seconds to return 0 to prevent timeout
        connector.get_elapsed_seconds = mock.Mock(return_value=0.0)
        module_under_test._wait_for_query_job(
            connector, mock_bigquery_client, mock_query, 1000
        )

    mock_bigquery_client.cancel_job.assert_not_called()


def test__wait_for_query_job_cancels_after_timeout(mock_bigquery_client):
    connector = _make_connector()
    connector.client = mock_bigquery_client
    connector.start = datetime.datetime(2020, 1, 1).timestamp()

    mock_query = mock.create_autospec(google.cloud.bigquery.QueryJob)
    mock_query.job_id = "a-random-id"
    mock_query.location = "job-location"
    mock_query.state = "RUNNING"
    mock_query.result.side_effect = concurrent.futures.TimeoutError("fake timeout")

    with (
        freezegun.freeze_time("2020-01-01 00:00:00", auto_tick_seconds=15),
        pytest.raises(pandas_gbq.exceptions.QueryTimeout),
    ):
        module_under_test._wait_for_query_job(
            connector, mock_bigquery_client, mock_query, 60
        )

    mock_bigquery_client.cancel_job.assert_called_with(
        "a-random-id", location="job-location"
    )
