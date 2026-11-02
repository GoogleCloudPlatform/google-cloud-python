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
import proto  # type: ignore

from google.cloud.storage_transfer_v1.types import transfer_types

__protobuf__ = proto.module(
    package="google.storagetransfer.v1",
    manifest={
        "GetGoogleServiceAccountRequest",
        "CreateTransferJobRequest",
        "UpdateTransferJobRequest",
        "GetTransferJobRequest",
        "DeleteTransferJobRequest",
        "ListTransferJobsRequest",
        "ListTransferJobsResponse",
        "PauseTransferOperationRequest",
        "ResumeTransferOperationRequest",
        "RunTransferJobRequest",
        "CreateAgentPoolRequest",
        "UpdateAgentPoolRequest",
        "GetAgentPoolRequest",
        "DeleteAgentPoolRequest",
        "ListAgentPoolsRequest",
        "ListAgentPoolsResponse",
    },
)


class GetGoogleServiceAccountRequest(proto.Message):
    r"""Request passed to GetGoogleServiceAccount.

    Attributes:
        project_id (str):
            Required. The ID of the Google Cloud project
            that the Google service account is associated
            with.
    """

    project_id: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateTransferJobRequest(proto.Message):
    r"""Request passed to CreateTransferJob.

    Attributes:
        transfer_job (google.cloud.storage_transfer_v1.types.TransferJob):
            Required. The job to create.
    """

    transfer_job: transfer_types.TransferJob = proto.Field(
        proto.MESSAGE,
        number=1,
        message=transfer_types.TransferJob,
    )


class UpdateTransferJobRequest(proto.Message):
    r"""Request passed to UpdateTransferJob.

    Attributes:
        job_name (str):
            Required. The name of job to update.
        project_id (str):
            Required. The ID of the Google Cloud project
            that owns the job.
        transfer_job (google.cloud.storage_transfer_v1.types.TransferJob):
            Required. The job to update. ``transferJob`` is expected to
            specify one or more of five fields:
            [description][google.storagetransfer.v1.TransferJob.description],
            [transfer_spec][google.storagetransfer.v1.TransferJob.transfer_spec],
            [notification_config][google.storagetransfer.v1.TransferJob.notification_config],
            [logging_config][google.storagetransfer.v1.TransferJob.logging_config],
            and [status][google.storagetransfer.v1.TransferJob.status].
            An ``UpdateTransferJobRequest`` that specifies other fields
            are rejected with the error
            [INVALID_ARGUMENT][google.rpc.Code.INVALID_ARGUMENT].
            Updating a job status to
            [DELETED][google.storagetransfer.v1.TransferJob.Status.DELETED]
            requires ``storagetransfer.jobs.delete`` permission.
        update_transfer_job_field_mask (google.protobuf.field_mask_pb2.FieldMask):
            The field mask of the fields in ``transferJob`` that are to
            be updated in this request. Fields in ``transferJob`` that
            can be updated are:
            [description][google.storagetransfer.v1.TransferJob.description],
            [transfer_spec][google.storagetransfer.v1.TransferJob.transfer_spec],
            [notification_config][google.storagetransfer.v1.TransferJob.notification_config],
            [logging_config][google.storagetransfer.v1.TransferJob.logging_config],
            and [status][google.storagetransfer.v1.TransferJob.status].
            To update the ``transfer_spec`` of the job, a complete
            transfer specification must be provided. An incomplete
            specification missing any required fields is rejected with
            the error
            [INVALID_ARGUMENT][google.rpc.Code.INVALID_ARGUMENT].
    """

    job_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    project_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    transfer_job: transfer_types.TransferJob = proto.Field(
        proto.MESSAGE,
        number=3,
        message=transfer_types.TransferJob,
    )
    update_transfer_job_field_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=4,
        message=field_mask_pb2.FieldMask,
    )


class GetTransferJobRequest(proto.Message):
    r"""Request passed to GetTransferJob.

    Attributes:
        job_name (str):
            Required. The job to get.
        project_id (str):
            Required. The ID of the Google Cloud project
            that owns the job.
    """

    job_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    project_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class DeleteTransferJobRequest(proto.Message):
    r"""Request passed to DeleteTransferJob.

    Attributes:
        job_name (str):
            Required. The job to delete.
        project_id (str):
            Required. The ID of the Google Cloud project
            that owns the job.
    """

    job_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    project_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ListTransferJobsRequest(proto.Message):
    r"""``projectId``, ``jobNames``, and ``jobStatuses`` are query
    parameters that can be specified when listing transfer jobs.

    Attributes:
        filter (str):
            Required. A list of query parameters specified as JSON text
            in the form of:

            ::

               {
                 "projectId":"my_project_id",
                 "jobNames":["jobid1","jobid2",...],
                 "jobStatuses":["status1","status2",...],
                 "dataBackend":"QUERY_REPLICATION_CONFIGS",
                 "sourceBucket":"source-bucket-name",
                 "sinkBucket":"sink-bucket-name",
               }

            The JSON formatting in the example is for display only;
            provide the query parameters without spaces or line breaks.

            - ``projectId`` is required.
            - Since ``jobNames`` and ``jobStatuses`` support multiple
              values, their values must be specified with array
              notation. ``jobNames`` and ``jobStatuses`` are optional.
              Valid values are case-insensitive:

              - [ENABLED][google.storagetransfer.v1.TransferJob.Status.ENABLED]
              - [DISABLED][google.storagetransfer.v1.TransferJob.Status.DISABLED]
              - [DELETED][google.storagetransfer.v1.TransferJob.Status.DELETED]

            - Specify ``"dataBackend":"QUERY_REPLICATION_CONFIGS"`` to
              return a list of cross-bucket replication jobs.
            - Limit the results to jobs from a particular bucket with
              ``sourceBucket`` and/or to a particular bucket with
              ``sinkBucket``.
        page_size (int):
            The list page size. The max allowed value is
            256.
        page_token (str):
            The list page token.
    """

    filter: str = proto.Field(
        proto.STRING,
        number=1,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=4,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=5,
    )


class ListTransferJobsResponse(proto.Message):
    r"""Response from ListTransferJobs.

    Attributes:
        transfer_jobs (MutableSequence[google.cloud.storage_transfer_v1.types.TransferJob]):
            A list of transfer jobs.
        next_page_token (str):
            The list next page token.
    """

    @property
    def raw_page(self):
        return self

    transfer_jobs: MutableSequence[transfer_types.TransferJob] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=transfer_types.TransferJob,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class PauseTransferOperationRequest(proto.Message):
    r"""Request passed to PauseTransferOperation.

    Attributes:
        name (str):
            Required. The name of the transfer operation.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ResumeTransferOperationRequest(proto.Message):
    r"""Request passed to ResumeTransferOperation.

    Attributes:
        name (str):
            Required. The name of the transfer operation.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class RunTransferJobRequest(proto.Message):
    r"""Request passed to RunTransferJob.

    Attributes:
        job_name (str):
            Required. The name of the transfer job.
        project_id (str):
            Required. The ID of the Google Cloud project
            that owns the transfer job.
    """

    job_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    project_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class CreateAgentPoolRequest(proto.Message):
    r"""Specifies the request passed to CreateAgentPool.

    Attributes:
        project_id (str):
            Required. The ID of the Google Cloud project
            that owns the agent pool.
        agent_pool (google.cloud.storage_transfer_v1.types.AgentPool):
            Required. The agent pool to create.
        agent_pool_id (str):
            Required. The ID of the agent pool to create.

            The ``agent_pool_id`` must meet the following requirements:

            - Length of 128 characters or less.
            - Not start with the string ``goog``.
            - Start with a lowercase ASCII character, followed by:

              - Zero or more: lowercase Latin alphabet characters,
                numerals, hyphens (``-``), periods (``.``), underscores
                (``_``), or tildes (``~``).
              - One or more numerals or lowercase ASCII characters.

            As expressed by the regular expression:
            ``^(?!goog)[a-z]([a-z0-9-._~]*[a-z0-9])?$``.
    """

    project_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    agent_pool: transfer_types.AgentPool = proto.Field(
        proto.MESSAGE,
        number=2,
        message=transfer_types.AgentPool,
    )
    agent_pool_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class UpdateAgentPoolRequest(proto.Message):
    r"""Specifies the request passed to UpdateAgentPool.

    Attributes:
        agent_pool (google.cloud.storage_transfer_v1.types.AgentPool):
            Required. The agent pool to update. ``agent_pool`` is
            expected to specify following fields:

            - [name][google.storagetransfer.v1.AgentPool.name]

            - [display_name][google.storagetransfer.v1.AgentPool.display_name]

            - [bandwidth_limit][google.storagetransfer.v1.AgentPool.bandwidth_limit]
              An ``UpdateAgentPoolRequest`` with any other fields is
              rejected with the error
              [INVALID_ARGUMENT][google.rpc.Code.INVALID_ARGUMENT].
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            The [field mask]
            (https://developers.google.com/protocol-buffers/docs/reference/google.protobuf)
            of the fields in ``agentPool`` to update in this request.
            The following ``agentPool`` fields can be updated:

            - [display_name][google.storagetransfer.v1.AgentPool.display_name]

            - [bandwidth_limit][google.storagetransfer.v1.AgentPool.bandwidth_limit]
    """

    agent_pool: transfer_types.AgentPool = proto.Field(
        proto.MESSAGE,
        number=1,
        message=transfer_types.AgentPool,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class GetAgentPoolRequest(proto.Message):
    r"""Specifies the request passed to GetAgentPool.

    Attributes:
        name (str):
            Required. The name of the agent pool to get.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class DeleteAgentPoolRequest(proto.Message):
    r"""Specifies the request passed to DeleteAgentPool.

    Attributes:
        name (str):
            Required. The name of the agent pool to
            delete.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListAgentPoolsRequest(proto.Message):
    r"""The request passed to ListAgentPools.

    Attributes:
        project_id (str):
            Required. The ID of the Google Cloud project
            that owns the job.
        filter (str):
            An optional list of query parameters specified as JSON text
            in the form of:

            ``{"agentPoolNames":["agentpool1","agentpool2",...]}``

            Since ``agentPoolNames`` support multiple values, its values
            must be specified with array notation. When the filter is
            either empty or not provided, the list returns all agent
            pools for the project.
        page_size (int):
            The list page size. The max allowed value is ``256``.
        page_token (str):
            The list page token.
    """

    project_id: str = proto.Field(
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


class ListAgentPoolsResponse(proto.Message):
    r"""Response from ListAgentPools.

    Attributes:
        agent_pools (MutableSequence[google.cloud.storage_transfer_v1.types.AgentPool]):
            A list of agent pools.
        next_page_token (str):
            The list next page token.
    """

    @property
    def raw_page(self):
        return self

    agent_pools: MutableSequence[transfer_types.AgentPool] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=transfer_types.AgentPool,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
