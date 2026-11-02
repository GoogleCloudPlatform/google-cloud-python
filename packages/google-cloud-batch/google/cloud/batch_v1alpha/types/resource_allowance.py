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
import google.type.interval_pb2 as interval_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.batch_v1alpha.types import notification

__protobuf__ = proto.module(
    package="google.cloud.batch.v1alpha",
    manifest={
        "CalendarPeriod",
        "ResourceAllowanceState",
        "ResourceAllowance",
        "UsageResourceAllowance",
        "UsageResourceAllowanceSpec",
        "UsageResourceAllowanceStatus",
    },
)


class CalendarPeriod(proto.Enum):
    r"""A ``CalendarPeriod`` represents the abstract concept of a time
    period that has a canonical start. All calendar times begin at 12 AM
    US and Canadian Pacific Time (UTC-8).

    Values:
        CALENDAR_PERIOD_UNSPECIFIED (0):
            Unspecified.
        MONTH (1):
            The month starts on the first date of the
            month and resets at the beginning of each month.
        QUARTER (2):
            The quarter starts on dates January 1, April
            1, July 1, and October 1 of each year and resets
            at the beginning of the next quarter.
        YEAR (3):
            The year starts on January 1 and resets at
            the beginning of the next year.
        WEEK (4):
            The week period starts and resets every
            Monday.
        DAY (5):
            The day starts at 12:00am.
    """

    CALENDAR_PERIOD_UNSPECIFIED = 0
    MONTH = 1
    QUARTER = 2
    YEAR = 3
    WEEK = 4
    DAY = 5


class ResourceAllowanceState(proto.Enum):
    r"""ResourceAllowance valid state.

    Values:
        RESOURCE_ALLOWANCE_STATE_UNSPECIFIED (0):
            Unspecified.
        RESOURCE_ALLOWANCE_ACTIVE (1):
            ResourceAllowance is active and in use.
        RESOURCE_ALLOWANCE_DEPLETED (2):
            ResourceAllowance limit is reached.
    """

    RESOURCE_ALLOWANCE_STATE_UNSPECIFIED = 0
    RESOURCE_ALLOWANCE_ACTIVE = 1
    RESOURCE_ALLOWANCE_DEPLETED = 2


class ResourceAllowance(proto.Message):
    r"""The Resource Allowance description for Cloud Batch.
    Only one Resource Allowance is supported now under a specific
    location and project.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        usage_resource_allowance (google.cloud.batch_v1alpha.types.UsageResourceAllowance):
            The detail of usage resource allowance.

            This field is a member of `oneof`_ ``resource_allowance``.
        name (str):
            Identifier. ResourceAllowance name.
            For example:

            "projects/123456/locations/us-central1/resourceAllowances/resource-allowance-1".
        uid (str):
            Output only. A system generated unique ID (in
            UUID4 format) for the ResourceAllowance.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time when the ResourceAllowance
            was created.
        labels (MutableMapping[str, str]):
            Optional. Labels are attributes that can be set and used by
            both the user and by Batch. Labels must meet the following
            constraints:

            - Keys and values can contain only lowercase letters,
              numeric characters, underscores, and dashes.
            - All characters must use UTF-8 encoding, and international
              characters are allowed.
            - Keys must start with a lowercase letter or international
              character.
            - Each resource is limited to a maximum of 64 labels.

            Both keys and values are additionally constrained to be <=
            128 bytes.
        notifications (MutableSequence[google.cloud.batch_v1alpha.types.Notification]):
            Optional. Notification configurations.
    """

    usage_resource_allowance: "UsageResourceAllowance" = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="resource_allowance",
        message="UsageResourceAllowance",
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
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=5,
    )
    notifications: MutableSequence[notification.Notification] = proto.RepeatedField(
        proto.MESSAGE,
        number=6,
        message=notification.Notification,
    )


class UsageResourceAllowance(proto.Message):
    r"""UsageResourceAllowance describes the detail of usage resource
    allowance.

    Attributes:
        spec (google.cloud.batch_v1alpha.types.UsageResourceAllowanceSpec):
            Required. Spec of a usage ResourceAllowance.
        status (google.cloud.batch_v1alpha.types.UsageResourceAllowanceStatus):
            Output only. Status of a usage
            ResourceAllowance.
    """

    spec: "UsageResourceAllowanceSpec" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="UsageResourceAllowanceSpec",
    )
    status: "UsageResourceAllowanceStatus" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="UsageResourceAllowanceStatus",
    )


class UsageResourceAllowanceSpec(proto.Message):
    r"""Spec of a usage ResourceAllowance.

    Attributes:
        type_ (str):
            Required. Spec type is unique for each usage
            ResourceAllowance. Batch now only supports type
            as "cpu-core-hours" for CPU usage consumption
            tracking.
        limit (google.cloud.batch_v1alpha.types.UsageResourceAllowanceSpec.Limit):
            Required. Threshold of a
            UsageResourceAllowance limiting how many
            resources can be consumed for each type.
    """

    class Limit(proto.Message):
        r"""UsageResourceAllowance limitation.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            calendar_period (google.cloud.batch_v1alpha.types.CalendarPeriod):
                Optional. A CalendarPeriod represents the
                abstract concept of a time period that has a
                canonical start.

                This field is a member of `oneof`_ ``duration``.
            limit (float):
                Required. Limit value of a UsageResourceAllowance within its
                one duration.

                Limit cannot be a negative value. Default is 0. For example,
                you can set ``limit`` as 10000.0 with duration of the
                current month by setting ``calendar_period`` field as
                monthly. That means in your current month, 10000.0 is the
                core hour limitation that your resources are allowed to
                consume.

                This field is a member of `oneof`_ ``_limit``.
        """

        calendar_period: "CalendarPeriod" = proto.Field(
            proto.ENUM,
            number=1,
            oneof="duration",
            enum="CalendarPeriod",
        )
        limit: float = proto.Field(
            proto.DOUBLE,
            number=2,
            optional=True,
        )

    type_: str = proto.Field(
        proto.STRING,
        number=1,
    )
    limit: Limit = proto.Field(
        proto.MESSAGE,
        number=2,
        message=Limit,
    )


class UsageResourceAllowanceStatus(proto.Message):
    r"""Status of a usage ResourceAllowance.

    Attributes:
        state (google.cloud.batch_v1alpha.types.ResourceAllowanceState):
            Output only. ResourceAllowance state.
        limit_status (google.cloud.batch_v1alpha.types.UsageResourceAllowanceStatus.LimitStatus):
            Output only. ResourceAllowance consumption
            status for usage resources.
        report (google.cloud.batch_v1alpha.types.UsageResourceAllowanceStatus.ConsumptionReport):
            Output only. The report of ResourceAllowance
            consumptions in a time period.
    """

    class LimitStatus(proto.Message):
        r"""UsageResourceAllowanceStatus detail about usage consumption.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            consumption_interval (google.type.interval_pb2.Interval):
                Output only. The consumption interval.
            limit (float):
                Output only. Limit value of a
                UsageResourceAllowance within its one duration.

                This field is a member of `oneof`_ ``_limit``.
            consumed (float):
                Output only. Accumulated consumption during
                ``consumption_interval``.

                This field is a member of `oneof`_ ``_consumed``.
        """

        consumption_interval: interval_pb2.Interval = proto.Field(
            proto.MESSAGE,
            number=1,
            message=interval_pb2.Interval,
        )
        limit: float = proto.Field(
            proto.DOUBLE,
            number=2,
            optional=True,
        )
        consumed: float = proto.Field(
            proto.DOUBLE,
            number=3,
            optional=True,
        )

    class PeriodConsumption(proto.Message):
        r"""

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            consumption_interval (google.type.interval_pb2.Interval):
                Output only. The consumption interval.
            consumed (float):
                Output only. Accumulated consumption during
                ``consumption_interval``.

                This field is a member of `oneof`_ ``_consumed``.
        """

        consumption_interval: interval_pb2.Interval = proto.Field(
            proto.MESSAGE,
            number=1,
            message=interval_pb2.Interval,
        )
        consumed: float = proto.Field(
            proto.DOUBLE,
            number=2,
            optional=True,
        )

    class ConsumptionReport(proto.Message):
        r"""ConsumptionReport is the report of ResourceAllowance
        consumptions in a time period.

        Attributes:
            latest_period_consumptions (MutableMapping[str, google.cloud.batch_v1alpha.types.UsageResourceAllowanceStatus.PeriodConsumption]):
                Output only. ResourceAllowance consumptions
                in the latest calendar period. Key is the
                calendar period in string format. Batch
                currently supports HOUR, DAY, MONTH and YEAR.
        """

        latest_period_consumptions: MutableMapping[
            str, "UsageResourceAllowanceStatus.PeriodConsumption"
        ] = proto.MapField(
            proto.STRING,
            proto.MESSAGE,
            number=1,
            message="UsageResourceAllowanceStatus.PeriodConsumption",
        )

    state: "ResourceAllowanceState" = proto.Field(
        proto.ENUM,
        number=1,
        enum="ResourceAllowanceState",
    )
    limit_status: LimitStatus = proto.Field(
        proto.MESSAGE,
        number=2,
        message=LimitStatus,
    )
    report: ConsumptionReport = proto.Field(
        proto.MESSAGE,
        number=3,
        message=ConsumptionReport,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
