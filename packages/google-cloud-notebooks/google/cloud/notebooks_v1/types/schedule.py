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

from google.cloud.notebooks_v1.types import execution

__protobuf__ = proto.module(
    package="google.cloud.notebooks.v1",
    manifest={
        "Schedule",
    },
)


class Schedule(proto.Message):
    r"""The definition of a schedule.

    Attributes:
        name (str):
            Output only. The name of this schedule. Format:
            ``projects/{project_id}/locations/{location}/schedules/{schedule_id}``
        display_name (str):
            Output only. Display name used for UI purposes. Name can
            only contain alphanumeric characters, hyphens ``-``, and
            underscores ``_``.
        description (str):
            A brief description of this environment.
        state (google.cloud.notebooks_v1.types.Schedule.State):

        cron_schedule (str):
            Cron-tab formatted schedule by which the job will execute.
            Format: minute, hour, day of month, month, day of week, e.g.
            ``0 0 * * WED`` = every Wednesday More examples:
            https://crontab.guru/examples.html
        time_zone (str):
            Timezone on which the cron_schedule. The value of this field
            must be a time zone name from the tz database. TZ Database:
            https://en.wikipedia.org/wiki/List_of_tz_database_time_zones

            Note that some time zones include a provision for daylight
            savings time. The rules for daylight saving time are
            determined by the chosen tz. For UTC use the string "utc".
            If a time zone is not specified, the default will be in UTC
            (also known as GMT).
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time the schedule was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time the schedule was last
            updated.
        execution_template (google.cloud.notebooks_v1.types.ExecutionTemplate):
            Notebook Execution Template corresponding to
            this schedule.
        recent_executions (MutableSequence[google.cloud.notebooks_v1.types.Execution]):
            Output only. The most recent execution names
            triggered from this schedule and their
            corresponding states.
    """

    class State(proto.Enum):
        r"""State of the job.

        Values:
            STATE_UNSPECIFIED (0):
                Unspecified state.
            ENABLED (1):
                The job is executing normally.
            PAUSED (2):
                The job is paused by the user. It will not execute. A user
                can intentionally pause the job using [PauseJobRequest][].
            DISABLED (3):
                The job is disabled by the system due to
                error. The user cannot directly set a job to be
                disabled.
            UPDATE_FAILED (4):
                The job state resulting from a failed
                [CloudScheduler.UpdateJob][] operation. To recover a job
                from this state, retry [CloudScheduler.UpdateJob][] until a
                successful response is received.
            INITIALIZING (5):
                The schedule resource is being created.
            DELETING (6):
                The schedule resource is being deleted.
        """

        STATE_UNSPECIFIED = 0
        ENABLED = 1
        PAUSED = 2
        DISABLED = 3
        UPDATE_FAILED = 4
        INITIALIZING = 5
        DELETING = 6

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    description: str = proto.Field(
        proto.STRING,
        number=3,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=4,
        enum=State,
    )
    cron_schedule: str = proto.Field(
        proto.STRING,
        number=5,
    )
    time_zone: str = proto.Field(
        proto.STRING,
        number=6,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=7,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=8,
        message=timestamp_pb2.Timestamp,
    )
    execution_template: execution.ExecutionTemplate = proto.Field(
        proto.MESSAGE,
        number=9,
        message=execution.ExecutionTemplate,
    )
    recent_executions: MutableSequence[execution.Execution] = proto.RepeatedField(
        proto.MESSAGE,
        number=10,
        message=execution.Execution,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
