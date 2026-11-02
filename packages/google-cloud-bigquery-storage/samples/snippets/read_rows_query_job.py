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

# [START bigquerystorage_read_rows_query_job]
from typing import Iterable, Optional

import pyarrow

from google.cloud import bigquery, bigquery_storage_v1


def read_rows_query_job() -> Iterable[pyarrow.RecordBatch]:
    """Queries BigQuery and yields batches directly via BigQueryReadClient using a job stream.

    Yields:
        pyarrow.RecordBatch: Apache Arrow RecordBatch objects streamed from BigQuery.
    """
    # Initialize BigQuery and BigQuery Storage clients.
    client = bigquery.Client()
    read_client = bigquery_storage_v1.BigQueryReadClient()

    query = """
        SELECT name, number, state
        FROM `bigquery-public-data.usa_names.usa_1910_current`
        LIMIT 20000
    """

    # Start the query job.
    job = client.query(query)

    # Construct the job default stream name.
    # Format: projects/{project_id}/locations/{location}/jobs/{job_id}/streams/_default
    stream = f"projects/{job.project}/locations/{job.location}/jobs/{job.job_id}/streams/_default"

    # Read rows directly from the stream using the Storage Read API.
    schema: Optional[pyarrow.Schema] = None

    for chunk in read_client.read_rows(name=stream, offset=0):
        # Extract the schema from the first chunk that provides it.
        if (
            schema is None
            and chunk.arrow_schema
            and chunk.arrow_schema.serialized_schema
        ):
            schema = pyarrow.ipc.read_schema(
                pyarrow.py_buffer(chunk.arrow_schema.serialized_schema)
            )

        # Deserialize and yield each record batch using the schema.
        if (
            chunk.arrow_record_batch
            and chunk.arrow_record_batch.serialized_record_batch
        ):
            yield pyarrow.ipc.read_record_batch(
                pyarrow.py_buffer(chunk.arrow_record_batch.serialized_record_batch),
                schema,
            )


# [END bigquerystorage_read_rows_query_job]
