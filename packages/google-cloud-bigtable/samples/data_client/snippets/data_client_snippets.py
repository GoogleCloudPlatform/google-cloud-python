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


def write_simple(table):
    # [START bigtable_writes_simple]
    from google.cloud.bigtable.data import BigtableDataClient, SetCell

    def write_simple(project_id, instance_id, table_id):
        with BigtableDataClient(project=project_id) as client:
            with client.get_table(instance_id, table_id) as table:
                family_id = "stats_summary"
                row_key = b"phone#4c410523#20190501"

                cell_mutation = SetCell(family_id, "connected_cell", 1)
                wifi_mutation = SetCell(family_id, "connected_wifi", 1)
                os_mutation = SetCell(family_id, "os_build", "PQ2A.190405.003")

                table.mutate_row(row_key, cell_mutation)
                table.mutate_row(row_key, wifi_mutation)
                table.mutate_row(row_key, os_mutation)

    # [END bigtable_writes_simple]
    write_simple(table.client.project, table.instance_id, table.table_id)


def write_batch(table):
    # [START bigtable_writes_batch]
    from google.cloud.bigtable.data import BigtableDataClient
    from google.cloud.bigtable.data.exceptions import MutationsExceptionGroup
    from google.cloud.bigtable.data.mutations import RowMutationEntry, SetCell

    def write_batch(project_id, instance_id, table_id):
        with BigtableDataClient(project=project_id) as client:
            with client.get_table(instance_id, table_id) as table:
                family_id = "stats_summary"
                try:
                    with table.mutations_batcher() as batcher:
                        mutation_list = [
                            SetCell(family_id, "connected_cell", 1),
                            SetCell(family_id, "connected_wifi", 1),
                            SetCell(family_id, "os_build", "12155.0.0-rc1"),
                        ]
                        # batcher.append adds the RowMutationEntry to the batcher's
                        # queue to be written in the next flush.
                        batcher.append(
                            RowMutationEntry("tablet#a0b81f74#20190501", mutation_list)
                        )
                        batcher.append(
                            RowMutationEntry("tablet#a0b81f74#20190502", mutation_list)
                        )
                except MutationsExceptionGroup as e:
                    # MutationsExceptionGroup contains a FailedMutationEntryError for
                    # each mutation that failed.
                    for sub_exception in e.exceptions:
                        failed_entry: RowMutationEntry = sub_exception.entry
                        cause: Exception = sub_exception.__cause__
                        print(
                            f"Failed mutation: {failed_entry.row_key} with error: {cause!r}"
                        )

    # [END bigtable_writes_batch]
    write_batch(table.client.project, table.instance_id, table.table_id)


def write_increment(table):
    # [START bigtable_writes_increment]
    from google.cloud.bigtable.data import BigtableDataClient
    from google.cloud.bigtable.data.read_modify_write_rules import IncrementRule

    def write_increment(project_id, instance_id, table_id):
        with BigtableDataClient(project=project_id) as client:
            with client.get_table(instance_id, table_id) as table:
                family_id = "stats_summary"
                row_key = "phone#4c410523#20190501"

                # Decrement the connected_wifi value by 1.
                increment_rule = IncrementRule(
                    family_id, "connected_wifi", increment_amount=-1
                )
                result_row = table.read_modify_write_row(row_key, increment_rule)

                # check result
                cell = result_row[0]
                print(f"{cell.row_key} value: {int(cell)}")

    # [END bigtable_writes_increment]
    write_increment(table.client.project, table.instance_id, table.table_id)


def write_conditional(table):
    # [START bigtable_writes_conditional]
    from google.cloud.bigtable.data import BigtableDataClient, SetCell, row_filters

    def write_conditional(project_id, instance_id, table_id):
        with BigtableDataClient(project=project_id) as client:
            with client.get_table(instance_id, table_id) as table:
                family_id = "stats_summary"
                row_key = "phone#4c410523#20190501"

                row_filter = row_filters.RowFilterChain(
                    filters=[
                        row_filters.FamilyNameRegexFilter(family_id),
                        row_filters.ColumnQualifierRegexFilter("os_build"),
                        row_filters.ValueRegexFilter("PQ2A\\..*"),
                    ]
                )

                if_true = SetCell(family_id, "os_name", "android")
                result = table.check_and_mutate_row(
                    row_key,
                    row_filter,
                    true_case_mutations=if_true,
                    false_case_mutations=None,
                )
                if result is True:
                    print("The row os_name was set to android")

    # [END bigtable_writes_conditional]
    write_conditional(table.client.project, table.instance_id, table.table_id)


def write_aggregate(table):
    # [START bigtable_writes_aggregate]
    import time

    from google.cloud.bigtable.data import BigtableDataClient
    from google.cloud.bigtable.data.exceptions import MutationsExceptionGroup
    from google.cloud.bigtable.data.mutations import AddToCell, RowMutationEntry

    def write_aggregate(project_id, instance_id, table_id):
        """Increments a value in a Bigtable table using AddToCell mutation."""
        with BigtableDataClient(project=project_id) as client:
            with client.get_table(instance_id, table_id) as table:
                row_key = "unique_device_ids_1"
                try:
                    with table.mutations_batcher() as batcher:
                        # The AddToCell mutation increments the value of a cell.
                        # The `counters` family must be set up to be an aggregate
                        # family with an int64 input type.
                        reading = AddToCell(
                            family="counters",
                            qualifier="odometer",
                            value=32304,
                            # Convert nanoseconds to microseconds
                            timestamp_micros=time.time_ns() // 1000,
                        )
                        batcher.append(
                            RowMutationEntry(row_key.encode("utf-8"), [reading])
                        )
                except MutationsExceptionGroup as e:
                    # MutationsExceptionGroup contains a FailedMutationEntryError for
                    # each mutation that failed.
                    for sub_exception in e.exceptions:
                        failed_entry: RowMutationEntry = sub_exception.entry
                        cause: Exception = sub_exception.__cause__
                        print(
                            f"Failed mutation for row {failed_entry.row_key!r} with error: {cause!r}"
                        )

    # [END bigtable_writes_aggregate]
    write_aggregate(table.client.project, table.instance_id, table.table_id)


def read_row(table):
    # [START bigtable_reads_row]
    from google.cloud.bigtable.data import BigtableDataClient

    def read_row(project_id, instance_id, table_id):
        with BigtableDataClient(project=project_id) as client:
            with client.get_table(instance_id, table_id) as table:
                row_key = "phone#4c410523#20190501"
                row = table.read_row(row_key)
                print(row)

    # [END bigtable_reads_row]
    read_row(table.client.project, table.instance_id, table.table_id)


def read_row_partial(table):
    # [START bigtable_reads_row_partial]
    from google.cloud.bigtable.data import BigtableDataClient, row_filters

    def read_row_partial(project_id, instance_id, table_id):
        with BigtableDataClient(project=project_id) as client:
            with client.get_table(instance_id, table_id) as table:
                row_key = "phone#4c410523#20190501"
                col_filter = row_filters.ColumnQualifierRegexFilter(b"os_build")

                row = table.read_row(row_key, row_filter=col_filter)
                print(row)

    # [END bigtable_reads_row_partial]
    read_row_partial(table.client.project, table.instance_id, table.table_id)


def read_rows_multiple(table):
    # [START bigtable_reads_rows]
    from google.cloud.bigtable.data import BigtableDataClient, ReadRowsQuery

    def read_rows(project_id, instance_id, table_id):
        with BigtableDataClient(project=project_id) as client:
            with client.get_table(instance_id, table_id) as table:
                query = ReadRowsQuery(
                    row_keys=[b"phone#4c410523#20190501", b"phone#4c410523#20190502"]
                )
                for row in table.read_rows_stream(query):
                    print(row)

    # [END bigtable_reads_rows]
    read_rows(table.client.project, table.instance_id, table.table_id)


def read_row_range(table):
    # [START bigtable_reads_row_range]
    from google.cloud.bigtable.data import (
        BigtableDataClient,
        ReadRowsQuery,
        RowRange,
    )

    def read_row_range(project_id, instance_id, table_id):
        with BigtableDataClient(project=project_id) as client:
            with client.get_table(instance_id, table_id) as table:
                row_range = RowRange(
                    start_key=b"phone#4c410523#20190501",
                    end_key=b"phone#4c410523#201906201",
                )
                query = ReadRowsQuery(row_ranges=[row_range])

                for row in table.read_rows_stream(query):
                    print(row)

    # [END bigtable_reads_row_range]
    read_row_range(table.client.project, table.instance_id, table.table_id)


def read_row_ranges(table):
    # [START bigtable_reads_row_ranges]
    from google.cloud.bigtable.data import (
        BigtableDataClient,
        ReadRowsQuery,
        RowRange,
    )

    def read_row_ranges(project_id, instance_id, table_id):
        with BigtableDataClient(project=project_id) as client:
            with client.get_table(instance_id, table_id) as table:
                row_ranges = [
                    RowRange(
                        start_key=b"phone#4c410523#20190501",
                        end_key=b"phone#4c410523#201906201",
                    ),
                    RowRange(
                        start_key=b"phone#5c10102#20190501",
                        end_key=b"phone#5c10102#201906201",
                    ),
                ]
                query = ReadRowsQuery(row_ranges=row_ranges)

                for row in table.read_rows_stream(query):
                    print(row)

    # [END bigtable_reads_row_ranges]
    read_row_ranges(table.client.project, table.instance_id, table.table_id)


def read_with_prefix(table):
    # [START bigtable_reads_prefix]
    from google.cloud.bigtable.data import (
        BigtableDataClient,
        ReadRowsQuery,
        RowRange,
    )

    def read_prefix(project_id, instance_id, table_id):
        with BigtableDataClient(project=project_id) as client:
            with client.get_table(instance_id, table_id) as table:
                prefix = "phone#"
                end_key = prefix[:-1] + chr(ord(prefix[-1]) + 1)
                prefix_range = RowRange(start_key=prefix, end_key=end_key)
                query = ReadRowsQuery(row_ranges=[prefix_range])

                for row in table.read_rows_stream(query):
                    print(row)

    # [END bigtable_reads_prefix]
    read_prefix(table.client.project, table.instance_id, table.table_id)


def read_with_filter(table):
    # [START bigtable_reads_filter]
    from google.cloud.bigtable.data import (
        BigtableDataClient,
        ReadRowsQuery,
        row_filters,
    )

    def read_with_filter(project_id, instance_id, table_id):
        with BigtableDataClient(project=project_id) as client:
            with client.get_table(instance_id, table_id) as table:
                row_filter = row_filters.ValueRegexFilter(b"PQ2A.*$")
                query = ReadRowsQuery(row_filter=row_filter)

                for row in table.read_rows_stream(query):
                    print(row)

    # [END bigtable_reads_filter]
    read_with_filter(table.client.project, table.instance_id, table.table_id)


def execute_query(table):
    # [START bigtable_execute_query]
    from google.cloud.bigtable.data import BigtableDataClient

    def execute_query(project_id, instance_id, table_id):
        with BigtableDataClient(project=project_id) as client:
            query = (
                "SELECT _key, stats_summary['os_build'], "
                "stats_summary['connected_cell'], "
                "stats_summary['connected_wifi'] "
                f"from `{table_id}` WHERE _key=@row_key"
            )
            result = client.execute_query(
                query,
                instance_id,
                parameters={"row_key": b"phone#4c410523#20190501"},
            )
            results = list(result)
            print(results)

    # [END bigtable_execute_query]
    execute_query(table.client.project, table.instance_id, table.table_id)


# [START bigtable_reads_print]
def print_row(row):
    from google.cloud._helpers import _datetime_from_microseconds

    print("Reading data for {}:".format(row.row_key.decode("utf-8")))
    last_family = None
    for cell in row.cells:
        if last_family != cell.family:
            print("Column Family {}".format(cell.family))
            last_family = cell.family

        labels = " [{}]".format(",".join(cell.labels)) if len(cell.labels) else ""
        print(
            "\t{}: {} @{}{}".format(
                cell.qualifier.decode("utf-8"),
                cell.value.decode("utf-8"),
                _datetime_from_microseconds(cell.timestamp_micros),
                labels,
            )
        )
    print("")


# [END bigtable_reads_print]
