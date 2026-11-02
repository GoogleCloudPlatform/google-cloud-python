# Copyright 2024 Google Inc. All Rights Reserved.
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

import backup_snippet
import pytest
from google.api_core.exceptions import DeadlineExceeded
from test_utils.retry import RetryErrors


def unique_database_id():
    """Creates a unique id for the database."""
    return f"test-db-{uuid.uuid4().hex[:10]}"


def unique_backup_id():
    """Creates a unique id for the backup."""
    return f"test-backup-{uuid.uuid4().hex[:10]}"


RESTORE_DB_ID = unique_database_id()
BACKUP_ID = unique_backup_id()
CMEK_RESTORE_DB_ID = unique_database_id()
CMEK_BACKUP_ID = unique_backup_id()
RETENTION_DATABASE_ID = unique_database_id()
RETENTION_PERIOD = "7d"
COPY_BACKUP_ID = unique_backup_id()


@pytest.mark.dependency(name="create_backup")
def test_create_backup(capsys, instance_id, sample_database):
    with sample_database.snapshot() as snapshot:
        results = snapshot.execute_sql("SELECT CURRENT_TIMESTAMP()")
        version_time = list(results)[0][0]

    backup_snippet.create_backup(
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
    backup_snippet.copy_backup(instance_id, COPY_BACKUP_ID, source_backp_path)
    out, _ = capsys.readouterr()
    assert COPY_BACKUP_ID in out


@pytest.mark.dependency(name="create_backup_with_encryption_key")
def test_create_backup_with_encryption_key(
    capsys,
    instance_id,
    sample_database,
    kms_key_name,
):
    backup_snippet.create_backup_with_encryption_key(
        instance_id,
        sample_database.database_id,
        CMEK_BACKUP_ID,
        kms_key_name,
    )
    out, _ = capsys.readouterr()
    assert CMEK_BACKUP_ID in out
    assert kms_key_name in out


@pytest.mark.skip(
    reason="same test passes on unarchived test suite, "
    "but fails here. Needs investigation"
)
@pytest.mark.dependency(depends=["create_backup"])
@RetryErrors(exception=DeadlineExceeded, max_tries=2)
def test_restore_database(capsys, instance_id, sample_database):
    backup_snippet.restore_database(instance_id, RESTORE_DB_ID, BACKUP_ID)
    out, _ = capsys.readouterr()
    assert (sample_database.database_id + " restored to ") in out
    assert (RESTORE_DB_ID + " from backup ") in out
    assert BACKUP_ID in out


@pytest.mark.skip(
    reason="same test passes on unarchived test suite, "
    "but fails here. Needs investigation"
)
@pytest.mark.dependency(depends=["create_backup_with_encryption_key"])
@RetryErrors(exception=DeadlineExceeded, max_tries=2)
def test_restore_database_with_encryption_key(
    capsys,
    instance_id,
    sample_database,
    kms_key_name,
):
    backup_snippet.restore_database_with_encryption_key(
        instance_id, CMEK_RESTORE_DB_ID, CMEK_BACKUP_ID, kms_key_name
    )
    out, _ = capsys.readouterr()
    assert (sample_database.database_id + " restored to ") in out
    assert (CMEK_RESTORE_DB_ID + " from backup ") in out
    assert CMEK_BACKUP_ID in out
    assert kms_key_name in out


@pytest.mark.dependency(depends=["create_backup", "copy_backup"])
def test_list_backup_operations(capsys, instance_id, sample_database):
    backup_snippet.list_backup_operations(
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
    backup_snippet.list_backups(
        instance_id,
        sample_database.database_id,
        BACKUP_ID,
    )
    out, _ = capsys.readouterr()
    id_count = out.count(BACKUP_ID)
    assert id_count == 7


@pytest.mark.dependency(depends=["create_backup"])
def test_update_backup(capsys, instance_id):
    backup_snippet.update_backup(instance_id, BACKUP_ID)
    out, _ = capsys.readouterr()
    assert BACKUP_ID in out


@pytest.mark.dependency(depends=["create_backup", "copy_backup", "list_backup"])
def test_delete_backup(capsys, instance_id):
    backup_snippet.delete_backup(instance_id, BACKUP_ID)
    out, _ = capsys.readouterr()
    assert BACKUP_ID in out
    backup_snippet.delete_backup(instance_id, COPY_BACKUP_ID)
    out, _ = capsys.readouterr()
    assert "has been deleted." in out
    assert COPY_BACKUP_ID in out


@pytest.mark.dependency(depends=["create_backup"])
def test_cancel_backup(capsys, instance_id, sample_database):
    backup_snippet.cancel_backup(
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


@RetryErrors(exception=DeadlineExceeded, max_tries=2)
def test_create_database_with_retention_period(capsys, sample_instance):
    backup_snippet.create_database_with_version_retention_period(
        sample_instance.instance_id,
        RETENTION_DATABASE_ID,
        RETENTION_PERIOD,
    )
    out, _ = capsys.readouterr()
    assert (RETENTION_DATABASE_ID + " created with ") in out
    assert ("retention period " + RETENTION_PERIOD) in out
