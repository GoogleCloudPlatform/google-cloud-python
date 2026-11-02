# -*- coding: utf-8 -*-
# Copyright 2026 Google LLC
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
#
from __future__ import annotations

from typing import MutableMapping, MutableSequence

import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.oracledatabase.v1",
    manifest={
        "AutonomousDatabaseBackup",
        "AutonomousDatabaseBackupProperties",
    },
)


class AutonomousDatabaseBackup(proto.Message):
    r"""Details of the Autonomous Database Backup resource.
    https://docs.oracle.com/en-us/iaas/api/#/en/database/20160918/AutonomousDatabaseBackup/

    Attributes:
        name (str):
            Identifier. The name of the Autonomous Database Backup
            resource with the format:
            projects/{project}/locations/{region}/autonomousDatabaseBackups/{autonomous_database_backup}
        autonomous_database (str):
            Required. The name of the Autonomous Database resource for
            which the backup is being created. Format:
            projects/{project}/locations/{region}/autonomousDatabases/{autonomous_database}
        display_name (str):
            Optional. User friendly name for the Backup.
            The name does not have to be unique.
        properties (google.cloud.oracledatabase_v1.types.AutonomousDatabaseBackupProperties):
            Optional. Various properties of the backup.
        labels (MutableMapping[str, str]):
            Optional. labels or tags associated with the
            resource.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    autonomous_database: str = proto.Field(
        proto.STRING,
        number=2,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=3,
    )
    properties: "AutonomousDatabaseBackupProperties" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="AutonomousDatabaseBackupProperties",
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=5,
    )


class AutonomousDatabaseBackupProperties(proto.Message):
    r"""Properties of the Autonomous Database Backup resource.

    Attributes:
        ocid (str):
            Output only. OCID of the Autonomous Database
            backup.
            https://docs.oracle.com/en-us/iaas/Content/General/Concepts/identifiers.htm#Oracle
        retention_period_days (int):
            Optional. Retention period in days for the
            backup.
        compartment_id (str):
            Output only. The OCID of the compartment.
        database_size_tb (float):
            Output only. The quantity of data in the
            database, in terabytes.
        db_version (str):
            Output only. A valid Oracle Database version
            for Autonomous Database.
        is_long_term_backup (bool):
            Output only. Indicates if the backup is long
            term backup.
        is_automatic_backup (bool):
            Output only. Indicates if the backup is
            automatic or user initiated.
        is_restorable (bool):
            Output only. Indicates if the backup can be
            used to restore the Autonomous Database.
        key_store_id (str):
            Optional. The OCID of the key store of Oracle
            Vault.
        key_store_wallet (str):
            Optional. The wallet name for Oracle Key
            Vault.
        kms_key_id (str):
            Optional. The OCID of the key container that
            is used as the master encryption key in database
            transparent data encryption (TDE) operations.
        kms_key_version_id (str):
            Optional. The OCID of the key container
            version that is used in database transparent
            data encryption (TDE) operations KMS Key can
            have multiple key versions. If none is
            specified, the current key version (latest) of
            the Key Id is used for the operation. Autonomous
            Database Serverless does not use key versions,
            hence is not applicable for Autonomous Database
            Serverless instances.
        lifecycle_details (str):
            Output only. Additional information about the
            current lifecycle state.
        lifecycle_state (google.cloud.oracledatabase_v1.types.AutonomousDatabaseBackupProperties.State):
            Output only. The lifecycle state of the
            backup.
        size_tb (float):
            Output only. The backup size in terabytes.
        available_till_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Timestamp until when the backup
            will be available.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The date and time the backup
            completed.
        start_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The date and time the backup
            started.
        type_ (google.cloud.oracledatabase_v1.types.AutonomousDatabaseBackupProperties.Type):
            Output only. The type of the backup.
        vault_id (str):
            Optional. The OCID of the vault.
    """

    class State(proto.Enum):
        r"""// The various lifecycle states of the Autonomous Database
        Backup.

        Values:
            STATE_UNSPECIFIED (0):
                Default unspecified value.
            CREATING (1):
                Indicates that the resource is in creating
                state.
            ACTIVE (2):
                Indicates that the resource is in active
                state.
            DELETING (3):
                Indicates that the resource is in deleting
                state.
            DELETED (4):
                Indicates that the resource is in deleted
                state.
            FAILED (6):
                Indicates that the resource is in failed
                state.
            UPDATING (7):
                Indicates that the resource is in updating
                state.
        """

        STATE_UNSPECIFIED = 0
        CREATING = 1
        ACTIVE = 2
        DELETING = 3
        DELETED = 4
        FAILED = 6
        UPDATING = 7

    class Type(proto.Enum):
        r"""The type of the backup.

        Values:
            TYPE_UNSPECIFIED (0):
                Default unspecified value.
            INCREMENTAL (1):
                Incremental backups.
            FULL (2):
                Full backups.
            LONG_TERM (3):
                Long term backups.
        """

        TYPE_UNSPECIFIED = 0
        INCREMENTAL = 1
        FULL = 2
        LONG_TERM = 3

    ocid: str = proto.Field(
        proto.STRING,
        number=1,
    )
    retention_period_days: int = proto.Field(
        proto.INT32,
        number=2,
    )
    compartment_id: str = proto.Field(
        proto.STRING,
        number=3,
    )
    database_size_tb: float = proto.Field(
        proto.FLOAT,
        number=4,
    )
    db_version: str = proto.Field(
        proto.STRING,
        number=5,
    )
    is_long_term_backup: bool = proto.Field(
        proto.BOOL,
        number=6,
    )
    is_automatic_backup: bool = proto.Field(
        proto.BOOL,
        number=7,
    )
    is_restorable: bool = proto.Field(
        proto.BOOL,
        number=8,
    )
    key_store_id: str = proto.Field(
        proto.STRING,
        number=9,
    )
    key_store_wallet: str = proto.Field(
        proto.STRING,
        number=10,
    )
    kms_key_id: str = proto.Field(
        proto.STRING,
        number=11,
    )
    kms_key_version_id: str = proto.Field(
        proto.STRING,
        number=12,
    )
    lifecycle_details: str = proto.Field(
        proto.STRING,
        number=13,
    )
    lifecycle_state: State = proto.Field(
        proto.ENUM,
        number=14,
        enum=State,
    )
    size_tb: float = proto.Field(
        proto.FLOAT,
        number=15,
    )
    available_till_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=16,
        message=timestamp_pb2.Timestamp,
    )
    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=17,
        message=timestamp_pb2.Timestamp,
    )
    start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=18,
        message=timestamp_pb2.Timestamp,
    )
    type_: Type = proto.Field(
        proto.ENUM,
        number=19,
        enum=Type,
    )
    vault_id: str = proto.Field(
        proto.STRING,
        number=20,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
