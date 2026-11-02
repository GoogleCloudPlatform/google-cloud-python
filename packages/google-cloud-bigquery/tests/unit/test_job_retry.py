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
import re
from unittest import mock

import pytest

import google.api_core.exceptions
import google.api_core.retry
import freezegun
import requests.exceptions

from google.cloud.bigquery import _job_helpers
import google.cloud.bigquery.retry

from .helpers import make_client, make_connection


_RETRY_NOT_FOUND = {
    "job_retry": google.api_core.retry.Retry(
        predicate=google.api_core.retry.if_exception_type(
            google.api_core.exceptions.NotFound,
        ),
    ),
}
_RETRY_BAD_REQUEST = {
    "job_retry": google.api_core.retry.Retry(
        predicate=google.api_core.retry.if_exception_type(
            google.api_core.exceptions.BadRequest,
        ),
    ),
}


# Test retry of job failures, instead of API-invocation failures. 4 scenarios:
# - No `job_retry` passed, retry on default rateLimitExceeded.
# - Pass NotFound retry to `query`.
# - Pass NotFound retry to `result`.
# - Pass BadRequest retry to query, with the value passed to `result` overriding.
@mock.patch("time.sleep")
@pytest.mark.parametrize(
    "reason, job_retry, result_retry",
    [
        pytest.param(
            "rateLimitExceeded",
            {},
            {},
            id="no job_retry",
        ),
        pytest.param(
            "notFound",
            _RETRY_NOT_FOUND,
            {},
            id="Query NotFound",
        ),
        pytest.param(
            "notFound",
            _RETRY_NOT_FOUND,
            _RETRY_NOT_FOUND,
            id="Result NotFound",
        ),
        pytest.param(
            "notFound",
            _RETRY_BAD_REQUEST,
            _RETRY_NOT_FOUND,
            id="BadRequest",
        ),
    ],
)
def test_retry_failed_jobs(sleep, reason, job_retry, result_retry, global_time_lock):
    client = make_client()
    err = dict(reason=reason)
    conn = client._connection = make_connection(
        dict(
            status=dict(state="DONE", errors=[err], errorResult=err),
            jobReference={"jobId": "id_1"},
        ),
        dict(
            status=dict(state="DONE", errors=[err], errorResult=err),
            jobReference={"jobId": "id_1"},
        ),
        dict(
            status=dict(state="DONE", errors=[err], errorResult=err),
            jobReference={"jobId": "id_1"},
        ),
        dict(status=dict(state="DONE"), jobReference={"jobId": "id_2"}),
        dict(rows=[{"f": [{"v": "1"}]}], totalRows="1"),
    )

    job = client.query("select 1", **job_retry)
    result = job.result(**result_retry)

    assert result.total_rows == 1

    # We made all the calls we expected to.
    assert conn.api_request.call_count == 5

    # The job adjusts it's job id based on the id of the last attempt.
    assert job.job_id == "id_2"

    # We had to sleep three times
    assert len(sleep.mock_calls) == 3

    # Sleeps are random, however they're more than 0
    assert min(c[1][0] for c in sleep.mock_calls) > 0

    # They're at most 2 * (multiplier**(number of sleeps - 1)) * initial
    # The default multiplier is 2
    assert max(c[1][0] for c in sleep.mock_calls) <= 8

    # We can ask for the result again:
    conn = client._connection = make_connection(
        dict(rows=[{"f": [{"v": "1"}]}], totalRows="1"),
    )
    result = job.result()

    assert result.total_rows == 1

    # We made all the calls we expected to.
    assert conn.api_request.call_count == 1

    # We wouldn't (and didn't) fail, because we're dealing with a successful job.
    # So the job id hasn't changed.
    assert job.job_id == "id_2"


def test_retry_connection_error_with_default_retries_and_successful_first_job(
    monkeypatch, client, global_time_lock
):
    """
    Make sure ConnectionError can be retried at `is_job_done` level, even if
    retries are exhaused by API-level retry.

    Note: Because restart_query_job is set to True only in the case of a
    confirmed job failure, this should be safe to do even when a job is not
    idempotent.

    Regression test for issue
    https://github.com/googleapis/python-bigquery/issues/1929
    """
    job_counter = 0

    def make_job_id(*args, **kwargs):
        nonlocal job_counter
        job_counter += 1
        return f"{job_counter}"

    monkeypatch.setattr(_job_helpers, "make_job_id", make_job_id)
    conn = client._connection = make_connection()
    project = client.project
    job_reference_1 = {"projectId": project, "jobId": "1", "location": "test-loc"}
    NUM_API_RETRIES = 2

    with freezegun.freeze_time(
        "2024-01-01 00:00:00",
        # Note: because of exponential backoff and a bit of jitter,
        # NUM_API_RETRIES will get less accurate the greater the value.
        # We add 1 because we know there will be at least some additional
        # calls to fetch the time / sleep before the retry deadline is hit.
        auto_tick_seconds=(
            google.cloud.bigquery.retry._DEFAULT_RETRY_DEADLINE / NUM_API_RETRIES
        )
        + 1,
    ):
        conn.api_request.side_effect = [
            # jobs.insert
            {"jobReference": job_reference_1, "status": {"state": "PENDING"}},
            # jobs.get
            {"jobReference": job_reference_1, "status": {"state": "RUNNING"}},
            # jobs.getQueryResults x2
            requests.exceptions.ConnectionError(),
            requests.exceptions.ConnectionError(),
            # jobs.get
            # Job actually succeeeded, so we shouldn't be restarting the job,
            # even though we are retrying at the `is_job_done` level.
            {"jobReference": job_reference_1, "status": {"state": "DONE"}},
            # jobs.getQueryResults
            {"jobReference": job_reference_1, "jobComplete": True},
        ]

        job = client.query("select 1")
        rows_iter = job.result()

    assert job.done()  # Shouldn't make any additional API calls.
    assert rows_iter is not None

    # Should only have created one job, even though we did call job_retry.
    assert job_counter == 1

    # Double-check that we made the API calls we expected to make.
    conn.api_request.assert_has_calls(
        [
            # jobs.insert
            mock.call(
                method="POST",
                path="/projects/PROJECT/jobs",
                data={
                    "jobReference": {"jobId": "1", "projectId": "PROJECT"},
                    "configuration": {
                        "query": {"useLegacySql": False, "query": "select 1"}
                    },
                },
                timeout=None,
            ),
            # jobs.get
            mock.call(
                method="GET",
                path="/projects/PROJECT/jobs/1",
                query_params={"location": "test-loc", "projection": "full"},
                timeout=google.cloud.bigquery.retry.DEFAULT_GET_JOB_TIMEOUT,
            ),
            # jobs.getQueryResults x2
            mock.call(
                method="GET",
                path="/projects/PROJECT/queries/1",
                query_params={"maxResults": 0, "location": "test-loc"},
                timeout=None,
            ),
            mock.call(
                method="GET",
                path="/projects/PROJECT/queries/1",
                query_params={"maxResults": 0, "location": "test-loc"},
                timeout=None,
            ),
            # jobs.get -- is_job_done checking again
            mock.call(
                method="GET",
                path="/projects/PROJECT/jobs/1",
                query_params={"location": "test-loc", "projection": "full"},
                timeout=google.cloud.bigquery.retry.DEFAULT_GET_JOB_TIMEOUT,
            ),
            # jobs.getQueryResults
            mock.call(
                method="GET",
                path="/projects/PROJECT/queries/1",
                query_params={"maxResults": 0, "location": "test-loc"},
                timeout=None,
            ),
        ],
    )


def test_query_retry_with_default_retry_and_ambiguous_errors_only_retries_with_failed_job(
    client, monkeypatch, global_time_lock
):
    """
    Some errors like 'rateLimitExceeded' can be ambiguous. Make sure we only
    retry the job when we know for sure that the job has failed for a retriable
    reason. We can only be sure after a "successful" call to jobs.get to fetch
    the failed job status.
    """
    job_counter = 0

    def make_job_id(*args, **kwargs):
        nonlocal job_counter
        job_counter += 1
        return f"{job_counter}"

    monkeypatch.setattr(_job_helpers, "make_job_id", make_job_id)

    project = client.project
    job_reference_1 = {"projectId": project, "jobId": "1", "location": "test-loc"}
    job_reference_2 = {"projectId": project, "jobId": "2", "location": "test-loc"}
    NUM_API_RETRIES = 2

    # This error is modeled after a real customer exception in
    # https://github.com/googleapis/python-bigquery/issues/707.
    internal_error = google.api_core.exceptions.InternalServerError(
        "Job failed just because...",
        errors=[
            {"reason": "internalError"},
        ],
    )
    responses = [
        # jobs.insert
        {"jobReference": job_reference_1, "status": {"state": "PENDING"}},
        # jobs.get
        {"jobReference": job_reference_1, "status": {"state": "RUNNING"}},
        # jobs.getQueryResults x2
        #
        # Note: internalError is ambiguous in jobs.getQueryResults. The
        # problem could be at the Google Frontend level or it could be because
        # the job has failed due to some transient issues and the BigQuery
        # REST API is translating the job failed status into failure HTTP
        # codes.
        #
        # TODO(GH#1903): We shouldn't retry nearly this many times when we get
        # ambiguous errors from jobs.getQueryResults.
        # See: https://github.com/googleapis/python-bigquery/issues/1903
        internal_error,
        internal_error,
        # jobs.get -- the job has failed
        {
            "jobReference": job_reference_1,
            "status": {"state": "DONE", "errorResult": {"reason": "internalError"}},
        },
        # jobs.insert
        {"jobReference": job_reference_2, "status": {"state": "PENDING"}},
        # jobs.get
        {"jobReference": job_reference_2, "status": {"state": "RUNNING"}},
        # jobs.getQueryResults
        {"jobReference": job_reference_2, "jobComplete": True},
        # jobs.get
        {"jobReference": job_reference_2, "status": {"state": "DONE"}},
    ]

    conn = client._connection = make_connection(*responses)

    with freezegun.freeze_time(
        # Note: because of exponential backoff and a bit of jitter,
        # NUM_API_RETRIES will get less accurate the greater the value.
        # We add 1 because we know there will be at least some additional
        # calls to fetch the time / sleep before the retry deadline is hit.
        auto_tick_seconds=(
            google.cloud.bigquery.retry._DEFAULT_RETRY_DEADLINE / NUM_API_RETRIES
        )
        + 1,
    ):
        job = client.query("select 1")
        job.result()

    conn.api_request.assert_has_calls(
        [
            # jobs.insert
            mock.call(
                method="POST",
                path="/projects/PROJECT/jobs",
                data={
                    "jobReference": {"jobId": "1", "projectId": "PROJECT"},
                    "configuration": {
                        "query": {"useLegacySql": False, "query": "select 1"}
                    },
                },
                timeout=None,
            ),
            # jobs.get
            mock.call(
                method="GET",
                path="/projects/PROJECT/jobs/1",
                query_params={"location": "test-loc", "projection": "full"},
                timeout=google.cloud.bigquery.retry.DEFAULT_GET_JOB_TIMEOUT,
            ),
            # jobs.getQueryResults x2
            mock.call(
                method="GET",
                path="/projects/PROJECT/queries/1",
                query_params={"maxResults": 0, "location": "test-loc"},
                timeout=None,
            ),
            mock.call(
                method="GET",
                path="/projects/PROJECT/queries/1",
                query_params={"maxResults": 0, "location": "test-loc"},
                timeout=None,
            ),
            # jobs.get -- verify that the job has failed
            mock.call(
                method="GET",
                path="/projects/PROJECT/jobs/1",
                query_params={"location": "test-loc", "projection": "full"},
                timeout=google.cloud.bigquery.retry.DEFAULT_GET_JOB_TIMEOUT,
            ),
            # jobs.insert
            mock.call(
                method="POST",
                path="/projects/PROJECT/jobs",
                data={
                    "jobReference": {
                        # Make sure that we generated a new job ID.
                        "jobId": "2",
                        "projectId": "PROJECT",
                    },
                    "configuration": {
                        "query": {"useLegacySql": False, "query": "select 1"}
                    },
                },
                timeout=None,
            ),
            # jobs.get
            mock.call(
                method="GET",
                path="/projects/PROJECT/jobs/2",
                query_params={"location": "test-loc", "projection": "full"},
                timeout=google.cloud.bigquery.retry.DEFAULT_GET_JOB_TIMEOUT,
            ),
            # jobs.getQueryResults
            mock.call(
                method="GET",
                path="/projects/PROJECT/queries/2",
                query_params={"maxResults": 0, "location": "test-loc"},
                timeout=None,
            ),
            # jobs.get
            mock.call(
                method="GET",
                path="/projects/PROJECT/jobs/2",
                query_params={"location": "test-loc", "projection": "full"},
                timeout=google.cloud.bigquery.retry.DEFAULT_GET_JOB_TIMEOUT,
            ),
        ]
    )


# With job_retry_on_query, we're testing 4 scenarios:
# - Pass None retry to `query`.
# - Pass None retry to `result`.
@pytest.mark.parametrize("job_retry_on_query", ["Query", "Result"])
@mock.patch("time.sleep")
def test_disable_retry_failed_jobs(sleep, client, job_retry_on_query, global_time_lock):
    """
    Test retry of job failures, as opposed to API-invocation failures.
    """
    err = dict(reason="rateLimitExceeded")
    responses = [dict(status=dict(state="DONE", errors=[err], errorResult=err))] * 3

    def api_request(method, path, query_params=None, data=None, **kw):
        response = responses.pop(0)
        response["jobReference"] = data["jobReference"]
        return response

    conn = client._connection = make_connection()
    conn.api_request.side_effect = api_request

    if job_retry_on_query == "Query":
        job_retry = dict(job_retry=None)
    else:
        job_retry = {}
    job = client.query("select 1", **job_retry)

    orig_job_id = job.job_id
    job_retry = dict(job_retry=None) if job_retry_on_query == "Result" else {}
    with pytest.raises(google.api_core.exceptions.TooManyRequests):
        job.result(**job_retry)

    assert job.job_id == orig_job_id
    assert len(sleep.mock_calls) == 0


@mock.patch("time.sleep")
def test_retry_failed_jobs_after_retry_failed(sleep, client, global_time_lock):
    """
    If at first you don't succeed, maybe you will later. :)
    """
    conn = client._connection = make_connection()

    with freezegun.freeze_time("2024-01-01 00:00:00") as frozen_datetime:
        err = dict(reason="rateLimitExceeded")

        def api_request(method, path, query_params=None, data=None, **kw):
            calls = sleep.mock_calls
            if calls:
                frozen_datetime.tick(delta=datetime.timedelta(seconds=calls[-1][1][0]))
            response = dict(status=dict(state="DONE", errors=[err], errorResult=err))
            response["jobReference"] = data["jobReference"]
            return response

        conn.api_request.side_effect = api_request

        job = client.query("select 1")
        orig_job_id = job.job_id

        with pytest.raises(google.api_core.exceptions.RetryError):
            job.result()

        # We retried the job at least once, so we should have generated a new job ID.
        assert job.job_id != orig_job_id

        # We failed because we couldn't succeed after 120 seconds.
        # But we can try again:
        err2 = dict(reason="backendError")  # We also retry on this
        responses = [
            dict(status=dict(state="DONE", errors=[err2], errorResult=err2)),
            dict(status=dict(state="DONE", errors=[err], errorResult=err)),
            dict(status=dict(state="DONE", errors=[err2], errorResult=err2)),
            dict(status=dict(state="DONE")),
            dict(rows=[{"f": [{"v": "1"}]}], totalRows="1"),
        ]

        def api_request(method, path, query_params=None, data=None, **kw):
            calls = sleep.mock_calls
            frozen_datetime.tick(delta=datetime.timedelta(seconds=calls[-1][1][0]))
            response = responses.pop(0)
            if data:
                response["jobReference"] = data["jobReference"]
            else:
                response["jobReference"] = dict(
                    jobId=path.split("/")[-1], projectId="PROJECT"
                )
            return response

        conn.api_request.side_effect = api_request
        result = job.result()
        assert result.total_rows == 1
        assert not responses  # We made all the calls we expected to.
        assert job.job_id != orig_job_id


def test_raises_on_job_retry_on_query_with_non_retryable_jobs(client, global_time_lock):
    with pytest.raises(
        TypeError,
        match=(
            "`job_retry` was provided, but the returned job is"
            " not retryable, because a custom `job_id` was"
            " provided."
        ).replace(" ", r"\s"),
    ):
        client.query("select 42", job_id=42, job_retry=google.api_core.retry.Retry())


def test_raises_on_job_retry_on_result_with_non_retryable_jobs(
    client, global_time_lock
):
    client._connection = make_connection({})

    with pytest.warns(
        FutureWarning,
        match=re.escape("job_retry must be explicitly set to None if job_id is set."),
    ):
        # Implicitly providing a job_retry is a warning and will be an error in the future.
        job = client.query("select 42", job_id=42)

    with pytest.raises(
        TypeError,
        match=(
            "`job_retry` was provided, but this job is"
            " not retryable, because a custom `job_id` was"
            " provided to the query that created this job."
        ).replace(" ", r"\s"),
    ):
        # Explicitly providing a job_retry is an error.
        job.result(job_retry=google.api_core.retry.Retry())


def test_query_and_wait_retries_job_for_DDL_queries(global_time_lock):
    """
    Specific test for retrying DDL queries with "jobRateLimitExceeded" error:
    https://github.com/googleapis/python-bigquery/issues/1790
    """
    freezegun.freeze_time(auto_tick_seconds=1)

    client = make_client()
    conn = client._connection = make_connection(
        {
            "jobReference": {
                "projectId": "response-project",
                "jobId": "abc",
                "location": "response-location",
            },
            "jobComplete": False,
        },
        google.api_core.exceptions.InternalServerError(
            "job_retry me", errors=[{"reason": "jobRateLimitExceeded"}]
        ),
        google.api_core.exceptions.BadRequest(
            "retry me", errors=[{"reason": "jobRateLimitExceeded"}]
        ),
        {
            "jobReference": {
                "projectId": "response-project",
                "jobId": "abc",
                "location": "response-location",
            },
            "jobComplete": True,
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
        },
    )
    rows = _job_helpers.query_and_wait(
        client,
        query="SELECT 1",
        location="request-location",
        project="request-project",
        job_config=None,
        page_size=None,
        max_results=None,
        retry=google.cloud.bigquery.retry.DEFAULT_RETRY,
        job_retry=google.cloud.bigquery.retry.DEFAULT_JOB_RETRY,
    )
    assert len(list(rows)) == 4

    # Relevant docs for the REST API path: https://cloud.google.com/bigquery/docs/reference/rest/v2/jobs/query
    # and https://cloud.google.com/bigquery/docs/reference/rest/v2/jobs/getQueryResults
    query_request_path = "/projects/request-project/queries"

    calls = conn.api_request.call_args_list
    _, kwargs = calls[0]
    assert kwargs["method"] == "POST"
    assert kwargs["path"] == query_request_path

    # TODO: Add assertion statements for response paths after PR#1797 is fixed

    _, kwargs = calls[3]
    assert kwargs["method"] == "POST"
    assert kwargs["path"] == query_request_path


@pytest.mark.parametrize(
    "result_retry_param",
    [
        pytest.param(
            {},
            id="default retry {}",
        ),
        pytest.param(
            {
                "retry": google.cloud.bigquery.retry.DEFAULT_RETRY.with_timeout(
                    timeout=10.0
                )
            },
            id="custom retry object with timeout 10.0",
        ),
    ],
)
def test_retry_load_job_result(result_retry_param, PROJECT, DS_ID):
    from google.cloud.bigquery.dataset import DatasetReference
    from google.cloud.bigquery.job.load import LoadJob
    import google.cloud.bigquery.retry

    client = make_client()
    conn = client._connection = make_connection(
        dict(
            status=dict(state="RUNNING"),
            jobReference={"jobId": "id_1"},
        ),
        google.api_core.exceptions.ServiceUnavailable("retry me"),
        dict(
            status=dict(state="DONE"),
            jobReference={"jobId": "id_1"},
            statistics={"load": {"outputRows": 1}},
        ),
    )

    table_ref = DatasetReference(project=PROJECT, dataset_id=DS_ID).table("new_table")
    job = LoadJob("id_1", source_uris=None, destination=table_ref, client=client)

    with mock.patch.object(
        client, "_call_api", wraps=client._call_api
    ) as wrapped_call_api:
        result = job.result(**result_retry_param)

    assert job.state == "DONE"
    assert result.output_rows == 1

    # Check that _call_api was called multiple times due to retry
    assert wrapped_call_api.call_count > 1

    # Verify the retry object used in the calls to _call_api
    expected_retry = result_retry_param.get(
        "retry", google.cloud.bigquery.retry.DEFAULT_RETRY
    )

    for call in wrapped_call_api.mock_calls:
        name, args, kwargs = call
        # The retry object is the first positional argument to _call_api
        called_retry = args[0]

        # We only care about the calls made during the job.result() polling
        if kwargs.get("method") == "GET" and "jobs/id_1" in kwargs.get("path", ""):
            assert called_retry._predicate == expected_retry._predicate
            assert called_retry._initial == expected_retry._initial
            assert called_retry._maximum == expected_retry._maximum
            assert called_retry._multiplier == expected_retry._multiplier
            assert called_retry._deadline == expected_retry._deadline
            if "retry" in result_retry_param:
                # Specifically check the timeout for the custom retry case
                assert called_retry._timeout == 10.0
            else:
                assert called_retry._timeout == expected_retry._timeout

    # The number of api_request calls should still be 3
    assert conn.api_request.call_count == 3
