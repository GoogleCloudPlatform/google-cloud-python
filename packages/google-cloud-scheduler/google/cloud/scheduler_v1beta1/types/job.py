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
import google.rpc.status_pb2 as status_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.scheduler_v1beta1.types import target

__protobuf__ = proto.module(
    package="google.cloud.scheduler.v1beta1",
    manifest={
        "Job",
        "RetryConfig",
    },
)


class Job(proto.Message):
    r"""Configuration for a job.
    The maximum allowed size for a job is 1MB.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Optionally caller-specified in
            [CreateJob][google.cloud.scheduler.v1beta1.CloudScheduler.CreateJob],
            after which it becomes output only.

            The job name. For example:
            ``projects/PROJECT_ID/locations/LOCATION_ID/jobs/JOB_ID``.

            - ``PROJECT_ID`` can contain letters ([A-Za-z]), numbers
              ([0-9]), hyphens (-), colons (:), or periods (.). For more
              information, see `Identifying
              projects <https://cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects>`__
            - ``LOCATION_ID`` is the canonical ID for the job's
              location. The list of available locations can be obtained
              by calling
              [ListLocations][google.cloud.location.Locations.ListLocations].
              For more information, see
              https://cloud.google.com/about/locations/.
            - ``JOB_ID`` can contain only letters ([A-Za-z]), numbers
              ([0-9]), hyphens (-), or underscores (\_). The maximum
              length is 500 characters.
        description (str):
            Optionally caller-specified in
            [CreateJob][google.cloud.scheduler.v1beta1.CloudScheduler.CreateJob]
            or
            [UpdateJob][google.cloud.scheduler.v1beta1.CloudScheduler.UpdateJob].

            A human-readable description for the job. This string must
            not contain more than 500 characters.
        pubsub_target (google.cloud.scheduler_v1beta1.types.PubsubTarget):
            Pub/Sub target.

            This field is a member of `oneof`_ ``target``.
        app_engine_http_target (google.cloud.scheduler_v1beta1.types.AppEngineHttpTarget):
            App Engine HTTP target.

            This field is a member of `oneof`_ ``target``.
        http_target (google.cloud.scheduler_v1beta1.types.HttpTarget):
            HTTP target.

            This field is a member of `oneof`_ ``target``.
        schedule (str):
            Required, except when used with
            [UpdateJob][google.cloud.scheduler.v1beta1.CloudScheduler.UpdateJob].

            Describes the schedule on which the job will be executed.

            The schedule can be either of the following types:

            - `Crontab <https://en.wikipedia.org/wiki/Cron#Overview>`__
            - English-like
              `schedule <https://cloud.google.com/scheduler/docs/configuring/cron-job-schedules>`__

            As a general rule, execution ``n + 1`` of a job will not
            begin until execution ``n`` has finished. Cloud Scheduler
            will never allow two simultaneously outstanding executions.
            For example, this implies that if the ``n+1``\ th execution
            is scheduled to run at 16:00 but the ``n``\ th execution
            takes until 16:15, the ``n+1``\ th execution will not start
            until ``16:15``. A scheduled start time will be delayed if
            the previous execution has not ended when its scheduled time
            occurs.

            If
            [retry_count][google.cloud.scheduler.v1beta1.RetryConfig.retry_count]
            > 0 and a job attempt fails, the job will be tried a total
            of
            [retry_count][google.cloud.scheduler.v1beta1.RetryConfig.retry_count]
            times, with exponential backoff, until the next scheduled
            start time.
        time_zone (str):
            Specifies the time zone to be used in interpreting
            [schedule][google.cloud.scheduler.v1beta1.Job.schedule]. The
            value of this field must be a time zone name from the `tz
            database <http://en.wikipedia.org/wiki/Tz_database>`__.

            Note that some time zones include a provision for daylight
            savings time. The rules for daylight saving time are
            determined by the chosen tz. For UTC use the string "utc".
            If a time zone is not specified, the default will be in UTC
            (also known as GMT).
        user_update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The creation time of the job.
        state (google.cloud.scheduler_v1beta1.types.Job.State):
            Output only. State of the job.
        status (google.rpc.status_pb2.Status):
            Output only. The response from the target for
            the last attempted execution.
        schedule_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The next time the job is
            scheduled. Note that this may be a retry of a
            previously failed attempt or the next execution
            time according to the schedule.
        last_attempt_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the last job attempt
            started.
        retry_config (google.cloud.scheduler_v1beta1.types.RetryConfig):
            Settings that determine the retry behavior.
        attempt_deadline (google.protobuf.duration_pb2.Duration):
            The deadline for job attempts. If the request handler does
            not respond by this deadline then the request is cancelled
            and the attempt is marked as a ``DEADLINE_EXCEEDED``
            failure. The failed attempt can be viewed in execution logs.
            Cloud Scheduler will retry the job according to the
            [RetryConfig][google.cloud.scheduler.v1beta1.RetryConfig].

            The default and the allowed values depend on the type of
            target:

            - For [HTTP
              targets][google.cloud.scheduler.v1beta1.Job.http_target],
              the default is 3 minutes. The deadline must be in the
              interval [15 seconds, 30 minutes].

            - For [App Engine HTTP
              targets][google.cloud.scheduler.v1beta1.Job.app_engine_http_target],
              0 indicates that the request has the default deadline. The
              default deadline depends on the scaling type of the
              service: 10 minutes for standard apps with automatic
              scaling, 24 hours for standard apps with manual and basic
              scaling, and 60 minutes for flex apps. If the request
              deadline is set, it must be in the interval [15 seconds,
              24 hours 15 seconds].

            - For [Pub/Sub
              targets][google.cloud.scheduler.v1beta1.Job.pubsub_target],
              this field is ignored.
        legacy_app_engine_cron (bool):
            Immutable. This field is used to manage the
            legacy App Engine Cron jobs using the Cloud
            Scheduler API. If the field is set to true, the
            job will be considered a legacy job. Note that
            App Engine Cron jobs have fewer features than
            Cloud Scheduler jobs, e.g., are only limited to
            App Engine targets.
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
                can intentionally pause the job using
                [PauseJobRequest][google.cloud.scheduler.v1beta1.PauseJobRequest].
            DISABLED (3):
                The job is disabled by the system due to
                error. The user cannot directly set a job to be
                disabled.
            UPDATE_FAILED (4):
                The job state resulting from a failed
                [CloudScheduler.UpdateJob][google.cloud.scheduler.v1beta1.CloudScheduler.UpdateJob]
                operation. To recover a job from this state, retry
                [CloudScheduler.UpdateJob][google.cloud.scheduler.v1beta1.CloudScheduler.UpdateJob]
                until a successful response is received.
        """

        STATE_UNSPECIFIED = 0
        ENABLED = 1
        PAUSED = 2
        DISABLED = 3
        UPDATE_FAILED = 4

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    description: str = proto.Field(
        proto.STRING,
        number=2,
    )
    pubsub_target: target.PubsubTarget = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="target",
        message=target.PubsubTarget,
    )
    app_engine_http_target: target.AppEngineHttpTarget = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="target",
        message=target.AppEngineHttpTarget,
    )
    http_target: target.HttpTarget = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="target",
        message=target.HttpTarget,
    )
    schedule: str = proto.Field(
        proto.STRING,
        number=20,
    )
    time_zone: str = proto.Field(
        proto.STRING,
        number=21,
    )
    user_update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=9,
        message=timestamp_pb2.Timestamp,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=10,
        enum=State,
    )
    status: status_pb2.Status = proto.Field(
        proto.MESSAGE,
        number=11,
        message=status_pb2.Status,
    )
    schedule_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=17,
        message=timestamp_pb2.Timestamp,
    )
    last_attempt_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=18,
        message=timestamp_pb2.Timestamp,
    )
    retry_config: "RetryConfig" = proto.Field(
        proto.MESSAGE,
        number=19,
        message="RetryConfig",
    )
    attempt_deadline: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=22,
        message=duration_pb2.Duration,
    )
    legacy_app_engine_cron: bool = proto.Field(
        proto.BOOL,
        number=23,
    )


class RetryConfig(proto.Message):
    r"""Settings that determine the retry behavior.

    By default, if a job does not complete successfully (meaning that an
    acknowledgement is not received from the handler, then it will be
    retried with exponential backoff according to the settings in
    [RetryConfig][google.cloud.scheduler.v1beta1.RetryConfig].

    Attributes:
        retry_count (int):
            The number of attempts that the system will make to run a
            job using the exponential backoff procedure described by
            [max_doublings][google.cloud.scheduler.v1beta1.RetryConfig.max_doublings].

            The default value of retry_count is zero.

            If retry_count is zero, a job attempt will *not* be retried
            if it fails. Instead the Cloud Scheduler system will wait
            for the next scheduled execution time.

            If retry_count is set to a non-zero number then Cloud
            Scheduler will retry failed attempts, using exponential
            backoff, retry_count times, or until the next scheduled
            execution time, whichever comes first.

            Values greater than 5 and negative values are not allowed.
        max_retry_duration (google.protobuf.duration_pb2.Duration):
            The time limit for retrying a failed job, measured from time
            when an execution was first attempted. If specified with
            [retry_count][google.cloud.scheduler.v1beta1.RetryConfig.retry_count],
            the job will be retried until both limits are reached.

            The default value for max_retry_duration is zero, which
            means retry duration is unlimited.
        min_backoff_duration (google.protobuf.duration_pb2.Duration):
            The minimum amount of time to wait before
            retrying a job after it fails.

            The default value of this field is 5 seconds.
        max_backoff_duration (google.protobuf.duration_pb2.Duration):
            The maximum amount of time to wait before
            retrying a job after it fails.

            The default value of this field is 1 hour.
        max_doublings (int):
            The time between retries will double ``max_doublings``
            times.

            A job's retry interval starts at
            [min_backoff_duration][google.cloud.scheduler.v1beta1.RetryConfig.min_backoff_duration],
            then doubles ``max_doublings`` times, then increases
            linearly, and finally retries at intervals of
            [max_backoff_duration][google.cloud.scheduler.v1beta1.RetryConfig.max_backoff_duration]
            up to
            [retry_count][google.cloud.scheduler.v1beta1.RetryConfig.retry_count]
            times.

            For example, if
            [min_backoff_duration][google.cloud.scheduler.v1beta1.RetryConfig.min_backoff_duration]
            is 10s,
            [max_backoff_duration][google.cloud.scheduler.v1beta1.RetryConfig.max_backoff_duration]
            is 300s, and ``max_doublings`` is 3, then the a job will
            first be retried in 10s. The retry interval will double
            three times, and then increase linearly by 2^3 \* 10s.
            Finally, the job will retry at intervals of
            [max_backoff_duration][google.cloud.scheduler.v1beta1.RetryConfig.max_backoff_duration]
            until the job has been attempted
            [retry_count][google.cloud.scheduler.v1beta1.RetryConfig.retry_count]
            times. Thus, the requests will retry at 10s, 20s, 40s, 80s,
            160s, 240s, 300s, 300s, ....

            The default value of this field is 5.
    """

    retry_count: int = proto.Field(
        proto.INT32,
        number=1,
    )
    max_retry_duration: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=2,
        message=duration_pb2.Duration,
    )
    min_backoff_duration: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=3,
        message=duration_pb2.Duration,
    )
    max_backoff_duration: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=4,
        message=duration_pb2.Duration,
    )
    max_doublings: int = proto.Field(
        proto.INT32,
        number=5,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
