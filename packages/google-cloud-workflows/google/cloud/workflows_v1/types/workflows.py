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
    package="google.cloud.workflows.v1",
    manifest={
        "ExecutionHistoryLevel",
        "Workflow",
        "ListWorkflowsRequest",
        "ListWorkflowsResponse",
        "GetWorkflowRequest",
        "CreateWorkflowRequest",
        "DeleteWorkflowRequest",
        "UpdateWorkflowRequest",
        "OperationMetadata",
        "ListWorkflowRevisionsRequest",
        "ListWorkflowRevisionsResponse",
    },
)


class ExecutionHistoryLevel(proto.Enum):
    r"""Define possible options for enabling the execution history
    level.

    Values:
        EXECUTION_HISTORY_LEVEL_UNSPECIFIED (0):
            The default/unset value.
        EXECUTION_HISTORY_BASIC (1):
            Enable execution history basic feature.
        EXECUTION_HISTORY_DETAILED (2):
            Enable execution history detailed feature.
    """

    EXECUTION_HISTORY_LEVEL_UNSPECIFIED = 0
    EXECUTION_HISTORY_BASIC = 1
    EXECUTION_HISTORY_DETAILED = 2


class Workflow(proto.Message):
    r"""Workflow program to be executed by Workflows.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            The resource name of the workflow.
            Format:
            projects/{project}/locations/{location}/workflows/{workflow}.
            This is a workflow-wide field and is not tied to
            a specific revision.
        description (str):
            Description of the workflow provided by the
            user. Must be at most 1000 Unicode characters
            long. This is a workflow-wide field and is not
            tied to a specific revision.
        state (google.cloud.workflows_v1.types.Workflow.State):
            Output only. State of the workflow
            deployment.
        revision_id (str):
            Output only. The revision of the workflow. A new revision of
            a workflow is created as a result of updating the following
            properties of a workflow:

            - [Service
              account][google.cloud.workflows.v1.Workflow.service_account]
            - [Workflow code to be
              executed][google.cloud.workflows.v1.Workflow.source_contents]

            The format is "000001-a4d", where the first six characters
            define the zero-padded revision ordinal number. They are
            followed by a hyphen and three hexadecimal random
            characters.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp for when the
            workflow was created. This is a workflow-wide
            field and is not tied to a specific revision.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp for when the
            workflow was last updated. This is a
            workflow-wide field and is not tied to a
            specific revision.
        revision_create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp for the latest
            revision of the workflow's creation.
        labels (MutableMapping[str, str]):
            Labels associated with this workflow.
            Labels can contain at most 64 entries. Keys and
            values can be no longer than 63 characters and
            can only contain lowercase letters, numeric
            characters, underscores, and dashes. Label keys
            must start with a letter. International
            characters are allowed.
            This is a workflow-wide field and is not tied to
            a specific revision.
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
        crypto_key_name (str):
            Optional. The resource name of a KMS crypto key used to
            encrypt or decrypt the data associated with the workflow.

            Format:
            projects/{project}/locations/{location}/keyRings/{keyRing}/cryptoKeys/{cryptoKey}

            Using ``-`` as a wildcard for the ``{project}`` or not
            providing one at all will infer the project from the
            account.

            If not provided, data associated with the workflow will not
            be CMEK-encrypted.
        state_error (google.cloud.workflows_v1.types.Workflow.StateError):
            Output only. Error regarding the state of the
            workflow. For example, this field will have
            error details if the execution data is
            unavailable due to revoked KMS key permissions.
        call_log_level (google.cloud.workflows_v1.types.Workflow.CallLogLevel):
            Optional. Describes the level of platform
            logging to apply to calls and call responses
            during executions of this workflow. If both the
            workflow and the execution specify a logging
            level, the execution level takes precedence.
        user_env_vars (MutableMapping[str, str]):
            Optional. User-defined environment variables
            associated with this workflow revision. This map
            has a maximum length of 20. Each string can take
            up to 4KiB. Keys cannot be empty strings and
            cannot start with "GOOGLE" or "WORKFLOWS".
        execution_history_level (google.cloud.workflows_v1.types.ExecutionHistoryLevel):
            Optional. Describes the execution history
            level to apply to this workflow.
        all_kms_keys (MutableSequence[str]):
            Output only. A list of all KMS crypto keys
            used to encrypt or decrypt the data associated
            with the workflow.
        all_kms_keys_versions (MutableSequence[str]):
            Output only. A list of all KMS crypto key
            versions used to encrypt or decrypt the data
            associated with the workflow.
        crypto_key_version (str):
            Output only. The resource name of a KMS
            crypto key version used to encrypt or decrypt
            the data associated with the workflow.

            Format:

            projects/{project}/locations/{location}/keyRings/{keyRing}/cryptoKeys/{cryptoKey}/cryptoKeyVersions/{cryptoKeyVersion}
        tags (MutableMapping[str, str]):
            Optional. Input only. Immutable. Tags
            associated with this workflow.
    """

    class State(proto.Enum):
        r"""Describes the current state of workflow deployment.

        Values:
            STATE_UNSPECIFIED (0):
                Invalid state.
            ACTIVE (1):
                The workflow has been deployed successfully
                and is serving.
            UNAVAILABLE (2):
                Workflow data is unavailable. See the ``state_error`` field.
        """

        STATE_UNSPECIFIED = 0
        ACTIVE = 1
        UNAVAILABLE = 2

    class CallLogLevel(proto.Enum):
        r"""Describes the level of platform logging to apply to calls and
        call responses during workflow executions.

        Values:
            CALL_LOG_LEVEL_UNSPECIFIED (0):
                No call logging level specified.
            LOG_ALL_CALLS (1):
                Log all call steps within workflows, all call
                returns, and all exceptions raised.
            LOG_ERRORS_ONLY (2):
                Log only exceptions that are raised from call
                steps within workflows.
            LOG_NONE (3):
                Explicitly log nothing.
        """

        CALL_LOG_LEVEL_UNSPECIFIED = 0
        LOG_ALL_CALLS = 1
        LOG_ERRORS_ONLY = 2
        LOG_NONE = 3

    class StateError(proto.Message):
        r"""Describes an error related to the current state of the
        workflow.

        Attributes:
            details (str):
                Provides specifics about the error.
            type_ (google.cloud.workflows_v1.types.Workflow.StateError.Type):
                The type of this state error.
        """

        class Type(proto.Enum):
            r"""Describes the possibled types of a state error.

            Values:
                TYPE_UNSPECIFIED (0):
                    No type specified.
                KMS_ERROR (1):
                    Caused by an issue with KMS.
            """

            TYPE_UNSPECIFIED = 0
            KMS_ERROR = 1

        details: str = proto.Field(
            proto.STRING,
            number=1,
        )
        type_: "Workflow.StateError.Type" = proto.Field(
            proto.ENUM,
            number=2,
            enum="Workflow.StateError.Type",
        )

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
    crypto_key_name: str = proto.Field(
        proto.STRING,
        number=11,
    )
    state_error: StateError = proto.Field(
        proto.MESSAGE,
        number=12,
        message=StateError,
    )
    call_log_level: CallLogLevel = proto.Field(
        proto.ENUM,
        number=13,
        enum=CallLogLevel,
    )
    user_env_vars: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=14,
    )
    execution_history_level: "ExecutionHistoryLevel" = proto.Field(
        proto.ENUM,
        number=15,
        enum="ExecutionHistoryLevel",
    )
    all_kms_keys: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=16,
    )
    all_kms_keys_versions: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=17,
    )
    crypto_key_version: str = proto.Field(
        proto.STRING,
        number=18,
    )
    tags: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=19,
    )


class ListWorkflowsRequest(proto.Message):
    r"""Request for the
    [ListWorkflows][google.cloud.workflows.v1.Workflows.ListWorkflows]
    method.

    Attributes:
        parent (str):
            Required. Project and location from which the
            workflows should be listed. Format:
            projects/{project}/locations/{location}
        page_size (int):
            Maximum number of workflows to return per
            call. The service might return fewer than this
            value even if not at the end of the collection.
            If a value is not specified, a default value of
            500 is used. The maximum permitted value is 1000
            and values greater than 1000 are coerced down to
            1000.
        page_token (str):
            A page token, received from a previous ``ListWorkflows``
            call. Provide this to retrieve the subsequent page.

            When paginating, all other parameters provided to
            ``ListWorkflows`` must match the call that provided the page
            token.
        filter (str):
            Filter to restrict results to specific workflows. For
            details, see AIP-160.

            For example, if you are using the Google APIs Explorer:

            ``state="SUCCEEDED"``

            or

            ``createTime>"2023-08-01" AND state="FAILED"``
        order_by (str):
            Comma-separated list of fields that specify
            the order of the results. Default sorting order
            for a field is ascending. To specify descending
            order for a field, append a "desc" suffix.
            If not specified, the results are returned in an
            unspecified order.
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
    [ListWorkflows][google.cloud.workflows.v1.Workflows.ListWorkflows]
    method.

    Attributes:
        workflows (MutableSequence[google.cloud.workflows_v1.types.Workflow]):
            The workflows that match the request.
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
    [GetWorkflow][google.cloud.workflows.v1.Workflows.GetWorkflow]
    method.

    Attributes:
        name (str):
            Required. Name of the workflow for which
            information should be retrieved. Format:
            projects/{project}/locations/{location}/workflows/{workflow}
        revision_id (str):
            Optional. The revision of the workflow to retrieve. If the
            revision_id is empty, the latest revision is retrieved. The
            format is "000001-a4d", where the first six characters
            define the zero-padded decimal revision number. They are
            followed by a hyphen and three hexadecimal characters.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    revision_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class CreateWorkflowRequest(proto.Message):
    r"""Request for the
    [CreateWorkflow][google.cloud.workflows.v1.Workflows.CreateWorkflow]
    method.

    Attributes:
        parent (str):
            Required. Project and location in which the
            workflow should be created. Format:
            projects/{project}/locations/{location}
        workflow (google.cloud.workflows_v1.types.Workflow):
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
    [DeleteWorkflow][google.cloud.workflows.v1.Workflows.DeleteWorkflow]
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
    [UpdateWorkflow][google.cloud.workflows.v1.Workflows.UpdateWorkflow]
    method.

    Attributes:
        workflow (google.cloud.workflows_v1.types.Workflow):
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


class ListWorkflowRevisionsRequest(proto.Message):
    r"""Request for the
    [ListWorkflowRevisions][google.cloud.workflows.v1.Workflows.ListWorkflowRevisions]
    method.

    Attributes:
        name (str):
            Required. Workflow for which the revisions
            should be listed. Format:
            projects/{project}/locations/{location}/workflows/{workflow}
        page_size (int):
            The maximum number of revisions to return per
            page. If a value is not specified, a default
            value of 20 is used. The maximum permitted value
            is
            100. Values greater than 100 are coerced down to
                100.
        page_token (str):
            The page token, received from a previous
            ListWorkflowRevisions call. Provide this to
            retrieve the subsequent page.
    """

    name: str = proto.Field(
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


class ListWorkflowRevisionsResponse(proto.Message):
    r"""Response for the
    [ListWorkflowRevisions][google.cloud.workflows.v1.Workflows.ListWorkflowRevisions]
    method.

    Attributes:
        workflows (MutableSequence[google.cloud.workflows_v1.types.Workflow]):
            The revisions of the workflow, ordered in
            reverse chronological order.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
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


__all__ = tuple(sorted(__protobuf__.manifest))
