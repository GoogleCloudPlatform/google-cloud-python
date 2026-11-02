# Copyright 2020 Google LLC All rights reserved.
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


import datetime

import mock
import pytest

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

ALT_INSTANCE = "other-instance-id"
ALT_INSTANCE_NAME = "projects/" + PROJECT_ID + "/instances/" + ALT_INSTANCE
ALT_CLUSTER_NAME = ALT_INSTANCE_NAME + "/clusters/" + CLUSTER_ID
ALT_BACKUP_NAME = ALT_CLUSTER_NAME + "/backups/" + BACKUP_ID


def _make_timestamp():
    return datetime.datetime.now(datetime.timezone.utc)


def _make_table_admin_client():
    from google.cloud.bigtable_admin_v2 import BaseBigtableTableAdminClient

    return mock.create_autospec(BaseBigtableTableAdminClient, instance=True)


def _make_backup(*args, **kwargs):
    from google.cloud.bigtable.backup import Backup

    return Backup(*args, **kwargs)


def test_backup_constructor_defaults():
    instance = _Instance(INSTANCE_NAME)
    backup = _make_backup(BACKUP_ID, instance)

    assert backup.backup_id == BACKUP_ID
    assert backup._instance is instance
    assert backup._cluster is None
    assert backup.table_id is None
    assert backup._expire_time is None

    assert backup._parent is None
    assert backup._source_table is None
    assert backup._start_time is None
    assert backup._end_time is None
    assert backup._size_bytes is None
    assert backup._state is None
    assert backup._encryption_info is None


def test_backup_constructor_explicit():
    instance = _Instance(INSTANCE_NAME)
    expire_time = _make_timestamp()

    backup = _make_backup(
        BACKUP_ID,
        instance,
        cluster_id=CLUSTER_ID,
        table_id=TABLE_ID,
        expire_time=expire_time,
        encryption_info="encryption_info",
    )

    assert backup.backup_id == BACKUP_ID
    assert backup._instance is instance
    assert backup._cluster is CLUSTER_ID
    assert backup.table_id == TABLE_ID
    assert backup._expire_time == expire_time
    assert backup._encryption_info == "encryption_info"

    assert backup._parent is None
    assert backup._source_table is None
    assert backup._start_time is None
    assert backup._end_time is None
    assert backup._size_bytes is None
    assert backup._state is None


def test_backup_from_pb_w_project_mismatch():
    from google.cloud.bigtable.backup import Backup
    from google.cloud.bigtable_admin_v2.types import table

    alt_project_id = "alt-project-id"
    client = _Client(project=alt_project_id)
    instance = _Instance(INSTANCE_NAME, client)
    backup_pb = table.Backup(name=BACKUP_NAME)

    with pytest.raises(ValueError):
        Backup.from_pb(backup_pb, instance)


def test_backup_from_pb_w_instance_mismatch():
    from google.cloud.bigtable.backup import Backup
    from google.cloud.bigtable_admin_v2.types import table

    alt_instance = "/projects/%s/instances/alt-instance" % PROJECT_ID
    client = _Client()
    instance = _Instance(alt_instance, client)
    backup_pb = table.Backup(name=BACKUP_NAME)

    with pytest.raises(ValueError):
        Backup.from_pb(backup_pb, instance)


def test_backup_from_pb_w_bad_name():
    from google.cloud.bigtable.backup import Backup
    from google.cloud.bigtable_admin_v2.types import table

    client = _Client()
    instance = _Instance(INSTANCE_NAME, client)
    backup_pb = table.Backup(name="invalid_name")

    with pytest.raises(ValueError):
        Backup.from_pb(backup_pb, instance)


def test_backup_from_pb_success():
    from google.cloud._helpers import _datetime_to_pb_timestamp
    from google.rpc.code_pb2 import Code

    from google.cloud.bigtable.backup import Backup
    from google.cloud.bigtable.encryption_info import EncryptionInfo
    from google.cloud.bigtable.error import Status
    from google.cloud.bigtable_admin_v2.types import table

    client = _Client()
    instance = _Instance(INSTANCE_NAME, client)
    timestamp = _datetime_to_pb_timestamp(_make_timestamp())
    size_bytes = 1234
    state = table.Backup.State.READY
    GOOGLE_DEFAULT_ENCRYPTION = (
        table.EncryptionInfo.EncryptionType.GOOGLE_DEFAULT_ENCRYPTION
    )
    backup_pb = table.Backup(
        name=BACKUP_NAME,
        source_table=TABLE_NAME,
        expire_time=timestamp,
        start_time=timestamp,
        end_time=timestamp,
        size_bytes=size_bytes,
        state=state,
        encryption_info=table.EncryptionInfo(
            encryption_type=GOOGLE_DEFAULT_ENCRYPTION,
            encryption_status=_StatusPB(Code.OK, "Status OK"),
            kms_key_version="2",
        ),
    )

    backup = Backup.from_pb(backup_pb, instance)

    assert isinstance(backup, Backup)
    assert backup._instance == instance
    assert backup.backup_id == BACKUP_ID
    assert backup.cluster == CLUSTER_ID
    assert backup.table_id == TABLE_ID
    assert backup._expire_time == timestamp
    assert backup.start_time == timestamp
    assert backup.end_time == timestamp
    assert backup._size_bytes == size_bytes
    assert backup._state == state
    expected_info = EncryptionInfo(
        encryption_type=GOOGLE_DEFAULT_ENCRYPTION,
        encryption_status=Status(_StatusPB(Code.OK, "Status OK")),
        kms_key_version="2",
    )
    assert backup.encryption_info == expected_info


def test_backup_name():
    from google.cloud.bigtable.client import Client
    from google.cloud.bigtable_admin_v2.services.bigtable_instance_admin import (
        BigtableInstanceAdminClient,
    )

    api = mock.create_autospec(BigtableInstanceAdminClient)
    credentials = _make_credentials()
    client = Client(project=PROJECT_ID, credentials=credentials, admin=True)
    client._table_admin_client = api
    instance = _Instance(INSTANCE_NAME, client)

    backup = _make_backup(BACKUP_ID, instance, cluster_id=CLUSTER_ID)
    assert backup.name == BACKUP_NAME


def test_backup_cluster():
    backup = _make_backup(BACKUP_ID, _Instance(INSTANCE_NAME), cluster_id=CLUSTER_ID)
    assert backup.cluster == CLUSTER_ID


def test_backup_cluster_setter():
    backup = _make_backup(BACKUP_ID, _Instance(INSTANCE_NAME))
    backup.cluster = CLUSTER_ID
    assert backup.cluster == CLUSTER_ID


def test_backup_parent_none():
    backup = _make_backup(
        BACKUP_ID,
        _Instance(INSTANCE_NAME),
    )
    assert backup.parent is None


def test_backup_parent_w_cluster():
    from google.cloud.bigtable.client import Client
    from google.cloud.bigtable_admin_v2.services.bigtable_instance_admin import (
        BigtableInstanceAdminClient,
    )

    api = mock.create_autospec(BigtableInstanceAdminClient)
    credentials = _make_credentials()
    client = Client(project=PROJECT_ID, credentials=credentials, admin=True)
    client._table_admin_client = api
    instance = _Instance(INSTANCE_NAME, client)

    backup = _make_backup(BACKUP_ID, instance, cluster_id=CLUSTER_ID)
    assert backup._cluster == CLUSTER_ID
    assert backup.parent == CLUSTER_NAME


def test_backup_source_table_none():
    from google.cloud.bigtable.client import Client
    from google.cloud.bigtable_admin_v2.services.bigtable_instance_admin import (
        BigtableInstanceAdminClient,
    )

    api = mock.create_autospec(BigtableInstanceAdminClient)
    credentials = _make_credentials()
    client = Client(project=PROJECT_ID, credentials=credentials, admin=True)
    client._table_admin_client = api
    instance = _Instance(INSTANCE_NAME, client)

    backup = _make_backup(BACKUP_ID, instance)
    assert backup.source_table is None


def test_backup_source_table_valid():
    from google.cloud.bigtable.client import Client
    from google.cloud.bigtable_admin_v2.services.bigtable_instance_admin import (
        BigtableInstanceAdminClient,
    )

    api = mock.create_autospec(BigtableInstanceAdminClient)
    credentials = _make_credentials()
    client = Client(project=PROJECT_ID, credentials=credentials, admin=True)
    client._table_admin_client = api
    instance = _Instance(INSTANCE_NAME, client)

    backup = _make_backup(BACKUP_ID, instance, table_id=TABLE_ID)
    assert backup.source_table == TABLE_NAME


def test_backup_expire_time():
    instance = _Instance(INSTANCE_NAME)
    expire_time = _make_timestamp()
    backup = _make_backup(BACKUP_ID, instance, expire_time=expire_time)
    assert backup.expire_time == expire_time


def test_backup_expire_time_setter():
    instance = _Instance(INSTANCE_NAME)
    expire_time = _make_timestamp()
    backup = _make_backup(BACKUP_ID, instance)
    backup.expire_time = expire_time
    assert backup.expire_time == expire_time


def test_backup_start_time():
    instance = _Instance(INSTANCE_NAME)
    backup = _make_backup(BACKUP_ID, instance)
    expected = backup._start_time = _make_timestamp()
    assert backup.start_time == expected


def test_backup_end_time():
    instance = _Instance(INSTANCE_NAME)
    backup = _make_backup(BACKUP_ID, instance)
    expected = backup._end_time = _make_timestamp()
    assert backup.end_time == expected


def test_backup_size():
    instance = _Instance(INSTANCE_NAME)
    backup = _make_backup(BACKUP_ID, instance)
    expected = backup._size_bytes = 10
    assert backup.size_bytes == expected


def test_backup_state():
    from google.cloud.bigtable_admin_v2.types import table

    instance = _Instance(INSTANCE_NAME)
    backup = _make_backup(BACKUP_ID, instance)
    expected = backup._state = table.Backup.State.READY
    assert backup.state == expected


def test_backup___eq__():
    instance = object()
    backup1 = _make_backup(BACKUP_ID, instance)
    backup2 = _make_backup(BACKUP_ID, instance)
    assert backup1 == backup2


def test_backup___eq___w_different_types():
    instance = object()
    backup1 = _make_backup(BACKUP_ID, instance)
    backup2 = object()
    assert not (backup1 == backup2)


def test_backup___ne___w_same_value():
    instance = object()
    backup1 = _make_backup(BACKUP_ID, instance)
    backup2 = _make_backup(BACKUP_ID, instance)
    assert not (backup1 != backup2)


def test_backup___ne__():
    backup1 = _make_backup("backup_1", "instance1")
    backup2 = _make_backup("backup_2", "instance2")
    assert backup1 != backup2


def test_backup_create_w_grpc_error():
    from google.api_core.exceptions import GoogleAPICallError, Unknown
    from google.cloud._helpers import _datetime_to_pb_timestamp

    from google.cloud.bigtable_admin_v2.types import table

    client = _Client()
    api = client.table_admin_client = _make_table_admin_client()
    api.create_backup.side_effect = Unknown("testing")

    timestamp = _make_timestamp()
    backup = _make_backup(
        BACKUP_ID,
        _Instance(INSTANCE_NAME, client=client),
        table_id=TABLE_ID,
        expire_time=timestamp,
    )

    backup_pb = table.Backup(
        source_table=TABLE_NAME,
        expire_time=_datetime_to_pb_timestamp(timestamp),
    )

    with pytest.raises(GoogleAPICallError):
        backup.create(CLUSTER_ID)

    api.create_backup.assert_called_once_with(
        request={"parent": CLUSTER_NAME, "backup_id": BACKUP_ID, "backup": backup_pb}
    )


def test_backup_create_w_already_exists():
    from google.cloud._helpers import _datetime_to_pb_timestamp
    from google.cloud.exceptions import Conflict

    from google.cloud.bigtable_admin_v2.types import table

    client = _Client()
    api = client.table_admin_client = _make_table_admin_client()
    api.create_backup.side_effect = Conflict("testing")

    timestamp = _make_timestamp()
    backup = _make_backup(
        BACKUP_ID,
        _Instance(INSTANCE_NAME, client=client),
        table_id=TABLE_ID,
        expire_time=timestamp,
    )

    backup_pb = table.Backup(
        source_table=TABLE_NAME,
        expire_time=_datetime_to_pb_timestamp(timestamp),
    )

    with pytest.raises(Conflict):
        backup.create(CLUSTER_ID)

    api.create_backup.assert_called_once_with(
        request={"parent": CLUSTER_NAME, "backup_id": BACKUP_ID, "backup": backup_pb}
    )


def test_backup_create_w_instance_not_found():
    from google.cloud._helpers import _datetime_to_pb_timestamp
    from google.cloud.exceptions import NotFound

    from google.cloud.bigtable_admin_v2.types import table

    client = _Client()
    api = client.table_admin_client = _make_table_admin_client()
    api.create_backup.side_effect = NotFound("testing")

    timestamp = _make_timestamp()
    backup = _make_backup(
        BACKUP_ID,
        _Instance(INSTANCE_NAME, client=client),
        table_id=TABLE_ID,
        expire_time=timestamp,
    )

    backup_pb = table.Backup(
        source_table=TABLE_NAME,
        expire_time=_datetime_to_pb_timestamp(timestamp),
    )

    with pytest.raises(NotFound):
        backup.create(CLUSTER_ID)

    api.create_backup.assert_called_once_with(
        request={"parent": CLUSTER_NAME, "backup_id": BACKUP_ID, "backup": backup_pb}
    )


def test_backup_create_w_cluster_not_set():
    backup = _make_backup(
        BACKUP_ID,
        _Instance(INSTANCE_NAME),
        table_id=TABLE_ID,
        expire_time=_make_timestamp(),
    )

    with pytest.raises(ValueError):
        backup.create()


def test_backup_create_w_table_not_set():
    backup = _make_backup(
        BACKUP_ID,
        _Instance(INSTANCE_NAME),
        expire_time=_make_timestamp(),
    )

    with pytest.raises(ValueError):
        backup.create(CLUSTER_ID)


def test_backup_create_w_expire_time_not_set():
    backup = _make_backup(
        BACKUP_ID,
        _Instance(INSTANCE_NAME),
        table_id=TABLE_ID,
    )

    with pytest.raises(ValueError):
        backup.create(CLUSTER_ID)


def test_backup_create_success():
    from google.cloud._helpers import _datetime_to_pb_timestamp

    from google.cloud.bigtable import Client
    from google.cloud.bigtable_admin_v2.types import table

    op_future = object()
    credentials = _make_credentials()
    client = Client(project=PROJECT_ID, credentials=credentials, admin=True)
    api = client._table_admin_client = _make_table_admin_client()
    api.create_backup.return_value = op_future

    timestamp = _make_timestamp()
    backup = _make_backup(
        BACKUP_ID,
        _Instance(INSTANCE_NAME, client=client),
        table_id=TABLE_ID,
        expire_time=timestamp,
    )

    backup_pb = table.Backup(
        source_table=TABLE_NAME,
        expire_time=_datetime_to_pb_timestamp(timestamp),
    )

    future = backup.create(CLUSTER_ID)
    assert backup._cluster == CLUSTER_ID
    assert future is op_future

    api.create_backup.assert_called_once_with(
        request={"parent": CLUSTER_NAME, "backup_id": BACKUP_ID, "backup": backup_pb}
    )


def test_backup_get():
    from google.cloud._helpers import _datetime_to_pb_timestamp

    from google.cloud.bigtable_admin_v2.types import table

    timestamp = _datetime_to_pb_timestamp(_make_timestamp())
    state = table.Backup.State.READY

    client = _Client()
    backup_pb = table.Backup(
        name=BACKUP_NAME,
        source_table=TABLE_NAME,
        expire_time=timestamp,
        start_time=timestamp,
        end_time=timestamp,
        size_bytes=0,
        state=state,
    )
    api = client.table_admin_client = _make_table_admin_client()
    api.get_backup.return_value = backup_pb

    instance = _Instance(INSTANCE_NAME, client=client)
    backup = _make_backup(BACKUP_ID, instance, cluster_id=CLUSTER_ID)

    assert backup.get() == backup_pb


def test_backup_reload():
    from google.cloud._helpers import _datetime_to_pb_timestamp

    from google.cloud.bigtable_admin_v2.types import table

    timestamp = _datetime_to_pb_timestamp(_make_timestamp())
    state = table.Backup.State.READY

    client = _Client()
    backup_pb = table.Backup(
        name=BACKUP_NAME,
        source_table=TABLE_NAME,
        expire_time=timestamp,
        start_time=timestamp,
        end_time=timestamp,
        size_bytes=0,
        state=state,
    )
    api = client.table_admin_client = _make_table_admin_client()
    api.get_backup.return_value = backup_pb

    instance = _Instance(INSTANCE_NAME, client=client)
    backup = _make_backup(BACKUP_ID, instance, cluster_id=CLUSTER_ID)

    backup.reload()
    assert backup._source_table == TABLE_NAME
    assert backup._expire_time == timestamp
    assert backup._start_time == timestamp
    assert backup._end_time == timestamp
    assert backup._size_bytes == 0
    assert backup._state == state


def test_backup_exists_w_grpc_error():
    from google.api_core.exceptions import Unknown

    client = _Client()
    api = client.table_admin_client = _make_table_admin_client()
    api.get_backup.side_effect = Unknown("testing")

    instance = _Instance(INSTANCE_NAME, client=client)
    backup = _make_backup(BACKUP_ID, instance, cluster_id=CLUSTER_ID)

    with pytest.raises(Unknown):
        backup.exists()

    request = {"name": BACKUP_NAME}
    api.get_backup.assert_called_once_with(request)


def test_backup_exists_w_not_found():
    from google.api_core.exceptions import NotFound

    client = _Client()
    api = client.table_admin_client = _make_table_admin_client()
    api.get_backup.side_effect = NotFound("testing")

    instance = _Instance(INSTANCE_NAME, client=client)
    backup = _make_backup(BACKUP_ID, instance, cluster_id=CLUSTER_ID)

    assert not backup.exists()

    api.get_backup.assert_called_once_with(request={"name": BACKUP_NAME})


def test_backup_exists_success():
    from google.cloud.bigtable_admin_v2.types import table

    client = _Client()
    backup_pb = table.Backup(name=BACKUP_NAME)
    api = client.table_admin_client = _make_table_admin_client()
    api.get_backup.return_value = backup_pb

    instance = _Instance(INSTANCE_NAME, client=client)
    backup = _make_backup(BACKUP_ID, instance, cluster_id=CLUSTER_ID)

    assert backup.exists()

    api.get_backup.assert_called_once_with(request={"name": BACKUP_NAME})


def test_backup_delete_w_grpc_error():
    from google.api_core.exceptions import Unknown

    client = _Client()
    api = client.table_admin_client = _make_table_admin_client()
    api.delete_backup.side_effect = Unknown("testing")
    instance = _Instance(INSTANCE_NAME, client=client)
    backup = _make_backup(BACKUP_ID, instance, cluster_id=CLUSTER_ID)

    with pytest.raises(Unknown):
        backup.delete()

    api.delete_backup.assert_called_once_with(request={"name": BACKUP_NAME})


def test_backup_delete_w_not_found():
    from google.api_core.exceptions import NotFound

    client = _Client()
    api = client.table_admin_client = _make_table_admin_client()
    api.delete_backup.side_effect = NotFound("testing")
    instance = _Instance(INSTANCE_NAME, client=client)
    backup = _make_backup(BACKUP_ID, instance, cluster_id=CLUSTER_ID)

    with pytest.raises(NotFound):
        backup.delete()

    api.delete_backup.assert_called_once_with(request={"name": BACKUP_NAME})


def test_backup_delete_success():
    from google.protobuf.empty_pb2 import Empty

    client = _Client()
    api = client.table_admin_client = _make_table_admin_client()
    api.delete_backup.return_value = Empty()
    instance = _Instance(INSTANCE_NAME, client=client)
    backup = _make_backup(BACKUP_ID, instance, cluster_id=CLUSTER_ID)

    backup.delete()

    api.delete_backup.assert_called_once_with(request={"name": BACKUP_NAME})


def test_backup_update_expire_time_w_grpc_error():
    from google.api_core.exceptions import Unknown
    from google.cloud._helpers import _datetime_to_pb_timestamp
    from google.protobuf import field_mask_pb2

    from google.cloud.bigtable_admin_v2.types import table

    client = _Client()
    api = client.table_admin_client = _make_table_admin_client()
    api.update_backup.side_effect = Unknown("testing")
    instance = _Instance(INSTANCE_NAME, client=client)
    backup = _make_backup(BACKUP_ID, instance, cluster_id=CLUSTER_ID)
    expire_time = _make_timestamp()

    with pytest.raises(Unknown):
        backup.update_expire_time(expire_time)

    backup_update = table.Backup(
        name=BACKUP_NAME,
        expire_time=_datetime_to_pb_timestamp(expire_time),
    )
    update_mask = field_mask_pb2.FieldMask(paths=["expire_time"])
    api.update_backup.assert_called_once_with(
        request={"backup": backup_update, "update_mask": update_mask}
    )


def test_backup_update_expire_time_w_not_found():
    from google.api_core.exceptions import NotFound
    from google.cloud._helpers import _datetime_to_pb_timestamp
    from google.protobuf import field_mask_pb2

    from google.cloud.bigtable_admin_v2.types import table

    client = _Client()
    api = client.table_admin_client = _make_table_admin_client()
    api.update_backup.side_effect = NotFound("testing")
    instance = _Instance(INSTANCE_NAME, client=client)
    backup = _make_backup(BACKUP_ID, instance, cluster_id=CLUSTER_ID)
    expire_time = _make_timestamp()

    with pytest.raises(NotFound):
        backup.update_expire_time(expire_time)

    backup_update = table.Backup(
        name=BACKUP_NAME,
        expire_time=_datetime_to_pb_timestamp(expire_time),
    )
    update_mask = field_mask_pb2.FieldMask(paths=["expire_time"])
    api.update_backup.assert_called_once_with(
        request={"backup": backup_update, "update_mask": update_mask}
    )


def test_backup_update_expire_time_success():
    from google.cloud._helpers import _datetime_to_pb_timestamp
    from google.protobuf import field_mask_pb2

    from google.cloud.bigtable_admin_v2.types import table

    client = _Client()
    api = client.table_admin_client = _make_table_admin_client()
    api.update_backup.return_type = table.Backup(name=BACKUP_NAME)
    instance = _Instance(INSTANCE_NAME, client=client)
    backup = _make_backup(BACKUP_ID, instance, cluster_id=CLUSTER_ID)
    expire_time = _make_timestamp()

    backup.update_expire_time(expire_time)

    backup_update = table.Backup(
        name=BACKUP_NAME,
        expire_time=_datetime_to_pb_timestamp(expire_time),
    )
    update_mask = field_mask_pb2.FieldMask(paths=["expire_time"])
    api.update_backup.assert_called_once_with(
        request={"backup": backup_update, "update_mask": update_mask}
    )


def test_backup_restore_w_grpc_error():
    from google.api_core.exceptions import GoogleAPICallError, Unknown

    client = _Client()
    api = client.table_admin_client = _make_table_admin_client()
    api._restore_table.side_effect = Unknown("testing")

    timestamp = _make_timestamp()
    backup = _make_backup(
        BACKUP_ID,
        _Instance(INSTANCE_NAME, client=client),
        cluster_id=CLUSTER_ID,
        table_id=TABLE_NAME,
        expire_time=timestamp,
    )

    with pytest.raises(GoogleAPICallError):
        backup.restore(TABLE_ID)

    api._restore_table.assert_called_once_with(
        request={"parent": INSTANCE_NAME, "table_id": TABLE_ID, "backup": BACKUP_NAME}
    )


def test_backup_restore_w_cluster_not_set():
    client = _Client()
    client.table_admin_client = _make_table_admin_client()
    backup = _make_backup(
        BACKUP_ID,
        _Instance(INSTANCE_NAME, client=client),
        table_id=TABLE_ID,
        expire_time=_make_timestamp(),
    )

    with pytest.raises(ValueError):
        backup.restore(TABLE_ID)


def _restore_helper(instance_id=None, instance_name=None):
    op_future = object()
    client = _Client()
    api = client.table_admin_client = _make_table_admin_client()
    api._restore_table.return_value = op_future

    timestamp = _make_timestamp()
    backup = _make_backup(
        BACKUP_ID,
        _Instance(INSTANCE_NAME, client=client),
        cluster_id=CLUSTER_ID,
        table_id=TABLE_NAME,
        expire_time=timestamp,
    )

    future = backup.restore(TABLE_ID, instance_id)
    assert backup._cluster == CLUSTER_ID
    assert future is op_future

    api._restore_table.assert_called_once_with(
        request={
            "parent": instance_name or INSTANCE_NAME,
            "table_id": TABLE_ID,
            "backup": BACKUP_NAME,
        }
    )
    api._restore_table.reset_mock()


def test_backup_restore_default():
    _restore_helper()


def test_backup_restore_to_another_instance():
    _restore_helper(ALT_INSTANCE, ALT_INSTANCE_NAME)


def test_backup_get_iam_policy():
    from google.iam.v1 import policy_pb2

    from google.cloud.bigtable.client import Client
    from google.cloud.bigtable.policy import BIGTABLE_ADMIN_ROLE
    from google.cloud.bigtable_admin_v2.services.bigtable_table_admin import (
        BaseBigtableTableAdminClient,
    )

    credentials = _make_credentials()
    client = Client(project=PROJECT_ID, credentials=credentials, admin=True)

    instance = client.instance(instance_id=INSTANCE_ID)
    backup = _make_backup(BACKUP_ID, instance, cluster_id=CLUSTER_ID)

    version = 1
    etag = b"etag_v1"
    members = ["serviceAccount:service_acc1@test.com", "user:user1@test.com"]
    bindings = [{"role": BIGTABLE_ADMIN_ROLE, "members": members}]
    iam_policy = policy_pb2.Policy(version=version, etag=etag, bindings=bindings)

    table_api = mock.create_autospec(BaseBigtableTableAdminClient)
    client._table_admin_client = table_api
    table_api.get_iam_policy.return_value = iam_policy

    result = backup.get_iam_policy()

    table_api.get_iam_policy.assert_called_once_with(request={"resource": backup.name})
    assert result.version == version
    assert result.etag == etag

    admins = result.bigtable_admins
    assert len(admins) == len(members)
    for found, expected in zip(sorted(admins), sorted(members)):
        assert found == expected


def test_backup_set_iam_policy():
    from google.iam.v1 import policy_pb2

    from google.cloud.bigtable.client import Client
    from google.cloud.bigtable.policy import BIGTABLE_ADMIN_ROLE, Policy
    from google.cloud.bigtable_admin_v2.services.bigtable_table_admin import (
        BaseBigtableTableAdminClient,
    )

    credentials = _make_credentials()
    client = Client(project=PROJECT_ID, credentials=credentials, admin=True)

    instance = client.instance(instance_id=INSTANCE_ID)
    backup = _make_backup(BACKUP_ID, instance, cluster_id=CLUSTER_ID)

    version = 1
    etag = b"etag_v1"
    members = ["serviceAccount:service_acc1@test.com", "user:user1@test.com"]
    bindings = [{"role": BIGTABLE_ADMIN_ROLE, "members": sorted(members)}]
    iam_policy_pb = policy_pb2.Policy(version=version, etag=etag, bindings=bindings)

    table_api = mock.create_autospec(BaseBigtableTableAdminClient)
    client._table_admin_client = table_api
    table_api.set_iam_policy.return_value = iam_policy_pb

    iam_policy = Policy(etag=etag, version=version)
    iam_policy[BIGTABLE_ADMIN_ROLE] = [
        Policy.user("user1@test.com"),
        Policy.service_account("service_acc1@test.com"),
    ]

    result = backup.set_iam_policy(iam_policy)

    table_api.set_iam_policy.assert_called_once_with(
        request={"resource": backup.name, "policy": iam_policy_pb}
    )
    assert result.version == version
    assert result.etag == etag

    admins = result.bigtable_admins
    assert len(admins) == len(members)
    for found, expected in zip(sorted(admins), sorted(members)):
        assert found == expected


def test_backup_test_iam_permissions():
    from google.iam.v1 import iam_policy_pb2

    from google.cloud.bigtable.client import Client
    from google.cloud.bigtable_admin_v2.services.bigtable_table_admin import (
        BaseBigtableTableAdminClient,
    )

    credentials = _make_credentials()
    client = Client(project=PROJECT_ID, credentials=credentials, admin=True)

    instance = client.instance(instance_id=INSTANCE_ID)
    backup = _make_backup(BACKUP_ID, instance, cluster_id=CLUSTER_ID)

    permissions = ["bigtable.backups.create", "bigtable.backups.list"]

    response = iam_policy_pb2.TestIamPermissionsResponse(permissions=permissions)

    table_api = mock.create_autospec(BaseBigtableTableAdminClient)
    table_api.test_iam_permissions.return_value = response
    client._table_admin_client = table_api

    result = backup.test_iam_permissions(permissions)

    assert result == permissions
    table_api.test_iam_permissions.assert_called_once_with(
        request={"resource": backup.name, "permissions": permissions}
    )


class _Client(object):
    def __init__(self, project=PROJECT_ID):
        self.project = project
        self.project_name = "projects/" + self.project


class _Instance(object):
    def __init__(self, name, client=None):
        self.name = name
        self.instance_id = name.rsplit("/", 1)[1]
        self._client = client


def _StatusPB(code, message):
    from google.rpc import status_pb2

    status_pb = status_pb2.Status()
    status_pb.code = code
    status_pb.message = message

    return status_pb
