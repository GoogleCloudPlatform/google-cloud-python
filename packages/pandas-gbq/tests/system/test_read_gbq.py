# Copyright (c) 2021 pandas-gbq Authors All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

import collections
import datetime
import decimal
import random

import db_dtypes
import packaging.version
import pandas
import pandas.testing
import pytest
from google.cloud import bigquery

from pandas_gbq.features import FEATURES

QueryTestCase = collections.namedtuple(
    "QueryTestCase",
    ["query", "expected", "use_bqstorage_apis"],
    defaults=[None, None, {True, False}],
)


@pytest.fixture
def writable_table(
    bigquery_client: bigquery.Client, project_id: str, random_dataset: bigquery.Dataset
):
    full_table_id = f"{project_id}.{random_dataset.dataset_id}.writable_table_{random.randrange(1_000_000_000)}"
    table = bigquery.Table(full_table_id)
    table.schema = [
        bigquery.SchemaField("field1", "STRING"),
        bigquery.SchemaField("field2", "INTEGER"),
    ]
    bigquery_client.create_table(table)
    yield full_table_id
    bigquery_client.delete_table(full_table_id)


@pytest.mark.skipif(
    packaging.version.parse(pandas.__version__).release >= (2, 0), reason=""
)
@pytest.mark.parametrize(["use_bqstorage_api"], [(True,), (False,)])
@pytest.mark.parametrize(
    ["query", "expected", "use_bqstorage_apis"],
    [
        pytest.param(
            *QueryTestCase(
                query="""
SELECT
  bools.row_num AS row_num,
  bool_col,
  bytes_col,
  date_col,
  datetime_col,
  float_col,
  int64_col,
  numeric_col,
  string_col,
  time_col,
  timestamp_col
FROM
  UNNEST([
      STRUCT(1 AS row_num, TRUE AS bool_col),
      STRUCT(2 AS row_num, FALSE AS bool_col),
      STRUCT(3 AS row_num, TRUE AS bool_col) ]) AS `bools`
INNER JOIN
  UNNEST([
      STRUCT(1 AS row_num, CAST('C00010FF' AS BYTES FORMAT 'HEX') AS bytes_col),
      STRUCT(2 AS row_num, CAST('F1AC' AS BYTES FORMAT 'HEX') AS bytes_col),
      STRUCT(3 AS row_num, CAST('FFBADD11' AS BYTES FORMAT 'HEX') AS bytes_co) ]) AS `bytes`
INNER JOIN
  UNNEST([
      STRUCT(1 AS row_num, DATE(1998, 9, 4) AS date_col),
      STRUCT(2 AS row_num, DATE(2011, 10, 1) AS date_col),
      STRUCT(3 AS row_num, DATE(2018, 4, 11) AS date_col) ]) AS `dates`
INNER JOIN
  UNNEST([
      STRUCT(1 AS row_num, DATETIME('1998-09-04 12:34:56.789101') AS datetime_col),
      STRUCT(2 AS row_num, DATETIME('2011-10-01 00:01:02.345678') AS datetime_col),
      STRUCT(3 AS row_num, DATETIME('2018-04-11 23:59:59.999999') AS datetime_col) ]) AS `datetimes`
INNER JOIN
  UNNEST([
      STRUCT(1 AS row_num, 1.125 AS float_col),
      STRUCT(2 AS row_num, -2.375 AS float_col),
      STRUCT(3 AS row_num, 0.0 AS float_col) ]) AS `floats`
INNER JOIN
  UNNEST([
      -- 2 ^ 63 - 1, but in hex to avoid intermediate overlfow.
      STRUCT(1 AS row_num, 0x7fffffffffffffff AS int64_col),
      STRUCT(2 AS row_num, -1 AS in64_col),
      -- -2 ^ 63, but in hex to avoid intermediate overlfow.
      STRUCT(3 AS row_num, -0x8000000000000000 AS int64_col) ]) AS `ints`
INNER JOIN
  UNNEST([
      STRUCT(1 AS row_num, CAST('123.456789' AS NUMERIC) AS numeric_col),
      STRUCT(2 AS row_num, CAST('-123.456789' AS NUMERIC) AS numeric_col),
      STRUCT(3 AS row_num, CAST('999.999999' AS NUMERIC) AS numeric_col) ]) AS `numerics`
INNER JOIN
  UNNEST([
      STRUCT(1 AS row_num, 'abcdefghijklmnopqrstuvwxyz' AS string_col),
      STRUCT(2 AS row_num, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' AS string_col),
      STRUCT(3 AS row_num, 'こんにちは' AS string_col) ]) AS `strings`
INNER JOIN
  UNNEST([
      STRUCT(1 AS row_num, CAST('00:00:00.000000' AS TIME) AS time_col),
      STRUCT(2 AS row_num, CAST('09:08:07.654321' AS TIME) AS time_col),
      STRUCT(3 AS row_num, CAST('23:59:59.999999' AS TIME) AS time_col) ]) AS `times`
INNER JOIN
  UNNEST([
      STRUCT(1 AS row_num, TIMESTAMP('1998-09-04 12:34:56.789101') AS timestamp_col),
      STRUCT(2 AS row_num, TIMESTAMP('2011-10-01 00:01:02.345678') AS timestamp_col),
      STRUCT(3 AS row_num, TIMESTAMP('2018-04-11 23:59:59.999999') AS timestamp_col) ]) AS `timestamps`
WHERE
  `bools`.row_num = `dates`.row_num
  AND `bools`.row_num = `bytes`.row_num
  AND `bools`.row_num = `datetimes`.row_num
  AND `bools`.row_num = `floats`.row_num
  AND `bools`.row_num = `ints`.row_num
  AND `bools`.row_num = `numerics`.row_num
  AND `bools`.row_num = `strings`.row_num
  AND `bools`.row_num = `times`.row_num
  AND `bools`.row_num = `timestamps`.row_num
ORDER BY row_num ASC
                """,
                expected=pandas.DataFrame(
                    {
                        "row_num": pandas.Series([1, 2, 3], dtype="Int64"),
                        "bool_col": pandas.Series(
                            [True, False, True],
                            dtype="boolean"
                            if FEATURES.pandas_has_boolean_dtype
                            else "bool",
                        ),
                        "bytes_col": [
                            bytes.fromhex("C00010FF"),
                            bytes.fromhex("F1AC"),
                            bytes.fromhex("FFBADD11"),
                        ],
                        "date_col": pandas.Series(
                            [
                                datetime.date(1998, 9, 4),
                                datetime.date(2011, 10, 1),
                                datetime.date(2018, 4, 11),
                            ],
                            dtype=db_dtypes.DateDtype(),
                        ),
                        "datetime_col": pandas.Series(
                            [
                                "1998-09-04 12:34:56.789101",
                                "2011-10-01 00:01:02.345678",
                                "2018-04-11 23:59:59.999999",
                            ],
                            dtype="datetime64[ns]",
                        ),
                        "float_col": [1.125, -2.375, 0.0],
                        "int64_col": pandas.Series(
                            [(2**63) - 1, -1, -(2**63)], dtype="Int64"
                        ),
                        "numeric_col": [
                            decimal.Decimal("123.456789"),
                            decimal.Decimal("-123.456789"),
                            decimal.Decimal("999.999999"),
                        ],
                        "string_col": [
                            "abcdefghijklmnopqrstuvwxyz",
                            "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
                            "こんにちは",
                        ],
                        "time_col": pandas.Series(
                            ["00:00:00.000000", "09:08:07.654321", "23:59:59.999999"],
                            dtype=db_dtypes.TimeDtype(),
                        ),
                        "timestamp_col": pandas.Series(
                            [
                                "1998-09-04 12:34:56.789101",
                                "2011-10-01 00:01:02.345678",
                                "2018-04-11 23:59:59.999999",
                            ],
                            dtype="datetime64[ns]",
                        ).dt.tz_localize(datetime.timezone.utc),
                    }
                ),
            ),
            id="scalar-types-nonnull-normal-range",
        ),
        pytest.param(
            *QueryTestCase(
                query="""
SELECT
  bools.row_num AS row_num,
  bool_col,
  bytes_col,
  date_col,
  datetime_col,
  float_col,
  int64_col,
  numeric_col,
  string_col,
  time_col,
  timestamp_col
FROM
  UNNEST([
      STRUCT(1 AS row_num, TRUE AS bool_col),
      STRUCT(2 AS row_num, FALSE AS bool_col),
      STRUCT(3 AS row_num, NULL AS bool_col) ]) AS `bools`
INNER JOIN
  UNNEST([
      STRUCT(1 AS row_num, NULL AS bytes_col),
      STRUCT(2 AS row_num, CAST('F1AC' AS BYTES FORMAT 'HEX') AS bytes_col),
      STRUCT(3 AS row_num, CAST('' AS BYTES FORMAT 'HEX') AS bytes_co) ]) AS `bytes`
INNER JOIN
  UNNEST([
      STRUCT(1 AS row_num, DATE(1970, 1, 1) AS date_col),
      STRUCT(2 AS row_num, NULL AS date_col),
      STRUCT(3 AS row_num, DATE(2018, 4, 11) AS date_col) ]) AS `dates`
INNER JOIN
  UNNEST([
      STRUCT(1 AS row_num, DATETIME('1970-01-01 00:00:00.000000') AS datetime_col),
      STRUCT(2 AS row_num, DATETIME('2011-10-01 00:01:02.345678') AS datetime_col),
      STRUCT(3 AS row_num, NULL AS datetime_col) ]) AS `datetimes`
INNER JOIN
  UNNEST([
      STRUCT(1 AS row_num, NULL AS float_col),
      STRUCT(2 AS row_num, -2.375 AS float_col),
      STRUCT(3 AS row_num, 0.0 AS float_col) ]) AS `floats`
INNER JOIN
  UNNEST([
      STRUCT(1 AS row_num, -1 AS int64_col),
      STRUCT(2 AS row_num, NULL AS int64_col),
      STRUCT(3 AS row_num, 0 AS int64_col) ]) AS `int64s`
INNER JOIN
  UNNEST([
      STRUCT(1 AS row_num, CAST('123.456789' AS NUMERIC) AS numeric_col),
      STRUCT(2 AS row_num, NULL AS numeric_col),
      STRUCT(3 AS row_num, CAST('999.999999' AS NUMERIC) AS numeric_col) ]) AS `numerics`
INNER JOIN
  UNNEST([
      STRUCT(1 AS row_num, '' AS string_col),
      STRUCT(2 AS row_num, 'こんにちは' AS string_col),
      STRUCT(3 AS row_num, NULL AS string_col) ]) AS `strings`
INNER JOIN
  UNNEST([
      STRUCT(1 AS row_num, NULL AS time_col),
      STRUCT(2 AS row_num, CAST('00:00:00.000000' AS TIME) AS time_col),
      STRUCT(3 AS row_num, CAST('23:59:59.999999' AS TIME) AS time_col) ]) AS `times`
INNER JOIN
  UNNEST([
      STRUCT(1 AS row_num, TIMESTAMP('1970-01-01 00:00:00.000000') AS timestamp_col),
      STRUCT(2 AS row_num, NULL AS timestamp_col),
      STRUCT(3 AS row_num, TIMESTAMP('2018-04-11 23:59:59.999999') AS timestamp_col) ]) AS `timestamps`
WHERE
  `bools`.row_num = `dates`.row_num
  AND `bools`.row_num = `bytes`.row_num
  AND `bools`.row_num = `datetimes`.row_num
  AND `bools`.row_num = `floats`.row_num
  AND `bools`.row_num = `int64s`.row_num
  AND `bools`.row_num = `numerics`.row_num
  AND `bools`.row_num = `strings`.row_num
  AND `bools`.row_num = `times`.row_num
  AND `bools`.row_num = `timestamps`.row_num
ORDER BY row_num ASC
            """,
                expected=pandas.DataFrame(
                    {
                        "row_num": pandas.Series([1, 2, 3], dtype="Int64"),
                        "bool_col": pandas.Series(
                            [True, False, None],
                            dtype="boolean"
                            if FEATURES.pandas_has_boolean_dtype
                            else "object",
                        ),
                        "bytes_col": [None, bytes.fromhex("F1AC"), b""],
                        "date_col": pandas.Series(
                            [
                                datetime.date(1970, 1, 1),
                                None,
                                datetime.date(2018, 4, 11),
                            ],
                            dtype=db_dtypes.DateDtype(),
                        ),
                        "datetime_col": pandas.Series(
                            [
                                "1970-01-01 00:00:00.000000",
                                "2011-10-01 00:01:02.345678",
                                None,
                            ],
                            dtype="datetime64[ns]",
                        ),
                        "float_col": [None, -2.375, 0.0],
                        "int64_col": pandas.Series([-1, None, 0], dtype="Int64"),
                        "numeric_col": [
                            decimal.Decimal("123.456789"),
                            None,
                            decimal.Decimal("999.999999"),
                        ],
                        "string_col": ["", "こんにちは", None],
                        "time_col": pandas.Series(
                            [None, "00:00:00", "23:59:59.999999"],
                            dtype=db_dtypes.TimeDtype(),
                        ),
                        "timestamp_col": pandas.Series(
                            [
                                "1970-01-01 00:00:00.000000",
                                None,
                                "2018-04-11 23:59:59.999999",
                            ],
                            dtype="datetime64[ns]",
                        ).dt.tz_localize(datetime.timezone.utc),
                    }
                ),
            ),
            id="scalar-types-nullable-normal-range",
        ),
        pytest.param(
            *QueryTestCase(
                query="""
SELECT
  bools.row_num AS row_num,
  bool_col,
  bytes_col,
  date_col,
  datetime_col,
  float_col,
  int64_col,
  numeric_col,
  string_col,
  time_col,
  timestamp_col
FROM
  UNNEST([
      STRUCT(1 AS row_num, CAST(NULL AS BOOL) AS bool_col) ]) AS `bools`
INNER JOIN
  UNNEST([
      STRUCT(1 AS row_num, CAST(NULL AS BYTES) AS bytes_col) ]) AS `bytes`
INNER JOIN
  UNNEST([
      STRUCT(1 AS row_num, CAST(NULL AS DATE) AS date_col) ]) AS `dates`
INNER JOIN
  UNNEST([
      STRUCT(1 AS row_num, CAST(NULL AS DATETIME) AS datetime_col) ]) AS `datetimes`
INNER JOIN
  UNNEST([
      STRUCT(1 AS row_num, CAST(NULL AS FLOAT64) AS float_col) ]) AS `floats`
INNER JOIN
  UNNEST([
      STRUCT(1 AS row_num, CAST(NULL AS INT64) AS int64_col) ]) AS `int64s`
INNER JOIN
  UNNEST([
      STRUCT(1 AS row_num, CAST(NULL AS NUMERIC) AS numeric_col) ]) AS `numerics`
INNER JOIN
  UNNEST([
      STRUCT(1 AS row_num, CAST(NULL AS STRING) AS string_col) ]) AS `strings`
INNER JOIN
  UNNEST([
      STRUCT(1 AS row_num, CAST(NULL AS TIME) AS time_col) ]) AS `times`
INNER JOIN
  UNNEST([
      STRUCT(1 AS row_num, CAST(NULL AS TIMESTAMP) AS timestamp_col) ]) AS `timestamps`
WHERE
  `bools`.row_num = `dates`.row_num
  AND `bools`.row_num = `bytes`.row_num
  AND `bools`.row_num = `datetimes`.row_num
  AND `bools`.row_num = `floats`.row_num
  AND `bools`.row_num = `int64s`.row_num
  AND `bools`.row_num = `numerics`.row_num
  AND `bools`.row_num = `strings`.row_num
  AND `bools`.row_num = `times`.row_num
  AND `bools`.row_num = `timestamps`.row_num
ORDER BY row_num ASC
            """,
                expected=pandas.DataFrame(
                    {
                        "row_num": pandas.Series([1], dtype="Int64"),
                        "bool_col": pandas.Series(
                            [None],
                            dtype="boolean"
                            if FEATURES.pandas_has_boolean_dtype
                            else "object",
                        ),
                        "bytes_col": [None],
                        "date_col": pandas.Series(
                            [None],
                            dtype=db_dtypes.DateDtype(),
                        ),
                        "datetime_col": pandas.Series(
                            [None],
                            dtype="datetime64[ns]",
                        ),
                        "float_col": pandas.Series([None], dtype="float64"),
                        "int64_col": pandas.Series([None], dtype="Int64"),
                        "numeric_col": [None],
                        "string_col": [None],
                        "time_col": pandas.Series(
                            [None],
                            dtype=db_dtypes.TimeDtype(),
                        ),
                        "timestamp_col": pandas.Series(
                            [None],
                            dtype="datetime64[ns]",
                        ).dt.tz_localize(datetime.timezone.utc),
                    }
                ),
            ),
            id="scalar-types-null",
        ),
        pytest.param(
            *QueryTestCase(
                query="""
SELECT
  bignumerics.row_num AS row_num,
  bignumeric_col,
  nullable_col,
  null_col
FROM
  UNNEST([
      STRUCT(1 AS row_num, CAST('123456789.123456789' AS BIGNUMERIC) AS bignumeric_col),
      STRUCT(2 AS row_num, CAST('-123456789.123456789' AS BIGNUMERIC) AS bignumeric_col),
      STRUCT(3 AS row_num, CAST('987654321.987654321' AS BIGNUMERIC) AS bignumeric_col) ]) AS `bignumerics`
INNER JOIN
  UNNEST([
      STRUCT(1 AS row_num, CAST('123456789.123456789' AS BIGNUMERIC) AS nullable_col),
      STRUCT(2 AS row_num, NULL AS nullable_col),
      STRUCT(3 AS row_num, CAST('987654321.987654321' AS BIGNUMERIC) AS nullable_col) ]) AS `nullables`
INNER JOIN
  UNNEST([
      STRUCT(1 AS row_num, CAST(NULL AS BIGNUMERIC) AS null_col),
      STRUCT(2 AS row_num, CAST(NULL AS BIGNUMERIC) AS null_col),
      STRUCT(3 AS row_num, CAST(NULL AS BIGNUMERIC) AS null_col) ]) AS `nulls`
WHERE
  `bignumerics`.row_num = `nullables`.row_num
  AND `bignumerics`.row_num = `nulls`.row_num
ORDER BY row_num ASC
            """,
                expected=pandas.DataFrame(
                    {
                        "row_num": pandas.Series([1, 2, 3], dtype="Int64"),
                        # TODO: Support a special (nullable) dtype for decimal data.
                        # https://github.com/googleapis/python-db-dtypes-pandas/issues/49
                        "bignumeric_col": [
                            decimal.Decimal("123456789.123456789"),
                            decimal.Decimal("-123456789.123456789"),
                            decimal.Decimal("987654321.987654321"),
                        ],
                        "nullable_col": [
                            decimal.Decimal("123456789.123456789"),
                            None,
                            decimal.Decimal("987654321.987654321"),
                        ],
                        "null_col": [None, None, None],
                    }
                ),
            ),
            id="bignumeric-normal-range",
        ),
        pytest.param(
            *QueryTestCase(
                query="""
SELECT
  dates.row_num AS row_num,
  date_col,
  datetime_col,
  timestamp_col
FROM
  UNNEST([
      STRUCT(1 AS row_num, DATE(1, 1, 1) AS date_col),
      STRUCT(2 AS row_num, DATE(9999, 12, 31) AS date_col),
      STRUCT(3 AS row_num, DATE(2262, 4, 12) AS date_col) ]) AS `dates`
INNER JOIN
  UNNEST([
      STRUCT(1 AS row_num, DATETIME('0001-01-01 00:00:00.000000') AS datetime_col),
      STRUCT(2 AS row_num, DATETIME('9999-12-31 23:59:59.999999') AS datetime_col),
      STRUCT(3 AS row_num, DATETIME('2262-04-11 23:47:16.854776') AS datetime_col) ]) AS `datetimes`
INNER JOIN
  UNNEST([
      STRUCT(1 AS row_num, TIMESTAMP('0001-01-01 00:00:00.000000') AS timestamp_col),
      STRUCT(2 AS row_num, TIMESTAMP('9999-12-31 23:59:59.999999') AS timestamp_col),
      STRUCT(3 AS row_num, TIMESTAMP('2262-04-11 23:47:16.854776') AS timestamp_col) ]) AS `timestamps`
WHERE
  `dates`.row_num = `datetimes`.row_num
  AND `dates`.row_num = `timestamps`.row_num
ORDER BY row_num ASC
            """,
                expected=pandas.DataFrame(
                    {
                        "row_num": pandas.Series([1, 2, 3], dtype="Int64"),
                        "date_col": pandas.Series(
                            [
                                datetime.date(1, 1, 1),
                                datetime.date(9999, 12, 31),
                                datetime.date(2262, 4, 12),
                            ],
                            dtype="object",
                        ),
                        "datetime_col": pandas.Series(
                            [
                                datetime.datetime(1, 1, 1, 0, 0, 0, 0),
                                datetime.datetime(9999, 12, 31, 23, 59, 59, 999999),
                                # One microsecond more than pandas.Timestamp.max.
                                datetime.datetime(2262, 4, 11, 23, 47, 16, 854776),
                            ],
                            dtype="object",
                        ),
                        "timestamp_col": pandas.Series(
                            [
                                datetime.datetime(
                                    1, 1, 1, 0, 0, 0, 0, tzinfo=datetime.timezone.utc
                                ),
                                datetime.datetime(
                                    9999,
                                    12,
                                    31,
                                    23,
                                    59,
                                    59,
                                    999999,
                                    tzinfo=datetime.timezone.utc,
                                ),
                                # One microsecond more than pandas.Timestamp.max.
                                datetime.datetime(
                                    2262,
                                    4,
                                    11,
                                    23,
                                    47,
                                    16,
                                    854776,
                                    tzinfo=datetime.timezone.utc,
                                ),
                            ],
                            dtype="object",
                        ),
                    }
                ),
                use_bqstorage_apis={True, False},
            ),
            id="issue365-extreme-datetimes",
        ),
    ],
)
def test_default_dtypes(
    read_gbq, query, expected, use_bqstorage_apis, use_bqstorage_api
):
    if use_bqstorage_api not in use_bqstorage_apis:
        pytest.skip(f"use_bqstorage_api={use_bqstorage_api} not supported.")
    # the parameter useQueryCache=False is used in the following function call
    # to avoid a failing test due to cached data that may be out of order.
    result = read_gbq(
        query,
        use_bqstorage_api=use_bqstorage_api,
        configuration={"query": {"useQueryCache": False}},
    )
    pandas.testing.assert_frame_equal(result, expected)


@pytest.mark.parametrize(["use_bqstorage_api"], [(True,), (False,)])
def test_empty_dataframe(read_gbq, use_bqstorage_api):
    # Bug fix for https://github.com/pandas-dev/pandas/issues/10273 and
    # https://github.com/googleapis/python-bigquery-pandas/issues/299
    query = """
SELECT
  bools.row_num AS row_num,
  bool_col,
  bytes_col,
  date_col,
  datetime_col,
  float_col,
  int64_col,
  numeric_col,
  string_col,
  time_col,
  timestamp_col
FROM
  UNNEST([
      STRUCT(1 AS row_num, TRUE AS bool_col) ]) AS `bools`
INNER JOIN
  UNNEST([
      STRUCT(1 AS row_num, CAST('F1AC' AS BYTES FORMAT 'HEX') AS bytes_col) ]) AS `bytes`
INNER JOIN
  UNNEST([
      STRUCT(1 AS row_num, DATE(2018, 4, 11) AS date_col) ]) AS `dates`
INNER JOIN
  UNNEST([
      STRUCT(1 AS row_num, DATETIME('2011-10-01 00:01:02.345678') AS datetime_col) ]) AS `datetimes`
INNER JOIN
  UNNEST([
      STRUCT(1 AS row_num, -2.375 AS float_col) ]) AS `floats`
INNER JOIN
  UNNEST([
      STRUCT(1 AS row_num, 1234 AS int64_col) ]) AS `int64s`
INNER JOIN
  UNNEST([
      STRUCT(1 AS row_num, CAST('123.456789' AS NUMERIC) AS numeric_col) ]) AS `numerics`
INNER JOIN
  UNNEST([
      STRUCT(1 AS row_num, 'abcdefghijklmnopqrstuvwxyz' AS string_col) ]) AS `strings`
INNER JOIN
  UNNEST([
      STRUCT(1 AS row_num, CAST('09:08:07.654321' AS TIME) AS time_col) ]) AS `times`
INNER JOIN
  UNNEST([
      STRUCT(1 AS row_num, TIMESTAMP('1998-09-04 12:34:56.789101') AS timestamp_col) ]) AS `timestamps`
WHERE
  `bools`.row_num = `dates`.row_num
  AND `bools`.row_num = `bytes`.row_num
  AND `bools`.row_num = `datetimes`.row_num
  AND `bools`.row_num = `floats`.row_num
  AND `bools`.row_num = `int64s`.row_num
  AND `bools`.row_num = `numerics`.row_num
  AND `bools`.row_num = `strings`.row_num
  AND `bools`.row_num = `times`.row_num
  AND `bools`.row_num = `timestamps`.row_num
  AND `bools`.row_num = -1
ORDER BY row_num ASC
    """
    expected = pandas.DataFrame(
        {
            "row_num": pandas.Series([], dtype="Int64"),
            "bool_col": pandas.Series(
                [],
                dtype="boolean" if FEATURES.pandas_has_boolean_dtype else "bool",
            ),
            "bytes_col": pandas.Series([], dtype="object"),
            "date_col": pandas.Series(
                [],
                dtype=db_dtypes.DateDtype(),
            ),
            "datetime_col": pandas.Series(
                [],
                dtype="datetime64[ns]",
            ),
            "float_col": pandas.Series([], dtype="float64"),
            "int64_col": pandas.Series([], dtype="Int64"),
            "numeric_col": pandas.Series([], dtype="object"),
            "string_col": pandas.Series([], dtype="object"),
            "time_col": pandas.Series(
                [],
                dtype=db_dtypes.TimeDtype(),
            ),
            "timestamp_col": pandas.Series(
                [],
                dtype="datetime64[ns]",
            ).dt.tz_localize(datetime.timezone.utc),
        }
    )
    result = read_gbq(query, use_bqstorage_api=use_bqstorage_api)
    pandas.testing.assert_frame_equal(
        result, expected, check_index_type=False, check_dtype=False
    )


def test_dml_query(read_gbq, writable_table: str):
    query = f"""
    UPDATE `{writable_table}`
    SET field1 = NULL
    WHERE field1 = 'string';
    UPDATE `{writable_table}`
    SET field2 = NULL
    WHERE field2 < 0;
    """
    result = read_gbq(query)
    assert result is not None


def test_read_gbq_with_bq_client(read_gbq_with_bq_client):
    query = "SELECT * FROM UNNEST([1, 2, 3]) AS numbers"

    actual_result = read_gbq_with_bq_client(query)

    expected_result = pandas.DataFrame(
        {"numbers": pandas.Series([1, 2, 3], dtype="Int64")}
    )
    pandas.testing.assert_frame_equal(actual_result, expected_result)
