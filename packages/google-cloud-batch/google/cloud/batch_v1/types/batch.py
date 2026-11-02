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

from google.cloud.batch_v1.types import job as gcb_job
from google.cloud.batch_v1.types import task

__protobuf__ = proto.module(
    package="google.cloud.batch.v1",
    manifest={
        "CreateJobRequest",
        "GetJobRequest",
        "DeleteJobRequest",
        "CancelJobRequest",
        "CancelJobResponse",
        "ListJobsRequest",
        "ListJobsResponse",
        "ListTasksRequest",
        "ListTasksResponse",
        "GetTaskRequest",
        "OperationMetadata",
    },
)


class CreateJobRequest(proto.Message):
    r"""CreateJob Request.

    Attributes:
        parent (str):
            Required. The parent resource name where the
            Job will be created. Pattern:
            "projects/{project}/locations/{location}".
        job_id (str):
            ID used to uniquely identify the Job within its parent
            scope. This field should contain at most 63 characters and
            must start with lowercase characters. Only lowercase
            characters, numbers and '-' are accepted. The '-' character
            cannot be the first or the last one. A system generated ID
            will be used if the field is not set.

            The job.name field in the request will be ignored and the
            created resource name of the Job will be
            "{parent}/jobs/{job_id}".
        job (google.cloud.batch_v1.types.Job):
            Required. The Job to create.
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server will
            know to ignore the request if it has already
            been completed. The server will guarantee that
            for at least 60 minutes since the first request.

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

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    job_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    job: gcb_job.Job = proto.Field(
        proto.MESSAGE,
        number=3,
        message=gcb_job.Job,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class GetJobRequest(proto.Message):
    r"""GetJob Request.

    Attributes:
        name (str):
            Required. Job name.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class DeleteJobRequest(proto.Message):
    r"""DeleteJob Request.

    Attributes:
        name (str):
            Job name.
        reason (str):
            Optional. Reason for this deletion.
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
    reason: str = proto.Field(
        proto.STRING,
        number=2,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class CancelJobRequest(proto.Message):
    r"""CancelJob Request.

    Attributes:
        name (str):
            Required. Job name.
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
        number=4,
    )


class CancelJobResponse(proto.Message):
    r"""Response to the CancelJob request."""


class ListJobsRequest(proto.Message):
    r"""ListJob Request.

    Attributes:
        parent (str):
            Parent path.
        filter (str):
            List filter.
        order_by (str):
            Optional. Sort results. Supported are "name", "name desc",
            "create_time", and "create_time desc".
        page_size (int):
            Page size.
        page_token (str):
            Page token.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=4,
    )
    order_by: str = proto.Field(
        proto.STRING,
        number=5,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=2,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ListJobsResponse(proto.Message):
    r"""ListJob Response.

    Attributes:
        jobs (MutableSequence[google.cloud.batch_v1.types.Job]):
            Jobs.
        next_page_token (str):
            Next page token.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    jobs: MutableSequence[gcb_job.Job] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=gcb_job.Job,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class ListTasksRequest(proto.Message):
    r"""ListTasks Request.

    Attributes:
        parent (str):
            Required. Name of a TaskGroup from which Tasks are being
            requested. Pattern:
            "projects/{project}/locations/{location}/jobs/{job}/taskGroups/{task_group}".
        filter (str):
            Task filter, null filter matches all Tasks.
            Filter string should be of the format
            State=TaskStatus.State e.g. State=RUNNING
        page_size (int):
            Page size.
        page_token (str):
            Page token.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=2,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=3,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=4,
    )


class ListTasksResponse(proto.Message):
    r"""ListTasks Response.

    Attributes:
        tasks (MutableSequence[google.cloud.batch_v1.types.Task]):
            Tasks.
        next_page_token (str):
            Next page token.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    tasks: MutableSequence[task.Task] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=task.Task,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetTaskRequest(proto.Message):
    r"""Request for a single Task by name.

    Attributes:
        name (str):
            Required. Task name.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class OperationMetadata(proto.Message):
    r"""Represents the metadata of the long-running operation.

    Attributes:
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the operation was
            created.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the operation finished
            running.
        target (str):
            Output only. Server-defined resource path for
            the target of the operation.
        verb (str):
            Output only. Name of the verb executed by the
            operation.
        status_message (str):
            Output only. Human-readable status of the
            operation, if any.
        requested_cancellation (bool):
            Output only. Identifies whether the user has requested
            cancellation of the operation. Operations that have
            successfully been cancelled have
            [google.longrunning.Operation.error][google.longrunning.Operation.error]
            value with a
            [google.rpc.Status.code][google.rpc.Status.code] of 1,
            corresponding to ``Code.CANCELLED``.
        api_version (str):
            Output only. API version used to start the
            operation.
    """

    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )
    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    target: str = proto.Field(
        proto.STRING,
        number=3,
    )
    verb: str = proto.Field(
        proto.STRING,
        number=4,
    )
    status_message: str = proto.Field(
        proto.STRING,
        number=5,
    )
    requested_cancellation: bool = proto.Field(
        proto.BOOL,
        number=6,
    )
    api_version: str = proto.Field(
        proto.STRING,
        number=7,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
