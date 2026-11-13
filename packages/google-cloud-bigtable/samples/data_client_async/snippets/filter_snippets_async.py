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


# [START bigtable_filters_limit_row_sample_asyncio]
async def filter_limit_row_sample(project_id, instance_id, table_id):
    from google.cloud.bigtable.data import (
        BigtableDataClientAsync,
        ReadRowsQuery,
        row_filters,
    )

    query = ReadRowsQuery(row_filter=row_filters.RowSampleFilter(0.75))

    async with BigtableDataClientAsync(project=project_id) as client:
        async with client.get_table(instance_id, table_id) as table:
            for row in await table.read_rows(query):
                print_row(row)


# [END bigtable_filters_limit_row_sample_asyncio]
# [START bigtable_filters_limit_row_regex_asyncio]
async def filter_limit_row_regex(project_id, instance_id, table_id):
    from google.cloud.bigtable.data import (
        BigtableDataClientAsync,
        ReadRowsQuery,
        row_filters,
    )

    query = ReadRowsQuery(
        row_filter=row_filters.RowKeyRegexFilter(".*#20190501$".encode("utf-8"))
    )

    async with BigtableDataClientAsync(project=project_id) as client:
        async with client.get_table(instance_id, table_id) as table:
            for row in await table.read_rows(query):
                print_row(row)


# [END bigtable_filters_limit_row_regex_asyncio]
# [START bigtable_filters_limit_cells_per_col_asyncio]
async def filter_limit_cells_per_col(project_id, instance_id, table_id):
    from google.cloud.bigtable.data import (
        BigtableDataClientAsync,
        ReadRowsQuery,
        row_filters,
    )

    query = ReadRowsQuery(row_filter=row_filters.CellsColumnLimitFilter(2))

    async with BigtableDataClientAsync(project=project_id) as client:
        async with client.get_table(instance_id, table_id) as table:
            for row in await table.read_rows(query):
                print_row(row)


# [END bigtable_filters_limit_cells_per_col_asyncio]
# [START bigtable_filters_limit_cells_per_row_asyncio]
async def filter_limit_cells_per_row(project_id, instance_id, table_id):
    from google.cloud.bigtable.data import (
        BigtableDataClientAsync,
        ReadRowsQuery,
        row_filters,
    )

    query = ReadRowsQuery(row_filter=row_filters.CellsRowLimitFilter(2))

    async with BigtableDataClientAsync(project=project_id) as client:
        async with client.get_table(instance_id, table_id) as table:
            for row in await table.read_rows(query):
                print_row(row)


# [END bigtable_filters_limit_cells_per_row_asyncio]
# [START bigtable_filters_limit_cells_per_row_offset_asyncio]
async def filter_limit_cells_per_row_offset(project_id, instance_id, table_id):
    from google.cloud.bigtable.data import (
        BigtableDataClientAsync,
        ReadRowsQuery,
        row_filters,
    )

    query = ReadRowsQuery(row_filter=row_filters.CellsRowOffsetFilter(2))

    async with BigtableDataClientAsync(project=project_id) as client:
        async with client.get_table(instance_id, table_id) as table:
            for row in await table.read_rows(query):
                print_row(row)


# [END bigtable_filters_limit_cells_per_row_offset_asyncio]
# [START bigtable_filters_limit_col_family_regex_asyncio]
async def filter_limit_col_family_regex(project_id, instance_id, table_id):
    from google.cloud.bigtable.data import (
        BigtableDataClientAsync,
        ReadRowsQuery,
        row_filters,
    )

    query = ReadRowsQuery(
        row_filter=row_filters.FamilyNameRegexFilter("stats_.*$".encode("utf-8"))
    )

    async with BigtableDataClientAsync(project=project_id) as client:
        async with client.get_table(instance_id, table_id) as table:
            for row in await table.read_rows(query):
                print_row(row)


# [END bigtable_filters_limit_col_family_regex_asyncio]
# [START bigtable_filters_limit_col_qualifier_regex_asyncio]
async def filter_limit_col_qualifier_regex(project_id, instance_id, table_id):
    from google.cloud.bigtable.data import (
        BigtableDataClientAsync,
        ReadRowsQuery,
        row_filters,
    )

    query = ReadRowsQuery(
        row_filter=row_filters.ColumnQualifierRegexFilter(
            "connected_.*$".encode("utf-8")
        )
    )

    async with BigtableDataClientAsync(project=project_id) as client:
        async with client.get_table(instance_id, table_id) as table:
            for row in await table.read_rows(query):
                print_row(row)


# [END bigtable_filters_limit_col_qualifier_regex_asyncio]
# [START bigtable_filters_limit_col_range_asyncio]
async def filter_limit_col_range(project_id, instance_id, table_id):
    from google.cloud.bigtable.data import (
        BigtableDataClientAsync,
        ReadRowsQuery,
        row_filters,
    )

    query = ReadRowsQuery(
        row_filter=row_filters.ColumnRangeFilter(
            "cell_plan", b"data_plan_01gb", b"data_plan_10gb", inclusive_end=False
        )
    )

    async with BigtableDataClientAsync(project=project_id) as client:
        async with client.get_table(instance_id, table_id) as table:
            for row in await table.read_rows(query):
                print_row(row)


# [END bigtable_filters_limit_col_range_asyncio]
# [START bigtable_filters_limit_value_range_asyncio]
async def filter_limit_value_range(project_id, instance_id, table_id):
    from google.cloud.bigtable.data import (
        BigtableDataClientAsync,
        ReadRowsQuery,
        row_filters,
    )

    query = ReadRowsQuery(
        row_filter=row_filters.ValueRangeFilter(b"PQ2A.190405", b"PQ2A.190406")
    )

    async with BigtableDataClientAsync(project=project_id) as client:
        async with client.get_table(instance_id, table_id) as table:
            for row in await table.read_rows(query):
                print_row(row)


# [END bigtable_filters_limit_value_range_asyncio]
# [START bigtable_filters_limit_value_regex_asyncio]


async def filter_limit_value_regex(project_id, instance_id, table_id):
    from google.cloud.bigtable.data import (
        BigtableDataClientAsync,
        ReadRowsQuery,
        row_filters,
    )

    query = ReadRowsQuery(
        row_filter=row_filters.ValueRegexFilter("PQ2A.*$".encode("utf-8"))
    )

    async with BigtableDataClientAsync(project=project_id) as client:
        async with client.get_table(instance_id, table_id) as table:
            for row in await table.read_rows(query):
                print_row(row)


# [END bigtable_filters_limit_value_regex_asyncio]
# [START bigtable_filters_limit_timestamp_range_asyncio]
async def filter_limit_timestamp_range(project_id, instance_id, table_id):
    import datetime

    from google.cloud.bigtable.data import (
        BigtableDataClientAsync,
        ReadRowsQuery,
        row_filters,
    )

    end = datetime.datetime(2019, 5, 1)

    query = ReadRowsQuery(row_filter=row_filters.TimestampRangeFilter(end=end))

    async with BigtableDataClientAsync(project=project_id) as client:
        async with client.get_table(instance_id, table_id) as table:
            for row in await table.read_rows(query):
                print_row(row)


# [END bigtable_filters_limit_timestamp_range_asyncio]
# [START bigtable_filters_limit_block_all_asyncio]
async def filter_limit_block_all(project_id, instance_id, table_id):
    from google.cloud.bigtable.data import (
        BigtableDataClientAsync,
        ReadRowsQuery,
        row_filters,
    )

    query = ReadRowsQuery(row_filter=row_filters.BlockAllFilter(True))

    async with BigtableDataClientAsync(project=project_id) as client:
        async with client.get_table(instance_id, table_id) as table:
            for row in await table.read_rows(query):
                print_row(row)


# [END bigtable_filters_limit_block_all_asyncio]
# [START bigtable_filters_limit_pass_all_asyncio]
async def filter_limit_pass_all(project_id, instance_id, table_id):
    from google.cloud.bigtable.data import (
        BigtableDataClientAsync,
        ReadRowsQuery,
        row_filters,
    )

    query = ReadRowsQuery(row_filter=row_filters.PassAllFilter(True))

    async with BigtableDataClientAsync(project=project_id) as client:
        async with client.get_table(instance_id, table_id) as table:
            for row in await table.read_rows(query):
                print_row(row)


# [END bigtable_filters_limit_pass_all_asyncio]
# [START bigtable_filters_modify_strip_value_asyncio]
async def filter_modify_strip_value(project_id, instance_id, table_id):
    from google.cloud.bigtable.data import (
        BigtableDataClientAsync,
        ReadRowsQuery,
        row_filters,
    )

    query = ReadRowsQuery(row_filter=row_filters.StripValueTransformerFilter(True))

    async with BigtableDataClientAsync(project=project_id) as client:
        async with client.get_table(instance_id, table_id) as table:
            for row in await table.read_rows(query):
                print_row(row)


# [END bigtable_filters_modify_strip_value_asyncio]
# [START bigtable_filters_modify_apply_label_asyncio]
async def filter_modify_apply_label(project_id, instance_id, table_id):
    from google.cloud.bigtable.data import (
        BigtableDataClientAsync,
        ReadRowsQuery,
        row_filters,
    )

    query = ReadRowsQuery(row_filter=row_filters.ApplyLabelFilter(label="labelled"))

    async with BigtableDataClientAsync(project=project_id) as client:
        async with client.get_table(instance_id, table_id) as table:
            for row in await table.read_rows(query):
                print_row(row)


# [END bigtable_filters_modify_apply_label_asyncio]
# [START bigtable_filters_composing_chain_asyncio]
async def filter_composing_chain(project_id, instance_id, table_id):
    from google.cloud.bigtable.data import (
        BigtableDataClientAsync,
        ReadRowsQuery,
        row_filters,
    )

    query = ReadRowsQuery(
        row_filter=row_filters.RowFilterChain(
            filters=[
                row_filters.CellsColumnLimitFilter(1),
                row_filters.FamilyNameRegexFilter("cell_plan"),
            ]
        )
    )

    async with BigtableDataClientAsync(project=project_id) as client:
        async with client.get_table(instance_id, table_id) as table:
            for row in await table.read_rows(query):
                print_row(row)


# [END bigtable_filters_composing_chain_asyncio]
# [START bigtable_filters_composing_interleave_asyncio]
async def filter_composing_interleave(project_id, instance_id, table_id):
    from google.cloud.bigtable.data import (
        BigtableDataClientAsync,
        ReadRowsQuery,
        row_filters,
    )

    query = ReadRowsQuery(
        row_filter=row_filters.RowFilterUnion(
            filters=[
                row_filters.ValueRegexFilter("true"),
                row_filters.ColumnQualifierRegexFilter("os_build"),
            ]
        )
    )

    async with BigtableDataClientAsync(project=project_id) as client:
        async with client.get_table(instance_id, table_id) as table:
            for row in await table.read_rows(query):
                print_row(row)


# [END bigtable_filters_composing_interleave_asyncio]
# [START bigtable_filters_composing_condition_asyncio]
async def filter_composing_condition(project_id, instance_id, table_id):
    from google.cloud.bigtable.data import (
        BigtableDataClientAsync,
        ReadRowsQuery,
        row_filters,
    )

    query = ReadRowsQuery(
        row_filter=row_filters.ConditionalRowFilter(
            predicate_filter=row_filters.RowFilterChain(
                filters=[
                    row_filters.ColumnQualifierRegexFilter("data_plan_10gb"),
                    row_filters.ValueRegexFilter("true"),
                ]
            ),
            true_filter=row_filters.ApplyLabelFilter(label="passed-filter"),
            false_filter=row_filters.ApplyLabelFilter(label="filtered-out"),
        )
    )

    async with BigtableDataClientAsync(project=project_id) as client:
        async with client.get_table(instance_id, table_id) as table:
            for row in await table.read_rows(query):
                print_row(row)


# [END bigtable_filters_composing_condition_asyncio]


# [START bigtable_filters_print_asyncio]
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


# [END bigtable_filters_print_asyncio]
