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

from google.cloud.bigquery_migration_v2alpha.types import migration_entities

__protobuf__ = proto.module(
    package="google.cloud.bigquery.migration.v2alpha",
    manifest={
        "CreateMigrationWorkflowRequest",
        "GetMigrationWorkflowRequest",
        "ListMigrationWorkflowsRequest",
        "ListMigrationWorkflowsResponse",
        "DeleteMigrationWorkflowRequest",
        "StartMigrationWorkflowRequest",
        "GetMigrationSubtaskRequest",
        "ListMigrationSubtasksRequest",
        "ListMigrationSubtasksResponse",
    },
)


class CreateMigrationWorkflowRequest(proto.Message):
    r"""Request to create a migration workflow resource.

    Attributes:
        parent (str):
            Required. The name of the project to which this migration
            workflow belongs. Example: ``projects/foo/locations/bar``
        migration_workflow (google.cloud.bigquery_migration_v2alpha.types.MigrationWorkflow):
            Required. The migration workflow to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    migration_workflow: migration_entities.MigrationWorkflow = proto.Field(
        proto.MESSAGE,
        number=2,
        message=migration_entities.MigrationWorkflow,
    )


class GetMigrationWorkflowRequest(proto.Message):
    r"""A request to get a previously created migration workflow.

    Attributes:
        name (str):
            Required. The unique identifier for the migration workflow.
            Example: ``projects/123/locations/us/workflows/1234``
        read_mask (google.protobuf.field_mask_pb2.FieldMask):
            The list of fields to be retrieved.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    read_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class ListMigrationWorkflowsRequest(proto.Message):
    r"""A request to list previously created migration workflows.

    Attributes:
        parent (str):
            Required. The project and location of the migration
            workflows to list. Example: ``projects/123/locations/us``
        read_mask (google.protobuf.field_mask_pb2.FieldMask):
            The list of fields to be retrieved.
        page_size (int):
            The maximum number of migration workflows to
            return. The service may return fewer than this
            number.
        page_token (str):
            A page token, received from previous
            ``ListMigrationWorkflows`` call. Provide this to retrieve
            the subsequent page.

            When paginating, all other parameters provided to
            ``ListMigrationWorkflows`` must match the call that provided
            the page token.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    read_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=3,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=4,
    )


class ListMigrationWorkflowsResponse(proto.Message):
    r"""Response object for a ``ListMigrationWorkflows`` call.

    Attributes:
        migration_workflows (MutableSequence[google.cloud.bigquery_migration_v2alpha.types.MigrationWorkflow]):
            The migration workflows for the specified
            project / location.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    migration_workflows: MutableSequence[migration_entities.MigrationWorkflow] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=migration_entities.MigrationWorkflow,
        )
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class DeleteMigrationWorkflowRequest(proto.Message):
    r"""A request to delete a previously created migration workflow.

    Attributes:
        name (str):
            Required. The unique identifier for the migration workflow.
            Example: ``projects/123/locations/us/workflows/1234``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class StartMigrationWorkflowRequest(proto.Message):
    r"""A request to start a previously created migration workflow.

    Attributes:
        name (str):
            Required. The unique identifier for the migration workflow.
            Example: ``projects/123/locations/us/workflows/1234``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class GetMigrationSubtaskRequest(proto.Message):
    r"""A request to get a previously created migration subtasks.

    Attributes:
        name (str):
            Required. The unique identifier for the migration subtask.
            Example:
            ``projects/123/locations/us/workflows/1234/subtasks/543``
        read_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. The list of fields to be retrieved.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    read_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class ListMigrationSubtasksRequest(proto.Message):
    r"""A request to list previously created migration subtasks.

    Attributes:
        parent (str):
            Required. The migration task of the subtasks to list.
            Example: ``projects/123/locations/us/workflows/1234``
        read_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. The list of fields to be retrieved.
        page_size (int):
            Optional. The maximum number of migration
            tasks to return. The service may return fewer
            than this number.
        page_token (str):
            Optional. A page token, received from previous
            ``ListMigrationSubtasks`` call. Provide this to retrieve the
            subsequent page.

            When paginating, all other parameters provided to
            ``ListMigrationSubtasks`` must match the call that provided
            the page token.
        filter (str):
            Optional. The filter to apply. This can be used to get the
            subtasks of a specific tasks in a workflow, e.g.
            ``migration_task = "ab012"`` where ``"ab012"`` is the task
            ID (not the name in the named map).
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    read_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=3,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=4,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=5,
    )


class ListMigrationSubtasksResponse(proto.Message):
    r"""Response object for a ``ListMigrationSubtasks`` call.

    Attributes:
        migration_subtasks (MutableSequence[google.cloud.bigquery_migration_v2alpha.types.MigrationSubtask]):
            The migration subtasks for the specified
            task.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    migration_subtasks: MutableSequence[migration_entities.MigrationSubtask] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=migration_entities.MigrationSubtask,
        )
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
