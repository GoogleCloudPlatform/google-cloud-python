# Copyright 2011 Google LLC
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

import operator
from datetime import datetime, timedelta, timezone

import pytest
from grpc import RpcError, StatusCode, UnaryStreamClientInterceptor, intercept_channel

from google.cloud.bigtable import row_filters

COLUMN_FAMILY_ID1 = "col-fam-id1"
COLUMN_FAMILY_ID2 = "col-fam-id2"
COL_NAME1 = b"col-name1"
COL_NAME2 = b"col-name2"
COL_NAME3 = b"col-name3-but-other-fam"
CELL_VAL1 = b"cell-val"
CELL_VAL2 = b"cell-val-newer"
CELL_VAL3 = b"altcol-cell-val"
CELL_VAL4 = b"foo"
CELL_VAL_READ_ROWS_RETRY = b"1" * 512
ROW_KEY = b"row-key"
ROW_KEY_ALT = b"row-key-alt"

CELL_VAL_TRUE = b"true"
CELL_VAL_FALSE = b"false"
INT_COL_NAME = 67890
INT_CELL_VAL = 12345
OVERFLOW_INT_CELL_VAL = 10**100
OVERFLOW_INT_CELL_VAL2 = -(10**100)
FLOAT_CELL_VAL = 1.4
FLOAT_CELL_VAL2 = -1.4

INITIAL_ROW_SPLITS = [b"row_split_1", b"row_split_2", b"row_split_3"]
JOY_EMOJI = "\N{FACE WITH TEARS OF JOY}"

GAP_MARGIN_OF_ERROR = 0.05

PASS_ALL_FILTER = row_filters.PassAllFilter(True)
BLOCK_ALL_FILTER = row_filters.BlockAllFilter(True)

READ_ROWS_METHOD_NAME = "/google.bigtable.v2.Bigtable/ReadRows"


class ReadRowsErrorInjector(UnaryStreamClientInterceptor):
    """An error injector that can be configured to raise errors for the ReadRows method.

    The error injector is configured to inject errors off the self.errors_to_inject queue.
    Exceptions can be configured to arise either during stream initialization or in the middle
    of a stream. If no errors are in the error injection queue, the ReadRows RPC call will behave
    normally.
    """

    def __init__(self):
        self.errors_to_inject = []

    def clear(self):
        self.errors_to_inject.clear()

    @staticmethod
    def make_exception(
        status_code, message=None, fail_mid_stream=False, successes_before_fail=0
    ):
        # successes_before_fail allows us to test injecting failures mid-iterator iteration.
        exc = RpcError(status_code)
        exc.code = lambda: status_code

        _, status_message = status_code.value
        exc.details = lambda: message if message else status_message

        exc.initial_metadata = lambda: []
        exc.trailing_metadata = lambda: []
        exc.fail_mid_stream = fail_mid_stream
        exc.successes_before_fail = successes_before_fail

        def _result():
            raise exc

        exc.result = _result
        return exc

    def intercept_unary_stream(self, continuation, client_call_details, request):
        if (
            client_call_details.method == READ_ROWS_METHOD_NAME
            and self.errors_to_inject
        ):
            error = self.errors_to_inject.pop(0)
            if not error.fail_mid_stream:
                raise error

            response = continuation(client_call_details, request)
            if error.fail_mid_stream:

                class CallWrapper:
                    def __init__(self, call, exc_to_raise):
                        self._call = call
                        self._exc = exc_to_raise
                        self._successes_remaining = exc_to_raise.successes_before_fail
                        self._raised = False

                    def __iter__(self):
                        return self

                    def __next__(self):
                        if not self._raised and self._successes_remaining == 0:
                            self._raised = True
                            if self._exc:
                                raise self._exc

                        else:
                            if self._successes_remaining > 0:
                                self._successes_remaining -= 1
                            return self._call.__next__()

                    def __getattr__(self, name):
                        return getattr(self._call, name)

                return CallWrapper(response, error)
        else:
            return continuation(client_call_details, request)


@pytest.fixture(scope="module")
def data_table_id():
    return "test-data-api"


@pytest.fixture(scope="module")
def data_table(data_instance_populated, data_table_id):
    table = data_instance_populated.table(data_table_id)
    table.create(initial_split_keys=INITIAL_ROW_SPLITS)
    table.column_family(COLUMN_FAMILY_ID1).create()
    table.column_family(COLUMN_FAMILY_ID2).create()

    yield table

    table.delete()


@pytest.fixture(scope="function")
def rows_to_delete():
    rows_to_delete = []

    yield rows_to_delete

    for row in rows_to_delete:
        row.clear()
        row.delete()
        row.commit()


@pytest.fixture(scope="module")
def data_table_read_rows_retry_tests_setup(data_table):
    row_keys = [f"row_key_{i}".encode() for i in range(0, 32)]
    columns = [f"col_{i}".encode() for i in range(0, 32)]

    # Set up the error injector here
    data_client = data_table._instance._client.table_data_client
    error_injector = ReadRowsErrorInjector()
    old_logged_channel = data_client.transport._logged_channel
    data_client.transport._logged_channel = intercept_channel(
        old_logged_channel, error_injector
    )
    data_table.error_injector = error_injector
    data_client.transport._stubs = {}
    data_client.transport._prep_wrapped_messages(None)

    # Need to add this here as a class level teardown since rows_to_delete
    # is a function level fixture.
    rows_to_delete = []

    try:
        _populate_table(
            data_table, rows_to_delete, row_keys, columns, CELL_VAL_READ_ROWS_RETRY
        )
        yield data_table
    finally:
        del data_table.error_injector
        data_client.transport._logged_channel = old_logged_channel
        data_client.transport._stubs = {}
        data_client.transport._prep_wrapped_messages(None)

        for row in rows_to_delete:
            row.clear()
            row.delete()
            row.commit()


@pytest.fixture(scope="function")
def data_table_read_rows_retry_tests(data_table_read_rows_retry_tests_setup):
    yield data_table_read_rows_retry_tests_setup

    data_table_read_rows_retry_tests_setup.error_injector.clear()


def test_table_read_rows_filter_millis(data_table):
    from google.cloud.bigtable import row_filters

    end = datetime.now()
    start = end - timedelta(minutes=60)
    timestamp_range = row_filters.TimestampRange(start=start, end=end)
    timefilter = row_filters.TimestampRangeFilter(timestamp_range)
    row_data = data_table.read_rows(filter_=timefilter)
    row_data.consume_all()


def test_table_direct_row_commit(data_table, rows_to_delete):
    from google.rpc import code_pb2

    row = data_table.direct_row(ROW_KEY)

    # Test set cell
    row.set_cell(COLUMN_FAMILY_ID1, COL_NAME1, CELL_VAL1)
    row.set_cell(COLUMN_FAMILY_ID1, COL_NAME2, CELL_VAL1)
    status = row.commit()
    rows_to_delete.append(row)
    assert status.code == code_pb2.Code.OK
    row_data = data_table.read_row(ROW_KEY)
    assert row_data.cells[COLUMN_FAMILY_ID1][COL_NAME1][0].value == CELL_VAL1
    assert row_data.cells[COLUMN_FAMILY_ID1][COL_NAME2][0].value == CELL_VAL1

    # Test delete cell
    row.delete_cell(COLUMN_FAMILY_ID1, COL_NAME1)
    status = row.commit()
    assert status.code == code_pb2.Code.OK
    row_data = data_table.read_row(ROW_KEY)
    assert COL_NAME1 not in row_data.cells[COLUMN_FAMILY_ID1]
    assert row_data.cells[COLUMN_FAMILY_ID1][COL_NAME2][0].value == CELL_VAL1

    # Test delete row
    row.delete()
    status = row.commit()
    assert status.code == code_pb2.Code.OK
    row_data = data_table.read_row(ROW_KEY)
    assert row_data is None


def test_table_mutate_rows(data_table, rows_to_delete):
    row1 = data_table.direct_row(ROW_KEY)
    row1.set_cell(COLUMN_FAMILY_ID1, COL_NAME1, CELL_VAL1)
    row1.commit()
    rows_to_delete.append(row1)

    row2 = data_table.direct_row(ROW_KEY_ALT)
    row2.set_cell(COLUMN_FAMILY_ID1, COL_NAME1, CELL_VAL2)
    row2.commit()
    rows_to_delete.append(row2)

    # Change the contents
    row1.set_cell(COLUMN_FAMILY_ID1, COL_NAME1, CELL_VAL3)
    row2.set_cell(COLUMN_FAMILY_ID1, COL_NAME1, CELL_VAL4)
    rows = [row1, row2]

    statuses = data_table.mutate_rows(rows)
    assert len(statuses) == len(rows)
    for status in statuses:
        assert status.code == 0

    # Check the contents
    row1_data = data_table.read_row(ROW_KEY)
    assert row1_data.cells[COLUMN_FAMILY_ID1][COL_NAME1][0].value == CELL_VAL3

    row2_data = data_table.read_row(ROW_KEY_ALT)
    assert row2_data.cells[COLUMN_FAMILY_ID1][COL_NAME1][0].value == CELL_VAL4


def test_table_mutate_rows_retries_timeout(data_table, rows_to_delete):
    import mock
    from google.rpc.code_pb2 import Code
    from google.rpc.status_pb2 import Status

    from google.cloud.bigtable.table import DEFAULT_RETRY
    from google.cloud.bigtable_v2 import MutateRowsResponse

    # Simulate a server error on row 2, and a normal response on row 1, followed by a bunch of error
    # responses on row 2
    initial_error_response = [
        MutateRowsResponse(
            entries=[
                MutateRowsResponse.Entry(),
                MutateRowsResponse.Entry(
                    index=1,
                    status=Status(
                        code=Code.INTERNAL,
                        message="Test error",
                    ),
                ),
            ]
        )
    ]

    followup_error_response = [
        MutateRowsResponse(
            entries=[
                MutateRowsResponse.Entry(
                    status=Status(
                        code=Code.INTERNAL,
                        message="Test error",
                    )
                )
            ]
        )
    ]

    final_success_response = [MutateRowsResponse(entries=[MutateRowsResponse.Entry()])]

    # Explicit timestamp ensures mutations are idempotent and eligible for retry.
    timestamp = datetime(2023, 1, 1, tzinfo=timezone.utc)

    with mock.patch.object(
        data_table._instance._client.table_data_client, "mutate_rows"
    ) as mutate_mock:
        mutate_mock.side_effect = [
            initial_error_response,
            followup_error_response,
            followup_error_response,
            final_success_response,
        ]

        row = data_table.direct_row(ROW_KEY)
        rows_to_delete.append(row)
        row.set_cell(COLUMN_FAMILY_ID1, COL_NAME1, CELL_VAL1, timestamp=timestamp)

        row_2 = data_table.direct_row(ROW_KEY_ALT)
        rows_to_delete.append(row_2)
        row_2.set_cell(COLUMN_FAMILY_ID1, COL_NAME1, CELL_VAL1, timestamp=timestamp)

        statuses = data_table.mutate_rows([row, row_2])
        assert statuses[0].code == Code.OK
        assert statuses[1].code == Code.OK

    # Simulate only server failures for row 2.
    with mock.patch.object(
        data_table._instance._client.table_data_client, "mutate_rows"
    ) as mutate_mock:
        mutate_mock.side_effect = [initial_error_response] + [
            followup_error_response
        ] * 1000000

        row = data_table.direct_row(ROW_KEY)
        rows_to_delete.append(row)
        row.set_cell(COLUMN_FAMILY_ID1, COL_NAME1, CELL_VAL1, timestamp=timestamp)

        row_2 = data_table.direct_row(ROW_KEY_ALT)
        rows_to_delete.append(row_2)
        row_2.set_cell(COLUMN_FAMILY_ID1, COL_NAME1, CELL_VAL1, timestamp=timestamp)

        statuses = data_table.mutate_rows([row, row_2])
        assert statuses[0].code == Code.OK
        assert statuses[1].code == Code.DEADLINE_EXCEEDED

    # Retries with deadline 0 should do nothing.
    with mock.patch.object(
        data_table._instance._client.table_data_client, "mutate_rows"
    ) as mutate_mock:
        mutate_mock.side_effect = [
            initial_error_response,
            followup_error_response,
            followup_error_response,
            final_success_response,
        ]

        row = data_table.direct_row(ROW_KEY)
        rows_to_delete.append(row)
        row.set_cell(COLUMN_FAMILY_ID1, COL_NAME1, CELL_VAL1, timestamp=timestamp)

        row_2 = data_table.direct_row(ROW_KEY_ALT)
        rows_to_delete.append(row_2)
        row_2.set_cell(COLUMN_FAMILY_ID1, COL_NAME1, CELL_VAL1, timestamp=timestamp)

        do_nothing_retry = DEFAULT_RETRY.with_deadline(0.0)

        statuses = data_table.mutate_rows([row, row_2], retry=do_nothing_retry)
        assert statuses[0].code == Code.OK
        assert statuses[1].code == Code.INTERNAL
        mutate_mock.assert_called_once()


def _populate_table(
    data_table, rows_to_delete, row_keys, columns=[COL_NAME1], cell_value=CELL_VAL1
):
    for row_key in row_keys:
        row = data_table.direct_row(row_key)
        for column in columns:
            row.set_cell(COLUMN_FAMILY_ID1, column, cell_value)
        row.commit()
        rows_to_delete.append(row)


def test_table_truncate(data_table, rows_to_delete):
    row_keys = [
        b"row_key_1",
        b"row_key_2",
        b"row_key_3",
        b"row_key_4",
        b"row_key_5",
        b"row_key_pr_1",
        b"row_key_pr_2",
        b"row_key_pr_3",
        b"row_key_pr_4",
        b"row_key_pr_5",
    ]
    _populate_table(data_table, rows_to_delete, row_keys)

    data_table.truncate(timeout=200)

    assert list(data_table.read_rows()) == []


def test_table_drop_by_prefix(data_table, rows_to_delete):
    row_keys = [
        b"row_key_1",
        b"row_key_2",
        b"row_key_3",
        b"row_key_4",
        b"row_key_5",
        b"row_key_pr_1",
        b"row_key_pr_2",
        b"row_key_pr_3",
        b"row_key_pr_4",
        b"row_key_pr_5",
    ]
    _populate_table(data_table, rows_to_delete, row_keys)

    data_table.drop_by_prefix(row_key_prefix="row_key_pr", timeout=200)

    remaining_row_keys = [
        row_key for row_key in row_keys if not row_key.startswith(b"row_key_pr")
    ]
    expected_rows_count = len(remaining_row_keys)
    found_rows_count = 0

    for row in data_table.read_rows():
        if row.row_key in row_keys:
            found_rows_count += 1

    assert expected_rows_count == found_rows_count


def test_table_mutate_rows_integers(data_table, rows_to_delete):
    row = data_table.direct_row(ROW_KEY)
    row.set_cell(COLUMN_FAMILY_ID1, COL_NAME1, CELL_VAL1)
    row.commit()
    rows_to_delete.append(row)

    # Change the contents to an integer
    row.set_cell(COLUMN_FAMILY_ID1, COL_NAME1, INT_CELL_VAL)
    statuses = data_table.mutate_rows([row])
    assert len(statuses) == 1
    for status in statuses:
        assert status.code == 0

    # Check the contents
    row1_data = data_table.read_row(ROW_KEY)
    assert (
        int.from_bytes(
            row1_data.cells[COLUMN_FAMILY_ID1][COL_NAME1][0].value, byteorder="big"
        )
        == INT_CELL_VAL
    )


def test_table_mutate_rows_input_errors(data_table, rows_to_delete):
    from google.cloud.bigtable.table import _MAX_BULK_MUTATIONS

    row = data_table.direct_row(ROW_KEY)
    rows_to_delete.append(row)

    # Mutate row with 0 mutations gives a ValueError from the client library.
    with pytest.raises(ValueError):
        data_table.mutate_rows([row])

    row.clear()

    # Mutate row with >100k mutations gives a ValueError from the
    # client library.
    for _ in range(0, _MAX_BULK_MUTATIONS + 1):
        row.set_cell(COLUMN_FAMILY_ID1, COL_NAME1, CELL_VAL1)

    with pytest.raises(ValueError):
        data_table.mutate_rows([row])


def test_table_read_rows_w_row_set(data_table, rows_to_delete):
    from google.cloud.bigtable.row_set import RowRange, RowSet

    row_keys = [
        b"row_key_1",
        b"row_key_2",
        b"row_key_3",
        b"row_key_4",
        b"row_key_5",
        b"row_key_6",
        b"row_key_7",
        b"row_key_8",
        b"row_key_9",
    ]
    _populate_table(data_table, rows_to_delete, row_keys)

    row_range = RowRange(start_key=b"row_key_3", end_key=b"row_key_7")
    row_set = RowSet()
    row_set.add_row_range(row_range)
    row_set.add_row_key(b"row_key_1")

    found_rows = data_table.read_rows(row_set=row_set)

    found_row_keys = [row.row_key for row in found_rows]
    expected_row_keys = [
        row_key for row_key in row_keys[:6] if not row_key.endswith(b"_2")
    ]
    assert found_row_keys == expected_row_keys


def test_rowset_add_row_range_w_pfx(data_table, rows_to_delete):
    from google.cloud.bigtable.row_set import RowSet

    row_keys = [
        b"row_key_1",
        b"row_key_2",
        b"row_key_3",
        b"row_key_4",
        b"sample_row_key_1",
        b"sample_row_key_2",
    ]
    _populate_table(data_table, rows_to_delete, row_keys)

    row_set = RowSet()
    row_set.add_row_range_with_prefix("row")

    expected_row_keys = [row_key for row_key in row_keys if row_key.startswith(b"row")]
    found_rows = data_table.read_rows(row_set=row_set)
    found_row_keys = [row.row_key for row in found_rows]
    assert found_row_keys == expected_row_keys


def test_table_read_row_large_cell(data_table, rows_to_delete, skip_on_emulator):
    # Maximum gRPC received message size for emulator is 4194304 bytes.
    row = data_table.direct_row(ROW_KEY)
    rows_to_delete.append(row)

    number_of_bytes = 10 * 1024 * 1024
    data = b"1" * number_of_bytes  # 10MB of 1's.
    row.set_cell(COLUMN_FAMILY_ID1, COL_NAME1, data)
    row.commit()

    # Read back the contents of the row.
    row_data = data_table.read_row(ROW_KEY)
    assert row_data.row_key == ROW_KEY

    cell = row_data.cells[COLUMN_FAMILY_ID1]
    column = cell[COL_NAME1]
    assert len(column) == 1
    assert column[0].value == data


def _write_to_row(row1, row2, row3, row4):
    from google.cloud._helpers import (
        _datetime_from_microseconds,
        _microseconds_from_datetime,
    )

    from google.cloud.bigtable.row_data import Cell

    timestamp1 = datetime.now(timezone.utc)
    timestamp1_micros = _microseconds_from_datetime(timestamp1)
    # Truncate to millisecond granularity.
    timestamp1_micros -= timestamp1_micros % 1000
    timestamp1 = _datetime_from_microseconds(timestamp1_micros)
    # 1000 microseconds is a millisecond
    timestamp2 = timestamp1 + timedelta(microseconds=1000)
    timestamp2_micros = _microseconds_from_datetime(timestamp2)
    timestamp3 = timestamp1 + timedelta(microseconds=2000)
    timestamp3_micros = _microseconds_from_datetime(timestamp3)
    timestamp4 = timestamp1 + timedelta(microseconds=3000)
    timestamp4_micros = _microseconds_from_datetime(timestamp4)

    if row1 is not None:
        row1.set_cell(COLUMN_FAMILY_ID1, COL_NAME1, CELL_VAL1, timestamp=timestamp1)
    if row2 is not None:
        row2.set_cell(COLUMN_FAMILY_ID1, COL_NAME1, CELL_VAL2, timestamp=timestamp2)
    if row3 is not None:
        row3.set_cell(COLUMN_FAMILY_ID1, COL_NAME2, CELL_VAL3, timestamp=timestamp3)
    if row4 is not None:
        row4.set_cell(COLUMN_FAMILY_ID2, COL_NAME3, CELL_VAL4, timestamp=timestamp4)

    # Create the cells we will check.
    cell1 = Cell(CELL_VAL1, timestamp1_micros)
    cell2 = Cell(CELL_VAL2, timestamp2_micros)
    cell3 = Cell(CELL_VAL3, timestamp3_micros)
    cell4 = Cell(CELL_VAL4, timestamp4_micros)

    return cell1, cell2, cell3, cell4


def test_table_read_row(data_table, rows_to_delete):
    row = data_table.direct_row(ROW_KEY)
    rows_to_delete.append(row)
    cell1, cell2, cell3, cell4 = _write_to_row(row, row, row, row)
    row.commit()

    partial_row_data = data_table.read_row(ROW_KEY)

    assert partial_row_data.row_key == ROW_KEY

    # Check the cells match.
    ts_attr = operator.attrgetter("timestamp")
    expected_row_contents = {
        COLUMN_FAMILY_ID1: {
            COL_NAME1: sorted([cell1, cell2], key=ts_attr, reverse=True),
            COL_NAME2: [cell3],
        },
        COLUMN_FAMILY_ID2: {COL_NAME3: [cell4]},
    }
    assert partial_row_data.cells == expected_row_contents


def test_table_read_rows(data_table, rows_to_delete):
    from google.cloud.bigtable.row_data import PartialRowData

    row = data_table.direct_row(ROW_KEY)
    rows_to_delete.append(row)
    row_alt = data_table.direct_row(ROW_KEY_ALT)
    rows_to_delete.append(row_alt)

    cell1, cell2, cell3, cell4 = _write_to_row(row, row_alt, row, row_alt)
    row.commit()
    row_alt.commit()

    rows_data = data_table.read_rows()
    assert rows_data.rows == {}
    rows_data.consume_all()

    # NOTE: We should refrain from editing protected data on instances.
    #       Instead we should make the values public or provide factories
    #       for constructing objects with them.
    row_data = PartialRowData(ROW_KEY)
    row_data._chunks_encountered = True
    row_data._committed = True
    row_data._cells = {COLUMN_FAMILY_ID1: {COL_NAME1: [cell1], COL_NAME2: [cell3]}}

    row_alt_data = PartialRowData(ROW_KEY_ALT)
    row_alt_data._chunks_encountered = True
    row_alt_data._committed = True
    row_alt_data._cells = {
        COLUMN_FAMILY_ID1: {COL_NAME1: [cell2]},
        COLUMN_FAMILY_ID2: {COL_NAME3: [cell4]},
    }

    expected_rows = {ROW_KEY: row_data, ROW_KEY_ALT: row_alt_data}
    assert rows_data.rows == expected_rows


def test_read_with_label_applied(data_table, rows_to_delete, skip_on_emulator):
    from google.cloud.bigtable.row_filters import (
        ApplyLabelFilter,
        ColumnQualifierRegexFilter,
        RowFilterChain,
        RowFilterUnion,
    )

    row = data_table.direct_row(ROW_KEY)
    rows_to_delete.append(row)

    cell1, _, cell3, _ = _write_to_row(row, None, row, None)
    row.commit()

    # Combine a label with column 1.
    label1 = "label-red"
    label1_filter = ApplyLabelFilter(label1)
    col1_filter = ColumnQualifierRegexFilter(COL_NAME1)
    chain1 = RowFilterChain(filters=[col1_filter, label1_filter])

    # Combine a label with column 2.
    label2 = "label-blue"
    label2_filter = ApplyLabelFilter(label2)
    col2_filter = ColumnQualifierRegexFilter(COL_NAME2)
    chain2 = RowFilterChain(filters=[col2_filter, label2_filter])

    # Bring our two labeled columns together.
    row_filter = RowFilterUnion(filters=[chain1, chain2])
    partial_row_data = data_table.read_row(ROW_KEY, filter_=row_filter)
    assert partial_row_data.row_key == ROW_KEY

    cells_returned = partial_row_data.cells
    col_fam1 = cells_returned.pop(COLUMN_FAMILY_ID1)
    # Make sure COLUMN_FAMILY_ID1 was the only key.
    assert len(cells_returned) == 0

    (cell1_new,) = col_fam1.pop(COL_NAME1)
    (cell3_new,) = col_fam1.pop(COL_NAME2)
    # Make sure COL_NAME1 and COL_NAME2 were the only keys.
    assert len(col_fam1) == 0

    # Check that cell1 has matching values and gained a label.
    assert cell1_new.value == cell1.value
    assert cell1_new.timestamp == cell1.timestamp
    assert cell1.labels == []
    assert cell1_new.labels == [label1]

    # Check that cell3 has matching values and gained a label.
    assert cell3_new.value == cell3.value
    assert cell3_new.timestamp == cell3.timestamp
    assert cell3.labels == []
    assert cell3_new.labels == [label2]


def _assert_data_table_read_rows_retry_correct(rows_data):
    for row_num in range(0, 32):
        row = rows_data.rows[f"row_key_{row_num}".encode()]
        for col_num in range(0, 32):
            assert (
                row.cells[COLUMN_FAMILY_ID1][f"col_{col_num}".encode()][0].value
                == CELL_VAL_READ_ROWS_RETRY
            )


def test_table_read_rows_multiple_reads(
    data_table_read_rows_retry_tests,
):
    from types import SimpleNamespace

    rows_data = data_table_read_rows_retry_tests.read_rows()
    first_iteration = SimpleNamespace()
    first_iteration.rows = {}

    second_iteration = SimpleNamespace()
    second_iteration.rows = {}
    for item in rows_data:
        first_iteration.rows[item.row_key] = item

    for item in rows_data:
        second_iteration.rows[item.row_key] = item

    _assert_data_table_read_rows_retry_correct(first_iteration)
    assert second_iteration.rows == {}


def test_table_read_rows_retry_unretriable_error_establishing_stream(
    data_table_read_rows_retry_tests,
):
    from google.api_core import exceptions

    error_injector = data_table_read_rows_retry_tests.error_injector
    error_injector.errors_to_inject = [
        error_injector.make_exception(StatusCode.DATA_LOSS, fail_mid_stream=False)
    ]

    rows_data = data_table_read_rows_retry_tests.read_rows()
    with pytest.raises(exceptions.DataLoss):
        rows_data.consume_all()


def test_table_read_rows_retry_retriable_error_establishing_stream(
    data_table_read_rows_retry_tests,
):
    error_injector = data_table_read_rows_retry_tests.error_injector
    error_injector.errors_to_inject = [
        error_injector.make_exception(
            StatusCode.DEADLINE_EXCEEDED, fail_mid_stream=False
        )
    ] * 3

    rows_data = data_table_read_rows_retry_tests.read_rows()
    rows_data.consume_all()

    _assert_data_table_read_rows_retry_correct(rows_data)


def test_table_read_rows_retry_unretriable_error_mid_stream(
    data_table_read_rows_retry_tests,
):
    from google.api_core import exceptions

    error_injector = data_table_read_rows_retry_tests.error_injector
    error_injector.errors_to_inject = [
        error_injector.make_exception(
            StatusCode.DATA_LOSS, fail_mid_stream=True, successes_before_fail=5
        )
    ]

    rows_data = data_table_read_rows_retry_tests.read_rows()
    with pytest.raises(exceptions.DataLoss):
        rows_data.consume_all()


def test_table_read_rows_retry_retriable_errors_mid_stream(
    data_table_read_rows_retry_tests,
):
    error_injector = data_table_read_rows_retry_tests.error_injector
    error_injector.errors_to_inject = [
        error_injector.make_exception(
            StatusCode.UNAVAILABLE, fail_mid_stream=True, successes_before_fail=4
        ),
        error_injector.make_exception(
            StatusCode.UNAVAILABLE, fail_mid_stream=True, successes_before_fail=0
        ),
        error_injector.make_exception(
            StatusCode.UNAVAILABLE, fail_mid_stream=True, successes_before_fail=0
        ),
    ]

    rows_data = data_table_read_rows_retry_tests.read_rows()
    rows_data.consume_all()

    _assert_data_table_read_rows_retry_correct(rows_data)


def test_table_read_rows_retry_retriable_internal_errors_mid_stream(
    data_table_read_rows_retry_tests,
):
    from google.cloud.bigtable.data._helpers import _RETRYABLE_INTERNAL_ERROR_MESSAGES

    error_injector = data_table_read_rows_retry_tests.error_injector
    error_injector.errors_to_inject = [
        error_injector.make_exception(
            StatusCode.INTERNAL,
            message=_RETRYABLE_INTERNAL_ERROR_MESSAGES[0],
            fail_mid_stream=True,
            successes_before_fail=2,
        ),
        error_injector.make_exception(
            StatusCode.INTERNAL,
            message=_RETRYABLE_INTERNAL_ERROR_MESSAGES[1],
            fail_mid_stream=True,
            successes_before_fail=1,
        ),
        error_injector.make_exception(
            StatusCode.INTERNAL,
            message=_RETRYABLE_INTERNAL_ERROR_MESSAGES[2],
            fail_mid_stream=True,
            successes_before_fail=0,
        ),
    ]

    rows_data = data_table_read_rows_retry_tests.read_rows()
    rows_data.consume_all()

    _assert_data_table_read_rows_retry_correct(rows_data)


def test_table_read_rows_retry_unretriable_internal_errors_mid_stream(
    data_table_read_rows_retry_tests,
):
    from google.api_core import exceptions

    error_injector = data_table_read_rows_retry_tests.error_injector
    error_injector.errors_to_inject = [
        error_injector.make_exception(
            StatusCode.INTERNAL,
            message="Don't retry this at home!",
            fail_mid_stream=True,
            successes_before_fail=2,
        ),
    ]

    rows_data = data_table_read_rows_retry_tests.read_rows()
    with pytest.raises(exceptions.InternalServerError):
        rows_data.consume_all()


def test_table_read_rows_retry_retriable_error_mid_stream_unretriable_error_reestablishing_stream(
    data_table_read_rows_retry_tests,
):
    # Simulate a connection failure mid-stream into an unretriable error when trying to reconnect.
    from google.api_core import exceptions

    error_injector = data_table_read_rows_retry_tests.error_injector
    error_injector.errors_to_inject = [
        error_injector.make_exception(
            StatusCode.UNAVAILABLE, fail_mid_stream=True, successes_before_fail=5
        ),
        error_injector.make_exception(StatusCode.DATA_LOSS, fail_mid_stream=False),
    ]

    rows_data = data_table_read_rows_retry_tests.read_rows()

    with pytest.raises(exceptions.DataLoss):
        rows_data.consume_all()


def test_table_read_rows_retry_retriable_error_mid_stream_retriable_error_reestablishing_stream(
    data_table_read_rows_retry_tests,
):
    # Simulate a connection failure mid-stream into retriable errors when trying to reconnect.
    error_injector = data_table_read_rows_retry_tests.error_injector
    error_injector.errors_to_inject = [
        error_injector.make_exception(
            StatusCode.UNAVAILABLE, fail_mid_stream=True, successes_before_fail=5
        ),
        error_injector.make_exception(StatusCode.UNAVAILABLE, fail_mid_stream=False),
        error_injector.make_exception(StatusCode.UNAVAILABLE, fail_mid_stream=False),
        error_injector.make_exception(StatusCode.UNAVAILABLE, fail_mid_stream=False),
    ]

    rows_data = data_table_read_rows_retry_tests.read_rows()
    rows_data.consume_all()

    _assert_data_table_read_rows_retry_correct(rows_data)


def test_table_read_rows_retry_timeout_mid_stream(
    data_table_read_rows_retry_tests,
):
    # Simulate a read timeout mid stream.

    from google.api_core import exceptions

    from google.cloud.bigtable.data._helpers import _RETRYABLE_INTERNAL_ERROR_MESSAGES
    from google.cloud.bigtable.row_data import (
        DEFAULT_RETRY_READ_ROWS,
    )

    error_injector = data_table_read_rows_retry_tests.error_injector
    error_injector.errors_to_inject = [
        error_injector.make_exception(
            StatusCode.INTERNAL,
            message=_RETRYABLE_INTERNAL_ERROR_MESSAGES[0],
            fail_mid_stream=True,
            successes_before_fail=5,
        ),
    ] + [
        error_injector.make_exception(
            StatusCode.INTERNAL,
            message=_RETRYABLE_INTERNAL_ERROR_MESSAGES[0],
            fail_mid_stream=True,
            successes_before_fail=0,
        ),
    ] * 20

    # Shorten the deadline so the timeout test is shorter.
    data_table_read_rows_retry_tests._table_impl.default_read_rows_operation_timeout = (
        10.0
    )
    rows_data = data_table_read_rows_retry_tests.read_rows(
        retry=DEFAULT_RETRY_READ_ROWS.with_deadline(10.0)
    )
    with pytest.raises(exceptions.RetryError):
        rows_data.consume_all()


def test_table_read_rows_retry_timeout_establishing_stream(
    data_table_read_rows_retry_tests,
):
    # Simulate a read timeout when creating the stream.

    from google.api_core import exceptions

    from google.cloud.bigtable.row_data import DEFAULT_RETRY_READ_ROWS

    error_injector = data_table_read_rows_retry_tests.error_injector
    error_injector.errors_to_inject = [
        error_injector.make_exception(
            StatusCode.DEADLINE_EXCEEDED, fail_mid_stream=False
        ),
    ] + [
        error_injector.make_exception(
            StatusCode.DEADLINE_EXCEEDED, fail_mid_stream=False
        ),
    ] * 20

    # Shorten the deadline so the timeout test is shorter.
    data_table_read_rows_retry_tests._table_impl.default_read_rows_operation_timeout = (
        10.0
    )
    rows_data = data_table_read_rows_retry_tests.read_rows(
        retry=DEFAULT_RETRY_READ_ROWS.with_deadline(10.0)
    )
    with pytest.raises(exceptions.RetryError):
        rows_data.consume_all()


def test_table_check_and_mutate_rows(data_table, rows_to_delete):
    true_mutation_row_key = b"true_row"
    false_mutation_row_key = b"false_row"

    columns = [
        b"col_1",
        b"col_2",
        b"col_3",
        b"col_4",
        b"col_pr_1",
        b"col_pr_2",
    ]
    _populate_table(
        data_table,
        rows_to_delete,
        [true_mutation_row_key, false_mutation_row_key],
        columns=columns,
    )
    true_row = data_table.conditional_row(true_mutation_row_key, PASS_ALL_FILTER)
    for column in columns:
        true_row.set_cell(COLUMN_FAMILY_ID1, column, CELL_VAL_TRUE, state=True)
        true_row.set_cell(COLUMN_FAMILY_ID1, column, CELL_VAL_FALSE, state=False)
    matched = true_row.commit()
    assert matched

    false_row = data_table.conditional_row(false_mutation_row_key, BLOCK_ALL_FILTER)
    for column in columns:
        false_row.set_cell(COLUMN_FAMILY_ID1, column, CELL_VAL_TRUE, state=True)
        false_row.delete_cell(COLUMN_FAMILY_ID1, column, state=False)
    matched = false_row.commit()
    assert not matched

    row1_data = data_table.read_row(true_mutation_row_key)
    for column in columns:
        assert row1_data.cells[COLUMN_FAMILY_ID1][column][0].value == CELL_VAL_TRUE

    row2_data = data_table.read_row(false_mutation_row_key)
    assert row2_data is None  # all cells should be deleted


def test_table_append_row(data_table, rows_to_delete):
    row = data_table.append_row(ROW_KEY)
    rows_to_delete.append(data_table.direct_row(ROW_KEY))

    int_col_name = b"int_col"
    str_col_name = b"str_col"
    num_increments = 100

    row.append_cell_value(COLUMN_FAMILY_ID1, str_col_name, b"foo")
    row.append_cell_value(COLUMN_FAMILY_ID1, str_col_name, b"bar")

    # Column names are convertible to byte strings provided it's a valid ascii string.
    row.append_cell_value(COLUMN_FAMILY_ID1, str_col_name.decode("ascii"), b"baz")

    for _ in range(0, num_increments):
        row.increment_cell_value(COLUMN_FAMILY_ID1, int_col_name, 1)

    row.commit()

    row_data = data_table.read_row(ROW_KEY)
    assert row_data.cells[COLUMN_FAMILY_ID1][int_col_name][
        0
    ].value == num_increments.to_bytes(8, byteorder="big", signed=True)
    assert row_data.cells[COLUMN_FAMILY_ID1][str_col_name][0].value == b"foobarbaz"


def test_table_sample_row_keys(data_table, skip_on_emulator):
    # Skip on emulator because it gives a random response.

    # sample_row_keys returns a generator
    response = list(data_table.sample_row_keys())
    previous_offset_bytes = 0
    for idx in range(len(INITIAL_ROW_SPLITS)):
        assert response[idx].row_key == INITIAL_ROW_SPLITS[idx]

        offset_bytes = response[idx].offset_bytes
        assert isinstance(offset_bytes, int)
        assert offset_bytes >= previous_offset_bytes

        previous_offset_bytes = offset_bytes
    assert response[-1].row_key == b""
    assert isinstance(response[-1].offset_bytes, int)
    assert response[-1].offset_bytes >= previous_offset_bytes


def test_table_direct_row_input_errors(data_table, rows_to_delete):
    from google.cloud.bigtable.row import MAX_MUTATIONS

    row = data_table.direct_row(ROW_KEY)
    rows_to_delete.append(row)

    # Column names are converted to bytes successfully if they're ASCII strings
    # or bytes already.
    with pytest.raises(TypeError):
        row.set_cell(COLUMN_FAMILY_ID1, INT_COL_NAME, CELL_VAL1)

    with pytest.raises(TypeError):
        row.delete_cell(COLUMN_FAMILY_ID1, INT_COL_NAME)

    # Various non int64s
    with pytest.raises(ValueError):
        row.set_cell(COLUMN_FAMILY_ID1, COL_NAME1, OVERFLOW_INT_CELL_VAL)

    with pytest.raises(ValueError):
        row.set_cell(COLUMN_FAMILY_ID1, COL_NAME1, OVERFLOW_INT_CELL_VAL2)

    # Since floats aren't ints, they aren't converted to bytes via struct.pack,
    # but via _to_bytes, so you get a TypeError instead.
    with pytest.raises(TypeError):
        row.set_cell(COLUMN_FAMILY_ID1, COL_NAME1, FLOAT_CELL_VAL)

    # Can't have more than MAX_MUTATIONS mutations, but only enforced after
    # a row.commit
    row.clear()
    for _ in range(0, MAX_MUTATIONS + 1):
        row.set_cell(COLUMN_FAMILY_ID1, COL_NAME1, CELL_VAL1)

    with pytest.raises(ValueError):
        row.commit()

    # Not having any mutations raises a ValueError
    row.clear()
    with pytest.raises(ValueError):
        row.commit()


def test_table_conditional_row_input_errors(data_table, rows_to_delete):
    from google.cloud.bigtable.row import MAX_MUTATIONS

    rows = [ROW_KEY, ROW_KEY_ALT]
    columns = [COL_NAME1]

    _populate_table(data_table, rows_to_delete, rows, columns=columns)

    true_row = data_table.conditional_row(ROW_KEY, PASS_ALL_FILTER)
    false_row = data_table.conditional_row(ROW_KEY_ALT, BLOCK_ALL_FILTER)
    rows_to_delete.append(true_row)
    rows_to_delete.append(false_row)

    # Column names are converted to bytes successfully if they're ASCII strings
    # or bytes already.
    with pytest.raises(TypeError):
        true_row.set_cell(COLUMN_FAMILY_ID1, INT_COL_NAME, CELL_VAL1)

    with pytest.raises(TypeError):
        true_row.delete_cell(COLUMN_FAMILY_ID1, INT_COL_NAME)

    # Various non int64s
    with pytest.raises(ValueError):
        true_row.set_cell(COLUMN_FAMILY_ID1, COL_NAME1, OVERFLOW_INT_CELL_VAL)

    with pytest.raises(ValueError):
        true_row.set_cell(COLUMN_FAMILY_ID1, COL_NAME1, OVERFLOW_INT_CELL_VAL2)

    # Since floats aren't ints, they aren't converted to bytes via struct.pack,
    # but via _to_bytes, so you get a TypeError instead.
    with pytest.raises(TypeError):
        true_row.set_cell(COLUMN_FAMILY_ID1, COL_NAME1, FLOAT_CELL_VAL)

    # Can't have more than MAX_MUTATIONS mutations, but only enforced after
    # a row.commit
    true_row.clear()
    for _ in range(0, MAX_MUTATIONS + 1):
        true_row.set_cell(COLUMN_FAMILY_ID1, COL_NAME1, CELL_VAL1)

    with pytest.raises(ValueError):
        true_row.commit()

    true_row.clear()

    # State could be anything, but it is evaluated to a boolean later.
    true_row.set_cell(COLUMN_FAMILY_ID1, COL_NAME1, CELL_VAL1, state=0)
    true_row.set_cell(COLUMN_FAMILY_ID1, COL_NAME1, CELL_VAL2, state=1)
    true_row.commit()

    false_row.set_cell(COLUMN_FAMILY_ID1, COL_NAME1, CELL_VAL1, state="")
    false_row.set_cell(COLUMN_FAMILY_ID1, COL_NAME1, CELL_VAL2, state="true_state")
    false_row.commit()

    true_row_data = data_table.read_row(true_row.row_key)
    assert true_row_data.cells[COLUMN_FAMILY_ID1][COL_NAME1][0].value == CELL_VAL2

    false_row_data = data_table.read_row(false_row.row_key)
    assert false_row_data.cells[COLUMN_FAMILY_ID1][COL_NAME1][0].value == CELL_VAL1

    # Not having any mutations is enforced client-side for conditional row; nothing happens.
    true_row.clear()
    true_row.commit()

    false_row.clear()
    false_row.commit()


def test_table_append_row_input_errors(data_table, rows_to_delete):
    from google.cloud.bigtable.row import MAX_MUTATIONS

    row = data_table.append_row(ROW_KEY)
    rows_to_delete.append(data_table.direct_row(ROW_KEY))

    # Column names should be convertible to bytes (str or bytes)
    with pytest.raises(AttributeError):
        row.append_cell_value(COLUMN_FAMILY_ID1, INT_COL_NAME, CELL_VAL1)

    with pytest.raises(AttributeError):
        row.increment_cell_value(COLUMN_FAMILY_ID1, INT_COL_NAME, 1)

    with pytest.raises(ValueError):
        row.increment_cell_value(COLUMN_FAMILY_ID1, COL_NAME1, OVERFLOW_INT_CELL_VAL)

    with pytest.raises(TypeError):
        row.increment_cell_value(COLUMN_FAMILY_ID1, COL_NAME1, FLOAT_CELL_VAL)

    # Can't have more than MAX_MUTATIONS mutations, but only enforced after
    # a row.commit
    row.clear()
    for _ in range(0, MAX_MUTATIONS + 1):
        row.append_cell_value(COLUMN_FAMILY_ID1, COL_NAME1, CELL_VAL1)

    with pytest.raises(ValueError):
        row.commit()

    # Not having any mutations gives a response of empty dict.
    row.clear()
    response = row.commit()
    assert response == {}


def test_access_with_non_admin_client(data_client, data_instance_id, data_table_id):
    instance = data_client.instance(data_instance_id)
    table = instance.table(data_table_id)
    assert table.read_row("nonesuch") is None  # no raise


def test_mutations_batcher_threading(data_table, rows_to_delete):
    """
    Test the mutations batcher by sending a bunch of mutations using different
    flush methods
    """
    import time

    import mock

    from google.cloud.bigtable.batcher import MutationsBatcher

    num_sent = 20
    all_results = []

    def callback(results):
        all_results.extend(results)

    # override flow control max elements
    with mock.patch("google.cloud.bigtable.batcher.MAX_OUTSTANDING_ELEMENTS", 2):
        with MutationsBatcher(
            data_table,
            flush_count=5,
            flush_interval=0.07,
            batch_completed_callback=callback,
        ) as batcher:
            # send mutations in a way that timed flushes and count flushes interleave
            for i in range(num_sent):
                row = data_table.direct_row("row{}".format(i))
                row.set_cell(
                    COLUMN_FAMILY_ID1, COL_NAME1, "val{}".format(i).encode("utf-8")
                )
                rows_to_delete.append(row)
                batcher.mutate(row)
                time.sleep(0.01)
    # ensure all mutations were sent
    assert len(all_results) == num_sent


def test_mutations_batcher_exceptions(data_table, rows_to_delete):
    """Test the mutations batcher exception handling"""
    import mock
    from google.api_core import exceptions as core_exceptions
    from google.rpc import code_pb2, status_pb2

    from google.cloud.bigtable.batcher import MutationsBatcher, MutationsBatchError
    from google.cloud.bigtable_v2 import MutateRowsResponse

    num_sent = 5

    error_response = [
        MutateRowsResponse(
            entries=[
                MutateRowsResponse.Entry(
                    index=i,
                    status=status_pb2.Status(
                        code=code_pb2.INTERNAL,
                        message="Test error",
                    ),
                )
                for i in range(num_sent)
            ]
        )
    ]

    # Simulate only failures
    with pytest.raises(MutationsBatchError):
        with mock.patch.object(
            data_table._instance._client.table_data_client, "mutate_rows"
        ) as mutate_mock:
            mutate_mock.side_effect = [error_response] * 100000
            with MutationsBatcher(
                data_table,
                flush_count=10,
                flush_interval=1,
            ) as batcher:
                for i in range(num_sent):
                    row = data_table.direct_row("row{}".format(i))
                    row.set_cell(
                        COLUMN_FAMILY_ID1, COL_NAME1, "val{}".format(i).encode("utf-8")
                    )
                    rows_to_delete.append(row)
                    batcher.mutate(row)
                batcher.flush()

    # Test that exceptions are only raised on close.
    with mock.patch.object(
        data_table._instance._client.table_data_client, "mutate_rows"
    ) as mutate_mock:
        mutate_mock.side_effect = [error_response] * 100000
        batcher = MutationsBatcher(
            data_table,
            flush_count=10,
            flush_interval=1,
        )
        for i in range(num_sent):
            row = data_table.direct_row("row{}".format(i))
            row.set_cell(
                COLUMN_FAMILY_ID1, COL_NAME1, "val{}".format(i).encode("utf-8")
            )
            rows_to_delete.append(row)
            batcher.mutate(row)
        batcher.flush()

        with pytest.raises(MutationsBatchError):
            batcher.close()

    # Test RPC-level error.
    with pytest.raises(MutationsBatchError) as exc_info:
        with mock.patch.object(
            data_table._instance._client.table_data_client, "mutate_rows"
        ) as mutate_mock:
            mutate_mock.side_effect = core_exceptions.InternalServerError(
                "Test RPC error"
            )
            with MutationsBatcher(
                data_table,
                flush_count=10,
                flush_interval=1,
            ) as batcher:
                for i in range(num_sent):
                    row = data_table.direct_row("row{}".format(i))
                    row.set_cell(
                        COLUMN_FAMILY_ID1, COL_NAME1, "val{}".format(i).encode("utf-8")
                    )
                    rows_to_delete.append(row)
                    batcher.mutate(row)
                batcher.flush()
    assert len(exc_info.value.exc) == num_sent


def test_mutations_batcher_manual_flush(data_table, rows_to_delete):
    """Test the mutations batcher manual flush"""
    import mock
    from google.rpc import code_pb2, status_pb2

    from google.cloud.bigtable.batcher import MutationsBatcher

    num_batches = 5
    batch_size = 4
    callback = mock.MagicMock()

    with MutationsBatcher(
        data_table,
        flush_count=500,
        flush_interval=5,
        batch_completed_callback=callback,
    ) as batcher:
        for i in range(num_batches):
            for j in range(batch_size):
                num = i * batch_size + j
                row = data_table.direct_row(f"row{num}".encode("utf-8"))
                row.set_cell(COLUMN_FAMILY_ID1, COL_NAME1, f"val{num}".encode("utf-8"))
                rows_to_delete.append(row)
                batcher.mutate(row)
            batcher.flush()
            callback.assert_called_with(
                [status_pb2.Status(code=code_pb2.OK)] * batch_size
            )

    # ensure all mutations were sent
    rows = data_table.read_rows()
    rows.consume_all()
    for row_num in range(0, num_batches * batch_size):
        row = rows.rows[f"row{row_num}".encode("utf-8")]
        assert row.cells[COLUMN_FAMILY_ID1][COL_NAME1][
            0
        ].value == f"val{row_num}".encode("utf-8")
