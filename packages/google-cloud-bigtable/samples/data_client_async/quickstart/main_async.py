#!/usr/bin/env python

# Copyright 2024 Google Inc.
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

# [START bigtable_quickstart_asyncio]
import argparse
import asyncio

from google.cloud.bigtable.data import BigtableDataClientAsync


async def main(project_id="project-id", instance_id="instance-id", table_id="my-table"):
    # Create a Cloud Bigtable client.
    client = BigtableDataClientAsync(project=project_id)

    # Open an existing table.
    table = client.get_table(instance_id, table_id)

    row_key = "r1"
    row = await table.read_row(row_key)

    column_family_id = "cf1"
    column_id = b"c1"
    value = row.get_cells(column_family_id, column_id)[0].value.decode("utf-8")

    await table.close()
    await client.close()

    print("Row key: {}\nData: {}".format(row_key, value))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument("project_id", help="Your Cloud Platform project ID.")
    parser.add_argument(
        "instance_id", help="ID of the Cloud Bigtable instance to connect to."
    )
    parser.add_argument(
        "--table", help="Existing table used in the quickstart.", default="my-table"
    )

    args = parser.parse_args()
    asyncio.get_event_loop().run_until_complete(
        main(args.project_id, args.instance_id, args.table)
    )

# [END bigtable_quickstart_asyncio]
