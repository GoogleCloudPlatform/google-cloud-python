# Copyright (c) 2024 pandas-gbq Authors All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

import pyarrow
import pytest
from google.cloud import bigquery

from pandas_gbq.schema import pyarrow_to_bigquery


@pytest.mark.parametrize(
    (
        "pyarrow_type",
        "bigquery_type",
    ),
    (
        # All integer types should map to BigQuery INT64 (or INTEGER since
        # SchemaField uses the legacy SQL names). See:
        # https://github.com/googleapis/python-bigquery-pandas/issues/616
        (pyarrow.int8(), "INTEGER"),
        (pyarrow.int16(), "INTEGER"),
        (pyarrow.int32(), "INTEGER"),
        (pyarrow.int64(), "INTEGER"),
        (pyarrow.uint8(), "INTEGER"),
        (pyarrow.uint16(), "INTEGER"),
        (pyarrow.uint32(), "INTEGER"),
        (pyarrow.uint64(), "INTEGER"),
        # If there is no associated timezone, assume a naive (timezone-less)
        # DATETIME. See:
        # https://github.com/googleapis/python-bigquery-pandas/issues/450
        (pyarrow.timestamp("ns"), "DATETIME"),
        (pyarrow.timestamp("ns", tz="UTC"), "TIMESTAMP"),
    ),
)
def test_arrow_type_to_bigquery_field_scalar_types(pyarrow_type, bigquery_type):
    field: bigquery.SchemaField = pyarrow_to_bigquery.arrow_type_to_bigquery_field(
        "test_name", pyarrow_type
    )
    assert field.name == "test_name"
    assert field.field_type == bigquery_type


def test_arrow_type_to_bigquery_field_unknown():
    assert pyarrow_to_bigquery.arrow_type_to_bigquery_field(
        "test_name", pyarrow.null(), default_type="DEFAULT_TYPE"
    ) == bigquery.SchemaField("test_name", "DEFAULT_TYPE")


def test_arrow_type_to_bigquery_field_list_of_unknown():
    assert pyarrow_to_bigquery.arrow_type_to_bigquery_field(
        "test_name",
        pyarrow.list_(pyarrow.null()),
        default_type="DEFAULT_TYPE",
    ) == bigquery.SchemaField("test_name", "DEFAULT_TYPE", mode="REPEATED")
