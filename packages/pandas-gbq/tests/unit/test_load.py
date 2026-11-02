# Copyright (c) 2017 pandas-gbq Authors All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

# -*- coding: utf-8 -*-

import datetime
import decimal
import textwrap
from io import StringIO

import db_dtypes
import numpy
import pandas
import pandas.testing
import pytest

from pandas_gbq import exceptions, load


def load_method(bqclient, api_method):
    return bqclient.load_table_from_dataframe


def test_encode_chunk_with_unicode():
    """Test that a dataframe containing unicode can be encoded as a file.

    See: https://github.com/pydata/pandas-gbq/issues/106
    """
    df = pandas.DataFrame(
        numpy.random.randn(6, 4), index=range(6), columns=list("ABCD")
    )
    df["s"] = "信用卡"
    csv_buffer = load.encode_chunk(df)
    csv_bytes = csv_buffer.read()
    csv_string = csv_bytes.decode("utf-8")
    assert "信用卡" in csv_string


def test_encode_chunk_with_floats():
    """Test that floats in a dataframe are encoded with at most 17 significant
        figures.

    See: https://github.com/pydata/pandas-gbq/issues/192 and
    https://github.com/pydata/pandas-gbq/issues/326
    """
    input_csv = textwrap.dedent(
        """01/01/17 23:00,0.14285714285714285,4
        01/02/17 22:00,1.05148,3
        01/03/17 21:00,1.05153,2
        01/04/17 20:00,3.141592653589793,1
        01/05/17 19:00,2.0988936657440586e+43,0
        """
    )
    input_df = pandas.read_csv(
        StringIO(input_csv), header=None, float_precision="round_trip"
    )
    csv_buffer = load.encode_chunk(input_df)
    round_trip = pandas.read_csv(csv_buffer, header=None, float_precision="round_trip")
    pandas.testing.assert_frame_equal(
        round_trip,
        input_df,
        check_exact=True,
    )


def test_encode_chunk_with_newlines():
    """See: https://github.com/pydata/pandas-gbq/issues/180"""
    df = pandas.DataFrame({"s": ["abcd", "ef\ngh", "ij\r\nkl"]})
    csv_buffer = load.encode_chunk(df)
    csv_bytes = csv_buffer.read()
    csv_string = csv_bytes.decode("utf-8")
    assert "abcd" in csv_string
    assert '"ef\ngh"' in csv_string
    assert '"ij\r\nkl"' in csv_string


def test_split_dataframe():
    df = pandas.DataFrame(numpy.random.randn(6, 4), index=range(6))
    chunks = list(load.split_dataframe(df, chunksize=2))
    assert len(chunks) == 3
    remaining, chunk = chunks[0]
    assert remaining == 4
    assert len(chunk.index) == 2


def test_encode_chunks_with_chunksize_none():
    df = pandas.DataFrame(numpy.random.randn(6, 4), index=range(6))
    chunks = list(load.split_dataframe(df))
    assert len(chunks) == 1
    remaining, chunk = chunks[0]
    assert remaining == 0
    assert len(chunk.index) == 6


def test_load_csv_from_dataframe_allows_client_to_generate_schema(mock_bigquery_client):
    import google.cloud.bigquery

    df = pandas.DataFrame({"int_col": [1, 2, 3]})
    destination = google.cloud.bigquery.TableReference.from_string(
        "my-project.my_dataset.my_table"
    )

    _ = list(
        load.load_csv_from_dataframe(
            mock_bigquery_client, df, destination, None, None, None, None
        )
    )

    mock_load = mock_bigquery_client.load_table_from_dataframe
    assert mock_load.called
    _, kwargs = mock_load.call_args
    assert "job_config" in kwargs
    assert kwargs["job_config"].schema is None


def test_load_csv_from_file_generates_schema(mock_bigquery_client):
    import google.cloud.bigquery

    df = pandas.DataFrame(
        {
            "int_col": [1, 2, 3],
            "bool_col": [True, False, True],
            "float_col": [0.0, 1.25, -2.75],
            "string_col": ["a", "b", "c"],
            "datetime_col": pandas.Series(
                [
                    "2021-12-21 13:28:40.123789",
                    "2000-01-01 11:10:09",
                    "2040-10-31 23:59:59.999999",
                ],
                dtype="datetime64[ns]",
            ),
            "timestamp_col": pandas.Series(
                [
                    "2021-12-21 13:28:40.123789",
                    "2000-01-01 11:10:09",
                    "2040-10-31 23:59:59.999999",
                ],
                dtype="datetime64[ns]",
            ).dt.tz_localize(datetime.timezone.utc),
        }
    )
    destination = google.cloud.bigquery.TableReference.from_string(
        "my-project.my_dataset.my_table"
    )

    _ = list(
        load.load_csv_from_file(
            mock_bigquery_client, df, destination, None, None, None, None
        )
    )

    mock_load = mock_bigquery_client.load_table_from_file
    assert mock_load.called
    _, kwargs = mock_load.call_args
    assert "job_config" in kwargs
    sent_schema = kwargs["job_config"].schema
    assert len(sent_schema) == len(df.columns)
    assert sent_schema[0].name == "int_col"
    assert sent_schema[0].field_type == "INTEGER"
    assert sent_schema[1].name == "bool_col"
    assert sent_schema[1].field_type == "BOOLEAN"
    assert sent_schema[2].name == "float_col"
    assert sent_schema[2].field_type == "FLOAT"
    assert sent_schema[3].name == "string_col"
    assert sent_schema[3].field_type == "STRING"
    assert sent_schema[4].name == "datetime_col"
    assert sent_schema[4].field_type == "DATETIME"
    assert sent_schema[5].name == "timestamp_col"
    assert sent_schema[5].field_type == "TIMESTAMP"


@pytest.mark.parametrize(
    ["api_method"],
    [("load_parquet",), ("load_csv",)],
)
def test_load_chunks_omits_policy_tags(monkeypatch, mock_bigquery_client, api_method):
    """Ensure that policyTags are omitted.

    We don't want to change the policyTags via a load job, as this can cause
    403 error. See: https://github.com/googleapis/python-bigquery/pull/557
    """
    import google.cloud.bigquery

    df = pandas.DataFrame({"col1": [1, 2, 3]})
    destination = google.cloud.bigquery.TableReference.from_string(
        "my-project.my_dataset.my_table"
    )
    schema = {
        "fields": [
            {"name": "col1", "type": "INT64", "policyTags": {"names": ["tag1", "tag2"]}}
        ]
    }

    _ = list(
        load.load_chunks(
            mock_bigquery_client, df, destination, schema=schema, api_method=api_method
        )
    )

    mock_load = load_method(mock_bigquery_client, api_method=api_method)
    assert mock_load.called
    _, kwargs = mock_load.call_args
    assert "job_config" in kwargs
    sent_field = kwargs["job_config"].schema[0].to_api_repr()
    assert "policyTags" not in sent_field


def test_load_chunks_with_invalid_api_method():
    with pytest.raises(ValueError, match="Got unexpected api_method:"):
        load.load_chunks(None, None, None, None, api_method="not_a_thing")


def test_load_parquet_allows_client_to_generate_schema(mock_bigquery_client):
    import google.cloud.bigquery

    df = pandas.DataFrame({"int_col": [1, 2, 3]})
    destination = google.cloud.bigquery.TableReference.from_string(
        "my-project.my_dataset.my_table"
    )

    load.load_parquet(
        mock_bigquery_client,
        df,
        destination,
        None,
        None,
        None,
    )

    mock_load = mock_bigquery_client.load_table_from_dataframe
    assert mock_load.called
    _, kwargs = mock_load.call_args
    assert "job_config" in kwargs
    assert kwargs["job_config"].schema is None


def test_load_parquet_with_bad_conversion(mock_bigquery_client):
    import google.cloud.bigquery
    import pyarrow

    mock_bigquery_client.load_table_from_dataframe.side_effect = (
        pyarrow.lib.ArrowInvalid()
    )
    df = pandas.DataFrame({"int_col": [1, 2, 3]})
    destination = google.cloud.bigquery.TableReference.from_string(
        "my-project.my_dataset.my_table"
    )

    with pytest.raises(exceptions.ConversionError):
        load.load_parquet(mock_bigquery_client, df, destination, None, None, None)


@pytest.mark.parametrize(
    ("numeric_type",),
    (
        ("NUMERIC",),
        ("DECIMAL",),
        ("BIGNUMERIC",),
        ("BIGDECIMAL",),
        ("numeric",),
        ("decimal",),
        ("bignumeric",),
        ("bigdecimal",),
    ),
)
def test_cast_dataframe_for_parquet_w_float_numeric(numeric_type):
    dataframe = pandas.DataFrame(
        {
            "row_num": [0, 1, 2],
            "num_col": pandas.Series(
                # Very much not recommend as the whole point of NUMERIC is to
                # be more accurate than a floating point number, but tested to
                # keep compatibility with CSV-based uploads. See:
                # https://github.com/googleapis/python-bigquery-pandas/issues/421
                [1.25, -1.25, 42.5],
                dtype="float64",
            ),
            "row_num_2": [0, 1, 2],
        },
        # Use multiple columns to ensure column order is maintained.
        columns=["row_num", "num_col", "row_num_2"],
    )
    schema = {
        "fields": [
            {"name": "num_col", "type": numeric_type},
            {"name": "not_in_df", "type": "IGNORED"},
        ]
    }
    result = load.cast_dataframe_for_parquet(dataframe, schema)
    expected = pandas.DataFrame(
        {
            "row_num": [0, 1, 2],
            "num_col": pandas.Series(
                [decimal.Decimal(1.25), decimal.Decimal(-1.25), decimal.Decimal(42.5)],
                dtype="object",
            ),
            "row_num_2": [0, 1, 2],
        },
        columns=["row_num", "num_col", "row_num_2"],
    )
    pandas.testing.assert_frame_equal(result, expected)


def test_cast_dataframe_for_parquet_w_string_date():
    dataframe = pandas.DataFrame(
        {
            "row_num": [0, 1, 2],
            "date_col": pandas.Series(
                ["2021-04-17", "1999-12-31", "2038-01-19"],
                dtype="object",
            ),
            "row_num_2": [0, 1, 2],
        },
        # Use multiple columns to ensure column order is maintained.
        columns=["row_num", "date_col", "row_num_2"],
    )
    schema = {
        "fields": [
            {"name": "date_col", "type": "DATE"},
            {"name": "not_in_df", "type": "IGNORED"},
        ]
    }
    result = load.cast_dataframe_for_parquet(dataframe, schema)
    expected = pandas.DataFrame(
        {
            "row_num": [0, 1, 2],
            "date_col": pandas.Series(
                ["2021-04-17", "1999-12-31", "2038-01-19"],
                dtype=db_dtypes.DateDtype(),
            ),
            "row_num_2": [0, 1, 2],
        },
        columns=["row_num", "date_col", "row_num_2"],
    )
    pandas.testing.assert_frame_equal(result, expected)


def test_cast_dataframe_for_parquet_ignores_repeated_fields():
    dataframe = pandas.DataFrame(
        {
            "row_num": [0, 1, 2],
            "repeated_col": pandas.Series(
                [
                    [datetime.date(2021, 4, 17)],
                    [datetime.date(199, 12, 31)],
                    [datetime.date(2038, 1, 19)],
                ],
                dtype="object",
            ),
            "row_num_2": [0, 1, 2],
        },
        # Use multiple columns to ensure column order is maintained.
        columns=["row_num", "repeated_col", "row_num_2"],
    )
    expected = dataframe.copy()
    schema = {"fields": [{"name": "repeated_col", "type": "DATE", "mode": "REPEATED"}]}
    result = load.cast_dataframe_for_parquet(dataframe, schema)
    pandas.testing.assert_frame_equal(result, expected)


def test_cast_dataframe_for_parquet_w_null_fields():
    dataframe = pandas.DataFrame({"int_col": [0, 1, 2], "str_col": ["a", "b", "c"]})
    expected = dataframe.copy()
    schema = {"fields": None}
    result = load.cast_dataframe_for_parquet(dataframe, schema)
    pandas.testing.assert_frame_equal(result, expected)


# Verifies null numerics are properly handled
# https://github.com/googleapis/python-bigquery-pandas/issues/719
def test_cast_dataframe_for_parquet_w_null_numerics():
    from decimal import Decimal

    nans = pandas.Series([Decimal("3.14"), Decimal("nan"), None, pandas.NA])
    dataframe = pandas.DataFrame({"A": nans})

    schema = {"fields": [{"name": "A", "type": "BIGNUMERIC"}]}
    result = load.cast_dataframe_for_parquet(dataframe, schema)

    # pandas.testing.assert_frame_equal() doesn't distinguish Decimal("NaN")
    # vs. None, verify Decimal("NaN") directly.
    # https://github.com/pandas-dev/pandas/issues/18463
    assert result["A"][1].is_nan()
    assert result["A"][2].is_nan()
    assert result["A"][3].is_nan()
