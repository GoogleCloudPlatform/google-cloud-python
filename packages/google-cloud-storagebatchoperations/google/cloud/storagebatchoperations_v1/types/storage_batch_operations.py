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

from google.cloud.storagebatchoperations_v1.types import storage_batch_operations_types

__protobuf__ = proto.module(
    package="google.cloud.storagebatchoperations.v1",
    manifest={
        "ListJobsRequest",
        "ListJobsResponse",
        "GetJobRequest",
        "CreateJobRequest",
        "CancelJobRequest",
        "DeleteJobRequest",
        "CancelJobResponse",
        "ListBucketOperationsRequest",
        "ListBucketOperationsResponse",
        "GetBucketOperationRequest",
        "OperationMetadata",
    },
)


class ListJobsRequest(proto.Message):
    r"""Message for request to list Jobs

    Attributes:
        parent (str):
            Required. Format: projects/{project_id}/locations/global.
        filter (str):
            Optional. Filters results as defined by
            https://google.aip.dev/160.
        page_size (int):
            Optional. The list page size. default page
            size is 100.
        page_token (str):
            Optional. The list page token.
        order_by (str):
            Optional. Field to sort by. Supported fields are name,
            create_time.
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
    order_by: str = proto.Field(
        proto.STRING,
        number=5,
    )


class ListJobsResponse(proto.Message):
    r"""Message for response to listing Jobs

    Attributes:
        jobs (MutableSequence[google.cloud.storagebatchoperations_v1.types.Job]):
            A list of storage batch jobs.
        next_page_token (str):
            A token identifying a page of results.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    jobs: MutableSequence[storage_batch_operations_types.Job] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=storage_batch_operations_types.Job,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetJobRequest(proto.Message):
    r"""Message for getting a Job

    Attributes:
        name (str):
            Required. ``name`` of the job to retrieve. Format:
            projects/{project_id}/locations/global/jobs/{job_id} .
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateJobRequest(proto.Message):
    r"""Message for creating a Job

    Attributes:
        parent (str):
            Required. Value for parent.
        job_id (str):
            Required. The optional ``job_id`` for this Job . If not
            specified, an id is generated. ``job_id`` should be no more
            than 128 characters and must include only characters
            available in DNS names, as defined by RFC-1123.
        job (google.cloud.storagebatchoperations_v1.types.Job):
            Required. The resource being created
        request_id (str):
            Optional. An optional request ID to identify requests.
            Specify a unique request ID in case you need to retry your
            request. Requests with same ``request_id`` will be ignored
            for at least 60 minutes since the first request. The request
            ID must be a valid UUID with the exception that zero UUID is
            not supported (00000000-0000-0000-0000-000000000000).
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    job_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    job: storage_batch_operations_types.Job = proto.Field(
        proto.MESSAGE,
        number=3,
        message=storage_batch_operations_types.Job,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class CancelJobRequest(proto.Message):
    r"""Message for Job to Cancel

    Attributes:
        name (str):
            Required. The ``name`` of the job to cancel. Format:
            projects/{project_id}/locations/global/jobs/{job_id}.
        request_id (str):
            Optional. An optional request ID to identify requests.
            Specify a unique request ID in case you need to retry your
            request. Requests with same ``request_id`` will be ignored
            for at least 60 minutes since the first request. The request
            ID must be a valid UUID with the exception that zero UUID is
            not supported (00000000-0000-0000-0000-000000000000).
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class DeleteJobRequest(proto.Message):
    r"""Message for deleting a Job

    Attributes:
        name (str):
            Required. The ``name`` of the job to delete. Format:
            projects/{project_id}/locations/global/jobs/{job_id} .
        request_id (str):
            Optional. An optional request ID to identify requests.
            Specify a unique request ID in case you need to retry your
            request. Requests with same ``request_id`` will be ignored
            for at least 60 minutes since the first request. The request
            ID must be a valid UUID with the exception that zero UUID is
            not supported (00000000-0000-0000-0000-000000000000).
        force (bool):
            Optional. If set to true, any child bucket
            operations of the job will also be deleted.
            Highly recommended to be set to true by all
            clients. Users cannot mutate bucket operations
            directly, so only the jobs.delete permission is
            required to delete a job (and its child bucket
            operations).
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    force: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


class CancelJobResponse(proto.Message):
    r"""Message for response to cancel Job."""


class ListBucketOperationsRequest(proto.Message):
    r"""Message for request to list BucketOperations

    Attributes:
        parent (str):
            Required. Format:
            projects/{project_id}/locations/global/jobs/{job_id}.
        filter (str):
            Optional. Filters results as defined by
            https://google.aip.dev/160.
        page_size (int):
            Optional. The list page size. Default page
            size is 100.
        page_token (str):
            Optional. The list page token.
        order_by (str):
            Optional. Field to sort by. Supported fields are name,
            create_time.
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
    order_by: str = proto.Field(
        proto.STRING,
        number=5,
    )


class ListBucketOperationsResponse(proto.Message):
    r"""Message for response to listing BucketOperations

    Attributes:
        bucket_operations (MutableSequence[google.cloud.storagebatchoperations_v1.types.BucketOperation]):
            A list of storage batch bucket operations.
        next_page_token (str):
            A token identifying a page of results.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    bucket_operations: MutableSequence[
        storage_batch_operations_types.BucketOperation
    ] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=storage_batch_operations_types.BucketOperation,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetBucketOperationRequest(proto.Message):
    r"""Message for getting a BucketOperation.

    Attributes:
        name (str):
            Required. ``name`` of the bucket operation to retrieve.
            Format:
            projects/{project_id}/locations/global/jobs/{job_id}/bucketOperations/{bucket_operation_id}.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class OperationMetadata(proto.Message):
    r"""Represents the metadata of the long-running operation.

    Attributes:
        operation (str):
            Output only. The unique operation resource
            name. Format:
            projects/{project}/locations/global/operations/{operation}.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the operation was
            created.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the operation finished
            running.
        requested_cancellation (bool):
            Output only. Identifies whether the user has requested
            cancellation of the operation. Operations that have been
            cancelled successfully have
            [google.longrunning.Operation.error][google.longrunning.Operation.error]
            value with a
            [google.rpc.Status.code][google.rpc.Status.code] of 1,
            corresponding to
            ``[Code.CANCELLED][google.rpc.Code.CANCELLED]``.
        api_version (str):
            Output only. API version used to start the
            operation.
        job (google.cloud.storagebatchoperations_v1.types.Job):
            Output only. The Job associated with the
            operation.
    """

    operation: str = proto.Field(
        proto.STRING,
        number=1,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    requested_cancellation: bool = proto.Field(
        proto.BOOL,
        number=7,
    )
    api_version: str = proto.Field(
        proto.STRING,
        number=8,
    )
    job: storage_batch_operations_types.Job = proto.Field(
        proto.MESSAGE,
        number=10,
        message=storage_batch_operations_types.Job,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
