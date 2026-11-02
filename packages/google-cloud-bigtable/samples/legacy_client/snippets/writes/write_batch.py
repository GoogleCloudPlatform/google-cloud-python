#!/usr/bin/env python

# Copyright 2019, Google LLC
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# [START bigtable_writes_batch_legacy]
from datetime import datetime, timezone

from google.cloud import bigtable
from google.cloud.bigtable.batcher import MutationsBatcher


def write_batch(project_id, instance_id, table_id):
    client = bigtable.Client(project=project_id, admin=True)
    instance = client.instance(instance_id)
    table = instance.table(table_id)

    with MutationsBatcher(table=table) as batcher:
        timestamp = datetime.now(timezone.utc)
        column_family_id = "stats_summary"

        rows = [
            table.direct_row("tablet#a0b81f74#20190501"),
            table.direct_row("tablet#a0b81f74#20190502"),
        ]

        rows[0].set_cell(column_family_id, "connected_wifi", 1, timestamp)
        rows[0].set_cell(column_family_id, "os_build", "12155.0.0-rc1", timestamp)
        rows[1].set_cell(column_family_id, "connected_wifi", 1, timestamp)
        rows[1].set_cell(column_family_id, "os_build", "12145.0.0-rc6", timestamp)

        batcher.mutate_rows(rows)

    print("Successfully wrote 2 rows.")


# [END bigtable_writes_batch_legacy]
