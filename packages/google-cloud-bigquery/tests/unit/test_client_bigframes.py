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

"""Tests for Client features enabling the bigframes integration."""

from __future__ import annotations

import datetime
from unittest import mock

import pytest

import google.auth.credentials
from google.api_core import exceptions
from google.cloud import bigquery
import google.cloud.bigquery.client
from google.cloud.bigquery import _job_helpers


PROJECT = "test-project"
LOCATION = "test-location"


def make_response(body, *, status_code: int = 200):
    response = mock.Mock()
    type(response).status_code = mock.PropertyMock(return_value=status_code)
    response.json.return_value = body
    return response


@pytest.fixture
def client():
    """A real client object with mocked API requests."""
    credentials = mock.create_autospec(
        google.auth.credentials.Credentials, instance=True
    )
    http_session = mock.Mock()
    return google.cloud.bigquery.client.Client(
        project=PROJECT,
        credentials=credentials,
        _http=http_session,
        location=LOCATION,
    )


def test_query_and_wait_bigframes_dry_run_no_callback(client):
    client._http.request.side_effect = [
        make_response(
            {
                # https://cloud.google.com/bigquery/docs/reference/rest/v2/jobs/query
                "location": LOCATION,
                "queryId": "abcdefg",
                "totalBytesProcessed": "123",
                "jobComplete": True,
            }
        ),
    ]
    callback = mock.Mock()
    job_config = bigquery.QueryJobConfig(dry_run=True)
    response = client._query_and_wait_bigframes(
        query="SELECT 1", job_config=job_config, callback=callback
    )
    callback.assert_not_called()
    assert response.total_bytes_processed == 123
    assert response.query_id == "abcdefg"


def test_query_and_wait_bigframes_callback(client):
    created = datetime.datetime(
        2025, 8, 18, 10, 11, 12, 345000, tzinfo=datetime.timezone.utc
    )
    started = datetime.datetime(
        2025, 8, 18, 10, 11, 13, 456000, tzinfo=datetime.timezone.utc
    )
    ended = datetime.datetime(
        2025, 8, 18, 10, 11, 14, 567000, tzinfo=datetime.timezone.utc
    )
    client._http.request.side_effect = [
        make_response(
            {
                # https://cloud.google.com/bigquery/docs/reference/rest/v2/jobs/query
                "location": LOCATION,
                "queryId": "abcdefg",
                "totalRows": "100",
                "totalBytesProcessed": "123",
                "totalSlotMs": "987",
                "jobComplete": True,
                "creationTime": _to_millis(created),
                "startTime": _to_millis(started),
                "endTime": _to_millis(ended),
            }
        ),
    ]
    callback = mock.Mock()
    client._query_and_wait_bigframes(query="SELECT 1", callback=callback)
    callback.assert_has_calls(
        [
            mock.call(
                _job_helpers.QuerySentEvent(
                    query="SELECT 1",
                    billing_project=PROJECT,
                    location=LOCATION,
                    # No job ID, because a basic query is eligible for jobs.query.
                    job_id=None,
                    request_id=mock.ANY,
                )
            ),
            mock.call(
                _job_helpers.QueryFinishedEvent(
                    billing_project=PROJECT,
                    location=LOCATION,
                    query_id="abcdefg",
                    total_rows=100,
                    total_bytes_processed=123,
                    slot_millis=987,
                    created=created,
                    started=started,
                    ended=ended,
                    # No job ID or destination, because a basic query is eligible for jobs.query.
                    job_id=None,
                    destination=None,
                ),
            ),
        ]
    )


def _to_millis(dt: datetime.datetime) -> str:
    return str(
        int(
            (dt - datetime.datetime(1970, 1, 1, 0, 0, 0, tzinfo=datetime.timezone.utc))
            / datetime.timedelta(milliseconds=1)
        )
    )


def test_query_and_wait_bigframes_with_jobs_insert_callback_empty_results(client):
    client._http.request.side_effect = [
        # jobs.insert because destination table present in job_config
        make_response(
            {
                # https://cloud.google.com/bigquery/docs/reference/rest/v2/jobs/insert
                # https://cloud.google.com/bigquery/docs/reference/rest/v2/Job
                "jobReference": {
                    "projectId": "response-project",
                    "jobId": "response-job-id",
                    "location": "response-location",
                },
                "statistics": {
                    "creationTime": _to_millis(
                        datetime.datetime(
                            2025, 8, 13, 13, 7, 31, 123000, tzinfo=datetime.timezone.utc
                        )
                    ),
                    "query": {
                        "statementType": "SELECT",
                        # "queryPlan": [{"name": "part1"}, {"name": "part2"}],
                    },
                },
                "status": {
                    "state": "PENDING",
                },
            }
        ),
        # jobs.get waiting for query to finish
        make_response(
            {
                # https://cloud.google.com/bigquery/docs/reference/rest/v2/jobs/insert
                # https://cloud.google.com/bigquery/docs/reference/rest/v2/Job
                "jobReference": {
                    "projectId": "response-project",
                    "jobId": "response-job-id",
                    "location": "response-location",
                },
                "status": {
                    "state": "PENDING",
                },
            }
        ),
        # jobs.getQueryResults with max_results=0
        make_response(
            {
                "jobReference": {
                    "projectId": "response-project",
                    "jobId": "response-job-id",
                    "location": "response-location",
                },
                "jobComplete": True,
                # totalRows is intentionally missing so we end up in the _EmptyRowIterator code path.
            }
        ),
        # jobs.get
        make_response(
            {
                "jobReference": {
                    "projectId": "response-project",
                    "jobId": "response-job-id",
                    "location": "response-location",
                },
                "statistics": {
                    "creationTime": _to_millis(
                        datetime.datetime(
                            2025, 8, 13, 13, 7, 31, 123000, tzinfo=datetime.timezone.utc
                        )
                    ),
                    "startTime": _to_millis(
                        datetime.datetime(
                            2025, 8, 13, 13, 7, 32, 123000, tzinfo=datetime.timezone.utc
                        )
                    ),
                    "endTime": _to_millis(
                        datetime.datetime(
                            2025, 8, 13, 13, 7, 33, 123000, tzinfo=datetime.timezone.utc
                        )
                    ),
                    "query": {
                        "statementType": "SELECT",
                        "totalBytesProcessed": 123,
                        "totalSlotMs": 987,
                    },
                },
                "status": {"state": "DONE"},
            }
        ),
    ]
    callback = mock.Mock()
    config = bigquery.QueryJobConfig()
    config.destination = "proj.dset.table"
    client._query_and_wait_bigframes(
        query="SELECT 1", job_config=config, callback=callback
    )
    callback.assert_has_calls(
        [
            mock.call(
                _job_helpers.QuerySentEvent(
                    query="SELECT 1",
                    billing_project="response-project",
                    location="response-location",
                    job_id="response-job-id",
                    # We use jobs.insert not jobs.query because destination is
                    # present on job_config.
                    request_id=None,
                )
            ),
            mock.call(
                _job_helpers.QueryReceivedEvent(
                    billing_project="response-project",
                    location="response-location",
                    job_id="response-job-id",
                    statement_type="SELECT",
                    state="PENDING",
                    query_plan=[],
                    created=datetime.datetime(
                        2025, 8, 13, 13, 7, 31, 123000, tzinfo=datetime.timezone.utc
                    ),
                    started=None,
                    ended=None,
                )
            ),
            mock.call(
                _job_helpers.QueryFinishedEvent(
                    billing_project="response-project",
                    location="response-location",
                    job_id="response-job-id",
                    query_id=None,
                    total_rows=0,
                    total_bytes_processed=123,
                    slot_millis=987,
                    created=datetime.datetime(
                        2025, 8, 13, 13, 7, 31, 123000, tzinfo=datetime.timezone.utc
                    ),
                    started=datetime.datetime(
                        2025, 8, 13, 13, 7, 32, 123000, tzinfo=datetime.timezone.utc
                    ),
                    ended=datetime.datetime(
                        2025, 8, 13, 13, 7, 33, 123000, tzinfo=datetime.timezone.utc
                    ),
                    destination=None,
                ),
            ),
        ]
    )


def test_query_and_wait_bigframes_with_jobs_insert_dry_run_no_callback(client):
    client._http.request.side_effect = [
        # jobs.insert because destination table present in job_config
        make_response(
            {
                "jobReference": {
                    "projectId": "response-project",
                    "jobId": "response-job-id",
                    "location": "response-location",
                },
                "statistics": {
                    "creationTime": _to_millis(
                        datetime.datetime(
                            2025, 8, 13, 13, 7, 31, 123000, tzinfo=datetime.timezone.utc
                        )
                    ),
                    "query": {
                        "statementType": "SELECT",
                        "totalBytesProcessed": 123,
                        "schema": {
                            "fields": [
                                {"name": "_f0", "type": "INTEGER"},
                            ],
                        },
                    },
                },
                "configuration": {
                    "dryRun": True,
                },
                "status": {"state": "DONE"},
            }
        ),
    ]
    callback = mock.Mock()
    config = bigquery.QueryJobConfig()
    config.destination = "proj.dset.table"
    config.dry_run = True
    result = client._query_and_wait_bigframes(
        query="SELECT 1", job_config=config, callback=callback
    )
    callback.assert_not_called()
    assert result.total_bytes_processed == 123
    assert result.schema == [bigquery.SchemaField("_f0", "INTEGER")]


def test_query_and_wait_bigframes_with_query_retry_callbacks(client, global_time_lock):
    created = datetime.datetime(
        2025, 8, 18, 10, 11, 12, 345000, tzinfo=datetime.timezone.utc
    )
    started = datetime.datetime(
        2025, 8, 18, 10, 11, 13, 456000, tzinfo=datetime.timezone.utc
    )
    ended = datetime.datetime(
        2025, 8, 18, 10, 11, 14, 567000, tzinfo=datetime.timezone.utc
    )
    client._http.request.side_effect = [
        exceptions.InternalServerError(
            "first try", errors=({"reason": "jobInternalError"},)
        ),
        make_response(
            {
                # https://cloud.google.com/bigquery/docs/reference/rest/v2/jobs/query
                "location": LOCATION,
                "queryId": "abcdefg",
                "totalRows": "100",
                "totalBytesProcessed": "123",
                "totalSlotMs": "987",
                "jobComplete": True,
                "creationTime": _to_millis(created),
                "startTime": _to_millis(started),
                "endTime": _to_millis(ended),
            }
        ),
    ]
    callback = mock.Mock()
    client._query_and_wait_bigframes(query="SELECT 1", callback=callback)
    callback.assert_has_calls(
        [
            mock.call(
                _job_helpers.QuerySentEvent(
                    query="SELECT 1",
                    billing_project=PROJECT,
                    location=LOCATION,
                    # No job ID, because a basic query is eligible for jobs.query.
                    job_id=None,
                    request_id=mock.ANY,
                )
            ),
            mock.call(
                _job_helpers.QueryRetryEvent(
                    query="SELECT 1",
                    billing_project=PROJECT,
                    location=LOCATION,
                    # No job ID, because a basic query is eligible for jobs.query.
                    job_id=None,
                    request_id=mock.ANY,
                )
            ),
            mock.call(
                _job_helpers.QueryFinishedEvent(
                    billing_project=PROJECT,
                    location=LOCATION,
                    query_id=mock.ANY,
                    total_rows=100,
                    total_bytes_processed=123,
                    slot_millis=987,
                    created=created,
                    started=started,
                    ended=ended,
                    # No job ID or destination, because a basic query is eligible for jobs.query.
                    job_id=None,
                    destination=None,
                ),
            ),
        ]
    )
