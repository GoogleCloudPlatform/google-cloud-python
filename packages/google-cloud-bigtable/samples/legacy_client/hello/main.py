#!/usr/bin/env python

# Copyright 2016 Google Inc.
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

"""Demonstrates how to connect to Cloud Bigtable and run some basic operations.

Prerequisites:

- Create a Cloud Bigtable instance.
  https://cloud.google.com/bigtable/docs/creating-instance
- Set your Google Application Default Credentials.
  https://developers.google.com/identity/protocols/application-default-credentials
"""

import argparse

# [START bigtable_hw_imports_legacy]
from datetime import datetime, timezone

from google.cloud import bigtable
from google.cloud.bigtable import column_family, row_filters

from ...utils import wait_for_table

# [END bigtable_hw_imports_legacy]

# use to avoid warnings
row_filters
column_family


def main(project_id, instance_id, table_id):
    # [START bigtable_hw_connect_legacy]
    # The client must be created with admin=True because it will create a
    # table.
    client = bigtable.Client(project=project_id, admin=True)
    instance = client.instance(instance_id)
    # [END bigtable_hw_connect_legacy]

    # [START bigtable_hw_create_table_legacy]
    print("Creating the {} table.".format(table_id))
    table = instance.table(table_id)

    print("Creating column family cf1 with Max Version GC rule...")
    # Create a column family with GC policy : most recent N versions
    # Define the GC policy to retain only the most recent 2 versions
    max_versions_rule = bigtable.column_family.MaxVersionsGCRule(2)
    column_family_id = b"cf1"
    column_families = {column_family_id: max_versions_rule}
    if not table.exists():
        table.create(column_families=column_families)
    else:
        print("Table {} already exists.".format(table_id))
    # [END bigtable_hw_create_table_legacy]

    try:
        # let table creation complete
        wait_for_table(table)

        # [START bigtable_hw_write_rows_legacy]
        print("Writing some greetings to the table.")
        greetings = [b"Hello World!", b"Hello Cloud Bigtable!", b"Hello Python!"]
        rows = []
        column = b"greeting"
        for i, value in enumerate(greetings):
            # Note: This example uses sequential numeric IDs for simplicity,
            # but this can result in poor performance in a production
            # application.  Since rows are stored in sorted order by key,
            # sequential keys can result in poor distribution of operations
            # across nodes.
            #
            # We recommend that you use bytestrings directly for row keys
            # where possible, rather than encoding strings.
            #
            # For more information about how to design a Bigtable schema for
            # the best performance, see the documentation:
            #
            #     https://cloud.google.com/bigtable/docs/schema-design
            row_key = f"greeting{i}".encode()
            row = table.direct_row(row_key)
            row.set_cell(
                column_family_id,
                column,
                value,
                timestamp=datetime.now(timezone.utc),
            )
            rows.append(row)
        table.mutate_rows(rows)
        # [END bigtable_hw_write_rows_legacy]

        # [START bigtable_hw_create_filter_legacy]
        # Create a filter to only retrieve the most recent version of the cell
        # for each column across entire row.
        row_filter = bigtable.row_filters.CellsColumnLimitFilter(1)
        # [END bigtable_hw_create_filter_legacy]

        # [START bigtable_hw_get_with_filter_legacy]
        # [START bigtable_hw_get_by_key_legacy]
        print("Getting a single greeting by row key.")
        key = b"greeting0"

        row = table.read_row(key, row_filter)
        cell = row.cells[column_family_id.decode("utf-8")][column][0]
        print(cell.value.decode("utf-8"))
        # [END bigtable_hw_get_by_key_legacy]
        # [END bigtable_hw_get_with_filter_legacy]

        # [START bigtable_hw_scan_with_filter_legacy]
        # [START bigtable_hw_scan_all_legacy]
        print("Scanning for all greetings:")
        partial_rows = table.read_rows(filter_=row_filter)

        for row in partial_rows:
            column_family_id_str = column_family_id.decode("utf-8")
            cell = row.cells[column_family_id_str][column][0]
            print(cell.value.decode("utf-8"))
        # [END bigtable_hw_scan_all_legacy]
        # [END bigtable_hw_scan_with_filter_legacy]

    finally:
        # [START bigtable_hw_delete_table_legacy]
        print("Deleting the {} table.".format(table_id))
        table.delete()
        # [END bigtable_hw_delete_table_legacy]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument("project_id", help="Your Cloud Platform project ID.")
    parser.add_argument(
        "instance_id", help="ID of the Cloud Bigtable instance to connect to."
    )
    parser.add_argument(
        "--table", help="Table to create and destroy.", default="Hello-Bigtable"
    )

    args = parser.parse_args()
    main(args.project_id, args.instance_id, args.table)
