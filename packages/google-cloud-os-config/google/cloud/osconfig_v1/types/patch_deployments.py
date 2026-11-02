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
import google.protobuf.field_mask_pb2 as field_mask_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import google.type.datetime_pb2 as datetime_pb2  # type: ignore
import google.type.dayofweek_pb2 as dayofweek_pb2  # type: ignore
import google.type.timeofday_pb2 as timeofday_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.osconfig_v1.types import patch_jobs

__protobuf__ = proto.module(
    package="google.cloud.osconfig.v1",
    manifest={
        "PatchDeployment",
        "OneTimeSchedule",
        "RecurringSchedule",
        "WeeklySchedule",
        "MonthlySchedule",
        "WeekDayOfMonth",
        "CreatePatchDeploymentRequest",
        "GetPatchDeploymentRequest",
        "ListPatchDeploymentsRequest",
        "ListPatchDeploymentsResponse",
        "DeletePatchDeploymentRequest",
        "UpdatePatchDeploymentRequest",
        "PausePatchDeploymentRequest",
        "ResumePatchDeploymentRequest",
    },
)


class PatchDeployment(proto.Message):
    r"""Patch deployments are configurations that individual patch jobs use
    to complete a patch. These configurations include instance filter,
    package repository settings, and a schedule. For more information
    about creating and managing patch deployments, see `Scheduling patch
    jobs <https://cloud.google.com/compute/docs/os-patch-management/schedule-patch-jobs>`__.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Unique name for the patch deployment resource in a project.
            The patch deployment name is in the form:
            ``projects/{project_id}/patchDeployments/{patch_deployment_id}``.
            This field is ignored when you create a new patch
            deployment.
        description (str):
            Optional. Description of the patch
            deployment. Length of the description is limited
            to 1024 characters.
        instance_filter (google.cloud.osconfig_v1.types.PatchInstanceFilter):
            Required. VM instances to patch.
        patch_config (google.cloud.osconfig_v1.types.PatchConfig):
            Optional. Patch configuration that is
            applied.
        duration (google.protobuf.duration_pb2.Duration):
            Optional. Duration of the patch. After the
            duration ends, the patch times out.
        one_time_schedule (google.cloud.osconfig_v1.types.OneTimeSchedule):
            Required. Schedule a one-time execution.

            This field is a member of `oneof`_ ``schedule``.
        recurring_schedule (google.cloud.osconfig_v1.types.RecurringSchedule):
            Required. Schedule recurring executions.

            This field is a member of `oneof`_ ``schedule``.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time the patch deployment was created.
            Timestamp is in
            `RFC3339 <https://www.ietf.org/rfc/rfc3339.txt>`__ text
            format.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time the patch deployment was last updated.
            Timestamp is in
            `RFC3339 <https://www.ietf.org/rfc/rfc3339.txt>`__ text
            format.
        last_execute_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The last time a patch job was started by this
            deployment. Timestamp is in
            `RFC3339 <https://www.ietf.org/rfc/rfc3339.txt>`__ text
            format.
        rollout (google.cloud.osconfig_v1.types.PatchRollout):
            Optional. Rollout strategy of the patch job.
        state (google.cloud.osconfig_v1.types.PatchDeployment.State):
            Output only. Current state of the patch
            deployment.
    """

    class State(proto.Enum):
        r"""Represents state of patch peployment.

        Values:
            STATE_UNSPECIFIED (0):
                The default value. This value is used if the
                state is omitted.
            ACTIVE (1):
                Active value means that patch deployment
                generates Patch Jobs.
            PAUSED (2):
                Paused value means that patch deployment does
                not generate Patch jobs. Requires user action to
                move in and out from this state.
        """

        STATE_UNSPECIFIED = 0
        ACTIVE = 1
        PAUSED = 2

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    description: str = proto.Field(
        proto.STRING,
        number=2,
    )
    instance_filter: patch_jobs.PatchInstanceFilter = proto.Field(
        proto.MESSAGE,
        number=3,
        message=patch_jobs.PatchInstanceFilter,
    )
    patch_config: patch_jobs.PatchConfig = proto.Field(
        proto.MESSAGE,
        number=4,
        message=patch_jobs.PatchConfig,
    )
    duration: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=5,
        message=duration_pb2.Duration,
    )
    one_time_schedule: "OneTimeSchedule" = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="schedule",
        message="OneTimeSchedule",
    )
    recurring_schedule: "RecurringSchedule" = proto.Field(
        proto.MESSAGE,
        number=7,
        oneof="schedule",
        message="RecurringSchedule",
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=8,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=9,
        message=timestamp_pb2.Timestamp,
    )
    last_execute_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=10,
        message=timestamp_pb2.Timestamp,
    )
    rollout: patch_jobs.PatchRollout = proto.Field(
        proto.MESSAGE,
        number=11,
        message=patch_jobs.PatchRollout,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=12,
        enum=State,
    )


class OneTimeSchedule(proto.Message):
    r"""Sets the time for a one time patch deployment. Timestamp is in
    `RFC3339 <https://www.ietf.org/rfc/rfc3339.txt>`__ text format.

    Attributes:
        execute_time (google.protobuf.timestamp_pb2.Timestamp):
            Required. The desired patch job execution
            time.
    """

    execute_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )


class RecurringSchedule(proto.Message):
    r"""Sets the time for recurring patch deployments.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        time_zone (google.type.datetime_pb2.TimeZone):
            Required. Defines the time zone that ``time_of_day`` is
            relative to. The rules for daylight saving time are
            determined by the chosen time zone.
        start_time (google.protobuf.timestamp_pb2.Timestamp):
            Optional. The time that the recurring schedule becomes
            effective. Defaults to ``create_time`` of the patch
            deployment.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            Optional. The end time at which a recurring
            patch deployment schedule is no longer active.
        time_of_day (google.type.timeofday_pb2.TimeOfDay):
            Required. Time of the day to run a recurring
            deployment.
        frequency (google.cloud.osconfig_v1.types.RecurringSchedule.Frequency):
            Required. The frequency unit of this
            recurring schedule.
        weekly (google.cloud.osconfig_v1.types.WeeklySchedule):
            Required. Schedule with weekly executions.

            This field is a member of `oneof`_ ``schedule_config``.
        monthly (google.cloud.osconfig_v1.types.MonthlySchedule):
            Required. Schedule with monthly executions.

            This field is a member of `oneof`_ ``schedule_config``.
        last_execute_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the last patch job ran
            successfully.
        next_execute_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the next patch job is
            scheduled to run.
    """

    class Frequency(proto.Enum):
        r"""Specifies the frequency of the recurring patch deployments.

        Values:
            FREQUENCY_UNSPECIFIED (0):
                Invalid. A frequency must be specified.
            WEEKLY (1):
                Indicates that the frequency of recurrence
                should be expressed in terms of weeks.
            MONTHLY (2):
                Indicates that the frequency of recurrence
                should be expressed in terms of months.
            DAILY (3):
                Indicates that the frequency of recurrence
                should be expressed in terms of days.
        """

        FREQUENCY_UNSPECIFIED = 0
        WEEKLY = 1
        MONTHLY = 2
        DAILY = 3

    time_zone: datetime_pb2.TimeZone = proto.Field(
        proto.MESSAGE,
        number=1,
        message=datetime_pb2.TimeZone,
    )
    start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    time_of_day: timeofday_pb2.TimeOfDay = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timeofday_pb2.TimeOfDay,
    )
    frequency: Frequency = proto.Field(
        proto.ENUM,
        number=5,
        enum=Frequency,
    )
    weekly: "WeeklySchedule" = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="schedule_config",
        message="WeeklySchedule",
    )
    monthly: "MonthlySchedule" = proto.Field(
        proto.MESSAGE,
        number=7,
        oneof="schedule_config",
        message="MonthlySchedule",
    )
    last_execute_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=9,
        message=timestamp_pb2.Timestamp,
    )
    next_execute_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=10,
        message=timestamp_pb2.Timestamp,
    )


class WeeklySchedule(proto.Message):
    r"""Represents a weekly schedule.

    Attributes:
        day_of_week (google.type.dayofweek_pb2.DayOfWeek):
            Required. Day of the week.
    """

    day_of_week: dayofweek_pb2.DayOfWeek = proto.Field(
        proto.ENUM,
        number=1,
        enum=dayofweek_pb2.DayOfWeek,
    )


class MonthlySchedule(proto.Message):
    r"""Represents a monthly schedule. An example of a valid monthly
    schedule is "on the third Tuesday of the month" or "on the 15th
    of the month".

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        week_day_of_month (google.cloud.osconfig_v1.types.WeekDayOfMonth):
            Required. Week day in a month.

            This field is a member of `oneof`_ ``day_of_month``.
        month_day (int):
            Required. One day of the month. 1-31
            indicates the 1st to the 31st day. -1 indicates
            the last day of the month. Months without the
            target day will be skipped. For example, a
            schedule to run "every month on the 31st" will
            not run in February, April, June, etc.

            This field is a member of `oneof`_ ``day_of_month``.
    """

    week_day_of_month: "WeekDayOfMonth" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="day_of_month",
        message="WeekDayOfMonth",
    )
    month_day: int = proto.Field(
        proto.INT32,
        number=2,
        oneof="day_of_month",
    )


class WeekDayOfMonth(proto.Message):
    r"""Represents one week day in a month. An example is "the 4th
    Sunday".

    Attributes:
        week_ordinal (int):
            Required. Week number in a month. 1-4
            indicates the 1st to 4th week of the month. -1
            indicates the last week of the month.
        day_of_week (google.type.dayofweek_pb2.DayOfWeek):
            Required. A day of the week.
        day_offset (int):
            Optional. Represents the number of days before or after the
            given week day of month that the patch deployment is
            scheduled for. For example if ``week_ordinal`` and
            ``day_of_week`` values point to the second day of the month
            and this ``day_offset`` value is set to ``3``, the patch
            deployment takes place three days after the second Tuesday
            of the month. If this value is negative, for example -5, the
            patches are deployed five days before before the second
            Tuesday of the month. Allowed values are in range [-30, 30].
    """

    week_ordinal: int = proto.Field(
        proto.INT32,
        number=1,
    )
    day_of_week: dayofweek_pb2.DayOfWeek = proto.Field(
        proto.ENUM,
        number=2,
        enum=dayofweek_pb2.DayOfWeek,
    )
    day_offset: int = proto.Field(
        proto.INT32,
        number=3,
    )


class CreatePatchDeploymentRequest(proto.Message):
    r"""A request message for creating a patch deployment.

    Attributes:
        parent (str):
            Required. The project to apply this patch deployment to in
            the form ``projects/*``.
        patch_deployment_id (str):
            Required. A name for the patch deployment in the project.
            When creating a name the following rules apply:

            - Must contain only lowercase letters, numbers, and hyphens.
            - Must start with a letter.
            - Must be between 1-63 characters.
            - Must end with a number or a letter.
            - Must be unique within the project.
        patch_deployment (google.cloud.osconfig_v1.types.PatchDeployment):
            Required. The patch deployment to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    patch_deployment_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    patch_deployment: "PatchDeployment" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="PatchDeployment",
    )


class GetPatchDeploymentRequest(proto.Message):
    r"""A request message for retrieving a patch deployment.

    Attributes:
        name (str):
            Required. The resource name of the patch deployment in the
            form ``projects/*/patchDeployments/*``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListPatchDeploymentsRequest(proto.Message):
    r"""A request message for listing patch deployments.

    Attributes:
        parent (str):
            Required. The resource name of the parent in the form
            ``projects/*``.
        page_size (int):
            Optional. The maximum number of patch
            deployments to return. Default is 100.
        page_token (str):
            Optional. A pagination token returned from a
            previous call to ListPatchDeployments that
            indicates where this listing should continue
            from.
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


class ListPatchDeploymentsResponse(proto.Message):
    r"""A response message for listing patch deployments.

    Attributes:
        patch_deployments (MutableSequence[google.cloud.osconfig_v1.types.PatchDeployment]):
            The list of patch deployments.
        next_page_token (str):
            A pagination token that can be used to get
            the next page of patch deployments.
    """

    @property
    def raw_page(self):
        return self

    patch_deployments: MutableSequence["PatchDeployment"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="PatchDeployment",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class DeletePatchDeploymentRequest(proto.Message):
    r"""A request message for deleting a patch deployment.

    Attributes:
        name (str):
            Required. The resource name of the patch deployment in the
            form ``projects/*/patchDeployments/*``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdatePatchDeploymentRequest(proto.Message):
    r"""A request message for updating a patch deployment.

    Attributes:
        patch_deployment (google.cloud.osconfig_v1.types.PatchDeployment):
            Required. The patch deployment to Update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. Field mask that controls which
            fields of the patch deployment should be
            updated.
    """

    patch_deployment: "PatchDeployment" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="PatchDeployment",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class PausePatchDeploymentRequest(proto.Message):
    r"""A request message for pausing a patch deployment.

    Attributes:
        name (str):
            Required. The resource name of the patch deployment in the
            form ``projects/*/patchDeployments/*``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ResumePatchDeploymentRequest(proto.Message):
    r"""A request message for resuming a patch deployment.

    Attributes:
        name (str):
            Required. The resource name of the patch deployment in the
            form ``projects/*/patchDeployments/*``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
