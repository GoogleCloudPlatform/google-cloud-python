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
        "Backup",
        "ListBackupsRequest",
        "ListBackupsResponse",
        "GetBackupRequest",
        "CreateBackupRequest",
        "DeleteBackupRequest",
        "UpdateBackupRequest",
        "OntapSource",
    },
)


class Backup(proto.Message):
    r"""A NetApp Backup.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Identifier. The resource name of the backup. Format:
            ``projects/{project_id}/locations/{location}/backupVaults/{backup_vault_id}/backups/{backup_id}``.
        state (google.cloud.netapp_v1.types.Backup.State):
            Output only. The backup state.
        description (str):
            A description of the backup with 2048
            characters or less. Requests with longer
            descriptions will be rejected.
        volume_usage_bytes (int):
            Output only. Size of the file system when the
            backup was created. When creating a new volume
            from the backup, the volume capacity will have
            to be at least as big.
        backup_type (google.cloud.netapp_v1.types.Backup.Type):
            Output only. Type of backup, manually created
            or created by a backup policy.
        source_volume (str):
            The resource name of the volume that this backup belongs to.
            You must provide either ``source_volume`` or
            ``ontap_source``. Format:
            ``projects/{project_id}/locations/{location}/volumes/{volume_id}``
        source_snapshot (str):
            If specified, backup will be created from the given
            snapshot. If not specified, there will be a new snapshot
            taken to initiate the backup creation. Format:
            ``projects/{project_id}/locations/{location}/volumes/{volume_id}/snapshots/{snapshot_id}``

            This field is a member of `oneof`_ ``_source_snapshot``.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the backup was
            created.
        labels (MutableMapping[str, str]):
            Resource labels to represent user provided
            metadata.
        chain_storage_bytes (int):
            Output only. Total size of all backups in a
            chain in bytes = baseline backup size +
            sum(incremental backup size)
        satisfies_pzs (bool):
            Output only. Reserved for future use
        satisfies_pzi (bool):
            Output only. Reserved for future use
        volume_region (str):
            Output only. Region of the volume from which the backup was
            created. Format:
            ``projects/{project_id}/locations/{location}``
        backup_region (str):
            Output only. Region in which backup is stored. Format:
            ``projects/{project_id}/locations/{location}``
        enforced_retention_end_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time until which the backup
            is not deletable.
        ontap_source (google.cloud.netapp_v1.types.OntapSource):
            Optional. Represents source details for ONTAP backups.
            Either source_volume or ontap_source should be provided.
    """

    class State(proto.Enum):
        r"""The Backup States

        Values:
            STATE_UNSPECIFIED (0):
                State not set.
            CREATING (1):
                Backup is being created. While in this state,
                the snapshot for the backup point-in-time may
                not have been created yet, and so the
                point-in-time may not have been fixed.
            UPLOADING (2):
                Backup is being uploaded. While in this
                state, none of the writes to the volume will be
                included in the backup.
            READY (3):
                Backup is available for use.
            DELETING (4):
                Backup is being deleted.
            ERROR (5):
                Backup is not valid and cannot be used for
                creating new volumes or restoring existing
                volumes.
            UPDATING (6):
                Backup is being updated.
        """

        STATE_UNSPECIFIED = 0
        CREATING = 1
        UPLOADING = 2
        READY = 3
        DELETING = 4
        ERROR = 5
        UPDATING = 6

    class Type(proto.Enum):
        r"""Backup types.

        Values:
            TYPE_UNSPECIFIED (0):
                Unspecified backup type.
            MANUAL (1):
                Manual backup type.
            SCHEDULED (2):
                Scheduled backup type.
        """

        TYPE_UNSPECIFIED = 0
        MANUAL = 1
        SCHEDULED = 2

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=2,
        enum=State,
    )
    description: str = proto.Field(
        proto.STRING,
        number=3,
    )
    volume_usage_bytes: int = proto.Field(
        proto.INT64,
        number=4,
    )
    backup_type: Type = proto.Field(
        proto.ENUM,
        number=5,
        enum=Type,
    )
    source_volume: str = proto.Field(
        proto.STRING,
        number=6,
    )
    source_snapshot: str = proto.Field(
        proto.STRING,
        number=7,
        optional=True,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=8,
        message=timestamp_pb2.Timestamp,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=9,
    )
    chain_storage_bytes: int = proto.Field(
        proto.INT64,
        number=10,
    )
    satisfies_pzs: bool = proto.Field(
        proto.BOOL,
        number=11,
    )
    satisfies_pzi: bool = proto.Field(
        proto.BOOL,
        number=12,
    )
    volume_region: str = proto.Field(
        proto.STRING,
        number=13,
    )
    backup_region: str = proto.Field(
        proto.STRING,
        number=14,
    )
    enforced_retention_end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=15,
        message=timestamp_pb2.Timestamp,
    )
    ontap_source: "OntapSource" = proto.Field(
        proto.MESSAGE,
        number=16,
        message="OntapSource",
    )


class ListBackupsRequest(proto.Message):
    r"""ListBackupsRequest lists backups.

    Attributes:
        parent (str):
            Required. The backupVault for which to retrieve backup
            information, in the format
            ``projects/{project_id}/locations/{location}/backupVaults/{backup_vault_id}``.
            To retrieve backup information for all locations, use "-"
            for the ``{location}`` value. To retrieve backup information
            for all backupVaults, use "-" for the ``{backup_vault_id}``
            value. To retrieve backup information for a volume, use "-"
            for the ``{backup_vault_id}`` value and specify volume full
            name with the filter.
        page_size (int):
            The maximum number of items to return. The
            service may return fewer than this value. The
            maximum value is 1000; values above 1000 will be
            coerced to 1000.
        page_token (str):
            The next_page_token value to use if there are additional
            results to retrieve for this list request.
        order_by (str):
            Sort results. Supported values are "name",
            "name desc" or "" (unsorted).
        filter (str):
            The standard list filter.
            If specified, backups will be returned based on
            the attribute name that matches the filter
            expression. If empty, then no backups are
            filtered out. See https://google.aip.dev/160
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


class ListBackupsResponse(proto.Message):
    r"""ListBackupsResponse is the result of ListBackupsRequest.

    Attributes:
        backups (MutableSequence[google.cloud.netapp_v1.types.Backup]):
            A list of backups in the project.
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

    backups: MutableSequence["Backup"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Backup",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetBackupRequest(proto.Message):
    r"""GetBackupRequest gets the state of a backup.

    Attributes:
        name (str):
            Required. The backup resource name, in the format
            ``projects/{project_id}/locations/{location}/backupVaults/{backup_vault_id}/backups/{backup_id}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateBackupRequest(proto.Message):
    r"""CreateBackupRequest creates a backup.

    Attributes:
        parent (str):
            Required. The NetApp backupVault to create the backups of,
            in the format
            ``projects/*/locations/*/backupVaults/{backup_vault_id}``
        backup_id (str):
            Required. The ID to use for the backup.
            The ID must be unique within the specified
            backupVault. Must contain only letters, numbers
            and hyphen, with the first character a letter,
            the last a letter or a
            number, and a 63 character maximum.
        backup (google.cloud.netapp_v1.types.Backup):
            Required. A backup resource
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    backup_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    backup: "Backup" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="Backup",
    )


class DeleteBackupRequest(proto.Message):
    r"""DeleteBackupRequest deletes a backup.

    Attributes:
        name (str):
            Required. The backup resource name, in the format
            ``projects/{project_id}/locations/{location}/backupVaults/{backup_vault_id}/backups/{backup_id}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateBackupRequest(proto.Message):
    r"""UpdateBackupRequest updates description and/or labels for a
    backup.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. Field mask is used to specify the fields to be
            overwritten in the Backup resource to be updated. The fields
            specified in the update_mask are relative to the resource,
            not the full request. A field will be overwritten if it is
            in the mask. If the user does not provide a mask then all
            fields will be overwritten.
        backup (google.cloud.netapp_v1.types.Backup):
            Required. The backup being updated
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    backup: "Backup" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Backup",
    )


class OntapSource(proto.Message):
    r"""Represents ONTAP source details.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        storage_pool (str):
            Required. Name of the storage pool. This must be specified
            for creating backups for ONTAP mode volumes. Format:
            ``projects/{projects_id}/locations/{location}/storagePools/{storage_pool_id}``

            This field is a member of `oneof`_ ``_storage_pool``.
        volume_uuid (str):
            Required. The UUID of the ONTAP source
            volume.
        snapshot_uuid (str):
            Optional. The UUID of the ONTAP source
            snapshot.
    """

    storage_pool: str = proto.Field(
        proto.STRING,
        number=1,
        optional=True,
    )
    volume_uuid: str = proto.Field(
        proto.STRING,
        number=2,
    )
    snapshot_uuid: str = proto.Field(
        proto.STRING,
        number=3,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
