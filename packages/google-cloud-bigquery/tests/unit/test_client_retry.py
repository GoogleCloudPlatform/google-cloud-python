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

from unittest import mock

import freezegun
import google.api_core.exceptions
from google.cloud.bigquery import job as bqjob
from google.cloud.bigquery.retry import DEFAULT_RETRY
from .helpers import make_connection


PROJECT = "test-project"

# A deadline > 1.0s is required because the default retry (google.api_core.retry.Retry)
# has an initial delay of 1.0s. If the deadline is <= 1.0s, the first retry attempt
# (scheduled for now + 1.0s) will be rejected immediately as exceeding the deadline.
_RETRY_DEADLINE = 10.0


def _make_credentials():
    import google.auth.credentials

    return mock.Mock(spec=google.auth.credentials.Credentials)


def _make_client(*args, **kw):
    from google.cloud.bigquery.client import Client

    return Client(*args, **kw)


def test_get_service_account_email_w_custom_retry(global_time_lock):
    api_path = f"/projects/{PROJECT}/serviceAccount"
    creds = _make_credentials()
    http = object()
    client = _make_client(project=PROJECT, credentials=creds, _http=http)

    resource = {
        "kind": "bigquery#getServiceAccountResponse",
        "email": "bq-123@bigquery-encryption.iam.gserviceaccount.com",
    }
    api_request_patcher = mock.patch.object(
        client._connection,
        "api_request",
        side_effect=[ValueError, resource],
    )

    retry = DEFAULT_RETRY.with_deadline(1).with_predicate(
        lambda exc: isinstance(exc, ValueError)
    )

    with api_request_patcher as fake_api_request:
        with mock.patch(
            "google.cloud.bigquery.opentelemetry_tracing._get_final_span_attributes"
        ) as final_attributes:
            service_account_email = client.get_service_account_email(
                retry=retry, timeout=7.5
            )

    final_attributes.assert_called_once_with({"path": api_path}, client, None)
    assert service_account_email == "bq-123@bigquery-encryption.iam.gserviceaccount.com"
    assert fake_api_request.call_args_list == [
        mock.call(method="GET", path=api_path, timeout=7.5),
        mock.call(method="GET", path=api_path, timeout=7.5),  # was retried once
    ]


def test_call_api_applying_custom_retry_on_timeout(global_time_lock):
    from concurrent.futures import TimeoutError

    creds = _make_credentials()
    client = _make_client(project=PROJECT, credentials=creds)

    api_request_patcher = mock.patch.object(
        client._connection,
        "api_request",
        side_effect=[TimeoutError, "result"],
    )
    retry = DEFAULT_RETRY.with_deadline(_RETRY_DEADLINE).with_predicate(
        lambda exc: isinstance(exc, TimeoutError)
    )

    with api_request_patcher as fake_api_request:
        result = client._call_api(retry, foo="bar")

    assert result == "result"
    assert fake_api_request.call_args_list == [
        mock.call(foo="bar"),
        mock.call(foo="bar"),
    ]


def test_query_job_rpc_fail_w_conflict_random_id_job_fetch_retries_404(
    global_time_lock,
):
    """Regression test for https://github.com/googleapis/python-bigquery/issues/2134

    Sometimes after a Conflict, the fetch fails with a 404, but we know
    because of the conflict that really the job does exist. Retry until we
    get the job status (or timeout).
    """
    job_id = "abc123"
    creds = _make_credentials()
    http = object()
    client = _make_client(project=PROJECT, credentials=creds, _http=http)
    conn = client._connection = make_connection(
        # We're mocking QueryJob._begin, so this is only going to be
        # jobs.get requests and responses.
        google.api_core.exceptions.TooManyRequests("this is retriable by default"),
        google.api_core.exceptions.NotFound("we lost your job"),
        google.api_core.exceptions.NotFound("we lost your job again, sorry"),
        {
            "jobReference": {
                "projectId": PROJECT,
                "location": "TESTLOC",
                "jobId": job_id,
            }
        },
    )

    job_create_error = google.api_core.exceptions.Conflict("Job already exists.")
    job_begin_patcher = mock.patch.object(
        bqjob.QueryJob, "_begin", side_effect=job_create_error
    )
    job_id_patcher = mock.patch.object(
        google.cloud.bigquery._job_helpers,
        "make_job_id",
        return_value=job_id,
    )

    with job_begin_patcher, job_id_patcher:
        # If get job request fails there does exist a job
        # with this ID already, retry 404 until we get it (or fails for a
        # non-retriable reason, see other tests).
        result = client.query("SELECT 1;", job_id=None)

    jobs_get_path = mock.call(
        method="GET",
        path=f"/projects/{PROJECT}/jobs/{job_id}",
        query_params={
            "projection": "full",
        },
        timeout=google.cloud.bigquery.retry.DEFAULT_GET_JOB_TIMEOUT,
    )
    conn.api_request.assert_has_calls(
        # Double-check that it was jobs.get that was called for each of our
        # mocked responses.
        [jobs_get_path]
        * 4,
    )
    assert result.job_id == job_id


def test_query_job_rpc_fail_w_conflict_random_id_job_fetch_retries_404_and_query_job_insert(
    global_time_lock,
):
    """Regression test for https://github.com/googleapis/python-bigquery/issues/2134

    Sometimes after a Conflict, the fetch fails with a 404. If it keeps
    failing with a 404, assume that the job actually doesn't exist.
    """
    job_id_1 = "abc123"
    job_id_2 = "xyz789"
    creds = _make_credentials()
    http = object()
    client = _make_client(project=PROJECT, credentials=creds, _http=http)

    # We're mocking QueryJob._begin, so that the connection should only get
    # jobs.get requests.
    job_create_error = google.api_core.exceptions.Conflict("Job already exists.")
    job_begin_patcher = mock.patch.object(
        bqjob.QueryJob, "_begin", side_effect=job_create_error
    )
    conn = client._connection = make_connection(
        google.api_core.exceptions.NotFound("we lost your job again, sorry"),
        {
            "jobReference": {
                "projectId": PROJECT,
                "location": "TESTLOC",
                "jobId": job_id_2,
            }
        },
    )

    # Choose a small deadline so the 404 retries give up.
    retry = google.cloud.bigquery.retry._DEFAULT_GET_JOB_CONFLICT_RETRY.with_deadline(1)
    job_id_patcher = mock.patch.object(
        google.cloud.bigquery._job_helpers,
        "make_job_id",
        side_effect=[job_id_1, job_id_2],
    )
    retry_patcher = mock.patch.object(
        google.cloud.bigquery.retry,
        "_DEFAULT_GET_JOB_CONFLICT_RETRY",
        retry,
    )

    with freezegun.freeze_time(
        "2025-01-01 00:00:00",
        # 10x the retry deadline to guarantee a timeout.
        auto_tick_seconds=10,
    ), job_begin_patcher, job_id_patcher, retry_patcher:
        # If get job request fails there does exist a job
        # with this ID already, retry 404 until we get it (or fails for a
        # non-retriable reason, see other tests).
        result = client.query("SELECT 1;", job_id=None)

    jobs_get_path_1 = mock.call(
        method="GET",
        path=f"/projects/{PROJECT}/jobs/{job_id_1}",
        query_params={
            "projection": "full",
        },
        timeout=google.cloud.bigquery.retry.DEFAULT_GET_JOB_TIMEOUT,
    )
    jobs_get_path_2 = mock.call(
        method="GET",
        path=f"/projects/{PROJECT}/jobs/{job_id_2}",
        query_params={
            "projection": "full",
        },
        timeout=google.cloud.bigquery.retry.DEFAULT_GET_JOB_TIMEOUT,
    )
    conn.api_request.assert_has_calls(
        # Double-check that it was jobs.get that was called for each of our
        # mocked responses.
        [jobs_get_path_1, jobs_get_path_2],
    )
    assert result.job_id == job_id_2


def test_query_job_rpc_fail_w_conflict_random_id_job_fetch_retry(global_time_lock):
    """Regression test for https://github.com/googleapis/python-bigquery/issues/2134

    If we get a 409 conflict on jobs.insert, and we are using a random
    job ID, we should retry by getting the job by ID. This test ensures that
    if the get job by ID fails, we retry the whole sequence.
    """
    from google.cloud.bigquery import job

    client = _make_client(project=PROJECT, credentials=_make_credentials())
    job_id = "some-random-job-id"
    query_text = "SELECT 1"
    job_config = job.QueryJobConfig()
    job_config.use_legacy_sql = False

    job_resource = {
        "jobReference": {"projectId": PROJECT, "jobId": job_id},
        "configuration": {"query": {"query": query_text}},
        "status": {"state": "DONE"},
    }

    conn = make_connection(
        # First attempt at jobs.insert fails with a 409
        google.api_core.exceptions.Conflict("Job already exists."),
        # First attempt at jobs.get fails with a 500
        google.api_core.exceptions.InternalServerError("get job failed"),
        # Second attempt at jobs.insert succeeds
        job_resource,
    )
    client._connection = conn

    job_id_patcher = mock.patch.object(
        google.cloud.bigquery._job_helpers,
        "make_job_id",
        return_value=job_id,
    )

    with job_id_patcher:
        query_job = client.query(query_text, job_config=job_config, job_id=None)

    assert query_job.job_id == job_id
