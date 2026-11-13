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

# [START bigquerystorage_query_and_wait_arrow]
from typing import Iterable

import pyarrow
from google.cloud.bigquery import enums

from google.cloud import bigquery


def query_and_wait_arrow() -> Iterable[pyarrow.RecordBatch]:
    """Queries BigQuery and returns results as an iterable of Apache Arrow RecordBatches.

    Returns:
        Iterable[pyarrow.RecordBatch]: An iterable of Apache Arrow RecordBatch objects.
    """
    # Initialize a BigQuery client.
    client = bigquery.Client()

    query = """
        SELECT name, number, state
        FROM `bigquery-public-data.usa_names.usa_1910_current`
        LIMIT 100000
    """

    # Run the query and wait for results returned directly in Arrow format
    # compressed with LZ4_FRAME.
    results = client.query_and_wait(
        query,
        query_results_format=enums.QueryResultsFormat.ARROW,
        compression_codec=enums.QueryResultsCompressionCodec.LZ4_FRAME,
    )

    # Return results as an iterable of pyarrow.RecordBatch objects.
    # Each batch contains a slice of the rows in Apache Arrow format.
    batches = results.to_arrow_iterable()
    return batches


# [END bigquerystorage_query_and_wait_arrow]
