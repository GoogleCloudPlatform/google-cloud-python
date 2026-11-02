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

import google.api_core.retry
import google.cloud.bigquery.job
from google.api_core import exceptions

from . import helpers

PROJECT = "test-project"
JOB_ID = "test-job-id"


def test_cancel_w_custom_retry(global_time_lock):
    api_path = "/projects/{}/jobs/{}/cancel".format(PROJECT, JOB_ID)
    resource = {
        "jobReference": {
            "jobId": JOB_ID,
            "projectId": PROJECT,
            "location": None,
        },
        "configuration": {"test": True},
    }
    expected = resource.copy()
    expected["statistics"] = {}
    response = {"job": resource}
    conn = helpers.make_connection(
        ValueError,
        response,
    )
    client = helpers._make_client(project=PROJECT, connection=conn)
    job = google.cloud.bigquery.job._AsyncJob(
        google.cloud.bigquery.job._JobReference(JOB_ID, PROJECT, "EU"), client
    )

    retry = google.api_core.retry.Retry(
        predicate=lambda exc: isinstance(exc, ValueError),
        initial=0.01,
        maximum=0.01,
        deadline=1.0,
    )

    with mock.patch(
        "google.cloud.bigquery.opentelemetry_tracing._get_final_span_attributes"
    ) as final_attributes:
        result = job.cancel(retry=retry, timeout=7.5)

    final_attributes.assert_called()

    assert result is True
    assert job._properties == expected
    conn.api_request.assert_has_calls(
        [
            mock.call(
                method="POST",
                path=api_path,
                query_params={"location": "EU"},
                timeout=7.5,
            ),
            mock.call(
                method="POST",
                path=api_path,
                query_params={"location": "EU"},
                timeout=7.5,
            ),  # was retried once
        ],
    )


def test_result_w_retry_wo_state(global_time_lock):
    from google.cloud.bigquery.retry import DEFAULT_GET_JOB_TIMEOUT

    begun_job_resource = helpers._make_job_resource(
        job_id=JOB_ID, project_id=PROJECT, location="EU", started=True
    )
    done_job_resource = helpers._make_job_resource(
        job_id=JOB_ID,
        project_id=PROJECT,
        location="EU",
        started=True,
        ended=True,
    )
    conn = helpers.make_connection(
        exceptions.NotFound("not normally retriable"),
        begun_job_resource,
        exceptions.NotFound("not normally retriable"),
        done_job_resource,
    )
    client = helpers._make_client(project=PROJECT, connection=conn)
    job = google.cloud.bigquery.job._AsyncJob(
        google.cloud.bigquery.job._JobReference(JOB_ID, PROJECT, "EU"), client
    )
    custom_predicate = mock.Mock()
    custom_predicate.return_value = True
    custom_retry = google.api_core.retry.Retry(
        predicate=custom_predicate,
        initial=0.001,
        maximum=0.001,
        deadline=1.0,
    )
    assert job.result(retry=custom_retry) is job

    begin_call = mock.call(
        method="POST",
        path=f"/projects/{PROJECT}/jobs",
        data={
            "jobReference": {
                "jobId": JOB_ID,
                "projectId": PROJECT,
                "location": "EU",
            }
        },
        timeout=None,
    )
    reload_call = mock.call(
        method="GET",
        path=f"/projects/{PROJECT}/jobs/{JOB_ID}",
        query_params={
            "projection": "full",
            "location": "EU",
        },
        timeout=DEFAULT_GET_JOB_TIMEOUT,
    )
    conn.api_request.assert_has_calls(
        [begin_call, begin_call, reload_call, reload_call]
    )
