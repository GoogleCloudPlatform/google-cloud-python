# -*- coding: utf-8 -*-
#
# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the 'License');
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an 'AS IS' BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import itertools
from unittest import mock

import pandas
import pandas.testing
import pytest

try:
    import importlib.metadata as metadata
except ImportError:
    import importlib_metadata as metadata

import google.api_core.exceptions

from google.cloud.bigquery_storage import types

from .helpers import SCALAR_BLOCKS, SCALAR_COLUMN_NAMES, SCALAR_COLUMNS

pyarrow = pytest.importorskip("pyarrow")

if pandas is not None:  # pragma: NO COVER
    PANDAS_INSTALLED_VERSION = metadata.version("pandas")
else:
    PANDAS_INSTALLED_VERSION = "0.0.0"


# This dictionary is duplicated in bigquery/google/cloud/bigquery/_pandas_helpers.py
# When modifying it be sure to update it there as well.
BQ_TO_ARROW_TYPES = {
    "int64": pyarrow.int64(),
    "float64": pyarrow.float64(),
    "bool": pyarrow.bool_(),
    "numeric": pyarrow.decimal128(38, 9),
    "string": pyarrow.utf8(),
    "bytes": pyarrow.binary(),
    "date": pyarrow.date32(),  # int32 days since epoch
    "datetime": pyarrow.timestamp("us"),
    "time": pyarrow.time64("us"),
    "timestamp": pyarrow.timestamp("us", tz="UTC"),
}


@pytest.fixture()
def mut():
    from google.cloud.bigquery_storage_v1 import reader

    return reader


@pytest.fixture()
def class_under_test(mut):
    return mut.ReadRowsStream


@pytest.fixture()
def mock_gapic_client():
    from google.cloud.bigquery_storage_v1.services import big_query_read

    return mock.create_autospec(big_query_read.BigQueryReadClient)


def _bq_to_arrow_batch_objects(bq_blocks, arrow_schema):
    arrow_batches = []
    for block in bq_blocks:
        arrays = []
        for name in arrow_schema.names:
            arrays.append(
                pyarrow.array(
                    (row[name] for row in block),
                    type=arrow_schema.field(name).type,
                    size=len(block),
                )
            )
        arrow_batches.append(
            pyarrow.RecordBatch.from_arrays(arrays, schema=arrow_schema)
        )
    return arrow_batches


def _bq_to_arrow_batches(bq_blocks, arrow_schema):
    arrow_batches = []
    first_message = True
    for record_batch in _bq_to_arrow_batch_objects(bq_blocks, arrow_schema):
        response = types.ReadRowsResponse()
        response.arrow_record_batch.serialized_record_batch = (
            record_batch.serialize().to_pybytes()
        )
        if first_message:
            response.arrow_schema = {
                "serialized_schema": arrow_schema.serialize().to_pybytes(),
            }
            first_message = False
        arrow_batches.append(response)
    return arrow_batches


def _bq_to_arrow_schema(bq_columns):
    def bq_col_as_field(column):
        metadata = None
        if column.get("description") is not None:
            metadata = {"description": column.get("description")}
        name = column["name"]
        type_ = BQ_TO_ARROW_TYPES[column["type"]]
        mode = column.get("mode", "nullable").lower()

        return pyarrow.field(name, type_, mode == "nullable", metadata)

    return pyarrow.schema(bq_col_as_field(c) for c in bq_columns)


def _generate_arrow_read_session(arrow_schema):
    return types.ReadSession(
        arrow_schema={"serialized_schema": arrow_schema.serialize().to_pybytes()}
    )


def _pages_w_unavailable(pages):
    for page in pages:
        yield page
    raise google.api_core.exceptions.ServiceUnavailable("test: please reconnect")


def test_pyarrow_rows_raises_import_error(
    mut, class_under_test, mock_gapic_client, monkeypatch
):
    monkeypatch.setattr(mut, "pyarrow", None)
    arrow_schema = _bq_to_arrow_schema(SCALAR_COLUMNS)
    arrow_batches = _bq_to_arrow_batches(SCALAR_BLOCKS, arrow_schema)
    mock_gapic_client.read_rows.return_value = arrow_batches
    reader = class_under_test(mock_gapic_client, "", 0, {})
    rows = iter(reader.rows())

    # Since session isn't passed in, reader doesn't know serialization type
    # until you start iterating.
    with pytest.raises(ImportError):
        next(rows)


def test_to_arrow_no_pyarrow_raises_import_error(
    mut, class_under_test, mock_gapic_client, monkeypatch
):
    monkeypatch.setattr(mut, "pyarrow", None)
    arrow_schema = _bq_to_arrow_schema(SCALAR_COLUMNS)
    arrow_batches = _bq_to_arrow_batches(SCALAR_BLOCKS, arrow_schema)
    mock_gapic_client.read_rows.return_value = arrow_batches
    reader = class_under_test(mock_gapic_client, "", 0, {})

    with pytest.raises(ImportError):
        reader.to_arrow()

    with pytest.raises(ImportError):
        reader.rows().to_arrow()

    with pytest.raises(ImportError):
        next(reader.rows().pages).to_arrow()


def test_to_arrow_w_scalars_arrow(class_under_test, mock_gapic_client):
    arrow_schema = _bq_to_arrow_schema(SCALAR_COLUMNS)
    arrow_batches = _bq_to_arrow_batches(SCALAR_BLOCKS, arrow_schema)
    mock_gapic_client.read_rows.return_value = arrow_batches
    reader = class_under_test(mock_gapic_client, "", 0, {})
    actual_table = reader.to_arrow()
    expected_table = pyarrow.Table.from_batches(
        _bq_to_arrow_batch_objects(SCALAR_BLOCKS, arrow_schema)
    )
    assert actual_table == expected_table


@pytest.mark.skipif(PANDAS_INSTALLED_VERSION[0:2] not in ["0.", "1."], reason="")
def test_to_dataframe_w_scalars_arrow(class_under_test, mock_gapic_client):
    arrow_schema = _bq_to_arrow_schema(SCALAR_COLUMNS)
    arrow_batches = _bq_to_arrow_batches(SCALAR_BLOCKS, arrow_schema)
    mock_gapic_client.read_rows.return_value = arrow_batches
    reader = class_under_test(mock_gapic_client, "", 0, {})
    got = reader.to_dataframe()

    expected = pandas.DataFrame(
        list(itertools.chain.from_iterable(SCALAR_BLOCKS)), columns=SCALAR_COLUMN_NAMES
    )

    pandas.testing.assert_frame_equal(
        got.reset_index(drop=True),  # reset_index to ignore row labels
        expected.reset_index(drop=True),
    )


def test_rows_w_empty_stream_arrow(class_under_test, mock_gapic_client):
    mock_gapic_client.read_rows.return_value = []
    reader = class_under_test(mock_gapic_client, "", 0, {})
    got = reader.rows()
    assert tuple(got) == ()


@pytest.mark.parametrize(
    "use_session",
    [False, True],
    ids=["no_session", "with_session"],
)
def test_to_arrow_empty_stream(class_under_test, mock_gapic_client, use_session):
    """Verify that to_arrow() handles empty streams safely.

    Note: This test focuses specifically on ReadRowsStream.to_arrow(), which
    accepts a read_session argument to provide schema hints for empty streams,
    unlike ReadRowsIterable.to_arrow().
    """
    arrow_schema = _bq_to_arrow_schema(SCALAR_COLUMNS)
    mock_gapic_client.read_rows.return_value = iter([])

    reader = class_under_test(mock_gapic_client, "name", 0, {})

    read_session = _generate_arrow_read_session(arrow_schema) if use_session else None
    expected_schema = arrow_schema if use_session else pyarrow.schema([])

    table = reader.to_arrow(read_session)

    assert len(table) == 0
    assert table.schema == expected_schema


def test_rows_w_scalars_arrow(class_under_test, mock_gapic_client):
    arrow_schema = _bq_to_arrow_schema(SCALAR_COLUMNS)
    arrow_batches = _bq_to_arrow_batches(SCALAR_BLOCKS, arrow_schema)
    mock_gapic_client.read_rows.return_value = arrow_batches
    reader = class_under_test(mock_gapic_client, "", 0, {})
    got = tuple(
        dict((key, value.as_py()) for key, value in row_dict.items())
        for row_dict in reader.rows()
    )

    expected = tuple(itertools.chain.from_iterable(SCALAR_BLOCKS))
    assert got == expected


def test_to_dataframe_w_dtypes_arrow(class_under_test, mock_gapic_client):
    arrow_schema = _bq_to_arrow_schema(
        [
            {"name": "bigfloat", "type": "float64"},
            {"name": "lilfloat", "type": "float64"},
        ]
    )
    blocks = [
        [{"bigfloat": 1.25, "lilfloat": 30.5}, {"bigfloat": 2.5, "lilfloat": 21.125}],
        [{"bigfloat": 3.75, "lilfloat": 11.0}],
    ]
    arrow_batches = _bq_to_arrow_batches(blocks, arrow_schema)
    mock_gapic_client.read_rows.return_value = arrow_batches
    reader = class_under_test(mock_gapic_client, "", 0, {})
    got = reader.to_dataframe(dtypes={"lilfloat": "float16"})

    expected = pandas.DataFrame(
        {
            "bigfloat": [1.25, 2.5, 3.75],
            "lilfloat": pandas.Series([30.5, 21.125, 11.0], dtype="float16"),
        },
        columns=["bigfloat", "lilfloat"],
    )
    pandas.testing.assert_frame_equal(
        got.reset_index(drop=True),  # reset_index to ignore row labels
        expected.reset_index(drop=True),
    )


@pytest.mark.skipif(PANDAS_INSTALLED_VERSION[0:2] not in ["0.", "1."], reason="")
def test_to_dataframe_empty_w_scalars_arrow(class_under_test, mock_gapic_client):
    arrow_schema = _bq_to_arrow_schema(SCALAR_COLUMNS)
    read_session = _generate_arrow_read_session(arrow_schema)
    arrow_batches = _bq_to_arrow_batches([], arrow_schema)
    mock_gapic_client.read_rows.return_value = arrow_batches
    reader = class_under_test(mock_gapic_client, "", 0, {})

    # Read session is needed to get a schema for empty streams.
    got = reader.to_dataframe(read_session)

    expected = pandas.DataFrame([], columns=SCALAR_COLUMN_NAMES)
    expected["int_col"] = expected["int_col"].astype("int64")
    expected["float_col"] = expected["float_col"].astype("float64")
    expected["bool_col"] = expected["bool_col"].astype("bool")
    expected["ts_col"] = (
        expected["ts_col"].astype("datetime64[ns]").dt.tz_localize("UTC")
    )

    pandas.testing.assert_frame_equal(
        got.reset_index(drop=True),  # reset_index to ignore row labels
        expected.reset_index(drop=True),
    )


def test_to_dataframe_empty_w_dtypes_arrow(class_under_test, mock_gapic_client):
    arrow_schema = _bq_to_arrow_schema(
        [
            {"name": "bigfloat", "type": "float64"},
            {"name": "lilfloat", "type": "float64"},
        ]
    )
    read_session = _generate_arrow_read_session(arrow_schema)
    arrow_batches = _bq_to_arrow_batches([], arrow_schema)
    mock_gapic_client.read_rows.return_value = arrow_batches
    reader = class_under_test(mock_gapic_client, "", 0, {})

    # Read session is needed to get a schema for empty streams.
    got = reader.to_dataframe(read_session, dtypes={"lilfloat": "float16"})

    expected = pandas.DataFrame([], columns=["bigfloat", "lilfloat"])
    expected["bigfloat"] = expected["bigfloat"].astype("float64")
    expected["lilfloat"] = expected["lilfloat"].astype("float16")

    pandas.testing.assert_frame_equal(
        got.reset_index(drop=True),  # reset_index to ignore row labels
        expected.reset_index(drop=True),
    )


def test_to_dataframe_by_page_arrow(class_under_test, mock_gapic_client):
    bq_columns = [
        {"name": "int_col", "type": "int64"},
        {"name": "bool_col", "type": "bool"},
    ]
    arrow_schema = _bq_to_arrow_schema(bq_columns)

    bq_block_1 = [
        {"int_col": 123, "bool_col": True},
        {"int_col": 234, "bool_col": False},
    ]
    bq_block_2 = [
        {"int_col": 345, "bool_col": True},
        {"int_col": 456, "bool_col": False},
    ]
    bq_block_3 = [
        {"int_col": 567, "bool_col": True},
        {"int_col": 789, "bool_col": False},
    ]
    bq_block_4 = [{"int_col": 890, "bool_col": True}]
    # Break blocks into two groups to test that iteration continues across
    # reconnection.
    bq_blocks_1 = [bq_block_1, bq_block_2]
    bq_blocks_2 = [bq_block_3, bq_block_4]
    batch_1 = _bq_to_arrow_batches(bq_blocks_1, arrow_schema)
    batch_2 = _bq_to_arrow_batches(bq_blocks_2, arrow_schema)

    mock_gapic_client.read_rows.side_effect = (
        _pages_w_unavailable(batch_1),
        batch_2,
    )

    reader = class_under_test(mock_gapic_client, "", 0, {})
    got = reader.rows()
    pages = iter(got.pages)

    page_1 = next(pages)
    pandas.testing.assert_frame_equal(
        page_1.to_dataframe(
            dtypes={"int_col": "int64", "bool_col": "bool"}
        ).reset_index(drop=True),
        pandas.DataFrame(bq_block_1, columns=["int_col", "bool_col"]).reset_index(
            drop=True
        ),
    )

    page_2 = next(pages)
    pandas.testing.assert_frame_equal(
        page_2.to_dataframe().reset_index(drop=True),
        pandas.DataFrame(bq_block_2, columns=["int_col", "bool_col"]).reset_index(
            drop=True
        ),
    )

    page_3 = next(pages)
    pandas.testing.assert_frame_equal(
        page_3.to_dataframe().reset_index(drop=True),
        pandas.DataFrame(bq_block_3, columns=["int_col", "bool_col"]).reset_index(
            drop=True
        ),
    )

    page_4 = next(pages)
    pandas.testing.assert_frame_equal(
        page_4.to_dataframe().reset_index(drop=True),
        pandas.DataFrame(bq_block_4, columns=["int_col", "bool_col"]).reset_index(
            drop=True
        ),
    )


def test_to_dataframe_mid_stream_failure(mut, class_under_test, mock_gapic_client):
    """
    Verify RuntimeError is raised if stream changes from Arrow to Avro mid-stream.
    This state is not expected in live environment.
    """
    if pandas is None or pyarrow is None:
        pytest.skip("Requires pandas and pyarrow")

    # Mock the first page to be a valid Arrow page.
    arrow_page = mock.Mock(spec=mut.ReadRowsPage)
    arrow_page.to_arrow.return_value = pyarrow.RecordBatch.from_arrays(
        [pyarrow.array([1])], names=["col"]
    )

    # Mock the second page to raise NotImplementedError (simulating Avro/unknown).
    avro_page = mock.Mock(spec=mut.ReadRowsPage)
    avro_page.to_arrow.side_effect = NotImplementedError("Not Arrow")

    # Setup the reader to yield these two pages.
    reader = class_under_test(mock_gapic_client, "name", 0, {})

    with mock.patch.object(
        mut.ReadRowsIterable, "pages", new_callable=mock.PropertyMock
    ) as mock_pages:
        mock_pages.return_value = iter([arrow_page, avro_page])

        it = reader.rows()

        with pytest.raises(RuntimeError, match="Stream format changed mid-stream"):
            it.to_dataframe()


def test_to_arrow_delegates_to_pandas_gbq_when_installed(mut):
    mock_parser = mock.Mock()
    mock_message = mock.Mock()
    page = mut.ReadRowsPage(mock_parser, mock_message)
    expected_batch = pyarrow.RecordBatch.from_arrays(
        [pyarrow.array([100])], names=["id"]
    )

    mock_arrow_module = mock.Mock()
    mock_arrow_module.from_read_rows_response.return_value = expected_batch

    mock_pandas_gbq = mock.Mock()
    mock_pandas_gbq.arrow = mock_arrow_module

    with mock.patch.dict(
        "sys.modules",
        {"pandas_gbq": mock_pandas_gbq, "pandas_gbq.arrow": mock_arrow_module},
    ):
        with pytest.warns(
            PendingDeprecationWarning,
            match="google-cloud-bigquery-storage is deprecated",
        ):
            actual_batch = page.to_arrow()

    assert actual_batch == expected_batch
    mock_arrow_module.from_read_rows_response.assert_called_once_with(
        mock_message, arrow_schema=mock_parser._schema
    )


def test_to_arrow_falls_back_when_pandas_gbq_uninstalled(mut):
    mock_parser = mock.Mock()
    mock_message = mock.Mock()
    expected_batch = pyarrow.RecordBatch.from_arrays(
        [pyarrow.array([200])], names=["id"]
    )
    mock_parser.to_arrow.return_value = expected_batch
    with mock.patch.dict("sys.modules", {"pandas_gbq": None, "pandas_gbq.arrow": None}):
        page = mut.ReadRowsPage(mock_parser, mock_message)
        with pytest.warns(
            PendingDeprecationWarning,
            match="google-cloud-bigquery-storage is deprecated",
        ):
            actual_batch = page.to_arrow()

    assert actual_batch == expected_batch
    mock_parser.to_arrow.assert_called_once_with(mock_message)
