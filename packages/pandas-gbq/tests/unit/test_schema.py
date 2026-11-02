# Copyright (c) 2017 pandas-gbq Authors All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

import datetime
from typing import Any, Dict, List

import google.cloud.bigquery
import pandas
import pyarrow
import pytest

import pandas_gbq
import pandas_gbq.gbq
import pandas_gbq.schema


@pytest.mark.parametrize(
    "original_fields,dataframe_fields",
    [
        (
            [
                {"name": "A", "type": "FLOAT"},
                {"name": "B", "type": "FLOAT64"},
                {"name": "C", "type": "STRING"},
            ],
            [{"name": "A", "type": "FLOAT64"}, {"name": "B", "type": "FLOAT"}],
        ),
        # Original schema from API may contain legacy SQL datatype names.
        # https://github.com/pydata/pandas-gbq/issues/322
        (
            [{"name": "A", "type": "INTEGER"}],
            [{"name": "A", "type": "INT64"}],
        ),
        (
            [{"name": "A", "type": "BOOL"}],
            [{"name": "A", "type": "BOOLEAN"}],
        ),
        (
            # TODO: include sub-fields when struct uploads are supported.
            [{"name": "A", "type": "STRUCT"}],
            [{"name": "A", "type": "RECORD"}],
        ),
    ],
)
def test_schema_is_subset_passes_if_subset(original_fields, dataframe_fields):
    # Issue #24 schema_is_subset indicates whether the schema of the
    # dataframe is a subset of the schema of the bigquery table
    table_schema = {"fields": original_fields}
    tested_schema = {"fields": dataframe_fields}
    assert pandas_gbq.schema.schema_is_subset(table_schema, tested_schema)


def test_schema_is_subset_fails_if_not_subset():
    table_schema = {
        "fields": [
            {"name": "A", "type": "FLOAT"},
            {"name": "B", "type": "FLOAT"},
            {"name": "C", "type": "STRING"},
        ]
    }
    tested_schema = {
        "fields": [{"name": "A", "type": "FLOAT"}, {"name": "C", "type": "FLOAT"}]
    }
    assert not pandas_gbq.schema.schema_is_subset(table_schema, tested_schema)


@pytest.mark.parametrize(
    "dataframe,expected_schema",
    [
        pytest.param(
            pandas.DataFrame(data={"col1": [object()]}),
            {"fields": [{"name": "col1", "type": "DEFAULT_TYPE"}]},
            id="default-type-fails-pyarrow-conversion",
        ),
        (
            pandas.DataFrame(data={"col1": [1, 2, 3]}),
            {"fields": [{"name": "col1", "type": "INTEGER"}]},
        ),
        (
            pandas.DataFrame(data={"col1": [True, False]}),
            {"fields": [{"name": "col1", "type": "BOOLEAN"}]},
        ),
        (
            pandas.DataFrame(data={"col1": [1.0, 3.14]}),
            {"fields": [{"name": "col1", "type": "FLOAT"}]},
        ),
        (
            pandas.DataFrame(data={"col1": ["hello", "world"]}),
            {"fields": [{"name": "col1", "type": "STRING"}]},
        ),
        pytest.param(
            # No time zone -> DATETIME,
            # Time zone -> TIMESTAMP
            # See: https://github.com/googleapis/python-bigquery-pandas/issues/450
            pandas.DataFrame(
                data={
                    "object1": pandas.Series([datetime.datetime.now()], dtype="object"),
                    "object2": pandas.Series(
                        [datetime.datetime.now(datetime.timezone.utc)], dtype="object"
                    ),
                    "datetime1": pandas.Series(
                        [datetime.datetime.now()], dtype="datetime64[ns]"
                    ),
                    "datetime2": pandas.Series(
                        [datetime.datetime.now(datetime.timezone.utc)],
                        dtype="datetime64[ns, UTC]",
                    ),
                }
            ),
            {
                "fields": [
                    {"name": "object1", "type": "DATETIME"},
                    {"name": "object2", "type": "TIMESTAMP"},
                    {"name": "datetime1", "type": "DATETIME"},
                    {"name": "datetime2", "type": "TIMESTAMP"},
                ]
            },
            id="issue450-datetime",
        ),
        (
            pandas.DataFrame(
                data={
                    "col0": [datetime.datetime.now(datetime.timezone.utc)],
                    "col1": [datetime.datetime.now()],
                    "col2": ["hello"],
                    "col3": [3.14],
                    "col4": [True],
                    "col5": [4],
                }
            ),
            {
                "fields": [
                    {"name": "col0", "type": "TIMESTAMP"},
                    {"name": "col1", "type": "DATETIME"},
                    {"name": "col2", "type": "STRING"},
                    {"name": "col3", "type": "FLOAT"},
                    {"name": "col4", "type": "BOOLEAN"},
                    {"name": "col5", "type": "INTEGER"},
                ]
            },
        ),
        pytest.param(
            # uint8, which is the result from get_dummies, should be INTEGER.
            # https://github.com/googleapis/python-bigquery-pandas/issues/616
            pandas.DataFrame({"col": [0, 1]}, dtype="uint8"),
            {"fields": [{"name": "col", "type": "INTEGER"}]},
            id="issue616-uint8",
        ),
        pytest.param(
            # object column containing dictionaries should load to STRUCT.
            # https://github.com/googleapis/python-bigquery-pandas/issues/452
            pandas.DataFrame(
                {
                    "my_struct": pandas.Series(
                        [{"test": "str1"}, {"test": "str2"}, {"test": "str3"}],
                        dtype="object",
                    ),
                }
            ),
            {
                "fields": [
                    {
                        "name": "my_struct",
                        "type": "RECORD",
                        "fields": [
                            {"name": "test", "type": "STRING", "mode": "NULLABLE"}
                        ],
                    }
                ]
            },
            id="issue452-struct",
        ),
        pytest.param(
            pandas.DataFrame(
                {
                    "object": pandas.Series([[], ["abc"], []], dtype="object"),
                    "list": pandas.Series(
                        [[], [1, 2, 3], []],
                        dtype=pandas.ArrowDtype(pyarrow.list_(pyarrow.int64()))
                        if hasattr(pandas, "ArrowDtype")
                        else "object",
                    ),
                    "list_of_struct": pandas.Series(
                        [[], [{"test": 123.0}], []],
                        dtype=pandas.ArrowDtype(
                            pyarrow.list_(pyarrow.struct([("test", pyarrow.float64())]))
                        )
                        if hasattr(pandas, "ArrowDtype")
                        else "object",
                    ),
                    "list_of_unknown": [[], [], []],
                    "list_of_null": [[None, None], [None], [None, None]],
                }
            ),
            {
                "fields": [
                    {"name": "object", "type": "STRING", "mode": "REPEATED"},
                    {"name": "list", "type": "INTEGER", "mode": "REPEATED"},
                    {
                        "name": "list_of_struct",
                        "type": "RECORD",
                        "mode": "REPEATED",
                        "fields": [
                            {"name": "test", "type": "FLOAT", "mode": "NULLABLE"},
                        ],
                    },
                    # Use DEFAULT_TYPE because there are no values to detect a type.
                    {
                        "name": "list_of_unknown",
                        "type": "DEFAULT_TYPE",
                        "mode": "REPEATED",
                    },
                    {
                        "name": "list_of_null",
                        "type": "DEFAULT_TYPE",
                        "mode": "REPEATED",
                    },
                ],
            },
            id="array",
        ),
        pytest.param(
            # If a struct contains only nulls in a sub-field, use the default
            # type for subfields without a type we can determine.
            # https://github.com/googleapis/python-bigquery-pandas/issues/836
            pandas.DataFrame(
                {
                    "id": [0, 1],
                    "positions": [{"state": None}, {"state": None}],
                },
            ),
            {
                "fields": [
                    {"name": "id", "type": "INTEGER"},
                    {
                        "name": "positions",
                        "type": "RECORD",
                        "fields": [
                            {
                                "name": "state",
                                "type": "DEFAULT_TYPE",
                                "mode": "NULLABLE",
                            },
                        ],
                    },
                ],
            },
            id="issue832-null-struct-field",
        ),
    ],
)
def test_generate_bq_schema(dataframe, expected_schema):
    schema = pandas_gbq.gbq._generate_bq_schema(dataframe, default_type="DEFAULT_TYPE")

    # NULLABLE is the default mode.
    for field in expected_schema["fields"]:
        if "mode" not in field:
            field["mode"] = "NULLABLE"

    assert schema == expected_schema


@pytest.mark.parametrize(
    "schema_old,schema_new,expected_output",
    [
        (
            {"fields": [{"name": "col1", "type": "INTEGER"}]},
            {"fields": [{"name": "col2", "type": "TIMESTAMP"}]},
            # Ignore fields that aren't in the DataFrame.
            {"fields": [{"name": "col1", "type": "INTEGER"}]},
        ),
        (
            {"fields": [{"name": "col1", "type": "INTEGER"}]},
            {"fields": [{"name": "col1", "type": "BOOLEAN"}]},
            # Update type for fields that are in the DataFrame.
            {"fields": [{"name": "col1", "type": "BOOLEAN"}]},
        ),
        (
            {
                "fields": [
                    {"name": "col1", "type": "INTEGER"},
                    {"name": "col2", "type": "INTEGER"},
                ]
            },
            {
                "fields": [
                    {"name": "col2", "type": "BOOLEAN"},
                    {"name": "col3", "type": "FLOAT"},
                ]
            },
            {
                "fields": [
                    {"name": "col1", "type": "INTEGER"},
                    {"name": "col2", "type": "BOOLEAN"},
                ]
            },
        ),
    ],
)
def test_update_schema(schema_old, schema_new, expected_output):
    output = pandas_gbq.schema.update_schema(schema_old, schema_new)
    assert output == expected_output


@pytest.mark.parametrize(
    ["bq_schema", "expected"],
    [
        ([], {"fields": []}),
        (
            [google.cloud.bigquery.SchemaField("test_col", "STRING")],
            {"fields": [{"name": "test_col", "type": "STRING", "mode": "NULLABLE"}]},
        ),
        (
            [google.cloud.bigquery.SchemaField("test_col", "STRING", mode="REQUIRED")],
            {"fields": [{"name": "test_col", "type": "STRING", "mode": "REQUIRED"}]},
        ),
        (
            [
                google.cloud.bigquery.SchemaField("test1", "STRING"),
                google.cloud.bigquery.SchemaField("test2", "INTEGER"),
            ],
            {
                "fields": [
                    {"name": "test1", "type": "STRING", "mode": "NULLABLE"},
                    {"name": "test2", "type": "INTEGER", "mode": "NULLABLE"},
                ]
            },
        ),
    ],
)
def test_to_pandas_gbq(
    bq_schema: List[google.cloud.bigquery.SchemaField], expected: Dict[str, Any]
):
    import pandas_gbq.schema

    result = pandas_gbq.schema.to_pandas_gbq(bq_schema)
    assert result == expected
