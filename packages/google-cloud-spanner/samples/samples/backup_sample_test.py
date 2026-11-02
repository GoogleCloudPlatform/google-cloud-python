# Copyright 2020 Google Inc. All Rights Reserved.
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
import uuid

from google.api_core.exceptions import AlreadyExists, DeadlineExceeded
import pytest
from test_utils.retry import RetryErrors

import backup_sample


def unique_database_id():
    """Creates a unique id for the database."""
    return f"test-db-{uuid.uuid4().hex[:10]}"


def unique_backup_id():
    """Creates a unique id for the backup."""
    return f"test-backup-{uuid.uuid4().hex[:10]}"


def _verify_restored_database(
    spanner_client,
    instance_id,
    database_id,
    backup_id,
    kms_key_name=None,
    kms_key_names=None,
):
    import time

    from google.cloud.spanner_admin_database_v1.types import spanner_database_admin

    database_admin_api = spanner_client.database_admin_api
    db_path = database_admin_api.database_path(
        spanner_client.project, instance_id, database_id
    )
    db = database_admin_api.get_database(name=db_path)

    # Verify it was restored from the correct backup
    restore_info = db.restore_info
    assert restore_info is not None
    assert backup_id in restore_info.backup_info.backup

    if kms_key_name:
        assert kms_key_name in db.encryption_config.kms_key_name
    if kms_key_names:
        assert kms_key_names[0] in db.encryption_config.kms_key_names[0]

    # Verify/Wait until the state is either READY or READY_OPTIMIZING
    for _ in range(40):  # Wait up to 20 minutes
        if db.state in (
            spanner_database_admin.Database.State.READY,
            spanner_database_admin.Database.State.READY_OPTIMIZING,
        ):
            break
        time.sleep(30)
        db = database_admin_api.get_database(name=db_path)

    assert db.state in (
        spanner_database_admin.Database.State.READY,
        spanner_database_admin.Database.State.READY_OPTIMIZING,
    )


RESTORE_DB_ID = unique_database_id()
BACKUP_ID = unique_backup_id()
CMEK_RESTORE_DB_ID = unique_database_id()
CMEK_BACKUP_ID = unique_backup_id()
RETENTION_DATABASE_ID = unique_database_id()
RETENTION_PERIOD = "7d"
COPY_BACKUP_ID = unique_backup_id()


@pytest.mark.dependency(name="create_backup")
def test_create_backup(capsys, instance_id, sample_database):
    version_time = None
    with sample_database.snapshot() as snapshot:
        results = snapshot.execute_sql("SELECT CURRENT_TIMESTAMP()")
        version_time = list(results)[0][0]

    backup_sample.create_backup(
        instance_id,
        sample_database.database_id,
        BACKUP_ID,
        version_time,
    )
    out, _ = capsys.readouterr()
    assert BACKUP_ID in out


@pytest.mark.dependency(name="copy_backup", depends=["create_backup"])
def test_copy_backup(capsys, instance_id, spanner_client):
    source_backp_path = (
        spanner_client.project_name
        + "/instances/"
        + instance_id
        + "/backups/"
        + BACKUP_ID
    )
    backup_sample.copy_backup(instance_id, COPY_BACKUP_ID, source_backp_path)
    out, _ = capsys.readouterr()
    assert COPY_BACKUP_ID in out


@pytest.mark.dependency(name="create_backup_with_encryption_key")
def test_create_backup_with_encryption_key(
    capsys,
    instance_id,
    sample_database,
    kms_key_name,
):
    backup_sample.create_backup_with_encryption_key(
        instance_id,
        sample_database.database_id,
        CMEK_BACKUP_ID,
        kms_key_name,
    )
    out, _ = capsys.readouterr()
    assert CMEK_BACKUP_ID in out
    assert kms_key_name in out


@pytest.mark.skip(reason="skipped since the KMS keys are not added on test project")
@pytest.mark.dependency(name="create_backup_with_multiple_kms_keys")
def test_create_backup_with_multiple_kms_keys(
    capsys,
    multi_region_instance,
    multi_region_instance_id,
    sample_multi_region_database,
    kms_key_names,
):
    backup_sample.create_backup_with_multiple_kms_keys(
        multi_region_instance_id,
        sample_multi_region_database.database_id,
        CMEK_BACKUP_ID,
        kms_key_names,
    )
    out, _ = capsys.readouterr()
    assert CMEK_BACKUP_ID in out
    assert kms_key_names[0] in out
    assert kms_key_names[1] in out
    assert kms_key_names[2] in out


@pytest.mark.skip(reason="skipped since the KMS keys are not added on test project")
@pytest.mark.dependency(depends=["create_backup_with_multiple_kms_keys"])
def test_copy_backup_with_multiple_kms_keys(
    capsys, multi_region_instance_id, spanner_client, kms_key_names
):
    source_backup_path = (
        spanner_client.project_name
        + "/instances/"
        + multi_region_instance_id
        + "/backups/"
        + CMEK_BACKUP_ID
    )
    backup_sample.copy_backup_with_multiple_kms_keys(
        multi_region_instance_id, COPY_BACKUP_ID, source_backup_path, kms_key_names
    )
    out, _ = capsys.readouterr()
    assert COPY_BACKUP_ID in out


@pytest.mark.dependency(depends=["create_backup"])
@RetryErrors(exception=(DeadlineExceeded, TimeoutError), max_tries=2)
def test_restore_database(capsys, instance_id, sample_database, spanner_client):
    try:
        backup_sample.restore_database(instance_id, RESTORE_DB_ID, BACKUP_ID)
        out, _ = capsys.readouterr()
        assert (sample_database.database_id + " restored to ") in out
        assert (RESTORE_DB_ID + " from backup ") in out
        assert BACKUP_ID in out
    except AlreadyExists:
        _verify_restored_database(spanner_client, instance_id, RESTORE_DB_ID, BACKUP_ID)


@pytest.mark.dependency(depends=["create_backup_with_encryption_key"])
@RetryErrors(exception=(DeadlineExceeded, TimeoutError), max_tries=2)
def test_restore_database_with_encryption_key(
    capsys,
    instance_id,
    sample_database,
    kms_key_name,
    spanner_client,
):
    try:
        backup_sample.restore_database_with_encryption_key(
            instance_id, CMEK_RESTORE_DB_ID, CMEK_BACKUP_ID, kms_key_name
        )
        out, _ = capsys.readouterr()
        assert (sample_database.database_id + " restored to ") in out
        assert (CMEK_RESTORE_DB_ID + " from backup ") in out
        assert CMEK_BACKUP_ID in out
        assert kms_key_name in out
    except AlreadyExists:
        _verify_restored_database(
            spanner_client,
            instance_id,
            CMEK_RESTORE_DB_ID,
            CMEK_BACKUP_ID,
            kms_key_name=kms_key_name,
        )


@pytest.mark.skip(reason="skipped since the KMS keys are not added on test project")
@pytest.mark.dependency(depends=["create_backup_with_multiple_kms_keys"])
@RetryErrors(exception=(DeadlineExceeded, TimeoutError), max_tries=2)
def test_restore_database_with_multiple_kms_keys(
    capsys,
    multi_region_instance_id,
    sample_multi_region_database,
    kms_key_names,
    spanner_client,
):
    try:
        backup_sample.restore_database_with_multiple_kms_keys(
            multi_region_instance_id, CMEK_RESTORE_DB_ID, CMEK_BACKUP_ID, kms_key_names
        )
        out, _ = capsys.readouterr()
        assert (sample_multi_region_database.database_id + " restored to ") in out
        assert (CMEK_RESTORE_DB_ID + " from backup ") in out
        assert CMEK_BACKUP_ID in out
        assert kms_key_names[0] in out
        assert kms_key_names[1] in out
        assert kms_key_names[2] in out
    except AlreadyExists:
        _verify_restored_database(
            spanner_client,
            multi_region_instance_id,
            CMEK_RESTORE_DB_ID,
            CMEK_BACKUP_ID,
            kms_key_names=kms_key_names,
        )


@pytest.mark.dependency(depends=["create_backup", "copy_backup"])
def test_list_backup_operations(capsys, instance_id, sample_database):
    backup_sample.list_backup_operations(
        instance_id, sample_database.database_id, BACKUP_ID
    )
    out, _ = capsys.readouterr()
    assert BACKUP_ID in out
    assert sample_database.database_id in out
    assert COPY_BACKUP_ID in out
    print(out)


@pytest.mark.dependency(name="list_backup", depends=["create_backup", "copy_backup"])
def test_list_backups(
    capsys,
    instance_id,
    sample_database,
):
    backup_sample.list_backups(
        instance_id,
        sample_database.database_id,
        BACKUP_ID,
    )
    out, _ = capsys.readouterr()
    id_count = out.count(BACKUP_ID)
    assert id_count == 7


@pytest.mark.dependency(depends=["create_backup"])
def test_update_backup(capsys, instance_id):
    backup_sample.update_backup(instance_id, BACKUP_ID)
    out, _ = capsys.readouterr()
    assert BACKUP_ID in out


@pytest.mark.dependency(depends=["create_backup", "copy_backup", "list_backup"])
def test_delete_backup(capsys, instance_id):
    backup_sample.delete_backup(instance_id, BACKUP_ID)
    out, _ = capsys.readouterr()
    assert BACKUP_ID in out
    backup_sample.delete_backup(instance_id, COPY_BACKUP_ID)
    out, _ = capsys.readouterr()
    assert COPY_BACKUP_ID in out


@pytest.mark.dependency(depends=["create_backup"])
def test_cancel_backup(capsys, instance_id, sample_database):
    backup_sample.cancel_backup(
        instance_id,
        sample_database.database_id,
        BACKUP_ID,
    )
    out, _ = capsys.readouterr()
    cancel_success = "Backup creation was successfully cancelled." in out
    cancel_failure = ("Backup was created before the cancel completed." in out) and (
        "Backup deleted." in out
    )
    assert cancel_success or cancel_failure


@RetryErrors(exception=(DeadlineExceeded, TimeoutError), max_tries=2)
def test_create_database_with_retention_period(capsys, sample_instance):
    backup_sample.create_database_with_version_retention_period(
        sample_instance.instance_id,
        RETENTION_DATABASE_ID,
        RETENTION_PERIOD,
    )
    out, _ = capsys.readouterr()
    assert (RETENTION_DATABASE_ID + " created with ") in out
    assert ("retention period " + RETENTION_PERIOD) in out
    database = sample_instance.database(RETENTION_DATABASE_ID)
    database.drop()
