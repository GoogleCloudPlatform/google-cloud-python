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

from google.cloud.dialogflowcx_v3beta1.types import data_store_connection, inline

__protobuf__ = proto.module(
    package="google.cloud.dialogflow.cx.v3beta1",
    manifest={
        "CreateToolRequest",
        "ListToolsRequest",
        "ListToolsResponse",
        "GetToolRequest",
        "ExportToolsRequest",
        "ExportToolsResponse",
        "UpdateToolRequest",
        "DeleteToolRequest",
        "Tool",
        "ListToolVersionsRequest",
        "ListToolVersionsResponse",
        "CreateToolVersionRequest",
        "GetToolVersionRequest",
        "DeleteToolVersionRequest",
        "RestoreToolVersionRequest",
        "RestoreToolVersionResponse",
        "ToolVersion",
        "ExportToolsMetadata",
    },
)


class CreateToolRequest(proto.Message):
    r"""The request message for
    [Tools.CreateTool][google.cloud.dialogflow.cx.v3beta1.Tools.CreateTool].

    Attributes:
        parent (str):
            Required. The agent to create a Tool for. Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>``.
        tool (google.cloud.dialogflowcx_v3beta1.types.Tool):
            Required. The Tool to be created.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    tool: "Tool" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Tool",
    )


class ListToolsRequest(proto.Message):
    r"""The request message for
    [Tools.ListTools][google.cloud.dialogflow.cx.v3beta1.Tools.ListTools].

    Attributes:
        parent (str):
            Required. The agent to list the Tools from. Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>``.
        page_size (int):
            The maximum number of items to return in a
            single page. By default 100 and at most 1000.
        page_token (str):
            The next_page_token value returned from a previous list
            request.
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


class ListToolsResponse(proto.Message):
    r"""The response message for
    [Tools.ListTools][google.cloud.dialogflow.cx.v3beta1.Tools.ListTools].

    Attributes:
        tools (MutableSequence[google.cloud.dialogflowcx_v3beta1.types.Tool]):
            The list of Tools. There will be a maximum number of items
            returned based on the page_size field in the request.
        next_page_token (str):
            Token to retrieve the next page of results,
            or empty if there are no more results in the
            list.
    """

    @property
    def raw_page(self):
        return self

    tools: MutableSequence["Tool"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Tool",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetToolRequest(proto.Message):
    r"""The request message for
    [Tools.GetTool][google.cloud.dialogflow.cx.v3beta1.Tools.GetTool].

    Attributes:
        name (str):
            Required. The name of the Tool. Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/tools/<ToolID>``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ExportToolsRequest(proto.Message):
    r"""The request message for
    [Tools.ExportTools][google.cloud.dialogflow.cx.v3beta1.Tools.ExportTools].

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        parent (str):
            Required. The agent to export tools from. Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>``.
        tools (MutableSequence[str]):
            Required. The name of the tools to export. Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/tools/<ToolID>``.
        tools_uri (str):
            Optional. The `Google Cloud
            Storage <https://cloud.google.com/storage/docs/>`__ URI to
            export the tools to. The format of this URI must be
            ``gs://<bucket-name>/<object-name>``.

            Dialogflow performs a write operation for the Cloud Storage
            object on the caller's behalf, so your request
            authentication must have write permissions for the object.
            For more information, see `Dialogflow access
            control <https://cloud.google.com/dialogflow/cx/docs/concept/access-control#storage>`__.

            This field is a member of `oneof`_ ``destination``.
        tools_content_inline (bool):
            Optional. The option to return the serialized
            tools inline.

            This field is a member of `oneof`_ ``destination``.
        data_format (google.cloud.dialogflowcx_v3beta1.types.ExportToolsRequest.DataFormat):
            Optional. The data format of the exported tools. If not
            specified, ``BLOB`` is assumed.
    """

    class DataFormat(proto.Enum):
        r"""Data format of the exported tools.

        Values:
            DATA_FORMAT_UNSPECIFIED (0):
                Unspecified format. Treated as ``BLOB``.
            BLOB (1):
                Tools will be exported as raw bytes.
        """

        DATA_FORMAT_UNSPECIFIED = 0
        BLOB = 1

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    tools: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )
    tools_uri: str = proto.Field(
        proto.STRING,
        number=3,
        oneof="destination",
    )
    tools_content_inline: bool = proto.Field(
        proto.BOOL,
        number=4,
        oneof="destination",
    )
    data_format: DataFormat = proto.Field(
        proto.ENUM,
        number=5,
        enum=DataFormat,
    )


class ExportToolsResponse(proto.Message):
    r"""The response message for
    [Tools.ExportTools][google.cloud.dialogflow.cx.v3beta1.Tools.ExportTools].

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        tools_uri (str):
            The URI to a file containing the exported tools. This field
            is populated only if ``tools_uri`` is specified in
            [ExportToolsRequest][google.cloud.dialogflow.cx.v3beta1.ExportToolsRequest].

            This field is a member of `oneof`_ ``tools``.
        tools_content (google.cloud.dialogflowcx_v3beta1.types.InlineDestination):
            Uncompressed byte content for tools. This field is populated
            only if ``tools_content_inline`` is set to true in
            [ExportToolsRequest][google.cloud.dialogflow.cx.v3beta1.ExportToolsRequest].

            This field is a member of `oneof`_ ``tools``.
    """

    tools_uri: str = proto.Field(
        proto.STRING,
        number=1,
        oneof="tools",
    )
    tools_content: inline.InlineDestination = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="tools",
        message=inline.InlineDestination,
    )


class UpdateToolRequest(proto.Message):
    r"""The request message for
    [Tools.UpdateTool][google.cloud.dialogflow.cx.v3beta1.Tools.UpdateTool].

    Attributes:
        tool (google.cloud.dialogflowcx_v3beta1.types.Tool):
            Required. The Tool to be updated.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            The mask to control which fields get updated.
            If the mask is not present, all fields will be
            updated.
    """

    tool: "Tool" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Tool",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class DeleteToolRequest(proto.Message):
    r"""The request message for
    [Tools.DeleteTool][google.cloud.dialogflow.cx.v3beta1.Tools.DeleteTool].

    Attributes:
        name (str):
            Required. The name of the Tool to be deleted. Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/tools/<ToolID>``.
        force (bool):
            This field has no effect for Tools not being used. For Tools
            that are used:

            - If ``force`` is set to false, an error will be returned
              with message indicating the referenced resources.
            - If ``force`` is set to true, Dialogflow will remove the
              tool, as well as any references to the tool.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    force: bool = proto.Field(
        proto.BOOL,
        number=2,
    )


class Tool(proto.Message):
    r"""A tool provides a list of actions which are available to the
    [Playbook][google.cloud.dialogflow.cx.v3beta1.Playbook] to attain
    its goal. A Tool consists of a description of the tool's usage and a
    specification of the tool which contains the schema and
    authentication information.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            The unique identifier of the Tool. Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/tools/<ToolID>``.
        display_name (str):
            Required. The human-readable name of the
            Tool, unique within an agent.
        description (str):
            Required. High level description of the Tool
            and its usage.
        open_api_spec (google.cloud.dialogflowcx_v3beta1.types.Tool.OpenApiTool):
            OpenAPI specification of the Tool.

            This field is a member of `oneof`_ ``specification``.
        data_store_spec (google.cloud.dialogflowcx_v3beta1.types.Tool.DataStoreTool):
            Data store search tool specification.

            This field is a member of `oneof`_ ``specification``.
        extension_spec (google.cloud.dialogflowcx_v3beta1.types.Tool.ExtensionTool):
            Vertex extension tool specification.

            This field is a member of `oneof`_ ``specification``.
        function_spec (google.cloud.dialogflowcx_v3beta1.types.Tool.FunctionTool):
            Client side executed function specification.

            This field is a member of `oneof`_ ``specification``.
        connector_spec (google.cloud.dialogflowcx_v3beta1.types.Tool.ConnectorTool):
            Integration connectors tool specification.

            This field is a member of `oneof`_ ``specification``.
        tool_type (google.cloud.dialogflowcx_v3beta1.types.Tool.ToolType):
            Output only. The tool type.
    """

    class ToolType(proto.Enum):
        r"""Represents the type of the tool.

        Values:
            TOOL_TYPE_UNSPECIFIED (0):
                Default value. This value is unused.
            CUSTOMIZED_TOOL (1):
                Customer provided tool.
            BUILTIN_TOOL (2):
                First party built-in tool created by
                Dialogflow which cannot be modified.
        """

        TOOL_TYPE_UNSPECIFIED = 0
        CUSTOMIZED_TOOL = 1
        BUILTIN_TOOL = 2

    class OpenApiTool(proto.Message):
        r"""An OpenAPI tool is a way to provide the Tool specifications
        in the Open API schema format.


        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            text_schema (str):
                Required. The OpenAPI schema specified as a
                text.

                This field is a member of `oneof`_ ``schema``.
            authentication (google.cloud.dialogflowcx_v3beta1.types.Tool.Authentication):
                Optional. Authentication information required
                by the API.
            tls_config (google.cloud.dialogflowcx_v3beta1.types.Tool.TLSConfig):
                Optional. TLS configuration for the HTTPS
                verification.
            service_directory_config (google.cloud.dialogflowcx_v3beta1.types.Tool.ServiceDirectoryConfig):
                Optional. Service Directory configuration.
        """

        text_schema: str = proto.Field(
            proto.STRING,
            number=1,
            oneof="schema",
        )
        authentication: "Tool.Authentication" = proto.Field(
            proto.MESSAGE,
            number=2,
            message="Tool.Authentication",
        )
        tls_config: "Tool.TLSConfig" = proto.Field(
            proto.MESSAGE,
            number=3,
            message="Tool.TLSConfig",
        )
        service_directory_config: "Tool.ServiceDirectoryConfig" = proto.Field(
            proto.MESSAGE,
            number=4,
            message="Tool.ServiceDirectoryConfig",
        )

    class DataStoreTool(proto.Message):
        r"""A DataStoreTool is a way to provide specifications needed to
        search a list of data stores.

        Attributes:
            data_store_connections (MutableSequence[google.cloud.dialogflowcx_v3beta1.types.DataStoreConnection]):
                Required. List of data stores to search.
            fallback_prompt (google.cloud.dialogflowcx_v3beta1.types.Tool.DataStoreTool.FallbackPrompt):
                Required. Fallback prompt configurations to
                use.
        """

        class FallbackPrompt(proto.Message):
            r"""A FallbackPrompt is a way to provide specifications for the
            Data Store fallback prompt when generating responses.

            """

        data_store_connections: MutableSequence[
            data_store_connection.DataStoreConnection
        ] = proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=data_store_connection.DataStoreConnection,
        )
        fallback_prompt: "Tool.DataStoreTool.FallbackPrompt" = proto.Field(
            proto.MESSAGE,
            number=3,
            message="Tool.DataStoreTool.FallbackPrompt",
        )

    class ExtensionTool(proto.Message):
        r"""An ExtensionTool is a way to use Vertex Extensions as a tool.

        Attributes:
            name (str):
                Required. The full name of the referenced vertex extension.
                Formats:
                ``projects/{project}/locations/{location}/extensions/{extension}``
        """

        name: str = proto.Field(
            proto.STRING,
            number=1,
        )

    class FunctionTool(proto.Message):
        r"""A Function tool describes the functions to be invoked on the
        client side.

        Attributes:
            input_schema (google.protobuf.struct_pb2.Struct):
                Optional. The JSON schema is encapsulated in a
                [google.protobuf.Struct][google.protobuf.Struct] to describe
                the input of the function. This input is a JSON object that
                contains the function's parameters as properties of the
                object.
            output_schema (google.protobuf.struct_pb2.Struct):
                Optional. The JSON schema is encapsulated in a
                [google.protobuf.Struct][google.protobuf.Struct] to describe
                the output of the function. This output is a JSON object
                that contains the function's parameters as properties of the
                object.
        """

        input_schema: struct_pb2.Struct = proto.Field(
            proto.MESSAGE,
            number=1,
            message=struct_pb2.Struct,
        )
        output_schema: struct_pb2.Struct = proto.Field(
            proto.MESSAGE,
            number=2,
            message=struct_pb2.Struct,
        )

    class ConnectorTool(proto.Message):
        r"""A ConnectorTool enabling using Integration Connectors
        Connections as tools.

        Attributes:
            name (str):
                Required. The full resource name of the referenced
                Integration Connectors Connection. Format:
                ``projects/*/locations/*/connections/*``
            actions (MutableSequence[google.cloud.dialogflowcx_v3beta1.types.Tool.ConnectorTool.Action]):
                Required. Actions for the tool to use.
            end_user_auth_config (google.cloud.dialogflowcx_v3beta1.types.Tool.EndUserAuthConfig):
                Optional. Integration Connectors end-user authentication
                configuration. If configured, the end-user authentication
                fields will be passed in the Integration Connectors API
                request and override the admin, default authentication
                configured for the Connection. **Note**: The Connection must
                have authentication override enabled in order to specify an
                EUC configuration here - otherwise, the ConnectorTool
                creation will fail. See:
                https://cloud.google.com/application-integration/docs/configure-connectors-task#configure-authentication-override
        """

        class Action(proto.Message):
            r"""Configuration of a Connection operation for the tool to use.

            This message has `oneof`_ fields (mutually exclusive fields).
            For each oneof, at most one member field can be set at the same time.
            Setting any member of the oneof automatically clears all other
            members.

            .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

            Attributes:
                connection_action_id (str):
                    ID of a Connection action for the tool to
                    use.

                    This field is a member of `oneof`_ ``action_spec``.
                entity_operation (google.cloud.dialogflowcx_v3beta1.types.Tool.ConnectorTool.Action.EntityOperation):
                    Entity operation configuration for the tool
                    to use.

                    This field is a member of `oneof`_ ``action_spec``.
                input_fields (MutableSequence[str]):
                    Optional. Entity fields to use as inputs for
                    the operation. If no fields are specified, all
                    fields of the Entity will be used.
                output_fields (MutableSequence[str]):
                    Optional. Entity fields to return from the
                    operation. If no fields are specified, all
                    fields of the Entity will be returned.
            """

            class EntityOperation(proto.Message):
                r"""Entity CRUD operation specification.

                Attributes:
                    entity_id (str):
                        Required. ID of the entity.
                    operation (google.cloud.dialogflowcx_v3beta1.types.Tool.ConnectorTool.Action.EntityOperation.OperationType):
                        Required. Operation to perform on the entity.
                """

                class OperationType(proto.Enum):
                    r"""The operation to perform on the entity.

                    Values:
                        OPERATION_TYPE_UNSPECIFIED (0):
                            Operation type unspecified. Invalid,
                            ConnectorTool create/update will fail.
                        LIST (1):
                            List operation.
                        GET (2):
                            Get operation.
                        CREATE (3):
                            Create operation.
                        UPDATE (4):
                            Update operation.
                        DELETE (5):
                            Delete operation.
                    """

                    OPERATION_TYPE_UNSPECIFIED = 0
                    LIST = 1
                    GET = 2
                    CREATE = 3
                    UPDATE = 4
                    DELETE = 5

                entity_id: str = proto.Field(
                    proto.STRING,
                    number=1,
                )
                operation: "Tool.ConnectorTool.Action.EntityOperation.OperationType" = (
                    proto.Field(
                        proto.ENUM,
                        number=2,
                        enum="Tool.ConnectorTool.Action.EntityOperation.OperationType",
                    )
                )

            connection_action_id: str = proto.Field(
                proto.STRING,
                number=4,
                oneof="action_spec",
            )
            entity_operation: "Tool.ConnectorTool.Action.EntityOperation" = proto.Field(
                proto.MESSAGE,
                number=5,
                oneof="action_spec",
                message="Tool.ConnectorTool.Action.EntityOperation",
            )
            input_fields: MutableSequence[str] = proto.RepeatedField(
                proto.STRING,
                number=2,
            )
            output_fields: MutableSequence[str] = proto.RepeatedField(
                proto.STRING,
                number=3,
            )

        name: str = proto.Field(
            proto.STRING,
            number=1,
        )
        actions: MutableSequence["Tool.ConnectorTool.Action"] = proto.RepeatedField(
            proto.MESSAGE,
            number=2,
            message="Tool.ConnectorTool.Action",
        )
        end_user_auth_config: "Tool.EndUserAuthConfig" = proto.Field(
            proto.MESSAGE,
            number=3,
            message="Tool.EndUserAuthConfig",
        )

    class Authentication(proto.Message):
        r"""Authentication information required for API calls

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            api_key_config (google.cloud.dialogflowcx_v3beta1.types.Tool.Authentication.ApiKeyConfig):
                Config for API key auth.

                This field is a member of `oneof`_ ``auth_config``.
            oauth_config (google.cloud.dialogflowcx_v3beta1.types.Tool.Authentication.OAuthConfig):
                Config for OAuth.

                This field is a member of `oneof`_ ``auth_config``.
            service_agent_auth_config (google.cloud.dialogflowcx_v3beta1.types.Tool.Authentication.ServiceAgentAuthConfig):
                Config for `Diglogflow service
                agent <https://cloud.google.com/iam/docs/service-agents#dialogflow-service-agent>`__
                auth.

                This field is a member of `oneof`_ ``auth_config``.
            bearer_token_config (google.cloud.dialogflowcx_v3beta1.types.Tool.Authentication.BearerTokenConfig):
                Config for bearer token auth.

                This field is a member of `oneof`_ ``auth_config``.
            service_account_auth_config (google.cloud.dialogflowcx_v3beta1.types.Tool.Authentication.ServiceAccountAuthConfig):
                Configuration for service account
                authentication.

                This field is a member of `oneof`_ ``auth_config``.
        """

        class RequestLocation(proto.Enum):
            r"""The location of the API key in the request.

            Values:
                REQUEST_LOCATION_UNSPECIFIED (0):
                    Default value. This value is unused.
                HEADER (1):
                    Represents the key in http header.
                QUERY_STRING (2):
                    Represents the key in query string.
            """

            REQUEST_LOCATION_UNSPECIFIED = 0
            HEADER = 1
            QUERY_STRING = 2

        class ApiKeyConfig(proto.Message):
            r"""Config for authentication with API key.

            Attributes:
                key_name (str):
                    Required. The parameter name or the header
                    name of the API key. E.g., If the API request is
                    "https://example.com/act?X-Api-Key=<API KEY>",
                    "X-Api-Key" would be the parameter name.
                api_key (str):
                    Optional. The API key. If the ``secret_version_for_api_key``
                    field is set, this field will be ignored.
                secret_version_for_api_key (str):
                    Optional. The name of the SecretManager secret version
                    resource storing the API key. If this field is set, the
                    ``api_key`` field will be ignored. Format:
                    ``projects/{project}/secrets/{secret}/versions/{version}``
                request_location (google.cloud.dialogflowcx_v3beta1.types.Tool.Authentication.RequestLocation):
                    Required. Key location in the request.
            """

            key_name: str = proto.Field(
                proto.STRING,
                number=1,
            )
            api_key: str = proto.Field(
                proto.STRING,
                number=2,
            )
            secret_version_for_api_key: str = proto.Field(
                proto.STRING,
                number=4,
            )
            request_location: "Tool.Authentication.RequestLocation" = proto.Field(
                proto.ENUM,
                number=3,
                enum="Tool.Authentication.RequestLocation",
            )

        class OAuthConfig(proto.Message):
            r"""Config for authentication with OAuth.

            Attributes:
                oauth_grant_type (google.cloud.dialogflowcx_v3beta1.types.Tool.Authentication.OAuthConfig.OauthGrantType):
                    Required. OAuth grant types.
                client_id (str):
                    Required. The client ID from the OAuth
                    provider.
                client_secret (str):
                    Optional. The client secret from the OAuth provider. If the
                    ``secret_version_for_client_secret`` field is set, this
                    field will be ignored.
                secret_version_for_client_secret (str):
                    Optional. The name of the SecretManager secret version
                    resource storing the client secret. If this field is set,
                    the ``client_secret`` field will be ignored. Format:
                    ``projects/{project}/secrets/{secret}/versions/{version}``
                token_endpoint (str):
                    Required. The token endpoint in the OAuth
                    provider to exchange for an access token.
                scopes (MutableSequence[str]):
                    Optional. The OAuth scopes to grant.
            """

            class OauthGrantType(proto.Enum):
                r"""OAuth grant types. Only `client credential
                grant <https://oauth.net/2/grant-types/client-credentials>`__ is
                supported.

                Values:
                    OAUTH_GRANT_TYPE_UNSPECIFIED (0):
                        Default value. This value is unused.
                    CLIENT_CREDENTIAL (1):
                        Represents the `client credential
                        flow <https://oauth.net/2/grant-types/client-credentials>`__.
                """

                OAUTH_GRANT_TYPE_UNSPECIFIED = 0
                CLIENT_CREDENTIAL = 1

            oauth_grant_type: "Tool.Authentication.OAuthConfig.OauthGrantType" = (
                proto.Field(
                    proto.ENUM,
                    number=1,
                    enum="Tool.Authentication.OAuthConfig.OauthGrantType",
                )
            )
            client_id: str = proto.Field(
                proto.STRING,
                number=2,
            )
            client_secret: str = proto.Field(
                proto.STRING,
                number=3,
            )
            secret_version_for_client_secret: str = proto.Field(
                proto.STRING,
                number=6,
            )
            token_endpoint: str = proto.Field(
                proto.STRING,
                number=4,
            )
            scopes: MutableSequence[str] = proto.RepeatedField(
                proto.STRING,
                number=5,
            )

        class ServiceAgentAuthConfig(proto.Message):
            r"""Config for auth using `Diglogflow service
            agent <https://cloud.google.com/iam/docs/service-agents#dialogflow-service-agent>`__.

            Attributes:
                service_agent_auth (google.cloud.dialogflowcx_v3beta1.types.Tool.Authentication.ServiceAgentAuthConfig.ServiceAgentAuth):
                    Optional. Indicate the auth token type generated from the
                    `Diglogflow service
                    agent <https://cloud.google.com/iam/docs/service-agents#dialogflow-service-agent>`__.
                    The generated token is sent in the Authorization header.
            """

            class ServiceAgentAuth(proto.Enum):
                r"""Indicate the auth token type generated from the `Diglogflow service
                agent <https://cloud.google.com/iam/docs/service-agents#dialogflow-service-agent>`__.

                Values:
                    SERVICE_AGENT_AUTH_UNSPECIFIED (0):
                        Service agent auth type unspecified. Default to ID_TOKEN.
                    ID_TOKEN (1):
                        Use `ID
                        token <https://cloud.google.com/docs/authentication/token-types#id>`__
                        generated from service agent. This can be used to access
                        Cloud Function and Cloud Run after you grant Invoker role to
                        ``service-<PROJECT-NUMBER>@gcp-sa-dialogflow.iam.gserviceaccount.com``.
                    ACCESS_TOKEN (2):
                        Use `access
                        token <https://cloud.google.com/docs/authentication/token-types#access>`__
                        generated from service agent. This can be used to access
                        other Google Cloud APIs after you grant required roles to
                        ``service-<PROJECT-NUMBER>@gcp-sa-dialogflow.iam.gserviceaccount.com``.
                """

                SERVICE_AGENT_AUTH_UNSPECIFIED = 0
                ID_TOKEN = 1
                ACCESS_TOKEN = 2

            service_agent_auth: "Tool.Authentication.ServiceAgentAuthConfig.ServiceAgentAuth" = proto.Field(
                proto.ENUM,
                number=1,
                enum="Tool.Authentication.ServiceAgentAuthConfig.ServiceAgentAuth",
            )

        class BearerTokenConfig(proto.Message):
            r"""Config for authentication using bearer token.

            Attributes:
                token (str):
                    Optional. The text token appended to the text ``Bearer`` to
                    the request Authorization header. `Session parameters
                    reference <https://cloud.google.com/dialogflow/cx/docs/concept/parameter#session-ref>`__
                    can be used to pass the token dynamically, e.g.
                    ``$session.params.parameter-id``.
                secret_version_for_token (str):
                    Optional. The name of the SecretManager secret version
                    resource storing the Bearer token. If this field is set, the
                    ``token`` field will be ignored. Format:
                    ``projects/{project}/secrets/{secret}/versions/{version}``
            """

            token: str = proto.Field(
                proto.STRING,
                number=1,
            )
            secret_version_for_token: str = proto.Field(
                proto.STRING,
                number=2,
            )

        class ServiceAccountAuthConfig(proto.Message):
            r"""Configuration for authentication using a service account.

            Attributes:
                service_account (str):
                    Required. The email address of the service account used to
                    authenticate the tool call. Dialogflow uses this service
                    account to exchange an access token and the access token is
                    then sent in the ``Authorization`` header of the tool
                    request.

                    The service account must have the
                    ``roles/iam.serviceAccountTokenCreator`` role granted to the
                    `Dialogflow service
                    agent <https://cloud.google.com/iam/docs/service-agents#dialogflow-service-agent>`__.
            """

            service_account: str = proto.Field(
                proto.STRING,
                number=1,
            )

        api_key_config: "Tool.Authentication.ApiKeyConfig" = proto.Field(
            proto.MESSAGE,
            number=1,
            oneof="auth_config",
            message="Tool.Authentication.ApiKeyConfig",
        )
        oauth_config: "Tool.Authentication.OAuthConfig" = proto.Field(
            proto.MESSAGE,
            number=2,
            oneof="auth_config",
            message="Tool.Authentication.OAuthConfig",
        )
        service_agent_auth_config: "Tool.Authentication.ServiceAgentAuthConfig" = (
            proto.Field(
                proto.MESSAGE,
                number=3,
                oneof="auth_config",
                message="Tool.Authentication.ServiceAgentAuthConfig",
            )
        )
        bearer_token_config: "Tool.Authentication.BearerTokenConfig" = proto.Field(
            proto.MESSAGE,
            number=4,
            oneof="auth_config",
            message="Tool.Authentication.BearerTokenConfig",
        )
        service_account_auth_config: "Tool.Authentication.ServiceAccountAuthConfig" = (
            proto.Field(
                proto.MESSAGE,
                number=5,
                oneof="auth_config",
                message="Tool.Authentication.ServiceAccountAuthConfig",
            )
        )

    class TLSConfig(proto.Message):
        r"""The TLS configuration.

        Attributes:
            ca_certs (MutableSequence[google.cloud.dialogflowcx_v3beta1.types.Tool.TLSConfig.CACert]):
                Required. Specifies a list of allowed custom
                CA certificates for HTTPS verification.
        """

        class CACert(proto.Message):
            r"""The CA certificate.

            Attributes:
                display_name (str):
                    Required. The name of the allowed custom CA
                    certificates. This can be used to disambiguate
                    the custom CA certificates.
                cert (bytes):
                    Required. The allowed custom CA certificates (in DER format)
                    for HTTPS verification. This overrides the default SSL trust
                    store. If this is empty or unspecified, Dialogflow will use
                    Google's default trust store to verify certificates. N.B.
                    Make sure the HTTPS server certificates are signed with
                    "subject alt name". For instance a certificate can be
                    self-signed using the following command:

                    ::

                          openssl x509 -req -days 200 -in example.com.csr \
                            -signkey example.com.key \
                            -out example.com.crt \
                            -extfile <(printf "\nsubjectAltName='DNS:www.example.com'")
            """

            display_name: str = proto.Field(
                proto.STRING,
                number=1,
            )
            cert: bytes = proto.Field(
                proto.BYTES,
                number=2,
            )

        ca_certs: MutableSequence["Tool.TLSConfig.CACert"] = proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="Tool.TLSConfig.CACert",
        )

    class ServiceDirectoryConfig(proto.Message):
        r"""Configuration for tools using Service Directory.

        Attributes:
            service (str):
                Required. The name of `Service
                Directory <https://cloud.google.com/service-directory>`__
                service. Format:
                ``projects/<ProjectID>/locations/<LocationID>/namespaces/<NamespaceID>/services/<ServiceID>``.
                ``LocationID`` of the service directory must be the same as
                the location of the agent.
        """

        service: str = proto.Field(
            proto.STRING,
            number=1,
        )

    class EndUserAuthConfig(proto.Message):
        r"""End-user authentication configuration used for Connection calls. The
        field values can either be hardcoded authentication values or the
        names of `session
        parameters <https://cloud.google.com/dialogflow/cx/docs/concept/parameter#session-ref>`__
        or `request
        parameters <https://cloud.google.com/dialogflow/cx/docs/concept/parameter#request-scoped>`__.

        If parameter names are provided, then those parameters can be used
        to pass the authentication values dynamically, through
        ``$session.params.param-id`` or ``$request.payload.param-id``.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            oauth2_auth_code_config (google.cloud.dialogflowcx_v3beta1.types.Tool.EndUserAuthConfig.Oauth2AuthCodeConfig):
                Oauth 2.0 Authorization Code authentication.

                This field is a member of `oneof`_ ``end_user_auth_config``.
            oauth2_jwt_bearer_config (google.cloud.dialogflowcx_v3beta1.types.Tool.EndUserAuthConfig.Oauth2JwtBearerConfig):
                JWT Profile Oauth 2.0 Authorization Grant
                authentication.

                This field is a member of `oneof`_ ``end_user_auth_config``.
        """

        class Oauth2AuthCodeConfig(proto.Message):
            r"""Oauth 2.0 Authorization Code authentication configuration.

            Attributes:
                oauth_token (str):
                    Required. Oauth token value or parameter name
                    to pass it through.
            """

            oauth_token: str = proto.Field(
                proto.STRING,
                number=1,
            )

        class Oauth2JwtBearerConfig(proto.Message):
            r"""JWT Profile Oauth 2.0 Authorization Grant authentication
            configuration.

            Attributes:
                issuer (str):
                    Required. Issuer value or parameter name to
                    pass it through.
                subject (str):
                    Required. Subject value or parameter name to
                    pass it through.
                client_key (str):
                    Required. Client key value or parameter name
                    to pass it through.
            """

            issuer: str = proto.Field(
                proto.STRING,
                number=1,
            )
            subject: str = proto.Field(
                proto.STRING,
                number=2,
            )
            client_key: str = proto.Field(
                proto.STRING,
                number=3,
            )

        oauth2_auth_code_config: "Tool.EndUserAuthConfig.Oauth2AuthCodeConfig" = (
            proto.Field(
                proto.MESSAGE,
                number=2,
                oneof="end_user_auth_config",
                message="Tool.EndUserAuthConfig.Oauth2AuthCodeConfig",
            )
        )
        oauth2_jwt_bearer_config: "Tool.EndUserAuthConfig.Oauth2JwtBearerConfig" = (
            proto.Field(
                proto.MESSAGE,
                number=3,
                oneof="end_user_auth_config",
                message="Tool.EndUserAuthConfig.Oauth2JwtBearerConfig",
            )
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    description: str = proto.Field(
        proto.STRING,
        number=3,
    )
    open_api_spec: OpenApiTool = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="specification",
        message=OpenApiTool,
    )
    data_store_spec: DataStoreTool = proto.Field(
        proto.MESSAGE,
        number=8,
        oneof="specification",
        message=DataStoreTool,
    )
    extension_spec: ExtensionTool = proto.Field(
        proto.MESSAGE,
        number=11,
        oneof="specification",
        message=ExtensionTool,
    )
    function_spec: FunctionTool = proto.Field(
        proto.MESSAGE,
        number=13,
        oneof="specification",
        message=FunctionTool,
    )
    connector_spec: ConnectorTool = proto.Field(
        proto.MESSAGE,
        number=15,
        oneof="specification",
        message=ConnectorTool,
    )
    tool_type: ToolType = proto.Field(
        proto.ENUM,
        number=12,
        enum=ToolType,
    )


class ListToolVersionsRequest(proto.Message):
    r"""The request message for
    [Tools.ListToolVersions][google.cloud.dialogflow.cx.v3beta1.Tools.ListToolVersions].

    Attributes:
        parent (str):
            Required. The parent of the tool versions. Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/tools/<ToolID>``.
        page_size (int):
            Optional. The maximum number of items to
            return in a single page. By default 100 and at
            most 1000.
        page_token (str):
            Optional. The next_page_token value returned from a previous
            list request.
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


class ListToolVersionsResponse(proto.Message):
    r"""The response message for
    [Tools.ListToolVersions][google.cloud.dialogflow.cx.v3beta1.Tools.ListToolVersions].

    Attributes:
        tool_versions (MutableSequence[google.cloud.dialogflowcx_v3beta1.types.ToolVersion]):
            The list of tool versions. There will be a maximum number of
            items returned based on the page_size field in the request.
        next_page_token (str):
            Token to retrieve the next page of results,
            or empty if there are no more results in the
            list.
    """

    @property
    def raw_page(self):
        return self

    tool_versions: MutableSequence["ToolVersion"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="ToolVersion",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class CreateToolVersionRequest(proto.Message):
    r"""The request message for
    [Tools.CreateToolVersion][google.cloud.dialogflow.cx.v3beta1.Tools.CreateToolVersion].
    The request message for
    [Tools.CreateToolVersion][google.cloud.dialogflow.cx.v3beta1.Tools.CreateToolVersion].

    Attributes:
        parent (str):
            Required. The tool to create a version for. Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/tools/<ToolID>``.
        tool_version (google.cloud.dialogflowcx_v3beta1.types.ToolVersion):
            Required. The tool version to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    tool_version: "ToolVersion" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="ToolVersion",
    )


class GetToolVersionRequest(proto.Message):
    r"""The request message for
    [Tools.GetToolVersion][google.cloud.dialogflow.cx.v3beta1.Tools.GetToolVersion].

    Attributes:
        name (str):
            Required. The name of the tool version. Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/tools/<ToolID>/versions/<VersionID>``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class DeleteToolVersionRequest(proto.Message):
    r"""The request message for
    [Tools.DeleteToolVersion][google.cloud.dialogflow.cx.v3beta1.Tools.DeleteToolVersion].

    Attributes:
        name (str):
            Required. The name of the tool version to delete. Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/tools/<ToolID>/versions/<VersionID>``.
        force (bool):
            Optional. This field has no effect for Tools not being used.
            For Tools that are used:

            - If ``force`` is set to false, an error will be returned
              with message indicating the referenced resources.
            - If ``force`` is set to true, Dialogflow will remove the
              tool, as well as any references to the tool.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    force: bool = proto.Field(
        proto.BOOL,
        number=2,
    )


class RestoreToolVersionRequest(proto.Message):
    r"""The request message for
    [Tools.RestoreToolVersion][google.cloud.dialogflow.cx.v3beta1.Tools.RestoreToolVersion].

    Attributes:
        name (str):
            Required. The name of the tool version. Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/tools/<ToolID>/versions/<VersionID>``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class RestoreToolVersionResponse(proto.Message):
    r"""The response message for
    [Tools.RestoreToolVersion][google.cloud.dialogflow.cx.v3beta1.Tools.RestoreToolVersion].

    Attributes:
        tool (google.cloud.dialogflowcx_v3beta1.types.Tool):
            The updated tool.
    """

    tool: "Tool" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Tool",
    )


class ToolVersion(proto.Message):
    r"""Tool version is a snapshot of the tool at certain timestamp.

    Attributes:
        name (str):
            Identifier. The unique identifier of the tool version.
            Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/tools/<ToolID>/versions/<VersionID>``.
        display_name (str):
            Required. The display name of the tool
            version.
        tool (google.cloud.dialogflowcx_v3beta1.types.Tool):
            Required. Snapshot of the tool to be
            associated with this version.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Last time the tool version was
            created or modified.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Last time the tool version was
            created or modified.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    tool: "Tool" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="Tool",
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )


class ExportToolsMetadata(proto.Message):
    r"""Metadata returned for the
    [Tools.ExportTools][google.cloud.dialogflow.cx.v3beta1.Tools.ExportTools]
    long running operation.

    """


__all__ = tuple(sorted(__protobuf__.manifest))
