# Copyright (c) 2017 pandas-gbq Authors All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

"""Unit tests for TIMESTAMP data type helpers."""

import pandas
import pandas.testing
import pytest


@pytest.fixture
def module_under_test():
    from pandas_gbq import timestamp

    return timestamp


def test_localize_df_with_empty_dataframe(module_under_test):
    df = pandas.DataFrame({"timestamp_col": [], "other_col": []})
    original = df.copy()
    bq_schema = [
        {"name": "timestamp_col", "type": "TIMESTAMP"},
        {"name": "other_col", "type": "STRING"},
    ]

    localized = module_under_test.localize_df(df, bq_schema)

    # Empty DataFrames should be unchanged.
    assert localized is df
    pandas.testing.assert_frame_equal(localized, original)


def test_localize_df_with_no_timestamp_columns(module_under_test):
    df = pandas.DataFrame({"integer_col": [1, 2, 3], "float_col": [0.1, 0.2, 0.3]})
    original = df.copy()
    bq_schema = [
        {"name": "integer_col", "type": "INTEGER"},
        {"name": "float_col", "type": "FLOAT"},
    ]

    localized = module_under_test.localize_df(df, bq_schema)

    # DataFrames with no TIMESTAMP columns should be unchanged.
    assert localized is df
    pandas.testing.assert_frame_equal(localized, original)


def test_localize_df_with_timestamp_column(module_under_test):
    df = pandas.DataFrame(
        {
            "integer_col": [1, 2, 3],
            "timestamp_col": pandas.Series(
                ["2011-01-01 01:02:03", "2012-02-02 04:05:06", "2013-03-03 07:08:09"],
                dtype="datetime64[ns]",
            ),
            "float_col": [0.1, 0.2, 0.3],
            "repeated_col": pandas.Series(
                [
                    ["2011-01-01 01:02:03"],
                    ["2012-02-02 04:05:06"],
                    ["2013-03-03 07:08:09"],
                ],
                dtype="object",
            ),
        }
    )
    expected = df.copy()
    expected["timestamp_col"] = df["timestamp_col"].dt.tz_localize("UTC")
    bq_schema = [
        {"name": "integer_col", "type": "INTEGER"},
        {"name": "timestamp_col", "type": "TIMESTAMP"},
        {"name": "float_col", "type": "FLOAT"},
        {"name": "repeated_col", "type": "TIMESTAMP", "mode": "REPEATED"},
    ]

    localized = module_under_test.localize_df(df, bq_schema)
    pandas.testing.assert_frame_equal(localized, expected)
