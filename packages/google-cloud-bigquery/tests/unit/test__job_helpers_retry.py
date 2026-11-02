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

import freezegun
import google.api_core.exceptions
from google.api_core import retry as retries
import pytest

from google.cloud.bigquery import _job_helpers

from . import helpers


def test_query_and_wait_retries_job(global_time_lock):
    with freezegun.freeze_time(auto_tick_seconds=100):
        conn = helpers.make_connection(
            google.api_core.exceptions.BadGateway("retry me"),
            google.api_core.exceptions.InternalServerError("job_retry me"),
            google.api_core.exceptions.BadGateway("retry me"),
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
        client = helpers.make_client(project="client-project")
        client._connection = conn
        rows = _job_helpers.query_and_wait(
            client,
            query="SELECT 1",
            location="request-location",
            project="request-project",
            job_config=None,
            page_size=None,
            max_results=None,
            retry=retries.Retry(
                lambda exc: isinstance(exc, google.api_core.exceptions.BadGateway),
                multiplier=1.0,
            ).with_deadline(
                200.0
            ),  # Since auto_tick_seconds is 100, we should get at least 1 retry.
            job_retry=retries.Retry(
                lambda exc: isinstance(
                    exc, google.api_core.exceptions.InternalServerError
                ),
                multiplier=1.0,
            ).with_deadline(600.0),
        )
        assert len(list(rows)) == 4

        # For this code path, where the query has finished immediately, we should
        # only be calling the jobs.query API and no other request path.
        request_path = "/projects/request-project/queries"
        for call in client._connection.api_request.call_args_list:
            _, kwargs = call
            assert kwargs["method"] == "POST"
            assert kwargs["path"] == request_path


def test_query_and_wait_retries_job_times_out(global_time_lock):
    with freezegun.freeze_time(auto_tick_seconds=100):
        conn = helpers.make_connection(
            google.api_core.exceptions.BadGateway("retry me"),
            google.api_core.exceptions.InternalServerError("job_retry me"),
            google.api_core.exceptions.BadGateway("retry me"),
            google.api_core.exceptions.InternalServerError("job_retry me"),
        )
        client = helpers.make_client(project="client-project")
        client._connection = conn

        with pytest.raises(google.api_core.exceptions.RetryError) as exc_info:
            _job_helpers.query_and_wait(
                client,
                query="SELECT 1",
                location="request-location",
                project="request-project",
                job_config=None,
                page_size=None,
                max_results=None,
                retry=retries.Retry(
                    lambda exc: isinstance(exc, google.api_core.exceptions.BadGateway),
                    multiplier=1.0,
                ).with_deadline(
                    200.0
                ),  # Since auto_tick_seconds is 100, we should get at least 1 retry.
                job_retry=retries.Retry(
                    lambda exc: isinstance(
                        exc, google.api_core.exceptions.InternalServerError
                    ),
                    multiplier=1.0,
                ).with_deadline(400.0),
            )

        assert isinstance(
            exc_info.value.cause, google.api_core.exceptions.InternalServerError
        )
