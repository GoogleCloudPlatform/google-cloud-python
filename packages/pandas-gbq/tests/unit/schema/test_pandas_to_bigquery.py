# Copyright (c) 2019 pandas-gbq Authors All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

import collections
import datetime
import decimal
import operator

import pandas
import pytest
from google.cloud.bigquery import schema


@pytest.fixture
def module_under_test():
    from pandas_gbq.schema import pandas_to_bigquery

    return pandas_to_bigquery


def test_dataframe_to_bigquery_fields_w_named_index(module_under_test):
    df_data = collections.OrderedDict(
        [
            ("str_index", ["a", "b"]),
            ("str_column", ["hello", "world"]),
            ("int_column", [42, 8]),
            ("nullable_int_column", pandas.Series([42, None], dtype="Int64")),
            ("uint_column", pandas.Series([7, 13], dtype="uint8")),
            ("bool_column", [True, False]),
            ("boolean_column", pandas.Series([True, None], dtype="boolean")),
            (
                "datetime_column",
                [
                    datetime.datetime(1999, 12, 31, 23, 59, 59, 999999),
                    datetime.datetime(2000, 1, 1, 0, 0, 0),
                ],
            ),
            (
                "timestamp_column",
                [
                    datetime.datetime(
                        1999, 12, 31, 23, 59, 59, 999999, tzinfo=datetime.timezone.utc
                    ),
                    datetime.datetime(
                        2000, 1, 1, 0, 0, 0, tzinfo=datetime.timezone.utc
                    ),
                ],
            ),
            # Need to fallback to Arrow to avoid data loss and disambiguate
            # NUMERIC from BIGNUMERIC. We don't want to pick too small of a
            # type and lose precision. See:
            # https://github.com/googleapis/python-bigquery/issues/1650
            #
            (
                "bignumeric_column",
                [
                    # Start with a lower precision Decimal to make sure we
                    # aren't trying to determine the type from just one value.
                    decimal.Decimal("1.25"),
                    decimal.Decimal("0.1234567891"),
                ],
            ),
            (
                "numeric_column",
                [
                    # Minimum value greater than 0 that can be handled: 1e-9
                    # https://cloud.google.com/bigquery/docs/reference/standard-sql/data-types#numeric_types
                    decimal.Decimal("0.000000001"),
                    decimal.Decimal("-0.000000001"),
                ],
            ),
        ]
    )
    dataframe = pandas.DataFrame(df_data).set_index("str_index", drop=True)

    returned_schema = module_under_test.dataframe_to_bigquery_fields(
        dataframe, [], index=True
    )

    expected_schema = (
        schema.SchemaField("str_index", "STRING", "NULLABLE"),
        schema.SchemaField("str_column", "STRING", "NULLABLE"),
        schema.SchemaField("int_column", "INTEGER", "NULLABLE"),
        schema.SchemaField("nullable_int_column", "INTEGER", "NULLABLE"),
        schema.SchemaField("uint_column", "INTEGER", "NULLABLE"),
        schema.SchemaField("bool_column", "BOOLEAN", "NULLABLE"),
        schema.SchemaField("boolean_column", "BOOLEAN", "NULLABLE"),
        schema.SchemaField("datetime_column", "DATETIME", "NULLABLE"),
        schema.SchemaField("timestamp_column", "TIMESTAMP", "NULLABLE"),
        schema.SchemaField("bignumeric_column", "BIGNUMERIC", "NULLABLE"),
        schema.SchemaField("numeric_column", "NUMERIC", "NULLABLE"),
    )
    assert returned_schema == expected_schema


def test_dataframe_to_bigquery_fields_w_multiindex(module_under_test):
    df_data = collections.OrderedDict(
        [
            ("str_index", ["a", "a"]),
            ("int_index", [0, 0]),
            (
                "dt_index",
                [
                    datetime.datetime(1999, 12, 31, 23, 59, 59, 999999),
                    datetime.datetime(2000, 1, 1, 0, 0, 0),
                ],
            ),
            ("str_column", ["hello", "world"]),
            ("int_column", [42, 8]),
            ("bool_column", [True, False]),
        ]
    )
    dataframe = pandas.DataFrame(df_data).set_index(
        ["str_index", "int_index", "dt_index"],
        drop=True,
    )

    returned_schema = module_under_test.dataframe_to_bigquery_fields(
        dataframe, [], index=True
    )

    expected_schema = (
        schema.SchemaField("str_index", "STRING", "NULLABLE"),
        schema.SchemaField("int_index", "INTEGER", "NULLABLE"),
        schema.SchemaField("dt_index", "DATETIME", "NULLABLE"),
        schema.SchemaField("str_column", "STRING", "NULLABLE"),
        schema.SchemaField("int_column", "INTEGER", "NULLABLE"),
        schema.SchemaField("bool_column", "BOOLEAN", "NULLABLE"),
    )
    assert returned_schema == expected_schema


def test_dataframe_to_bigquery_fields_w_bq_schema(module_under_test):
    df_data = collections.OrderedDict(
        [
            ("str_column", ["hello", "world"]),
            ("int_column", [42, 8]),
            ("bool_column", [True, False]),
        ]
    )
    dataframe = pandas.DataFrame(df_data)

    dict_schema = [
        {"name": "str_column", "type": "STRING", "mode": "NULLABLE"},
        {"name": "bool_column", "type": "BOOL", "mode": "REQUIRED"},
    ]

    returned_schema = module_under_test.dataframe_to_bigquery_fields(
        dataframe, dict_schema
    )

    expected_schema = (
        schema.SchemaField("str_column", "STRING", "NULLABLE"),
        schema.SchemaField("int_column", "INTEGER", "NULLABLE"),
        schema.SchemaField("bool_column", "BOOL", "REQUIRED"),
    )
    assert returned_schema == expected_schema


def test_dataframe_to_bigquery_fields_fallback_needed_w_pyarrow(module_under_test):
    dataframe = pandas.DataFrame(
        data=[
            {"id": 10, "status": "FOO", "created_at": datetime.date(2019, 5, 10)},
            {"id": 20, "status": "BAR", "created_at": datetime.date(2018, 9, 12)},
        ]
    )

    detected_schema = module_under_test.dataframe_to_bigquery_fields(
        dataframe, override_bigquery_fields=[]
    )
    expected_schema = (
        schema.SchemaField("id", "INTEGER", mode="NULLABLE"),
        schema.SchemaField("status", "STRING", mode="NULLABLE"),
        schema.SchemaField("created_at", "DATE", mode="NULLABLE"),
    )
    by_name = operator.attrgetter("name")
    assert sorted(detected_schema, key=by_name) == sorted(expected_schema, key=by_name)


def test_dataframe_to_bigquery_fields_w_extra_fields(module_under_test):
    dataframe = pandas.DataFrame({"in_df": [1, 2, 3]})
    bq_schema = (
        schema.SchemaField("in_df", "INTEGER"),
        schema.SchemaField("not_in_df", "STRING"),
        schema.SchemaField("also_not_in_df", "INTEGER"),
    )

    with pytest.warns(UserWarning) as record:
        returned_schema = module_under_test.dataframe_to_bigquery_fields(
            dataframe, override_bigquery_fields=bq_schema
        )

    assert len(record) == 1
    message = str(record[0].message)
    assert (
        "Provided BigQuery fields contain field(s) not present in DataFrame" in message
    )
    # Note: The field names are sorted in the warning message.
    assert "['also_not_in_df', 'not_in_df']" in message

    expected_schema = (
        schema.SchemaField("in_df", "INTEGER"),
        # Note: The fields are sorted by name as they are added from the set of
        # unused fields.
        schema.SchemaField("also_not_in_df", "INTEGER"),
        schema.SchemaField("not_in_df", "STRING"),
    )
    assert returned_schema == expected_schema


def test_dataframe_to_bigquery_fields_geography(module_under_test):
    geopandas = pytest.importorskip("geopandas")
    from shapely import wkt

    df = geopandas.GeoDataFrame(
        pandas.DataFrame(
            dict(
                name=["foo", "bar"],
                geo1=[None, None],
                geo2=[None, wkt.loads("Point(1 1)")],
            )
        ),
        geometry="geo1",
    )
    bq_schema = module_under_test.dataframe_to_bigquery_fields(df, [])
    assert bq_schema == (
        schema.SchemaField("name", "STRING"),
        schema.SchemaField("geo1", "GEOGRAPHY"),
        schema.SchemaField("geo2", "GEOGRAPHY"),
    )
