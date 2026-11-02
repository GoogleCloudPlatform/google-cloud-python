#!/usr/bin/env python

# Copyright 2024, Google LLC
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


# [START bigtable_delete_from_column_asyncio]
async def delete_from_column(project_id, instance_id, table_id):
    from google.cloud.bigtable.data import (
        BigtableDataClientAsync,
        DeleteRangeFromColumn,
    )

    client = BigtableDataClientAsync(project=project_id)
    table = client.get_table(instance_id, table_id)

    await table.mutate_row(
        "phone#4c410523#20190501",
        DeleteRangeFromColumn(family="cell_plan", qualifier=b"data_plan_01gb"),
    )

    await table.close()
    await client.close()


# [END bigtable_delete_from_column_asyncio]


# [START bigtable_delete_from_column_family_asyncio]
async def delete_from_column_family(project_id, instance_id, table_id):
    from google.cloud.bigtable.data import BigtableDataClientAsync, DeleteAllFromFamily

    client = BigtableDataClientAsync(project=project_id)
    table = client.get_table(instance_id, table_id)

    await table.mutate_row("phone#4c410523#20190501", DeleteAllFromFamily("cell_plan"))

    await table.close()
    await client.close()


# [END bigtable_delete_from_column_family_asyncio]


# [START bigtable_delete_from_row_asyncio]
async def delete_from_row(project_id, instance_id, table_id):
    from google.cloud.bigtable.data import BigtableDataClientAsync, DeleteAllFromRow

    client = BigtableDataClientAsync(project=project_id)
    table = client.get_table(instance_id, table_id)

    await table.mutate_row("phone#4c410523#20190501", DeleteAllFromRow())

    await table.close()
    await client.close()


# [END bigtable_delete_from_row_asyncio]


# [START bigtable_streaming_and_batching_asyncio]
async def streaming_and_batching(project_id, instance_id, table_id):
    from google.cloud.bigtable.data import (
        BigtableDataClientAsync,
        DeleteRangeFromColumn,
        ReadRowsQuery,
        RowMutationEntry,
    )

    client = BigtableDataClientAsync(project=project_id)
    table = client.get_table(instance_id, table_id)

    async with table.mutations_batcher() as batcher:
        async for row in await table.read_rows_stream(ReadRowsQuery(limit=10)):
            await batcher.append(
                RowMutationEntry(
                    row.row_key,
                    DeleteRangeFromColumn(
                        family="cell_plan", qualifier=b"data_plan_01gb"
                    ),
                )
            )

    await table.close()
    await client.close()


# [END bigtable_streaming_and_batching_asyncio]


# [START bigtable_check_and_mutate_asyncio]
async def check_and_mutate(project_id, instance_id, table_id):
    from google.cloud.bigtable.data import (
        BigtableDataClientAsync,
        DeleteRangeFromColumn,
    )
    from google.cloud.bigtable.data.row_filters import LiteralValueFilter

    client = BigtableDataClientAsync(project=project_id)
    table = client.get_table(instance_id, table_id)

    await table.check_and_mutate_row(
        "phone#4c410523#20190501",
        predicate=LiteralValueFilter("PQ2A.190405.003"),
        true_case_mutations=DeleteRangeFromColumn(
            family="cell_plan", qualifier=b"data_plan_01gb"
        ),
    )

    await table.close()
    await client.close()


# [END bigtable_check_and_mutate_asyncio]
