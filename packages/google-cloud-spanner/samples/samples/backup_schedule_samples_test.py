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

import pytest

import backup_schedule_samples as samples

__FULL_BACKUP_SCHEDULE_ID = "full-backup-schedule"
__INCREMENTAL_BACKUP_SCHEDULE_ID = "incremental-backup-schedule"


@pytest.fixture(scope="module")
def database_id():
    return f"test-db-{uuid.uuid4().hex[:10]}"


@pytest.mark.dependency(name="create_full_backup_schedule")
def test_create_full_backup_schedule(
    capsys,
    sample_instance,
    sample_database,
) -> None:
    samples.create_full_backup_schedule(
        sample_instance.instance_id,
        sample_database.database_id,
        __FULL_BACKUP_SCHEDULE_ID,
    )
    out, _ = capsys.readouterr()
    assert "Created full backup schedule" in out
    assert (
        f"/instances/{sample_instance.instance_id}"
        f"/databases/{sample_database.database_id}"
        f"/backupSchedules/{__FULL_BACKUP_SCHEDULE_ID}"
    ) in out


@pytest.mark.dependency(name="create_incremental_backup_schedule")
def test_create_incremental_backup_schedule(
    capsys,
    sample_instance,
    sample_database,
) -> None:
    samples.create_incremental_backup_schedule(
        sample_instance.instance_id,
        sample_database.database_id,
        __INCREMENTAL_BACKUP_SCHEDULE_ID,
    )
    out, _ = capsys.readouterr()
    assert "Created incremental backup schedule" in out
    assert (
        f"/instances/{sample_instance.instance_id}"
        f"/databases/{sample_database.database_id}"
        f"/backupSchedules/{__INCREMENTAL_BACKUP_SCHEDULE_ID}"
    ) in out


@pytest.mark.dependency(
    depends=[
        "create_full_backup_schedule",
        "create_incremental_backup_schedule",
    ]
)
def test_list_backup_schedules(
    capsys,
    sample_instance,
    sample_database,
) -> None:
    samples.list_backup_schedules(
        sample_instance.instance_id,
        sample_database.database_id,
    )
    out, _ = capsys.readouterr()
    assert (
        f"/instances/{sample_instance.instance_id}"
        f"/databases/{sample_database.database_id}"
        f"/backupSchedules/{__FULL_BACKUP_SCHEDULE_ID}"
    ) in out
    assert (
        f"/instances/{sample_instance.instance_id}"
        f"/databases/{sample_database.database_id}"
        f"/backupSchedules/{__INCREMENTAL_BACKUP_SCHEDULE_ID}"
    ) in out


@pytest.mark.dependency(depends=["create_full_backup_schedule"])
def test_get_backup_schedule(
    capsys,
    sample_instance,
    sample_database,
) -> None:
    samples.get_backup_schedule(
        sample_instance.instance_id,
        sample_database.database_id,
        __FULL_BACKUP_SCHEDULE_ID,
    )
    out, _ = capsys.readouterr()
    assert (
        f"/instances/{sample_instance.instance_id}"
        f"/databases/{sample_database.database_id}"
        f"/backupSchedules/{__FULL_BACKUP_SCHEDULE_ID}"
    ) in out


@pytest.mark.dependency(depends=["create_full_backup_schedule"])
def test_update_backup_schedule(
    capsys,
    sample_instance,
    sample_database,
) -> None:
    samples.update_backup_schedule(
        sample_instance.instance_id,
        sample_database.database_id,
        __FULL_BACKUP_SCHEDULE_ID,
    )
    out, _ = capsys.readouterr()
    assert "Updated backup schedule" in out
    assert (
        f"/instances/{sample_instance.instance_id}"
        f"/databases/{sample_database.database_id}"
        f"/backupSchedules/{__FULL_BACKUP_SCHEDULE_ID}"
    ) in out


@pytest.mark.dependency(
    depends=[
        "create_full_backup_schedule",
        "create_incremental_backup_schedule",
    ]
)
def test_delete_backup_schedule(
    capsys,
    sample_instance,
    sample_database,
) -> None:
    samples.delete_backup_schedule(
        sample_instance.instance_id,
        sample_database.database_id,
        __FULL_BACKUP_SCHEDULE_ID,
    )
    samples.delete_backup_schedule(
        sample_instance.instance_id,
        sample_database.database_id,
        __INCREMENTAL_BACKUP_SCHEDULE_ID,
    )
    out, _ = capsys.readouterr()
    assert "Deleted backup schedule" in out
