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

from google.cloud.gke_backup_v1.types import common

__protobuf__ = proto.module(
    package="google.cloud.gkebackup.v1",
    manifest={
        "VolumeBackup",
        "VolumeRestore",
    },
)


class VolumeBackup(proto.Message):
    r"""Represents the backup of a specific persistent volume as a
    component of a Backup - both the record of the operation and a
    pointer to the underlying storage-specific artifacts.

    Attributes:
        name (str):
            Output only. The full name of the VolumeBackup resource.
            Format:
            ``projects/*/locations/*/backupPlans/*/backups/*/volumeBackups/*``.
        uid (str):
            Output only. Server generated global unique identifier of
            `UUID <https://en.wikipedia.org/wiki/Universally_unique_identifier>`__
            format.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp when this
            VolumeBackup resource was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp when this
            VolumeBackup resource was last updated.
        source_pvc (google.cloud.gke_backup_v1.types.NamespacedName):
            Output only. A reference to the source
            Kubernetes PVC from which this VolumeBackup was
            created.
        volume_backup_handle (str):
            Output only. A storage system-specific opaque
            handle to the underlying volume backup.
        format_ (google.cloud.gke_backup_v1.types.VolumeBackup.VolumeBackupFormat):
            Output only. The format used for the volume
            backup.
        storage_bytes (int):
            Output only. The aggregate size of the
            underlying artifacts associated with this
            VolumeBackup in the backup storage. This may
            change over time when multiple backups of the
            same volume share the same backup storage
            location. In particular, this is likely to
            increase in size when the immediately preceding
            backup of the same volume is deleted.
        disk_size_bytes (int):
            Output only. The minimum size of the disk to
            which this VolumeBackup can be restored.
        complete_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp when the
            associated underlying volume backup operation
            completed.
        state (google.cloud.gke_backup_v1.types.VolumeBackup.State):
            Output only. The current state of this
            VolumeBackup.
        state_message (str):
            Output only. A human readable message
            explaining why the VolumeBackup is in its
            current state. This field is only meant for
            human consumption and should not be used
            programmatically as this field is not guaranteed
            to be consistent.
        etag (str):
            Output only. ``etag`` is used for optimistic concurrency
            control as a way to help prevent simultaneous updates of a
            volume backup from overwriting each other. It is strongly
            suggested that systems make use of the ``etag`` in the
            read-modify-write cycle to perform volume backup updates in
            order to avoid race conditions.
        satisfies_pzs (bool):
            Output only. [Output Only] Reserved for future use.
        satisfies_pzi (bool):
            Output only. [Output Only] Reserved for future use.
    """

    class VolumeBackupFormat(proto.Enum):
        r"""Identifies the format used for the volume backup.

        Values:
            VOLUME_BACKUP_FORMAT_UNSPECIFIED (0):
                Default value, not specified.
            GCE_PERSISTENT_DISK (1):
                Compute Engine Persistent Disk snapshot based
                volume backup.
        """

        VOLUME_BACKUP_FORMAT_UNSPECIFIED = 0
        GCE_PERSISTENT_DISK = 1

    class State(proto.Enum):
        r"""The current state of a VolumeBackup

        Values:
            STATE_UNSPECIFIED (0):
                This is an illegal state and should not be
                encountered.
            CREATING (1):
                A volume for the backup was identified and
                backup process is about to start.
            SNAPSHOTTING (2):
                The volume backup operation has begun and is
                in the initial "snapshot" phase of the process.
                Any defined ProtectedApplication "pre" hooks
                will be executed before entering this state and
                "post" hooks will be executed upon leaving this
                state.
            UPLOADING (3):
                The snapshot phase of the volume backup
                operation has completed and the snapshot is now
                being uploaded to backup storage.
            SUCCEEDED (4):
                The volume backup operation has completed
                successfully.
            FAILED (5):
                The volume backup operation has failed.
            DELETING (6):
                This VolumeBackup resource (and its
                associated artifacts) is in the process of being
                deleted.
            CLEANED_UP (7):
                The underlying artifacts of a volume backup
                (eg: persistent disk snapshots) are deleted.
        """

        STATE_UNSPECIFIED = 0
        CREATING = 1
        SNAPSHOTTING = 2
        UPLOADING = 3
        SUCCEEDED = 4
        FAILED = 5
        DELETING = 6
        CLEANED_UP = 7

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    uid: str = proto.Field(
        proto.STRING,
        number=2,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    source_pvc: common.NamespacedName = proto.Field(
        proto.MESSAGE,
        number=5,
        message=common.NamespacedName,
    )
    volume_backup_handle: str = proto.Field(
        proto.STRING,
        number=6,
    )
    format_: VolumeBackupFormat = proto.Field(
        proto.ENUM,
        number=7,
        enum=VolumeBackupFormat,
    )
    storage_bytes: int = proto.Field(
        proto.INT64,
        number=8,
    )
    disk_size_bytes: int = proto.Field(
        proto.INT64,
        number=9,
    )
    complete_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=10,
        message=timestamp_pb2.Timestamp,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=11,
        enum=State,
    )
    state_message: str = proto.Field(
        proto.STRING,
        number=12,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=13,
    )
    satisfies_pzs: bool = proto.Field(
        proto.BOOL,
        number=14,
    )
    satisfies_pzi: bool = proto.Field(
        proto.BOOL,
        number=15,
    )


class VolumeRestore(proto.Message):
    r"""Represents the operation of restoring a volume from a
    VolumeBackup.

    Attributes:
        name (str):
            Output only. Full name of the VolumeRestore resource.
            Format:
            ``projects/*/locations/*/restorePlans/*/restores/*/volumeRestores/*``
        uid (str):
            Output only. Server generated global unique identifier of
            `UUID <https://en.wikipedia.org/wiki/Universally_unique_identifier>`__
            format.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp when this
            VolumeRestore resource was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp when this
            VolumeRestore resource was last updated.
        volume_backup (str):
            Output only. The full name of the VolumeBackup from which
            the volume will be restored. Format:
            ``projects/*/locations/*/backupPlans/*/backups/*/volumeBackups/*``.
        target_pvc (google.cloud.gke_backup_v1.types.NamespacedName):
            Output only. The reference to the target
            Kubernetes PVC to be restored.
        volume_handle (str):
            Output only. A storage system-specific opaque
            handler to the underlying volume created for the
            target PVC from the volume backup.
        volume_type (google.cloud.gke_backup_v1.types.VolumeRestore.VolumeType):
            Output only. The type of volume provisioned
        complete_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp when the
            associated underlying volume restoration
            completed.
        state (google.cloud.gke_backup_v1.types.VolumeRestore.State):
            Output only. The current state of this
            VolumeRestore.
        state_message (str):
            Output only. A human readable message
            explaining why the VolumeRestore is in its
            current state.
        etag (str):
            Output only. ``etag`` is used for optimistic concurrency
            control as a way to help prevent simultaneous updates of a
            volume restore from overwriting each other. It is strongly
            suggested that systems make use of the ``etag`` in the
            read-modify-write cycle to perform volume restore updates in
            order to avoid race conditions.
    """

    class VolumeType(proto.Enum):
        r"""Supported volume types.

        Values:
            VOLUME_TYPE_UNSPECIFIED (0):
                Default
            GCE_PERSISTENT_DISK (1):
                Compute Engine Persistent Disk volume
        """

        VOLUME_TYPE_UNSPECIFIED = 0
        GCE_PERSISTENT_DISK = 1

    class State(proto.Enum):
        r"""The current state of a VolumeRestore

        Values:
            STATE_UNSPECIFIED (0):
                This is an illegal state and should not be
                encountered.
            CREATING (1):
                A volume for the restore was identified and
                restore process is about to start.
            RESTORING (2):
                The volume is currently being restored.
            SUCCEEDED (3):
                The volume has been successfully restored.
            FAILED (4):
                The volume restoration process failed.
            DELETING (5):
                This VolumeRestore resource is in the process
                of being deleted.
        """

        STATE_UNSPECIFIED = 0
        CREATING = 1
        RESTORING = 2
        SUCCEEDED = 3
        FAILED = 4
        DELETING = 5

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    uid: str = proto.Field(
        proto.STRING,
        number=2,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    volume_backup: str = proto.Field(
        proto.STRING,
        number=5,
    )
    target_pvc: common.NamespacedName = proto.Field(
        proto.MESSAGE,
        number=6,
        message=common.NamespacedName,
    )
    volume_handle: str = proto.Field(
        proto.STRING,
        number=7,
    )
    volume_type: VolumeType = proto.Field(
        proto.ENUM,
        number=8,
        enum=VolumeType,
    )
    complete_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=9,
        message=timestamp_pb2.Timestamp,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=10,
        enum=State,
    )
    state_message: str = proto.Field(
        proto.STRING,
        number=11,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=12,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
