# Copyright 2025 Google LLC.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from unittest import mock

import pytest
from google.api_core import exceptions, operation
from google.api_core.operations_v1 import operations_client
from google.longrunning import operations_pb2
from google.rpc import code_pb2, status_pb2

from google.cloud.bigtable_admin_v2.overlay.types import restore_table
from google.cloud.bigtable_admin_v2.types import bigtable_table_admin, table

# Set up the mock operations
DEFAULT_MAX_POLL = 3
RESTORE_TABLE_OPERATION_TABLE_NAME = "Test Table"
RESTORE_TABLE_OPERATION_NAME = "test/restore_table"
RESTORE_TABLE_OPERATION_METADATA = bigtable_table_admin.RestoreTableMetadata(
    name=RESTORE_TABLE_OPERATION_TABLE_NAME,
)
OPTIMIZE_RESTORED_TABLE_OPERATION_NAME = "test/optimize_restore_table"
OPTIMIZE_RESTORED_TABLE_METADATA = bigtable_table_admin.OptimizeRestoredTableMetadata(
    name=RESTORE_TABLE_OPERATION_TABLE_NAME,
)

OPTIMIZE_RESTORED_TABLE_OPERATION_ID = "abcdefg"
RESTORE_TABLE_OPERATION_FINISHED_RESPONSE = table.Table(
    name=RESTORE_TABLE_OPERATION_TABLE_NAME,
)
RESTORE_TABLE_OPERATION_FINISHED_ERROR = status_pb2.Status(
    code=code_pb2.DEADLINE_EXCEEDED, message="Deadline Exceeded"
)


def make_operation_proto(
    name, done=False, metadata=None, response=None, error=None, **kwargs
):
    operation_proto = operations_pb2.Operation(name=name, done=done, **kwargs)

    if metadata is not None:
        operation_proto.metadata.Pack(metadata._pb)

    if response is not None:
        operation_proto.response.Pack(response._pb)

    if error is not None:
        operation_proto.error.CopyFrom(error)

    return operation_proto


RESTORE_TABLE_IN_PROGRESS_OPERATION_PROTO = make_operation_proto(
    name=RESTORE_TABLE_OPERATION_NAME,
    done=False,
    metadata=RESTORE_TABLE_OPERATION_METADATA,
)

OPTIMIZE_RESTORED_TABLE_OPERATION_PROTO = make_operation_proto(
    name=OPTIMIZE_RESTORED_TABLE_OPERATION_NAME,
    metadata=OPTIMIZE_RESTORED_TABLE_METADATA,
)


# Set up the mock operation client
def mock_restore_table_operation(
    max_poll_count=DEFAULT_MAX_POLL, fail=False, has_optimize_operation=True
):
    client = mock.Mock(spec=operations_client.OperationsClient)

    # Set up the polling
    side_effect = [RESTORE_TABLE_IN_PROGRESS_OPERATION_PROTO] * (max_poll_count - 1)
    finished_operation_metadata = bigtable_table_admin.RestoreTableMetadata()
    bigtable_table_admin.RestoreTableMetadata.copy_from(
        finished_operation_metadata, RESTORE_TABLE_OPERATION_METADATA
    )
    if has_optimize_operation:
        finished_operation_metadata.optimize_table_operation_name = (
            OPTIMIZE_RESTORED_TABLE_OPERATION_ID
        )

    if fail:
        final_operation_proto = make_operation_proto(
            name=RESTORE_TABLE_OPERATION_NAME,
            done=True,
            metadata=finished_operation_metadata,
            error=RESTORE_TABLE_OPERATION_FINISHED_ERROR,
        )
    else:
        final_operation_proto = make_operation_proto(
            name=RESTORE_TABLE_OPERATION_NAME,
            done=True,
            metadata=finished_operation_metadata,
            response=RESTORE_TABLE_OPERATION_FINISHED_RESPONSE,
        )
    side_effect.append(final_operation_proto)
    refresh = mock.Mock(spec=["__call__"], side_effect=side_effect)
    cancel = mock.Mock(spec=["__call__"])
    future = operation.Operation(
        RESTORE_TABLE_IN_PROGRESS_OPERATION_PROTO,
        refresh,
        cancel,
        result_type=table.Table,
        metadata_type=bigtable_table_admin.RestoreTableMetadata,
    )

    # Set up the optimize_restore_table_operation
    client.get_operation.side_effect = [OPTIMIZE_RESTORED_TABLE_OPERATION_PROTO]

    return restore_table.RestoreTableOperation(client, future)


def test_restore_table_operation_client_success_has_optimize():
    restore_table_operation = mock_restore_table_operation()

    restore_table_operation.result()
    optimize_restored_table_operation = (
        restore_table_operation.optimize_restored_table_operation()
    )

    assert isinstance(optimize_restored_table_operation, operation.Operation)
    assert (
        optimize_restored_table_operation._operation
        == OPTIMIZE_RESTORED_TABLE_OPERATION_PROTO
    )
    restore_table_operation._operations_client.get_operation.assert_called_with(
        name=OPTIMIZE_RESTORED_TABLE_OPERATION_ID
    )
    restore_table_operation._refresh.assert_has_calls([mock.call()] * DEFAULT_MAX_POLL)


def test_restore_table_operation_client_success_has_optimize_multiple_calls():
    restore_table_operation = mock_restore_table_operation()

    restore_table_operation.result()
    optimize_restored_table_operation = (
        restore_table_operation.optimize_restored_table_operation()
    )

    assert isinstance(optimize_restored_table_operation, operation.Operation)
    assert (
        optimize_restored_table_operation._operation
        == OPTIMIZE_RESTORED_TABLE_OPERATION_PROTO
    )
    restore_table_operation._operations_client.get_operation.assert_called_with(
        name=OPTIMIZE_RESTORED_TABLE_OPERATION_ID
    )
    restore_table_operation._refresh.assert_has_calls([mock.call()] * DEFAULT_MAX_POLL)

    restore_table_operation.optimize_restored_table_operation()
    restore_table_operation._refresh.assert_has_calls([mock.call()] * DEFAULT_MAX_POLL)


def test_restore_table_operation_success_has_optimize_call_before_done():
    restore_table_operation = mock_restore_table_operation()

    with pytest.raises(exceptions.GoogleAPIError):
        restore_table_operation.optimize_restored_table_operation()

    restore_table_operation._operations_client.get_operation.assert_not_called()


def test_restore_table_operation_client_success_only_cache_after_finishing():
    restore_table_operation = mock_restore_table_operation()

    with pytest.raises(exceptions.GoogleAPIError):
        restore_table_operation.optimize_restored_table_operation()

    restore_table_operation.result()
    optimize_restored_table_operation = (
        restore_table_operation.optimize_restored_table_operation()
    )

    assert isinstance(optimize_restored_table_operation, operation.Operation)
    assert (
        optimize_restored_table_operation._operation
        == OPTIMIZE_RESTORED_TABLE_OPERATION_PROTO
    )
    restore_table_operation._operations_client.get_operation.assert_called_with(
        name=OPTIMIZE_RESTORED_TABLE_OPERATION_ID
    )
    restore_table_operation._refresh.assert_has_calls([mock.call()] * DEFAULT_MAX_POLL)

    restore_table_operation.optimize_restored_table_operation()
    restore_table_operation._refresh.assert_has_calls([mock.call()] * DEFAULT_MAX_POLL)


def test_restore_table_operation_success_no_optimize():
    restore_table_operation = mock_restore_table_operation(has_optimize_operation=False)

    restore_table_operation.result()
    optimize_restored_table_operation = (
        restore_table_operation.optimize_restored_table_operation()
    )

    assert optimize_restored_table_operation is None
    restore_table_operation._operations_client.get_operation.assert_not_called()


def test_restore_table_operation_exception():
    restore_table_operation = mock_restore_table_operation(
        fail=True, has_optimize_operation=False
    )

    with pytest.raises(exceptions.GoogleAPICallError):
        restore_table_operation.result()

    optimize_restored_table_operation = (
        restore_table_operation.optimize_restored_table_operation()
    )

    assert optimize_restored_table_operation is None
    restore_table_operation._operations_client.get_operation.assert_not_called()
