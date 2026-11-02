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

import contextlib
import threading
import time

import google.api_core.exceptions
import google.cloud.bigquery
import pytest


def thread(func):
    thread = threading.Thread(target=func, daemon=True)
    thread.start()
    return thread


@pytest.mark.parametrize("job_retry_on_query", [True, False])
def test_query_retry_539(bigquery_client, dataset_id, job_retry_on_query):
    """
    Test job_retry

    See: https://github.com/googleapis/python-bigquery/issues/539
    """
    from google.api_core import exceptions
    from google.api_core.retry import if_exception_type, Retry

    table_name = f"{dataset_id}.t539"

    # Without a custom retry, we fail:
    with pytest.raises(google.api_core.exceptions.NotFound):
        bigquery_client.query(f"select count(*) from {table_name}").result()

    retry_notfound = Retry(predicate=if_exception_type(exceptions.NotFound))

    job_retry = dict(job_retry=retry_notfound) if job_retry_on_query else {}
    job = bigquery_client.query(f"select count(*) from {table_name}", **job_retry)
    job_id = job.job_id

    # We can already know that the job failed, but we're not supposed
    # to find out until we call result, which is where retry happend
    assert job.done()
    assert job.exception() is not None

    @thread
    def create_table():
        time.sleep(1)  # Give the first retry attempt time to fail.
        with contextlib.closing(google.cloud.bigquery.Client()) as client:
            client.query(f"create table {table_name} (id int64)").result()

    job_retry = {} if job_retry_on_query else dict(job_retry=retry_notfound)
    [[count]] = list(job.result(**job_retry))
    assert count == 0

    # The job was retried, and thus got a new job id
    assert job.job_id != job_id

    # Make sure we don't leave a thread behind:
    create_table.join()
    bigquery_client.query(f"drop table {table_name}").result()
