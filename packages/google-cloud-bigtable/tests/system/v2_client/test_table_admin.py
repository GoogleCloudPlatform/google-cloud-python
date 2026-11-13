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

import datetime
import operator
import time

import pytest
from google.api_core.datetime_helpers import DatetimeWithNanoseconds

from . import _helpers


@pytest.fixture(scope="module")
def shared_table_id():
    return "google-cloud-python-test-table"


@pytest.fixture(scope="module")
def shared_table(data_instance_populated, shared_table_id):
    table = data_instance_populated.table(shared_table_id)
    table.create()

    yield table

    table.delete()


@pytest.fixture(scope="function")
def tables_to_delete():
    tables_to_delete = []

    yield tables_to_delete

    for table in tables_to_delete:
        table.delete()


@pytest.fixture(scope="function")
def backups_to_delete():
    backups_to_delete = []

    yield backups_to_delete

    for backup in backups_to_delete:
        backup.delete()


def test_instance_list_tables(data_instance_populated, shared_table, skip_on_emulator):
    # Since `data_instance_populated` is newly created, the
    # table created in `shared_table` here will be the only one.
    tables = data_instance_populated.list_tables()
    assert tables == [shared_table]


def test_table_exists(data_instance_populated):
    temp_table_id = "test-table_exists"
    temp_table = data_instance_populated.table(temp_table_id)
    assert not temp_table.exists()

    temp_table.create()
    assert _helpers.retry_until_true(temp_table.exists)()

    temp_table.delete()
    assert not _helpers.retry_until_false(temp_table.exists)()


def test_table_create(data_instance_populated, shared_table, tables_to_delete):
    temp_table_id = "test-table-create"
    temp_table = data_instance_populated.table(temp_table_id)
    temp_table.create()
    tables_to_delete.append(temp_table)

    # First, create a sorted version of our expected result.
    name_attr = operator.attrgetter("name")
    expected_tables = sorted([temp_table, shared_table], key=name_attr)

    # Then query for the tables in the instance and sort them by
    # name as well.
    tables = data_instance_populated.list_tables()
    sorted_tables = sorted(tables, key=name_attr)
    assert sorted_tables == expected_tables


def test_table_create_w_families(
    data_instance_populated,
    tables_to_delete,
):
    from google.cloud.bigtable.column_family import MaxVersionsGCRule

    temp_table_id = "test-create-table-with-failies"
    column_family_id = "col-fam-id1"
    temp_table = data_instance_populated.table(temp_table_id)
    gc_rule = MaxVersionsGCRule(1)
    temp_table.create(column_families={column_family_id: gc_rule})
    tables_to_delete.append(temp_table)

    col_fams = temp_table.list_column_families()
    assert len(col_fams) == 1

    retrieved_col_fam = col_fams[column_family_id]
    assert retrieved_col_fam._table is temp_table
    assert retrieved_col_fam.column_family_id == column_family_id
    assert retrieved_col_fam.gc_rule == gc_rule


def test_table_create_w_split_keys(
    data_instance_populated, tables_to_delete, skip_on_emulator
):
    temp_table_id = "foo-bar-baz-split-table"
    initial_split_keys = [b"split_key_1", b"split_key_10", b"split_key_20"]
    temp_table = data_instance_populated.table(temp_table_id)
    temp_table.create(initial_split_keys=initial_split_keys)
    tables_to_delete.append(temp_table)

    # Read Sample Row Keys for created splits
    sample_row_keys = temp_table.sample_row_keys()
    actual_keys = [srk.row_key for srk in sample_row_keys]

    expected_keys = initial_split_keys
    expected_keys.append(b"")
    assert actual_keys == expected_keys


def test_column_family_create(data_instance_populated, tables_to_delete):
    from google.cloud.bigtable.column_family import MaxVersionsGCRule

    temp_table_id = "test-create-column-family"
    temp_table = data_instance_populated.table(temp_table_id)
    temp_table.create()
    tables_to_delete.append(temp_table)

    assert temp_table.list_column_families() == {}

    column_family_id = "col-fam-id1"
    gc_rule = MaxVersionsGCRule(1)
    column_family = temp_table.column_family(column_family_id, gc_rule=gc_rule)
    column_family.create()

    col_fams = temp_table.list_column_families()
    assert len(col_fams) == 1

    retrieved_col_fam = col_fams[column_family_id]
    assert retrieved_col_fam._table is column_family._table
    assert retrieved_col_fam.column_family_id == column_family.column_family_id
    assert retrieved_col_fam.gc_rule == gc_rule


def test_column_family_update(data_instance_populated, tables_to_delete):
    from google.cloud.bigtable.column_family import MaxVersionsGCRule

    temp_table_id = "test-update-column-family"
    temp_table = data_instance_populated.table(temp_table_id)
    temp_table.create()
    tables_to_delete.append(temp_table)

    column_family_id = "col-fam-id1"
    gc_rule = MaxVersionsGCRule(1)
    column_family = temp_table.column_family(column_family_id, gc_rule=gc_rule)
    column_family.create()

    # Check that our created table is as expected.
    col_fams = temp_table.list_column_families()
    assert col_fams == {column_family_id: column_family}

    # Update the column family's GC rule and then try to update.
    column_family.gc_rule = None
    column_family.update()

    # Check that the update has propagated.
    col_fams = temp_table.list_column_families()
    assert col_fams[column_family_id].gc_rule is None


def test_column_family_delete(data_instance_populated, tables_to_delete):
    temp_table_id = "test-delete-column-family"
    temp_table = data_instance_populated.table(temp_table_id)
    temp_table.create()
    tables_to_delete.append(temp_table)

    column_family_id = "col-fam-id1"
    assert temp_table.list_column_families() == {}
    column_family = temp_table.column_family(column_family_id)
    column_family.create()

    # Make sure the family is there before deleting it.
    col_fams = temp_table.list_column_families()
    assert list(col_fams.keys()) == [column_family_id]

    _helpers.retry_504(column_family.delete)()
    # Make sure we have successfully deleted it.
    assert temp_table.list_column_families() == {}


def test_table_get_iam_policy(
    data_instance_populated, tables_to_delete, skip_on_emulator
):
    temp_table_id = "test-get-iam-policy-table"
    temp_table = data_instance_populated.table(temp_table_id)
    temp_table.create()
    tables_to_delete.append(temp_table)

    policy = temp_table.get_iam_policy().to_api_repr()
    assert policy["etag"] == "ACAB"
    assert policy["version"] == 0


def test_table_set_iam_policy(
    service_account, data_instance_populated, tables_to_delete, skip_on_emulator
):
    from google.cloud.bigtable.policy import BIGTABLE_ADMIN_ROLE, Policy

    temp_table_id = "test-set-iam-policy-table"
    temp_table = data_instance_populated.table(temp_table_id)
    temp_table.create()
    tables_to_delete.append(temp_table)

    new_policy = Policy()
    service_account_email = service_account.service_account_email
    new_policy[BIGTABLE_ADMIN_ROLE] = [Policy.service_account(service_account_email)]
    policy_latest = temp_table.set_iam_policy(new_policy).to_api_repr()

    assert policy_latest["bindings"][0]["role"] == BIGTABLE_ADMIN_ROLE
    assert service_account_email in policy_latest["bindings"][0]["members"][0]


def test_table_test_iam_permissions(
    data_instance_populated,
    tables_to_delete,
    skip_on_emulator,
):
    temp_table_id = "test-test-iam-policy-table"
    temp_table = data_instance_populated.table(temp_table_id)
    temp_table.create()
    tables_to_delete.append(temp_table)

    permissions = ["bigtable.tables.mutateRows", "bigtable.tables.readRows"]
    permissions_allowed = temp_table.test_iam_permissions(permissions)
    assert permissions == permissions_allowed


def test_table_backup(
    admin_client,
    unique_suffix,
    instance_labels,
    location_id,
    data_instance_populated,
    data_cluster_id,
    instances_to_delete,
    tables_to_delete,
    backups_to_delete,
    skip_on_emulator,
):
    from google.cloud._helpers import _datetime_to_pb_timestamp

    from google.cloud.bigtable import enums

    temp_table_id = "test-backup-table"
    temp_table = data_instance_populated.table(temp_table_id)
    temp_table.create()
    tables_to_delete.append(temp_table)

    temp_backup_id = "test-backup"

    # TODO: consider using `datetime.datetime.now().timestamp()`
    #  when support for Python 2 is fully dropped
    expire = int(time.mktime(datetime.datetime.now().timetuple())) + 604800

    # Testing `Table.backup()` factory
    temp_backup = temp_table.backup(
        temp_backup_id,
        cluster_id=data_cluster_id,
        expire_time=datetime.datetime.utcfromtimestamp(expire),
    )

    # Reinitialize the admin client. This is to test `_table_admin_client`
    # returns a client object (and not NoneType)
    temp_backup._instance._client = admin_client

    # Sanity check for `Backup.exists()` method
    assert not temp_backup.exists()

    # Testing `Backup.create()` method
    backup_op = temp_backup.create()
    backup_op.result(timeout=240)

    # Implicit testing of `Backup.delete()` method
    backups_to_delete.append(temp_backup)

    # Testing `Backup.exists()` method
    assert temp_backup.exists()

    # Testing `Table.list_backups()` method
    temp_table_backup = temp_table.list_backups()[0]
    assert temp_backup_id == temp_table_backup.backup_id
    assert data_cluster_id == temp_table_backup.cluster
    assert expire == temp_table_backup.expire_time.seconds
    assert (
        temp_table_backup.encryption_info.encryption_type
        == enums.EncryptionInfo.EncryptionType.GOOGLE_DEFAULT_ENCRYPTION
    )

    # Testing `Backup.update_expire_time()` method
    expire += 3600  # A one-hour change in the `expire_time` parameter
    updated_time = datetime.datetime.utcfromtimestamp(expire)
    temp_backup.update_expire_time(updated_time)
    test = _datetime_to_pb_timestamp(updated_time)

    # Testing `Backup.get()` method
    temp_table_backup = temp_backup.get()
    assert test.seconds == DatetimeWithNanoseconds.timestamp(
        temp_table_backup.expire_time
    )

    # Testing `Table.restore()` and `Backup.retore()` methods
    restored_table_id = "test-backup-table-restored"
    restored_table = data_instance_populated.table(restored_table_id)
    local_restore_op = temp_table.restore(
        restored_table_id, cluster_id=data_cluster_id, backup_id=temp_backup_id
    )
    local_restore_op.result(timeout=30)
    tables = data_instance_populated.list_tables()
    assert restored_table in tables
    restored_table.delete()

    # Testing `Backup.restore()`:
    restored_table_id_2 = "test-backup-table-restored-2"
    restore_op = temp_backup.restore(
        restored_table_id_2, data_instance_populated.instance_id
    )
    restore_op.result(timeout=240)
    restored_table_2 = data_instance_populated.table(restored_table_id_2)
    assert restored_table_2 in data_instance_populated.list_tables()
    restored_table_2.delete()
