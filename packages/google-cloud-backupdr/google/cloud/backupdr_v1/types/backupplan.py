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
import google.type.dayofweek_pb2 as dayofweek_pb2  # type: ignore
import google.type.month_pb2 as month_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.backupdr.v1",
    manifest={
        "BackupPlan",
        "BackupRule",
        "StandardSchedule",
        "BackupWindow",
        "WeekDayOfMonth",
        "CreateBackupPlanRequest",
        "ListBackupPlansRequest",
        "ListBackupPlansResponse",
        "GetBackupPlanRequest",
        "DeleteBackupPlanRequest",
        "UpdateBackupPlanRequest",
        "BackupPlanRevision",
        "GetBackupPlanRevisionRequest",
        "ListBackupPlanRevisionsRequest",
        "ListBackupPlanRevisionsResponse",
    },
)


class BackupPlan(proto.Message):
    r"""A ``BackupPlan`` specifies some common fields, such as
    ``description`` as well as one or more ``BackupRule`` messages. Each
    ``BackupRule`` has a retention policy and defines a schedule by
    which the system is to perform backup workloads.

    Attributes:
        name (str):
            Output only. Identifier. The resource name of the
            ``BackupPlan``.

            Format:
            ``projects/{project}/locations/{location}/backupPlans/{backup_plan}``
        description (str):
            Optional. The description of the ``BackupPlan`` resource.

            The description allows for additional details about
            ``BackupPlan`` and its use cases to be provided. An example
            description is the following: "This is a backup plan that
            performs a daily backup at 6pm and retains data for 3
            months". The description must be at most 2048 characters.
        labels (MutableMapping[str, str]):
            Optional. This collection of key/value pairs
            allows for custom labels to be supplied by the
            user.  Example, {"tag": "Weekly"}.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. When the ``BackupPlan`` was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. When the ``BackupPlan`` was last updated.
        backup_rules (MutableSequence[google.cloud.backupdr_v1.types.BackupRule]):
            Required. The backup rules for this ``BackupPlan``. There
            must be at least one ``BackupRule`` message.
        state (google.cloud.backupdr_v1.types.BackupPlan.State):
            Output only. The ``State`` for the ``BackupPlan``.
        resource_type (str):
            Required. The resource type to which the ``BackupPlan`` will
            be applied. Examples include,
            "compute.googleapis.com/Instance",
            "sqladmin.googleapis.com/Instance",
            "alloydb.googleapis.com/Cluster",
            "compute.googleapis.com/Disk".
        etag (str):
            Optional. ``etag`` is returned from the service in the
            response. As a user of the service, you may provide an etag
            value in this field to prevent stale resources.
        backup_vault (str):
            Required. Resource name of backup vault which
            will be used as storage location for backups.
            Format:

            projects/{project}/locations/{location}/backupVaults/{backupvault}
        backup_vault_service_account (str):
            Output only. The Google Cloud Platform
            Service Account to be used by the BackupVault
            for taking backups. Specify the email address of
            the Backup Vault Service Account.
        log_retention_days (int):
            Optional. Applicable only for CloudSQL and AlloyDB
            resource_type.

            Configures how long logs will be stored. It is defined in
            “days”. This value should be greater than or equal to
            minimum enforced log retention duration of the backup vault.
        supported_resource_types (MutableSequence[str]):
            Output only. All resource types to which
            backupPlan can be applied.
        revision_id (str):
            Output only. The user friendly revision ID of the
            ``BackupPlanRevision``.

            Example: v0, v1, v2, etc.
        revision_name (str):
            Output only. The resource id of the ``BackupPlanRevision``.

            Format:
            ``projects/{project}/locations/{location}/backupPlans/{backup_plan}/revisions/{revision_id}``
    """

    class State(proto.Enum):
        r"""``State`` enumerates the possible states for a ``BackupPlan``.

        Values:
            STATE_UNSPECIFIED (0):
                State not set.
            CREATING (1):
                The resource is being created.
            ACTIVE (2):
                The resource has been created and is fully
                usable.
            DELETING (3):
                The resource is being deleted.
            INACTIVE (4):
                The resource has been created but is not
                usable.
            UPDATING (5):
                The resource is being updated.
        """

        STATE_UNSPECIFIED = 0
        CREATING = 1
        ACTIVE = 2
        DELETING = 3
        INACTIVE = 4
        UPDATING = 5

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    description: str = proto.Field(
        proto.STRING,
        number=2,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=3,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    backup_rules: MutableSequence["BackupRule"] = proto.RepeatedField(
        proto.MESSAGE,
        number=6,
        message="BackupRule",
    )
    state: State = proto.Field(
        proto.ENUM,
        number=7,
        enum=State,
    )
    resource_type: str = proto.Field(
        proto.STRING,
        number=8,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=9,
    )
    backup_vault: str = proto.Field(
        proto.STRING,
        number=10,
    )
    backup_vault_service_account: str = proto.Field(
        proto.STRING,
        number=11,
    )
    log_retention_days: int = proto.Field(
        proto.INT64,
        number=12,
    )
    supported_resource_types: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=13,
    )
    revision_id: str = proto.Field(
        proto.STRING,
        number=14,
    )
    revision_name: str = proto.Field(
        proto.STRING,
        number=15,
    )


class BackupRule(proto.Message):
    r"""``BackupRule`` binds the backup schedule to a retention policy.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        rule_id (str):
            Required. Immutable. The unique id of this ``BackupRule``.
            The ``rule_id`` is unique per ``BackupPlan``.The ``rule_id``
            must start with a lowercase letter followed by up to 62
            lowercase letters, numbers, or hyphens. Pattern,
            /[a-z][a-z0-9-]{,62}/.
        backup_retention_days (int):
            Required. Configures the duration for which
            backup data will be kept. It is defined in
            “days”. The value should be greater than or
            equal to minimum enforced retention of the
            backup vault.

            Minimum value is 1 and maximum value is 36159
            for custom retention on-demand backup.
            Minimum and maximum values are workload specific
            for all other rules.
        standard_schedule (google.cloud.backupdr_v1.types.StandardSchedule):
            Optional. Defines a schedule that runs within
            the confines of a defined window of time.

            This field is a member of `oneof`_ ``backup_schedule_oneof``.
    """

    rule_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    backup_retention_days: int = proto.Field(
        proto.INT32,
        number=4,
    )
    standard_schedule: "StandardSchedule" = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="backup_schedule_oneof",
        message="StandardSchedule",
    )


class StandardSchedule(proto.Message):
    r"""``StandardSchedule`` defines a schedule that run within the confines
    of a defined window of days. We can define recurrence type for
    schedule as HOURLY, DAILY, WEEKLY, MONTHLY or YEARLY.

    Attributes:
        recurrence_type (google.cloud.backupdr_v1.types.StandardSchedule.RecurrenceType):
            Required. Specifies the ``RecurrenceType`` for the schedule.
        hourly_frequency (int):
            Optional. Specifies frequency for hourly backups. A hourly
            frequency of 2 means jobs will run every 2 hours from start
            time till end time defined.

            This is required for ``recurrence_type``, ``HOURLY`` and is
            not applicable otherwise. A validation error will occur if a
            value is supplied and ``recurrence_type`` is not ``HOURLY``.

            Value of hourly frequency should be between 4 and 23.

            Reason for limit : We found that there is bandwidth
            limitation of 3GB/S for GMI while taking a backup and 5GB/S
            while doing a restore. Given the amount of parallel backups
            and restore we are targeting, this will potentially take the
            backup time to mins and hours (in worst case scenario).
        days_of_week (MutableSequence[google.type.dayofweek_pb2.DayOfWeek]):
            Optional. Specifies days of week like, MONDAY or TUESDAY, on
            which jobs will run.

            This is required for ``recurrence_type``, ``WEEKLY`` and is
            not applicable otherwise. A validation error will occur if a
            value is supplied and ``recurrence_type`` is not ``WEEKLY``.
        days_of_month (MutableSequence[int]):
            Optional. Specifies days of months like 1, 5, or 14 on which
            jobs will run.

            Values for ``days_of_month`` are only applicable for
            ``recurrence_type``, ``MONTHLY`` and ``YEARLY``. A
            validation error will occur if other values are supplied.
        week_day_of_month (google.cloud.backupdr_v1.types.WeekDayOfMonth):
            Optional. Specifies a week day of the month like, FIRST
            SUNDAY or LAST MONDAY, on which jobs will run. This will be
            specified by two fields in ``WeekDayOfMonth``, one for the
            day, e.g. ``MONDAY``, and one for the week, e.g. ``LAST``.

            This field is only applicable for ``recurrence_type``,
            ``MONTHLY`` and ``YEARLY``. A validation error will occur if
            other values are supplied.
        months (MutableSequence[google.type.month_pb2.Month]):
            Optional. Specifies the months of year, like ``FEBRUARY``
            and/or ``MAY``, on which jobs will run.

            This field is only applicable when ``recurrence_type`` is
            ``YEARLY``. A validation error will occur if other values
            are supplied.
        backup_window (google.cloud.backupdr_v1.types.BackupWindow):
            Required. A BackupWindow defines the window of day during
            which backup jobs will run. Jobs are queued at the beginning
            of the window and will be marked as ``NOT_RUN`` if they do
            not start by the end of the window.

            Note: running jobs will not be cancelled at the end of the
            window.
        time_zone (str):
            Required. The time zone to be used when interpreting the
            schedule. The value of this field must be a time zone name
            from the IANA tz database. See
            https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
            for the list of valid timezone names. For e.g.,
            Europe/Paris.
    """

    class RecurrenceType(proto.Enum):
        r"""``RecurrenceTypes`` enumerates the applicable periodicity for the
        schedule.

        Values:
            RECURRENCE_TYPE_UNSPECIFIED (0):
                recurrence type not set
            HOURLY (1):
                The ``BackupRule`` is to be applied hourly.
            DAILY (2):
                The ``BackupRule`` is to be applied daily.
            WEEKLY (3):
                The ``BackupRule`` is to be applied weekly.
            MONTHLY (4):
                The ``BackupRule`` is to be applied monthly.
            YEARLY (5):
                The ``BackupRule`` is to be applied yearly.
        """

        RECURRENCE_TYPE_UNSPECIFIED = 0
        HOURLY = 1
        DAILY = 2
        WEEKLY = 3
        MONTHLY = 4
        YEARLY = 5

    recurrence_type: RecurrenceType = proto.Field(
        proto.ENUM,
        number=1,
        enum=RecurrenceType,
    )
    hourly_frequency: int = proto.Field(
        proto.INT32,
        number=2,
    )
    days_of_week: MutableSequence[dayofweek_pb2.DayOfWeek] = proto.RepeatedField(
        proto.ENUM,
        number=3,
        enum=dayofweek_pb2.DayOfWeek,
    )
    days_of_month: MutableSequence[int] = proto.RepeatedField(
        proto.INT32,
        number=4,
    )
    week_day_of_month: "WeekDayOfMonth" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="WeekDayOfMonth",
    )
    months: MutableSequence[month_pb2.Month] = proto.RepeatedField(
        proto.ENUM,
        number=6,
        enum=month_pb2.Month,
    )
    backup_window: "BackupWindow" = proto.Field(
        proto.MESSAGE,
        number=7,
        message="BackupWindow",
    )
    time_zone: str = proto.Field(
        proto.STRING,
        number=8,
    )


class BackupWindow(proto.Message):
    r"""``BackupWindow`` defines a window of the day during which backup
    jobs will run.

    Attributes:
        start_hour_of_day (int):
            Required. The hour of day (0-23) when the
            window starts for e.g. if value of start hour of
            day is 6 that mean backup window start at 6:00.
        end_hour_of_day (int):
            Required. The hour of day (1-24) when the window end for
            e.g. if value of end hour of day is 10 that mean backup
            window end time is 10:00.

            End hour of day should be greater than start hour of day. 0
            <= start_hour_of_day < end_hour_of_day <= 24

            End hour of day is not include in backup window that mean if
            end_hour_of_day= 10 jobs should start before 10:00.
    """

    start_hour_of_day: int = proto.Field(
        proto.INT32,
        number=1,
    )
    end_hour_of_day: int = proto.Field(
        proto.INT32,
        number=2,
    )


class WeekDayOfMonth(proto.Message):
    r"""``WeekDayOfMonth`` defines the week day of the month on which the
    backups will run. The message combines a ``WeekOfMonth`` and
    ``DayOfWeek`` to produce values like ``FIRST``/``MONDAY`` or
    ``LAST``/``FRIDAY``.

    Attributes:
        week_of_month (google.cloud.backupdr_v1.types.WeekDayOfMonth.WeekOfMonth):
            Required. Specifies the week of the month.
        day_of_week (google.type.dayofweek_pb2.DayOfWeek):
            Required. Specifies the day of the week.
    """

    class WeekOfMonth(proto.Enum):
        r"""``WeekOfMonth`` enumerates possible weeks in the month, e.g. the
        first, third, or last week of the month.

        Values:
            WEEK_OF_MONTH_UNSPECIFIED (0):
                The zero value. Do not use.
            FIRST (1):
                The first week of the month.
            SECOND (2):
                The second week of the month.
            THIRD (3):
                The third week of the month.
            FOURTH (4):
                The fourth  week of the month.
            LAST (5):
                The last  week of the month.
        """

        WEEK_OF_MONTH_UNSPECIFIED = 0
        FIRST = 1
        SECOND = 2
        THIRD = 3
        FOURTH = 4
        LAST = 5

    week_of_month: WeekOfMonth = proto.Field(
        proto.ENUM,
        number=1,
        enum=WeekOfMonth,
    )
    day_of_week: dayofweek_pb2.DayOfWeek = proto.Field(
        proto.ENUM,
        number=2,
        enum=dayofweek_pb2.DayOfWeek,
    )


class CreateBackupPlanRequest(proto.Message):
    r"""The request message for creating a ``BackupPlan``.

    Attributes:
        parent (str):
            Required. The ``BackupPlan`` project and location in the
            format ``projects/{project}/locations/{location}``. In Cloud
            BackupDR locations map to GCP regions, for example
            **us-central1**.
        backup_plan_id (str):
            Required. The name of the ``BackupPlan`` to create. The name
            must be unique for the specified project and location.The
            name must start with a lowercase letter followed by up to 62
            lowercase letters, numbers, or hyphens. Pattern,
            /[a-z][a-z0-9-]{,62}/.
        backup_plan (google.cloud.backupdr_v1.types.BackupPlan):
            Required. The ``BackupPlan`` resource object to create.
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server will
            know to ignore the request if it has already
            been completed. The server will guarantee that
            for at least 60 minutes since the first request.

            For example, consider a situation where you make
            an initial request and t he request times out.
            If you make the request again with the same
            request ID, the server can check if original
            operation with the same request ID was received,
            and if so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    backup_plan_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    backup_plan: "BackupPlan" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="BackupPlan",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class ListBackupPlansRequest(proto.Message):
    r"""The request message for getting a list ``BackupPlan``.

    Attributes:
        parent (str):
            Required. The project and location for which to retrieve
            ``BackupPlans`` information. Format:
            ``projects/{project}/locations/{location}``. In Cloud
            BackupDR, locations map to GCP regions, for e.g.
            **us-central1**. To retrieve backup plans for all locations,
            use "-" for the ``{location}`` value.
        page_size (int):
            Optional. The maximum number of ``BackupPlans`` to return in
            a single response. If not specified, a default value will be
            chosen by the service. Note that the response may include a
            partial list and a caller should only rely on the response's
            [next_page_token][google.cloud.backupdr.v1.ListBackupPlansResponse.next_page_token]
            to determine if there are more instances left to be queried.
        page_token (str):
            Optional. The value of
            [next_page_token][google.cloud.backupdr.v1.ListBackupPlansResponse.next_page_token]
            received from a previous ``ListBackupPlans`` call. Provide
            this to retrieve the subsequent page in a multi-page list of
            results. When paginating, all other parameters provided to
            ``ListBackupPlans`` must match the call that provided the
            page token.
        filter (str):
            Optional. Field match expression used to
            filter the results.
        order_by (str):
            Optional. Field by which to sort the results.
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
    filter: str = proto.Field(
        proto.STRING,
        number=4,
    )
    order_by: str = proto.Field(
        proto.STRING,
        number=5,
    )


class ListBackupPlansResponse(proto.Message):
    r"""The response message for getting a list of ``BackupPlan``.

    Attributes:
        backup_plans (MutableSequence[google.cloud.backupdr_v1.types.BackupPlan]):
            The list of ``BackupPlans`` in the project for the specified
            location.

            If the ``{location}`` value in the request is "-", the
            response contains a list of resources from all locations. In
            case any location is unreachable, the response will only
            return backup plans in reachable locations and the
            'unreachable' field will be populated with a list of
            unreachable locations. BackupPlan
        next_page_token (str):
            A token which may be sent as
            [page_token][google.cloud.backupdr.v1.ListBackupPlansRequest.page_token]
            in a subsequent ``ListBackupPlans`` call to retrieve the
            next page of results. If this field is omitted or empty,
            then there are no more results to return.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    backup_plans: MutableSequence["BackupPlan"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="BackupPlan",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetBackupPlanRequest(proto.Message):
    r"""The request message for getting a ``BackupPlan``.

    Attributes:
        name (str):
            Required. The resource name of the ``BackupPlan`` to
            retrieve.

            Format:
            ``projects/{project}/locations/{location}/backupPlans/{backup_plan}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class DeleteBackupPlanRequest(proto.Message):
    r"""The request message for deleting a ``BackupPlan``.

    Attributes:
        name (str):
            Required. The resource name of the ``BackupPlan`` to delete.

            Format:
            ``projects/{project}/locations/{location}/backupPlans/{backup_plan}``
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server will
            know to ignore the request if it has already
            been completed. The server will guarantee that
            for at least 60 minutes after the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class UpdateBackupPlanRequest(proto.Message):
    r"""Request message for updating a backup plan.

    Attributes:
        backup_plan (google.cloud.backupdr_v1.types.BackupPlan):
            Required. The resource being updated
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. The list of fields to update. Field mask is used
            to specify the fields to be overwritten in the BackupPlan
            resource by the update. The fields specified in the
            update_mask are relative to the resource, not the full
            request. A field will be overwritten if it is in the mask.
            If the user does not provide a mask then the request will
            fail. Currently, these fields are supported in update:
            description, schedules, retention period, adding and
            removing Backup Rules.
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server will
            know to ignore the request if it has already
            been completed. The server will guarantee that
            for at least 60 minutes since the first request.

            For example, consider a situation where you make
            an initial request and t he request times out.
            If you make the request again with the same
            request ID, the server can check if original
            operation with the same request ID was received,
            and if so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
    """

    backup_plan: "BackupPlan" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="BackupPlan",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class BackupPlanRevision(proto.Message):
    r"""``BackupPlanRevision`` represents a snapshot of a ``BackupPlan`` at
    a point in time.

    Attributes:
        name (str):
            Output only. Identifier. The resource name of the
            ``BackupPlanRevision``.

            Format:
            ``projects/{project}/locations/{location}/backupPlans/{backup_plan}/revisions/{revision}``
        revision_id (str):
            Output only. The user friendly revision ID of the
            ``BackupPlanRevision``.

            Example: v0, v1, v2, etc.
        state (google.cloud.backupdr_v1.types.BackupPlanRevision.State):
            Output only. Resource State
        backup_plan_snapshot (google.cloud.backupdr_v1.types.BackupPlan):
            The Backup Plan being encompassed by this
            revision.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp that the revision
            was created.
    """

    class State(proto.Enum):
        r"""The state of the ``BackupPlanRevision``.

        Values:
            STATE_UNSPECIFIED (0):
                State not set.
            CREATING (1):
                The resource is being created.
            ACTIVE (2):
                The resource has been created and is fully
                usable.
            DELETING (3):
                The resource is being deleted.
            INACTIVE (4):
                The resource has been created but is not
                usable.
        """

        STATE_UNSPECIFIED = 0
        CREATING = 1
        ACTIVE = 2
        DELETING = 3
        INACTIVE = 4

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    revision_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=3,
        enum=State,
    )
    backup_plan_snapshot: "BackupPlan" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="BackupPlan",
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )


class GetBackupPlanRevisionRequest(proto.Message):
    r"""The request message for getting a ``BackupPlanRevision``.

    Attributes:
        name (str):
            Required. The resource name of the ``BackupPlanRevision`` to
            retrieve.

            Format:
            ``projects/{project}/locations/{location}/backupPlans/{backup_plan}/revisions/{revision}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListBackupPlanRevisionsRequest(proto.Message):
    r"""The request message for getting a list of ``BackupPlanRevision``.

    Attributes:
        parent (str):
            Required. The project and location for which to retrieve
            ``BackupPlanRevisions`` information. Format:
            ``projects/{project}/locations/{location}/backupPlans/{backup_plan}``.
            In Cloud BackupDR, locations map to GCP regions, for e.g.
            **us-central1**.
        page_size (int):
            Optional. The maximum number of ``BackupPlans`` to return in
            a single response. If not specified, a default value will be
            chosen by the service. Note that the response may include a
            partial list and a caller should only rely on the response's
            [next_page_token][google.cloud.backupdr.v1.ListBackupPlansResponse.next_page_token]
            to determine if there are more instances left to be queried.
        page_token (str):
            Optional. The value of
            [next_page_token][google.cloud.backupdr.v1.ListBackupPlansResponse.next_page_token]
            received from a previous ``ListBackupPlans`` call. Provide
            this to retrieve the subsequent page in a multi-page list of
            results. When paginating, all other parameters provided to
            ``ListBackupPlans`` must match the call that provided the
            page token.
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


class ListBackupPlanRevisionsResponse(proto.Message):
    r"""The response message for getting a list of ``BackupPlanRevision``.

    Attributes:
        backup_plan_revisions (MutableSequence[google.cloud.backupdr_v1.types.BackupPlanRevision]):
            The list of ``BackupPlanRevisions`` in the project for the
            specified location.

            If the ``{location}`` value in the request is "-", the
            response contains a list of resources from all locations. In
            case any location is unreachable, the response will only
            return backup plans in reachable locations and the
            'unreachable' field will be populated with a list of
            unreachable locations.
        next_page_token (str):
            A token which may be sent as
            [page_token][google.cloud.backupdr.v1.ListBackupPlanRevisionsRequest.page_token]
            in a subsequent ``ListBackupPlanRevisions`` call to retrieve
            the next page of results. If this field is omitted or empty,
            then there are no more results to return.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    backup_plan_revisions: MutableSequence["BackupPlanRevision"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="BackupPlanRevision",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
