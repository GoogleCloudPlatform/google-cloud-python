# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from typing import Any, Dict, Optional
from unittest import mock

import google.api_core.exceptions
from google.api_core import retry as retries
import pytest

from google.cloud.bigquery import _arrow_query
from google.cloud.bigquery import _job_helpers
from google.cloud.bigquery import enums
from google.cloud.bigquery import retry
from google.cloud.bigquery.client import Client
from google.cloud.bigquery.job import copy_ as job_copy
from google.cloud.bigquery.job import extract as job_extract
from google.cloud.bigquery.job import load as job_load
from google.cloud.bigquery.job import query as job_query
from google.cloud.bigquery.query import ConnectionProperty, ScalarQueryParameter

from .helpers import make_client, make_connection


def make_query_request(additional_properties: Optional[Dict[str, Any]] = None):
    request = {"useLegacySql": False, "formatOptions": {"useInt64Timestamp": True}}
    if additional_properties is not None:
        request.update(additional_properties)
    return request


def make_query_response(
    completed: bool = False,
    job_id: str = "abcd-efg-hijk-lmnop",
    location="US",
    project_id="test-project",
    errors=None,
) -> Dict[str, Any]:
    response = {
        "jobReference": {
            "projectId": project_id,
            "jobId": job_id,
            "location": location,
        },
        "jobComplete": completed,
    }
    if errors is not None:
        response["errors"] = errors
    return response


@pytest.mark.parametrize(
    ("job_config", "expected"),
    (
        pytest.param(
            None,
            make_query_request(),
            id="job_config=None-default-request",
        ),
        pytest.param(
            job_query.QueryJobConfig(),
            make_query_request(),
            id="job_config=QueryJobConfig()-default-request",
        ),
        pytest.param(
            job_query.QueryJobConfig.from_api_repr(
                {
                    "unknownTopLevelProperty": "some-test-value",
                    "query": {
                        "unknownQueryProperty": "some-other-value",
                    },
                },
            ),
            make_query_request(
                {
                    "unknownTopLevelProperty": "some-test-value",
                    "unknownQueryProperty": "some-other-value",
                }
            ),
            id="job_config-with-unknown-properties-includes-all-properties-in-request",
        ),
        pytest.param(
            job_query.QueryJobConfig(default_dataset="my-project.my_dataset"),
            make_query_request(
                {
                    "defaultDataset": {
                        "projectId": "my-project",
                        "datasetId": "my_dataset",
                    }
                }
            ),
            id="job_config-with-default_dataset",
        ),
        pytest.param(
            job_query.QueryJobConfig(dry_run=True),
            make_query_request({"dryRun": True}),
            id="job_config-with-dry_run",
        ),
        pytest.param(
            job_query.QueryJobConfig(use_query_cache=False),
            make_query_request({"useQueryCache": False}),
            id="job_config-with-use_query_cache",
        ),
        pytest.param(
            job_query.QueryJobConfig(use_legacy_sql=True),
            make_query_request({"useLegacySql": True}),
            id="job_config-with-use_legacy_sql",
        ),
        pytest.param(
            job_query.QueryJobConfig(
                query_parameters=[
                    ScalarQueryParameter("named_param1", "STRING", "param-value"),
                    ScalarQueryParameter("named_param2", "INT64", 123),
                ]
            ),
            make_query_request(
                {
                    "parameterMode": "NAMED",
                    "queryParameters": [
                        {
                            "name": "named_param1",
                            "parameterType": {"type": "STRING"},
                            "parameterValue": {"value": "param-value"},
                        },
                        {
                            "name": "named_param2",
                            "parameterType": {"type": "INT64"},
                            "parameterValue": {"value": "123"},
                        },
                    ],
                }
            ),
            id="job_config-with-query_parameters-named",
        ),
        pytest.param(
            job_query.QueryJobConfig(
                query_parameters=[
                    ScalarQueryParameter(None, "STRING", "param-value"),
                    ScalarQueryParameter(None, "INT64", 123),
                ]
            ),
            make_query_request(
                {
                    "parameterMode": "POSITIONAL",
                    "queryParameters": [
                        {
                            "parameterType": {"type": "STRING"},
                            "parameterValue": {"value": "param-value"},
                        },
                        {
                            "parameterType": {"type": "INT64"},
                            "parameterValue": {"value": "123"},
                        },
                    ],
                }
            ),
            id="job_config-with-query_parameters-positional",
        ),
        pytest.param(
            job_query.QueryJobConfig(
                connection_properties=[
                    ConnectionProperty(key="time_zone", value="America/Chicago"),
                    ConnectionProperty(key="session_id", value="abcd-efgh-ijkl-mnop"),
                ]
            ),
            make_query_request(
                {
                    "connectionProperties": [
                        {"key": "time_zone", "value": "America/Chicago"},
                        {"key": "session_id", "value": "abcd-efgh-ijkl-mnop"},
                    ]
                }
            ),
            id="job_config-with-connection_properties",
        ),
        pytest.param(
            job_query.QueryJobConfig(labels={"abc": "def"}),
            make_query_request({"labels": {"abc": "def"}}),
            id="job_config-with-labels",
        ),
        pytest.param(
            job_query.QueryJobConfig(maximum_bytes_billed=987654),
            make_query_request({"maximumBytesBilled": "987654"}),
            id="job_config-with-maximum_bytes_billed",
        ),
        pytest.param(
            job_query.QueryJobConfig(
                write_incremental_results=True,
            ),
            make_query_request({"writeIncrementalResults": True}),
            id="job_config-with-incremental-results",
        ),
        pytest.param(
            job_query.QueryJobConfig(
                reservation="foo",
                max_slots=100,
            ),
            make_query_request(
                {
                    "maxSlots": "100",
                    "reservation": "foo",
                }
            ),
            id="job_config-with-reservation-and-slots",
        ),
    ),
)
def test__to_query_request(job_config, expected):
    result = _job_helpers._to_query_request(job_config, query="SELECT 1")
    expected["query"] = "SELECT 1"
    assert result == expected


@pytest.mark.parametrize(
    ("job_config", "invalid_key"),
    (
        pytest.param(job_copy.CopyJobConfig(), "copy", id="copy"),
        pytest.param(job_extract.ExtractJobConfig(), "extract", id="extract"),
        pytest.param(job_load.LoadJobConfig(), "load", id="load"),
    ),
)
def test__to_query_request_raises_for_invalid_config(job_config, invalid_key):
    with pytest.raises(ValueError, match=f"{repr(invalid_key)} in job_config"):
        _job_helpers._to_query_request(job_config, query="SELECT 1")


def test__to_query_job_defaults():
    mock_client = mock.create_autospec(Client)
    response = make_query_response(
        job_id="test-job", project_id="some-project", location="asia-northeast1"
    )
    job: job_query.QueryJob = _job_helpers._to_query_job(
        mock_client, "query-str", None, response
    )
    assert job.query == "query-str"
    assert job._client is mock_client
    assert job.job_id == "test-job"
    assert job.project == "some-project"
    assert job.location == "asia-northeast1"
    assert job.error_result is None
    assert job.errors is None


def test__to_query_job_dry_run():
    mock_client = mock.create_autospec(Client)
    response = make_query_response(
        job_id="test-job", project_id="some-project", location="asia-northeast1"
    )
    job_config: job_query.QueryJobConfig = job_query.QueryJobConfig()
    job_config.dry_run = True
    job: job_query.QueryJob = _job_helpers._to_query_job(
        mock_client, "query-str", job_config, response
    )
    assert job.dry_run is True


@pytest.mark.parametrize(
    ("completed", "expected_state"),
    (
        # Always pending so that we refresh the job state to get the
        # destination table or job stats in case it's needed.
        (True, "PENDING"),
        (False, "PENDING"),
    ),
)
def test__to_query_job_sets_state(completed, expected_state):
    mock_client = mock.create_autospec(Client)
    response = make_query_response(completed=completed)
    job: job_query.QueryJob = _job_helpers._to_query_job(
        mock_client, "query-str", None, response
    )
    assert job.state == expected_state


def test__to_query_job_sets_errors():
    mock_client = mock.create_autospec(Client)
    response = make_query_response(
        errors=[
            # https://cloud.google.com/bigquery/docs/reference/rest/v2/ErrorProto
            {"reason": "backendError", "message": "something went wrong"},
            {"message": "something else went wrong"},
        ]
    )
    job: job_query.QueryJob = _job_helpers._to_query_job(
        mock_client, "query-str", None, response
    )
    assert len(job.errors) == 2
    # If we got back a response instead of an HTTP error status code, most
    # likely the job didn't completely fail.
    assert job.error_result is None


def test_query_jobs_query_defaults():
    mock_client = mock.create_autospec(Client)
    mock_retry = mock.create_autospec(retries.Retry)
    mock_job_retry = mock.create_autospec(retries.Retry)
    mock_client._call_api.return_value = {
        "jobReference": {
            "projectId": "test-project",
            "jobId": "abc",
            "location": "asia-northeast1",
        }
    }
    _job_helpers.query_jobs_query(
        mock_client,
        "SELECT * FROM test",
        None,
        "asia-northeast1",
        "test-project",
        mock_retry,
        None,
        mock_job_retry,
    )

    assert mock_client._call_api.call_count == 1
    call_args, call_kwargs = mock_client._call_api.call_args
    assert call_args[0] is mock_retry
    # See: https://cloud.google.com/bigquery/docs/reference/rest/v2/jobs/query
    assert call_kwargs["path"] == "/projects/test-project/queries"
    assert call_kwargs["method"] == "POST"
    # See: https://cloud.google.com/bigquery/docs/reference/rest/v2/jobs/query#QueryRequest
    request = call_kwargs["data"]
    assert request["requestId"] is not None
    assert request["query"] == "SELECT * FROM test"
    assert request["location"] == "asia-northeast1"
    assert request["formatOptions"]["useInt64Timestamp"] is True
    assert "timeoutMs" not in request
    assert "timestampOutputFormat" not in request["formatOptions"]


def test_query_jobs_query_sets_format_options():
    """Since jobs.query can return results, ensure we use the lossless
    timestamp format.

    See: https://github.com/googleapis/python-bigquery/issues/395
    """
    mock_client = mock.create_autospec(Client)
    mock_retry = mock.create_autospec(retries.Retry)
    mock_job_retry = mock.create_autospec(retries.Retry)
    mock_client._call_api.return_value = {
        "jobReference": {"projectId": "test-project", "jobId": "abc", "location": "US"}
    }
    _job_helpers.query_jobs_query(
        mock_client,
        "SELECT * FROM test",
        None,
        "US",
        "test-project",
        mock_retry,
        None,
        mock_job_retry,
    )

    assert mock_client._call_api.call_count == 1
    _, call_kwargs = mock_client._call_api.call_args
    # See: https://cloud.google.com/bigquery/docs/reference/rest/v2/jobs/query#QueryRequest
    request = call_kwargs["data"]
    assert request["formatOptions"]["useInt64Timestamp"] is True


@pytest.mark.parametrize(
    ("timeout", "expected_timeout"),
    (
        (-1, 0),
        (0, 0),
        (1, 1000 - _job_helpers._TIMEOUT_BUFFER_MILLIS),
    ),
)
def test_query_jobs_query_sets_timeout(timeout, expected_timeout):
    mock_client = mock.create_autospec(Client)
    mock_retry = mock.create_autospec(retries.Retry)
    mock_job_retry = mock.create_autospec(retries.Retry)
    mock_client._call_api.return_value = {
        "jobReference": {"projectId": "test-project", "jobId": "abc", "location": "US"}
    }
    _job_helpers.query_jobs_query(
        mock_client,
        "SELECT * FROM test",
        None,
        "US",
        "test-project",
        mock_retry,
        timeout,
        mock_job_retry,
    )

    assert mock_client._call_api.call_count == 1
    _, call_kwargs = mock_client._call_api.call_args
    # See: https://cloud.google.com/bigquery/docs/reference/rest/v2/jobs/query#QueryRequest
    request = call_kwargs["data"]
    assert request["timeoutMs"] == expected_timeout


def test_query_jobs_query_picosecond():
    mock_client = mock.create_autospec(Client)
    mock_retry = mock.create_autospec(retries.Retry)
    mock_job_retry = mock.create_autospec(retries.Retry)
    mock_client._call_api.return_value = {
        "jobReference": {
            "projectId": "test-project",
            "jobId": "abc",
            "location": "asia-northeast1",
        }
    }
    _job_helpers.query_jobs_query(
        mock_client,
        "SELECT * FROM test",
        None,
        "asia-northeast1",
        "test-project",
        mock_retry,
        None,
        mock_job_retry,
        enums.TimestampPrecision.PICOSECOND,
    )

    _, call_kwargs = mock_client._call_api.call_args
    request = call_kwargs["data"]
    assert "useInt64Timestamp" not in request["formatOptions"]
    assert request["formatOptions"]["timestampOutputFormat"] == "ISO8601_STRING"


def test_query_and_wait_uses_jobs_insert():
    """With unsupported features, call jobs.insert instead of jobs.query."""
    client = mock.create_autospec(Client)
    client._call_api.return_value = {
        "jobReference": {
            "projectId": "response-project",
            "jobId": "abc",
            "location": "response-location",
        },
        "query": {
            "query": "SELECT 1",
        },
        # Make sure the job has "started"
        "status": {"state": "DONE"},
        "jobComplete": True,
    }
    job_config = job_query.QueryJobConfig(
        destination="dest-project.dest_dset.dest_table",
    )
    _job_helpers.query_and_wait(
        client,
        query="SELECT 1",
        location="request-location",
        project="request-project",
        job_config=job_config,
        retry=None,
        job_retry=None,
        page_size=None,
        max_results=None,
    )

    # We should call jobs.insert since jobs.query doesn't support destination.
    request_path = "/projects/request-project/jobs"
    client._call_api.assert_any_call(
        None,  # retry,
        span_name="BigQuery.job.begin",
        span_attributes={"path": request_path},
        job_ref=mock.ANY,
        method="POST",
        path=request_path,
        data={
            "jobReference": {
                "jobId": mock.ANY,
                "projectId": "request-project",
                "location": "request-location",
            },
            "configuration": {
                "query": {
                    "destinationTable": {
                        "projectId": "dest-project",
                        "datasetId": "dest_dset",
                        "tableId": "dest_table",
                    },
                    "useLegacySql": False,
                    "query": "SELECT 1",
                }
            },
        },
        timeout=None,
    )


def test_query_and_wait_sets_job_creation_mode():
    client = mock.create_autospec(Client)
    client.default_job_creation_mode = "JOB_CREATION_OPTIONAL"
    client._call_api.return_value = {
        "jobReference": {
            "projectId": "response-project",
            "jobId": "abc",
            "location": "response-location",
        },
        "jobComplete": True,
    }
    _job_helpers.query_and_wait(
        client,
        query="SELECT 1",
        location="request-location",
        project="request-project",
        job_config=None,
        retry=None,
        job_retry=None,
        page_size=None,
        max_results=None,
    )

    # We should only call jobs.query once, no additional row requests needed.
    request_path = "/projects/request-project/queries"
    client._call_api.assert_called_once_with(
        None,  # retry
        span_name="BigQuery.query",
        span_attributes={"path": request_path},
        method="POST",
        path=request_path,
        data={
            "query": "SELECT 1",
            "location": "request-location",
            "useLegacySql": False,
            "formatOptions": {
                "useInt64Timestamp": True,
            },
            "requestId": mock.ANY,
            "jobCreationMode": "JOB_CREATION_OPTIONAL",
        },
        timeout=None,
    )


@pytest.mark.parametrize(
    ("default_job_creation_mode", "query_results_format", "expected", "job_id"),
    [
        # ARROW skips creating a job by default.
        (None, "ARROW", "JOB_CREATION_OPTIONAL", None),
        # A mode set on the client still wins.
        ("JOB_CREATION_REQUIRED", "ARROW", "JOB_CREATION_REQUIRED", "abc"),
        # Other formats keep sending no mode.
        (None, None, None, "abc"),
    ],
)
def test_query_and_wait_job_creation_mode_for_arrow(
    default_job_creation_mode, query_results_format, expected, job_id
):
    client = mock.create_autospec(Client)
    client.default_job_creation_mode = default_job_creation_mode
    response = {
        "queryId": "qid-123",
        "jobComplete": True,
    }
    if job_id is not None:
        response["jobReference"] = {
            "projectId": "response-project",
            "jobId": job_id,
            "location": "response-location",
        }
    client._call_api.return_value = response

    # These tests check the request, not whether pyarrow and
    # google-cloud-bigquery-storage are installed.
    with mock.patch.object(_arrow_query, "_check_dependencies"):
        rows = _job_helpers.query_and_wait(
            client,
            query="SELECT 1",
            location="request-location",
            project="request-project",
            job_config=None,
            retry=None,
            job_retry=None,
            page_size=None,
            max_results=None,
            query_results_format=query_results_format,
        )

    request_body = client._call_api.call_args.kwargs["data"]
    assert request_body.get("jobCreationMode") == expected
    assert rows.query_id == "qid-123"
    assert rows.job_id == job_id


def test_query_and_wait_arrow_with_jobs_insert_creates_a_job():
    # jobs.query doesn't support destination, so this goes through jobs.insert,
    # which always creates a job.
    client = mock.create_autospec(Client)
    client.default_job_creation_mode = None
    client._call_api.return_value = {
        "jobReference": {
            "projectId": "response-project",
            "jobId": "abc",
            "location": "response-location",
        },
        "query": {
            "query": "SELECT 1",
        },
        "status": {"state": "DONE"},
        "jobComplete": True,
    }
    job_config = job_query.QueryJobConfig(
        destination="dest-project.dest_dset.dest_table",
    )
    # This test checks the request, not whether pyarrow and
    # google-cloud-bigquery-storage are installed.
    with mock.patch.object(_arrow_query, "_check_dependencies"):
        _job_helpers.query_and_wait(
            client,
            query="SELECT 1",
            location="request-location",
            project="request-project",
            job_config=job_config,
            retry=None,
            job_retry=None,
            page_size=None,
            max_results=None,
            query_results_format="ARROW",
        )

    first_call = client._call_api.call_args_list[0]
    assert first_call.kwargs["path"] == "/projects/request-project/jobs"
    assert "jobCreationMode" not in first_call.kwargs["data"]


def test_query_and_wait_sets_location():
    client = mock.create_autospec(Client)
    client._call_api.return_value = {
        "jobReference": {
            "projectId": "response-project",
            "jobId": "abc",
            "location": "response-location",
        },
        "jobComplete": True,
    }
    rows = _job_helpers.query_and_wait(
        client,
        query="SELECT 1",
        location="request-location",
        project="request-project",
        job_config=None,
        retry=None,
        job_retry=None,
        page_size=None,
        max_results=None,
    )
    assert rows.location == "response-location"

    # We should only call jobs.query once, no additional row requests needed.
    request_path = "/projects/request-project/queries"
    client._call_api.assert_called_once_with(
        None,  # retry
        span_name="BigQuery.query",
        span_attributes={"path": request_path},
        method="POST",
        path=request_path,
        data={
            "query": "SELECT 1",
            "location": "request-location",
            "useLegacySql": False,
            "formatOptions": {
                "useInt64Timestamp": True,
            },
            "requestId": mock.ANY,
            "jobCreationMode": mock.ANY,
        },
        timeout=None,
    )


@pytest.mark.parametrize(
    ("max_results", "page_size", "expected"),
    [
        (10, None, 10),
        (None, 11, 11),
        (12, 100, 12),
        (100, 13, 13),
    ],
)
def test_query_and_wait_sets_max_results(max_results, page_size, expected):
    client = mock.create_autospec(Client)
    client.default_job_creation_mode = None
    client._call_api.return_value = {
        "jobReference": {
            "projectId": "response-project",
            "jobId": "abc",
            "location": "response-location",
        },
        "jobComplete": True,
    }
    rows = _job_helpers.query_and_wait(
        client,
        query="SELECT 1",
        location="request-location",
        project="request-project",
        job_config=None,
        retry=None,
        job_retry=None,
        page_size=page_size,
        max_results=max_results,
    )
    assert rows.location == "response-location"

    # We should only call jobs.query once, no additional row requests needed.
    request_path = "/projects/request-project/queries"
    client._call_api.assert_called_once_with(
        None,  # retry
        span_name="BigQuery.query",
        span_attributes={"path": request_path},
        method="POST",
        path=request_path,
        data={
            "query": "SELECT 1",
            "location": "request-location",
            "useLegacySql": False,
            "formatOptions": {
                "useInt64Timestamp": True,
            },
            "requestId": mock.ANY,
            "maxResults": expected,
        },
        timeout=None,
    )


def test_query_and_wait_caches_completed_query_results_one_page():
    client = mock.create_autospec(Client)
    client.default_job_creation_mode = None
    client._call_api.return_value = {
        "jobReference": {
            "projectId": "response-project",
            "jobId": "abc",
            "location": "US",
        },
        "jobComplete": True,
        "queryId": "xyz",
        "schema": {
            "fields": [
                {"name": "full_name", "type": "STRING", "mode": "REQUIRED"},
                {"name": "age", "type": "INT64", "mode": "NULLABLE"},
            ],
        },
        "rows": [
            {"f": [{"v": "Whillma Phlyntstone"}, {"v": "27"}]},
            {"f": [{"v": "Bhetty Rhubble"}, {"v": "28"}]},
            {"f": [{"v": "Phred Phlyntstone"}, {"v": "32"}]},
            {"f": [{"v": "Bharney Rhubble"}, {"v": "33"}]},
        ],
        # Even though totalRows > len(rows), we should use the presence of a
        # next page token to decide if there are any more pages.
        "totalRows": 8,
    }
    rows = _job_helpers.query_and_wait(
        client,
        query="SELECT full_name, age FROM people;",
        job_config=None,
        location=None,
        project="request-project",
        retry=None,
        job_retry=None,
        page_size=None,
        max_results=None,
    )
    rows_list = list(rows)
    assert rows.project == "response-project"
    assert rows.job_id == "abc"
    assert rows.location == "US"
    assert rows.query_id == "xyz"
    assert rows.total_rows == 8
    assert len(rows_list) == 4

    # We should only call jobs.query once, no additional row requests needed.
    request_path = "/projects/request-project/queries"
    client._call_api.assert_called_once_with(
        None,  # retry
        span_name="BigQuery.query",
        span_attributes={"path": request_path},
        method="POST",
        path=request_path,
        data={
            "query": "SELECT full_name, age FROM people;",
            "useLegacySql": False,
            "formatOptions": {
                "useInt64Timestamp": True,
            },
            "requestId": mock.ANY,
        },
        timeout=None,
    )


def test_query_and_wait_caches_completed_query_results_one_page_no_rows():
    client = mock.create_autospec(Client)
    client.default_job_creation_mode = None
    client._call_api.return_value = {
        "jobReference": {
            "projectId": "response-project",
            "jobId": "abc",
            "location": "US",
        },
        "jobComplete": True,
        "queryId": "xyz",
    }
    rows = _job_helpers.query_and_wait(
        client,
        query="CREATE TABLE abc;",
        project="request-project",
        job_config=None,
        location=None,
        retry=None,
        job_retry=None,
        page_size=None,
        max_results=None,
    )
    assert rows.project == "response-project"
    assert rows.job_id == "abc"
    assert rows.location == "US"
    assert rows.query_id == "xyz"
    assert list(rows) == []

    # We should only call jobs.query once, no additional row requests needed.
    request_path = "/projects/request-project/queries"
    client._call_api.assert_called_once_with(
        None,  # retry
        span_name="BigQuery.query",
        span_attributes={"path": request_path},
        method="POST",
        path=request_path,
        data={
            "query": "CREATE TABLE abc;",
            "useLegacySql": False,
            "formatOptions": {
                "useInt64Timestamp": True,
            },
            "requestId": mock.ANY,
        },
        timeout=None,
    )


def test_query_and_wait_caches_completed_query_results_more_pages():
    client = make_client()
    conn = client._connection = make_connection(
        {
            "jobReference": {
                "projectId": "response-project",
                "jobId": "response-job-id",
                "location": "response-location",
            },
            "jobComplete": True,
            "queryId": "xyz",
            "schema": {
                "fields": [
                    {"name": "full_name", "type": "STRING", "mode": "REQUIRED"},
                    {"name": "age", "type": "INT64", "mode": "NULLABLE"},
                ],
            },
            "rows": [
                {"f": [{"v": "Whillma Phlyntstone"}, {"v": "27"}]},
                {"f": [{"v": "Bhetty Rhubble"}, {"v": "28"}]},
                {"f": [{"v": "Phred Phlyntstone"}, {"v": "32"}]},
                {"f": [{"v": "Bharney Rhubble"}, {"v": "33"}]},
            ],
            # Even though totalRows <= len(rows), we should use the presence of a
            # next page token to decide if there are any more pages.
            "totalRows": 2,
            "pageToken": "page-2",
        },
        # TODO(swast): This is a case where we can avoid a call to jobs.get,
        # but currently do so because the RowIterator might need the
        # destination table, since results aren't fully cached.
        {
            "jobReference": {
                "projectId": "response-project",
                "jobId": "response-job-id",
                "location": "response-location",
            },
            "status": {"state": "DONE"},
        },
        {
            "rows": [
                {"f": [{"v": "Pebbles Phlyntstone"}, {"v": "4"}]},
                {"f": [{"v": "Bamm-Bamm Rhubble"}, {"v": "5"}]},
                {"f": [{"v": "Joseph Rockhead"}, {"v": "32"}]},
                {"f": [{"v": "Perry Masonry"}, {"v": "33"}]},
            ],
            "totalRows": 3,
            "pageToken": "page-3",
        },
        {
            "rows": [
                {"f": [{"v": "Pearl Slaghoople"}, {"v": "53"}]},
            ],
            "totalRows": 4,
        },
    )
    rows = _job_helpers.query_and_wait(
        client,
        query="SELECT full_name, age FROM people;",
        project="request-project",
        job_config=None,
        location=None,
        retry=None,
        job_retry=None,
        page_size=None,
        max_results=None,
    )
    assert rows.total_rows == 2  # Match the API response.
    rows_list = list(rows)
    assert rows.total_rows == 4  # Match the final API response.
    assert len(rows_list) == 9

    # Start the query.
    jobs_query_path = "/projects/request-project/queries"
    conn.api_request.assert_any_call(
        method="POST",
        path=jobs_query_path,
        data={
            "query": "SELECT full_name, age FROM people;",
            "useLegacySql": False,
            "formatOptions": {
                "useInt64Timestamp": True,
            },
            "requestId": mock.ANY,
        },
        timeout=None,
    )

    # Note: There is no get call to
    # "/projects/response-project/jobs/response-job-id", because fetching job
    # metadata isn't necessary in this case. The job already completed in
    # jobs.query and we don't need the full job metadata in query_and_wait.

    # Fetch the remaining two pages.
    jobs_get_query_results_path = "/projects/response-project/queries/response-job-id"
    conn.api_request.assert_any_call(
        timeout=None,
        method="GET",
        path=jobs_get_query_results_path,
        query_params={
            "pageToken": "page-2",
            "fields": "jobReference,totalRows,pageToken,rows",
            "location": "response-location",
            "formatOptions.useInt64Timestamp": True,
        },
    )
    conn.api_request.assert_any_call(
        timeout=None,
        method="GET",
        path=jobs_get_query_results_path,
        query_params={
            "pageToken": "page-3",
            "fields": "jobReference,totalRows,pageToken,rows",
            "location": "response-location",
            "formatOptions.useInt64Timestamp": True,
        },
    )


def test_query_and_wait_incomplete_query():
    client = make_client()
    conn = client._connection = make_connection(
        # jobs.query
        {
            "jobReference": {
                "projectId": "response-project",
                "jobId": "response-job-id",
                "location": "response-location",
            },
            "jobComplete": False,
        },
        # jobs.get
        {
            "jobReference": {
                "projectId": "response-project",
                "jobId": "response-job-id",
                "location": "response-location",
            },
            "status": {"state": "RUNNING"},
        },
        # jobs.getQueryResults with max_results=0
        {
            "jobReference": {
                "projectId": "response-project",
                "jobId": "response-job-id",
                "location": "response-location",
            },
            "jobComplete": True,
            "totalRows": 2,
            "queryId": "xyz",
            "schema": {
                "fields": [
                    {"name": "full_name", "type": "STRING", "mode": "REQUIRED"},
                    {"name": "age", "type": "INT64", "mode": "NULLABLE"},
                ],
            },
        },
        # jobs.get
        {
            "jobReference": {
                "projectId": "response-project",
                "jobId": "response-job-id",
                "location": "response-location",
            },
            "status": {"state": "DONE"},
        },
        # jobs.getQueryResults
        # Note: No more jobs.getQueryResults with max_results=0 because the
        # previous call to jobs.getQueryResults returned with jobComplete=True.
        {
            "rows": [
                {"f": [{"v": "Whillma Phlyntstone"}, {"v": "27"}]},
                {"f": [{"v": "Bhetty Rhubble"}, {"v": "28"}]},
                {"f": [{"v": "Phred Phlyntstone"}, {"v": "32"}]},
                {"f": [{"v": "Bharney Rhubble"}, {"v": "33"}]},
            ],
            # Even though totalRows <= len(rows), we should use the presence of a
            # next page token to decide if there are any more pages.
            "totalRows": 2,
            "pageToken": "page-2",
        },
        # jobs.getQueryResults
        {
            "rows": [
                {"f": [{"v": "Pearl Slaghoople"}, {"v": "53"}]},
            ],
        },
    )
    rows = _job_helpers.query_and_wait(
        client,
        query="SELECT full_name, age FROM people;",
        project="request-project",
        job_config=None,
        location=None,
        retry=None,
        job_retry=None,
        page_size=None,
        max_results=None,
    )
    rows_list = list(rows)
    assert rows.total_rows == 2  # Match the API response.
    assert len(rows_list) == 5

    # Start the query.
    jobs_query_path = "/projects/request-project/queries"
    conn.api_request.assert_any_call(
        method="POST",
        path=jobs_query_path,
        data={
            "query": "SELECT full_name, age FROM people;",
            "useLegacySql": False,
            "formatOptions": {
                "useInt64Timestamp": True,
            },
            "requestId": mock.ANY,
        },
        timeout=None,
    )

    # Wait for the query to finish.
    jobs_get_query_results_path = "/projects/response-project/queries/response-job-id"
    conn.api_request.assert_any_call(
        method="GET",
        path=jobs_get_query_results_path,
        query_params={
            # job_query.QueryJob uses getQueryResults to wait for the query to finish.
            # It avoids fetching the results because:
            # (1) For large rows this can take a long time, much longer than
            #     our progress bar update frequency.
            #     See: https://github.com/googleapis/python-bigquery/issues/403
            # (2) Caching the first page of results uses an unexpected increase in memory.
            #     See: https://github.com/googleapis/python-bigquery/issues/394
            "maxResults": 0,
            "location": "response-location",
        },
        timeout=None,
    )

    # Fetch the job metadata in case the RowIterator needs the destination table.
    jobs_get_path = "/projects/response-project/jobs/response-job-id"
    conn.api_request.assert_any_call(
        method="GET",
        path=jobs_get_path,
        query_params={"projection": "full", "location": "response-location"},
        timeout=retry.DEFAULT_GET_JOB_TIMEOUT,
    )

    # Fetch the remaining two pages.
    conn.api_request.assert_any_call(
        timeout=None,
        method="GET",
        path=jobs_get_query_results_path,
        query_params={
            "fields": "jobReference,totalRows,pageToken,rows",
            "location": "response-location",
            "formatOptions.useInt64Timestamp": True,
        },
    )
    conn.api_request.assert_any_call(
        timeout=None,
        method="GET",
        path=jobs_get_query_results_path,
        query_params={
            "pageToken": "page-2",
            "fields": "jobReference,totalRows,pageToken,rows",
            "location": "response-location",
            "formatOptions.useInt64Timestamp": True,
        },
    )


def test_make_job_id_wo_suffix():
    job_id = _job_helpers.make_job_id("job_id")
    assert job_id == "job_id"


def test_make_job_id_w_suffix():
    with mock.patch("uuid.uuid4", side_effect=["212345"]):
        job_id = _job_helpers.make_job_id(None, prefix="job_id")

    assert job_id == "job_id212345"


def test_make_job_id_random():
    with mock.patch("uuid.uuid4", side_effect=["212345"]):
        job_id = _job_helpers.make_job_id(None)

    assert job_id == "212345"


def test_make_job_id_w_job_id_overrides_prefix():
    job_id = _job_helpers.make_job_id("job_id", prefix="unused_prefix")
    assert job_id == "job_id"


@pytest.mark.parametrize(
    ("job_config", "expected"),
    (
        pytest.param(None, True),
        pytest.param(job_query.QueryJobConfig(), True, id="default"),
        pytest.param(
            job_query.QueryJobConfig(use_query_cache=False), True, id="use_query_cache"
        ),
        pytest.param(
            job_query.QueryJobConfig(maximum_bytes_billed=10_000_000),
            True,
            id="maximum_bytes_billed",
        ),
        pytest.param(
            job_query.QueryJobConfig(clustering_fields=["a", "b", "c"]),
            False,
            id="clustering_fields",
        ),
        pytest.param(
            job_query.QueryJobConfig(destination="p.d.t"), False, id="destination"
        ),
        pytest.param(
            job_query.QueryJobConfig(
                destination_encryption_configuration=job_query.EncryptionConfiguration(
                    "key"
                )
            ),
            False,
            id="destination_encryption_configuration",
        ),
        # priority="BATCH" is not supported. See:
        # https://github.com/googleapis/python-bigquery/issues/1867
        pytest.param(
            job_query.QueryJobConfig(
                priority=enums.QueryPriority.BATCH,
            ),
            False,
            id="priority=BATCH",
        ),
        pytest.param(
            job_query.QueryJobConfig(write_incremental_results=True),
            True,
            id="write_incremental_results",
        ),
        pytest.param(
            job_query.QueryJobConfig(job_timeout_ms=1000),
            True,
            id="job_timeout_ms",
        ),
        pytest.param(
            job_query.QueryJobConfig(reservation="foo"),
            True,
            id="reservation",
        ),
        pytest.param(
            job_query.QueryJobConfig(max_slots=20),
            True,
            id="max_slots",
        ),
    ),
)
def test_supported_by_jobs_query_from_queryjobconfig(
    job_config: Optional[job_query.QueryJobConfig], expected: bool
):
    request_body = _job_helpers._to_query_request(job_config, query="SELECT 1")
    assert _job_helpers._supported_by_jobs_query(request_body) == expected


def test_wait_or_cancel_no_exception():
    job = mock.create_autospec(job_query.QueryJob, instance=True)
    expected_rows = mock.MagicMock()
    job.result.return_value = expected_rows
    retry = retries.Retry()

    rows = _job_helpers._wait_or_cancel(
        job,
        api_timeout=123,
        wait_timeout=456,
        retry=retry,
        page_size=789,
        max_results=101112,
    )

    job.result.assert_called_once_with(
        timeout=456,
        retry=retry,
        page_size=789,
        max_results=101112,
    )
    assert rows is expected_rows


def test_wait_or_cancel_exception_cancels_job():
    job = mock.create_autospec(job_query.QueryJob, instance=True)
    job.result.side_effect = google.api_core.exceptions.BadGateway("test error")
    retry = retries.Retry()

    with pytest.raises(google.api_core.exceptions.BadGateway):
        _job_helpers._wait_or_cancel(
            job,
            api_timeout=123,
            wait_timeout=456,
            retry=retry,
            page_size=789,
            max_results=101112,
        )

    job.result.assert_called_once_with(
        timeout=456,
        retry=retry,
        page_size=789,
        max_results=101112,
    )
    job.cancel.assert_called_once_with(
        timeout=123,
        retry=retry,
    )


def test_wait_or_cancel_exception_raises_original_exception():
    job = mock.create_autospec(job_query.QueryJob, instance=True)
    job.result.side_effect = google.api_core.exceptions.BadGateway("test error")
    job.cancel.side_effect = google.api_core.exceptions.NotFound("don't raise me")
    retry = retries.Retry()

    with pytest.raises(google.api_core.exceptions.BadGateway):
        _job_helpers._wait_or_cancel(
            job,
            api_timeout=123,
            wait_timeout=456,
            retry=retry,
            page_size=789,
            max_results=101112,
        )

    job.result.assert_called_once_with(
        timeout=456,
        retry=retry,
        page_size=789,
        max_results=101112,
    )
    job.cancel.assert_called_once_with(
        timeout=123,
        retry=retry,
    )
