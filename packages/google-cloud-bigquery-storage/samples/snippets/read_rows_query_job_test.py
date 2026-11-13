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

import pyarrow

from . import read_rows_query_job


def test_read_rows_query_job():
    batches = read_rows_query_job.read_rows_query_job()

    total_rows = 0
    batch_count = 0
    for batch in batches:
        assert isinstance(batch, pyarrow.RecordBatch)
        assert batch.schema.names == ["name", "number", "state"]
        assert batch.schema.field("name").type == pyarrow.string()
        assert batch.schema.field("number").type == pyarrow.int64()
        assert batch.schema.field("state").type == pyarrow.string()
        total_rows += batch.num_rows
        batch_count += 1

    assert total_rows == 20000
    assert batch_count > 0
