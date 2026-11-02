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
        "Backup",
    },
)


class Backup(proto.Message):
    r"""Represents a request to perform a single point-in-time
    capture of some portion of the state of a GKE cluster, the
    record of the backup operation itself, and an anchor for the
    underlying artifacts that comprise the Backup (the config backup
    and VolumeBackups).

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Output only. The fully qualified name of the Backup.
            ``projects/*/locations/*/backupPlans/*/backups/*``
        uid (str):
            Output only. Server generated global unique identifier of
            `UUID4 <https://en.wikipedia.org/wiki/Universally_unique_identifier>`__
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp when this Backup
            resource was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp when this Backup
            resource was last updated.
        manual (bool):
            Output only. This flag indicates whether this
            Backup resource was created manually by a user
            or via a schedule in the BackupPlan. A value of
            True means that the Backup was created manually.
        labels (MutableMapping[str, str]):
            Optional. A set of custom labels supplied by
            user.
        delete_lock_days (int):
            Optional. Minimum age for this Backup (in days). If this
            field is set to a non-zero value, the Backup will be
            "locked" against deletion (either manual or automatic
            deletion) for the number of days provided (measured from the
            creation time of the Backup). MUST be an integer value
            between 0-90 (inclusive).

            Defaults to parent BackupPlan's
            [backup_delete_lock_days][google.cloud.gkebackup.v1.BackupPlan.RetentionPolicy.backup_delete_lock_days]
            setting and may only be increased (either at creation time
            or in a subsequent update).
        delete_lock_expire_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time at which an existing delete lock will
            expire for this backup (calculated from create_time +
            [delete_lock_days][google.cloud.gkebackup.v1.Backup.delete_lock_days]).
        retain_days (int):
            Optional. The age (in days) after which this Backup will be
            automatically deleted. Must be an integer value >= 0:

            - If 0, no automatic deletion will occur for this Backup.
            - If not 0, this must be >=
              [delete_lock_days][google.cloud.gkebackup.v1.Backup.delete_lock_days]
              and <= 365.

            Once a Backup is created, this value may only be increased.

            Defaults to the parent BackupPlan's
            [backup_retain_days][google.cloud.gkebackup.v1.BackupPlan.RetentionPolicy.backup_retain_days]
            value.
        retain_expire_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time at which this Backup will be
            automatically deleted (calculated from create_time +
            [retain_days][google.cloud.gkebackup.v1.Backup.retain_days]).
        encryption_key (google.cloud.gke_backup_v1.types.EncryptionKey):
            Output only. The customer managed encryption key that was
            used to encrypt the Backup's artifacts. Inherited from the
            parent BackupPlan's
            [encryption_key][google.cloud.gkebackup.v1.BackupPlan.BackupConfig.encryption_key]
            value.
        all_namespaces (bool):
            Output only. If True, all namespaces were
            included in the Backup.

            This field is a member of `oneof`_ ``backup_scope``.
        selected_namespaces (google.cloud.gke_backup_v1.types.Namespaces):
            Output only. If set, the list of namespaces
            that were included in the Backup.

            This field is a member of `oneof`_ ``backup_scope``.
        selected_applications (google.cloud.gke_backup_v1.types.NamespacedNames):
            Output only. If set, the list of
            ProtectedApplications whose resources were
            included in the Backup.

            This field is a member of `oneof`_ ``backup_scope``.
        contains_volume_data (bool):
            Output only. Whether or not the Backup contains volume data.
            Controlled by the parent BackupPlan's
            [include_volume_data][google.cloud.gkebackup.v1.BackupPlan.BackupConfig.include_volume_data]
            value.
        contains_secrets (bool):
            Output only. Whether or not the Backup contains Kubernetes
            Secrets. Controlled by the parent BackupPlan's
            [include_secrets][google.cloud.gkebackup.v1.BackupPlan.BackupConfig.include_secrets]
            value.
        cluster_metadata (google.cloud.gke_backup_v1.types.Backup.ClusterMetadata):
            Output only. Information about the GKE
            cluster from which this Backup was created.
        state (google.cloud.gke_backup_v1.types.Backup.State):
            Output only. Current state of the Backup
        state_reason (str):
            Output only. Human-readable description of why the backup is
            in the current ``state``. This field is only meant for human
            readability and should not be used programmatically as this
            field is not guaranteed to be consistent.
        complete_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Completion time of the Backup
        resource_count (int):
            Output only. The total number of Kubernetes
            resources included in the Backup.
        volume_count (int):
            Output only. The total number of volume
            backups contained in the Backup.
        size_bytes (int):
            Output only. The total size of the Backup in
            bytes = config backup size + sum(volume backup
            sizes)
        etag (str):
            Output only. ``etag`` is used for optimistic concurrency
            control as a way to help prevent simultaneous updates of a
            backup from overwriting each other. It is strongly suggested
            that systems make use of the ``etag`` in the
            read-modify-write cycle to perform backup updates in order
            to avoid race conditions: An ``etag`` is returned in the
            response to ``GetBackup``, and systems are expected to put
            that etag in the request to ``UpdateBackup`` or
            ``DeleteBackup`` to ensure that their change will be applied
            to the same version of the resource.
        description (str):
            Optional. User specified descriptive string
            for this Backup.
        pod_count (int):
            Output only. The total number of Kubernetes
            Pods contained in the Backup.
        config_backup_size_bytes (int):
            Output only. The size of the config backup in
            bytes.
        permissive_mode (bool):
            Output only. If false, Backup will fail when Backup for GKE
            detects Kubernetes configuration that is non-standard or
            requires additional setup to restore.

            Inherited from the parent BackupPlan's
            [permissive_mode][google.cloud.gkebackup.v1.BackupPlan.BackupConfig.permissive_mode]
            value.
        satisfies_pzs (bool):
            Output only. [Output Only] Reserved for future use.
        satisfies_pzi (bool):
            Output only. [Output Only] Reserved for future use.
    """

    class State(proto.Enum):
        r"""State

        Values:
            STATE_UNSPECIFIED (0):
                The Backup resource is in the process of
                being created.
            CREATING (1):
                The Backup resource has been created and the
                associated BackupJob Kubernetes resource has
                been injected into the source cluster.
            IN_PROGRESS (2):
                The gkebackup agent in the cluster has begun
                executing the backup operation.
            SUCCEEDED (3):
                The backup operation has completed
                successfully.
            FAILED (4):
                The backup operation has failed.
            DELETING (5):
                This Backup resource (and its associated
                artifacts) is in the process of being deleted.
        """

        STATE_UNSPECIFIED = 0
        CREATING = 1
        IN_PROGRESS = 2
        SUCCEEDED = 3
        FAILED = 4
        DELETING = 5

    class ClusterMetadata(proto.Message):
        r"""Information about the GKE cluster from which this Backup was
        created.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            cluster (str):
                Output only. The source cluster from which this Backup was
                created. Valid formats:

                - ``projects/*/locations/*/clusters/*``
                - ``projects/*/zones/*/clusters/*``

                This is inherited from the parent BackupPlan's
                [cluster][google.cloud.gkebackup.v1.BackupPlan.cluster]
                field.
            k8s_version (str):
                Output only. The Kubernetes server version of
                the source cluster.
            backup_crd_versions (MutableMapping[str, str]):
                Output only. A list of the Backup for GKE CRD
                versions found in the cluster.
            gke_version (str):
                Output only. GKE version

                This field is a member of `oneof`_ ``platform_version``.
            anthos_version (str):
                Output only. Anthos version

                This field is a member of `oneof`_ ``platform_version``.
        """

        cluster: str = proto.Field(
            proto.STRING,
            number=1,
        )
        k8s_version: str = proto.Field(
            proto.STRING,
            number=2,
        )
        backup_crd_versions: MutableMapping[str, str] = proto.MapField(
            proto.STRING,
            proto.STRING,
            number=3,
        )
        gke_version: str = proto.Field(
            proto.STRING,
            number=4,
            oneof="platform_version",
        )
        anthos_version: str = proto.Field(
            proto.STRING,
            number=5,
            oneof="platform_version",
        )

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
    manual: bool = proto.Field(
        proto.BOOL,
        number=5,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=6,
    )
    delete_lock_days: int = proto.Field(
        proto.INT32,
        number=7,
    )
    delete_lock_expire_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=8,
        message=timestamp_pb2.Timestamp,
    )
    retain_days: int = proto.Field(
        proto.INT32,
        number=9,
    )
    retain_expire_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=10,
        message=timestamp_pb2.Timestamp,
    )
    encryption_key: common.EncryptionKey = proto.Field(
        proto.MESSAGE,
        number=11,
        message=common.EncryptionKey,
    )
    all_namespaces: bool = proto.Field(
        proto.BOOL,
        number=12,
        oneof="backup_scope",
    )
    selected_namespaces: common.Namespaces = proto.Field(
        proto.MESSAGE,
        number=13,
        oneof="backup_scope",
        message=common.Namespaces,
    )
    selected_applications: common.NamespacedNames = proto.Field(
        proto.MESSAGE,
        number=14,
        oneof="backup_scope",
        message=common.NamespacedNames,
    )
    contains_volume_data: bool = proto.Field(
        proto.BOOL,
        number=15,
    )
    contains_secrets: bool = proto.Field(
        proto.BOOL,
        number=16,
    )
    cluster_metadata: ClusterMetadata = proto.Field(
        proto.MESSAGE,
        number=17,
        message=ClusterMetadata,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=18,
        enum=State,
    )
    state_reason: str = proto.Field(
        proto.STRING,
        number=19,
    )
    complete_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=20,
        message=timestamp_pb2.Timestamp,
    )
    resource_count: int = proto.Field(
        proto.INT32,
        number=21,
    )
    volume_count: int = proto.Field(
        proto.INT32,
        number=22,
    )
    size_bytes: int = proto.Field(
        proto.INT64,
        number=23,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=24,
    )
    description: str = proto.Field(
        proto.STRING,
        number=25,
    )
    pod_count: int = proto.Field(
        proto.INT32,
        number=26,
    )
    config_backup_size_bytes: int = proto.Field(
        proto.INT64,
        number=27,
    )
    permissive_mode: bool = proto.Field(
        proto.BOOL,
        number=28,
    )
    satisfies_pzs: bool = proto.Field(
        proto.BOOL,
        number=29,
    )
    satisfies_pzi: bool = proto.Field(
        proto.BOOL,
        number=30,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
