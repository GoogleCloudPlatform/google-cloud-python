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

import datetime
from unittest import mock

import pytest

from google.cloud.bigquery.retry import DEFAULT_TIMEOUT
from .helpers import make_connection


@pytest.mark.parametrize(
    "extra,query", [({}, {}), (dict(page_size=42), dict(maxResults=42))]
)
def test_list_jobs_defaults(client, PROJECT, DS_ID, extra, query):
    from google.cloud.bigquery.job import CopyJob
    from google.cloud.bigquery.job import CreateDisposition
    from google.cloud.bigquery.job import ExtractJob
    from google.cloud.bigquery.job import LoadJob
    from google.cloud.bigquery.job import QueryJob
    from google.cloud.bigquery.job import WriteDisposition

    SOURCE_TABLE = "source_table"
    DESTINATION_TABLE = "destination_table"
    QUERY_DESTINATION_TABLE = "query_destination_table"
    SOURCE_URI = "gs://test_bucket/src_object*"
    DESTINATION_URI = "gs://test_bucket/dst_object*"
    JOB_TYPES = {
        "load_job": LoadJob,
        "copy_job": CopyJob,
        "extract_job": ExtractJob,
        "query_job": QueryJob,
    }
    PATH = "projects/%s/jobs" % PROJECT
    TOKEN = "TOKEN"
    QUERY = "SELECT * from test_dataset:test_table"
    ASYNC_QUERY_DATA = {
        "id": "%s:%s" % (PROJECT, "query_job"),
        "jobReference": {"projectId": PROJECT, "jobId": "query_job"},
        "state": "DONE",
        "configuration": {
            "query": {
                "query": QUERY,
                "destinationTable": {
                    "projectId": PROJECT,
                    "datasetId": DS_ID,
                    "tableId": QUERY_DESTINATION_TABLE,
                },
                "createDisposition": CreateDisposition.CREATE_IF_NEEDED,
                "writeDisposition": WriteDisposition.WRITE_TRUNCATE,
            }
        },
    }
    EXTRACT_DATA = {
        "id": "%s:%s" % (PROJECT, "extract_job"),
        "jobReference": {"projectId": PROJECT, "jobId": "extract_job"},
        "state": "DONE",
        "configuration": {
            "extract": {
                "sourceTable": {
                    "projectId": PROJECT,
                    "datasetId": DS_ID,
                    "tableId": SOURCE_TABLE,
                },
                "destinationUris": [DESTINATION_URI],
            }
        },
    }
    COPY_DATA = {
        "id": "%s:%s" % (PROJECT, "copy_job"),
        "jobReference": {"projectId": PROJECT, "jobId": "copy_job"},
        "state": "DONE",
        "configuration": {
            "copy": {
                "sourceTables": [
                    {"projectId": PROJECT, "datasetId": DS_ID, "tableId": SOURCE_TABLE}
                ],
                "destinationTable": {
                    "projectId": PROJECT,
                    "datasetId": DS_ID,
                    "tableId": DESTINATION_TABLE,
                },
            }
        },
    }
    LOAD_DATA = {
        "id": "%s:%s" % (PROJECT, "load_job"),
        "jobReference": {"projectId": PROJECT, "jobId": "load_job"},
        "state": "DONE",
        "configuration": {
            "load": {
                "destinationTable": {
                    "projectId": PROJECT,
                    "datasetId": DS_ID,
                    "tableId": SOURCE_TABLE,
                },
                "sourceUris": [SOURCE_URI],
            }
        },
    }
    DATA = {
        "nextPageToken": TOKEN,
        "jobs": [ASYNC_QUERY_DATA, EXTRACT_DATA, COPY_DATA, LOAD_DATA],
    }
    conn = client._connection = make_connection(DATA)

    iterator = client.list_jobs(**extra)
    with mock.patch(
        "google.cloud.bigquery.opentelemetry_tracing._get_final_span_attributes"
    ) as final_attributes:
        page = next(iterator.pages)

    final_attributes.assert_called_once_with({"path": "/%s" % PATH}, client, None)
    jobs = list(page)
    token = iterator.next_page_token

    assert len(jobs) == len(DATA["jobs"])
    for found, expected in zip(jobs, DATA["jobs"]):
        name = expected["jobReference"]["jobId"]
        assert isinstance(found, JOB_TYPES[name])
        assert found.job_id == name
    assert token == TOKEN

    conn.api_request.assert_called_once_with(
        method="GET",
        path="/%s" % PATH,
        query_params=dict({"projection": "full"}, **query),
        timeout=DEFAULT_TIMEOUT,
    )


def test_list_jobs_load_job_wo_sourceUris(client, PROJECT, DS_ID):
    from google.cloud.bigquery.job import LoadJob

    SOURCE_TABLE = "source_table"
    JOB_TYPES = {"load_job": LoadJob}
    PATH = "projects/%s/jobs" % PROJECT
    TOKEN = "TOKEN"
    LOAD_DATA = {
        "id": "%s:%s" % (PROJECT, "load_job"),
        "jobReference": {"projectId": PROJECT, "jobId": "load_job"},
        "state": "DONE",
        "configuration": {
            "load": {
                "destinationTable": {
                    "projectId": PROJECT,
                    "datasetId": DS_ID,
                    "tableId": SOURCE_TABLE,
                }
            }
        },
    }
    DATA = {"nextPageToken": TOKEN, "jobs": [LOAD_DATA]}
    conn = client._connection = make_connection(DATA)

    iterator = client.list_jobs()
    with mock.patch(
        "google.cloud.bigquery.opentelemetry_tracing._get_final_span_attributes"
    ) as final_attributes:
        page = next(iterator.pages)

    final_attributes.assert_called_once_with({"path": "/%s" % PATH}, client, None)
    jobs = list(page)
    token = iterator.next_page_token

    assert len(jobs) == len(DATA["jobs"])
    for found, expected in zip(jobs, DATA["jobs"]):
        name = expected["jobReference"]["jobId"]
        assert isinstance(found, JOB_TYPES[name])
        assert found.job_id == name
    assert token == TOKEN

    conn.api_request.assert_called_once_with(
        method="GET",
        path="/%s" % PATH,
        query_params={"projection": "full"},
        timeout=DEFAULT_TIMEOUT,
    )


def test_list_jobs_explicit_missing(client, PROJECT):
    PATH = "projects/%s/jobs" % PROJECT
    DATA = {}
    TOKEN = "TOKEN"
    conn = client._connection = make_connection(DATA)

    iterator = client.list_jobs(
        max_results=1000, page_token=TOKEN, all_users=True, state_filter="done"
    )
    with mock.patch(
        "google.cloud.bigquery.opentelemetry_tracing._get_final_span_attributes"
    ) as final_attributes:
        page = next(iterator.pages)

    final_attributes.assert_called_once_with({"path": "/%s" % PATH}, client, None)
    jobs = list(page)
    token = iterator.next_page_token

    assert len(jobs) == 0
    assert token is None

    conn.api_request.assert_called_once_with(
        method="GET",
        path="/%s" % PATH,
        query_params={
            "projection": "full",
            "maxResults": 1000,
            "pageToken": TOKEN,
            "allUsers": True,
            "stateFilter": "done",
        },
        timeout=DEFAULT_TIMEOUT,
    )


def test_list_jobs_w_project(client, PROJECT):
    conn = client._connection = make_connection({})

    list(client.list_jobs(project="other-project"))

    conn.api_request.assert_called_once_with(
        method="GET",
        path="/projects/other-project/jobs",
        query_params={"projection": "full"},
        timeout=DEFAULT_TIMEOUT,
    )


def test_list_jobs_w_timeout(client, PROJECT):
    conn = client._connection = make_connection({})

    list(client.list_jobs(timeout=7.5))

    conn.api_request.assert_called_once_with(
        method="GET",
        path="/projects/{}/jobs".format(PROJECT),
        query_params={"projection": "full"},
        timeout=7.5,
    )


def test_list_jobs_w_time_filter(client, PROJECT):
    conn = client._connection = make_connection({})

    # One millisecond after the unix epoch.
    start_time = datetime.datetime(1970, 1, 1, 0, 0, 0, 1000)
    # One millisecond after the the 2038 31-bit signed int rollover
    end_time = datetime.datetime(2038, 1, 19, 3, 14, 7, 1000)
    end_time_millis = (((2**31) - 1) * 1000) + 1

    list(client.list_jobs(min_creation_time=start_time, max_creation_time=end_time))

    conn.api_request.assert_called_once_with(
        method="GET",
        path="/projects/%s/jobs" % PROJECT,
        query_params={
            "projection": "full",
            "minCreationTime": "1",
            "maxCreationTime": str(end_time_millis),
        },
        timeout=DEFAULT_TIMEOUT,
    )


def test_list_jobs_w_parent_job_filter(client, PROJECT):
    from google.cloud.bigquery import job

    conn = client._connection = make_connection({}, {})

    parent_job_args = ["parent-job-123", job._AsyncJob("parent-job-123", client)]

    for parent_job in parent_job_args:
        list(client.list_jobs(parent_job=parent_job))
        conn.api_request.assert_called_once_with(
            method="GET",
            path="/projects/%s/jobs" % PROJECT,
            query_params={"projection": "full", "parentJobId": "parent-job-123"},
            timeout=DEFAULT_TIMEOUT,
        )
        conn.api_request.reset_mock()
