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
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.workflows.v1beta",
    manifest={
        "Workflow",
        "ListWorkflowsRequest",
        "ListWorkflowsResponse",
        "GetWorkflowRequest",
        "CreateWorkflowRequest",
        "DeleteWorkflowRequest",
        "UpdateWorkflowRequest",
        "OperationMetadata",
    },
)


class Workflow(proto.Message):
    r"""Workflow program to be executed by Workflows.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            The resource name of the workflow.
            Format:
            projects/{project}/locations/{location}/workflows/{workflow}
        description (str):
            Description of the workflow provided by the
            user. Must be at most 1000 unicode characters
            long.
        state (google.cloud.workflows_v1beta.types.Workflow.State):
            Output only. State of the workflow
            deployment.
        revision_id (str):
            Output only. The revision of the workflow. A new revision of
            a workflow is created as a result of updating the following
            properties of a workflow:

            - [Service
              account][google.cloud.workflows.v1beta.Workflow.service_account]
            - [Workflow code to be
              executed][google.cloud.workflows.v1beta.Workflow.source_contents]

            The format is "000001-a4d", where the first 6 characters
            define the zero-padded revision ordinal number. They are
            followed by a hyphen and 3 hexadecimal random characters.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp of when the
            workflow was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The last update timestamp of the
            workflow.
        revision_create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp that the latest
            revision of the workflow was created.
        labels (MutableMapping[str, str]):
            Labels associated with this workflow.
            Labels can contain at most 64 entries. Keys and
            values can be no longer than 63 characters and
            can only contain lowercase letters, numeric
            characters, underscores and dashes. Label keys
            must start with a letter. International
            characters are allowed.
        service_account (str):
            The service account associated with the latest workflow
            version. This service account represents the identity of the
            workflow and determines what permissions the workflow has.
            Format: projects/{project}/serviceAccounts/{account} or
            {account}

            Using ``-`` as a wildcard for the ``{project}`` or not
            providing one at all will infer the project from the
            account. The ``{account}`` value can be the ``email``
            address or the ``unique_id`` of the service account.

            If not provided, workflow will use the project's default
            service account. Modifying this field for an existing
            workflow results in a new workflow revision.
        source_contents (str):
            Workflow code to be executed. The size limit
            is 128KB.

            This field is a member of `oneof`_ ``source_code``.
    """

    class State(proto.Enum):
        r"""Describes the current state of workflow deployment. More
        states may be added in the future.

        Values:
            STATE_UNSPECIFIED (0):
                Invalid state.
            ACTIVE (1):
                The workflow has been deployed successfully
                and is serving.
        """

        STATE_UNSPECIFIED = 0
        ACTIVE = 1

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    description: str = proto.Field(
        proto.STRING,
        number=2,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=3,
        enum=State,
    )
    revision_id: str = proto.Field(
        proto.STRING,
        number=4,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )
    revision_create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=7,
        message=timestamp_pb2.Timestamp,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=8,
    )
    service_account: str = proto.Field(
        proto.STRING,
        number=9,
    )
    source_contents: str = proto.Field(
        proto.STRING,
        number=10,
        oneof="source_code",
    )


class ListWorkflowsRequest(proto.Message):
    r"""Request for the
    [ListWorkflows][google.cloud.workflows.v1beta.Workflows.ListWorkflows]
    method.

    Attributes:
        parent (str):
            Required. Project and location from which the
            workflows should be listed. Format:
            projects/{project}/locations/{location}
        page_size (int):
            Maximum number of workflows to return per
            call. The service may return fewer than this
            value. If the value is not specified, a default
            value of 500 will be used. The maximum permitted
            value is 1000 and values greater than 1000 will
            be coerced down to 1000.
        page_token (str):
            A page token, received from a previous ``ListWorkflows``
            call. Provide this to retrieve the subsequent page.

            When paginating, all other parameters provided to
            ``ListWorkflows`` must match the call that provided the page
            token.
        filter (str):
            Filter to restrict results to specific
            workflows.
        order_by (str):
            Comma-separated list of fields that that
            specify the order of the results. Default
            sorting order for a field is ascending. To
            specify descending order for a field, append a "
            desc" suffix.
            If not specified, the results will be returned
            in an unspecified order.
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
    filter: str = proto.Field(
        proto.STRING,
        number=4,
    )
    order_by: str = proto.Field(
        proto.STRING,
        number=5,
    )


class ListWorkflowsResponse(proto.Message):
    r"""Response for the
    [ListWorkflows][google.cloud.workflows.v1beta.Workflows.ListWorkflows]
    method.

    Attributes:
        workflows (MutableSequence[google.cloud.workflows_v1beta.types.Workflow]):
            The workflows which match the request.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
        unreachable (MutableSequence[str]):
            Unreachable resources.
    """

    @property
    def raw_page(self):
        return self

    workflows: MutableSequence["Workflow"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Workflow",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetWorkflowRequest(proto.Message):
    r"""Request for the
    [GetWorkflow][google.cloud.workflows.v1beta.Workflows.GetWorkflow]
    method.

    Attributes:
        name (str):
            Required. Name of the workflow which
            information should be retrieved. Format:
            projects/{project}/locations/{location}/workflows/{workflow}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateWorkflowRequest(proto.Message):
    r"""Request for the
    [CreateWorkflow][google.cloud.workflows.v1beta.Workflows.CreateWorkflow]
    method.

    Attributes:
        parent (str):
            Required. Project and location in which the
            workflow should be created. Format:
            projects/{project}/locations/{location}
        workflow (google.cloud.workflows_v1beta.types.Workflow):
            Required. Workflow to be created.
        workflow_id (str):
            Required. The ID of the workflow to be created. It has to
            fulfill the following requirements:

            - Must contain only letters, numbers, underscores and
              hyphens.
            - Must start with a letter.
            - Must be between 1-64 characters.
            - Must end with a number or a letter.
            - Must be unique within the customer project and location.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    workflow: "Workflow" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Workflow",
    )
    workflow_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class DeleteWorkflowRequest(proto.Message):
    r"""Request for the
    [DeleteWorkflow][google.cloud.workflows.v1beta.Workflows.DeleteWorkflow]
    method.

    Attributes:
        name (str):
            Required. Name of the workflow to be deleted.
            Format:
            projects/{project}/locations/{location}/workflows/{workflow}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateWorkflowRequest(proto.Message):
    r"""Request for the
    [UpdateWorkflow][google.cloud.workflows.v1beta.Workflows.UpdateWorkflow]
    method.

    Attributes:
        workflow (google.cloud.workflows_v1beta.types.Workflow):
            Required. Workflow to be updated.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            List of fields to be updated. If not present,
            the entire workflow will be updated.
    """

    workflow: "Workflow" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Workflow",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class OperationMetadata(proto.Message):
    r"""Represents the metadata of the long-running operation.

    Attributes:
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            The time the operation was created.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            The time the operation finished running.
        target (str):
            Server-defined resource path for the target
            of the operation.
        verb (str):
            Name of the verb executed by the operation.
        api_version (str):
            API version used to start the operation.
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
    api_version: str = proto.Field(
        proto.STRING,
        number=5,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
