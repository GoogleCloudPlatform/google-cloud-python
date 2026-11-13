# Copyright 2016 Google LLC
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


import pytest

from google.cloud.bigtable.data.row import Cell, Row

TIMESTAMP_MICROS = 18738724000  # Make sure millis granularity
ROW_KEY = b"row-key"
FAMILY_NAME = "family"
QUALIFIER = b"qualifier"
VALUE = b"value"
TABLE_NAME = "table_name"
ROWS = [
    Row(
        key=ROW_KEY,
        cells=[
            Cell(
                value=VALUE,
                row_key=ROW_KEY,
                family=FAMILY_NAME,
                qualifier=QUALIFIER,
                timestamp_micros=TIMESTAMP_MICROS,
            )
        ],
    ),
    Row(
        key=ROW_KEY + b"2",
        cells=[
            Cell(
                value=VALUE,
                row_key=ROW_KEY + b"2",
                family=FAMILY_NAME,
                qualifier=QUALIFIER,
                timestamp_micros=TIMESTAMP_MICROS,
            )
        ],
    ),
    Row(
        key=ROW_KEY + b"3",
        cells=[
            Cell(
                value=VALUE,
                row_key=ROW_KEY + b"3",
                family=FAMILY_NAME,
                qualifier=QUALIFIER,
                timestamp_micros=TIMESTAMP_MICROS,
            )
        ],
    ),
]


def _make_cell(*args, **kwargs):
    from google.cloud.bigtable.row_data import Cell

    return Cell(*args, **kwargs)


def _cell_from_pb_test_helper(labels=None):
    import datetime

    from google.cloud._helpers import _EPOCH

    from google.cloud.bigtable.row_data import Cell
    from google.cloud.bigtable_v2.types import data as data_v2_pb2

    timestamp = _EPOCH + datetime.timedelta(microseconds=TIMESTAMP_MICROS)
    value = b"value-bytes"

    if labels is None:
        cell_pb = data_v2_pb2.Cell(value=value, timestamp_micros=TIMESTAMP_MICROS)
        cell_expected = _make_cell(value, TIMESTAMP_MICROS)
    else:
        cell_pb = data_v2_pb2.Cell(
            value=value, timestamp_micros=TIMESTAMP_MICROS, labels=labels
        )
        cell_expected = _make_cell(value, TIMESTAMP_MICROS, labels=labels)

    result = Cell.from_pb(cell_pb)

    assert result == cell_expected
    assert result.timestamp == timestamp


def test_cell_from_pb():
    _cell_from_pb_test_helper()


def test_cell_from_pb_with_labels():
    labels = ["label1", "label2"]
    _cell_from_pb_test_helper(labels)


def test_cell__from_data_client_cell():
    from google.cloud.bigtable.data.row import Cell as DataCell
    from google.cloud.bigtable.row_data import Cell

    data_cell = DataCell(
        value=VALUE,
        row_key=ROW_KEY,
        family=FAMILY_NAME,
        qualifier=QUALIFIER,
        timestamp_micros=TIMESTAMP_MICROS,
    )

    cell = Cell._from_data_client_cell(data_cell)

    assert cell.value == VALUE
    assert cell.timestamp_micros == TIMESTAMP_MICROS
    assert cell.labels == []


def test_cell__from_data_client_cell_with_labels():
    from google.cloud.bigtable.data.row import Cell as DataCell
    from google.cloud.bigtable.row_data import Cell

    data_cell = DataCell(
        value=VALUE,
        row_key=ROW_KEY,
        family=FAMILY_NAME,
        qualifier=QUALIFIER,
        timestamp_micros=TIMESTAMP_MICROS,
        labels=["label1", "label2"],
    )

    cell = Cell._from_data_client_cell(data_cell)

    assert cell.value == VALUE
    assert cell.timestamp_micros == TIMESTAMP_MICROS
    assert cell.labels == ["label1", "label2"]


def test_cell_constructor():
    value = object()
    cell = _make_cell(value, TIMESTAMP_MICROS)
    assert cell.value == value


def test_cell___eq__():
    value = object()
    cell1 = _make_cell(value, TIMESTAMP_MICROS)
    cell2 = _make_cell(value, TIMESTAMP_MICROS)
    assert cell1 == cell2


def test_cell___eq__type_differ():
    cell1 = _make_cell(None, None)
    cell2 = object()
    assert not (cell1 == cell2)


def test_cell___ne__same_value():
    value = object()
    cell1 = _make_cell(value, TIMESTAMP_MICROS)
    cell2 = _make_cell(value, TIMESTAMP_MICROS)
    assert not (cell1 != cell2)


def test_cell___ne__():
    value1 = "value1"
    value2 = "value2"
    cell1 = _make_cell(value1, TIMESTAMP_MICROS)
    cell2 = _make_cell(value2, TIMESTAMP_MICROS)
    assert cell1 != cell2


def _make_partial_row_data(*args, **kwargs):
    from google.cloud.bigtable.row_data import PartialRowData

    return PartialRowData(*args, **kwargs)


def test_partial_row_data_constructor():
    row_key = object()
    partial_row_data = _make_partial_row_data(row_key)
    assert partial_row_data._row_key is row_key
    assert partial_row_data._cells == {}


def test_partial_row_data__from_data_client_row():
    from google.cloud.bigtable.data.row import Cell as DataCell
    from google.cloud.bigtable.data.row import Row as DataRow
    from google.cloud.bigtable.row_data import PartialRowData

    cells = [
        DataCell(
            value=b"1",
            row_key=ROW_KEY,
            family="family1",
            qualifier=b"qual1",
            timestamp_micros=1,
        ),
        DataCell(
            value=b"2",
            row_key=ROW_KEY,
            family="family1",
            qualifier=b"qual1",
            timestamp_micros=2,
        ),
        DataCell(
            value=b"3",
            row_key=ROW_KEY,
            family="family1",
            qualifier=b"qual2",
            timestamp_micros=3,
        ),
        DataCell(
            value=b"4",
            row_key=ROW_KEY,
            family="family2",
            qualifier=b"qual1",
            timestamp_micros=4,
        ),
        DataCell(
            value=b"5",
            row_key=ROW_KEY,
            family="family2",
            qualifier=b"qual2",
            timestamp_micros=5,
        ),
    ]

    row = DataRow(ROW_KEY, cells)
    partial_row_data = PartialRowData._from_data_client_row(row)

    expected_cells = {
        "family1": {
            b"qual1": [
                _make_cell(b"1", 1),
                _make_cell(b"2", 2),
            ],
            b"qual2": [
                _make_cell(b"3", 3),
            ],
        },
        "family2": {
            b"qual1": [
                _make_cell(b"4", 4),
            ],
            b"qual2": [
                _make_cell(b"5", 5),
            ],
        },
    }

    assert partial_row_data._row_key == ROW_KEY
    assert partial_row_data._cells == expected_cells


def test_partial_row_data___eq__():
    row_key = object()
    partial_row_data1 = _make_partial_row_data(row_key)
    partial_row_data2 = _make_partial_row_data(row_key)
    assert partial_row_data1 == partial_row_data2


def test_partial_row_data___eq__type_differ():
    partial_row_data1 = _make_partial_row_data(None)
    partial_row_data2 = object()
    assert not (partial_row_data1 == partial_row_data2)


def test_partial_row_data___ne__same_value():
    row_key = object()
    partial_row_data1 = _make_partial_row_data(row_key)
    partial_row_data2 = _make_partial_row_data(row_key)
    assert not (partial_row_data1 != partial_row_data2)


def test_partial_row_data___ne__():
    row_key1 = object()
    partial_row_data1 = _make_partial_row_data(row_key1)
    row_key2 = object()
    partial_row_data2 = _make_partial_row_data(row_key2)
    assert partial_row_data1 != partial_row_data2


def test_partial_row_data___ne__cells():
    row_key = object()
    partial_row_data1 = _make_partial_row_data(row_key)
    partial_row_data1._cells = object()
    partial_row_data2 = _make_partial_row_data(row_key)
    assert partial_row_data1 != partial_row_data2


def test_partial_row_data_to_dict():
    cell1 = object()
    cell2 = object()
    cell3 = object()

    family_name1 = "name1"
    family_name2 = "name2"
    qual1 = b"col1"
    qual2 = b"col2"
    qual3 = b"col3"

    partial_row_data = _make_partial_row_data(None)
    partial_row_data._cells = {
        family_name1: {qual1: cell1, qual2: cell2},
        family_name2: {qual3: cell3},
    }

    result = partial_row_data.to_dict()
    expected_result = {
        b"name1:col1": cell1,
        b"name1:col2": cell2,
        b"name2:col3": cell3,
    }
    assert result == expected_result


def test_partial_row_data_cell_value():
    family_name = "name1"
    qualifier = b"col1"
    cell = _make_cell_pb(b"value-bytes")

    partial_row_data = _make_partial_row_data(None)
    partial_row_data._cells = {family_name: {qualifier: [cell]}}

    result = partial_row_data.cell_value(family_name, qualifier)
    assert result == cell.value


def test_partial_row_data_cell_value_invalid_index():
    family_name = "name1"
    qualifier = b"col1"
    cell = _make_cell_pb(b"")

    partial_row_data = _make_partial_row_data(None)
    partial_row_data._cells = {family_name: {qualifier: [cell]}}

    with pytest.raises(IndexError):
        partial_row_data.cell_value(family_name, qualifier, index=None)


def test_partial_row_data_cell_value_invalid_column_family_key():
    family_name = "name1"
    qualifier = b"col1"

    partial_row_data = _make_partial_row_data(None)

    with pytest.raises(KeyError):
        partial_row_data.cell_value(family_name, qualifier)


def test_partial_row_data_cell_value_invalid_column_key():
    family_name = "name1"
    qualifier = b"col1"

    partial_row_data = _make_partial_row_data(None)
    partial_row_data._cells = {family_name: {}}

    with pytest.raises(KeyError):
        partial_row_data.cell_value(family_name, qualifier)


def test_partial_row_data_cell_values():
    family_name = "name1"
    qualifier = b"col1"
    cell = _make_cell_pb(b"value-bytes")

    partial_row_data = _make_partial_row_data(None)
    partial_row_data._cells = {family_name: {qualifier: [cell]}}

    values = []
    for value, timestamp_micros in partial_row_data.cell_values(family_name, qualifier):
        values.append(value)

    assert values[0] == cell.value


def test_partial_row_data_cell_values_with_max_count():
    family_name = "name1"
    qualifier = b"col1"
    cell_1 = _make_cell_pb(b"value-bytes-1")
    cell_2 = _make_cell_pb(b"value-bytes-2")

    partial_row_data = _make_partial_row_data(None)
    partial_row_data._cells = {family_name: {qualifier: [cell_1, cell_2]}}

    values = []
    for value, timestamp_micros in partial_row_data.cell_values(
        family_name, qualifier, max_count=1
    ):
        values.append(value)

    assert 1 == len(values)
    assert values[0] == cell_1.value


def test_partial_row_data_cells_property():
    partial_row_data = _make_partial_row_data(None)
    cells = {1: 2}
    partial_row_data._cells = cells
    assert partial_row_data.cells == cells


def test_partial_row_data_row_key_getter():
    row_key = object()
    partial_row_data = _make_partial_row_data(row_key)
    assert partial_row_data.row_key is row_key


def _make_grpc_call_error(exception):
    from grpc import Call, RpcError

    class TestingException(Call, RpcError):
        def __init__(self, exception):
            self.exception = exception

        def code(self):
            return self.exception.grpc_status_code

        def details(self):
            return "Testing"

        def trailing_metadata(self):
            return None

    return TestingException(exception)


def test_partial_cell_data():
    from google.cloud.bigtable.row_data import PartialCellData

    expected_key = b"row-key"
    expected_family_name = b"family-name"
    expected_qualifier = b"qualifier"
    expected_timestamp = 1234
    instance = PartialCellData(
        expected_key, expected_family_name, expected_qualifier, expected_timestamp
    )
    assert instance.row_key == expected_key
    assert instance.family_name == expected_family_name
    assert instance.qualifier == expected_qualifier
    assert instance.timestamp_micros == expected_timestamp
    assert instance.value == b""
    assert instance.labels == ()
    # test updating value
    added_value = b"added-value"
    instance.append_value(added_value)
    assert instance.value == added_value
    instance.append_value(added_value)
    assert instance.value == added_value + added_value


def _make_partial_rows_data(generator):
    from google.cloud.bigtable.row_data import PartialRowsData

    return PartialRowsData._from_generator(generator)


def _partial_rows_data_consume_all(yrd):
    return [row.row_key for row in yrd]


def _make_generator(rows, error=None):
    for row in rows:
        if error:
            raise error
        else:
            yield row


def _assert_generator_closed(generator):
    with pytest.raises(StopIteration):
        next(generator)


def test_partial_rows_data_consume_all():
    generator = _make_generator(ROWS)
    partial_rows_data = _make_partial_rows_data(generator)
    partial_rows_data.consume_all()

    row1 = _make_partial_row_data(ROW_KEY)
    row1._cells[FAMILY_NAME] = {
        QUALIFIER: [_make_cell(value=VALUE, timestamp_micros=TIMESTAMP_MICROS)]
    }
    row2 = _make_partial_row_data(ROW_KEY + b"2")
    row2._cells[FAMILY_NAME] = {
        QUALIFIER: [_make_cell(value=VALUE, timestamp_micros=TIMESTAMP_MICROS)]
    }
    row3 = _make_partial_row_data(ROW_KEY + b"3")
    row3._cells[FAMILY_NAME] = {
        QUALIFIER: [_make_cell(value=VALUE, timestamp_micros=TIMESTAMP_MICROS)]
    }

    assert partial_rows_data.rows == {
        row1.row_key: row1,
        row2.row_key: row2,
        row3.row_key: row3,
    }

    _assert_generator_closed(generator)


def test_partial_rows_data_cancel():
    generator = _make_generator(ROWS)
    partial_rows_data = _make_partial_rows_data(generator)
    row_data = []

    count = 0
    for row in partial_rows_data:
        row_data.append(row)
        count += 1
        if count == 1:
            partial_rows_data.cancel()

    row1 = _make_partial_row_data(ROW_KEY)
    row1._cells[FAMILY_NAME] = {
        QUALIFIER: [_make_cell(value=VALUE, timestamp_micros=TIMESTAMP_MICROS)]
    }
    assert row_data == [row1]

    # We should have closed the generator, so there should be no more
    # elements left in there even though we haven't iterated through all the rows.
    _assert_generator_closed(generator)


def test_partial_rows_data_deadline_exceeded():
    from google.api_core import exceptions

    generator = _make_generator(
        ROWS, error=exceptions.DeadlineExceeded("Operation timed out.")
    )

    partial_rows_data = _make_partial_rows_data(generator)
    with pytest.raises(exceptions.RetryError):
        list(partial_rows_data)

    # An exception should close the generator.
    _assert_generator_closed(generator)


def _make_cell_pb(value):
    from google.cloud.bigtable import row_data

    return row_data.Cell(value, TIMESTAMP_MICROS)


def test_partial_rows_data_legacy_constructor_fallback():
    import warnings

    from google.cloud.bigtable.row_data import PartialRowsData

    read_method = object()
    request = object()

    with warnings.catch_warnings(record=True) as warned:
        warnings.simplefilter("always")
        prd = PartialRowsData(read_method, request)

    assert len(warned) == 1
    assert issubclass(warned[0].category, DeprecationWarning)
    assert "Direct instantiation of `PartialRowsData` is deprecated" in str(
        warned[0].message
    )
    assert list(prd) == []
    assert prd.rows == {}
    # cancel() should work cleanly on the generator fallback
    prd.cancel()


def test_partial_rows_data_keyword_generator():
    import warnings

    from google.cloud.bigtable.row_data import PartialRowsData

    generator = _make_generator([])
    with warnings.catch_warnings(record=True) as warned:
        warnings.simplefilter("always")
        prd = PartialRowsData(generator=generator)

    assert len(warned) == 0
    assert prd._generator is generator
    assert prd.rows == {}


def test_partial_rows_data_deprecated_properties():
    import warnings

    from google.cloud.bigtable.row_data import PartialRowsData

    generator = _make_generator([])
    prd = PartialRowsData._from_generator(generator)

    for attr in [
        "state",
        "last_scanned_row_key",
        "read_method",
        "request",
        "retry",
        "response_iterator",
    ]:
        with warnings.catch_warnings(record=True) as warned:
            warnings.simplefilter("always")
            val = getattr(prd, attr)

        assert val is None
        assert len(warned) == 1
        assert issubclass(warned[0].category, DeprecationWarning)
        assert f"The `{attr}` attribute on `PartialRowsData` is deprecated" in str(
            warned[0].message
        )
