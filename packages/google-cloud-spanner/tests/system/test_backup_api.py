# Copyright 2021 Google LLC All rights reserved.
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
import time

import pytest
from google.api_core import exceptions

from google.cloud import spanner_v1
from google.cloud.spanner_admin_database_v1.types.common import DatabaseDialect

from . import _helpers

skip_env_reason = f"""\
Remove {_helpers.SKIP_BACKUP_TESTS_ENVVAR} from environment to run these tests.\
"""
skip_emulator_reason = "Backup operations not supported by emulator."
skip_spanner_omni_reason = "Backup operations not supported on Spanner Omni yet."

pytestmark = [
    pytest.mark.skipif(_helpers.SKIP_BACKUP_TESTS, reason=skip_env_reason),
    pytest.mark.skipif(_helpers.USE_EMULATOR, reason=skip_emulator_reason),
    pytest.mark.skipif(_helpers.USE_SPANNER_OMNI, reason=skip_spanner_omni_reason),
]


@pytest.fixture(scope="session")
def same_config_instance(spanner_client, shared_instance, instance_operation_timeout):
    current_config = shared_instance.configuration_name
    same_config_instance_id = _helpers.unique_id("same-config")
    create_time = str(int(time.time()))
    labels = {"python-spanner-systests": "true", "created": create_time}
    same_config_instance = spanner_client.instance(
        same_config_instance_id, current_config, labels=labels
    )
    op = same_config_instance.create()
    op.result(instance_operation_timeout)

    yield same_config_instance

    _helpers.scrub_instance_ignore_not_found(same_config_instance)


@pytest.fixture(scope="session")
def diff_config(shared_instance, instance_configs, not_postgres):
    current_config = shared_instance.configuration_name
    for config in reversed(instance_configs):
        if "-us-" in config.name and config.name != current_config:
            return config.name
    return None


@pytest.fixture(scope="session")
def diff_config_instance(
    spanner_client,
    shared_instance,
    instance_operation_timeout,
    diff_config,
):
    if diff_config is None:
        return None

    diff_config_instance_id = _helpers.unique_id("diff-config")
    create_time = str(int(time.time()))
    labels = {"python-spanner-systests": "true", "created": create_time}
    diff_config_instance = spanner_client.instance(
        diff_config_instance_id, diff_config, labels=labels
    )
    op = diff_config_instance.create()
    op.result(instance_operation_timeout)

    yield diff_config_instance

    _helpers.scrub_instance_ignore_not_found(diff_config_instance)


@pytest.fixture(scope="session")
def database_version_time(shared_database):
    shared_database.reload()
    diff = (
        datetime.datetime.now(datetime.timezone.utc)
        - shared_database.earliest_version_time
    )
    return shared_database.earliest_version_time + diff / 2


@pytest.fixture(scope="session")
def second_database(
    shared_instance, database_operation_timeout, database_dialect, proto_descriptor_file
):
    database_name = _helpers.unique_id("test_database2")
    pool = spanner_v1.BurstyPool(labels={"testcase": "database_api"})
    if database_dialect == DatabaseDialect.POSTGRESQL:
        database = shared_instance.database(
            database_name,
            pool=pool,
            database_dialect=database_dialect,
        )
        operation = database.create()
        operation.result(database_operation_timeout)  # raises on failure / timeout.

        operation = database.update_ddl(ddl_statements=_helpers.DDL_STATEMENTS)
        operation.result(database_operation_timeout)  # raises on failure / timeout.

    else:
        database = shared_instance.database(
            database_name,
            ddl_statements=_helpers.DDL_STATEMENTS,
            pool=pool,
            database_dialect=database_dialect,
            proto_descriptors=proto_descriptor_file,
        )
        operation = database.create()
        operation.result(database_operation_timeout)  # raises on failure / timeout.

    yield database

    database.drop()


@pytest.fixture(scope="function")
def backups_to_delete():
    to_delete = []

    yield to_delete

    for backup in to_delete:
        _helpers.retry_429_503(backup.delete)()


def test_backup_workflow(
    shared_instance,
    shared_database,
    database_dialect,
    database_version_time,
    backups_to_delete,
    databases_to_delete,
):
    from google.cloud.spanner_admin_database_v1 import (
        CreateBackupEncryptionConfig,
        EncryptionConfig,
        EncryptionInfo,
        RestoreDatabaseEncryptionConfig,
    )

    backup_id = _helpers.unique_id("backup_id", separator="_")
    expire_time = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(
        days=3
    )
    encryption_enum = CreateBackupEncryptionConfig.EncryptionType
    encryption_config = CreateBackupEncryptionConfig(
        encryption_type=encryption_enum.GOOGLE_DEFAULT_ENCRYPTION,
    )

    # Create backup.
    backup = shared_instance.backup(
        backup_id,
        database=shared_database,
        expire_time=expire_time,
        version_time=database_version_time,
        encryption_config=encryption_config,
    )
    operation = backup.create()
    backups_to_delete.append(backup)

    # Check metadata.
    metadata = operation.metadata
    assert backup.name == metadata.name
    assert shared_database.name == metadata.database
    operation.result()  # blocks indefinitely

    # Check backup object.
    backup.reload()
    assert shared_database.name == backup._database
    assert expire_time == backup.expire_time
    assert backup.create_time is not None
    assert database_version_time == backup.version_time
    assert backup.size_bytes is not None
    assert backup.state is not None
    assert (
        EncryptionInfo.Type.GOOGLE_DEFAULT_ENCRYPTION
        == backup.encryption_info.encryption_type
    )

    # Update with valid argument.
    valid_expire_time = datetime.datetime.now(
        datetime.timezone.utc
    ) + datetime.timedelta(days=7)
    backup.update_expire_time(valid_expire_time)
    assert valid_expire_time == backup.expire_time

    # Restore database to same instance.
    restored_id = _helpers.unique_id("restored_db", separator="_")
    encryption_config = RestoreDatabaseEncryptionConfig(
        encryption_type=RestoreDatabaseEncryptionConfig.EncryptionType.GOOGLE_DEFAULT_ENCRYPTION,
    )
    database = shared_instance.database(
        restored_id,
        encryption_config=encryption_config,
    )
    databases_to_delete.append(database)
    operation = database.restore(source=backup)
    restored_db = operation.result()  # blocks indefinitely
    assert database_version_time == restored_db.restore_info.backup_info.version_time

    metadata = operation.metadata
    assert database_version_time == metadata.backup_info.version_time

    database.reload()
    expected_encryption_config = EncryptionConfig()
    assert expected_encryption_config == database.encryption_config
    assert database_dialect == database.database_dialect

    database.drop()
    backup.delete()
    assert not backup.exists()


def test_copy_backup_workflow(
    shared_instance,
    shared_backup,
    backups_to_delete,
):
    from google.cloud.spanner_admin_database_v1 import (
        CopyBackupEncryptionConfig,
        EncryptionInfo,
    )

    backup_id = _helpers.unique_id("backup_id", separator="_")
    expire_time = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(
        days=3
    )
    copy_encryption_enum = CopyBackupEncryptionConfig.EncryptionType
    copy_encryption_config = CopyBackupEncryptionConfig(
        encryption_type=copy_encryption_enum.GOOGLE_DEFAULT_ENCRYPTION,
    )

    # Create backup.
    shared_backup.reload()
    # Create a copy backup
    copy_backup = shared_instance.copy_backup(
        backup_id=backup_id,
        source_backup=shared_backup.name,
        expire_time=expire_time,
        encryption_config=copy_encryption_config,
    )
    operation = copy_backup.create()
    backups_to_delete.append(copy_backup)

    # Check metadata.
    metadata = operation.metadata
    assert copy_backup.name == metadata.name
    operation.result()  # blocks indefinitely

    # Check backup object.
    copy_backup.reload()
    assert expire_time == copy_backup.expire_time
    assert copy_backup.create_time is not None
    assert copy_backup.size_bytes is not None
    assert copy_backup.state is not None
    assert (
        EncryptionInfo.Type.GOOGLE_DEFAULT_ENCRYPTION
        == copy_backup.encryption_info.encryption_type
    )

    # Update with valid argument.
    valid_expire_time = datetime.datetime.now(
        datetime.timezone.utc
    ) + datetime.timedelta(days=7)
    copy_backup.update_expire_time(valid_expire_time)
    assert valid_expire_time == copy_backup.expire_time

    copy_backup.delete()
    assert not copy_backup.exists()


def test_backup_create_w_version_time_dflt_to_create_time(
    shared_instance,
    shared_database,
    backups_to_delete,
    databases_to_delete,
):
    backup_id = _helpers.unique_id("backup_id", separator="_")
    expire_time = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(
        days=3
    )

    # Create backup.
    backup = shared_instance.backup(
        backup_id,
        database=shared_database,
        expire_time=expire_time,
    )
    operation = backup.create()
    backups_to_delete.append(backup)

    # Check metadata.
    metadata = operation.metadata
    assert backup.name == metadata.name
    assert shared_database.name == metadata.database
    operation.result()  # blocks indefinitely

    # Check backup object.
    backup.reload()
    assert shared_database.name == backup._database
    assert backup.create_time is not None
    assert backup.create_time == backup.version_time

    backup.delete()
    assert not backup.exists()


def test_backup_create_w_invalid_expire_time(shared_instance, shared_database):
    backup_id = _helpers.unique_id("backup_id", separator="_")
    expire_time = datetime.datetime.now(datetime.timezone.utc)

    backup = shared_instance.backup(
        backup_id, database=shared_database, expire_time=expire_time
    )

    with pytest.raises(exceptions.InvalidArgument):
        op = backup.create()
        op.result()  # blocks indefinitely


def test_backup_create_w_invalid_version_time_past(
    shared_instance,
    shared_database,
):
    backup_id = _helpers.unique_id("backup_id", separator="_")
    expire_time = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(
        days=3
    )
    version_time = datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(
        days=10
    )

    backup = shared_instance.backup(
        backup_id,
        database=shared_database,
        expire_time=expire_time,
        version_time=version_time,
    )

    with pytest.raises(exceptions.InvalidArgument):
        op = backup.create()
        op.result()  # blocks indefinitely


def test_backup_create_w_invalid_version_time_future(
    shared_instance,
    shared_database,
):
    backup_id = _helpers.unique_id("backup_id", separator="_")
    expire_time = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(
        days=3
    )
    version_time = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(
        days=2
    )

    backup = shared_instance.backup(
        backup_id,
        database=shared_database,
        expire_time=expire_time,
        version_time=version_time,
    )

    with pytest.raises(exceptions.InvalidArgument):
        op = backup.create()
        op.result()  # blocks indefinitely


def test_database_restore_to_diff_instance(
    shared_instance,
    shared_database,
    backups_to_delete,
    same_config_instance,
    databases_to_delete,
):
    backup_id = _helpers.unique_id("backup_id", separator="_")
    expire_time = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(
        days=3
    )

    # Create backup.
    backup = shared_instance.backup(
        backup_id,
        database=shared_database,
        expire_time=expire_time,
    )
    op = backup.create()
    backups_to_delete.append(backup)
    op.result()

    # Restore database to different instance with same config.
    restored_id = _helpers.unique_id("restored_db")
    database = same_config_instance.database(restored_id)
    databases_to_delete.append(database)
    operation = database.restore(source=backup)
    operation.result()  # blocks indefinitely

    database.drop()
    backup.delete()
    assert not backup.exists()


def test_multi_create_cancel_update_error_restore_errors(
    shared_instance,
    shared_database,
    second_database,
    diff_config_instance,
    backups_to_delete,
    databases_to_delete,
):
    backup_id_1 = _helpers.unique_id("backup_id1", separator="_")
    backup_id_2 = _helpers.unique_id("backup_id2", separator="_")
    expire_time = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(
        days=3
    )

    backup1 = shared_instance.backup(
        backup_id_1, database=shared_database, expire_time=expire_time
    )
    backup2 = shared_instance.backup(
        backup_id_2, database=second_database, expire_time=expire_time
    )

    # Create two backups.
    op1 = backup1.create()
    backups_to_delete.append(backup1)
    op2 = backup2.create()
    backups_to_delete.append(backup2)

    backup1.reload()
    assert not backup1.is_ready()

    backup2.reload()
    assert not backup2.is_ready()

    # Cancel a create operation.
    op2.cancel()
    assert op2.cancelled()

    op1.result()  # blocks indefinitely
    backup1.reload()
    assert backup1.is_ready()

    # Update expire time to invalid value.
    max_expire_days = 366  # documented maximum
    invalid_expire_time = datetime.datetime.now(
        datetime.timezone.utc
    ) + datetime.timedelta(days=max_expire_days + 1)
    with pytest.raises(exceptions.InvalidArgument):
        backup1.update_expire_time(invalid_expire_time)

    # Restore to existing database.
    with pytest.raises(exceptions.AlreadyExists):
        shared_database.restore(source=backup1)

    # Restore to instance with different config.
    if diff_config_instance is not None:
        new_db = diff_config_instance.database("diff_config")

        with pytest.raises(exceptions.InvalidArgument):
            new_db.restore(source=backup1)


def test_instance_list_backups(
    shared_instance,
    shared_database,
    second_database,
    backups_to_delete,
):
    # Remove un-scrubbed backups FBO count below.
    _helpers.scrub_instance_backups(shared_instance)

    backup_id_1 = _helpers.unique_id("backup_id1", separator="_")
    backup_id_2 = _helpers.unique_id("backup_id2", separator="_")

    expire_time_1 = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(
        days=21
    )
    expire_time_1_stamp = expire_time_1.strftime("%Y-%m-%dT%H:%M:%S.%fZ")

    backup1 = shared_instance.backup(
        backup_id_1,
        database=shared_database,
        expire_time=expire_time_1,
    )

    expire_time_2 = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(
        days=1
    )
    backup2 = shared_instance.backup(
        backup_id_2, database=second_database, expire_time=expire_time_2
    )

    # Create two backups.
    op1 = backup1.create()
    backups_to_delete.append(backup1)
    op1.result()  # blocks indefinitely
    backup1.reload()

    create_time_compare = datetime.datetime.now(datetime.timezone.utc)
    create_time_stamp = create_time_compare.strftime("%Y-%m-%dT%H:%M:%S.%fZ")

    backup2.create()
    # This test doesn't block for the result of the 'backup2.create()' call
    # because it wants to find `backup2` in the upcoming search for
    # backups matching 'state;CREATING`:  inherently racy, but probably
    # safe, given how long it takes to create a backup (on the order of
    # minutes, not seconds).
    backups_to_delete.append(backup2)

    # List backups filtered by state.
    filter_ = "state:CREATING"
    for backup in shared_instance.list_backups(filter_=filter_):
        assert backup.name == backup2.name

    # List backups filtered by backup name.
    filter_ = f"name:{backup_id_1}"
    for backup in shared_instance.list_backups(filter_=filter_):
        assert backup.name == backup1.name

    # List backups filtered by database name.
    filter_ = f"database:{shared_database.name}"
    for backup in shared_instance.list_backups(filter_=filter_):
        assert backup.name == backup1.name

    # List backups filtered by create time.
    filter_ = f'create_time > "{create_time_stamp}"'
    for backup in shared_instance.list_backups(filter_=filter_):
        assert backup.name == backup2.name

    # List backups filtered by version time.
    filter_ = f'version_time > "{create_time_stamp}"'
    for backup in shared_instance.list_backups(filter_=filter_):
        assert backup.name == backup2.name

    # List backups filtered by expire time.
    filter_ = f'expire_time > "{expire_time_1_stamp}"'
    for backup in shared_instance.list_backups(filter_=filter_):
        assert backup.name == backup1.name

    # List backups filtered by size bytes.
    # XXX: this one may only pass if other tests have run first,
    #      munging 'shared_database' so that its backup will be bigger?
    filter_ = f"size_bytes < {backup1.size_bytes}"
    for backup in shared_instance.list_backups(filter_=filter_):
        assert backup.name == backup2.name

    # List backups using pagination.
    count = 0
    for page in shared_instance.list_backups(page_size=1):
        count += 1
    assert count == 2
