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
import google.protobuf.struct_pb2 as struct_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.backupdr_v1.types import restore_template_common
from google.cloud.backupdr_v1.types import (
    restore_template_execution as gcb_restore_template_execution,
)

__protobuf__ = proto.module(
    package="google.cloud.backupdr.v1",
    manifest={
        "RestoreTemplate",
        "ExecutionSummary",
        "CreateRestoreTemplateRequest",
        "GetRestoreTemplateRequest",
        "UpdateRestoreTemplateRequest",
        "DeleteRestoreTemplateRequest",
        "RunRestoreTemplateRequest",
        "RunRestoreTemplateResponse",
        "ListRestoreTemplatesRequest",
        "ListRestoreTemplatesResponse",
    },
)


class RestoreTemplate(proto.Message):
    r"""A ``RestoreTemplate`` encapsulates DR readiness configurations for
    validating backups.

    Attributes:
        name (str):
            Identifier. The resource name of the
            RestoreTemplate.
        description (str):
            Optional. User-provided description of the
            restore template.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the restore
            template was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the restore
            template was last updated.
        resource_type (str):
            Required. Immutable. The specific type of the workload being
            restored. The format is "{service_name}/{resource_kind}",
            for example, "compute.googleapis.com/Instance".
        labels (MutableMapping[str, str]):
            Optional. User-defined labels.
        backup_selection_config (google.cloud.backupdr_v1.types.BackupSelectionConfig):
            Required. Backup selection configuration.
        pre_restore_config (google.cloud.backupdr_v1.types.PreRestoreConfig):
            Optional. Pre-restore configuration.
        post_restore_config (google.cloud.backupdr_v1.types.PostRestoreConfig):
            Optional. Post-restore configuration.
        verification_config (google.cloud.backupdr_v1.types.VerificationConfig):
            Optional. Verification configuration.
        restore_properties (google.protobuf.struct_pb2.Struct):
            Required. Defines target environments where the resource
            will be restored.

            The target resource name in ``restore_properties`` supports
            the ``{EXECUTION_ID}`` token to dynamically generate unique
            resource names for each execution. During restore execution,
            every occurrence of ``{EXECUTION_ID}`` in the target
            resource name is replaced with the 8-character
            ``RestoreTemplateExecution`` ID (for example,
            ``"restored-resource-{EXECUTION_ID}"`` or
            ``"restored-{EXECUTION_ID}-resource"`` resolves to
            ``"restored-resource-5d437b06"`` or
            ``"restored-5d437b06-resource"``).
        state (google.cloud.backupdr_v1.types.RestoreTemplate.State):
            Output only. The state of the restore
            template.
        execution_summary (google.cloud.backupdr_v1.types.ExecutionSummary):
            Output only. Summary of the last execution.
        etag (str):
            Optional. Etag for concurrency control.
    """

    class State(proto.Enum):
        r"""The state of the RestoreTemplate.

        Values:
            STATE_UNSPECIFIED (0):
                State not specified.
            CREATING (1):
                The template is being created.
            ACTIVE (2):
                The template is active and ready to use.
            UPDATING (3):
                The template is being updated.
            DELETING (4):
                The template is being deleted.
        """

        STATE_UNSPECIFIED = 0
        CREATING = 1
        ACTIVE = 2
        UPDATING = 3
        DELETING = 4

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    description: str = proto.Field(
        proto.STRING,
        number=2,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    resource_type: str = proto.Field(
        proto.STRING,
        number=5,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=6,
    )
    backup_selection_config: restore_template_common.BackupSelectionConfig = (
        proto.Field(
            proto.MESSAGE,
            number=7,
            message=restore_template_common.BackupSelectionConfig,
        )
    )
    pre_restore_config: restore_template_common.PreRestoreConfig = proto.Field(
        proto.MESSAGE,
        number=8,
        message=restore_template_common.PreRestoreConfig,
    )
    post_restore_config: restore_template_common.PostRestoreConfig = proto.Field(
        proto.MESSAGE,
        number=9,
        message=restore_template_common.PostRestoreConfig,
    )
    verification_config: restore_template_common.VerificationConfig = proto.Field(
        proto.MESSAGE,
        number=10,
        message=restore_template_common.VerificationConfig,
    )
    restore_properties: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=11,
        message=struct_pb2.Struct,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=12,
        enum=State,
    )
    execution_summary: "ExecutionSummary" = proto.Field(
        proto.MESSAGE,
        number=13,
        message="ExecutionSummary",
    )
    etag: str = proto.Field(
        proto.STRING,
        number=14,
    )


class ExecutionSummary(proto.Message):
    r"""Summary of the last execution.

    Attributes:
        last_execution (str):
            Output only. The resource name of the last execution.
            Format:
            ``projects/{project}/locations/{location}/restoreTemplates/{restore_template}/executions/{execution}``
        last_execution_state (google.cloud.backupdr_v1.types.RestoreTemplateExecution.ExecutionState):
            Output only. The state of the last execution.
    """

    last_execution: str = proto.Field(
        proto.STRING,
        number=1,
    )
    last_execution_state: gcb_restore_template_execution.RestoreTemplateExecution.ExecutionState = proto.Field(
        proto.ENUM,
        number=2,
        enum=gcb_restore_template_execution.RestoreTemplateExecution.ExecutionState,
    )


class CreateRestoreTemplateRequest(proto.Message):
    r"""Request message for creating a RestoreTemplate instance.

    Attributes:
        parent (str):
            Required. The restore template project and location in the
            format 'projects/{project_id}/locations/{location}'.
        restore_template_id (str):
            Required. The ID of the restore template to
            create. The ID must be unique for the specified
            project and location.
        restore_template (google.cloud.backupdr_v1.types.RestoreTemplate):
            Required. A RestoreTemplate resource.
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server will
            know to ignore the request if it has already
            been completed.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    restore_template_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    restore_template: "RestoreTemplate" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="RestoreTemplate",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class GetRestoreTemplateRequest(proto.Message):
    r"""Request message for getting a RestoreTemplate instance.

    Attributes:
        name (str):
            Required. The name of the restore template to retrieve.
            Format:
            'projects/{project_id}/locations/{location}/restoreTemplates/{restore_template_id}'
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateRestoreTemplateRequest(proto.Message):
    r"""Request message for updating a RestoreTemplate instance.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. The list of fields to update. Field mask is used
            to specify the fields to be overwritten in the
            RestoreTemplate resource by the update. The fields specified
            in the update_mask are relative to the resource, not the
            full request. A field will be overwritten if it is in the
            mask.
        restore_template (google.cloud.backupdr_v1.types.RestoreTemplate):
            Required. The restore template to update.
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server will
            know to ignore the request if it has already
            been completed.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
        validate_only (bool):
            Optional. Only validate the request, but do
            not perform mutations. The default is 'false'.
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    restore_template: "RestoreTemplate" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="RestoreTemplate",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=4,
    )


class DeleteRestoreTemplateRequest(proto.Message):
    r"""Request message for deleting a RestoreTemplate instance.

    Attributes:
        name (str):
            Required. The name of the restore template to delete.
            Format:
            'projects/{project_id}/locations/{location}/restoreTemplates/{restore_template_id}'
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server will
            know to ignore the request if it has already
            been completed.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
        force (bool):
            Optional. If set to true, any child
            RestoreTemplateExecutions will also be deleted.
            If false and the RestoreTemplate has any child
            executions, the request will fail.
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


class RunRestoreTemplateRequest(proto.Message):
    r"""Request message for running a RestoreTemplate.

    Attributes:
        name (str):
            Required. The name of the restore template to run. Format:
            'projects/{project_id}/locations/{location}/restoreTemplates/{restore_template_id}'
        backup (str):
            Optional. The resource name of the Backup to restore from.
            If not specified, the latest backup matching the backup
            selection configuration in the RestoreTemplate will be used.
            Format:
            'projects/{project}/locations/{location}/backupVaults/{backup_vault}/dataSources/{data_source}/backups/{backup}'
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server will
            know to ignore the request if it has already
            been completed.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    backup: str = proto.Field(
        proto.STRING,
        number=2,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class RunRestoreTemplateResponse(proto.Message):
    r"""Response message for RunRestoreTemplate.

    Attributes:
        restore_template_execution (str):
            Output only. The resource name of the initiated
            RestoreTemplateExecution. Format:
            ``projects/{project}/locations/{location}/restoreTemplates/{restore_template}/executions/{execution}``
    """

    restore_template_execution: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListRestoreTemplatesRequest(proto.Message):
    r"""Request message for listing RestoreTemplates.

    Attributes:
        parent (str):
            Required. The project and location from which to list the
            restore templates. Format:
            ``projects/{project}/locations/{location}``.
        page_size (int):
            Optional. The maximum number of items to
            return.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListRestoreTemplates`` call.
        filter (str):
            Optional. Field match expression used to
            filter the results.
        order_by (str):
            Optional. Field by which to sort the results.
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


class ListRestoreTemplatesResponse(proto.Message):
    r"""Response message for listing RestoreTemplates.

    Attributes:
        restore_templates (MutableSequence[google.cloud.backupdr_v1.types.RestoreTemplate]):
            The list of RestoreTemplates.
        next_page_token (str):
            A token which may be sent as ``page_token`` in a subsequent
            ``ListRestoreTemplates`` call.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    restore_templates: MutableSequence["RestoreTemplate"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="RestoreTemplate",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
