# Copyright 2026 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import datetime
import decimal
from unittest import mock

import pytest

from google.cloud.bigquery_storage import types
from google.cloud.bigquery_storage_v1 import reader

pyarrow = pytest.importorskip("pyarrow")


_TEST_SCHEMA = pyarrow.schema(
    [
        pyarrow.field("int_col", pyarrow.int64()),
        pyarrow.field("float_col", pyarrow.float64()),
        pyarrow.field("num_col", pyarrow.decimal128(38, 9)),
        pyarrow.field("bool_col", pyarrow.bool_()),
        pyarrow.field("str_col", pyarrow.utf8()),
        pyarrow.field("bytes_col", pyarrow.binary()),
        pyarrow.field("date_col", pyarrow.date32()),
        pyarrow.field("ts_col", pyarrow.timestamp("us", tz="UTC")),
    ]
)

_TEST_ROWS = [
    {
        "int_col": 123,
        "float_col": 3.14,
        "num_col": decimal.Decimal("9.99"),
        "bool_col": True,
        "str_col": "hello world",
        "bytes_col": b"ascii bytes",
        "date_col": datetime.date(1998, 9, 4),
        "ts_col": datetime.datetime(2000, 1, 1, 5, 0, tzinfo=datetime.timezone.utc),
    },
    {
        "int_col": 456,
        "float_col": 2.72,
        "num_col": decimal.Decimal("0.99"),
        "bool_col": False,
        "str_col": "hallo welt",
        "bytes_col": b"\xbb\xee\xff",
        "date_col": datetime.date(1995, 3, 2),
        "ts_col": datetime.datetime(1965, 4, 3, 2, 1, tzinfo=datetime.timezone.utc),
    },
]


def _create_sample_batch(schema=_TEST_SCHEMA, rows=_TEST_ROWS):
    arrays = [
        pyarrow.array([row[field.name] for row in rows], type=field.type)
        for field in schema
    ]
    return pyarrow.RecordBatch.from_arrays(arrays, schema=schema)


def _create_read_rows_response(record_batch=None):
    response = types.ReadRowsResponse()
    if record_batch is not None:
        response.row_count = record_batch.num_rows
        response.arrow_record_batch.serialized_record_batch = (
            record_batch.serialize().to_pybytes()
        )
    else:
        response.row_count = 0
        response.arrow_record_batch.serialized_record_batch = b""
    return response


def _create_read_session(schema=_TEST_SCHEMA):
    return types.ReadSession(
        arrow_schema={"serialized_schema": schema.serialize().to_pybytes()}
    )


def test_from_read_rows_response_decodes_serialized_record_batch():
    pandas_gbq_arrow = pytest.importorskip("pandas_gbq.arrow")
    expected_batch = _create_sample_batch()
    response = _create_read_rows_response(expected_batch)

    actual_batch = pandas_gbq_arrow.from_read_rows_response(
        response, arrow_schema=_TEST_SCHEMA
    )

    assert actual_batch.equals(expected_batch)


def test_from_read_rows_response_handles_empty_response():
    pandas_gbq_arrow = pytest.importorskip("pandas_gbq.arrow")
    response = _create_read_rows_response(record_batch=None)

    actual_batch = pandas_gbq_arrow.from_read_rows_response(
        response, arrow_schema=_TEST_SCHEMA
    )

    assert actual_batch.num_rows == 0
    assert actual_batch.schema == _TEST_SCHEMA


def test_read_rows_page_to_arrow_delegates_when_pandas_gbq_installed():
    pytest.importorskip("pandas_gbq")
    expected_batch = _create_sample_batch()
    response = _create_read_rows_response(expected_batch)
    stream_parser = reader._ArrowStreamParser(_create_read_session(_TEST_SCHEMA))
    page = reader.ReadRowsPage(stream_parser, response)

    with pytest.warns(
        PendingDeprecationWarning,
        match="google-cloud-bigquery-storage is deprecated",
    ):
        actual_batch = page.to_arrow()

    assert actual_batch.equals(expected_batch)


def test_read_rows_page_to_arrow_falls_back_when_pandas_gbq_uninstalled():
    expected_batch = _create_sample_batch()
    response = _create_read_rows_response(expected_batch)
    stream_parser = reader._ArrowStreamParser(_create_read_session(_TEST_SCHEMA))
    page = reader.ReadRowsPage(stream_parser, response)

    with (
        mock.patch.dict("sys.modules", {"pandas_gbq": None, "pandas_gbq.arrow": None}),
        pytest.warns(
            PendingDeprecationWarning,
            match="google-cloud-bigquery-storage is deprecated",
        ),
    ):
        actual_batch = page.to_arrow()

    assert actual_batch.equals(expected_batch)


def test_read_rows_page_to_arrow_empty_batch_delegates_when_pandas_gbq_installed():
    pytest.importorskip("pandas_gbq")
    empty_batch = _create_sample_batch(rows=[])
    response = _create_read_rows_response(record_batch=empty_batch)
    stream_parser = reader._ArrowStreamParser(_create_read_session(_TEST_SCHEMA))
    page = reader.ReadRowsPage(stream_parser, response)

    with pytest.warns(
        PendingDeprecationWarning,
        match="google-cloud-bigquery-storage is deprecated",
    ):
        actual_batch = page.to_arrow()

    assert actual_batch.num_rows == 0
    assert actual_batch.schema == _TEST_SCHEMA


def test_read_rows_page_to_arrow_empty_batch_falls_back_when_pandas_gbq_uninstalled():
    empty_batch = _create_sample_batch(rows=[])
    response = _create_read_rows_response(record_batch=empty_batch)
    stream_parser = reader._ArrowStreamParser(_create_read_session(_TEST_SCHEMA))
    page = reader.ReadRowsPage(stream_parser, response)

    with (
        mock.patch.dict("sys.modules", {"pandas_gbq": None, "pandas_gbq.arrow": None}),
        pytest.warns(
            PendingDeprecationWarning,
            match="google-cloud-bigquery-storage is deprecated",
        ),
    ):
        actual_batch = page.to_arrow()

    assert actual_batch.num_rows == 0
    assert actual_batch.schema == _TEST_SCHEMA


def test_read_rows_stream_to_arrow_concatenates_multiple_batches():
    batch1 = _create_sample_batch()
    batch2 = _create_sample_batch()
    response1 = _create_read_rows_response(batch1)
    response2 = _create_read_rows_response(batch2)
    read_session = _create_read_session(_TEST_SCHEMA)
    gapic_client = mock.Mock()
    gapic_client.read_rows.return_value = iter([response1, response2])
    read_rows_stream = reader.ReadRowsStream(
        gapic_client,
        "projects/p/locations/l/sessions/s/streams/str1",
        0,
        {},
    )

    with pytest.warns(
        PendingDeprecationWarning,
        match="google-cloud-bigquery-storage is deprecated",
    ):
        table = read_rows_stream.to_arrow(read_session=read_session)

    assert table.num_rows == batch1.num_rows + batch2.num_rows
    assert table.schema == _TEST_SCHEMA
