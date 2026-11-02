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

from google.cloud.ces_v1.types import agent as gcc_agent
from google.cloud.ces_v1.types import app as gcc_app
from google.cloud.ces_v1.types import app_version as gcc_app_version
from google.cloud.ces_v1.types import changelog, conversation
from google.cloud.ces_v1.types import deployment as gcc_deployment
from google.cloud.ces_v1.types import example as gcc_example
from google.cloud.ces_v1.types import guardrail as gcc_guardrail
from google.cloud.ces_v1.types import tool as gcc_tool
from google.cloud.ces_v1.types import toolset as gcc_toolset

__protobuf__ = proto.module(
    package="google.cloud.ces.v1",
    manifest={
        "ListAppsRequest",
        "ListAppsResponse",
        "GetAppRequest",
        "CreateAppRequest",
        "UpdateAppRequest",
        "DeleteAppRequest",
        "ExportAppRequest",
        "ExportAppResponse",
        "ImportAppRequest",
        "ImportAppResponse",
        "ListAgentsRequest",
        "ListAgentsResponse",
        "GetAgentRequest",
        "CreateAgentRequest",
        "UpdateAgentRequest",
        "DeleteAgentRequest",
        "OperationMetadata",
        "ListExamplesRequest",
        "ListExamplesResponse",
        "GetExampleRequest",
        "CreateExampleRequest",
        "UpdateExampleRequest",
        "DeleteExampleRequest",
        "ListToolsRequest",
        "ListToolsResponse",
        "GetToolRequest",
        "CreateToolRequest",
        "UpdateToolRequest",
        "DeleteToolRequest",
        "ListConversationsRequest",
        "ListConversationsResponse",
        "GetConversationRequest",
        "DeleteConversationRequest",
        "BatchDeleteConversationsRequest",
        "BatchDeleteConversationsResponse",
        "ListGuardrailsRequest",
        "ListGuardrailsResponse",
        "GetGuardrailRequest",
        "CreateGuardrailRequest",
        "UpdateGuardrailRequest",
        "DeleteGuardrailRequest",
        "ListDeploymentsRequest",
        "ListDeploymentsResponse",
        "GetDeploymentRequest",
        "CreateDeploymentRequest",
        "UpdateDeploymentRequest",
        "DeleteDeploymentRequest",
        "ListToolsetsRequest",
        "ListToolsetsResponse",
        "GetToolsetRequest",
        "CreateToolsetRequest",
        "UpdateToolsetRequest",
        "DeleteToolsetRequest",
        "ListAppVersionsRequest",
        "ListAppVersionsResponse",
        "GetAppVersionRequest",
        "DeleteAppVersionRequest",
        "CreateAppVersionRequest",
        "RestoreAppVersionRequest",
        "RestoreAppVersionResponse",
        "ListChangelogsRequest",
        "ListChangelogsResponse",
        "GetChangelogRequest",
    },
)


class ListAppsRequest(proto.Message):
    r"""Request message for
    [AgentService.ListApps][google.cloud.ces.v1.AgentService.ListApps].

    Attributes:
        parent (str):
            Required. The resource name of the location
            to list apps from.
        page_size (int):
            Optional. Requested page size. Server may
            return fewer items than requested. If
            unspecified, server will pick an appropriate
            default.
        page_token (str):
            Optional. The
            [next_page_token][google.cloud.ces.v1.ListAppsResponse.next_page_token]
            value returned from a previous list
            [AgentService.ListApps][google.cloud.ces.v1.AgentService.ListApps]
            call.
        filter (str):
            Optional. Filter to be applied when listing
            the apps. See https://google.aip.dev/160 for
            more details.
        order_by (str):
            Optional. Field to sort by. Only "name" and "create_time" is
            supported. See https://google.aip.dev/132#ordering for more
            details.
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


class ListAppsResponse(proto.Message):
    r"""Response message for
    [AgentService.ListApps][google.cloud.ces.v1.AgentService.ListApps].

    Attributes:
        apps (MutableSequence[google.cloud.ces_v1.types.App]):
            The list of apps.
        next_page_token (str):
            A token that can be sent as
            [ListAppsRequest.page_token][google.cloud.ces.v1.ListAppsRequest.page_token]
            to retrieve the next page. Absence of this field indicates
            there are no subsequent pages.
        unreachable (MutableSequence[str]):
            Unordered list. Locations that could not be
            reached.
    """

    @property
    def raw_page(self):
        return self

    apps: MutableSequence[gcc_app.App] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=gcc_app.App,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetAppRequest(proto.Message):
    r"""Request message for
    [AgentService.GetApp][google.cloud.ces.v1.AgentService.GetApp].

    Attributes:
        name (str):
            Required. The resource name of the app to
            retrieve.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateAppRequest(proto.Message):
    r"""Request message for
    [AgentService.CreateApp][google.cloud.ces.v1.AgentService.CreateApp].

    Attributes:
        parent (str):
            Required. The resource name of the location
            to create an app in.
        app_id (str):
            Optional. The ID to use for the app, which
            will become the final component of the app's
            resource name. If not provided, a unique ID will
            be automatically assigned for the app.
        app (google.cloud.ces_v1.types.App):
            Required. The app to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    app_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    app: gcc_app.App = proto.Field(
        proto.MESSAGE,
        number=3,
        message=gcc_app.App,
    )


class UpdateAppRequest(proto.Message):
    r"""Request message for
    [AgentService.UpdateApp][google.cloud.ces.v1.AgentService.UpdateApp].

    Attributes:
        app (google.cloud.ces_v1.types.App):
            Required. The app to update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. Field mask is used to control which
            fields get updated. If the mask is not present,
            all fields will be updated.
    """

    app: gcc_app.App = proto.Field(
        proto.MESSAGE,
        number=1,
        message=gcc_app.App,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class DeleteAppRequest(proto.Message):
    r"""Request message for
    [AgentService.DeleteApp][google.cloud.ces.v1.AgentService.DeleteApp].

    Attributes:
        name (str):
            Required. The resource name of the app to
            delete.
        etag (str):
            Optional. The current etag of the app. If an
            etag is not provided, the deletion will
            overwrite any concurrent changes. If an etag is
            provided and does not match the current etag of
            the app, deletion will be blocked and an ABORTED
            error will be returned.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ExportAppRequest(proto.Message):
    r"""Request message for
    [AgentService.ExportApp][google.cloud.ces.v1.AgentService.ExportApp].

    Attributes:
        name (str):
            Required. The resource name of the app to
            export.
        export_format (google.cloud.ces_v1.types.ExportAppRequest.ExportFormat):
            Required. The format to export the app in.
        gcs_uri (str):
            Optional. The `Google Cloud
            Storage <https://cloud.google.com/storage/docs/>`__ URI to
            which to export the app. The format of this URI must be
            ``gs://<bucket-name>/<object-name>``. The exported app
            archive will be written directly to the specified GCS
            object.
        app_version (str):
            Optional. The resource name of the app version to export.
            Format:
            ``projects/{project}/locations/{location}/apps/{app}/versions/{version}``.
    """

    class ExportFormat(proto.Enum):
        r"""Export format for the app.

        Values:
            EXPORT_FORMAT_UNSPECIFIED (0):
                The export format is unspecified.
            JSON (1):
                The export format is JSON.
            YAML (2):
                The export format is YAML.
        """

        EXPORT_FORMAT_UNSPECIFIED = 0
        JSON = 1
        YAML = 2

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    export_format: ExportFormat = proto.Field(
        proto.ENUM,
        number=2,
        enum=ExportFormat,
    )
    gcs_uri: str = proto.Field(
        proto.STRING,
        number=3,
    )
    app_version: str = proto.Field(
        proto.STRING,
        number=4,
    )


class ExportAppResponse(proto.Message):
    r"""Response message for
    [AgentService.ExportApp][google.cloud.ces.v1.AgentService.ExportApp].

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        app_content (bytes):
            App folder compressed as a zip file.

            This field is a member of `oneof`_ ``app``.
        app_uri (str):
            The `Google Cloud
            Storage <https://cloud.google.com/storage/docs/>`__ URI to
            which the app was exported.

            This field is a member of `oneof`_ ``app``.
    """

    app_content: bytes = proto.Field(
        proto.BYTES,
        number=1,
        oneof="app",
    )
    app_uri: str = proto.Field(
        proto.STRING,
        number=2,
        oneof="app",
    )


class ImportAppRequest(proto.Message):
    r"""Request message for
    [AgentService.ImportApp][google.cloud.ces.v1.AgentService.ImportApp].

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        gcs_uri (str):
            The `Google Cloud
            Storage <https://cloud.google.com/storage/docs/>`__ URI from
            which to import app. The format of this URI must be
            ``gs://<bucket-name>/<object-name>``.

            This field is a member of `oneof`_ ``app``.
        app_content (bytes):
            Raw bytes representing the compressed zip
            file with the app folder structure.

            This field is a member of `oneof`_ ``app``.
        parent (str):
            Required. The parent resource name with the
            location of the app to import.
        display_name (str):
            Optional. The display name of the app to import.

            - If the app is created on import, and the display name is
              specified, the imported app will use this display name. If
              a conflict is detected with an existing app, a timestamp
              will be appended to the display name to make it unique.
            - If the app is a reimport, this field should not be set.
              Providing a display name during reimport will result in an
              INVALID_ARGUMENT error.
        app_id (str):
            Optional. The ID to use for the imported app.

            - If not specified, a unique ID will be automatically
              assigned for the app.
            - Otherwise, the imported app will use this ID as the final
              component of its resource name. If an app with the same ID
              already exists at the specified location in the project,
              the content of the existing app will be replaced.
        import_options (google.cloud.ces_v1.types.ImportAppRequest.ImportOptions):
            Optional. Options governing the import
            process for the app.
        ignore_app_lock (bool):
            Optional. Flag for overriding the app lock
            during import. If set to true, the import
            process will ignore the app lock.
    """

    class ImportOptions(proto.Message):
        r"""Configuration options for the app import process.
        These options control how the import behaves, particularly when
        conflicts arise with existing app data.

        Attributes:
            conflict_resolution_strategy (google.cloud.ces_v1.types.ImportAppRequest.ImportOptions.ConflictResolutionStrategy):
                Optional. The strategy to use when resolving
                conflicts during import.
        """

        class ConflictResolutionStrategy(proto.Enum):
            r"""Defines the strategy for handling conflicts when an app with
            the same ID already exists, or when imported resources (like
            Agents, Tools, etc.) have the same display names as existing
            resources within that app.

            Values:
                CONFLICT_RESOLUTION_STRATEGY_UNSPECIFIED (0):
                    The conflict resolution strategy is
                    unspecified.
                REPLACE (1):
                    Replace existing data with imported data. If an app with the
                    same ``app_id`` already exists, its content will be updated
                    based on the imported app.

                    - Resources (App, Agents, Tools, Examples, Guardrails,
                      Toolsets) in the imported app that have the same display
                      name as existing resources will overwrite the existing
                      ones.
                    - Imported resources with new display names will be created.
                    - Existing resources that do not have a matching display
                      name in the imported app will remain untouched.
                OVERWRITE (2):
                    Overwrite existing data with imported data. If an app with
                    the same ``app_id`` already exists, its content will be
                    overwritten with the imported app.

                    - Existing resources (Agents, Tools, Examples, Guardrails,
                      Toolsets) in the app will be deleted.
                    - Imported resources will be created as new resources.
            """

            CONFLICT_RESOLUTION_STRATEGY_UNSPECIFIED = 0
            REPLACE = 1
            OVERWRITE = 2

        conflict_resolution_strategy: "ImportAppRequest.ImportOptions.ConflictResolutionStrategy" = proto.Field(
            proto.ENUM,
            number=1,
            enum="ImportAppRequest.ImportOptions.ConflictResolutionStrategy",
        )

    gcs_uri: str = proto.Field(
        proto.STRING,
        number=4,
        oneof="app",
    )
    app_content: bytes = proto.Field(
        proto.BYTES,
        number=5,
        oneof="app",
    )
    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    app_id: str = proto.Field(
        proto.STRING,
        number=3,
    )
    import_options: ImportOptions = proto.Field(
        proto.MESSAGE,
        number=6,
        message=ImportOptions,
    )
    ignore_app_lock: bool = proto.Field(
        proto.BOOL,
        number=7,
    )


class ImportAppResponse(proto.Message):
    r"""Response message for
    [AgentService.ImportApp][google.cloud.ces.v1.AgentService.ImportApp].

    Attributes:
        name (str):
            The resource name of the app that was
            imported.
        warnings (MutableSequence[str]):
            Warning messages generated during the import
            process. If errors occur for specific resources,
            they will not be included in the imported app
            and the error will be mentioned here.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    warnings: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class ListAgentsRequest(proto.Message):
    r"""Request message for
    [AgentService.ListAgents][google.cloud.ces.v1.AgentService.ListAgents].

    Attributes:
        parent (str):
            Required. The resource name of the app to
            list agents from.
        page_size (int):
            Optional. Requested page size. Server may
            return fewer items than requested. If
            unspecified, server will pick an appropriate
            default.
        page_token (str):
            Optional. The
            [next_page_token][google.cloud.ces.v1.ListAgentsResponse.next_page_token]
            value returned from a previous list
            [AgentService.ListAgents][google.cloud.ces.v1.AgentService.ListAgents]
            call.
        filter (str):
            Optional. Filter to be applied when listing
            the agents. See https://google.aip.dev/160 for
            more details.
        order_by (str):
            Optional. Field to sort by. Only "name" and "create_time" is
            supported. See https://google.aip.dev/132#ordering for more
            details.
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


class ListAgentsResponse(proto.Message):
    r"""Response message for
    [AgentService.ListAgents][google.cloud.ces.v1.AgentService.ListAgents].

    Attributes:
        agents (MutableSequence[google.cloud.ces_v1.types.Agent]):
            The list of agents.
        next_page_token (str):
            A token that can be sent as
            [ListAgentsRequest.page_token][google.cloud.ces.v1.ListAgentsRequest.page_token]
            to retrieve the next page. Absence of this field indicates
            there are no subsequent pages.
    """

    @property
    def raw_page(self):
        return self

    agents: MutableSequence[gcc_agent.Agent] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=gcc_agent.Agent,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetAgentRequest(proto.Message):
    r"""Request message for
    [AgentService.GetAgent][google.cloud.ces.v1.AgentService.GetAgent].

    Attributes:
        name (str):
            Required. The resource name of the agent to
            retrieve.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateAgentRequest(proto.Message):
    r"""Request message for
    [AgentService.CreateAgent][google.cloud.ces.v1.AgentService.CreateAgent].

    Attributes:
        parent (str):
            Required. The resource name of the app to
            create an agent in.
        agent_id (str):
            Optional. The ID to use for the agent, which
            will become the final component of the agent's
            resource name. If not provided, a unique ID will
            be automatically assigned for the agent.
        agent (google.cloud.ces_v1.types.Agent):
            Required. The agent to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    agent_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    agent: gcc_agent.Agent = proto.Field(
        proto.MESSAGE,
        number=3,
        message=gcc_agent.Agent,
    )


class UpdateAgentRequest(proto.Message):
    r"""Request message for
    [AgentService.UpdateAgent][google.cloud.ces.v1.AgentService.UpdateAgent].

    Attributes:
        agent (google.cloud.ces_v1.types.Agent):
            Required. The agent to update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. Field mask is used to control which
            fields get updated. If the mask is not present,
            all fields will be updated.
    """

    agent: gcc_agent.Agent = proto.Field(
        proto.MESSAGE,
        number=1,
        message=gcc_agent.Agent,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class DeleteAgentRequest(proto.Message):
    r"""Request message for
    [AgentService.DeleteAgent][google.cloud.ces.v1.AgentService.DeleteAgent].

    Attributes:
        name (str):
            Required. The resource name of the agent to
            delete.
        force (bool):
            Optional. Indicates whether to forcefully delete the agent,
            even if it is still referenced by other app/agents/examples.

            - If ``force = false``, the deletion fails if other
              agents/examples reference it.
            - If ``force = true``, delete the agent and remove it from
              all referencing apps/agents/examples.
        etag (str):
            Optional. The current etag of the agent. If
            an etag is not provided, the deletion will
            overwrite any concurrent changes. If an etag is
            provided and does not match the current etag of
            the agent, deletion will be blocked and an
            ABORTED error will be returned.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    force: bool = proto.Field(
        proto.BOOL,
        number=2,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=3,
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
        status_message (str):
            Output only. Human-readable status of the
            operation, if any.
        requested_cancellation (bool):
            Output only. Identifies whether the user has requested
            cancellation of the operation. Operations that have been
            cancelled successfully have
            [google.longrunning.Operation.error][google.longrunning.Operation.error]
            value with a
            [google.rpc.Status.code][google.rpc.Status.code] of ``1``,
            corresponding to ``Code.CANCELLED``.
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
    status_message: str = proto.Field(
        proto.STRING,
        number=3,
    )
    requested_cancellation: bool = proto.Field(
        proto.BOOL,
        number=4,
    )


class ListExamplesRequest(proto.Message):
    r"""Request message for
    [AgentService.ListExamples][google.cloud.ces.v1.AgentService.ListExamples].

    Attributes:
        parent (str):
            Required. The resource name of the app to
            list examples from.
        page_size (int):
            Optional. Requested page size. Server may
            return fewer items than requested. If
            unspecified, server will pick an appropriate
            default.
        page_token (str):
            Optional. The
            [next_page_token][google.cloud.ces.v1.ListExamplesResponse.next_page_token]
            value returned from a previous list
            [AgentService.ListExamples][google.cloud.ces.v1.AgentService.ListExamples]
            call.
        filter (str):
            Optional. Filter to be applied when listing
            the examples. See https://google.aip.dev/160 for
            more details.
        order_by (str):
            Optional. Field to sort by. Only "name" and "create_time" is
            supported. See https://google.aip.dev/132#ordering for more
            details.
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


class ListExamplesResponse(proto.Message):
    r"""Response message for
    [AgentService.ListExamples][google.cloud.ces.v1.AgentService.ListExamples].

    Attributes:
        examples (MutableSequence[google.cloud.ces_v1.types.Example]):
            The list of examples.
        next_page_token (str):
            A token that can be sent as
            [ListExamplesRequest.page_token][google.cloud.ces.v1.ListExamplesRequest.page_token]
            to retrieve the next page. Absence of this field indicates
            there are no subsequent pages.
    """

    @property
    def raw_page(self):
        return self

    examples: MutableSequence[gcc_example.Example] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=gcc_example.Example,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetExampleRequest(proto.Message):
    r"""Request message for
    [AgentService.GetExample][google.cloud.ces.v1.AgentService.GetExample].

    Attributes:
        name (str):
            Required. The resource name of the example to
            retrieve.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateExampleRequest(proto.Message):
    r"""Request message for
    [AgentService.CreateExample][google.cloud.ces.v1.AgentService.CreateExample].

    Attributes:
        parent (str):
            Required. The resource name of the app to
            create an example in.
        example_id (str):
            Optional. The ID to use for the example,
            which will become the final component of the
            example's resource name. If not provided, a
            unique ID will be automatically assigned for the
            example.
        example (google.cloud.ces_v1.types.Example):
            Required. The example to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    example_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    example: gcc_example.Example = proto.Field(
        proto.MESSAGE,
        number=3,
        message=gcc_example.Example,
    )


class UpdateExampleRequest(proto.Message):
    r"""Request message for
    [AgentService.UpdateExample][google.cloud.ces.v1.AgentService.UpdateExample].

    Attributes:
        example (google.cloud.ces_v1.types.Example):
            Required. The example to update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. Field mask is used to control which
            fields get updated. If the mask is not present,
            all fields will be updated.
    """

    example: gcc_example.Example = proto.Field(
        proto.MESSAGE,
        number=1,
        message=gcc_example.Example,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class DeleteExampleRequest(proto.Message):
    r"""Request message for
    [AgentService.DeleteExample][google.cloud.ces.v1.AgentService.DeleteExample].

    Attributes:
        name (str):
            Required. The resource name of the example to
            delete.
        etag (str):
            Optional. The current etag of the example. If
            an etag is not provided, the deletion will
            overwrite any concurrent changes. If an etag is
            provided and does not match the current etag of
            the example, deletion will be blocked and an
            ABORTED error will be returned.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ListToolsRequest(proto.Message):
    r"""Request message for
    [AgentService.ListTools][google.cloud.ces.v1.AgentService.ListTools].

    Attributes:
        parent (str):
            Required. The resource name of the app to
            list tools from.
        page_size (int):
            Optional. Requested page size. Server may
            return fewer items than requested. If
            unspecified, server will pick an appropriate
            default.
        page_token (str):
            Optional. The
            [next_page_token][google.cloud.ces.v1.ListToolsResponse.next_page_token]
            value returned from a previous list
            [AgentService.ListTools][google.cloud.ces.v1.AgentService.ListTools]
            call.
        filter (str):
            Optional. Filter to be applied when listing the tools. Use
            "include_system_tools=true" to include system tools in the
            response. See https://google.aip.dev/160 for more details.
        order_by (str):
            Optional. Field to sort by. Only "name" and "create_time" is
            supported. See https://google.aip.dev/132#ordering for more
            details.
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


class ListToolsResponse(proto.Message):
    r"""Response message for
    [AgentService.ListTools][google.cloud.ces.v1.AgentService.ListTools].

    Attributes:
        tools (MutableSequence[google.cloud.ces_v1.types.Tool]):
            The list of tools.
        next_page_token (str):
            A token that can be sent as
            [ListToolsRequest.page_token][google.cloud.ces.v1.ListToolsRequest.page_token]
            to retrieve the next page. Absence of this field indicates
            there are no subsequent pages.
    """

    @property
    def raw_page(self):
        return self

    tools: MutableSequence[gcc_tool.Tool] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=gcc_tool.Tool,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetToolRequest(proto.Message):
    r"""Request message for
    [AgentService.GetTool][google.cloud.ces.v1.AgentService.GetTool].

    Attributes:
        name (str):
            Required. The resource name of the tool to
            retrieve.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateToolRequest(proto.Message):
    r"""Request message for
    [AgentService.CreateTool][google.cloud.ces.v1.AgentService.CreateTool].

    Attributes:
        parent (str):
            Required. The resource name of the app to
            create a tool in.
        tool_id (str):
            Optional. The ID to use for the tool, which
            will become the final component of the tool's
            resource name. If not provided, a unique ID will
            be automatically assigned for the tool.
        tool (google.cloud.ces_v1.types.Tool):
            Required. The tool to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    tool_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    tool: gcc_tool.Tool = proto.Field(
        proto.MESSAGE,
        number=3,
        message=gcc_tool.Tool,
    )


class UpdateToolRequest(proto.Message):
    r"""Request message for
    [AgentService.UpdateTool][google.cloud.ces.v1.AgentService.UpdateTool].

    Attributes:
        tool (google.cloud.ces_v1.types.Tool):
            Required. The tool to update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. Field mask is used to control which
            fields get updated. If the mask is not present,
            all fields will be updated.
    """

    tool: gcc_tool.Tool = proto.Field(
        proto.MESSAGE,
        number=1,
        message=gcc_tool.Tool,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class DeleteToolRequest(proto.Message):
    r"""Request message for
    [AgentService.DeleteTool][google.cloud.ces.v1.AgentService.DeleteTool].

    Attributes:
        name (str):
            Required. The resource name of the tool to
            delete.
        force (bool):
            Optional. Indicates whether to forcefully delete the tool,
            even if it is still referenced by agents/examples.

            - If ``force = false``, the deletion will fail if any agents
              still reference the tool.
            - If ``force = true``, all existing references from agents
              will be removed and the tool will be deleted.
        etag (str):
            Optional. The current etag of the tool. If an
            etag is not provided, the deletion will
            overwrite any concurrent changes. If an etag is
            provided and does not match the current etag of
            the tool, deletion will be blocked and an
            ABORTED error will be returned.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    force: bool = proto.Field(
        proto.BOOL,
        number=2,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ListConversationsRequest(proto.Message):
    r"""Request message for
    [AgentService.ListConversations][google.cloud.ces.v1.AgentService.ListConversations].

    Attributes:
        parent (str):
            Required. The resource name of the app to
            list conversations from.
        page_size (int):
            Optional. Requested page size. Server may
            return fewer items than requested. If
            unspecified, server will pick an appropriate
            default.
        page_token (str):
            Optional. The
            [next_page_token][google.cloud.ces.v1.ListConversationsResponse.next_page_token]
            value returned from a previous list
            [AgentService.ListConversations][google.cloud.ces.v1.AgentService.ListConversations]
            call.
        filter (str):
            Optional. Filter to be applied when listing
            the conversations. See
            https://google.aip.dev/160 for more details.
        source (google.cloud.ces_v1.types.Conversation.Source):
            Optional. Indicate the source of the conversation. If not
            set, Source.Live will be applied by default. Will be
            deprecated in favor of ``sources`` field.
        sources (MutableSequence[google.cloud.ces_v1.types.Conversation.Source]):
            Optional. Indicate the sources of the
            conversations. If not set, all available sources
            will be applied by default.
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
    source: conversation.Conversation.Source = proto.Field(
        proto.ENUM,
        number=5,
        enum=conversation.Conversation.Source,
    )
    sources: MutableSequence[conversation.Conversation.Source] = proto.RepeatedField(
        proto.ENUM,
        number=6,
        enum=conversation.Conversation.Source,
    )


class ListConversationsResponse(proto.Message):
    r"""Response message for
    [AgentService.ListConversations][google.cloud.ces.v1.AgentService.ListConversations].

    Attributes:
        conversations (MutableSequence[google.cloud.ces_v1.types.Conversation]):
            The list of conversations.
        next_page_token (str):
            A token that can be sent as
            [ListConversationsRequest.page_token][google.cloud.ces.v1.ListConversationsRequest.page_token]
            to retrieve the next page. Absence of this field indicates
            there are no subsequent pages.
    """

    @property
    def raw_page(self):
        return self

    conversations: MutableSequence[conversation.Conversation] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=conversation.Conversation,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetConversationRequest(proto.Message):
    r"""Request message for
    [AgentService.GetConversation][google.cloud.ces.v1.AgentService.GetConversation].

    Attributes:
        name (str):
            Required. The resource name of the
            conversation to retrieve.
        source (google.cloud.ces_v1.types.Conversation.Source):
            Optional. Indicate the source of the
            conversation. If not set, all source will be
            searched.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    source: conversation.Conversation.Source = proto.Field(
        proto.ENUM,
        number=2,
        enum=conversation.Conversation.Source,
    )


class DeleteConversationRequest(proto.Message):
    r"""Request message for
    [AgentService.DeleteConversation][google.cloud.ces.v1.AgentService.DeleteConversation].

    Attributes:
        name (str):
            Required. The resource name of the
            conversation to delete.
        source (google.cloud.ces_v1.types.Conversation.Source):
            Optional. Indicate the source of the
            conversation. If not set, Source.Live will be
            applied by default.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    source: conversation.Conversation.Source = proto.Field(
        proto.ENUM,
        number=2,
        enum=conversation.Conversation.Source,
    )


class BatchDeleteConversationsRequest(proto.Message):
    r"""Request message for
    [AgentService.BatchDeleteConversations][google.cloud.ces.v1.AgentService.BatchDeleteConversations].

    Attributes:
        parent (str):
            Required. The resource name of the app to delete
            conversations from. Format:
            ``projects/{project}/locations/{location}/apps/{app}``
        conversations (MutableSequence[str]):
            Required. The resource names of the
            conversations to delete.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    conversations: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class BatchDeleteConversationsResponse(proto.Message):
    r"""Response message for
    [AgentService.BatchDeleteConversations][google.cloud.ces.v1.AgentService.BatchDeleteConversations].

    Attributes:
        deleted_conversations (MutableSequence[str]):
            The list of conversations that were
            successfully deleted.
        failed_conversations (MutableSequence[str]):
            The list of conversations that failed to be
            deleted.
        error_messages (MutableSequence[str]):
            Optional. A list of error messages associated
            with conversations that failed to be deleted.
    """

    deleted_conversations: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )
    failed_conversations: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )
    error_messages: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class ListGuardrailsRequest(proto.Message):
    r"""Request message for
    [AgentService.ListGuardrails][google.cloud.ces.v1.AgentService.ListGuardrails].

    Attributes:
        parent (str):
            Required. The resource name of the app to
            list guardrails from.
        page_size (int):
            Optional. Requested page size. Server may
            return fewer items than requested. If
            unspecified, server will pick an appropriate
            default.
        page_token (str):
            Optional. The
            [next_page_token][google.cloud.ces.v1.ListGuardrailsResponse.next_page_token]
            value returned from a previous list
            [AgentService.ListGuardrails][google.cloud.ces.v1.AgentService.ListGuardrails]
            call.
        filter (str):
            Optional. Filter to be applied when listing
            the guardrails. See https://google.aip.dev/160
            for more details.
        order_by (str):
            Optional. Field to sort by. Only "name" and "create_time" is
            supported. See https://google.aip.dev/132#ordering for more
            details.
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


class ListGuardrailsResponse(proto.Message):
    r"""Response message for
    [AgentService.ListGuardrails][google.cloud.ces.v1.AgentService.ListGuardrails].

    Attributes:
        guardrails (MutableSequence[google.cloud.ces_v1.types.Guardrail]):
            The list of guardrails.
        next_page_token (str):
            A token that can be sent as
            [ListGuardrailsRequest.page_token][google.cloud.ces.v1.ListGuardrailsRequest.page_token]
            to retrieve the next page. Absence of this field indicates
            there are no subsequent pages.
    """

    @property
    def raw_page(self):
        return self

    guardrails: MutableSequence[gcc_guardrail.Guardrail] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=gcc_guardrail.Guardrail,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetGuardrailRequest(proto.Message):
    r"""Request message for
    [AgentService.GetGuardrail][google.cloud.ces.v1.AgentService.GetGuardrail].

    Attributes:
        name (str):
            Required. The resource name of the guardrail
            to retrieve.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateGuardrailRequest(proto.Message):
    r"""Request message for
    [AgentService.CreateGuardrail][google.cloud.ces.v1.AgentService.CreateGuardrail].

    Attributes:
        parent (str):
            Required. The resource name of the app to
            create a guardrail in.
        guardrail_id (str):
            Optional. The ID to use for the guardrail,
            which will become the final component of the
            guardrail's resource name. If not provided, a
            unique ID will be automatically assigned for the
            guardrail.
        guardrail (google.cloud.ces_v1.types.Guardrail):
            Required. The guardrail to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    guardrail_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    guardrail: gcc_guardrail.Guardrail = proto.Field(
        proto.MESSAGE,
        number=3,
        message=gcc_guardrail.Guardrail,
    )


class UpdateGuardrailRequest(proto.Message):
    r"""Request message for
    [AgentService.UpdateGuardrail][google.cloud.ces.v1.AgentService.UpdateGuardrail].

    Attributes:
        guardrail (google.cloud.ces_v1.types.Guardrail):
            Required. The guardrail to update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. Field mask is used to control which
            fields get updated. If the mask is not present,
            all fields will be updated.
    """

    guardrail: gcc_guardrail.Guardrail = proto.Field(
        proto.MESSAGE,
        number=1,
        message=gcc_guardrail.Guardrail,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class DeleteGuardrailRequest(proto.Message):
    r"""Request message for
    [AgentService.DeleteGuardrail][google.cloud.ces.v1.AgentService.DeleteGuardrail].

    Attributes:
        name (str):
            Required. The resource name of the guardrail
            to delete.
        force (bool):
            Optional. Indicates whether to forcefully delete the
            guardrail, even if it is still referenced by app/agents.

            - If ``force = false``, the deletion fails if any
              apps/agents still reference the guardrail.
            - If ``force = true``, all existing references from
              apps/agents will be removed and the guardrail will be
              deleted.
        etag (str):
            Optional. The current etag of the guardrail.
            If an etag is not provided, the deletion will
            overwrite any concurrent changes. If an etag is
            provided and does not match the current etag of
            the guardrail, deletion will be blocked and an
            ABORTED error will be returned.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    force: bool = proto.Field(
        proto.BOOL,
        number=2,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ListDeploymentsRequest(proto.Message):
    r"""Request message for
    [AgentService.ListDeployments][google.cloud.ces.v1.AgentService.ListDeployments].

    Attributes:
        parent (str):
            Required. The parent app. Format:
            ``projects/{project}/locations/{location}/apps/{app}``
        page_size (int):
            Optional. The maximum number of deployments
            to return. The service may return fewer than
            this value. If unspecified, at most 50
            deployments will be returned. The maximum value
            is 1000; values above 1000 will be coerced to
            1000.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListDeployments`` call. Provide this to retrieve the
            subsequent page.

            When paginating, all other parameters provided to
            ``ListDeployments`` must match the call that provided the
            page token.
        order_by (str):
            Optional. Field to sort by. Only "name" and "create_time" is
            supported. See https://google.aip.dev/132#ordering for more
            details.
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
    order_by: str = proto.Field(
        proto.STRING,
        number=4,
    )


class ListDeploymentsResponse(proto.Message):
    r"""Response message for
    [AgentService.ListDeployments][google.cloud.ces.v1.AgentService.ListDeployments].

    Attributes:
        deployments (MutableSequence[google.cloud.ces_v1.types.Deployment]):
            The list of deployments.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    deployments: MutableSequence[gcc_deployment.Deployment] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=gcc_deployment.Deployment,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetDeploymentRequest(proto.Message):
    r"""Request message for
    [AgentService.GetDeployment][google.cloud.ces.v1.AgentService.GetDeployment].

    Attributes:
        name (str):
            Required. The name of the deployment. Format:
            ``projects/{project}/locations/{location}/apps/{app}/deployments/{deployment}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateDeploymentRequest(proto.Message):
    r"""Request message for
    [AgentService.CreateDeployment][google.cloud.ces.v1.AgentService.CreateDeployment].

    Attributes:
        parent (str):
            Required. The parent app. Format:
            ``projects/{project}/locations/{location}/apps/{app}``
        deployment_id (str):
            Optional. The ID to use for the deployment,
            which will become the final component of the
            deployment's resource name. If not provided, a
            unique ID will be automatically assigned for the
            deployment.
        deployment (google.cloud.ces_v1.types.Deployment):
            Required. The deployment to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    deployment_id: str = proto.Field(
        proto.STRING,
        number=3,
    )
    deployment: gcc_deployment.Deployment = proto.Field(
        proto.MESSAGE,
        number=2,
        message=gcc_deployment.Deployment,
    )


class UpdateDeploymentRequest(proto.Message):
    r"""Request message for
    [AgentService.UpdateDeployment][google.cloud.ces.v1.AgentService.UpdateDeployment].

    Attributes:
        deployment (google.cloud.ces_v1.types.Deployment):
            Required. The deployment to update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. The list of fields to update.
    """

    deployment: gcc_deployment.Deployment = proto.Field(
        proto.MESSAGE,
        number=1,
        message=gcc_deployment.Deployment,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class DeleteDeploymentRequest(proto.Message):
    r"""Request message for
    [AgentService.DeleteDeployment][google.cloud.ces.v1.AgentService.DeleteDeployment].

    Attributes:
        name (str):
            Required. The name of the deployment to delete. Format:
            ``projects/{project}/locations/{location}/apps/{app}/deployments/{deployment}``
        etag (str):
            Optional. The etag of the deployment.
            If an etag is provided and does not match the
            current etag of the deployment, deletion will be
            blocked and an ABORTED error will be returned.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ListToolsetsRequest(proto.Message):
    r"""Request message for
    [AgentService.ListToolsets][google.cloud.ces.v1.AgentService.ListToolsets].

    Attributes:
        parent (str):
            Required. The resource name of the app to
            list toolsets from.
        page_size (int):
            Optional. Requested page size. Server may
            return fewer items than requested. If
            unspecified, server will pick an appropriate
            default.
        page_token (str):
            Optional. The
            [next_page_token][google.cloud.ces.v1.ListToolsetsResponse.next_page_token]
            value returned from a previous list
            [AgentService.ListToolsets][google.cloud.ces.v1.AgentService.ListToolsets]
            call.
        filter (str):
            Optional. Filter to be applied when listing
            the toolsets. See https://google.aip.dev/160 for
            more details.
        order_by (str):
            Optional. Field to sort by. Only "name" and "create_time" is
            supported. See https://google.aip.dev/132#ordering for more
            details.
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


class ListToolsetsResponse(proto.Message):
    r"""Response message for
    [AgentService.ListToolsets][google.cloud.ces.v1.AgentService.ListToolsets].

    Attributes:
        toolsets (MutableSequence[google.cloud.ces_v1.types.Toolset]):
            The list of toolsets.
        next_page_token (str):
            A token that can be sent as
            [ListToolsetsRequest.page_token][google.cloud.ces.v1.ListToolsetsRequest.page_token]
            to retrieve the next page. Absence of this field indicates
            there are no subsequent pages.
    """

    @property
    def raw_page(self):
        return self

    toolsets: MutableSequence[gcc_toolset.Toolset] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=gcc_toolset.Toolset,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetToolsetRequest(proto.Message):
    r"""Request message for
    [AgentService.GetToolset][google.cloud.ces.v1.AgentService.GetToolset].

    Attributes:
        name (str):
            Required. The resource name of the toolset to
            retrieve.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateToolsetRequest(proto.Message):
    r"""Request message for
    [AgentService.CreateToolset][google.cloud.ces.v1.AgentService.CreateToolset].

    Attributes:
        parent (str):
            Required. The resource name of the app to
            create a toolset in.
        toolset_id (str):
            Optional. The ID to use for the toolset,
            which will become the final component of the
            toolset's resource name. If not provided, a
            unique ID will be automatically assigned for the
            toolset.
        toolset (google.cloud.ces_v1.types.Toolset):
            Required. The toolset to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    toolset_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    toolset: gcc_toolset.Toolset = proto.Field(
        proto.MESSAGE,
        number=3,
        message=gcc_toolset.Toolset,
    )


class UpdateToolsetRequest(proto.Message):
    r"""Request message for
    [AgentService.UpdateToolset][google.cloud.ces.v1.AgentService.UpdateToolset].

    Attributes:
        toolset (google.cloud.ces_v1.types.Toolset):
            Required. The toolset to update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. Field mask is used to control which
            fields get updated. If the mask is not present,
            all fields will be updated.
    """

    toolset: gcc_toolset.Toolset = proto.Field(
        proto.MESSAGE,
        number=1,
        message=gcc_toolset.Toolset,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class DeleteToolsetRequest(proto.Message):
    r"""Request message for
    [AgentService.DeleteToolset][google.cloud.ces.v1.AgentService.DeleteToolset].

    Attributes:
        name (str):
            Required. The resource name of the toolset to
            delete.
        force (bool):
            Optional. Indicates whether to forcefully delete the
            toolset, even if it is still referenced by app/agents.

            - If ``force = false``, the deletion fails if any agents
              still reference the toolset.
            - If ``force = true``, all existing references from agents
              will be removed and the toolset will be deleted.
        etag (str):
            Optional. The current etag of the toolset. If
            an etag is not provided, the deletion will
            overwrite any concurrent changes. If an etag is
            provided and does not match the current etag of
            the toolset, deletion will be blocked and an
            ABORTED error will be returned.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    force: bool = proto.Field(
        proto.BOOL,
        number=2,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ListAppVersionsRequest(proto.Message):
    r"""Request message for
    [AgentService.ListAppVersions][google.cloud.ces.v1.AgentService.ListAppVersions].

    Attributes:
        parent (str):
            Required. The resource name of the app to
            list app versions from.
        page_size (int):
            Optional. Requested page size. Server may
            return fewer items than requested. If
            unspecified, server will pick an appropriate
            default.
        page_token (str):
            Optional. The
            [next_page_token][google.cloud.ces.v1.ListAppVersionsResponse.next_page_token]
            value returned from a previous list
            [AgentService.ListAppVersions][google.cloud.ces.v1.AgentService.ListAppVersions]
            call.
        filter (str):
            Optional. Filter to be applied when listing
            the app versions. See https://google.aip.dev/160
            for more details.
        order_by (str):
            Optional. Field to sort by. Only "name" and "create_time" is
            supported. See https://google.aip.dev/132#ordering for more
            details.
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


class ListAppVersionsResponse(proto.Message):
    r"""Response message for
    [AgentService.ListAppVersions][google.cloud.ces.v1.AgentService.ListAppVersions].

    Attributes:
        app_versions (MutableSequence[google.cloud.ces_v1.types.AppVersion]):
            The list of app versions.
        next_page_token (str):
            A token that can be sent as
            [ListAppVersionsRequest.page_token][google.cloud.ces.v1.ListAppVersionsRequest.page_token]
            to retrieve the next page. Absence of this field indicates
            there are no subsequent pages.
    """

    @property
    def raw_page(self):
        return self

    app_versions: MutableSequence[gcc_app_version.AppVersion] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=gcc_app_version.AppVersion,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetAppVersionRequest(proto.Message):
    r"""Request message for
    [AgentService.GetAppVersion][google.cloud.ces.v1.AgentService.GetAppVersion].

    Attributes:
        name (str):
            Required. The resource name of the app
            version to retrieve.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class DeleteAppVersionRequest(proto.Message):
    r"""Request message for
    [AgentService.DeleteAppVersion][google.cloud.ces.v1.AgentService.DeleteAppVersion].

    Attributes:
        name (str):
            Required. The resource name of the app
            version to delete.
        etag (str):
            Optional. The current etag of the app
            version. If an etag is not provided, the
            deletion will overwrite any concurrent changes.
            If an etag is provided and does not match the
            current etag of the app version, deletion will
            be blocked and an ABORTED error will be
            returned.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=2,
    )


class CreateAppVersionRequest(proto.Message):
    r"""Request message for
    [AgentService.CreateAppVersion][google.cloud.ces.v1.AgentService.CreateAppVersion]

    Attributes:
        parent (str):
            Required. The resource name of the app to
            create an app version in.
        app_version_id (str):
            Optional. The ID to use for the app version,
            which will become the final component of the app
            version's resource name. If not provided, a
            unique ID will be automatically assigned for the
            app version.
        app_version (google.cloud.ces_v1.types.AppVersion):
            Required. The app version to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    app_version_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    app_version: gcc_app_version.AppVersion = proto.Field(
        proto.MESSAGE,
        number=3,
        message=gcc_app_version.AppVersion,
    )


class RestoreAppVersionRequest(proto.Message):
    r"""Request message for
    [AgentService.RestoreAppVersion][google.cloud.ces.v1.AgentService.RestoreAppVersion]

    Attributes:
        name (str):
            Required. The resource name of the app
            version to restore.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class RestoreAppVersionResponse(proto.Message):
    r"""Response message for
    [AgentService.RestoreAppVersion][google.cloud.ces.v1.AgentService.RestoreAppVersion]

    """


class ListChangelogsRequest(proto.Message):
    r"""Request message for
    [AgentService.ListChangelogs][google.cloud.ces.v1.AgentService.ListChangelogs].

    Attributes:
        parent (str):
            Required. The resource name of the app to
            list changelogs from.
        page_size (int):
            Optional. Requested page size. Server may
            return fewer items than requested. If
            unspecified, server will pick an appropriate
            default.
        page_token (str):
            Optional. The
            [next_page_token][google.cloud.ces.v1.ListChangelogsResponse.next_page_token]
            value returned from a previous list
            [AgentService.ListChangelogs][google.cloud.ces.v1.AgentService.ListChangelogs]
            call.
        filter (str):
            Optional. Filter to be applied when listing the changelogs.
            See https://google.aip.dev/160 for more details.

            The filter string can be used to filter by ``action``,
            ``resource_type``, ``resource_name``, ``author``, and
            ``create_time``. The ``:`` comparator can be used for
            case-insensitive partial matching on string fields, while
            ``=`` performs an exact case-sensitive match.

            Examples:

            - ``action:update`` (case-insensitive partial match)
            - ``action="Create"`` (case-sensitive exact match)
            - ``resource_type:agent``
            - ``resource_name:my-agent``
            - ``author:me@example.com``
            - ``create_time > "2025-01-01T00:00:00Z"``
            - ``create_time <= "2025-01-01T00:00:00Z" AND resource_type:tool``
        order_by (str):
            Optional. Field to sort by. Only "name" and "create_time" is
            supported. See https://google.aip.dev/132#ordering for more
            details.
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


class ListChangelogsResponse(proto.Message):
    r"""Response message for
    [AgentService.ListChangelogs][google.cloud.ces.v1.AgentService.ListChangelogs].

    Attributes:
        changelogs (MutableSequence[google.cloud.ces_v1.types.Changelog]):
            The list of changelogs.
        next_page_token (str):
            A token that can be sent as
            [ListChangelogsRequest.page_token][google.cloud.ces.v1.ListChangelogsRequest.page_token]
            to retrieve the next page. Absence of this field indicates
            there are no subsequent pages.
    """

    @property
    def raw_page(self):
        return self

    changelogs: MutableSequence[changelog.Changelog] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=changelog.Changelog,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetChangelogRequest(proto.Message):
    r"""Request message for
    [AgentService.GetChangelog][google.cloud.ces.v1.AgentService.GetChangelog].

    Attributes:
        name (str):
            Required. The resource name of the changelog
            to retrieve.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
