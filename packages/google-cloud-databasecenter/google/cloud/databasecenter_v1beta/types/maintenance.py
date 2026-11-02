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
import google.type.date_pb2 as date_pb2  # type: ignore
import google.type.dayofweek_pb2 as dayofweek_pb2  # type: ignore
import google.type.timeofday_pb2 as timeofday_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.databasecenter.v1beta",
    manifest={
        "Phase",
        "MaintenanceState",
        "PossibleFailureReason",
        "ResourceMaintenanceSchedule",
        "ResourceMaintenanceDenySchedule",
        "UpcomingMaintenance",
        "MaintenanceInfo",
    },
)


class Phase(proto.Enum):
    r"""Phase/Week of the maintenance window. This is to capture
    order of maintenance. For example, for Cloud SQL resources -
    https://cloud.google.com/sql/docs/mysql/maintenance. This enum
    can be extended to support DB Center specific phases for
    recommendation plan generation.

    Values:
        PHASE_UNSPECIFIED (0):
            Phase is unspecified.
        PHASE_WEEK1 (1):
            Week 1.
        PHASE_WEEK2 (2):
            Week 2.
        PHASE_WEEK5 (3):
            Week 5.
        PHASE_ANY (4):
            Any phase.
    """

    PHASE_UNSPECIFIED = 0
    PHASE_WEEK1 = 1
    PHASE_WEEK2 = 2
    PHASE_WEEK5 = 3
    PHASE_ANY = 4


class MaintenanceState(proto.Enum):
    r"""Resource maintenance state.

    Values:
        MAINTENANCE_STATE_UNSPECIFIED (0):
            Status is unspecified.
        MAINTENANCE_STATE_SCHEDULED (1):
            Maintenance is scheduled.
        MAINTENANCE_STATE_IN_PROGRESS (2):
            Maintenance is in progress.
        MAINTENANCE_STATE_COMPLETED (3):
            Maintenance is completed.
        MAINTENANCE_STATE_FAILED (4):
            Maintenance has failed.
    """

    MAINTENANCE_STATE_UNSPECIFIED = 0
    MAINTENANCE_STATE_SCHEDULED = 1
    MAINTENANCE_STATE_IN_PROGRESS = 2
    MAINTENANCE_STATE_COMPLETED = 3
    MAINTENANCE_STATE_FAILED = 4


class PossibleFailureReason(proto.Enum):
    r"""Possible reasons why the maintenance is not completed. STATE_FAILED
    maintenance state may not always have a failure reason.

    Values:
        POSSIBLE_FAILURE_REASON_UNSPECIFIED (0):
            Failure reason is unspecified.
        POSSIBLE_FAILURE_REASON_DENY_POLICY_CONFLICT (1):
            Maintenance may not be completed because
            there is a deny policy overlapping with upcoming
            maintenance schedule.
        POSSIBLE_FAILURE_REASON_INSTANCE_IN_STOPPED_STATE (2):
            Maintenance may not be completed because the
            instance is stopped.
    """

    POSSIBLE_FAILURE_REASON_UNSPECIFIED = 0
    POSSIBLE_FAILURE_REASON_DENY_POLICY_CONFLICT = 1
    POSSIBLE_FAILURE_REASON_INSTANCE_IN_STOPPED_STATE = 2


class ResourceMaintenanceSchedule(proto.Message):
    r"""Maintenance window for the database resource. It specifies
    preferred time and day of the week and phase in some cases, when
    the maintenance can start.

    Attributes:
        start_time (google.type.timeofday_pb2.TimeOfDay):
            Optional. Preferred time to start the
            maintenance operation on the specified day.
        day (google.type.dayofweek_pb2.DayOfWeek):
            Optional. Preferred day of the week for
            maintenance, e.g. MONDAY, TUESDAY, etc.
        phase (google.cloud.databasecenter_v1beta.types.Phase):
            Optional. Phase of the maintenance window.
            This is to capture order of maintenance. For
            example, for Cloud SQL resources, this can be
            used to capture if the maintenance window is in
            Week1, Week2, Week5, etc. Non production
            resources are usually part of early phase. For
            more details, refer to Cloud SQL resources -
            https://cloud.google.com/sql/docs/mysql/maintenance
    """

    start_time: timeofday_pb2.TimeOfDay = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timeofday_pb2.TimeOfDay,
    )
    day: dayofweek_pb2.DayOfWeek = proto.Field(
        proto.ENUM,
        number=2,
        enum=dayofweek_pb2.DayOfWeek,
    )
    phase: "Phase" = proto.Field(
        proto.ENUM,
        number=3,
        enum="Phase",
    )


class ResourceMaintenanceDenySchedule(proto.Message):
    r"""Deny maintenance period for the database resource. It
    specifies the time range during which the maintenance cannot
    start. This is configured by the customer.

    Attributes:
        start_date (google.type.date_pb2.Date):
            Optional. The start date of the deny
            maintenance period.
        end_date (google.type.date_pb2.Date):
            Optional. Deny period end date.
        time (google.type.timeofday_pb2.TimeOfDay):
            Optional. Time in UTC when the deny period starts on
            start_date and ends on end_date.
    """

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
    time: timeofday_pb2.TimeOfDay = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timeofday_pb2.TimeOfDay,
    )


class UpcomingMaintenance(proto.Message):
    r"""Upcoming maintenance window for the database resource.

    Attributes:
        start_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Start time of the upcoming
            maintenance. Start time is always populated when
            an upcoming maintenance is scheduled.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. End time of the upcoming
            maintenance. This is only populated for an
            engine, if end time is public for the engine.
    """

    start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )
    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )


class MaintenanceInfo(proto.Message):
    r"""MaintenanceInfo to capture the maintenance details of
    database resource.

    Attributes:
        maintenance_schedule (google.cloud.databasecenter_v1beta.types.ResourceMaintenanceSchedule):
            Optional. Maintenance window for the database
            resource.
        deny_maintenance_schedules (MutableSequence[google.cloud.databasecenter_v1beta.types.ResourceMaintenanceDenySchedule]):
            Optional. List of Deny maintenance period for
            the database resource.
        maintenance_version (str):
            Output only. Current Maintenance version of the database
            resource. Example: "MYSQL_8_0_41.R20250531.01_15".
        current_version_release_date (google.type.date_pb2.Date):
            Output only. The date when the maintenance
            version was released.
        upcoming_maintenance (google.cloud.databasecenter_v1beta.types.UpcomingMaintenance):
            Output only. Upcoming maintenance window for the database
            resource. This is only populated for an engine, if upcoming
            maintenance is scheduled for the resource. This schedule is
            generated per engine and engine version, and there is only
            one upcoming maintenance window at any given time. In case
            of upcoming maintenance, the maintenance_state will be set
            to SCHEDULED first, and then IN_PROGRESS when the
            maintenance window starts.
        state (google.cloud.databasecenter_v1beta.types.MaintenanceState):
            Output only. Resource maintenance state. This
            is to capture the current state of the
            maintenance.
        possible_failure_reasons (MutableSequence[google.cloud.databasecenter_v1beta.types.PossibleFailureReason]):
            Output only. List of possible reasons why the
            maintenance is not completed. This is an
            optional field and is only populated if there
            are any reasons for failures recorded for the
            maintenance by DB Center. FAILURE maintenance
            status may not always have a failure reason.
        previous_maintenance_version (str):
            Output only. Previous maintenance version of the database
            resource. Example: "MYSQL_8_0_41.R20250531.01_15". This is
            available once a minor version maintenance is complete on a
            database resource.
    """

    maintenance_schedule: "ResourceMaintenanceSchedule" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="ResourceMaintenanceSchedule",
    )
    deny_maintenance_schedules: MutableSequence["ResourceMaintenanceDenySchedule"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=2,
            message="ResourceMaintenanceDenySchedule",
        )
    )
    maintenance_version: str = proto.Field(
        proto.STRING,
        number=3,
    )
    current_version_release_date: date_pb2.Date = proto.Field(
        proto.MESSAGE,
        number=4,
        message=date_pb2.Date,
    )
    upcoming_maintenance: "UpcomingMaintenance" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="UpcomingMaintenance",
    )
    state: "MaintenanceState" = proto.Field(
        proto.ENUM,
        number=6,
        enum="MaintenanceState",
    )
    possible_failure_reasons: MutableSequence["PossibleFailureReason"] = (
        proto.RepeatedField(
            proto.ENUM,
            number=7,
            enum="PossibleFailureReason",
        )
    )
    previous_maintenance_version: str = proto.Field(
        proto.STRING,
        number=8,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
