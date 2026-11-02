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

import time

import pyarrow as pa
import pytest

from . import append_rows_with_arrow


def create_table_with_batches(num_batches, rows_per_batch):
    # Generate a small table to get a valid batch
    small_table = append_rows_with_arrow.generate_pyarrow_table(rows_per_batch)
    # Ensure we get exactly one batch for the small table
    batches = small_table.to_batches()
    assert len(batches) == 1
    batch = batches[0]

    # Replicate the batch
    all_batches = [batch] * num_batches
    return pa.Table.from_batches(all_batches)


# Test generate_write_requests with different numbers of batches in the input table.
# The total rows in the generated table is constantly 1000000.
@pytest.mark.parametrize(
    "num_batches, rows_per_batch, expected_requests",
    [
        (1, 1000000, 32),
        (10, 100000, 40),
        (100, 10000, 34),
        (1000, 1000, 26),
        (10000, 100, 26),
        (100000, 10, 26),
        (1000000, 1, 26),
    ],
)
def test_generate_write_requests_varying_batches(
    num_batches, rows_per_batch, expected_requests
):
    """Test generate_write_requests with different numbers of batches in the input table."""
    # Create a table that returns `num_batches` when to_batches() is called.
    table = create_table_with_batches(num_batches, rows_per_batch)

    # Verify our setup is correct
    assert len(table.to_batches()) == num_batches

    # Generate requests
    start_time = time.perf_counter()
    requests = list(append_rows_with_arrow.generate_write_requests(table))
    end_time = time.perf_counter()
    print(
        f"\nTime used to generate requests for {num_batches} batches: {end_time - start_time:.4f} seconds"
    )

    assert len(requests) == expected_requests

    # Verify total rows in requests matches total rows in table
    total_rows_processed = 0
    for request in requests:
        # Deserialize the batch from the request to count rows
        serialized_batch = request.arrow_rows.rows.serialized_record_batch

        # Verify the batch size is less than 7MB
        assert len(serialized_batch) <= 7 * 1024 * 1024

        # We need a schema to read the batch. The schema is PYARROW_SCHEMA.
        batch = pa.ipc.read_record_batch(
            serialized_batch, append_rows_with_arrow.PYARROW_SCHEMA
        )
        total_rows_processed += batch.num_rows

    expected_rows = num_batches * rows_per_batch
    assert total_rows_processed == expected_rows
