#!/usr/bin/env python

# Copyright 2026 Google LLC
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


# [START bigtable_delete_from_column]
def delete_from_column(project_id, instance_id, table_id):
    from google.cloud.bigtable.data import (
        BigtableDataClient,
        DeleteRangeFromColumn,
    )

    client = BigtableDataClient(project=project_id)
    table = client.get_table(instance_id, table_id)

    table.mutate_row(
        "phone#4c410523#20190501",
        DeleteRangeFromColumn(family="cell_plan", qualifier=b"data_plan_01gb"),
    )

    table.close()
    client.close()


# [END bigtable_delete_from_column]


# [START bigtable_delete_from_column_family]
def delete_from_column_family(project_id, instance_id, table_id):
    from google.cloud.bigtable.data import BigtableDataClient, DeleteAllFromFamily

    client = BigtableDataClient(project=project_id)
    table = client.get_table(instance_id, table_id)

    table.mutate_row("phone#4c410523#20190501", DeleteAllFromFamily("cell_plan"))

    table.close()
    client.close()


# [END bigtable_delete_from_column_family]


# [START bigtable_delete_from_row]
def delete_from_row(project_id, instance_id, table_id):
    from google.cloud.bigtable.data import BigtableDataClient, DeleteAllFromRow

    client = BigtableDataClient(project=project_id)
    table = client.get_table(instance_id, table_id)

    table.mutate_row("phone#4c410523#20190501", DeleteAllFromRow())

    table.close()
    client.close()


# [END bigtable_delete_from_row]


# [START bigtable_streaming_and_batching]
def streaming_and_batching(project_id, instance_id, table_id):
    from google.cloud.bigtable.data import (
        BigtableDataClient,
        DeleteRangeFromColumn,
        ReadRowsQuery,
        RowMutationEntry,
    )

    client = BigtableDataClient(project=project_id)
    table = client.get_table(instance_id, table_id)

    with table.mutations_batcher() as batcher:
        for row in table.read_rows_stream(ReadRowsQuery(limit=10)):
            batcher.append(
                RowMutationEntry(
                    row.row_key,
                    DeleteRangeFromColumn(
                        family="cell_plan", qualifier=b"data_plan_01gb"
                    ),
                )
            )

    table.close()
    client.close()


# [END bigtable_streaming_and_batching]


# [START bigtable_check_and_mutate]
def check_and_mutate(project_id, instance_id, table_id):
    from google.cloud.bigtable.data import (
        BigtableDataClient,
        DeleteRangeFromColumn,
    )
    from google.cloud.bigtable.data.row_filters import LiteralValueFilter

    client = BigtableDataClient(project=project_id)
    table = client.get_table(instance_id, table_id)

    table.check_and_mutate_row(
        "phone#4c410523#20190501",
        predicate=LiteralValueFilter("PQ2A.190405.003"),
        true_case_mutations=DeleteRangeFromColumn(
            family="cell_plan", qualifier=b"data_plan_01gb"
        ),
    )

    table.close()
    client.close()


# [END bigtable_check_and_mutate]


# [START bigtable_drop_row_range]
def drop_row_range(project_id, instance_id, table_id):
    from google.cloud import bigtable_admin_v2

    client = bigtable_admin_v2.BigtableTableAdminClient()
    table_path = client.table_path(project_id, instance_id, table_id)
    row_key_prefix = b"phone#4c410523"
    client.drop_row_range(
        request={
            "name": table_path,
            "row_key_prefix": row_key_prefix,
        },
        timeout=200,
    )


# [END bigtable_drop_row_range]


# [START bigtable_delete_column_family]
def delete_column_family(project_id, instance_id, table_id):
    from google.cloud import bigtable_admin_v2

    client = bigtable_admin_v2.BigtableTableAdminClient()
    table_path = client.table_path(project_id, instance_id, table_id)
    column_family_id = "stats_summary"
    modification = bigtable_admin_v2.ModifyColumnFamiliesRequest.Modification(
        id=column_family_id, drop=True
    )
    client.modify_column_families(name=table_path, modifications=[modification])


# [END bigtable_delete_column_family]
