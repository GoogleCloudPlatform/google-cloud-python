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

from google.cloud.sqladmin_v1.types import cloud_sql_resources

__protobuf__ = proto.module(
    package="google.cloud.sql.v1",
    manifest={
        "WorkloadCapturesStartRequest",
        "WorkloadCapturesStopRequest",
        "WorkloadCapturesStartReplayRequest",
        "WorkloadCapturesStopReplayRequest",
        "SqlWorkloadCapturesListRequest",
        "WorkloadCapturesListResponse",
        "WorkloadCapture",
    },
)


class WorkloadCapturesStartRequest(proto.Message):
    r"""Request to start recording traffic from the primary instance
    (captured workload).

    Attributes:
        project (str):
            Required. Project ID of the project that
            contains the instance.
        instance (str):
            Required. Cloud SQL instance ID. This does
            not include the project ID.
        start_workload_capture_context (google.cloud.sqladmin_v1.types.StartWorkloadCaptureContext):
            Optional. Contains details about the start
            workload capture operation.
    """

    project: str = proto.Field(
        proto.STRING,
        number=1,
    )
    instance: str = proto.Field(
        proto.STRING,
        number=2,
    )
    start_workload_capture_context: cloud_sql_resources.StartWorkloadCaptureContext = (
        proto.Field(
            proto.MESSAGE,
            number=100,
            message=cloud_sql_resources.StartWorkloadCaptureContext,
        )
    )


class WorkloadCapturesStopRequest(proto.Message):
    r"""Request to stop recording traffic from the primary instance.

    Attributes:
        project (str):
            Required. Project ID of the project that
            contains the instance.
        instance (str):
            Required. Cloud SQL instance ID. This does
            not include the project ID.
        stop_workload_capture_context (google.cloud.sqladmin_v1.types.StopWorkloadCaptureContext):
            Optional. Contains details about the stop
            workload capture operation.
    """

    project: str = proto.Field(
        proto.STRING,
        number=1,
    )
    instance: str = proto.Field(
        proto.STRING,
        number=2,
    )
    stop_workload_capture_context: cloud_sql_resources.StopWorkloadCaptureContext = (
        proto.Field(
            proto.MESSAGE,
            number=100,
            message=cloud_sql_resources.StopWorkloadCaptureContext,
        )
    )


class WorkloadCapturesStartReplayRequest(proto.Message):
    r"""Request to start executing a captured workload on a replay
    instance (the Cloud SQL instance where the recorded SQL queries
    are executed).

    Attributes:
        project (str):
            Required. Project ID of the project that
            contains the instance.
        instance (str):
            Required. Cloud SQL instance ID. This does
            not include the project ID.
        start_workload_replay_context (google.cloud.sqladmin_v1.types.StartWorkloadReplayContext):
            Required. Contains details about the start
            workload replay operation.
        workload_id (str):
            Required. The ID of the workload to replay.
    """

    project: str = proto.Field(
        proto.STRING,
        number=1,
    )
    instance: str = proto.Field(
        proto.STRING,
        number=2,
    )
    start_workload_replay_context: cloud_sql_resources.StartWorkloadReplayContext = (
        proto.Field(
            proto.MESSAGE,
            number=100,
            message=cloud_sql_resources.StartWorkloadReplayContext,
        )
    )
    workload_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class WorkloadCapturesStopReplayRequest(proto.Message):
    r"""Request to stop an active workload replay on a target Cloud
    SQL replay instance.

    Attributes:
        project (str):
            Required. Project ID of the project that
            contains the target replay instance.
        instance (str):
            Required. Cloud SQL instance ID of the target
            replay instance. This does not include the
            project ID.
        stop_workload_replay_context (google.cloud.sqladmin_v1.types.StopWorkloadReplayContext):
            Optional. Contains details about the stop
            workload replay operation. If omitted, default
            values are used.
    """

    project: str = proto.Field(
        proto.STRING,
        number=1,
    )
    instance: str = proto.Field(
        proto.STRING,
        number=2,
    )
    stop_workload_replay_context: cloud_sql_resources.StopWorkloadReplayContext = (
        proto.Field(
            proto.MESSAGE,
            number=100,
            message=cloud_sql_resources.StopWorkloadReplayContext,
        )
    )


class SqlWorkloadCapturesListRequest(proto.Message):
    r"""Instance list captured workloads request.

    Attributes:
        project (str):
            Required. Project ID of the project that
            contains the instance.
        instance (str):
            Required. Cloud SQL instance ID. This does
            not include the project ID.
    """

    project: str = proto.Field(
        proto.STRING,
        number=1,
    )
    instance: str = proto.Field(
        proto.STRING,
        number=2,
    )


class WorkloadCapturesListResponse(proto.Message):
    r"""Instance list captured workloads response.

    Attributes:
        workload_captures (MutableSequence[google.cloud.sqladmin_v1.types.WorkloadCapture]):
            List of captured workloads for the instance.
        kind (str):
            This is always ``sql#workloadCapturesList``.
    """

    workload_captures: MutableSequence["WorkloadCapture"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="WorkloadCapture",
    )
    kind: str = proto.Field(
        proto.STRING,
        number=2,
    )


class WorkloadCapture(proto.Message):
    r"""Captured workload for an instance.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        workload_id (str):
            Output only. The ID of the captured workload.
        source_instance (str):
            Output only. The name of the source instance.
        workload_capture_state (google.cloud.sqladmin_v1.types.WorkloadCapture.State):
            Output only. The state of the workload
            capture.
        start_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The start time of the workload
            capture.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The end time of the workload
            capture.
        replay_instance (str):
            Output only. The name of the replay instance,
            if live replay was enabled.

            This field is a member of `oneof`_ ``_replay_instance``.
        retention_days (int):
            Output only. The retention period in days for
            the captured workload.

            This field is a member of `oneof`_ ``_retention_days``.
        backup_id (str):
            Output only. The base backup ID associated
            with the workload capture.

            This field is a member of `oneof`_ ``_backup_id``.
    """

    class State(proto.Enum):
        r"""State of the workload capture.

        Values:
            STATE_UNSPECIFIED (0):
                Default value. This value is unused.
            RUNNING (1):
                Workload capture is currently running.
            COMPLETED (2):
                Workload capture completed successfully. This
                state is set when the user explicitly stops the
                capture.
            FAILED (3):
                Workload capture failed.
            TERMINATED (4):
                Workload capture was terminated
                automatically. This state is set when Cloud SQL
                automatically stops the capture due to a
                conflicting operation or when the maximum
                duration is reached.
        """

        STATE_UNSPECIFIED = 0
        RUNNING = 1
        COMPLETED = 2
        FAILED = 3
        TERMINATED = 4

    workload_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    source_instance: str = proto.Field(
        proto.STRING,
        number=2,
    )
    workload_capture_state: State = proto.Field(
        proto.ENUM,
        number=3,
        enum=State,
    )
    start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    replay_instance: str = proto.Field(
        proto.STRING,
        number=6,
        optional=True,
    )
    retention_days: int = proto.Field(
        proto.INT32,
        number=7,
        optional=True,
    )
    backup_id: str = proto.Field(
        proto.STRING,
        number=8,
        optional=True,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
