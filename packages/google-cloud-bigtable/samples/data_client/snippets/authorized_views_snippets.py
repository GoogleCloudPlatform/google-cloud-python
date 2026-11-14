#!/usr/bin/env python

# Copyright 2026 Google LLC
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


# [START bigtable_create_authorized_view]
def create_authorized_view(project_id, instance_id, table_id, authorized_view_id):
    from google.cloud import bigtable_admin_v2

    admin_client = bigtable_admin_v2.BigtableTableAdminClient()
    table_path = admin_client.table_path(project_id, instance_id, table_id)

    column_family_id = "stats_summary"
    # Include only rows with the "phone#" prefix. Use b"" to include all rows.
    row_prefixes = [b"phone#"]

    # Include only "os_build" and columns starting with "connected_".
    family_subset = bigtable_admin_v2.AuthorizedView.FamilySubsets(
        qualifiers=[b"os_build"],
        qualifier_prefixes=[b"connected_"],
    )

    subset_view = bigtable_admin_v2.AuthorizedView.SubsetView(
        row_prefixes=row_prefixes,
        family_subsets={column_family_id: family_subset},
    )
    operation = admin_client.create_authorized_view(
        parent=table_path,
        authorized_view_id=authorized_view_id,
        authorized_view=bigtable_admin_v2.AuthorizedView(subset_view=subset_view),
    )
    authorized_view = operation.result()
    print(f"AuthorizedView: {authorized_view.name} created successfully")


# [END bigtable_create_authorized_view]


# [START bigtable_update_authorized_view]
def update_authorized_view(project_id, instance_id, table_id, authorized_view_id):
    from google.protobuf import field_mask_pb2

    from google.cloud import bigtable_admin_v2

    admin_client = bigtable_admin_v2.BigtableTableAdminClient()
    authorized_view_path = admin_client.authorized_view_path(
        project_id, instance_id, table_id, authorized_view_id
    )

    column_family_id = "stats_summary"
    row_prefixes = [b"phone#", b"tablet#"]
    # An empty prefix includes all columns in the family.
    family_subset = bigtable_admin_v2.AuthorizedView.FamilySubsets(
        qualifier_prefixes=[b""],
    )
    subset_view = bigtable_admin_v2.AuthorizedView.SubsetView(
        row_prefixes=row_prefixes,
        family_subsets={column_family_id: family_subset},
    )

    # Only update the subset_view field.
    update_mask = field_mask_pb2.FieldMask(paths=["subset_view"])

    operation = admin_client.update_authorized_view(
        authorized_view=bigtable_admin_v2.AuthorizedView(
            name=authorized_view_path, subset_view=subset_view
        ),
        update_mask=update_mask,
    )
    authorized_view = operation.result()
    print(f"AuthorizedView: {authorized_view.name} updated successfully")


# [END bigtable_update_authorized_view]


# [START bigtable_get_authorized_view]
def get_authorized_view(project_id, instance_id, table_id, authorized_view_id):
    from google.api_core.exceptions import NotFound

    from google.cloud import bigtable_admin_v2

    admin_client = bigtable_admin_v2.BigtableTableAdminClient()
    authorized_view_path = admin_client.authorized_view_path(
        project_id, instance_id, table_id, authorized_view_id
    )

    try:
        authorized_view = admin_client.get_authorized_view(name=authorized_view_path)
        subset_view = authorized_view.subset_view
        for row_prefix in subset_view.row_prefixes:
            print(f"Row Prefix: {row_prefix.decode()}")
        for family, family_subsets in subset_view.family_subsets.items():
            for qualifier_prefix in family_subsets.qualifier_prefixes:
                print(
                    f"Column Family: {family}, "
                    f"Qualifier Prefix: {qualifier_prefix.decode()}"
                )
            for qualifier in family_subsets.qualifiers:
                print(f"Column Family: {family}, Qualifier: {qualifier.decode()}")
    except NotFound as e:
        print(
            "Failed to retrieve metadata from a non-existent authorized view: "
            f"{e.message}"
        )


# [END bigtable_get_authorized_view]


# [START bigtable_list_authorized_views]
def list_authorized_views(project_id, instance_id, table_id):
    from google.api_core.exceptions import NotFound

    from google.cloud import bigtable_admin_v2

    admin_client = bigtable_admin_v2.BigtableTableAdminClient()
    table_path = admin_client.table_path(project_id, instance_id, table_id)

    try:
        for authorized_view in admin_client.list_authorized_views(parent=table_path):
            # Extract the authorized view ID from the full resource name.
            authorized_view_id = admin_client.parse_authorized_view_path(
                authorized_view.name
            )["authorized_view"]
            print(authorized_view_id)
    except NotFound as e:
        print(f"Failed to list authorized views from a non-existent table: {e.message}")


# [END bigtable_list_authorized_views]


# [START bigtable_delete_authorized_view]
def delete_authorized_view(project_id, instance_id, table_id, authorized_view_id):
    from google.api_core.exceptions import NotFound

    from google.cloud import bigtable_admin_v2

    admin_client = bigtable_admin_v2.BigtableTableAdminClient()
    authorized_view_path = admin_client.authorized_view_path(
        project_id, instance_id, table_id, authorized_view_id
    )

    try:
        admin_client.delete_authorized_view(name=authorized_view_path)
        print(f"AuthorizedView: {authorized_view_id} deleted successfully")
    except NotFound as e:
        print(f"Failed to delete a non-existent authorized view: {e.message}")


# [END bigtable_delete_authorized_view]


# [START bigtable_authorized_view_write_rows]
def write_to_authorized_view(project_id, instance_id, table_id, authorized_view_id):
    from google.api_core.exceptions import NotFound, PermissionDenied

    from google.cloud.bigtable.data import BigtableDataClient, SetCell

    with BigtableDataClient(project=project_id) as client:
        with client.get_authorized_view(
            instance_id, table_id, authorized_view_id
        ) as authorized_view:
            column_family_id = "stats_summary"
            # The row key and columns must be within the authorized view.
            row_key = b"phone#4c410523#20190501"
            mutations = [
                SetCell(column_family_id, b"connected_cell", 1),
                SetCell(column_family_id, b"connected_wifi", 1),
                SetCell(column_family_id, b"os_build", b"PQ2A.190405.003"),
            ]
            try:
                authorized_view.mutate_row(row_key, mutations)
                print(f"Successfully wrote row {row_key.decode()} to authorized view")
            except NotFound as e:
                print(f"Authorized view does not exist: {e.message}")
            except PermissionDenied as e:
                print(
                    "Mutation targets rows or columns outside the authorized view: "
                    f"{e.message}"
                )


# [END bigtable_authorized_view_write_rows]


# [START bigtable_authorized_view_get_by_key]
def read_single_row_from_authorized_view(
    project_id, instance_id, table_id, authorized_view_id
):
    from google.api_core.exceptions import NotFound, PermissionDenied

    from google.cloud.bigtable.data import BigtableDataClient

    with BigtableDataClient(project=project_id) as client:
        with client.get_authorized_view(
            instance_id, table_id, authorized_view_id
        ) as authorized_view:
            row_key = b"phone#4c410523#20190501"
            try:
                row = authorized_view.read_row(row_key)
                if row is not None:
                    print(f"Row key: {row.row_key.decode()}")
                    print(row)
            except NotFound as e:
                print(f"Authorized view does not exist: {e.message}")
            except PermissionDenied as e:
                print(
                    "Row key is outside the authorized view or access was denied: "
                    f"{e.message}"
                )


# [END bigtable_authorized_view_get_by_key]


# [START bigtable_authorized_view_scan_with_filter]
def read_rows_with_filter_from_authorized_view(
    project_id, instance_id, table_id, authorized_view_id
):
    from google.api_core.exceptions import NotFound, PermissionDenied

    from google.cloud.bigtable.data import (
        BigtableDataClient,
        ReadRowsQuery,
        RowRange,
        row_filters,
    )

    with BigtableDataClient(project=project_id) as client:
        with client.get_authorized_view(
            instance_id, table_id, authorized_view_id
        ) as authorized_view:
            # The row range must be within the authorized view.
            row_range = RowRange(
                start_key=b"phone#4c410523#20190501",
                end_key=b"phone#4c410523#20190601",
            )

            # Return only the most recent cell version for each column.
            max_cells_per_column = 1
            row_filter = row_filters.CellsColumnLimitFilter(max_cells_per_column)
            query = ReadRowsQuery(row_ranges=[row_range], row_filter=row_filter)

            try:
                for row in authorized_view.read_rows_stream(query):
                    print(f"Row key: {row.row_key.decode()}")
                    print(row)
            except NotFound as e:
                print(f"Authorized view does not exist: {e.message}")
            except PermissionDenied as e:
                print(
                    "Query targets rows or columns outside the authorized view: "
                    f"{e.message}"
                )


# [END bigtable_authorized_view_scan_with_filter]
