# Copyright 2021 Google LLC
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

import datetime
import decimal

from dateutil import relativedelta

from google.cloud import bigquery
from google.cloud.bigquery import enums


def test_list_rows_empty_table(bigquery_client: bigquery.Client, table_id: str):
    from google.cloud.bigquery.table import RowIterator

    table = bigquery_client.create_table(table_id)

    # It's a bit silly to list rows for an empty table, but this does
    # happen as the result of a DDL query from an IPython magic command.
    rows = bigquery_client.list_rows(table)
    assert isinstance(rows, RowIterator)
    assert tuple(rows) == ()


def test_list_rows_page_size(bigquery_client: bigquery.Client, table_id: str):
    num_items = 7
    page_size = 3
    num_pages, num_last_page = divmod(num_items, page_size)

    to_insert = [{"string_col": "item%d" % i, "rowindex": i} for i in range(num_items)]
    bigquery_client.load_table_from_json(to_insert, table_id).result()

    df = bigquery_client.list_rows(
        table_id,
        selected_fields=[bigquery.SchemaField("string_col", enums.SqlTypeNames.STRING)],
        page_size=page_size,
    )
    pages = df.pages

    for i in range(num_pages):
        page = next(pages)
        assert page.num_items == page_size
    page = next(pages)
    assert page.num_items == num_last_page


def test_list_rows_scalars(bigquery_client: bigquery.Client, scalars_table: str):
    rows = sorted(
        bigquery_client.list_rows(scalars_table), key=lambda row: row["rowindex"]
    )
    row = rows[0]
    assert row["bool_col"]  # True
    assert row["bytes_col"] == b"Hello, World!"
    assert row["date_col"] == datetime.date(2021, 7, 21)
    assert row["datetime_col"] == datetime.datetime(2021, 7, 21, 11, 39, 45)
    assert row["geography_col"] == "POINT(-122.0838511 37.3860517)"
    assert row["int64_col"] == 123456789
    assert row["interval_col"] == relativedelta.relativedelta(
        years=7, months=11, days=9, hours=4, minutes=15, seconds=37, microseconds=123456
    )
    assert row["numeric_col"] == decimal.Decimal("1.23456789")
    assert row["bignumeric_col"] == decimal.Decimal("10.111213141516171819")
    assert row["float64_col"] == 1.25
    assert row["string_col"] == "Hello, World!"
    assert row["time_col"] == datetime.time(11, 41, 43, 76160)
    assert row["timestamp_col"] == datetime.datetime(
        2021, 7, 21, 17, 43, 43, 945289, tzinfo=datetime.timezone.utc
    )

    nullrow = rows[1]
    for column, value in nullrow.items():
        if column == "rowindex":
            assert value == 1
        else:
            assert value is None


def test_list_rows_scalars_extreme(
    bigquery_client: bigquery.Client, scalars_extreme_table: str
):
    rows = sorted(
        bigquery_client.list_rows(scalars_extreme_table),
        key=lambda row: row["rowindex"],
    )
    row = rows[0]
    assert row["bool_col"]  # True
    assert row["bytes_col"] == b"\r\n"
    assert row["date_col"] == datetime.date(9999, 12, 31)
    assert row["datetime_col"] == datetime.datetime(9999, 12, 31, 23, 59, 59, 999999)
    assert row["geography_col"] == "POINT(-135 90)"
    assert row["int64_col"] == 9223372036854775807
    assert row["interval_col"] == relativedelta.relativedelta(
        years=-10000, days=-3660000, hours=-87840000
    )
    assert row["numeric_col"] == decimal.Decimal(f"9.{'9' * 37}E+28")
    assert row["bignumeric_col"] == decimal.Decimal(f"9.{'9' * 75}E+37")
    assert row["float64_col"] == float("Inf")
    assert row["string_col"] == "Hello, World"
    assert row["time_col"] == datetime.time(23, 59, 59, 999999)
    assert row["timestamp_col"] == datetime.datetime(
        9999, 12, 31, 23, 59, 59, 999999, tzinfo=datetime.timezone.utc
    )

    nullrow = rows[4]
    for column, value in nullrow.items():
        if column == "rowindex":
            assert value == 4
        else:
            assert value is None


def test_list_rows_range(bigquery_client: bigquery.Client, scalars_table_csv: str):
    rows = bigquery_client.list_rows(scalars_table_csv)
    rows = list(rows)
    row = rows[0]
    expected_range = {
        "start": datetime.date(2020, 1, 1),
        "end": datetime.date(2020, 2, 1),
    }
    assert row["range_date"] == expected_range

    row_null = rows[1]
    assert row_null["range_date"] is None


def test_list_rows_pico(bigquery_client: bigquery.Client, scalars_table_pico: str):
    rows = bigquery_client.list_rows(
        scalars_table_pico, timestamp_precision=enums.TimestampPrecision.PICOSECOND
    )
    rows = list(rows)
    row = rows[0]
    assert row["pico_col"] == "2025-01-01T00:00:00.123456789012Z"


def test_list_rows_pico_truncate(
    bigquery_client: bigquery.Client, scalars_table_pico: str
):
    # For a picosecond timestamp column, if the user does not explicitly set
    # timestamp_precision, will return truncated microsecond precision.
    rows = bigquery_client.list_rows(scalars_table_pico)
    rows = list(rows)
    row = rows[0]
    assert row["pico_col"] == "1735689600123456"
