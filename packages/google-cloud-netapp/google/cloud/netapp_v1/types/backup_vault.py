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

import google.protobuf.field_mask_pb2 as field_mask_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.netapp.v1",
    manifest={
        "BackupVault",
        "GetBackupVaultRequest",
        "ListBackupVaultsRequest",
        "ListBackupVaultsResponse",
        "CreateBackupVaultRequest",
        "DeleteBackupVaultRequest",
        "UpdateBackupVaultRequest",
    },
)


class BackupVault(proto.Message):
    r"""A NetApp BackupVault.

    Attributes:
        name (str):
            Identifier. The resource name of the backup vault. Format:
            ``projects/{project_id}/locations/{location}/backupVaults/{backup_vault_id}``.
        state (google.cloud.netapp_v1.types.BackupVault.State):
            Output only. The backup vault state.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Create time of the backup vault.
        description (str):
            Description of the backup vault.
        labels (MutableMapping[str, str]):
            Resource labels to represent user provided
            metadata.
        backup_vault_type (google.cloud.netapp_v1.types.BackupVault.BackupVaultType):
            Optional. Type of backup vault to be created. Default is
            IN_REGION.
        source_region (str):
            Optional. Region in which the backup vault is created.
            Format: ``projects/{project_id}/locations/{location}``
        backup_region (str):
            Optional. Region where the backups are stored. Format:
            ``projects/{project_id}/locations/{location}``
        source_backup_vault (str):
            Output only. Name of the Backup vault created in source
            region. Format:
            ``projects/{project_id}/locations/{location}/backupVaults/{backup_vault_id}``
        destination_backup_vault (str):
            Output only. Name of the Backup vault created in backup
            region. Format:
            ``projects/{project_id}/locations/{location}/backupVaults/{backup_vault_id}``
        backup_retention_policy (google.cloud.netapp_v1.types.BackupVault.BackupRetentionPolicy):
            Optional. Backup retention policy defining
            the retention of backups.
        kms_config (str):
            Optional. Specifies the Key Management System (KMS)
            configuration to be used for backup encryption. Format:
            ``projects/{project}/locations/{location}/kmsConfigs/{kms_config}``
        encryption_state (google.cloud.netapp_v1.types.BackupVault.EncryptionState):
            Output only. Field indicating encryption
            state of CMEK backups.
        backups_crypto_key_version (str):
            Output only. The crypto key version used to encrypt the
            backup vault. Format:
            ``projects/{project}/locations/{location}/keyRings/{key_ring}/cryptoKeys/{crypto_key}/cryptoKeyVersions/{crypto_key_version}``
    """

    class State(proto.Enum):
        r"""The Backup Vault States

        Values:
            STATE_UNSPECIFIED (0):
                State not set.
            CREATING (1):
                BackupVault is being created.
            READY (2):
                BackupVault is available for use.
            DELETING (3):
                BackupVault is being deleted.
            ERROR (4):
                BackupVault is not valid and cannot be used.
            UPDATING (5):
                BackupVault is being updated.
        """

        STATE_UNSPECIFIED = 0
        CREATING = 1
        READY = 2
        DELETING = 3
        ERROR = 4
        UPDATING = 5

    class BackupVaultType(proto.Enum):
        r"""Backup Vault Type.

        Values:
            BACKUP_VAULT_TYPE_UNSPECIFIED (0):
                BackupVault type not set.
            IN_REGION (1):
                BackupVault type is IN_REGION.
            CROSS_REGION (2):
                BackupVault type is CROSS_REGION.
        """

        BACKUP_VAULT_TYPE_UNSPECIFIED = 0
        IN_REGION = 1
        CROSS_REGION = 2

    class EncryptionState(proto.Enum):
        r"""Encryption state of customer-managed encryption keys (CMEK)
        backups.

        Values:
            ENCRYPTION_STATE_UNSPECIFIED (0):
                Encryption state not set.
            ENCRYPTION_STATE_PENDING (1):
                Encryption state is pending.
            ENCRYPTION_STATE_COMPLETED (2):
                Encryption is complete.
            ENCRYPTION_STATE_IN_PROGRESS (3):
                Encryption is in progress.
            ENCRYPTION_STATE_FAILED (4):
                Encryption has failed.
        """

        ENCRYPTION_STATE_UNSPECIFIED = 0
        ENCRYPTION_STATE_PENDING = 1
        ENCRYPTION_STATE_COMPLETED = 2
        ENCRYPTION_STATE_IN_PROGRESS = 3
        ENCRYPTION_STATE_FAILED = 4

    class BackupRetentionPolicy(proto.Message):
        r"""Retention policy for backups in the backup vault

        Attributes:
            backup_minimum_enforced_retention_days (int):
                Required. Minimum retention duration in days
                for backups in the backup vault.
            daily_backup_immutable (bool):
                Optional. Indicates if the daily backups are immutable. At
                least one of daily_backup_immutable,
                weekly_backup_immutable, monthly_backup_immutable and
                manual_backup_immutable must be true.
            weekly_backup_immutable (bool):
                Optional. Indicates if the weekly backups are immutable. At
                least one of daily_backup_immutable,
                weekly_backup_immutable, monthly_backup_immutable and
                manual_backup_immutable must be true.
            monthly_backup_immutable (bool):
                Optional. Indicates if the monthly backups are immutable. At
                least one of daily_backup_immutable,
                weekly_backup_immutable, monthly_backup_immutable and
                manual_backup_immutable must be true.
            manual_backup_immutable (bool):
                Optional. Indicates if the manual backups are immutable. At
                least one of daily_backup_immutable,
                weekly_backup_immutable, monthly_backup_immutable and
                manual_backup_immutable must be true.
        """

        backup_minimum_enforced_retention_days: int = proto.Field(
            proto.INT32,
            number=1,
        )
        daily_backup_immutable: bool = proto.Field(
            proto.BOOL,
            number=2,
        )
        weekly_backup_immutable: bool = proto.Field(
            proto.BOOL,
            number=3,
        )
        monthly_backup_immutable: bool = proto.Field(
            proto.BOOL,
            number=4,
        )
        manual_backup_immutable: bool = proto.Field(
            proto.BOOL,
            number=5,
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=2,
        enum=State,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    description: str = proto.Field(
        proto.STRING,
        number=4,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=5,
    )
    backup_vault_type: BackupVaultType = proto.Field(
        proto.ENUM,
        number=6,
        enum=BackupVaultType,
    )
    source_region: str = proto.Field(
        proto.STRING,
        number=7,
    )
    backup_region: str = proto.Field(
        proto.STRING,
        number=8,
    )
    source_backup_vault: str = proto.Field(
        proto.STRING,
        number=9,
    )
    destination_backup_vault: str = proto.Field(
        proto.STRING,
        number=10,
    )
    backup_retention_policy: BackupRetentionPolicy = proto.Field(
        proto.MESSAGE,
        number=11,
        message=BackupRetentionPolicy,
    )
    kms_config: str = proto.Field(
        proto.STRING,
        number=12,
    )
    encryption_state: EncryptionState = proto.Field(
        proto.ENUM,
        number=13,
        enum=EncryptionState,
    )
    backups_crypto_key_version: str = proto.Field(
        proto.STRING,
        number=14,
    )


class GetBackupVaultRequest(proto.Message):
    r"""GetBackupVaultRequest gets the state of a backupVault.

    Attributes:
        name (str):
            Required. The backupVault resource name, in the format
            ``projects/{project_id}/locations/{location}/backupVaults/{backup_vault_id}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListBackupVaultsRequest(proto.Message):
    r"""ListBackupVaultsRequest lists backupVaults.

    Attributes:
        parent (str):
            Required. The location for which to retrieve backupVault
            information, in the format
            ``projects/{project_id}/locations/{location}``.
        page_size (int):
            The maximum number of items to return.
        page_token (str):
            The next_page_token value to use if there are additional
            results to retrieve for this list request.
        order_by (str):
            Sort results. Supported values are "name",
            "name desc" or "" (unsorted).
        filter (str):
            List filter.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=2,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )
    order_by: str = proto.Field(
        proto.STRING,
        number=4,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=5,
    )


class ListBackupVaultsResponse(proto.Message):
    r"""ListBackupVaultsResponse is the result of
    ListBackupVaultsRequest.

    Attributes:
        backup_vaults (MutableSequence[google.cloud.netapp_v1.types.BackupVault]):
            A list of backupVaults in the project for the
            specified location.
        next_page_token (str):
            The token you can use to retrieve the next
            page of results. Not returned if there are no
            more results in the list.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    backup_vaults: MutableSequence["BackupVault"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="BackupVault",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class CreateBackupVaultRequest(proto.Message):
    r"""CreateBackupVaultRequest creates a backup vault.

    Attributes:
        parent (str):
            Required. The location to create the backup vaults, in the
            format ``projects/{project_id}/locations/{location}``
        backup_vault_id (str):
            Required. The ID to use for the backupVault.
            The ID must be unique within the specified
            location. Must contain only letters, numbers and
            hyphen, with the first character a letter, the
            last a letter or a
            number, and a 63 character maximum.
        backup_vault (google.cloud.netapp_v1.types.BackupVault):
            Required. A backupVault resource
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    backup_vault_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    backup_vault: "BackupVault" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="BackupVault",
    )


class DeleteBackupVaultRequest(proto.Message):
    r"""DeleteBackupVaultRequest deletes a backupVault.

    Attributes:
        name (str):
            Required. The backupVault resource name, in the format
            ``projects/{project_id}/locations/{location}/backupVaults/{backup_vault_id}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateBackupVaultRequest(proto.Message):
    r"""UpdateBackupVaultRequest updates description and/or labels
    for a backupVault.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. Field mask is used to specify the fields to be
            overwritten in the Backup resource to be updated. The fields
            specified in the update_mask are relative to the resource,
            not the full request. A field will be overwritten if it is
            in the mask. If the user does not provide a mask then all
            fields will be overwritten.
        backup_vault (google.cloud.netapp_v1.types.BackupVault):
            Required. The backupVault being updated
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    backup_vault: "BackupVault" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="BackupVault",
    )


__all__ = tuple(sorted(__protobuf__.manifest))
