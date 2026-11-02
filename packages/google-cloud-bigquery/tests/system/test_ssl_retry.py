# Copyright 2026 Google LLC
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

import time
from unittest import mock

import pytest
import requests.exceptions
from google.cloud import bigquery


def test_insert_rows_json_ssl_error_no_retry(bigquery_client, dataset_id, project_id):
    """
    Verify that SSLError during insert_rows_json is NOT retried and
    propagates a descriptive error message immediately.
    """
    table_id = f"{project_id}.{dataset_id}.test_ssl_retry_{int(time.time())}"
    schema = [bigquery.SchemaField("name", "STRING")]
    table = bigquery.Table(table_id, schema=schema)
    bigquery_client.create_table(table)
    try:
        # We mock the api_request to simulate the GFE abruptly closing the connection
        # which manifests as a requests.exceptions.SSLError.
        bigquery_client._connection.api_request
        call_count = 0

        def mock_api_request(*args, **kwargs):
            nonlocal call_count
            call_count += 1
            raise requests.exceptions.SSLError("EOF occurred in violation of protocol")

        with mock.patch.object(
            bigquery_client._connection, "api_request", side_effect=mock_api_request
        ):
            # Use a reasonably short deadline for the test, although it should fail on the first attempt anyway.
            retry = bigquery.DEFAULT_RETRY.with_deadline(5.0)

            start_time = time.time()
            with pytest.raises(requests.exceptions.SSLError) as excinfo:
                bigquery_client.insert_rows_json(table, [{"name": "test"}], retry=retry)
            duration = time.time() - start_time

        # Verification:
        # 1. It should NOT have retried (total calls should be 1)
        assert call_count == 1

        # 2. It should have failed quickly (much less than the 5s deadline)
        assert duration < 2.0

        # 3. The error message should contain our descriptive wrapping
        assert "invalid table schema" in str(excinfo.value)
        assert "SSL/Connection error occurred" in str(excinfo.value)
    finally:
        # Cleanup
        bigquery_client.delete_table(table_id)
