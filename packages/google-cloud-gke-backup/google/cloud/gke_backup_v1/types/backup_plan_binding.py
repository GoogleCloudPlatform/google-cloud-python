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
        "BackupPlanBinding",
    },
)


class BackupPlanBinding(proto.Message):
    r"""A BackupPlanBinding binds a BackupPlan with a BackupChannel.
    This resource is created automatically when a BackupPlan is
    created using a BackupChannel. This also serves as a holder for
    cross-project fields that need to be displayed in the current
    project.

    Attributes:
        name (str):
            Identifier. The fully qualified name of the
            BackupPlanBinding.
            ``projects/*/locations/*/backupChannels/*/backupPlanBindings/*``
        uid (str):
            Output only. Server generated global unique identifier of
            `UUID4 <https://en.wikipedia.org/wiki/Universally_unique_identifier>`__
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp when this binding
            was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp when this binding
            was created.
        backup_plan (str):
            Output only. Immutable. The fully qualified name of the
            BackupPlan bound with the parent BackupChannel.
            ``projects/*/locations/*/backupPlans/{backup_plan}``
        cluster (str):
            Output only. Immutable. The fully qualified name of the
            cluster that is being backed up Valid formats:

            - ``projects/*/locations/*/clusters/*``
            - ``projects/*/zones/*/clusters/*``
        backup_plan_details (google.cloud.gke_backup_v1.types.BackupPlanBinding.BackupPlanDetails):
            Output only. Contains details about the
            backup plan/backup.
        etag (str):
            Output only. ``etag`` is used for optimistic concurrency
            control as a way to help prevent simultaneous updates of a
            BackupPlanBinding from overwriting each other. It is
            strongly suggested that systems make use of the 'etag' in
            the read-modify-write cycle to perform BackupPlanBinding
            updates in order to avoid race conditions: An ``etag`` is
            returned in the response to ``GetBackupPlanBinding``, and
            systems are expected to put that etag in the request to
            ``UpdateBackupPlanBinding`` or ``DeleteBackupPlanBinding``
            to ensure that their change will be applied to the same
            version of the resource.
    """

    class BackupPlanDetails(proto.Message):
        r"""Contains metadata about the backup plan/backup.

        Attributes:
            protected_pod_count (int):
                Output only. The number of Kubernetes Pods
                backed up in the last successful Backup created
                via this BackupPlan.
            state (google.cloud.gke_backup_v1.types.BackupPlanBinding.BackupPlanDetails.State):
                Output only. State of the BackupPlan.
            last_successful_backup_time (google.protobuf.timestamp_pb2.Timestamp):
                Output only. Completion time of the last successful Backup.
                This is sourced from a successful Backup's complete_time
                field.
            next_scheduled_backup_time (google.protobuf.timestamp_pb2.Timestamp):
                Output only. Start time of next scheduled backup under this
                BackupPlan by either cron_schedule or rpo config. This is
                sourced from BackupPlan.
            rpo_risk_level (int):
                Output only. A number that represents the
                current risk level of this BackupPlan from RPO
                perspective with 1 being no risk and 5 being
                highest risk.
            last_successful_backup (str):
                Output only. The fully qualified name of the last successful
                Backup created under this BackupPlan.
                ``projects/*/locations/*/backupPlans/*/backups/*``
            backup_config_details (google.cloud.gke_backup_v1.types.BackupPlanBinding.BackupPlanDetails.BackupConfigDetails):
                Output only. Contains details about the
                BackupConfig of Backups created via this
                BackupPlan.
            retention_policy_details (google.cloud.gke_backup_v1.types.BackupPlanBinding.BackupPlanDetails.RetentionPolicyDetails):
                Output only. Contains details about the
                RetentionPolicy of Backups created via this
                BackupPlan.
        """

        class State(proto.Enum):
            r"""State

            Values:
                STATE_UNSPECIFIED (0):
                    Default first value for Enums.
                CLUSTER_PENDING (1):
                    Waiting for cluster state to be RUNNING.
                PROVISIONING (2):
                    The BackupPlan is in the process of being
                    created.
                READY (3):
                    The BackupPlan has successfully been created
                    and is ready for Backups.
                FAILED (4):
                    BackupPlan creation has failed.
                DEACTIVATED (5):
                    The BackupPlan has been deactivated.
                DELETING (6):
                    The BackupPlan is in the process of being
                    deleted.
            """

            STATE_UNSPECIFIED = 0
            CLUSTER_PENDING = 1
            PROVISIONING = 2
            READY = 3
            FAILED = 4
            DEACTIVATED = 5
            DELETING = 6

        class BackupConfigDetails(proto.Message):
            r"""BackupConfigDetails defines the configuration of Backups
            created via this BackupPlan.

            This message has `oneof`_ fields (mutually exclusive fields).
            For each oneof, at most one member field can be set at the same time.
            Setting any member of the oneof automatically clears all other
            members.

            .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

            Attributes:
                all_namespaces (bool):
                    Output only. If True, include all namespaced
                    resources

                    This field is a member of `oneof`_ ``backup_scope``.
                selected_namespaces (google.cloud.gke_backup_v1.types.Namespaces):
                    Output only. If set, include just the
                    resources in the listed namespaces.

                    This field is a member of `oneof`_ ``backup_scope``.
                selected_applications (google.cloud.gke_backup_v1.types.NamespacedNames):
                    Output only. If set, include just the
                    resources referenced by the listed
                    ProtectedApplications.

                    This field is a member of `oneof`_ ``backup_scope``.
                include_volume_data (bool):
                    Output only. This flag specifies whether
                    volume data should be backed up when PVCs are
                    included in the scope of a Backup.

                    Default: False
                include_secrets (bool):
                    Output only. This flag specifies whether
                    Kubernetes Secret resources should be included
                    when they fall into the scope of Backups.

                    Default: False
                encryption_key (google.cloud.gke_backup_v1.types.EncryptionKey):
                    Output only. This defines a customer managed
                    encryption key that will be used to encrypt the
                    "config" portion (the Kubernetes resources) of
                    Backups created via this plan.

                    Default (empty): Config backup artifacts will
                    not be encrypted.
            """

            all_namespaces: bool = proto.Field(
                proto.BOOL,
                number=1,
                oneof="backup_scope",
            )
            selected_namespaces: common.Namespaces = proto.Field(
                proto.MESSAGE,
                number=2,
                oneof="backup_scope",
                message=common.Namespaces,
            )
            selected_applications: common.NamespacedNames = proto.Field(
                proto.MESSAGE,
                number=3,
                oneof="backup_scope",
                message=common.NamespacedNames,
            )
            include_volume_data: bool = proto.Field(
                proto.BOOL,
                number=5,
            )
            include_secrets: bool = proto.Field(
                proto.BOOL,
                number=6,
            )
            encryption_key: common.EncryptionKey = proto.Field(
                proto.MESSAGE,
                number=7,
                message=common.EncryptionKey,
            )

        class RetentionPolicyDetails(proto.Message):
            r"""RetentionPolicyDetails defines a Backup retention policy for
            a BackupPlan.

            Attributes:
                backup_delete_lock_days (int):
                    Optional. Minimum age for Backups created via this
                    BackupPlan (in days). This field MUST be an integer value
                    between 0-90 (inclusive). A Backup created under this
                    BackupPlan will NOT be deletable until it reaches Backup's
                    (create_time + backup_delete_lock_days). Updating this field
                    of a BackupPlan does NOT affect existing Backups under it.
                    Backups created AFTER a successful update will inherit the
                    new value.

                    Default: 0 (no delete blocking)
                backup_retain_days (int):
                    Optional. The default maximum age of a Backup created via
                    this BackupPlan. This field MUST be an integer value >= 0
                    and <= 365. If specified, a Backup created under this
                    BackupPlan will be automatically deleted after its age
                    reaches (create_time + backup_retain_days). If not
                    specified, Backups created under this BackupPlan will NOT be
                    subject to automatic deletion. Default: 0 (no automatic
                    deletion)
            """

            backup_delete_lock_days: int = proto.Field(
                proto.INT32,
                number=1,
            )
            backup_retain_days: int = proto.Field(
                proto.INT32,
                number=2,
            )

        protected_pod_count: int = proto.Field(
            proto.INT32,
            number=1,
        )
        state: "BackupPlanBinding.BackupPlanDetails.State" = proto.Field(
            proto.ENUM,
            number=2,
            enum="BackupPlanBinding.BackupPlanDetails.State",
        )
        last_successful_backup_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=3,
            message=timestamp_pb2.Timestamp,
        )
        next_scheduled_backup_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=4,
            message=timestamp_pb2.Timestamp,
        )
        rpo_risk_level: int = proto.Field(
            proto.INT32,
            number=5,
        )
        last_successful_backup: str = proto.Field(
            proto.STRING,
            number=6,
        )
        backup_config_details: "BackupPlanBinding.BackupPlanDetails.BackupConfigDetails" = proto.Field(
            proto.MESSAGE,
            number=7,
            message="BackupPlanBinding.BackupPlanDetails.BackupConfigDetails",
        )
        retention_policy_details: "BackupPlanBinding.BackupPlanDetails.RetentionPolicyDetails" = proto.Field(
            proto.MESSAGE,
            number=8,
            message="BackupPlanBinding.BackupPlanDetails.RetentionPolicyDetails",
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
    backup_plan: str = proto.Field(
        proto.STRING,
        number=5,
    )
    cluster: str = proto.Field(
        proto.STRING,
        number=6,
    )
    backup_plan_details: BackupPlanDetails = proto.Field(
        proto.MESSAGE,
        number=7,
        message=BackupPlanDetails,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=8,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
