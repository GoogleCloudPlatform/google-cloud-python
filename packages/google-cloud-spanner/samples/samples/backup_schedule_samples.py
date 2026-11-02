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

"""
This application demonstrates how to create and manage backup schedules using
Cloud Spanner.
"""

import argparse
from enum import Enum


# [START spanner_create_full_backup_schedule]
def create_full_backup_schedule(
    instance_id: str,
    database_id: str,
    schedule_id: str,
) -> None:
    from datetime import timedelta

    from google.cloud import spanner
    from google.cloud.spanner_admin_database_v1.types import (
        CreateBackupEncryptionConfig,
        FullBackupSpec,
    )
    from google.cloud.spanner_admin_database_v1.types import (
        backup_schedule as backup_schedule_pb,
    )

    client = spanner.Client()
    database_admin_api = client.database_admin_api

    request = backup_schedule_pb.CreateBackupScheduleRequest(
        parent=database_admin_api.database_path(
            client.project, instance_id, database_id
        ),
        backup_schedule_id=schedule_id,
        backup_schedule=backup_schedule_pb.BackupSchedule(
            spec=backup_schedule_pb.BackupScheduleSpec(
                cron_spec=backup_schedule_pb.CrontabSpec(
                    text="30 12 * * *",
                ),
            ),
            retention_duration=timedelta(hours=24),
            encryption_config=CreateBackupEncryptionConfig(
                encryption_type=CreateBackupEncryptionConfig.EncryptionType.USE_DATABASE_ENCRYPTION,
            ),
            full_backup_spec=FullBackupSpec(),
        ),
    )

    response = database_admin_api.create_backup_schedule(request)
    print(f"Created full backup schedule: {response}")


# [END spanner_create_full_backup_schedule]


# [START spanner_create_incremental_backup_schedule]
def create_incremental_backup_schedule(
    instance_id: str,
    database_id: str,
    schedule_id: str,
) -> None:
    from datetime import timedelta

    from google.cloud import spanner
    from google.cloud.spanner_admin_database_v1.types import (
        CreateBackupEncryptionConfig,
        IncrementalBackupSpec,
    )
    from google.cloud.spanner_admin_database_v1.types import (
        backup_schedule as backup_schedule_pb,
    )

    client = spanner.Client()
    database_admin_api = client.database_admin_api

    request = backup_schedule_pb.CreateBackupScheduleRequest(
        parent=database_admin_api.database_path(
            client.project, instance_id, database_id
        ),
        backup_schedule_id=schedule_id,
        backup_schedule=backup_schedule_pb.BackupSchedule(
            spec=backup_schedule_pb.BackupScheduleSpec(
                cron_spec=backup_schedule_pb.CrontabSpec(
                    text="30 12 * * *",
                ),
            ),
            retention_duration=timedelta(hours=24),
            encryption_config=CreateBackupEncryptionConfig(
                encryption_type=CreateBackupEncryptionConfig.EncryptionType.GOOGLE_DEFAULT_ENCRYPTION,
            ),
            incremental_backup_spec=IncrementalBackupSpec(),
        ),
    )

    response = database_admin_api.create_backup_schedule(request)
    print(f"Created incremental backup schedule: {response}")


# [END spanner_create_incremental_backup_schedule]


# [START spanner_list_backup_schedules]
def list_backup_schedules(instance_id: str, database_id: str) -> None:
    from google.cloud import spanner
    from google.cloud.spanner_admin_database_v1.types import (
        backup_schedule as backup_schedule_pb,
    )

    client = spanner.Client()
    database_admin_api = client.database_admin_api

    request = backup_schedule_pb.ListBackupSchedulesRequest(
        parent=database_admin_api.database_path(
            client.project,
            instance_id,
            database_id,
        ),
    )

    for backup_schedule in database_admin_api.list_backup_schedules(request):
        print(f"Backup schedule: {backup_schedule}")


# [END spanner_list_backup_schedules]


# [START spanner_get_backup_schedule]
def get_backup_schedule(
    instance_id: str,
    database_id: str,
    schedule_id: str,
) -> None:
    from google.cloud import spanner
    from google.cloud.spanner_admin_database_v1.types import (
        backup_schedule as backup_schedule_pb,
    )

    client = spanner.Client()
    database_admin_api = client.database_admin_api

    request = backup_schedule_pb.GetBackupScheduleRequest(
        name=database_admin_api.backup_schedule_path(
            client.project,
            instance_id,
            database_id,
            schedule_id,
        ),
    )

    response = database_admin_api.get_backup_schedule(request)
    print(f"Backup schedule: {response}")


# [END spanner_get_backup_schedule]


# [START spanner_update_backup_schedule]
def update_backup_schedule(
    instance_id: str,
    database_id: str,
    schedule_id: str,
) -> None:
    from datetime import timedelta

    from google.cloud import spanner
    from google.cloud.spanner_admin_database_v1.types import (
        CreateBackupEncryptionConfig,
    )
    from google.cloud.spanner_admin_database_v1.types import (
        backup_schedule as backup_schedule_pb,
    )
    from google.protobuf.field_mask_pb2 import FieldMask

    client = spanner.Client()
    database_admin_api = client.database_admin_api

    request = backup_schedule_pb.UpdateBackupScheduleRequest(
        backup_schedule=backup_schedule_pb.BackupSchedule(
            name=database_admin_api.backup_schedule_path(
                client.project,
                instance_id,
                database_id,
                schedule_id,
            ),
            spec=backup_schedule_pb.BackupScheduleSpec(
                cron_spec=backup_schedule_pb.CrontabSpec(
                    text="45 15 * * *",
                ),
            ),
            retention_duration=timedelta(hours=48),
            encryption_config=CreateBackupEncryptionConfig(
                encryption_type=CreateBackupEncryptionConfig.EncryptionType.USE_DATABASE_ENCRYPTION,
            ),
        ),
        update_mask=FieldMask(
            paths=[
                "spec.cron_spec.text",
                "retention_duration",
                "encryption_config",
            ],
        ),
    )

    response = database_admin_api.update_backup_schedule(request)
    print(f"Updated backup schedule: {response}")


# [END spanner_update_backup_schedule]


# [START spanner_delete_backup_schedule]
def delete_backup_schedule(
    instance_id: str,
    database_id: str,
    schedule_id: str,
) -> None:
    from google.cloud import spanner
    from google.cloud.spanner_admin_database_v1.types import (
        backup_schedule as backup_schedule_pb,
    )

    client = spanner.Client()
    database_admin_api = client.database_admin_api

    request = backup_schedule_pb.DeleteBackupScheduleRequest(
        name=database_admin_api.backup_schedule_path(
            client.project,
            instance_id,
            database_id,
            schedule_id,
        ),
    )

    database_admin_api.delete_backup_schedule(request)
    print("Deleted backup schedule")


# [END spanner_delete_backup_schedule]


class Command(Enum):
    CREATE_FULL_BACKUP_SCHEDULE = "create-full-backup-schedule"
    CREATE_INCREMENTAL_BACKUP_SCHEDULE = "create-incremental-backup-schedule"
    LIST_BACKUP_SCHEDULES = "list-backup-schedules"
    GET_BACKUP_SCHEDULE = "get-backup-schedule"
    UPDATE_BACKUP_SCHEDULE = "update-backup-schedule"
    DELETE_BACKUP_SCHEDULE = "delete-backup-schedule"

    def __str__(self):
        return self.value


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--instance-id", required=True)
    parser.add_argument("--database-id", required=True)
    parser.add_argument("--schedule-id", required=False)
    parser.add_argument(
        "command",
        type=Command,
        choices=list(Command),
    )
    args = parser.parse_args()

    if args.command == Command.CREATE_FULL_BACKUP_SCHEDULE:
        create_full_backup_schedule(
            args.instance_id,
            args.database_id,
            args.schedule_id,
        )
    elif args.command == Command.CREATE_INCREMENTAL_BACKUP_SCHEDULE:
        create_incremental_backup_schedule(
            args.instance_id,
            args.database_id,
            args.schedule_id,
        )
    elif args.command == Command.LIST_BACKUP_SCHEDULES:
        list_backup_schedules(
            args.instance_id,
            args.database_id,
        )
    elif args.command == Command.GET_BACKUP_SCHEDULE:
        get_backup_schedule(
            args.instance_id,
            args.database_id,
            args.schedule_id,
        )
    elif args.command == Command.UPDATE_BACKUP_SCHEDULE:
        update_backup_schedule(
            args.instance_id,
            args.database_id,
            args.schedule_id,
        )
    elif args.command == Command.DELETE_BACKUP_SCHEDULE:
        delete_backup_schedule(
            args.instance_id,
            args.database_id,
            args.schedule_id,
        )
    else:
        print(f"Unknown command: {args.command}")
