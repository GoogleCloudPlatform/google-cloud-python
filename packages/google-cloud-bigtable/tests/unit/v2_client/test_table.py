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


import warnings

import mock
import pytest
from google.api_core.exceptions import DeadlineExceeded
from grpc import StatusCode

from google.cloud.bigtable.data.read_rows_query import ReadRowsQuery
from google.cloud.bigtable.row import DirectRow

from ._testing import _make_credentials

PROJECT_ID = "project-id"
INSTANCE_ID = "instance-id"
INSTANCE_NAME = "projects/" + PROJECT_ID + "/instances/" + INSTANCE_ID
CLUSTER_ID = "cluster-id"
CLUSTER_NAME = INSTANCE_NAME + "/clusters/" + CLUSTER_ID
TABLE_ID = "table-id"
TABLE_NAME = INSTANCE_NAME + "/tables/" + TABLE_ID
BACKUP_ID = "backup-id"
BACKUP_NAME = CLUSTER_NAME + "/backups/" + BACKUP_ID
ROW_KEY = b"row-key"
ROW_KEY_1 = b"row-key-1"
ROW_KEY_2 = b"row-key-2"
ROW_KEY_3 = b"row-key-3"
FAMILY_NAME = "family"
QUALIFIER = b"qualifier"
TIMESTAMP_MICROS = 100
VALUE = b"value"

# RPC Status Codes
SUCCESS = StatusCode.OK.value[0]
RETRYABLE_1 = StatusCode.DEADLINE_EXCEEDED.value[0]
RETRYABLE_2 = StatusCode.ABORTED.value[0]
RETRYABLE_3 = StatusCode.UNAVAILABLE.value[0]
RETRYABLES = (RETRYABLE_1, RETRYABLE_2, RETRYABLE_3)
NON_RETRYABLE = StatusCode.CANCELLED.value[0]
STATUS_INTERNAL = StatusCode.INTERNAL.value[0]
STATUS_UNKNOWN = StatusCode.UNKNOWN.value[0]


def _make_client(*args, **kwargs):
    from google.cloud.bigtable.client import Client

    return Client(*args, **kwargs)


def _make_table(*args, **kwargs):
    from google.cloud.bigtable.table import Table

    return Table(*args, **kwargs)


def test_table_constructor_defaults():
    from google.cloud.bigtable.client import Client

    client = mock.create_autospec(Client)
    instance = mock.Mock(
        _client=client,
        instance_id=INSTANCE_ID,
        spec=["_client", "instance_id"],
    )

    table = _make_table(TABLE_ID, instance)

    assert table.table_id == TABLE_ID
    assert table._instance is instance
    assert table.mutation_timeout is None
    assert table._app_profile_id is None
    assert table._table_impl is client._veneer_data_client.get_table.return_value
    client._veneer_data_client.get_table.assert_called_once_with(
        INSTANCE_ID,
        TABLE_ID,
        app_profile_id=None,
    )


def test_table_constructor_explicit():
    from google.cloud.bigtable.client import Client

    client = mock.create_autospec(Client)
    instance = mock.Mock(
        _client=client,
        instance_id=INSTANCE_ID,
        spec=["_client", "instance_id"],
    )

    mutation_timeout = 123
    app_profile_id = "profile-123"

    table = _make_table(
        TABLE_ID,
        instance,
        mutation_timeout=mutation_timeout,
        app_profile_id=app_profile_id,
    )

    assert table.table_id == TABLE_ID
    assert table._instance is instance
    assert table.mutation_timeout == mutation_timeout
    assert table._app_profile_id == app_profile_id
    assert table._table_impl is client._veneer_data_client.get_table.return_value
    client._veneer_data_client.get_table.assert_called_once_with(
        INSTANCE_ID,
        TABLE_ID,
        app_profile_id=app_profile_id,
    )


def test_table_name():
    table_data_client = mock.Mock(spec=["table_path"])
    _veneer_data_client = mock.Mock()
    client = mock.Mock(
        project=PROJECT_ID,
        table_data_client=table_data_client,
        _veneer_data_client=_veneer_data_client,
        spec=["project", "table_data_client", "_veneer_data_client"],
    )
    instance = mock.Mock(
        _client=client,
        instance_id=INSTANCE_ID,
        spec=["_client", "instance_id"],
    )

    table = _make_table(TABLE_ID, instance)

    assert table.name == table_data_client.table_path.return_value


def _table_row_methods_helper():
    client = _make_client(
        project="project-id", credentials=_make_credentials(), admin=True
    )
    instance = client.instance(instance_id=INSTANCE_ID)
    table = _make_table(TABLE_ID, instance)
    row_key = b"row_key"
    return table, row_key


def test_table_row_factory_direct():
    from google.cloud.bigtable.row import DirectRow

    table, row_key = _table_row_methods_helper()
    with warnings.catch_warnings(record=True) as warned:
        row = table.row(row_key)

    assert isinstance(row, DirectRow)
    assert row._row_key == row_key
    assert row._table == table

    assert len(warned) == 1
    assert warned[0].category is PendingDeprecationWarning


def test_table_row_factory_conditional():
    from google.cloud.bigtable.row import ConditionalRow

    table, row_key = _table_row_methods_helper()
    filter_ = object()

    with warnings.catch_warnings(record=True) as warned:
        row = table.row(row_key, filter_=filter_)

    assert isinstance(row, ConditionalRow)
    assert row._row_key == row_key
    assert row._table == table

    assert len(warned) == 1
    assert warned[0].category is PendingDeprecationWarning


def test_table_row_factory_append():
    from google.cloud.bigtable.row import AppendRow

    table, row_key = _table_row_methods_helper()

    with warnings.catch_warnings(record=True) as warned:
        row = table.row(row_key, append=True)

    assert isinstance(row, AppendRow)
    assert row._row_key == row_key
    assert row._table == table

    assert len(warned) == 1
    assert warned[0].category is PendingDeprecationWarning


def test_table_row_factory_failure():
    table, row_key = _table_row_methods_helper()

    with pytest.raises(ValueError):
        with warnings.catch_warnings(record=True) as warned:
            table.row(row_key, filter_=object(), append=True)

    assert len(warned) == 1
    assert warned[0].category is PendingDeprecationWarning


def test_table_direct_row():
    from google.cloud.bigtable.row import DirectRow

    table, row_key = _table_row_methods_helper()
    row = table.direct_row(row_key)

    assert isinstance(row, DirectRow)
    assert row._row_key == row_key
    assert row._table == table


def test_table_conditional_row():
    from google.cloud.bigtable.row import ConditionalRow

    table, row_key = _table_row_methods_helper()
    filter_ = object()
    row = table.conditional_row(row_key, filter_=filter_)

    assert isinstance(row, ConditionalRow)
    assert row._row_key == row_key
    assert row._table == table


def test_table_append_row():
    from google.cloud.bigtable.row import AppendRow

    table, row_key = _table_row_methods_helper()
    row = table.append_row(row_key)

    assert isinstance(row, AppendRow)
    assert row._row_key == row_key
    assert row._table == table


def test_table___eq__():
    credentials = _make_credentials()
    client = _make_client(project="project-id", credentials=credentials, admin=True)
    instance = client.instance(instance_id=INSTANCE_ID)
    table1 = _make_table(TABLE_ID, instance)
    table2 = _make_table(TABLE_ID, instance)
    assert table1 == table2


def test_table___eq__type_differ():
    credentials = _make_credentials()
    client = _make_client(project="project-id", credentials=credentials, admin=True)
    instance = client.instance(instance_id=INSTANCE_ID)
    table1 = _make_table(TABLE_ID, instance)
    table2 = object()
    assert not (table1 == table2)


def test_table___ne__same_value():
    credentials = _make_credentials()
    client = _make_client(project="project-id", credentials=credentials, admin=True)
    instance = client.instance(instance_id=INSTANCE_ID)
    table1 = _make_table(TABLE_ID, instance)
    table2 = _make_table(TABLE_ID, instance)
    assert not (table1 != table2)


def test_table___ne__():
    mock_instance = mock.Mock()
    table1 = _make_table("table_id1", mock_instance)
    table2 = _make_table("table_id2", mock_instance)
    assert table1 != table2


def _make_table_api():
    from google.cloud.bigtable_admin_v2.services.bigtable_table_admin import (
        client as bigtable_table_admin,
    )

    return mock.create_autospec(bigtable_table_admin.BaseBigtableTableAdminClient)


def _create_table_helper(split_keys=[], column_families={}):
    from google.cloud.bigtable.column_family import ColumnFamily
    from google.cloud.bigtable_admin_v2.types import (
        bigtable_table_admin as table_admin_messages_v2_pb2,
    )
    from google.cloud.bigtable_admin_v2.types import table as table_pb2

    credentials = _make_credentials()
    client = _make_client(project="project-id", credentials=credentials, admin=True)
    instance = client.instance(instance_id=INSTANCE_ID)
    table = _make_table(TABLE_ID, instance)

    table_api = client._table_admin_client = _make_table_api()

    table.create(column_families=column_families, initial_split_keys=split_keys)

    families = {
        id: ColumnFamily(id, table, rule).to_pb()
        for (id, rule) in column_families.items()
    }

    split = table_admin_messages_v2_pb2.CreateTableRequest.Split
    splits = [split(key=split_key) for split_key in split_keys]

    table_api.create_table.assert_called_once_with(
        request={
            "parent": INSTANCE_NAME,
            "table": table_pb2.Table(column_families=families),
            "table_id": TABLE_ID,
            "initial_splits": splits,
        }
    )


def test_table_create():
    _create_table_helper()


def test_table_create_with_families():
    from google.cloud.bigtable.column_family import MaxVersionsGCRule

    families = {"family": MaxVersionsGCRule(5)}
    _create_table_helper(column_families=families)


def test_table_create_with_split_keys():
    _create_table_helper(split_keys=[b"split1", b"split2", b"split3"])


def test_table_exists_hit():
    from google.cloud.bigtable import enums
    from google.cloud.bigtable_admin_v2.types import ListTablesResponse, Table

    credentials = _make_credentials()
    client = _make_client(project="project-id", credentials=credentials, admin=True)
    instance = client.instance(instance_id=INSTANCE_ID)
    table = instance.table(TABLE_ID)

    response_pb = ListTablesResponse(tables=[Table(name=TABLE_NAME)])
    table_api = client._table_admin_client = _make_table_api()
    table_api.get_table.return_value = response_pb

    assert table.exists()

    expected_request = {
        "name": table.name,
        "view": enums.Table.View.NAME_ONLY,
    }
    table_api.get_table.assert_called_once_with(request=expected_request)


def test_table_exists_miss():
    from google.api_core.exceptions import NotFound

    from google.cloud.bigtable import enums

    credentials = _make_credentials()
    client = _make_client(project="project-id", credentials=credentials, admin=True)
    instance = client.instance(instance_id=INSTANCE_ID)
    table = instance.table("nonesuch-table-id2")

    table_api = client._table_admin_client = _make_table_api()
    table_api.get_table.side_effect = NotFound("testing")

    assert not table.exists()

    expected_request = {
        "name": table.name,
        "view": enums.Table.View.NAME_ONLY,
    }
    table_api.get_table.assert_called_once_with(request=expected_request)


def test_table_exists_error():
    from google.api_core.exceptions import BadRequest

    from google.cloud.bigtable import enums

    credentials = _make_credentials()
    client = _make_client(project="project-id", credentials=credentials, admin=True)
    instance = client.instance(instance_id=INSTANCE_ID)

    table_api = client._table_admin_client = _make_table_api()
    table_api.get_table.side_effect = BadRequest("testing")

    table = instance.table(TABLE_ID)

    with pytest.raises(BadRequest):
        table.exists()

    expected_request = {
        "name": table.name,
        "view": enums.Table.View.NAME_ONLY,
    }
    table_api.get_table.assert_called_once_with(request=expected_request)


def test_table_delete():
    credentials = _make_credentials()
    client = _make_client(project="project-id", credentials=credentials, admin=True)
    instance = client.instance(instance_id=INSTANCE_ID)
    table = _make_table(TABLE_ID, instance)

    table_api = client._table_admin_client = _make_table_api()

    assert table.delete() is None

    table_api.delete_table.assert_called_once_with(request={"name": table.name})


def _table_list_column_families_helper():
    credentials = _make_credentials()
    client = _make_client(project="project-id", credentials=credentials, admin=True)
    instance = client.instance(instance_id=INSTANCE_ID)
    table = _make_table(TABLE_ID, instance)

    # Create response_pb
    COLUMN_FAMILY_ID = "foo"
    column_family = _ColumnFamilyPB()
    response_pb = _TablePB(column_families={COLUMN_FAMILY_ID: column_family})

    # Patch the stub used by the API method.
    table_api = client._table_admin_client = _make_table_api()
    table_api.get_table.return_value = response_pb

    # Create expected_result.
    expected_result = {COLUMN_FAMILY_ID: table.column_family(COLUMN_FAMILY_ID)}

    # Perform the method and check the result.
    result = table.list_column_families()

    assert result == expected_result

    table_api.get_table.assert_called_once_with(request={"name": table.name})


def test_table_list_column_families():
    _table_list_column_families_helper()


def test_table_get_cluster_states():
    from google.cloud.bigtable.enums import Table as enum_table
    from google.cloud.bigtable.table import ClusterState

    INITIALIZING = enum_table.ReplicationState.INITIALIZING
    PLANNED_MAINTENANCE = enum_table.ReplicationState.PLANNED_MAINTENANCE
    READY = enum_table.ReplicationState.READY

    credentials = _make_credentials()
    client = _make_client(project="project-id", credentials=credentials, admin=True)
    instance = client.instance(instance_id=INSTANCE_ID)
    table = _make_table(TABLE_ID, instance)

    response_pb = _TablePB(
        cluster_states={
            "cluster-id1": _ClusterStatePB(INITIALIZING),
            "cluster-id2": _ClusterStatePB(PLANNED_MAINTENANCE),
            "cluster-id3": _ClusterStatePB(READY),
        }
    )

    # Patch the stub used by the API method.
    table_api = client._table_admin_client = _make_table_api()
    table_api.get_table.return_value = response_pb

    # build expected result
    expected_result = {
        "cluster-id1": ClusterState(INITIALIZING),
        "cluster-id2": ClusterState(PLANNED_MAINTENANCE),
        "cluster-id3": ClusterState(READY),
    }

    # Perform the method and check the result.
    result = table.get_cluster_states()

    assert result == expected_result

    expected_request = {
        "name": table.name,
        "view": enum_table.View.REPLICATION_VIEW,
    }
    table_api.get_table.assert_called_once_with(request=expected_request)


def test_table_get_encryption_info():
    from google.rpc.code_pb2 import Code

    from google.cloud.bigtable.encryption_info import EncryptionInfo
    from google.cloud.bigtable.enums import EncryptionInfo as enum_crypto
    from google.cloud.bigtable.enums import Table as enum_table
    from google.cloud.bigtable.error import Status

    ENCRYPTION_TYPE_UNSPECIFIED = enum_crypto.EncryptionType.ENCRYPTION_TYPE_UNSPECIFIED
    GOOGLE_DEFAULT_ENCRYPTION = enum_crypto.EncryptionType.GOOGLE_DEFAULT_ENCRYPTION
    CUSTOMER_MANAGED_ENCRYPTION = enum_crypto.EncryptionType.CUSTOMER_MANAGED_ENCRYPTION

    credentials = _make_credentials()
    client = _make_client(project="project-id", credentials=credentials, admin=True)
    instance = client.instance(instance_id=INSTANCE_ID)
    table = _make_table(TABLE_ID, instance)

    response_pb = _TablePB(
        cluster_states={
            "cluster-id1": _ClusterStateEncryptionInfoPB(
                encryption_type=ENCRYPTION_TYPE_UNSPECIFIED,
                encryption_status=_StatusPB(Code.OK, "Status OK"),
            ),
            "cluster-id2": _ClusterStateEncryptionInfoPB(
                encryption_type=GOOGLE_DEFAULT_ENCRYPTION,
            ),
            "cluster-id3": _ClusterStateEncryptionInfoPB(
                encryption_type=CUSTOMER_MANAGED_ENCRYPTION,
                encryption_status=_StatusPB(
                    Code.UNKNOWN, "Key version is not yet known."
                ),
                kms_key_version="UNKNOWN",
            ),
        }
    )

    # Patch the stub used by the API method.
    table_api = client._table_admin_client = _make_table_api()
    table_api.get_table.return_value = response_pb

    # build expected result
    expected_result = {
        "cluster-id1": (
            EncryptionInfo(
                encryption_type=ENCRYPTION_TYPE_UNSPECIFIED,
                encryption_status=Status(_StatusPB(Code.OK, "Status OK")),
                kms_key_version="",
            ),
        ),
        "cluster-id2": (
            EncryptionInfo(
                encryption_type=GOOGLE_DEFAULT_ENCRYPTION,
                encryption_status=Status(_StatusPB(0, "")),
                kms_key_version="",
            ),
        ),
        "cluster-id3": (
            EncryptionInfo(
                encryption_type=CUSTOMER_MANAGED_ENCRYPTION,
                encryption_status=Status(
                    _StatusPB(Code.UNKNOWN, "Key version is not yet known.")
                ),
                kms_key_version="UNKNOWN",
            ),
        ),
    }

    # Perform the method and check the result.
    result = table.get_encryption_info()

    assert result == expected_result
    expected_request = {
        "name": table.name,
        "view": enum_table.View.ENCRYPTION_VIEW,
    }
    table_api.get_table.assert_called_once_with(request=expected_request)


def _make_data_api(client):
    from google.cloud.bigtable.data import BigtableDataClient

    data_client_mock = mock.create_autospec(BigtableDataClient)
    client._table_data_client = data_client_mock

    return data_client_mock


def _make_gapic_api(client):
    from google.cloud.bigtable_v2.services.bigtable import BigtableClient

    data_client_mock = _make_data_api(client)
    gapic_client_mock = mock.create_autospec(BigtableClient)
    data_client_mock._gapic_client = gapic_client_mock

    return gapic_client_mock


_DEFAULT_SENTINEL = object()


def _table_mutate_rows_helper(
    mutation_timeout=None,
    app_profile_id=None,
    retry=_DEFAULT_SENTINEL,
    timeout=None,
    expected_operation_timeout=None,
    expected_attempt_timeout=None,
    expected_retryable_errors=None,
):
    from google.api_core import exceptions as api_exceptions
    from google.rpc import status_pb2

    from google.cloud.bigtable.data.exceptions import (
        FailedMutationEntryError,
        MutationsExceptionGroup,
        RetryExceptionGroup,
    )
    from google.cloud.bigtable.data.mutations import RowMutationEntry
    from google.cloud.bigtable.table import DEFAULT_RETRY, RETRYABLE_MUTATION_ERRORS

    credentials = _make_credentials()
    client = _make_client(project="project-id", credentials=credentials, admin=True)
    instance = client.instance(instance_id=INSTANCE_ID)
    ctor_kwargs = {}

    if mutation_timeout is not None:
        ctor_kwargs["mutation_timeout"] = mutation_timeout

    if app_profile_id is not None:
        ctor_kwargs["app_profile_id"] = app_profile_id

    if expected_operation_timeout is None:
        expected_operation_timeout = DEFAULT_RETRY.deadline

    if expected_retryable_errors is None:
        expected_retryable_errors = RETRYABLE_MUTATION_ERRORS

    rows = [
        _MockRow(ROW_KEY),
        _MockRow(ROW_KEY_1),
        _MockRow(ROW_KEY_2),
        _MockRow(ROW_KEY_3),
    ]

    table = _make_table(TABLE_ID, instance, **ctor_kwargs)

    call_kwargs = {}

    if retry is not _DEFAULT_SENTINEL:
        call_kwargs["retry"] = retry

    if timeout is not None:
        call_kwargs["timeout"] = timeout

    with mock.patch.object(table._table_impl, "bulk_mutate_rows") as mutate_rows_mock:
        # First entry = success
        # Second entry = api error
        # Third entry = non-api error
        # Fourth entry = retryexceptiongroup
        mutate_rows_mock.side_effect = MutationsExceptionGroup(
            excs=[
                FailedMutationEntryError(
                    failed_idx=1,
                    failed_mutation_entry=RowMutationEntry(
                        ROW_KEY_1, [mock.MagicMock()]
                    ),
                    cause=api_exceptions.InternalServerError("Failure"),
                ),
                FailedMutationEntryError(
                    failed_idx=2,
                    failed_mutation_entry=RowMutationEntry(
                        ROW_KEY_2, [mock.MagicMock()]
                    ),
                    cause=ValueError("Invalid argument"),
                ),
                FailedMutationEntryError(
                    failed_idx=3,
                    failed_mutation_entry=RowMutationEntry(
                        ROW_KEY_3, [mock.MagicMock()]
                    ),
                    cause=RetryExceptionGroup(
                        [
                            api_exceptions.InternalServerError("First failure"),
                            OSError("Out of memory"),
                            api_exceptions.InternalServerError("Final failure"),
                        ]
                    ),
                ),
            ],
            total_entries=4,
        )

        statuses = table.mutate_rows(rows, **call_kwargs)

    assert statuses == [
        status_pb2.Status(
            code=SUCCESS,
            message="",
        ),
        status_pb2.Status(
            code=STATUS_INTERNAL,
            message="Failure",
        ),
        status_pb2.Status(
            code=STATUS_UNKNOWN,
            message="Invalid argument",
        ),
        status_pb2.Status(
            code=STATUS_INTERNAL,
            message="Final failure",
        ),
    ]

    # Check all call args other than mutation_entries
    mutate_rows_mock.assert_called_once_with(
        mock.ANY,
        operation_timeout=expected_operation_timeout,
        attempt_timeout=expected_attempt_timeout,
        retryable_errors=expected_retryable_errors,
    )

    # Check that mutation entries are in order
    mutation_entries = mutate_rows_mock.call_args.args[0]
    mutation_entry_keys = [row.row_key for row in mutation_entries]
    assert mutation_entry_keys == [
        ROW_KEY,
        ROW_KEY_1,
        ROW_KEY_2,
        ROW_KEY_3,
    ]


def test_table_mutate_rows_w_default_mutation_timeout_app_profile_id():
    _table_mutate_rows_helper()


def test_table_mutate_rows_w_mutation_timeout():
    mutation_timeout = 50
    _table_mutate_rows_helper(
        mutation_timeout=mutation_timeout, expected_attempt_timeout=mutation_timeout
    )


def test_table_mutate_rows_w_app_profile_id():
    app_profile_id = "profile-123"
    _table_mutate_rows_helper(app_profile_id=app_profile_id)


def test_table_mutate_rows_w_retry():
    deadline = 456.0
    retry = mock.Mock()
    retry.deadline = deadline
    _table_mutate_rows_helper(retry=retry, expected_operation_timeout=deadline)


def test_table_mutate_rows_w_zero_deadline_retry():
    from google.cloud.bigtable.data._helpers import TABLE_DEFAULT

    deadline = 0.0
    retry = mock.Mock()
    retry.deadline = deadline
    _table_mutate_rows_helper(
        retry=retry,
        expected_operation_timeout=TABLE_DEFAULT.MUTATE_ROWS,
        expected_retryable_errors=[],
    )


def test_table_mutate_rows_w_none_deadline_retry():
    from google.cloud.bigtable.data._helpers import TABLE_DEFAULT

    deadline = None
    retry = mock.Mock()
    retry.deadline = deadline
    _table_mutate_rows_helper(
        retry=retry, expected_operation_timeout=TABLE_DEFAULT.MUTATE_ROWS
    )


def test_table_mutate_rows_w_retry_none():
    from google.cloud.bigtable.data._helpers import TABLE_DEFAULT

    _table_mutate_rows_helper(
        retry=None,
        expected_operation_timeout=TABLE_DEFAULT.MUTATE_ROWS,
        expected_retryable_errors=[],
    )


def _make_mutate_rows_table_and_rows(row_keys):
    """Build a table and real ``DirectRow`` instances holding mutations.

    ``_MockRow`` fakes out ``_get_mutations``, so it cannot observe clearing.
    """
    credentials = _make_credentials()
    client = _make_client(project="project-id", credentials=credentials, admin=True)
    instance = client.instance(instance_id=INSTANCE_ID)
    table = _make_table(TABLE_ID, instance)

    rows = []
    for row_key in row_keys:
        row = DirectRow(row_key=row_key)
        row.set_cell(FAMILY_NAME, QUALIFIER, VALUE, timestamp=None)
        rows.append(row)

    return table, rows


def test_table_mutate_rows_clears_succeeded_rows_only():
    """Succeeded rows are cleaned up, failed rows keep their mutations so that
    they can be applied again separately."""
    from google.api_core import exceptions as api_exceptions

    from google.cloud.bigtable.data.exceptions import (
        FailedMutationEntryError,
        MutationsExceptionGroup,
    )
    from google.cloud.bigtable.data.mutations import RowMutationEntry

    table, rows = _make_mutate_rows_table_and_rows([ROW_KEY, ROW_KEY_1])

    with mock.patch.object(table._table_impl, "bulk_mutate_rows") as bulk_mock:
        bulk_mock.side_effect = MutationsExceptionGroup(
            excs=[
                FailedMutationEntryError(
                    failed_idx=1,
                    failed_mutation_entry=RowMutationEntry(
                        ROW_KEY_1, [mock.MagicMock()]
                    ),
                    cause=api_exceptions.InternalServerError("Failure"),
                )
            ],
            total_entries=2,
        )
        statuses = table.mutate_rows(rows)

    assert [status.code for status in statuses] == [SUCCESS, STATUS_INTERNAL]
    assert rows[0]._get_mutations() == []
    assert len(rows[1]._get_mutations()) == 1


def test_table_mutate_rows_clears_all_rows_on_success():
    table, rows = _make_mutate_rows_table_and_rows([ROW_KEY, ROW_KEY_1])

    with mock.patch.object(table._table_impl, "bulk_mutate_rows"):
        statuses = table.mutate_rows(rows)

    assert [status.code for status in statuses] == [SUCCESS, SUCCESS]
    assert all(row._get_mutations() == [] for row in rows)


def test_table_mutate_rows_keeps_mutations_when_call_raises():
    """An error that is not reported per entry leaves every row untouched."""
    table, rows = _make_mutate_rows_table_and_rows([ROW_KEY, ROW_KEY_1])

    with mock.patch.object(table._table_impl, "bulk_mutate_rows") as bulk_mock:
        bulk_mock.side_effect = DeadlineExceeded("deadline exceeded")
        with pytest.raises(DeadlineExceeded):
            table.mutate_rows(rows)

    assert all(len(row._get_mutations()) == 1 for row in rows)


def test_table_mutate_rows_w_iterator():
    """``rows`` may be any iterable, not just a sequence."""
    table, rows = _make_mutate_rows_table_and_rows([ROW_KEY, ROW_KEY_1])

    with mock.patch.object(table._table_impl, "bulk_mutate_rows"):
        statuses = table.mutate_rows(iter(rows))

    assert [status.code for status in statuses] == [SUCCESS, SUCCESS]
    assert all(row._get_mutations() == [] for row in rows)


def test_table_mutate_rows_wrong_row_type():
    import pytest

    from google.cloud.bigtable.row import ConditionalRow

    credentials = _make_credentials()
    client = _make_client(project="project-id", credentials=credentials, admin=True)
    instance = client.instance(instance_id=INSTANCE_ID)
    table = _make_table(TABLE_ID, instance)

    row = ConditionalRow(row_key=b"row_key", table=table, filter_=None)
    with pytest.raises(
        TypeError,
        match="Bulk processing can not be applied for conditional or append mutations.",
    ):
        table.mutate_rows([row])


def test_table_mutate_rows_table_mismatch():
    import pytest

    from google.cloud.bigtable.row import DirectRow
    from google.cloud.bigtable.table import TableMismatchError

    credentials = _make_credentials()
    client = _make_client(project="project-id", credentials=credentials, admin=True)
    instance = client.instance(instance_id=INSTANCE_ID)
    table = _make_table(TABLE_ID, instance)
    other_table = _make_table("other-table", instance)

    row = DirectRow(row_key=b"row_key", table=other_table)
    with pytest.raises(
        TableMismatchError,
        match=r"Row b'row_key' is a part of %s table\. Current table: %s"
        % (other_table.name, table.name),
    ):
        table.mutate_rows([row])


def test_table_mutate_rows_w_timeout_arg():
    timeout = 40
    _table_mutate_rows_helper(timeout=timeout, expected_attempt_timeout=timeout)


def test_table_mutate_rows_w_mutation_timeout_and_timeout_arg():
    mutation_timeout = 50
    timeout = 100
    _table_mutate_rows_helper(
        mutation_timeout=mutation_timeout,
        timeout=timeout,
        expected_attempt_timeout=timeout,
    )


def test_table_read_rows():
    from google.cloud.bigtable.data._helpers import TABLE_DEFAULT
    from google.cloud.bigtable.data.read_rows_query import ReadRowsQuery
    from google.cloud.bigtable.data.row import Cell, Row
    from google.cloud.bigtable.row import Cell as PartialRowDataCell
    from google.cloud.bigtable.row import PartialRowData
    from google.cloud.bigtable.row_data import DEFAULT_RETRY_READ_ROWS, PartialRowsData
    from google.cloud.bigtable.row_set import RowRange

    credentials = _make_credentials()
    client = _make_client(project="project-id", credentials=credentials, admin=True)
    instance = client.instance(instance_id=INSTANCE_ID)
    app_profile_id = "app-profile-id"
    table = _make_table(TABLE_ID, instance, app_profile_id=app_profile_id)

    # Create read_rows return value
    rows = [
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
            key=ROW_KEY_1,
            cells=[
                Cell(
                    value=VALUE,
                    row_key=ROW_KEY_1,
                    family=FAMILY_NAME,
                    qualifier=QUALIFIER,
                    timestamp_micros=TIMESTAMP_MICROS,
                )
            ],
        ),
    ]
    generator = (r for r in rows)

    # Create expected result.
    expected_result = PartialRowsData._from_generator(generator)

    # Perform the method and check the result.
    start_key = b"begin-key"
    end_key = b"end-key"
    filter_obj = object()
    limit = 22
    retry = DEFAULT_RETRY_READ_ROWS
    with mock.patch.object(table._table_impl, "read_rows_stream") as read_rows_mock:
        read_rows_mock.return_value = generator
        result = table.read_rows(
            start_key=start_key,
            end_key=end_key,
            filter_=filter_obj,
            limit=limit,
            retry=retry,
        )

    assert result.rows == expected_result.rows
    assert result._generator == expected_result._generator

    expected_read_rows_query = ReadRowsQuery(
        row_ranges=RowRange(start_key=start_key, end_key=end_key),
        row_filter=filter_obj,
        limit=limit,
    )

    read_rows_mock.assert_called_once_with(
        expected_read_rows_query,
        operation_timeout=TABLE_DEFAULT.READ_ROWS,
        attempt_timeout=retry.deadline,
        retryable_errors=TABLE_DEFAULT.READ_ROWS,
    )

    # Test that the correct rows get returned.
    partial_row_data = PartialRowData(ROW_KEY)
    partial_row_data._cells = {
        FAMILY_NAME: {
            QUALIFIER: [
                PartialRowDataCell(value=VALUE, timestamp_micros=TIMESTAMP_MICROS),
            ],
        },
    }
    partial_row_data_1 = PartialRowData(ROW_KEY_1)
    partial_row_data_1._cells = {
        FAMILY_NAME: {
            QUALIFIER: [
                PartialRowDataCell(value=VALUE, timestamp_micros=TIMESTAMP_MICROS),
            ],
        },
    }
    expected_row_data = [partial_row_data, partial_row_data_1]

    row_data = list(result)
    assert row_data == expected_row_data


def test_table_sample_row_keys():
    credentials = _make_credentials()
    client = _make_client(project="project-id", credentials=credentials, admin=True)
    instance = client.instance(instance_id=INSTANCE_ID)
    table = _make_table(TABLE_ID, instance)
    response_iterator = object()

    gapic_api = _make_gapic_api(client)
    gapic_api.sample_row_keys.return_value = [response_iterator]

    result = table.sample_row_keys()

    assert result[0] == response_iterator


def test_table_truncate():
    credentials = _make_credentials()
    client = _make_client(project="project-id", credentials=credentials, admin=True)
    instance = client.instance(instance_id=INSTANCE_ID)
    table = _make_table(TABLE_ID, instance)
    table_api = client._table_admin_client = _make_table_api()

    with mock.patch("google.cloud.bigtable.table.Table.name", new=TABLE_NAME):
        result = table.truncate()

    assert result is None

    table_api.drop_row_range.assert_called_once_with(
        request={"name": TABLE_NAME, "delete_all_data_from_table": True}
    )


def test_table_truncate_w_timeout():
    credentials = _make_credentials()
    client = _make_client(project="project-id", credentials=credentials, admin=True)
    instance = client.instance(instance_id=INSTANCE_ID)
    table = _make_table(TABLE_ID, instance)
    table_api = client._table_admin_client = _make_table_api()

    timeout = 120
    result = table.truncate(timeout=timeout)

    assert result is None

    table_api.drop_row_range.assert_called_once_with(
        request={"name": TABLE_NAME, "delete_all_data_from_table": True},
        timeout=120,
    )


def test_table_drop_by_prefix():
    credentials = _make_credentials()
    client = _make_client(project="project-id", credentials=credentials, admin=True)
    instance = client.instance(instance_id=INSTANCE_ID)
    table = _make_table(TABLE_ID, instance)
    table_api = client._table_admin_client = _make_table_api()

    row_key_prefix = b"row-key-prefix"

    result = table.drop_by_prefix(row_key_prefix=row_key_prefix)

    assert result is None

    table_api.drop_row_range.assert_called_once_with(
        request={"name": TABLE_NAME, "row_key_prefix": row_key_prefix},
    )


def test_table_drop_by_prefix_w_timeout():
    credentials = _make_credentials()
    client = _make_client(project="project-id", credentials=credentials, admin=True)
    instance = client.instance(instance_id=INSTANCE_ID)
    table = _make_table(TABLE_ID, instance)
    table_api = client._table_admin_client = _make_table_api()

    row_key_prefix = b"row-key-prefix"

    timeout = 120
    result = table.drop_by_prefix(row_key_prefix=row_key_prefix, timeout=timeout)

    assert result is None

    table_api.drop_row_range.assert_called_once_with(
        request={"name": TABLE_NAME, "row_key_prefix": row_key_prefix},
        timeout=120,
    )


def test_table_mutations_batcher_factory():
    flush_count = 100
    max_row_bytes = 1000
    table = _make_table(TABLE_ID, mock.Mock())
    mutation_batcher = table.mutations_batcher(
        flush_count=flush_count, max_row_bytes=max_row_bytes
    )

    assert mutation_batcher.table.table_id == TABLE_ID
    assert mutation_batcher._batcher_kwargs["flush_limit_mutation_count"] == flush_count
    assert mutation_batcher._batcher_kwargs["flush_limit_bytes"] == max_row_bytes


def test_table_get_iam_policy():
    from google.iam.v1 import policy_pb2

    from google.cloud.bigtable.policy import BIGTABLE_ADMIN_ROLE

    credentials = _make_credentials()
    client = _make_client(project="project-id", credentials=credentials, admin=True)
    instance = client.instance(instance_id=INSTANCE_ID)
    table = _make_table(TABLE_ID, instance)

    version = 1
    etag = b"etag_v1"
    members = ["serviceAccount:service_acc1@test.com", "user:user1@test.com"]
    bindings = [{"role": BIGTABLE_ADMIN_ROLE, "members": members}]
    iam_policy = policy_pb2.Policy(version=version, etag=etag, bindings=bindings)

    table_api = client._table_admin_client = _make_table_api()
    table_api.get_iam_policy.return_value = iam_policy

    result = table.get_iam_policy()

    assert result.version == version
    assert result.etag == etag
    admins = result.bigtable_admins
    assert len(admins) == len(members)

    for found, expected in zip(sorted(admins), sorted(members)):
        assert found == expected

    table_api.get_iam_policy.assert_called_once_with(request={"resource": table.name})


def test_table_set_iam_policy():
    from google.iam.v1 import policy_pb2

    from google.cloud.bigtable.policy import BIGTABLE_ADMIN_ROLE, Policy

    credentials = _make_credentials()
    client = _make_client(project="project-id", credentials=credentials, admin=True)
    instance = client.instance(instance_id=INSTANCE_ID)
    table = _make_table(TABLE_ID, instance)

    version = 1
    etag = b"etag_v1"
    members = ["serviceAccount:service_acc1@test.com", "user:user1@test.com"]
    bindings = [{"role": BIGTABLE_ADMIN_ROLE, "members": sorted(members)}]
    iam_policy_pb = policy_pb2.Policy(version=version, etag=etag, bindings=bindings)

    table_api = client._table_admin_client = _make_table_api()
    table_api.set_iam_policy.return_value = iam_policy_pb

    iam_policy = Policy(etag=etag, version=version)
    iam_policy[BIGTABLE_ADMIN_ROLE] = [
        Policy.user("user1@test.com"),
        Policy.service_account("service_acc1@test.com"),
    ]

    result = table.set_iam_policy(iam_policy)

    assert result.version == version
    assert result.etag == etag
    admins = result.bigtable_admins
    assert len(admins) == len(members)

    for found, expected in zip(sorted(admins), sorted(members)):
        assert found == expected

    table_api.set_iam_policy.assert_called_once_with(
        request={"resource": table.name, "policy": iam_policy_pb}
    )


def test_table_test_iam_permissions():
    from google.iam.v1 import iam_policy_pb2

    credentials = _make_credentials()
    client = _make_client(project="project-id", credentials=credentials, admin=True)
    instance = client.instance(instance_id=INSTANCE_ID)
    table = _make_table(TABLE_ID, instance)

    permissions = ["bigtable.tables.mutateRows", "bigtable.tables.readRows"]

    response = iam_policy_pb2.TestIamPermissionsResponse(permissions=permissions)

    table_api = client._table_admin_client = _make_table_api()
    table_api.test_iam_permissions.return_value = response

    result = table.test_iam_permissions(permissions)

    assert result == permissions

    table_api.test_iam_permissions.assert_called_once_with(
        request={"resource": table.name, "permissions": permissions}
    )


def test_table_backup_factory_defaults():
    from google.cloud.bigtable.backup import Backup
    from google.cloud.bigtable.client import Client
    from google.cloud.bigtable.instance import Instance

    instance = Instance(INSTANCE_ID, mock.create_autospec(Client))
    table = _make_table(TABLE_ID, instance)
    backup = table.backup(BACKUP_ID)

    assert isinstance(backup, Backup)
    assert backup.backup_id == BACKUP_ID
    assert backup._instance is instance
    assert backup._cluster is None
    assert backup.table_id == TABLE_ID
    assert backup._expire_time is None

    assert backup._parent is None
    assert backup._source_table is None
    assert backup._start_time is None
    assert backup._end_time is None
    assert backup._size_bytes is None
    assert backup._state is None


def test_table_backup_factory_non_defaults():
    import datetime

    from google.cloud.bigtable.backup import Backup
    from google.cloud.bigtable.client import Client
    from google.cloud.bigtable.instance import Instance

    instance = Instance(INSTANCE_ID, mock.create_autospec(Client))
    table = _make_table(TABLE_ID, instance)
    timestamp = datetime.datetime.now(datetime.timezone.utc)
    backup = table.backup(
        BACKUP_ID,
        cluster_id=CLUSTER_ID,
        expire_time=timestamp,
    )

    assert isinstance(backup, Backup)
    assert backup.backup_id == BACKUP_ID
    assert backup._instance is instance

    assert backup.backup_id == BACKUP_ID
    assert backup._cluster is CLUSTER_ID
    assert backup.table_id == TABLE_ID
    assert backup._expire_time == timestamp
    assert backup._start_time is None
    assert backup._end_time is None
    assert backup._size_bytes is None
    assert backup._state is None


def _table_list_backups_helper(cluster_id=None, filter_=None, **kwargs):
    from google.cloud.bigtable.backup import Backup
    from google.cloud.bigtable_admin_v2.types import (
        Backup as backup_pb,
    )
    from google.cloud.bigtable_admin_v2.types import (
        bigtable_table_admin,
    )

    client = _make_client(
        project=PROJECT_ID, credentials=_make_credentials(), admin=True
    )
    instance = client.instance(instance_id=INSTANCE_ID)
    table = _make_table(TABLE_ID, instance)

    parent = INSTANCE_NAME + "/clusters/cluster"
    backups_pb = bigtable_table_admin.ListBackupsResponse(
        backups=[
            backup_pb(name=parent + "/backups/op1"),
            backup_pb(name=parent + "/backups/op2"),
            backup_pb(name=parent + "/backups/op3"),
        ]
    )

    table_api = client._table_admin_client = _make_table_api()
    table_api.list_backups.return_value = backups_pb

    backups_filter = "source_table:{}".format(TABLE_NAME)
    if filter_:
        backups_filter = "({}) AND ({})".format(backups_filter, filter_)

    backups = table.list_backups(cluster_id=cluster_id, filter_=filter_, **kwargs)

    for backup in backups:
        assert isinstance(backup, Backup)

    if not cluster_id:
        cluster_id = "-"
    parent = "{}/clusters/{}".format(INSTANCE_NAME, cluster_id)

    order_by = None
    page_size = 0
    if "order_by" in kwargs:
        order_by = kwargs["order_by"]

    if "page_size" in kwargs:
        page_size = kwargs["page_size"]

    table_api.list_backups.assert_called_once_with(
        request={
            "parent": parent,
            "filter": backups_filter,
            "order_by": order_by,
            "page_size": page_size,
        }
    )


def test_table_list_backups_defaults():
    _table_list_backups_helper()


def test_table_list_backups_w_options():
    _table_list_backups_helper(
        cluster_id="cluster", filter_="filter", order_by="order_by", page_size=10
    )


def _table_restore_helper(backup_name=None):
    from google.cloud.bigtable.instance import Instance

    op_future = object()
    credentials = _make_credentials()
    client = _make_client(project=PROJECT_ID, credentials=credentials, admin=True)

    instance = Instance(INSTANCE_ID, client=client)
    table = _make_table(TABLE_ID, instance)

    table_api = client._table_admin_client = _make_table_api()
    table_api._restore_table.return_value = op_future

    if backup_name:
        future = table.restore(TABLE_ID, backup_name=BACKUP_NAME)
    else:
        future = table.restore(TABLE_ID, CLUSTER_ID, BACKUP_ID)

    assert future is op_future

    expected_request = {
        "parent": INSTANCE_NAME,
        "table_id": TABLE_ID,
        "backup": BACKUP_NAME,
    }
    table_api._restore_table.assert_called_once_with(request=expected_request)


def test_table_restore_table_w_backup_id():
    _table_restore_helper()


def test_table_restore_table_w_backup_name():
    _table_restore_helper(backup_name=BACKUP_NAME)


def test__create_row_request_row_range_row_set_conflict():
    from google.cloud.bigtable.table import _create_row_request

    with pytest.raises(ValueError):
        _create_row_request(None, end_key=object(), row_set=object())


def test__create_row_request_row_range_start_key():
    from google.cloud.bigtable.data.read_rows_query import RowRange
    from google.cloud.bigtable.table import _create_row_request

    start_key = b"begin_key"
    result = _create_row_request(start_key=start_key)
    expected_result = ReadRowsQuery(row_ranges=RowRange(start_key=start_key))
    assert result == expected_result


def test__create_row_request_row_range_end_key():
    from google.cloud.bigtable.data.read_rows_query import RowRange
    from google.cloud.bigtable.table import _create_row_request

    end_key = b"begin_key"
    result = _create_row_request(end_key=end_key)
    expected_result = ReadRowsQuery(row_ranges=RowRange(end_key=end_key))
    assert result == expected_result


def test__create_row_request_row_range_both_keys():
    from google.cloud.bigtable.data.read_rows_query import RowRange
    from google.cloud.bigtable.table import _create_row_request

    start_key = b"begin_key"
    end_key = b"end_key"
    result = _create_row_request(start_key=start_key, end_key=end_key)
    expected_result = ReadRowsQuery(
        row_ranges=RowRange(start_key=start_key, end_key=end_key)
    )
    assert result == expected_result


def test__create_row_request_row_range_both_keys_inclusive():
    from google.cloud.bigtable.data.read_rows_query import RowRange
    from google.cloud.bigtable.table import _create_row_request

    start_key = b"begin_key"
    end_key = b"end_key"
    result = _create_row_request(
        start_key=start_key, end_key=end_key, end_inclusive=True
    )
    expected_result = ReadRowsQuery(
        row_ranges=RowRange(start_key=start_key, end_key=end_key, end_is_inclusive=True)
    )
    assert result == expected_result


def test__create_row_request_with_filter():
    from google.cloud.bigtable.row_filters import RowSampleFilter
    from google.cloud.bigtable.table import _create_row_request

    row_filter = RowSampleFilter(0.33)
    result = _create_row_request(filter_=row_filter)
    expected_result = ReadRowsQuery(row_filter=row_filter)
    assert result == expected_result


def test__create_row_request_with_limit():
    from google.cloud.bigtable.table import _create_row_request

    limit = 1337
    result = _create_row_request(limit=limit)
    expected_result = ReadRowsQuery(limit=limit)
    assert result == expected_result


def test__create_row_request_with_row_set():
    from google.cloud.bigtable.row_set import RowSet
    from google.cloud.bigtable.table import _create_row_request

    row_set = RowSet()
    result = _create_row_request(row_set=row_set)
    expected_result = ReadRowsQuery()
    assert result == expected_result


def test_cluster_state___eq__():
    from google.cloud.bigtable.enums import Table as enum_table
    from google.cloud.bigtable.table import ClusterState

    READY = enum_table.ReplicationState.READY
    state1 = ClusterState(READY)
    state2 = ClusterState(READY)
    assert state1 == state2


def test_cluster_state___eq__type_differ():
    from google.cloud.bigtable.enums import Table as enum_table
    from google.cloud.bigtable.table import ClusterState

    READY = enum_table.ReplicationState.READY
    state1 = ClusterState(READY)
    state2 = object()
    assert not (state1 == state2)


def test_cluster_state___ne__same_value():
    from google.cloud.bigtable.enums import Table as enum_table
    from google.cloud.bigtable.table import ClusterState

    READY = enum_table.ReplicationState.READY
    state1 = ClusterState(READY)
    state2 = ClusterState(READY)
    assert not (state1 != state2)


def test_cluster_state___ne__():
    from google.cloud.bigtable.enums import Table as enum_table
    from google.cloud.bigtable.table import ClusterState

    READY = enum_table.ReplicationState.READY
    INITIALIZING = enum_table.ReplicationState.INITIALIZING
    state1 = ClusterState(READY)
    state2 = ClusterState(INITIALIZING)
    assert state1 != state2


def test_cluster_state__repr__():
    from google.cloud.bigtable.enums import Table as enum_table
    from google.cloud.bigtable.table import ClusterState

    STATE_NOT_KNOWN = enum_table.ReplicationState.STATE_NOT_KNOWN
    INITIALIZING = enum_table.ReplicationState.INITIALIZING
    PLANNED_MAINTENANCE = enum_table.ReplicationState.PLANNED_MAINTENANCE
    UNPLANNED_MAINTENANCE = enum_table.ReplicationState.UNPLANNED_MAINTENANCE
    READY = enum_table.ReplicationState.READY

    replication_dict = {
        STATE_NOT_KNOWN: "STATE_NOT_KNOWN",
        INITIALIZING: "INITIALIZING",
        PLANNED_MAINTENANCE: "PLANNED_MAINTENANCE",
        UNPLANNED_MAINTENANCE: "UNPLANNED_MAINTENANCE",
        READY: "READY",
    }

    assert str(ClusterState(STATE_NOT_KNOWN)) == replication_dict[STATE_NOT_KNOWN]
    assert str(ClusterState(INITIALIZING)) == replication_dict[INITIALIZING]
    assert (
        str(ClusterState(PLANNED_MAINTENANCE)) == replication_dict[PLANNED_MAINTENANCE]
    )
    assert (
        str(ClusterState(UNPLANNED_MAINTENANCE))
        == replication_dict[UNPLANNED_MAINTENANCE]
    )
    assert str(ClusterState(READY)) == replication_dict[READY]

    assert ClusterState(STATE_NOT_KNOWN).replication_state == STATE_NOT_KNOWN
    assert ClusterState(INITIALIZING).replication_state == INITIALIZING
    assert ClusterState(PLANNED_MAINTENANCE).replication_state == PLANNED_MAINTENANCE
    assert (
        ClusterState(UNPLANNED_MAINTENANCE).replication_state == UNPLANNED_MAINTENANCE
    )
    assert ClusterState(READY).replication_state == READY


def _ReadRowsResponseCellChunkPB(*args, **kw):
    from google.cloud.bigtable_v2.types import bigtable as messages_v2_pb2

    family_name = kw.pop("family_name")
    qualifier = kw.pop("qualifier")
    message = messages_v2_pb2.ReadRowsResponse.CellChunk(*args, **kw)
    message.family_name = family_name
    message.qualifier = qualifier
    return message


def _ReadRowsResponsePB(*args, **kw):
    from google.cloud.bigtable_v2.types import bigtable as messages_v2_pb2

    return messages_v2_pb2.ReadRowsResponse(*args, **kw)


class _MockRow(DirectRow):
    def __init__(self, row_key, table=None):
        super().__init__(row_key=row_key, table=table)

    def _get_mutations(self):
        return [mock.MagicMock()]


class _MockReadRowsIterator(object):
    def __init__(self, *values):
        self.iter_values = iter(values)

    def next(self):
        return next(self.iter_values)

    __next__ = next


class _MockFailureIterator_1(object):
    def next(self):
        raise DeadlineExceeded("Failed to read from server")

    def __init__(self, last_scanned_row_key=""):
        self.last_scanned_row_key = last_scanned_row_key

    __next__ = next


class _MockFailureIterator_2(object):
    def __init__(self, *values):
        self.iter_values = values[0]
        self.calls = 0
        self.last_scanned_row_key = ""

    def next(self):
        self.calls += 1
        if self.calls == 1:
            return self.iter_values[0]
        else:
            raise DeadlineExceeded("Failed to read from server")

    __next__ = next


def _ReadRowsResponseV2(chunks, last_scanned_row_key=b""):
    from google.cloud.bigtable_v2.types import bigtable as messages_v2_pb2

    return messages_v2_pb2.ReadRowsResponse(
        chunks=chunks, last_scanned_row_key=last_scanned_row_key
    )


def _TablePB(*args, **kw):
    from google.cloud.bigtable_admin_v2.types import table as table_v2_pb2

    return table_v2_pb2.Table(*args, **kw)


def _ColumnFamilyPB(*args, **kw):
    from google.cloud.bigtable_admin_v2.types import table as table_v2_pb2

    return table_v2_pb2.ColumnFamily(*args, **kw)


def _ClusterStatePB(replication_state):
    from google.cloud.bigtable_admin_v2.types import table as table_v2_pb2

    return table_v2_pb2.Table.ClusterState(replication_state=replication_state)


def _ClusterStateEncryptionInfoPB(
    encryption_type, encryption_status=None, kms_key_version=None
):
    from google.cloud.bigtable_admin_v2.types import table as table_v2_pb2

    return table_v2_pb2.Table.ClusterState(
        encryption_info=(
            table_v2_pb2.EncryptionInfo(
                encryption_type=encryption_type,
                encryption_status=encryption_status,
                kms_key_version=kms_key_version,
            ),
        )
    )


def _StatusPB(code, message):
    from google.rpc import status_pb2

    status_pb = status_pb2.Status()
    status_pb.code = code
    status_pb.message = message

    return status_pb


def _read_rows_retry_exception(exc):
    return isinstance(exc, DeadlineExceeded)
