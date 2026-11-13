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

import google.type.date_pb2 as date_pb2  # type: ignore
import google.type.dayofweek_pb2 as dayofweek_pb2  # type: ignore
import google.type.timeofday_pb2 as timeofday_pb2  # type: ignore
import proto  # type: ignore

from google.ads.admanager_v1.types import report_definition

__protobuf__ = proto.module(
    package="google.ads.admanager.v1",
    manifest={
        "ScheduleOptions",
    },
)


class ScheduleOptions(proto.Message):
    r"""The options for a scheduled report.

    Attributes:
        schedule (google.ads.admanager_v1.types.ScheduleOptions.Schedule):
            Information pertaining to schedule itself.
        delivery_condition (google.ads.admanager_v1.types.ScheduleOptions.DeliveryCondition):
            Option for when to deliver the scheduled
            report.
        flags (MutableSequence[google.ads.admanager_v1.types.ReportDefinition.Flag]):
            Optional. The flags evaluated when
            ReportDeliveryOption.WHEN_FLAG_PRESENT is specified.
    """

    class DeliveryCondition(proto.Enum):
        r"""Condition for when to email the scheduled report.

        Values:
            NEVER (0):
                Never deliver report.
            ALWAYS (1):
                Always deliver report.
            WHEN_FLAG_CONDITIONS_MET (2):
                Deliver report when flag's conditions are
                met.
        """

        NEVER = 0
        ALWAYS = 1
        WHEN_FLAG_CONDITIONS_MET = 2

    class Schedule(proto.Message):
        r"""The schedule for the report

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            weekly_schedule (google.ads.admanager_v1.types.ScheduleOptions.Schedule.WeeklySchedule):
                Days of week to schedule report run.

                This field is a member of `oneof`_ ``frequency_schedule``.
            monthly_schedule (google.ads.admanager_v1.types.ScheduleOptions.Schedule.MonthlySchedule):
                Days of month to schedule report run.

                This field is a member of `oneof`_ ``frequency_schedule``.
            start_date (google.type.date_pb2.Date):
                Date for the first run of the report.
            end_date (google.type.date_pb2.Date):
                Date for the final run of the report.
            frequency (google.ads.admanager_v1.types.ScheduleOptions.Schedule.Frequency):
                Frequency to run report.
            start_time (google.type.timeofday_pb2.TimeOfDay):
                Indicates start time for schedule to run. Will use the
                time_zone from
                [ReportDefinition][google.ads.admanager.v1.ReportDefinition].
                Defaults to the publisher's time zone if not specified.

                For HOURLY, TWO_TIMES_DAILY, THREE_TIMES_DAILY, or
                FOUR_TIMES_DAILY, this will be the time of day that the
                first report will run on the first day. For example, if the
                start time is 2:00 PM, and the frequency is
                THREE_TIMES_DAILY, the first day will have reports scheduled
                at 2:00 PM, 10:00 PM. Each subsequent day will have reports
                scheduled at 6:00 AM, 2:00 PM, 10:00 PM.
        """

        class Frequency(proto.Enum):
            r"""Frequency to run report.

            Values:
                FREQUENCY_UNSPECIFIED (0):
                    No Frequency specified.
                HOURLY (1):
                    Schedule report to run every hour.
                TWO_TIMES_DAILY (2):
                    Schedule report to run twice a day (every 12
                    hours).
                THREE_TIMES_DAILY (3):
                    Schedule report to run three times a day
                    (every 8 hours).
                FOUR_TIMES_DAILY (4):
                    Schedule report to run four times a day
                    (every 6 hours).
                DAILY (5):
                    Schedule report to run on a daily basis.
                WEEKLY (6):
                    Schedule report to run on a weekly basis.
                MONTHLY (7):
                    Schedule report to run on a monthly basis.
            """

            FREQUENCY_UNSPECIFIED = 0
            HOURLY = 1
            TWO_TIMES_DAILY = 2
            THREE_TIMES_DAILY = 3
            FOUR_TIMES_DAILY = 4
            DAILY = 5
            WEEKLY = 6
            MONTHLY = 7

        class WeeklySchedule(proto.Message):
            r"""Days of week to schedule report run.

            Attributes:
                weekly_scheduled_days (MutableSequence[google.type.dayofweek_pb2.DayOfWeek]):
                    Specifies days of the week on which to run
                    report.
            """

            weekly_scheduled_days: MutableSequence[dayofweek_pb2.DayOfWeek] = (
                proto.RepeatedField(
                    proto.ENUM,
                    number=1,
                    enum=dayofweek_pb2.DayOfWeek,
                )
            )

        class MonthlySchedule(proto.Message):
            r"""Days of Month to schedule report run.

            Attributes:
                monthly_scheduled_days (MutableSequence[int]):
                    Specifies days of the month to run report.
                    Range is from 1-31. Will ignore days that are
                    not valid for the given month.
            """

            monthly_scheduled_days: MutableSequence[int] = proto.RepeatedField(
                proto.INT32,
                number=1,
            )

        weekly_schedule: "ScheduleOptions.Schedule.WeeklySchedule" = proto.Field(
            proto.MESSAGE,
            number=6,
            oneof="frequency_schedule",
            message="ScheduleOptions.Schedule.WeeklySchedule",
        )
        monthly_schedule: "ScheduleOptions.Schedule.MonthlySchedule" = proto.Field(
            proto.MESSAGE,
            number=7,
            oneof="frequency_schedule",
            message="ScheduleOptions.Schedule.MonthlySchedule",
        )
        start_date: date_pb2.Date = proto.Field(
            proto.MESSAGE,
            number=1,
            message=date_pb2.Date,
        )
        end_date: date_pb2.Date = proto.Field(
            proto.MESSAGE,
            number=2,
            message=date_pb2.Date,
        )
        frequency: "ScheduleOptions.Schedule.Frequency" = proto.Field(
            proto.ENUM,
            number=3,
            enum="ScheduleOptions.Schedule.Frequency",
        )
        start_time: timeofday_pb2.TimeOfDay = proto.Field(
            proto.MESSAGE,
            number=4,
            message=timeofday_pb2.TimeOfDay,
        )

    schedule: Schedule = proto.Field(
        proto.MESSAGE,
        number=1,
        message=Schedule,
    )
    delivery_condition: DeliveryCondition = proto.Field(
        proto.ENUM,
        number=2,
        enum=DeliveryCondition,
    )
    flags: MutableSequence[report_definition.ReportDefinition.Flag] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=3,
            message=report_definition.ReportDefinition.Flag,
        )
    )


__all__ = tuple(sorted(__protobuf__.manifest))
