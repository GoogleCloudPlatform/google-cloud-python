# Copyright 2025 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import concurrent.futures
from unittest import mock

import freezegun
import google.api_core.retry
import pytest
from google.api_core import exceptions
from google.cloud.bigquery.client import _MIN_GET_QUERY_RESULTS_TIMEOUT
from google.cloud.bigquery.job import QueryJob
from google.cloud.bigquery.retry import DEFAULT_GET_JOB_TIMEOUT
from google.cloud.bigquery.table import RowIterator

from ..helpers import make_connection
from .helpers import _make_client

PROJECT = "test-project"
JOB_ID = "test-job-id"
QUERY = "select count(*) from persons"


def _make_resource(started=False, ended=False, location="US"):
    resource = {
        "jobReference": {"projectId": PROJECT, "jobId": JOB_ID, "location": location},
        "status": {"state": "PENDING"},
        "configuration": {
            "query": {"query": QUERY},
            "job_type": "query",
        },
        "statistics": {"creationTime": "1"},
    }

    if started:
        resource["status"]["state"] = "RUNNING"
        resource["statistics"]["startTime"] = "2"

    if ended:
        resource["status"]["state"] = "DONE"
        resource["statistics"]["endTime"] = "3"

    return resource


def test_result_w_custom_retry(global_time_lock):
    query_resource = {
        "jobComplete": False,
        "jobReference": {"projectId": PROJECT, "jobId": JOB_ID},
    }
    query_resource_done = {
        "jobComplete": True,
        "jobReference": {"projectId": PROJECT, "jobId": JOB_ID},
        "schema": {"fields": [{"name": "col1", "type": "STRING"}]},
        "totalRows": "2",
    }
    job_resource = _make_resource(started=True, location="asia-northeast1")
    job_resource_done = _make_resource(
        started=True, ended=True, location="asia-northeast1"
    )
    job_resource_done["configuration"]["query"]["destinationTable"] = {
        "projectId": "dest-project",
        "datasetId": "dest_dataset",
        "tableId": "dest_table",
    }

    connection = make_connection(
        # Also, for each API request, raise an exception that we know can
        # be retried. Because of this, for each iteration we do:
        # jobs.get (x2) & jobs.getQueryResults (x2)
        exceptions.NotFound("not normally retriable"),
        job_resource,
        exceptions.NotFound("not normally retriable"),
        query_resource,
        # Query still not done, repeat both.
        exceptions.NotFound("not normally retriable"),
        job_resource,
        exceptions.NotFound("not normally retriable"),
        query_resource,
        exceptions.NotFound("not normally retriable"),
        # Query still not done, repeat both.
        job_resource_done,
        exceptions.NotFound("not normally retriable"),
        query_resource_done,
        # Query finished!
    )
    client = _make_client(PROJECT, connection=connection)
    job = QueryJob.from_api_repr(job_resource, client)

    custom_predicate = mock.Mock()
    custom_predicate.return_value = True
    custom_retry = google.api_core.retry.Retry(
        initial=0.001,
        maximum=0.001,
        multiplier=1.0,
        deadline=1.0,
        predicate=custom_predicate,
    )

    assert isinstance(job.result(retry=custom_retry), RowIterator)
    query_results_call = mock.call(
        method="GET",
        path=f"/projects/{PROJECT}/queries/{JOB_ID}",
        query_params={"maxResults": 0, "location": "asia-northeast1"},
        timeout=mock.ANY,
    )
    reload_call = mock.call(
        method="GET",
        path=f"/projects/{PROJECT}/jobs/{JOB_ID}",
        query_params={"projection": "full", "location": "asia-northeast1"},
        timeout=DEFAULT_GET_JOB_TIMEOUT,
    )

    connection.api_request.assert_has_calls(
        [
            reload_call,
            reload_call,
            query_results_call,
            query_results_call,
            reload_call,
            reload_call,
            query_results_call,
            query_results_call,
            reload_call,
            reload_call,
            query_results_call,
            query_results_call,
        ]
    )


def test_result_w_timeout_doesnt_raise(global_time_lock):
    begun_resource = _make_resource()
    query_resource = {
        "jobComplete": True,
        "jobReference": {"projectId": PROJECT, "jobId": JOB_ID},
        "schema": {"fields": [{"name": "col1", "type": "STRING"}]},
    }
    done_resource = begun_resource.copy()
    done_resource["status"] = {"state": "DONE"}
    connection = make_connection(begun_resource, query_resource, done_resource)
    client = _make_client(project=PROJECT, connection=connection)
    job = QueryJob(JOB_ID, QUERY, client)
    job._properties["jobReference"]["location"] = "US"
    job._properties["status"] = {"state": "RUNNING"}

    with freezegun.freeze_time("1970-01-01 00:00:00", tick=False):
        job.result(
            timeout=1.125,
        )

    reload_call = mock.call(
        method="GET",
        path=f"/projects/{PROJECT}/jobs/{JOB_ID}",
        query_params={"projection": "full", "location": "US"},
        timeout=1.125,
    )
    get_query_results_call = mock.call(
        method="GET",
        path=f"/projects/{PROJECT}/queries/{JOB_ID}",
        query_params={
            "maxResults": 0,
            "location": "US",
        },
        timeout=_MIN_GET_QUERY_RESULTS_TIMEOUT,
    )
    connection.api_request.assert_has_calls(
        [
            reload_call,
            get_query_results_call,
            reload_call,
        ]
    )


def test_result_w_timeout_raises_concurrent_futures_timeout(global_time_lock):
    begun_resource = _make_resource()
    begun_resource["jobReference"]["location"] = "US"
    query_resource = {
        "jobComplete": True,
        "jobReference": {"projectId": PROJECT, "jobId": JOB_ID},
        "schema": {"fields": [{"name": "col1", "type": "STRING"}]},
    }
    done_resource = begun_resource.copy()
    done_resource["status"] = {"state": "DONE"}
    connection = make_connection(begun_resource, query_resource, done_resource)
    client = _make_client(project=PROJECT, connection=connection)
    job = QueryJob(JOB_ID, QUERY, client)
    job._properties["jobReference"]["location"] = "US"
    job._properties["status"] = {"state": "RUNNING"}

    with freezegun.freeze_time(
        "1970-01-01 00:00:00", auto_tick_seconds=1.0
    ), pytest.raises(concurrent.futures.TimeoutError):
        job.result(timeout=1.125)

    reload_call = mock.call(
        method="GET",
        path=f"/projects/{PROJECT}/jobs/{JOB_ID}",
        query_params={"projection": "full", "location": "US"},
        timeout=1.125,
    )
    get_query_results_call = mock.call(
        method="GET",
        path=f"/projects/{PROJECT}/queries/{JOB_ID}",
        query_params={
            "maxResults": 0,
            "location": "US",
        },
        timeout=_MIN_GET_QUERY_RESULTS_TIMEOUT,
    )
    connection.api_request.assert_has_calls(
        [
            reload_call,
            get_query_results_call,
        ]
    )
