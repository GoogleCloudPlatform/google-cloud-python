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

"""Demonstrates how to create, manage, and use a Bigtable authorized view
with the asyncio clients.

Prerequisites:

- Create a Cloud Bigtable instance.
  https://cloud.google.com/bigtable/docs/creating-instance
- Set your Google Application Default Credentials.
  https://developers.google.com/identity/protocols/application-default-credentials
"""

import argparse
import asyncio

from google.api_core.exceptions import NotFound, PermissionDenied
from google.protobuf import field_mask_pb2

from google.cloud import bigtable_admin_v2
from google.cloud.bigtable.data import (
    BigtableDataClientAsync,
    ReadRowsQuery,
    SetCell,
    row_filters,
)

COLUMN_FAMILY = "cf"
COLUMN_QUALIFIER_GREETING = "greeting"
COLUMN_QUALIFIER_NAME = "name"
ROW_KEY_PREFIX = "rowKey"


async def run(project_id, instance_id, table_id, authorized_view_id):
    await create_table(project_id, instance_id, table_id)
    await create_authorized_view(project_id, instance_id, table_id, authorized_view_id)
    await update_authorized_view(project_id, instance_id, table_id, authorized_view_id)
    await get_authorized_view(project_id, instance_id, table_id, authorized_view_id)
    await list_authorized_views(project_id, instance_id, table_id)
    await write_to_authorized_view(
        project_id, instance_id, table_id, authorized_view_id
    )
    await read_single_row_from_authorized_view(
        project_id, instance_id, table_id, authorized_view_id
    )
    await read_rows_with_filter_from_authorized_view(
        project_id, instance_id, table_id, authorized_view_id
    )
    await delete_authorized_view(project_id, instance_id, table_id, authorized_view_id)
    await delete_table(project_id, instance_id, table_id)


async def create_table(project_id, instance_id, table_id):
    # Checks if the table exists, creates it if it does not exist.
    async with bigtable_admin_v2.BigtableTableAdminAsyncClient() as admin_client:
        table_path = admin_client.table_path(project_id, instance_id, table_id)
        try:
            await admin_client.get_table(
                request={
                    "name": table_path,
                    "view": bigtable_admin_v2.Table.View.NAME_ONLY,
                }
            )
        except NotFound:
            print(f"Table does not exist, creating table: {table_id}")
            table = await admin_client.create_table(
                parent=admin_client.instance_path(project_id, instance_id),
                table_id=table_id,
                table=bigtable_admin_v2.Table(
                    column_families={COLUMN_FAMILY: bigtable_admin_v2.ColumnFamily()}
                ),
            )
            print(f"Table: {table.name} created successfully")


async def delete_table(project_id, instance_id, table_id):
    # Deletes the entire table.
    print(f"\nDelete table: {table_id}")
    async with bigtable_admin_v2.BigtableTableAdminAsyncClient() as admin_client:
        try:
            await admin_client.delete_table(
                name=admin_client.table_path(project_id, instance_id, table_id)
            )
            print(f"Table: {table_id} deleted successfully")
        except NotFound as e:
            print(f"Failed to delete a non-existent table: {e.message}")


async def create_authorized_view(project_id, instance_id, table_id, authorized_view_id):
    """Creates an authorized view under a table with the specified configuration."""
    print(f"\nCreating authorized view {authorized_view_id} in table {table_id}")
    # [START bigtable_async_create_authorized_view]
    async with bigtable_admin_v2.BigtableTableAdminAsyncClient() as admin_client:
        table_path = admin_client.table_path(project_id, instance_id, table_id)

        # Permit every row, but only the "name" column of the column family.
        subset_view = bigtable_admin_v2.AuthorizedView.SubsetView(
            row_prefixes=[b""],
            family_subsets={
                COLUMN_FAMILY: bigtable_admin_v2.AuthorizedView.FamilySubsets(
                    qualifier_prefixes=[COLUMN_QUALIFIER_NAME.encode()]
                )
            },
        )
        operation = await admin_client.create_authorized_view(
            parent=table_path,
            authorized_view_id=authorized_view_id,
            authorized_view=bigtable_admin_v2.AuthorizedView(subset_view=subset_view),
        )
        authorized_view = await operation.result()
        print(f"AuthorizedView: {authorized_view.name} created successfully")
    # [END bigtable_async_create_authorized_view]


async def update_authorized_view(project_id, instance_id, table_id, authorized_view_id):
    """Modifies an authorized view."""
    print(f"\nUpdating authorized view {authorized_view_id} in table {table_id}")
    # [START bigtable_async_update_authorized_view]
    async with bigtable_admin_v2.BigtableTableAdminAsyncClient() as admin_client:
        authorized_view_path = admin_client.authorized_view_path(
            project_id, instance_id, table_id, authorized_view_id
        )

        # Update to an authorized view permitting everything.
        subset_view = bigtable_admin_v2.AuthorizedView.SubsetView(
            row_prefixes=[b""],
            family_subsets={
                COLUMN_FAMILY: bigtable_admin_v2.AuthorizedView.FamilySubsets(
                    qualifier_prefixes=[b""]
                )
            },
        )
        operation = await admin_client.update_authorized_view(
            authorized_view=bigtable_admin_v2.AuthorizedView(
                name=authorized_view_path, subset_view=subset_view
            ),
            update_mask=field_mask_pb2.FieldMask(paths=["subset_view"]),
        )
        authorized_view = await operation.result()
        print(f"AuthorizedView: {authorized_view.name} updated successfully")
    # [END bigtable_async_update_authorized_view]


async def get_authorized_view(project_id, instance_id, table_id, authorized_view_id):
    """Gets an authorized view's metadata."""
    print(f"\nGetting authorized view {authorized_view_id} in table {table_id}")
    # [START bigtable_async_get_authorized_view]
    async with bigtable_admin_v2.BigtableTableAdminAsyncClient() as admin_client:
        authorized_view_path = admin_client.authorized_view_path(
            project_id, instance_id, table_id, authorized_view_id
        )

        try:
            authorized_view = await admin_client.get_authorized_view(
                name=authorized_view_path
            )
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
    # [END bigtable_async_get_authorized_view]


async def list_authorized_views(project_id, instance_id, table_id):
    """Lists all authorized views within a table."""
    print(f"\nListing authorized views in table {table_id}")
    # [START bigtable_async_list_authorized_views]
    async with bigtable_admin_v2.BigtableTableAdminAsyncClient() as admin_client:
        table_path = admin_client.table_path(project_id, instance_id, table_id)

        try:
            async for authorized_view in await admin_client.list_authorized_views(
                parent=table_path
            ):
                authorized_view_id = admin_client.parse_authorized_view_path(
                    authorized_view.name
                )["authorized_view"]
                print(authorized_view_id)
        except NotFound as e:
            print(
                "Failed to list authorized views from a non-existent table: "
                f"{e.message}"
            )
    # [END bigtable_async_list_authorized_views]


async def delete_authorized_view(project_id, instance_id, table_id, authorized_view_id):
    """Deletes an authorized view."""
    print(f"\nDeleting authorized view {authorized_view_id} in table {table_id}")
    # [START bigtable_async_delete_authorized_view]
    async with bigtable_admin_v2.BigtableTableAdminAsyncClient() as admin_client:
        authorized_view_path = admin_client.authorized_view_path(
            project_id, instance_id, table_id, authorized_view_id
        )

        try:
            await admin_client.delete_authorized_view(name=authorized_view_path)
            print(f"AuthorizedView: {authorized_view_id} deleted successfully")
        except NotFound as e:
            print(f"Failed to delete a non-existent authorized view: {e.message}")
    # [END bigtable_async_delete_authorized_view]


async def write_to_authorized_view(
    project_id, instance_id, table_id, authorized_view_id
):
    """Writes some rows to an authorized view."""
    # [START bigtable_async_authorized_view_write_rows]
    async with BigtableDataClientAsync(project=project_id) as client:
        async with client.get_authorized_view(
            instance_id, table_id, authorized_view_id
        ) as authorized_view:
            try:
                print("\nWriting to authorized view")
                names = ["World", "Bigtable", "Python"]
                for i, name in enumerate(names):
                    greeting = f"Hello {name}!"
                    await authorized_view.mutate_row(
                        f"{ROW_KEY_PREFIX}{i}",
                        [
                            SetCell(COLUMN_FAMILY, COLUMN_QUALIFIER_NAME, name),
                            SetCell(COLUMN_FAMILY, COLUMN_QUALIFIER_GREETING, greeting),
                        ],
                    )
                    print(greeting)
            except NotFound as e:
                print(f"Failed to write to non-existent authorized view: {e.message}")
            except PermissionDenied as e:
                print(
                    "Failed to apply mutations outside of the authorized view: "
                    f"{e.message}"
                )
    # [END bigtable_async_authorized_view_write_rows]


async def read_single_row_from_authorized_view(
    project_id, instance_id, table_id, authorized_view_id
):
    """Reads a single row from an authorized view."""
    # [START bigtable_async_authorized_view_get_by_key]
    async with BigtableDataClientAsync(project=project_id) as client:
        async with client.get_authorized_view(
            instance_id, table_id, authorized_view_id
        ) as authorized_view:
            try:
                print("\nReading a single row by row key from an authorized view")
                row = await authorized_view.read_row(f"{ROW_KEY_PREFIX}0")
                print(f"Row: {row.row_key.decode()}")
                for cell in row.cells:
                    print(
                        f"Family: {cell.family}    "
                        f"Qualifier: {cell.qualifier.decode()}    "
                        f"Value: {cell.value.decode()}"
                    )
            except NotFound as e:
                print(
                    f"Failed to read from a non-existent authorized view: {e.message}"
                )
    # [END bigtable_async_authorized_view_get_by_key]


async def read_rows_with_filter_from_authorized_view(
    project_id, instance_id, table_id, authorized_view_id
):
    """Reads rows from an authorized view with a filter."""
    # [START bigtable_async_authorized_view_scan_with_filter]
    async with BigtableDataClientAsync(project=project_id) as client:
        async with client.get_authorized_view(
            instance_id, table_id, authorized_view_id
        ) as authorized_view:
            try:
                # A filter that matches only the most recent cell within each column
                row_filter = row_filters.CellsColumnLimitFilter(1)
                print("\nScanning authorized view with filter")
                query = ReadRowsQuery(row_filter=row_filter)
                async for row in await authorized_view.read_rows_stream(query):
                    print(f"Row Key: {row.row_key.decode()}")
                    for cell in row.cells:
                        print(
                            f"Family: {cell.family}    "
                            f"Qualifier: {cell.qualifier.decode()}    "
                            f"Value: {cell.value.decode()}"
                        )
            except NotFound as e:
                print(f"Failed to read a non-existent authorized view: {e.message}")
    # [END bigtable_async_authorized_view_scan_with_filter]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument("project_id", help="Your Cloud Platform project ID.")
    parser.add_argument(
        "instance_id", help="ID of the Cloud Bigtable instance to connect to."
    )
    parser.add_argument(
        "--table", help="Table to create and destroy.", default="test-table"
    )
    parser.add_argument(
        "--authorized_view",
        help="Authorized view to create and destroy.",
        default="test-authorized-view",
    )

    args = parser.parse_args()
    asyncio.run(
        run(args.project_id, args.instance_id, args.table, args.authorized_view)
    )
