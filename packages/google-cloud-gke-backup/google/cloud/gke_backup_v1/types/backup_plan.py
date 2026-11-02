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

import google.protobuf.duration_pb2 as duration_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import google.type.date_pb2 as date_pb2  # type: ignore
import google.type.dayofweek_pb2 as dayofweek_pb2  # type: ignore
import google.type.timeofday_pb2 as timeofday_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.gke_backup_v1.types import common

__protobuf__ = proto.module(
    package="google.cloud.gkebackup.v1",
    manifest={
        "BackupPlan",
        "RpoConfig",
        "ExclusionWindow",
    },
)


class BackupPlan(proto.Message):
    r"""Defines the configuration and scheduling for a "line" of
    Backups.

    Attributes:
        name (str):
            Output only. The full name of the BackupPlan resource.
            Format: ``projects/*/locations/*/backupPlans/*``
        uid (str):
            Output only. Server generated global unique identifier of
            `UUID <https://en.wikipedia.org/wiki/Universally_unique_identifier>`__
            format.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp when this
            BackupPlan resource was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp when this
            BackupPlan resource was last updated.
        description (str):
            Optional. User specified descriptive string
            for this BackupPlan.
        cluster (str):
            Required. Immutable. The source cluster from which Backups
            will be created via this BackupPlan. Valid formats:

            - ``projects/*/locations/*/clusters/*``
            - ``projects/*/zones/*/clusters/*``
        retention_policy (google.cloud.gke_backup_v1.types.BackupPlan.RetentionPolicy):
            Optional. RetentionPolicy governs lifecycle
            of Backups created under this plan.
        labels (MutableMapping[str, str]):
            Optional. A set of custom labels supplied by
            user.
        backup_schedule (google.cloud.gke_backup_v1.types.BackupPlan.Schedule):
            Optional. Defines a schedule for automatic
            Backup creation via this BackupPlan.
        etag (str):
            Output only. ``etag`` is used for optimistic concurrency
            control as a way to help prevent simultaneous updates of a
            backup plan from overwriting each other. It is strongly
            suggested that systems make use of the 'etag' in the
            read-modify-write cycle to perform BackupPlan updates in
            order to avoid race conditions: An ``etag`` is returned in
            the response to ``GetBackupPlan``, and systems are expected
            to put that etag in the request to ``UpdateBackupPlan`` or
            ``DeleteBackupPlan`` to ensure that their change will be
            applied to the same version of the resource.
        deactivated (bool):
            Optional. This flag indicates whether this
            BackupPlan has been deactivated. Setting this
            field to True locks the BackupPlan such that no
            further updates will be allowed (except
            deletes), including the deactivated field
            itself. It also prevents any new Backups from
            being created via this BackupPlan (including
            scheduled Backups).

            Default: False
        backup_config (google.cloud.gke_backup_v1.types.BackupPlan.BackupConfig):
            Optional. Defines the configuration of
            Backups created via this BackupPlan.
        protected_pod_count (int):
            Output only. The number of Kubernetes Pods
            backed up in the last successful Backup created
            via this BackupPlan.
        state (google.cloud.gke_backup_v1.types.BackupPlan.State):
            Output only. State of the BackupPlan. This
            State field reflects the various stages a
            BackupPlan can be in during the Create
            operation. It will be set to "DEACTIVATED" if
            the BackupPlan is deactivated on an Update
        state_reason (str):
            Output only. Human-readable description of why BackupPlan is
            in the current ``state``. This field is only meant for human
            readability and should not be used programmatically as this
            field is not guaranteed to be consistent.
        rpo_risk_level (int):
            Output only. A number that represents the
            current risk level of this BackupPlan from RPO
            perspective with 1 being no risk and 5 being
            highest risk.
        rpo_risk_reason (str):
            Output only. Human-readable description of why the
            BackupPlan is in the current rpo_risk_level and action items
            if any.
        backup_channel (str):
            Output only. The fully qualified name of the BackupChannel
            to be used to create a backup. This field is set only if the
            cluster being backed up is in a different project.
            ``projects/*/locations/*/backupChannels/*``
        last_successful_backup_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Completion time of the last successful Backup.
            This is sourced from a successful Backup's complete_time
            field. This field is added to maintain consistency with
            BackupPlanBinding to display last successful backup time.
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

    class RetentionPolicy(proto.Message):
        r"""RetentionPolicy defines a Backup retention policy for a
        BackupPlan.

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
                subject to automatic deletion. Updating this field does NOT
                affect existing Backups under it. Backups created AFTER a
                successful update will automatically pick up the new value.
                NOTE: backup_retain_days must be >=
                [backup_delete_lock_days][google.cloud.gkebackup.v1.BackupPlan.RetentionPolicy.backup_delete_lock_days].
                If
                [cron_schedule][google.cloud.gkebackup.v1.BackupPlan.Schedule.cron_schedule]
                is defined, then this must be <= 360 \* the creation
                interval. If
                [rpo_config][google.cloud.gkebackup.v1.BackupPlan.Schedule.rpo_config]
                is defined, then this must be <= 360 \*
                [target_rpo_minutes][Schedule.rpo_config.target_rpo_minutes]
                / (1440minutes/day).

                Default: 0 (no automatic deletion)
            locked (bool):
                Optional. This flag denotes whether the retention policy of
                this BackupPlan is locked. If set to True, no further update
                is allowed on this policy, including the ``locked`` field
                itself.

                Default: False
        """

        backup_delete_lock_days: int = proto.Field(
            proto.INT32,
            number=1,
        )
        backup_retain_days: int = proto.Field(
            proto.INT32,
            number=2,
        )
        locked: bool = proto.Field(
            proto.BOOL,
            number=3,
        )

    class Schedule(proto.Message):
        r"""Defines scheduling parameters for automatically creating
        Backups via this BackupPlan.

        Attributes:
            cron_schedule (str):
                Optional. A standard
                `cron <https://wikipedia.com/wiki/cron>`__ string that
                defines a repeating schedule for creating Backups via this
                BackupPlan. This is mutually exclusive with the
                [rpo_config][google.cloud.gkebackup.v1.BackupPlan.Schedule.rpo_config]
                field since at most one schedule can be defined for a
                BackupPlan. If this is defined, then
                [backup_retain_days][google.cloud.gkebackup.v1.BackupPlan.RetentionPolicy.backup_retain_days]
                must also be defined.

                Default (empty): no automatic backup creation will occur.
            paused (bool):
                Optional. This flag denotes whether automatic
                Backup creation is paused for this BackupPlan.

                Default: False
            rpo_config (google.cloud.gke_backup_v1.types.RpoConfig):
                Optional. Defines the RPO schedule configuration for this
                BackupPlan. This is mutually exclusive with the
                [cron_schedule][google.cloud.gkebackup.v1.BackupPlan.Schedule.cron_schedule]
                field since at most one schedule can be defined for a
                BackupPLan. If this is defined, then
                [backup_retain_days][google.cloud.gkebackup.v1.BackupPlan.RetentionPolicy.backup_retain_days]
                must also be defined.

                Default (empty): no automatic backup creation will occur.
            next_scheduled_backup_time (google.protobuf.timestamp_pb2.Timestamp):
                Output only. Start time of next scheduled backup under this
                BackupPlan by either cron_schedule or rpo config.
        """

        cron_schedule: str = proto.Field(
            proto.STRING,
            number=1,
        )
        paused: bool = proto.Field(
            proto.BOOL,
            number=2,
        )
        rpo_config: "RpoConfig" = proto.Field(
            proto.MESSAGE,
            number=3,
            message="RpoConfig",
        )
        next_scheduled_backup_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=4,
            message=timestamp_pb2.Timestamp,
        )

    class BackupConfig(proto.Message):
        r"""BackupConfig defines the configuration of Backups created via
        this BackupPlan.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            all_namespaces (bool):
                If True, include all namespaced resources

                This field is a member of `oneof`_ ``backup_scope``.
            selected_namespaces (google.cloud.gke_backup_v1.types.Namespaces):
                If set, include just the resources in the
                listed namespaces.

                This field is a member of `oneof`_ ``backup_scope``.
            selected_applications (google.cloud.gke_backup_v1.types.NamespacedNames):
                If set, include just the resources referenced
                by the listed ProtectedApplications.

                This field is a member of `oneof`_ ``backup_scope``.
            include_volume_data (bool):
                Optional. This flag specifies whether volume
                data should be backed up when PVCs are included
                in the scope of a Backup.

                Default: False
            include_secrets (bool):
                Optional. This flag specifies whether
                Kubernetes Secret resources should be included
                when they fall into the scope of Backups.

                Default: False
            encryption_key (google.cloud.gke_backup_v1.types.EncryptionKey):
                Optional. This defines a customer managed
                encryption key that will be used to encrypt the
                "config" portion (the Kubernetes resources) of
                Backups created via this plan.

                Default (empty): Config backup artifacts will
                not be encrypted.
            permissive_mode (bool):
                Optional. If false, Backups will fail when
                Backup for GKE detects Kubernetes configuration
                that is non-standard or requires additional
                setup to restore.

                Default: False
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
            number=4,
        )
        include_secrets: bool = proto.Field(
            proto.BOOL,
            number=5,
        )
        encryption_key: common.EncryptionKey = proto.Field(
            proto.MESSAGE,
            number=6,
            message=common.EncryptionKey,
        )
        permissive_mode: bool = proto.Field(
            proto.BOOL,
            number=7,
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
    description: str = proto.Field(
        proto.STRING,
        number=5,
    )
    cluster: str = proto.Field(
        proto.STRING,
        number=6,
    )
    retention_policy: RetentionPolicy = proto.Field(
        proto.MESSAGE,
        number=7,
        message=RetentionPolicy,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=8,
    )
    backup_schedule: Schedule = proto.Field(
        proto.MESSAGE,
        number=9,
        message=Schedule,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=10,
    )
    deactivated: bool = proto.Field(
        proto.BOOL,
        number=11,
    )
    backup_config: BackupConfig = proto.Field(
        proto.MESSAGE,
        number=12,
        message=BackupConfig,
    )
    protected_pod_count: int = proto.Field(
        proto.INT32,
        number=13,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=14,
        enum=State,
    )
    state_reason: str = proto.Field(
        proto.STRING,
        number=15,
    )
    rpo_risk_level: int = proto.Field(
        proto.INT32,
        number=16,
    )
    rpo_risk_reason: str = proto.Field(
        proto.STRING,
        number=17,
    )
    backup_channel: str = proto.Field(
        proto.STRING,
        number=18,
    )
    last_successful_backup_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=19,
        message=timestamp_pb2.Timestamp,
    )


class RpoConfig(proto.Message):
    r"""Defines RPO scheduling configuration for automatically
    creating Backups via this BackupPlan.

    Attributes:
        target_rpo_minutes (int):
            Required. Defines the target RPO for the
            BackupPlan in minutes, which means the target
            maximum data loss in time that is acceptable for
            this BackupPlan. This must be at least 60, i.e.,
            1 hour, and at most 86400, i.e., 60 days.
        exclusion_windows (MutableSequence[google.cloud.gke_backup_v1.types.ExclusionWindow]):
            Optional. User specified time windows during which backup
            can NOT happen for this BackupPlan - backups should start
            and finish outside of any given exclusion window. Note:
            backup jobs will be scheduled to start and finish outside
            the duration of the window as much as possible, but running
            jobs will not get canceled when it runs into the window. All
            the time and date values in exclusion_windows entry in the
            API are in UTC. We only allow <=1 recurrence (daily or
            weekly) exclusion window for a BackupPlan while no
            restriction on number of single occurrence windows.
    """

    target_rpo_minutes: int = proto.Field(
        proto.INT32,
        number=1,
    )
    exclusion_windows: MutableSequence["ExclusionWindow"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="ExclusionWindow",
    )


class ExclusionWindow(proto.Message):
    r"""Defines a time window during which no backup should
    happen. All time and date are in UTC.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        start_time (google.type.timeofday_pb2.TimeOfDay):
            Required. Specifies the start time of the
            window using time of the day in UTC.
        duration (google.protobuf.duration_pb2.Duration):
            Required. Specifies duration of the window. Duration must be
            >= 5 minutes and < (target RPO - 20 minutes). Additional
            restrictions based on the recurrence type to allow some time
            for backup to happen:

            - single_occurrence_date: no restriction, but UI may warn
              about this when duration >= target RPO
            - daily window: duration < 24 hours
            - weekly window:

              - days of week includes all seven days of a week: duration
                < 24 hours
              - all other weekly window: duration < 168 hours (i.e., 24
                \* 7 hours)
        single_occurrence_date (google.type.date_pb2.Date):
            No recurrence. The exclusion window occurs
            only once and on this date in UTC.

            This field is a member of `oneof`_ ``recurrence``.
        daily (bool):
            The exclusion window occurs every day if set
            to "True". Specifying this field to "False" is
            an error.

            This field is a member of `oneof`_ ``recurrence``.
        days_of_week (google.cloud.gke_backup_v1.types.ExclusionWindow.DayOfWeekList):
            The exclusion window occurs on these days of
            each week in UTC.

            This field is a member of `oneof`_ ``recurrence``.
    """

    class DayOfWeekList(proto.Message):
        r"""Holds repeated DaysOfWeek values as a container.

        Attributes:
            days_of_week (MutableSequence[google.type.dayofweek_pb2.DayOfWeek]):
                Optional. A list of days of week.
        """

        days_of_week: MutableSequence[dayofweek_pb2.DayOfWeek] = proto.RepeatedField(
            proto.ENUM,
            number=1,
            enum=dayofweek_pb2.DayOfWeek,
        )

    start_time: timeofday_pb2.TimeOfDay = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timeofday_pb2.TimeOfDay,
    )
    duration: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=2,
        message=duration_pb2.Duration,
    )
    single_occurrence_date: date_pb2.Date = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="recurrence",
        message=date_pb2.Date,
    )
    daily: bool = proto.Field(
        proto.BOOL,
        number=4,
        oneof="recurrence",
    )
    days_of_week: DayOfWeekList = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="recurrence",
        message=DayOfWeekList,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
