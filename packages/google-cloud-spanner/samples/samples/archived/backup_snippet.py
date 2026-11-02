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

"""This application demonstrates how to create and restore from backups
using Cloud Spanner.

For more information, see the README.rst under /spanner.
"""

import time
from datetime import datetime, timedelta

from google.cloud import spanner


# [START spanner_cancel_backup_create]
def cancel_backup(instance_id, database_id, backup_id):
    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)
    database = instance.database(database_id)

    expire_time = datetime.utcnow() + timedelta(days=30)

    # Create a backup.
    backup = instance.backup(backup_id, database=database, expire_time=expire_time)
    operation = backup.create()

    # Cancel backup creation.
    operation.cancel()

    # Cancel operations are best effort so either it will complete or
    # be cancelled.
    while not operation.done():
        time.sleep(300)  # 5 mins

    # Deal with resource if the operation succeeded.
    if backup.exists():
        print("Backup was created before the cancel completed.")
        backup.delete()
        print("Backup deleted.")
    else:
        print("Backup creation was successfully cancelled.")


# [END spanner_cancel_backup_create]


# [START spanner_copy_backup]
def copy_backup(instance_id, backup_id, source_backup_path):
    """Copies a backup."""
    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)

    # Create a backup object and wait for copy backup operation to complete.
    expire_time = datetime.utcnow() + timedelta(days=14)
    copy_backup = instance.copy_backup(
        backup_id=backup_id, source_backup=source_backup_path, expire_time=expire_time
    )
    operation = copy_backup.create()

    # Wait for copy backup operation to complete.
    operation.result(2100)

    # Verify that the copy backup is ready.
    copy_backup.reload()
    assert copy_backup.is_ready() is True

    print(
        "Backup {} of size {} bytes was created at {} with version time {}".format(
            copy_backup.name,
            copy_backup.size_bytes,
            copy_backup.create_time,
            copy_backup.version_time,
        )
    )


# [END spanner_copy_backup]


# [START spanner_create_backup]
def create_backup(instance_id, database_id, backup_id, version_time):
    """Creates a backup for a database."""
    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)
    database = instance.database(database_id)

    # Create a backup
    expire_time = datetime.utcnow() + timedelta(days=14)
    backup = instance.backup(
        backup_id, database=database, expire_time=expire_time, version_time=version_time
    )
    operation = backup.create()

    # Wait for backup operation to complete.
    operation.result(2100)

    # Verify that the backup is ready.
    backup.reload()
    assert backup.is_ready() is True

    # Get the name, create time and backup size.
    backup.reload()
    print(
        "Backup {} of size {} bytes was created at {} for version of database at {}".format(
            backup.name, backup.size_bytes, backup.create_time, backup.version_time
        )
    )


# [END spanner_create_backup]


# [START spanner_create_backup_with_encryption_key]
def create_backup_with_encryption_key(
    instance_id, database_id, backup_id, kms_key_name
):
    """Creates a backup for a database using a Customer Managed Encryption Key (CMEK)."""
    from google.cloud.spanner_admin_database_v1 import CreateBackupEncryptionConfig

    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)
    database = instance.database(database_id)

    # Create a backup
    expire_time = datetime.utcnow() + timedelta(days=14)
    encryption_config = {
        "encryption_type": CreateBackupEncryptionConfig.EncryptionType.CUSTOMER_MANAGED_ENCRYPTION,
        "kms_key_name": kms_key_name,
    }
    backup = instance.backup(
        backup_id,
        database=database,
        expire_time=expire_time,
        encryption_config=encryption_config,
    )
    operation = backup.create()

    # Wait for backup operation to complete.
    operation.result(2100)

    # Verify that the backup is ready.
    backup.reload()
    assert backup.is_ready() is True

    # Get the name, create time, backup size and encryption key.
    backup.reload()
    print(
        "Backup {} of size {} bytes was created at {} using encryption key {}".format(
            backup.name, backup.size_bytes, backup.create_time, kms_key_name
        )
    )


# [END spanner_create_backup_with_encryption_key]


# [START spanner_create_database_with_version_retention_period]
def create_database_with_version_retention_period(
    instance_id, database_id, retention_period
):
    """Creates a database with a version retention period."""
    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)
    ddl_statements = [
        "CREATE TABLE Singers ("
        + "  SingerId   INT64 NOT NULL,"
        + "  FirstName  STRING(1024),"
        + "  LastName   STRING(1024),"
        + "  SingerInfo BYTES(MAX)"
        + ") PRIMARY KEY (SingerId)",
        "CREATE TABLE Albums ("
        + "  SingerId     INT64 NOT NULL,"
        + "  AlbumId      INT64 NOT NULL,"
        + "  AlbumTitle   STRING(MAX)"
        + ") PRIMARY KEY (SingerId, AlbumId),"
        + "  INTERLEAVE IN PARENT Singers ON DELETE CASCADE",
        "ALTER DATABASE `{}` SET OPTIONS (version_retention_period = '{}')".format(
            database_id, retention_period
        ),
    ]
    db = instance.database(database_id, ddl_statements)
    operation = db.create()

    operation.result(30)

    db.reload()

    print(
        "Database {} created with version retention period {} and earliest version time {}".format(
            db.database_id, db.version_retention_period, db.earliest_version_time
        )
    )

    db.drop()


# [END spanner_create_database_with_version_retention_period]


# [START spanner_delete_backup]
def delete_backup(instance_id, backup_id):
    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)
    backup = instance.backup(backup_id)
    backup.reload()

    # Wait for databases that reference this backup to finish optimizing.
    while backup.referencing_databases:
        time.sleep(30)
        backup.reload()

    # Delete the backup.
    backup.delete()

    # Verify that the backup is deleted.
    assert backup.exists() is False
    print("Backup {} has been deleted.".format(backup.name))


# [END spanner_delete_backup]


# [START spanner_list_backup_operations]
def list_backup_operations(instance_id, database_id, backup_id):
    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)

    # List the CreateBackup operations.
    filter_ = (
        "(metadata.@type:type.googleapis.com/"
        "google.spanner.admin.database.v1.CreateBackupMetadata) "
        "AND (metadata.database:{})"
    ).format(database_id)
    operations = instance.list_backup_operations(filter_=filter_)
    for op in operations:
        metadata = op.metadata
        print(
            "Backup {} on database {}: {}% complete.".format(
                metadata.name, metadata.database, metadata.progress.progress_percent
            )
        )

    # List the CopyBackup operations.
    filter_ = (
        "(metadata.@type:type.googleapis.com/google.spanner.admin.database.v1.CopyBackupMetadata) "
        "AND (metadata.source_backup:{})"
    ).format(backup_id)
    operations = instance.list_backup_operations(filter_=filter_)
    for op in operations:
        metadata = op.metadata
        print(
            "Backup {} on source backup {}: {}% complete.".format(
                metadata.name,
                metadata.source_backup,
                metadata.progress.progress_percent,
            )
        )


# [END spanner_list_backup_operations]


# [START spanner_list_backups]
def list_backups(instance_id, database_id, backup_id):
    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)

    # List all backups.
    print("All backups:")
    for backup in instance.list_backups():
        print(backup.name)

    # List all backups that contain a name.
    print('All backups with backup name containing "{}":'.format(backup_id))
    for backup in instance.list_backups(filter_="name:{}".format(backup_id)):
        print(backup.name)

    # List all backups for a database that contains a name.
    print('All backups with database name containing "{}":'.format(database_id))
    for backup in instance.list_backups(filter_="database:{}".format(database_id)):
        print(backup.name)

    # List all backups that expire before a timestamp.
    expire_time = datetime.utcnow().replace(microsecond=0) + timedelta(days=30)
    print(
        'All backups with expire_time before "{}-{}-{}T{}:{}:{}Z":'.format(
            *expire_time.timetuple()
        )
    )
    for backup in instance.list_backups(
        filter_='expire_time < "{}-{}-{}T{}:{}:{}Z"'.format(*expire_time.timetuple())
    ):
        print(backup.name)

    # List all backups with a size greater than some bytes.
    print("All backups with backup size more than 100 bytes:")
    for backup in instance.list_backups(filter_="size_bytes > 100"):
        print(backup.name)

    # List backups that were created after a timestamp that are also ready.
    create_time = datetime.utcnow().replace(microsecond=0) - timedelta(days=1)
    print(
        'All backups created after "{}-{}-{}T{}:{}:{}Z" and are READY:'.format(
            *create_time.timetuple()
        )
    )
    for backup in instance.list_backups(
        filter_='create_time >= "{}-{}-{}T{}:{}:{}Z" AND state:READY'.format(
            *create_time.timetuple()
        )
    ):
        print(backup.name)

    print("All backups with pagination")
    # If there are multiple pages, additional ``ListBackup``
    # requests will be made as needed while iterating.
    paged_backups = set()
    for backup in instance.list_backups(page_size=2):
        paged_backups.add(backup.name)
    for backup in paged_backups:
        print(backup)


# [END spanner_list_backups]


# [START spanner_list_database_operations]
def list_database_operations(instance_id):
    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)

    # List the progress of restore.
    filter_ = (
        "(metadata.@type:type.googleapis.com/"
        "google.spanner.admin.database.v1.OptimizeRestoredDatabaseMetadata)"
    )
    operations = instance.list_database_operations(filter_=filter_)
    for op in operations:
        print(
            "Database {} restored from backup is {}% optimized.".format(
                op.metadata.name, op.metadata.progress.progress_percent
            )
        )


# [END spanner_list_database_operations]


# [START spanner_restore_backup]
def restore_database(instance_id, new_database_id, backup_id):
    """Restores a database from a backup."""
    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)
    # Create a backup on database_id.

    # Start restoring an existing backup to a new database.
    backup = instance.backup(backup_id)
    new_database = instance.database(new_database_id)
    operation = new_database.restore(backup)

    # Wait for restore operation to complete.
    operation.result(1600)

    # Newly created database has restore information.
    new_database.reload()
    restore_info = new_database.restore_info
    print(
        "Database {} restored to {} from backup {} with version time {}.".format(
            restore_info.backup_info.source_database,
            new_database_id,
            restore_info.backup_info.backup,
            restore_info.backup_info.version_time,
        )
    )


# [END spanner_restore_backup]


# [START spanner_restore_backup_with_encryption_key]
def restore_database_with_encryption_key(
    instance_id, new_database_id, backup_id, kms_key_name
):
    """Restores a database from a backup using a Customer Managed Encryption Key (CMEK)."""
    from google.cloud.spanner_admin_database_v1 import RestoreDatabaseEncryptionConfig

    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)

    # Start restoring an existing backup to a new database.
    backup = instance.backup(backup_id)
    encryption_config = {
        "encryption_type": RestoreDatabaseEncryptionConfig.EncryptionType.CUSTOMER_MANAGED_ENCRYPTION,
        "kms_key_name": kms_key_name,
    }
    new_database = instance.database(
        new_database_id, encryption_config=encryption_config
    )
    operation = new_database.restore(backup)

    # Wait for restore operation to complete.
    operation.result(1600)

    # Newly created database has restore information.
    new_database.reload()
    restore_info = new_database.restore_info
    print(
        "Database {} restored to {} from backup {} with using encryption key {}.".format(
            restore_info.backup_info.source_database,
            new_database_id,
            restore_info.backup_info.backup,
            new_database.encryption_config.kms_key_name,
        )
    )


# [END spanner_restore_backup_with_encryption_key]


# [START spanner_update_backup]
def update_backup(instance_id, backup_id):
    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)
    backup = instance.backup(backup_id)
    backup.reload()

    # Expire time must be within 366 days of the create time of the backup.
    old_expire_time = backup.expire_time
    # New expire time should be less than the max expire time
    new_expire_time = min(backup.max_expire_time, old_expire_time + timedelta(days=30))
    backup.update_expire_time(new_expire_time)
    print(
        "Backup {} expire time was updated from {} to {}.".format(
            backup.name, old_expire_time, new_expire_time
        )
    )


# [END spanner_update_backup]
