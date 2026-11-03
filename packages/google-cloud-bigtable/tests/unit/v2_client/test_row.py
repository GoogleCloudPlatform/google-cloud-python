# Copyright 2015 Google LLC
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


import mock
import pytest

from ._testing import _make_credentials

_INSTANCE_ID = "test-instance"


def _make_client(*args, **kwargs):
    from google.cloud.bigtable.client import Client

    return Client(*args, **kwargs)


def _make_row(*args, **kwargs):
    from google.cloud.bigtable.row import Row

    return Row(*args, **kwargs)


def test_row_key_getter():
    row = _make_row(row_key=b"row_key", table="table")
    assert b"row_key" == row.row_key


def test_row_table_getter():
    row = _make_row(row_key=b"row_key", table="table")
    assert "table" == row.table


def _make__set_delete_row(*args, **kwargs):
    from google.cloud.bigtable.row import _SetDeleteRow

    return _SetDeleteRow(*args, **kwargs)


def test__set_detlete_row__get_mutations_virtual():
    row = _make__set_delete_row(b"row-key", None)
    with pytest.raises(NotImplementedError):
        row._get_mutations(None)


def _make_direct_row(*args, **kwargs):
    from google.cloud.bigtable.row import DirectRow

    return DirectRow(*args, **kwargs)


def test_direct_row_constructor():
    row_key = b"row_key"
    table = object()

    row = _make_direct_row(row_key, table)
    assert row._row_key == row_key
    assert row._table is table
    assert row._mutations == []


def test_direct_row_constructor_with_unicode():
    row_key = "row_key"
    row_key_bytes = b"row_key"
    table = object()

    row = _make_direct_row(row_key, table)
    assert row._row_key == row_key_bytes
    assert row._table is table


def test_direct_row_constructor_with_non_bytes():
    row_key = object()
    with pytest.raises(TypeError):
        _make_direct_row(row_key, None)


def test_direct_row__get_mutations():
    row_key = b"row_key"
    row = _make_direct_row(row_key, None)

    row._mutations = mutations = object()
    assert mutations is row._get_mutations(None)


def test_direct_row__get_mutation_pbs():
    from google.cloud.bigtable.data.mutations import _SERVER_SIDE_TIMESTAMP, SetCell

    row_key = b"row_key"
    row = _make_direct_row(row_key, None)

    mutation = SetCell(
        family="column_family_id",
        qualifier=b"column",
        new_value=b"value",
        timestamp_micros=_SERVER_SIDE_TIMESTAMP,
    )

    row._mutations = [mutation]

    assert row._get_mutation_pbs() == [mutation._to_pb()]


def test_direct_row_get_mutations_size():
    row_key = b"row_key"
    row = _make_direct_row(row_key, None)

    column_family_id1 = "column_family_id1"
    column_family_id2 = "column_family_id2"
    column1 = b"column1"
    column2 = b"column2"
    number_of_bytes = 1 * 1024 * 1024
    value = b"1" * number_of_bytes

    row.set_cell(column_family_id1, column1, value)
    row.set_cell(column_family_id2, column2, value)

    total_mutations_size = 0
    for mutation in row._get_mutation_pbs():
        total_mutations_size += mutation._pb.ByteSize()

    assert row.get_mutations_size() == total_mutations_size


def _set_cell_helper(
    column=None,
    column_bytes=None,
    value=b"foobar",
    timestamp=None,
    timestamp_micros=-1,
):
    import struct

    from google.cloud.bigtable.data.mutations import SetCell

    row_key = b"row_key"
    column_family_id = "column_family_id"
    if column is None:
        column = b"column"
    table = object()
    row = _make_direct_row(row_key, table)
    assert row._mutations == []
    row.set_cell(column_family_id, column, value, timestamp=timestamp)

    if isinstance(value, int):
        value = struct.pack(">q", value)
    expected_mutation = SetCell(
        family=column_family_id,
        qualifier=column_bytes or column,
        new_value=value,
        timestamp_micros=timestamp_micros,
    )

    _assert_mutations_equal(row._mutations, [expected_mutation])


def test_direct_row_set_cell():
    _set_cell_helper()


def test_direct_row_set_cell_with_string_column():
    column_bytes = b"column"
    column_non_bytes = "column"
    _set_cell_helper(column=column_non_bytes, column_bytes=column_bytes)


def test_direct_row_set_cell_with_integer_value():
    value = 1337
    _set_cell_helper(value=value)


def test_direct_row_set_cell_with_min_int64_value():
    _set_cell_helper(value=-(2**63))


@pytest.mark.parametrize("bool_val", [True, False])
def test_direct_row_set_cell_with_bool_value(bool_val):
    row = _make_direct_row(b"row_key", object())
    with pytest.raises(TypeError):
        row.set_cell("column_family_id", b"column", bool_val)


def test_direct_row_set_cell_with_non_bytes_value():
    row_key = b"row_key"
    column = b"column"
    column_family_id = "column_family_id"
    table = object()

    row = _make_direct_row(row_key, table)
    value = object()  # Not bytes
    with pytest.raises(TypeError):
        row.set_cell(column_family_id, column, value)


def test_direct_row_set_cell_with_non_null_timestamp():
    import datetime

    from google.cloud._helpers import _EPOCH

    microseconds = 898294371
    millis_granularity = microseconds - (microseconds % 1000)
    timestamp = _EPOCH + datetime.timedelta(microseconds=microseconds)
    _set_cell_helper(timestamp=timestamp, timestamp_micros=millis_granularity)


def test_direct_row_delete():
    from google.cloud.bigtable.data.mutations import DeleteAllFromRow

    row_key = b"row_key"
    row = _make_direct_row(row_key, object())
    assert row._mutations == []
    row.delete()

    expected_mutation = DeleteAllFromRow()
    _assert_mutations_equal(row._mutations, [expected_mutation])


def test_direct_row_delete_cell():
    from google.cloud.bigtable.row import DirectRow

    class MockRow(DirectRow):
        def __init__(self, *args, **kwargs):
            super(MockRow, self).__init__(*args, **kwargs)
            self._args = []
            self._kwargs = []

        # Replace the called method with one that logs arguments.
        def _delete_cells(self, *args, **kwargs):
            self._args.append(args)
            self._kwargs.append(kwargs)

    row_key = b"row_key"
    column = b"column"
    column_family_id = "column_family_id"
    table = object()

    mock_row = MockRow(row_key, table)
    # Make sure no values are set before calling the method.
    assert mock_row._mutations == []
    assert mock_row._args == []
    assert mock_row._kwargs == []

    # Actually make the request against the mock class.
    time_range = object()
    mock_row.delete_cell(column_family_id, column, time_range=time_range)
    assert mock_row._mutations == []
    assert mock_row._args == [(column_family_id, [column])]
    assert mock_row._kwargs == [{"state": None, "time_range": time_range}]


def test_direct_row_delete_cells_non_iterable():
    row_key = b"row_key"
    column_family_id = "column_family_id"
    table = object()

    row = _make_direct_row(row_key, table)
    columns = object()  # Not iterable
    with pytest.raises(TypeError):
        row.delete_cells(column_family_id, columns)


@pytest.mark.parametrize("columns", ["col_abc", b"col_abc"])
def test_direct_row_delete_cells_rejects_str_and_bytes(columns):
    row = _make_direct_row(b"row_key", object())
    with pytest.raises(TypeError, match="columns must be an iterable of column names"):
        row.delete_cells("column_family_id", columns)
    assert row._mutations == []


@pytest.mark.parametrize("columns", ["col_abc", b"col_abc"])
def test_conditional_row_delete_cells_rejects_str_and_bytes(columns):
    row = _make_conditional_row(b"row_key", object(), filter_=object())
    with pytest.raises(TypeError, match="columns must be an iterable of column names"):
        row.delete_cells("column_family_id", columns, state=True)
    assert row._true_pb_mutations == []


def test_direct_row_delete_cells_all_columns():
    from google.cloud.bigtable.data.mutations import DeleteAllFromFamily
    from google.cloud.bigtable.row import DirectRow

    row_key = b"row_key"
    column_family_id = "column_family_id"
    table = object()

    row = _make_direct_row(row_key, table)
    assert row._mutations == []
    row.delete_cells(column_family_id, DirectRow.ALL_COLUMNS)

    expected_mutation = DeleteAllFromFamily(family_to_delete=column_family_id)
    _assert_mutations_equal(row._mutations, [expected_mutation])


def test_direct_row_delete_cells_no_columns():
    row_key = b"row_key"
    column_family_id = "column_family_id"
    table = object()

    row = _make_direct_row(row_key, table)
    columns = []
    assert row._mutations == []
    row.delete_cells(column_family_id, columns)
    assert row._mutations == []


def _delete_cells_helper(time_range=None):
    from google.cloud.bigtable.data.mutations import DeleteRangeFromColumn

    row_key = b"row_key"
    column = b"column"
    column_family_id = "column_family_id"
    table = object()

    row = _make_direct_row(row_key, table)
    columns = [column]
    assert row._mutations == []
    row.delete_cells(column_family_id, columns, time_range=time_range)

    expected_mutation = DeleteRangeFromColumn(family=column_family_id, qualifier=column)
    if time_range is not None:
        timestamps = time_range._to_dict()
        expected_mutation.start_timestamp_micros = timestamps.get(
            "start_timestamp_micros"
        )
        expected_mutation.end_timestamp_micros = timestamps.get("end_timestamp_micros")
    _assert_mutations_equal(row._mutations, [expected_mutation])


def test_direct_row_delete_cells_no_time_range():
    _delete_cells_helper()


def test_direct_row_delete_cells_with_time_range():
    import datetime

    from google.cloud._helpers import _EPOCH

    from google.cloud.bigtable.row_filters import TimestampRange

    microseconds = 30871000  # Makes sure already milliseconds granularity
    start = _EPOCH + datetime.timedelta(microseconds=microseconds)
    time_range = TimestampRange(start=start)
    _delete_cells_helper(time_range=time_range)


def test_direct_row_delete_cells_with_bad_column():
    # This makes sure a failure on one of the columns doesn't leave
    # the row's mutations in a bad state.
    row_key = b"row_key"
    column = b"column"
    column_family_id = "column_family_id"
    table = object()

    row = _make_direct_row(row_key, table)
    columns = [column, object()]
    assert row._mutations == []
    with pytest.raises(TypeError):
        row.delete_cells(column_family_id, columns)
    assert row._mutations == []


def test_direct_row_delete_cells_with_string_columns():
    from google.cloud.bigtable.data.mutations import DeleteRangeFromColumn

    row_key = b"row_key"
    column_family_id = "column_family_id"
    column1 = "column1"
    column1_bytes = b"column1"
    column2 = "column2"
    column2_bytes = b"column2"
    table = object()

    row = _make_direct_row(row_key, table)
    columns = [column1, column2]
    assert row._mutations == []
    row.delete_cells(column_family_id, columns)

    expected_mutation1 = DeleteRangeFromColumn(
        family=column_family_id, qualifier=column1_bytes
    )
    expected_mutation2 = DeleteRangeFromColumn(
        family=column_family_id, qualifier=column2_bytes
    )
    _assert_mutations_equal(row._mutations, [expected_mutation1, expected_mutation2])


def test_direct_row_commit():
    from google.rpc import code_pb2, status_pb2

    from google.cloud.bigtable_v2.services.bigtable import BigtableClient

    project_id = "project-id"
    row_key = b"row_key"
    table_name = "projects/more-stuff"
    app_profile_id = "app_profile_id"
    column_family_id = "column_family_id"
    column = b"column"

    credentials = _make_credentials()
    client = _make_client(project=project_id, credentials=credentials, admin=True)
    table = _Table(table_name, client=client, app_profile_id=app_profile_id)
    row = _make_direct_row(row_key, table)
    value = b"bytes-value"

    # Set mock
    api = mock.create_autospec(BigtableClient)
    response_pb = _MutateRowResponsePB()
    api.mutate_row.side_effect = [response_pb]
    client.table_data_client
    client._table_data_client._gapic_client = api

    # Perform the method and check the result.
    row.set_cell(column_family_id, column, value)
    response = row.commit()
    assert row._mutations == []
    assert response == status_pb2.Status(code=code_pb2.OK)
    call_args = api.mutate_row.call_args
    assert app_profile_id == call_args.app_profile_id[0]


def test_direct_row_commit_with_exception():
    from google.api_core.exceptions import InternalServerError
    from google.rpc import code_pb2, status_pb2

    from google.cloud.bigtable_v2.services.bigtable import BigtableClient

    project_id = "project-id"
    row_key = b"row_key"
    table_name = "projects/more-stuff"
    app_profile_id = "app_profile_id"
    column_family_id = "column_family_id"
    column = b"column"

    credentials = _make_credentials()
    client = _make_client(project=project_id, credentials=credentials, admin=True)
    table = _Table(table_name, client=client, app_profile_id=app_profile_id)
    row = _make_direct_row(row_key, table)
    value = b"bytes-value"

    # Set mock
    api = mock.create_autospec(BigtableClient)
    exception_message = "Boom!"
    exception = InternalServerError(exception_message)
    api.mutate_row.side_effect = [exception]
    client.table_data_client
    client._table_data_client._gapic_client = api

    # Perform the method and check the result.
    row.set_cell(column_family_id, column, value)
    result = row.commit()
    assert row._mutations == []
    assert result == status_pb2.Status(
        code=code_pb2.Code.INTERNAL, message=exception_message
    )
    call_args = api.mutate_row.call_args
    assert app_profile_id == call_args.app_profile_id[0]


def test_direct_row_commit_with_unknown_exception():
    from google.api_core.exceptions import GoogleAPICallError
    from google.rpc import code_pb2, status_pb2

    from google.cloud.bigtable_v2.services.bigtable import BigtableClient

    project_id = "project-id"
    row_key = b"row_key"
    table_name = "projects/more-stuff"
    app_profile_id = "app_profile_id"
    column_family_id = "column_family_id"
    column = b"column"

    credentials = _make_credentials()
    client = _make_client(project=project_id, credentials=credentials, admin=True)
    table = _Table(table_name, client=client, app_profile_id=app_profile_id)
    row = _make_direct_row(row_key, table)
    value = b"bytes-value"

    # Set mock
    api = mock.create_autospec(BigtableClient)
    exception_message = "Boom!"
    exception = GoogleAPICallError(message=exception_message)
    api.mutate_row.side_effect = [exception]
    client.table_data_client
    client._table_data_client._gapic_client = api

    # Perform the method and check the result.
    row.set_cell(column_family_id, column, value)
    result = row.commit()
    assert row._mutations == []
    assert result == status_pb2.Status(
        code=code_pb2.Code.UNKNOWN, message=exception_message
    )
    call_args = api.mutate_row.call_args
    assert app_profile_id == call_args.app_profile_id[0]


def _make_row_for_commit():
    """Build a DirectRow holding a single pending mutation."""
    credentials = _make_credentials()
    client = _make_client(project="project-id", credentials=credentials, admin=True)
    table = _Table("projects/more-stuff", client=client, app_profile_id=None)
    row = _make_direct_row(b"row_key", table)
    row.set_cell("column_family_id", b"column", b"bytes-value")
    return row


def _commit_with_operation_error(exc):
    """Commit a row whose underlying ``mutate_row`` fails with ``exc``."""
    row = _make_row_for_commit()

    with mock.patch.object(row._table._table_impl, "mutate_row") as mutate_row_mock:
        mutate_row_mock.side_effect = exc
        return row.commit()


def test_direct_row_commit_unwraps_retry_exception_group():
    """On timeout the synthetic DeadlineExceeded is unwrapped, so that a single
    row commit reports the same wire error as the equivalent bulk call."""
    from google.api_core.exceptions import ServiceUnavailable
    from google.api_core.retry import RetryFailureReason
    from google.rpc import code_pb2

    from google.cloud.bigtable.data._helpers import _retry_exception_factory

    source_exc, _ = _retry_exception_factory(
        [ServiceUnavailable("first failure"), ServiceUnavailable("final failure")],
        RetryFailureReason.TIMEOUT,
        60.0,
    )

    result = _commit_with_operation_error(source_exc)

    assert result.code == code_pb2.Code.UNAVAILABLE
    assert result.message == "final failure"


def test_direct_row_commit_reports_terminal_error_when_not_timed_out():
    """When retries stop for any other reason the raised exception already is
    the terminal error, so the chained earlier attempts are not unwrapped."""
    from google.api_core.exceptions import PermissionDenied, ServiceUnavailable
    from google.api_core.retry import RetryFailureReason
    from google.rpc import code_pb2

    from google.cloud.bigtable.data._helpers import _retry_exception_factory

    source_exc, _ = _retry_exception_factory(
        [ServiceUnavailable("earlier attempt"), PermissionDenied("terminal failure")],
        RetryFailureReason.NON_RETRYABLE_ERROR,
        60.0,
    )

    result = _commit_with_operation_error(source_exc)

    assert result.code == code_pb2.Code.PERMISSION_DENIED
    assert result.message == "terminal failure"


def test_direct_row_commit_keeps_deadline_exceeded_returned_by_server():
    """A DeadlineExceeded returned by the server is the terminal error and is
    reported as-is, unlike the locally built one."""
    from google.api_core.exceptions import DeadlineExceeded, ServiceUnavailable
    from google.rpc import code_pb2

    from google.cloud.bigtable.data.exceptions import RetryExceptionGroup

    exc = DeadlineExceeded("server deadline exceeded", response=mock.Mock())
    exc.__cause__ = RetryExceptionGroup([ServiceUnavailable("earlier attempt")])

    result = _commit_with_operation_error(exc)

    assert result.code == code_pb2.Code.DEADLINE_EXCEEDED
    assert result.message == "server deadline exceeded"


def test_direct_row_commit_keeps_mutations_when_it_raises():
    """An error that cannot be reported as a status escapes to the caller, who
    is left with no outcome to act on, so the mutations are kept."""
    row = _make_row_for_commit()

    with mock.patch.object(row._table._table_impl, "mutate_row") as mutate_row_mock:
        mutate_row_mock.side_effect = RuntimeError("failed with unspecified exception")
        with pytest.raises(RuntimeError):
            row.commit()

    assert len(row._get_mutations()) == 1


def test_direct_row_commit_with_invalid_argument():
    from google.cloud.bigtable_v2.services.bigtable import BigtableClient

    project_id = "project-id"
    row_key = b"row_key"
    table_name = "projects/more-stuff"
    app_profile_id = "app_profile_id"

    credentials = _make_credentials()
    client = _make_client(project=project_id, credentials=credentials, admin=True)
    table = _Table(table_name, client=client, app_profile_id=app_profile_id)
    row = _make_direct_row(row_key, table)

    # Set mock
    api = mock.create_autospec(BigtableClient)
    client.table_data_client
    client._table_data_client._gapic_client = api

    # Perform the method and check the result.
    with pytest.raises(ValueError, match="No mutations provided"):
        row.commit()
    api.mutate_row.assert_not_called()


def test_direct_row_commit_too_many_mutations():
    from google.cloud._testing import _Monkey

    from google.cloud.bigtable import row as MUT

    row_key = b"row_key"
    table = object()
    row = _make_direct_row(row_key, table)
    row._mutations = [1, 2, 3]
    num_mutations = len(row._mutations)
    with _Monkey(MUT, MAX_MUTATIONS=num_mutations - 1):
        with pytest.raises(
            ValueError, match="Number of mutations exceeds the maximum allowable"
        ):
            row.commit()


def _make_conditional_row(*args, **kwargs):
    from google.cloud.bigtable.row import ConditionalRow

    return ConditionalRow(*args, **kwargs)


def test_conditional_row_constructor():
    row_key = b"row_key"
    table = object()
    filter_ = object()

    row = _make_conditional_row(row_key, table, filter_=filter_)
    assert row._row_key == row_key
    assert row._table is table
    assert row._filter is filter_
    assert row._true_pb_mutations == []
    assert row._false_pb_mutations == []


def test_conditional_row__get_mutations():
    row_key = b"row_key"
    filter_ = object()
    row = _make_conditional_row(row_key, None, filter_=filter_)

    row._true_pb_mutations = true_mutations = object()
    row._false_pb_mutations = false_mutations = object()
    assert true_mutations is row._get_mutations(True)
    assert false_mutations is row._get_mutations(False)
    assert false_mutations is row._get_mutations(None)


def test_conditional_row_commit():
    from google.cloud.bigtable.row_filters import RowSampleFilter
    from google.cloud.bigtable_v2.services.bigtable import BigtableClient

    project_id = "project-id"
    row_key = b"row_key"
    table_name = "projects/more-stuff"
    app_profile_id = "app_profile_id"
    column_family_id1 = "column_family_id1"
    column_family_id2 = "column_family_id2"
    column_family_id3 = "column_family_id3"
    column1 = b"column1"
    column2 = b"column2"

    api = mock.create_autospec(BigtableClient)
    credentials = _make_credentials()
    client = _make_client(project=project_id, credentials=credentials, admin=True)
    table = _Table(table_name, client=client, app_profile_id=app_profile_id)
    row_filter = RowSampleFilter(0.33)
    row = _make_conditional_row(row_key, table, filter_=row_filter)

    # Create request_pb
    value1 = b"bytes-value"

    # Create response_pb
    predicate_matched = True
    response_pb = _CheckAndMutateRowResponsePB(predicate_matched=predicate_matched)

    # Patch the stub used by the API method.
    api.check_and_mutate_row.side_effect = [response_pb]
    client.table_data_client
    client._table_data_client._gapic_client = api

    # Create expected_result.
    expected_result = predicate_matched

    # Perform the method and check the result.
    row.set_cell(column_family_id1, column1, value1, state=True)
    row.delete(state=False)
    row.delete_cell(column_family_id2, column2, state=True)
    row.delete_cells(column_family_id3, row.ALL_COLUMNS, state=True)
    result = row.commit()
    call_args = api.check_and_mutate_row.call_args
    assert app_profile_id == call_args.app_profile_id[0]
    assert result == expected_result
    assert row._true_pb_mutations == []
    assert row._false_pb_mutations == []


def test_conditional_row_commit_too_many_mutations():
    from google.cloud._testing import _Monkey

    from google.cloud.bigtable import row as MUT

    row_key = b"row_key"
    table = object()
    filter_ = object()
    row = _make_conditional_row(row_key, table, filter_=filter_)
    row._true_pb_mutations = [1, 2, 3]
    num_mutations = len(row._true_pb_mutations)
    with _Monkey(MUT, MAX_MUTATIONS=num_mutations - 1):
        with pytest.raises(ValueError):
            row.commit()


def test_conditional_row_commit_no_mutations():
    from ._testing import _FakeStub

    project_id = "project-id"
    row_key = b"row_key"

    credentials = _make_credentials()
    client = _make_client(project=project_id, credentials=credentials, admin=True)
    table = _Table(None, client=client)
    filter_ = object()
    row = _make_conditional_row(row_key, table, filter_=filter_)
    assert row._true_pb_mutations == []
    assert row._false_pb_mutations == []

    # Patch the stub used by the API method.
    stub = _FakeStub()

    # Perform the method and check the result.
    result = row.commit()
    assert result is None
    # Make sure no request was sent.
    assert stub.method_calls == []


def _make_append_row(*args, **kwargs):
    from google.cloud.bigtable.row import AppendRow

    return AppendRow(*args, **kwargs)


def test_append_row_constructor():
    row_key = b"row_key"
    table = object()

    row = _make_append_row(row_key, table)
    assert row._row_key == row_key
    assert row._table is table
    assert row._rule_list == []


def test_append_row_clear():
    row_key = b"row_key"
    table = object()
    row = _make_append_row(row_key, table)
    row._rule_list = [1, 2, 3]
    row.clear()
    assert row._rule_list == []


def test_append_row_append_cell_value():
    from google.cloud.bigtable.data.read_modify_write_rules import AppendValueRule

    table = object()
    row_key = b"row_key"
    row = _make_append_row(row_key, table)
    assert row._rule_list == []

    column = b"column"
    column_family_id = "column_family_id"
    value = b"bytes-val"
    row.append_cell_value(column_family_id, column, value)
    expected_pb = AppendValueRule(
        family=column_family_id, qualifier=column, append_value=value
    )
    _assert_mutations_equal(row._rule_list, [expected_pb])


def test_append_row_increment_cell_value():
    from google.cloud.bigtable.data.read_modify_write_rules import IncrementRule

    table = object()
    row_key = b"row_key"
    row = _make_append_row(row_key, table)
    assert row._rule_list == []

    column = b"column"
    column_family_id = "column_family_id"
    int_value = 281330
    row.increment_cell_value(column_family_id, column, int_value)
    expected_pb = IncrementRule(
        family=column_family_id,
        qualifier=column,
        increment_amount=int_value,
    )
    _assert_mutations_equal(row._rule_list, [expected_pb])


def test_append_row_commit():
    from google.cloud._testing import _Monkey

    from google.cloud.bigtable import row as MUT
    from google.cloud.bigtable_v2.services.bigtable import BigtableClient

    project_id = "project-id"
    row_key = b"row_key"
    table_name = "projects/more-stuff"
    app_profile_id = "app_profile_id"
    column_family_id = "column_family_id"
    column = b"column"

    api = mock.create_autospec(BigtableClient)

    credentials = _make_credentials()
    client = _make_client(project=project_id, credentials=credentials, admin=True)
    table = _Table(table_name, client=client, app_profile_id=app_profile_id)
    row = _make_append_row(row_key, table)

    # Create request_pb
    value = b"bytes-value"

    # Create expected_result.
    row_responses = []
    expected_result = object()

    # Patch API calls
    client.table_data_client
    client._table_data_client._gapic_client = api

    def mock_parse_rmw_row_response(row_response):
        row_responses.append(row_response)
        return expected_result

    # Perform the method and check the result.
    with _Monkey(MUT, _parse_rmw_row_response=mock_parse_rmw_row_response):
        row._table._instance._client._table_data_client._gapic_client = api
        row.append_cell_value(column_family_id, column, value)
        result = row.commit()
    call_args = api.read_modify_write_row.call_args_list[0]
    assert app_profile_id == call_args.app_profile_id[0]
    assert result == expected_result
    assert row._rule_list == []


def test_append_row_commit_no_rules():
    from ._testing import _FakeStub

    project_id = "project-id"
    row_key = b"row_key"

    credentials = _make_credentials()
    client = _make_client(project=project_id, credentials=credentials, admin=True)
    table = _Table(None, client=client)
    row = _make_append_row(row_key, table)
    assert row._rule_list == []

    # Patch the stub used by the API method.
    stub = _FakeStub()

    # Perform the method and check the result.
    result = row.commit()
    assert result == {}
    # Make sure no request was sent.
    assert stub.method_calls == []


def test_append_row_commit_too_many_mutations():
    from google.cloud._testing import _Monkey

    from google.cloud.bigtable import row as MUT

    row_key = b"row_key"
    table = object()
    row = _make_append_row(row_key, table)
    row._rule_list = [1, 2, 3]
    num_mutations = len(row._rule_list)
    with _Monkey(MUT, MAX_MUTATIONS=num_mutations - 1):
        with pytest.raises(ValueError):
            row.commit()


def test__parse_rmw_row_response():
    from google.cloud._helpers import _datetime_from_microseconds

    from google.cloud.bigtable.data.row import Row
    from google.cloud.bigtable.row import _parse_rmw_row_response

    col_fam1 = "col-fam-id"
    col_fam2 = "col-fam-id2"
    col_name1 = b"col-name1"
    col_name2 = b"col-name2"
    col_name3 = b"col-name3-but-other-fam"
    cell_val1 = b"cell-val"
    cell_val2 = b"cell-val-newer"
    cell_val3 = b"altcol-cell-val"
    cell_val4 = b"foo"

    microseconds = 1000871
    timestamp = _datetime_from_microseconds(microseconds)
    expected_output = {
        col_fam1: {
            col_name1: [(cell_val1, timestamp), (cell_val2, timestamp)],
            col_name2: [(cell_val3, timestamp)],
        },
        col_fam2: {col_name3: [(cell_val4, timestamp)]},
    }
    response_row = _RowPB(
        families=[
            _FamilyPB(
                name=col_fam1,
                columns=[
                    _ColumnPB(
                        qualifier=col_name1,
                        cells=[
                            _CellPB(value=cell_val1, timestamp_micros=microseconds),
                            _CellPB(value=cell_val2, timestamp_micros=microseconds),
                        ],
                    ),
                    _ColumnPB(
                        qualifier=col_name2,
                        cells=[_CellPB(value=cell_val3, timestamp_micros=microseconds)],
                    ),
                ],
            ),
            _FamilyPB(
                name=col_fam2,
                columns=[
                    _ColumnPB(
                        qualifier=col_name3,
                        cells=[_CellPB(value=cell_val4, timestamp_micros=microseconds)],
                    )
                ],
            ),
        ]
    )
    sample_input = Row._from_pb(response_row)
    assert expected_output == _parse_rmw_row_response(sample_input)


def _MutateRowResponsePB():
    from google.cloud.bigtable_v2.types import bigtable as messages_v2_pb2

    return messages_v2_pb2.MutateRowResponse()


def _CheckAndMutateRowResponsePB(*args, **kw):
    from google.cloud.bigtable_v2.types import bigtable as messages_v2_pb2

    return messages_v2_pb2.CheckAndMutateRowResponse(*args, **kw)


def _CellPB(*args, **kw):
    from google.cloud.bigtable_v2.types import data as data_v2_pb2

    return data_v2_pb2.Cell(*args, **kw)


def _ColumnPB(*args, **kw):
    from google.cloud.bigtable_v2.types import data as data_v2_pb2

    return data_v2_pb2.Column(*args, **kw)


def _FamilyPB(*args, **kw):
    from google.cloud.bigtable_v2.types import data as data_v2_pb2

    return data_v2_pb2.Family(*args, **kw)


def _RowPB(*args, **kw):
    from google.cloud.bigtable_v2.types import data as data_v2_pb2

    return data_v2_pb2.Row(*args, **kw)


def _assert_mutations_equal(mutations_1, mutations_2):
    assert len(mutations_1) == len(mutations_2)

    for i in range(0, len(mutations_1)):
        assert type(mutations_1[i]) is type(mutations_2[i])
        assert mutations_1[i]._to_pb() == mutations_2[i]._to_pb()


class _Instance(object):
    def __init__(self, client=None):
        self._client = client


class _Table(object):
    def __init__(self, name, client=None, app_profile_id=None):
        self.name = name
        self._instance = _Instance(client)
        self._app_profile_id = app_profile_id
        self.client = client

        self._table_impl = self._instance._client._veneer_data_client.get_table(
            _INSTANCE_ID,
            self.name,
            app_profile_id=self._app_profile_id,
        )
