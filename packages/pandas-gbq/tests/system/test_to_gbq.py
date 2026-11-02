# Copyright (c) 2017 pandas-gbq Authors All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

import collections
import datetime
import decimal
import random

import db_dtypes
import pandas
import pandas.testing
import pyarrow
import pytest

pytest.importorskip("google.cloud.bigquery", minversion="1.24.0")


@pytest.fixture(params=["load_parquet", "load_csv"])
def api_method(request):
    return request.param


@pytest.fixture
def method_under_test(to_gbq):
    return to_gbq


SeriesRoundTripTestCase = collections.namedtuple(
    "SeriesRoundTripTestCase",
    ["input_series", "api_methods", "expected_dtype"],
    defaults=[None, {"load_csv", "load_parquet"}, None],
)


@pytest.mark.parametrize(
    ["input_series", "api_methods", "expected_dtype"],
    [
        # Ensure that 64-bit floating point numbers are unchanged.
        # See: https://github.com/pydata/pandas-gbq/issues/326
        SeriesRoundTripTestCase(
            input_series=pandas.Series(
                [
                    0.14285714285714285,
                    0.4406779661016949,
                    1.05148,
                    1.05153,
                    1.8571428571428572,
                    2.718281828459045,
                    3.141592653589793,
                    2.0988936657440586e43,
                ],
                name="test_col",
            ),
        ),
        pytest.param(
            *SeriesRoundTripTestCase(
                input_series=pandas.Series(
                    [
                        "abc",
                        "defg",
                        # Ensure that unicode characters are encoded. See:
                        # https://github.com/googleapis/python-bigquery-pandas/issues/106
                        "信用卡",
                        "Skywalker™",
                        "hülle",
                    ],
                    name="test_col",
                ),
            ),
            id="string-unicode",
        ),
        pytest.param(
            *SeriesRoundTripTestCase(
                input_series=pandas.Series(
                    [
                        "abc",
                        "defg",
                        # Ensure that empty strings are written as empty string,
                        # not NULL. See:
                        # https://github.com/googleapis/python-bigquery-pandas/issues/366
                        "",
                        None,
                    ],
                    name="empty_strings",
                ),
                # BigQuery CSV loader uses empty string as the "null marker" by
                # default. Potentially one could choose a rarely used character or
                # string as the null marker to disambiguate null from empty string,
                # but then that string couldn't be loaded.
                # TODO: Revist when custom load job configuration is supported.
                #       https://github.com/googleapis/python-bigquery-pandas/issues/425
                api_methods={"load_parquet"},
            ),
            id="string-empty-and-null",
        ),
    ],
)
def test_series_round_trip(
    method_under_test,
    random_dataset_id,
    read_gbq,
    input_series,
    api_method,
    api_methods,
    expected_dtype,
):
    if api_method not in api_methods:
        pytest.skip(f"{api_method} not supported.")
    table_id = f"{random_dataset_id}.round_trip_{random.randrange(1_000_000)}"
    input_series = input_series.sort_values().reset_index(drop=True)
    df = pandas.DataFrame(
        # Some errors only occur in multi-column dataframes. See:
        # https://github.com/googleapis/python-bigquery-pandas/issues/366
        {"test_col": input_series, "test_col2": input_series}
    )
    method_under_test(df, table_id, api_method=api_method)

    round_trip = read_gbq(table_id)
    round_trip_series = round_trip["test_col"].sort_values().reset_index(drop=True)

    expected_series = input_series.copy()
    if expected_dtype is not None:
        expected_series = expected_series.astype(expected_dtype)

    pandas.testing.assert_series_equal(
        round_trip_series,
        expected_series,
        check_exact=True,
        check_names=False,
    )


DataFrameRoundTripTestCase = collections.namedtuple(
    "DataFrameRoundTripTestCase",
    ["input_df", "expected_df", "table_schema", "api_methods"],
    defaults=[None, None, [], {"load_csv", "load_parquet"}],
)

DATAFRAME_ROUND_TRIPS = [
    # Ensure that a BOOLEAN column can be written with bool, boolean, and
    # object dtypes. See:
    # https://github.com/googleapis/python-bigquery-pandas/issues/105
    pytest.param(
        *DataFrameRoundTripTestCase(
            input_df=pandas.DataFrame(
                {
                    "row_num": [0, 1, 2],
                    "bool_col": pandas.Series(
                        [True, False, True],
                        dtype="bool",
                    ),
                    "boolean_col": pandas.Series(
                        [None, True, False],
                        dtype="boolean",
                    ),
                    "object_col": pandas.Series(
                        [False, pandas.NA, True],
                        dtype="object",
                    ),
                }
            ),
            expected_df=pandas.DataFrame(
                {
                    "row_num": [0, 1, 2],
                    "bool_col": pandas.Series(
                        [True, False, True],
                        dtype="bool",
                    ),
                    "boolean_col": pandas.Series(
                        [None, True, False],
                        dtype="boolean",
                    ),
                    "object_col": pandas.Series(
                        [
                            False,
                            (pandas.NA if hasattr(pandas, "NA") else None),
                            True,
                        ],
                        dtype="object",
                    ),
                }
            ),
            table_schema=[
                {"name": "bool_col", "type": "BOOLEAN"},
                {"name": "boolean_col", "type": "BOOLEAN"},
                {"name": "object_col", "type": "BOOLEAN"},
            ],
            api_methods={"load_csv", "load_parquet"},
        ),
        id="boolean",
    ),
    # Ensure that a DATE column can be written with datetime64[ns] dtype
    # data. See:
    # https://github.com/googleapis/python-bigquery-pandas/issues/362
    DataFrameRoundTripTestCase(
        input_df=pandas.DataFrame(
            {
                "row_num": [0, 1, 2],
                "date_col": pandas.Series(
                    ["2021-04-17", "1999-12-31", "2038-01-19"],
                    dtype="datetime64[ns]",
                ),
            }
        ),
        table_schema=[{"name": "date_col", "type": "DATE"}],
        # Skip CSV because the pandas CSV writer includes time when writing
        # datetime64 values.
        api_methods={"load_parquet"},
    ),
    DataFrameRoundTripTestCase(
        input_df=pandas.DataFrame(
            {
                "row_num": [0, 1, 2],
                "date_col": pandas.Series(
                    ["2021-04-17", "1999-12-31", "2038-01-19"],
                    dtype=db_dtypes.DateDtype(),
                ),
            }
        ),
        table_schema=[{"name": "date_col", "type": "DATE"}],
    ),
    # Loading a DATE column should work for string objects. See:
    # https://github.com/googleapis/python-bigquery-pandas/issues/421
    DataFrameRoundTripTestCase(
        input_df=pandas.DataFrame(
            {"row_num": [123], "date_col": ["2021-12-12"]},
            columns=["row_num", "date_col"],
        ),
        expected_df=pandas.DataFrame(
            {
                "row_num": [123],
                "date_col": pandas.Series(
                    [datetime.date(2021, 12, 12)], dtype=db_dtypes.DateDtype()
                ),
            },
            columns=["row_num", "date_col"],
        ),
        table_schema=[
            {"name": "row_num", "type": "INTEGER"},
            {"name": "date_col", "type": "DATE"},
        ],
    ),
    # Loading an INTEGER column should work for any integer dtype. See:
    # https://github.com/googleapis/python-bigquery-pandas/issues/616
    pytest.param(
        *DataFrameRoundTripTestCase(
            input_df=pandas.DataFrame(
                {
                    "row_num": [0, 1, 2],
                    "object": pandas.Series(
                        [None, 1, -2],
                        dtype="object",
                    ),
                    "nullable_int64": pandas.Series(
                        [3, None, -4],
                        dtype="Int64",
                    ),
                    "int8": pandas.Series(
                        [5, -6, 7],
                        dtype="int8",
                    ),
                    "int16": pandas.Series(
                        [-8, 9, -10],
                        dtype="int16",
                    ),
                    "int32": pandas.Series(
                        [11, -12, 13],
                        dtype="int32",
                    ),
                    "int64": pandas.Series(
                        [-14, 15, -16],
                        dtype="int64",
                    ),
                    "uint8": pandas.Series(
                        [0, 1, 2],
                        dtype="uint8",
                    ),
                    "uint16": pandas.Series(
                        [3, 4, 5],
                        dtype="uint16",
                    ),
                    "uint32": pandas.Series(
                        [6, 7, 8],
                        dtype="uint32",
                    ),
                }
            ),
            expected_df=pandas.DataFrame(
                {
                    "row_num": [0, 1, 2],
                    "object": pandas.Series(
                        [None, 1, -2],
                        dtype="Int64",
                    ),
                    "nullable_int64": pandas.Series(
                        [3, None, -4],
                        dtype="Int64",
                    ),
                    "int8": pandas.Series(
                        [5, -6, 7],
                        dtype="Int64",
                    ),
                    "int16": pandas.Series(
                        [-8, 9, -10],
                        dtype="Int64",
                    ),
                    "int32": pandas.Series(
                        [11, -12, 13],
                        dtype="Int64",
                    ),
                    "int64": pandas.Series(
                        [-14, 15, -16],
                        dtype="Int64",
                    ),
                    "uint8": pandas.Series(
                        [0, 1, 2],
                        dtype="Int64",
                    ),
                    "uint16": pandas.Series(
                        [3, 4, 5],
                        dtype="Int64",
                    ),
                    "uint32": pandas.Series(
                        [6, 7, 8],
                        dtype="Int64",
                    ),
                }
            ),
            api_methods={"load_csv", "load_parquet"},
        ),
        id="integer",
    ),
    # Loading a NUMERIC column should work for floating point objects. See:
    # https://github.com/googleapis/python-bigquery-pandas/issues/421
    DataFrameRoundTripTestCase(
        input_df=pandas.DataFrame(
            {"row_num": [123], "num_col": [1.25]},
            columns=["row_num", "num_col"],
        ),
        expected_df=pandas.DataFrame(
            {"row_num": [123], "num_col": [decimal.Decimal("1.25")]},
            columns=["row_num", "num_col"],
        ),
        table_schema=[
            {"name": "row_num", "type": "INTEGER"},
            {"name": "num_col", "type": "NUMERIC"},
        ],
    ),
    pytest.param(
        *DataFrameRoundTripTestCase(
            input_df=pandas.DataFrame(
                {
                    "row_num": [1, 2, 3],
                    # DATE valuess outside the pandas range for timestamp
                    # aren't supported by the db-dtypes package.
                    # https://github.com/googleapis/python-bigquery-pandas/issues/441
                    "date_col": [
                        datetime.date(1, 1, 1),
                        datetime.date(1970, 1, 1),
                        datetime.date(9999, 12, 31),
                    ],
                    # DATETIME values outside of the range for pandas timestamp
                    # require `date_as_object` parameter in
                    # google-cloud-bigquery versions 1.x and 2.x, but not 3.x.
                    # https://github.com/googleapis/python-bigquery-pandas/issues/365
                    "datetime_col": [
                        # CSV loader in BigQuery currently requires leading 0s
                        # for TIMESTAMP but not DATETIME. See internal issue
                        # b/467399807.
                        datetime.datetime(1000, 1, 1),
                        datetime.datetime(1970, 1, 1),
                        datetime.datetime(9999, 12, 31, 23, 59, 59, 999999),
                    ],
                    "timestamp_col": [
                        datetime.datetime(1, 1, 1, tzinfo=datetime.timezone.utc),
                        datetime.datetime(1970, 1, 1, tzinfo=datetime.timezone.utc),
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
                    ],
                },
                columns=["row_num", "date_col", "datetime_col", "timestamp_col"],
            ),
            table_schema=[
                {"name": "row_num", "type": "INTEGER"},
                {"name": "date_col", "type": "DATE"},
                {"name": "datetime_col", "type": "DATETIME"},
                {"name": "timestamp_col", "type": "TIMESTAMP"},
            ],
        ),
        id="issue365-extreme-datetimes",
    ),
    # Loading a STRING column should work with all available string dtypes.
    pytest.param(
        *DataFrameRoundTripTestCase(
            input_df=pandas.DataFrame(
                {
                    "row_num": [1, 2, 3],
                    # If a cast to STRING is lossless, pandas-gbq should do that automatically.
                    # See: https://github.com/googleapis/python-bigquery-pandas/issues/875
                    "int_want_string": [94043, 10011, 98033],
                    "object": pandas.Series(["a", "b", "c"], dtype="object"),
                    "string_python": pandas.Series(
                        ["d", "e", "f"],
                        dtype=(
                            pandas.StringDtype(storage="python")
                            if hasattr(pandas, "ArrowDtype")
                            else pandas.StringDtype()
                        ),
                    ),
                    "string_pyarrow": pandas.Series(
                        ["g", "h", "i"],
                        dtype=(
                            pandas.StringDtype(storage="pyarrow")
                            if hasattr(pandas, "ArrowDtype")
                            else pandas.StringDtype()
                        ),
                    ),
                    "arrowdtype_string": pandas.Series(
                        ["j", "k", "l"],
                        dtype=(
                            pandas.ArrowDtype(pyarrow.string())
                            if hasattr(pandas, "ArrowDtype")
                            else pandas.StringDtype()
                        ),
                    ),
                    "arrowdtype_large_string": pandas.Series(
                        ["m", "n", "o"],
                        dtype=(
                            pandas.ArrowDtype(pyarrow.large_string())
                            if hasattr(pandas, "ArrowDtype")
                            and hasattr(pyarrow, "large_string")
                            else pandas.StringDtype()
                        ),
                    ),
                },
            ),
            expected_df=pandas.DataFrame(
                {
                    "row_num": [1, 2, 3],
                    "int_want_string": pandas.Series(
                        ["94043", "10011", "98033"], dtype="object"
                    ),
                    "object": pandas.Series(["a", "b", "c"], dtype="object"),
                    "string_python": pandas.Series(["d", "e", "f"], dtype="object"),
                    "string_pyarrow": pandas.Series(["g", "h", "i"], dtype="object"),
                    "arrowdtype_string": pandas.Series(["j", "k", "l"], dtype="object"),
                    "arrowdtype_large_string": pandas.Series(
                        ["m", "n", "o"], dtype="object"
                    ),
                },
            ),
            table_schema=[
                {"name": "row_num", "type": "INTEGER"},
                {"name": "int_want_string", "type": "STRING"},
                {"name": "object", "type": "STRING"},
                {"name": "string_python", "type": "STRING"},
                {"name": "string_pyarrow", "type": "STRING"},
                {"name": "string_pyarrow_from_int", "type": "STRING"},
                {"name": "arrowdtype_string", "type": "STRING"},
                {"name": "arrowdtype_large_string", "type": "STRING"},
            ],
        ),
        id="issue875-strings",
    ),
    pytest.param(
        # Load STRUCT and ARRAY using either object column or ArrowDtype.
        # See: https://github.com/googleapis/python-bigquery-pandas/issues/452
        *DataFrameRoundTripTestCase(
            input_df=pandas.DataFrame(
                {
                    "row_num": [0, 1, 2],
                    "object_struct": pandas.Series(
                        [{"test": "str1"}, {"test": "str2"}, {"test": "str3"}],
                        dtype="object",
                    ),
                    # Array of DATETIME requires inspection into list elements.
                    # See:
                    # https://github.com/googleapis/python-bigquery/pull/1061
                    "object_array_datetime": pandas.Series(
                        [[], [datetime.datetime(1998, 9, 4, 12, 0, 0)], []],
                        dtype="object",
                    ),
                    "object_array_of_struct": pandas.Series(
                        [[], [{"test": "str4"}], []], dtype="object"
                    ),
                    "arrow_struct": pandas.Series(
                        [
                            {"version": 1, "project": "pandas"},
                            {"version": 2, "project": "pandas"},
                            {"version": 1, "project": "numpy"},
                        ],
                        dtype=pandas.ArrowDtype(
                            pyarrow.struct(
                                [
                                    ("version", pyarrow.int64()),
                                    ("project", pyarrow.string()),
                                ]
                            )
                        )
                        if hasattr(pandas, "ArrowDtype")
                        else "object",
                    ),
                    "arrow_array": pandas.Series(
                        [[1, 2, 3], None, [4, 5, 6]],
                        dtype=pandas.ArrowDtype(
                            pyarrow.list_(pyarrow.int64()),
                        )
                        if hasattr(pandas, "ArrowDtype")
                        else "object",
                    ),
                    "arrow_array_of_struct": pandas.Series(
                        [
                            [{"test": "str5"}],
                            None,
                            [{"test": "str6"}, {"test": "str7"}],
                        ],
                        dtype=pandas.ArrowDtype(
                            pyarrow.list_(pyarrow.struct([("test", pyarrow.string())])),
                        )
                        if hasattr(pandas, "ArrowDtype")
                        else "object",
                    ),
                },
            ),
            expected_df=pandas.DataFrame(
                {
                    "row_num": [0, 1, 2],
                    "object_struct": pandas.Series(
                        [{"test": "str1"}, {"test": "str2"}, {"test": "str3"}],
                        dtype=pandas.ArrowDtype(
                            pyarrow.struct([("test", pyarrow.string())]),
                        )
                        if hasattr(pandas, "ArrowDtype")
                        else "object",
                    ),
                    # Array of DATETIME requires inspection into list elements.
                    # See:
                    # https://github.com/googleapis/python-bigquery/pull/1061
                    "object_array_datetime": pandas.Series(
                        [[], [datetime.datetime(1998, 9, 4, 12, 0, 0)], []],
                        dtype=pandas.ArrowDtype(pyarrow.list_(pyarrow.timestamp("us")))
                        if hasattr(pandas, "ArrowDtype")
                        else "object",
                    ),
                    "object_array_of_struct": pandas.Series(
                        [[], [{"test": "str4"}], []],
                        dtype=pandas.ArrowDtype(
                            pyarrow.list_(pyarrow.struct([("test", pyarrow.string())])),
                        )
                        if hasattr(pandas, "ArrowDtype")
                        else "object",
                    ),
                    "arrow_struct": pandas.Series(
                        [
                            {"version": 1, "project": "pandas"},
                            {"version": 2, "project": "pandas"},
                            {"version": 1, "project": "numpy"},
                        ],
                        dtype=pandas.ArrowDtype(
                            pyarrow.struct(
                                [
                                    ("version", pyarrow.int64()),
                                    ("project", pyarrow.string()),
                                ]
                            )
                        )
                        if hasattr(pandas, "ArrowDtype")
                        else "object",
                    ),
                    "arrow_array": pandas.Series(
                        [[1, 2, 3], [], [4, 5, 6]],
                        dtype=pandas.ArrowDtype(
                            pyarrow.list_(pyarrow.int64()),
                        )
                        if hasattr(pandas, "ArrowDtype")
                        else "object",
                    ),
                    "arrow_array_of_struct": pandas.Series(
                        [[{"test": "str5"}], [], [{"test": "str6"}, {"test": "str7"}]],
                        dtype=pandas.ArrowDtype(
                            pyarrow.list_(pyarrow.struct([("test", pyarrow.string())])),
                        )
                        if hasattr(pandas, "ArrowDtype")
                        else "object",
                    ),
                },
            ),
            api_methods={"load_parquet"},
        ),
        id="struct",
    ),
]


@pytest.mark.parametrize(
    ["input_df", "expected_df", "table_schema", "api_methods"], DATAFRAME_ROUND_TRIPS
)
def test_dataframe_round_trip_with_table_schema(
    method_under_test,
    read_gbq,
    random_dataset_id,
    input_df,
    expected_df,
    table_schema,
    api_method,
    api_methods,
):
    if api_method not in api_methods:
        pytest.skip(f"{api_method} not supported.")
    if expected_df is None:
        expected_df = input_df
    table_id = f"{random_dataset_id}.round_trip_w_schema_{random.randrange(1_000_000)}"
    method_under_test(
        input_df, table_id, table_schema=table_schema, api_method=api_method
    )
    round_trip = (
        read_gbq(
            table_id,
            dtypes=dict(zip(expected_df.columns, expected_df.dtypes)),
            # BigQuery Storage API is required to avoid out-of-bound due to extra
            # day from rounding error which was fixed in google-cloud-bigquery
            # 2.6.0. https://github.com/googleapis/python-bigquery/pull/402
            use_bqstorage_api=True,
        )
        .set_index("row_num")
        .sort_index()
    )

    # TODO(tswast): Support writing index columns if to_gbq(index=True).
    pandas.testing.assert_frame_equal(
        expected_df.set_index("row_num").sort_index(), round_trip
    )


def test_dataframe_round_trip_with_bq_client(
    to_gbq_with_bq_client, read_gbq_with_bq_client, random_dataset_id
):
    table_id = (
        f"{random_dataset_id}.round_trip_w_bq_client_{random.randrange(1_000_000)}"
    )
    df = pandas.DataFrame({"numbers": pandas.Series([1, 2, 3], dtype="Int64")})

    to_gbq_with_bq_client(df, table_id)
    result = read_gbq_with_bq_client(table_id)

    pandas.testing.assert_frame_equal(result, df)
