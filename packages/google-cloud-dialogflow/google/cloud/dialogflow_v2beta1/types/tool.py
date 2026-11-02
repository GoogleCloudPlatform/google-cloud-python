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

__protobuf__ = proto.module(
    package="google.cloud.dialogflow.v2beta1",
    manifest={
        "CreateToolRequest",
        "GetToolRequest",
        "ListToolsRequest",
        "ListToolsResponse",
        "DeleteToolRequest",
        "UpdateToolRequest",
        "Tool",
    },
)


class CreateToolRequest(proto.Message):
    r"""Request message of CreateTool.

    Attributes:
        parent (str):
            Required. The project/location to create tool for. Format:
            ``projects/<Project ID>/locations/<Location ID>``
        tool (google.cloud.dialogflow_v2beta1.types.Tool):
            Required. The tool to create.
        tool_id (str):
            Optional. The ID to use for the tool, which will become the
            final component of the tool's resource name.

            The tool ID must be compliant with the regression formula
            ``[a-zA-Z][a-zA-Z0-9_-]*`` with the characters length in
            range of [3,64]. If the field is not provide, an Id will be
            auto-generated. If the field is provided, the caller is
            responsible for

            1. the uniqueness of the ID, otherwise the request will be
               rejected.
            2. the consistency for whether to use custom ID or not under
               a project to better ensure uniqueness.
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
    tool_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class GetToolRequest(proto.Message):
    r"""Request message of GetTool.

    Attributes:
        name (str):
            Required. The tool resource name to retrieve. Format:
            ``projects/<Project ID>/locations/<Location ID>/tools/<Tool ID>``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListToolsRequest(proto.Message):
    r"""Request message of ListTools.

    Attributes:
        parent (str):
            Required. The project/location to list tools for. Format:
            ``projects/<Project ID>/locations/<Location ID>``
        page_size (int):
            Optional. Maximum number of conversation
            models to return in a single page. Default to
            10.
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


class ListToolsResponse(proto.Message):
    r"""Response of ListTools.

    Attributes:
        tools (MutableSequence[google.cloud.dialogflow_v2beta1.types.Tool]):
            List of tools retrieved.
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


class DeleteToolRequest(proto.Message):
    r"""Request of DeleteTool.

    Attributes:
        name (str):
            Required. The tool resource name to delete. Format:
            ``projects/<Project ID>/locations/<Location ID>/tools/<Tool ID>``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateToolRequest(proto.Message):
    r"""Request of UpdateTool.

    Attributes:
        tool (google.cloud.dialogflow_v2beta1.types.Tool):
            Required. The tool to update.
            The name field of tool is to identify the tool
            to update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. The list of fields to update.
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


class Tool(proto.Message):
    r"""Represents a tool.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Output only. Identifier. The resource name of the tool.
            Format:
            ``projects/<Project ID>/locations/<Location ID>/tools/<Tool ID>``.
        tool_key (str):
            Required. A human readable short name of the
            tool, which should be unique within the project.
            It should only contain letters, numbers, and
            underscores, and it will be used by LLM to
            identify the tool.
        display_name (str):
            Optional. A human readable short name of the
            tool, to be shown on the UI.
        description (str):
            Optional. A human readable description of the
            tool.
        action_confirmation_requirement (MutableMapping[str, google.cloud.dialogflow_v2beta1.types.Tool.ConfirmationRequirement]):
            Optional. Confirmation requirement for the actions. Each key
            is an action name in the action_schemas. If an action's
            confirmation requirement is unspecified (either the key is
            not present, or its value is
            CONFIRMATION_REQUIREMENT_UNSPECIFIED), the requirement is
            inferred from the action's method_type - confirmation is not
            required if and only if method_type is GET.
        extension_spec (google.cloud.dialogflow_v2beta1.types.Tool.ExtensionTool):
            Vertex extension tool specification.

            This field is a member of `oneof`_ ``specification``.
        function_spec (google.cloud.dialogflow_v2beta1.types.Tool.FunctionTool):
            Client side executed function specification.

            This field is a member of `oneof`_ ``specification``.
        connector_spec (google.cloud.dialogflow_v2beta1.types.Tool.ConnectorTool):
            Integration connectors tool specification.

            This field is a member of `oneof`_ ``specification``.
        open_api_spec (google.cloud.dialogflow_v2beta1.types.Tool.OpenApiTool):
            OpenAPI tool.

            This field is a member of `oneof`_ ``specification``.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Creation time of this tool.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Update time of this tool.
        satisfies_pzs (bool):
            Output only. A read only boolean field
            reflecting Zone Separation status of the tool.
            If the field is absent, it means the status is
            unknown.

            This field is a member of `oneof`_ ``_satisfies_pzs``.
        satisfies_pzi (bool):
            Output only. A read only boolean field
            reflecting Zone Isolation status of the tool. If
            the field is absent, it means the status is
            unknown.

            This field is a member of `oneof`_ ``_satisfies_pzi``.
    """

    class ConfirmationRequirement(proto.Enum):
        r"""Types of confirmation requirement.

        Values:
            CONFIRMATION_REQUIREMENT_UNSPECIFIED (0):
                Unspecified. Whether the action requires confirmation is
                inferred from method_type.
            REQUIRED (1):
                Conformation is required.
            NOT_REQUIRED (2):
                Conformation is not required.
        """

        CONFIRMATION_REQUIREMENT_UNSPECIFIED = 0
        REQUIRED = 1
        NOT_REQUIRED = 2

    class MethodType(proto.Enum):
        r"""The method type of the function.

        Values:
            METHOD_TYPE_UNSPECIFIED (0):
                Unspecified.
            GET (1):
                GET method.
            POST (2):
                POST method.
            PUT (3):
                PUT method.
            DELETE (4):
                DELETE method.
            PATCH (5):
                PATCH method.
        """

        METHOD_TYPE_UNSPECIFIED = 0
        GET = 1
        POST = 2
        PUT = 3
        DELETE = 4
        PATCH = 5

    class ExtensionTool(proto.Message):
        r"""An ExtensionTool is a way to use Vertex Extensions as a tool.

        Attributes:
            name (str):
                Required. The full name of the referenced vertex extension.
                Format:
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
            method_type (google.cloud.dialogflow_v2beta1.types.Tool.MethodType):
                Optional. The method type of the function. If
                not specified, the default value is GET.
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
        method_type: "Tool.MethodType" = proto.Field(
            proto.ENUM,
            number=4,
            enum="Tool.MethodType",
        )

    class OpenApiTool(proto.Message):
        r"""An OpenAPI tool is a way to provide the Tool specifications
        in the Open API schema format.


        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            text_schema (str):
                Required. The OpenAPI schema specified as a
                text.

                This field is a member of `oneof`_ ``schema``.
            authentication (google.cloud.dialogflow_v2beta1.types.Tool.Authentication):
                Optional. Authentication information required
                by the API.
            tls_config (google.cloud.dialogflow_v2beta1.types.Tool.TLSConfig):
                Optional. TLS configuration for the HTTPS
                verification.
            service_directory_config (google.cloud.dialogflow_v2beta1.types.Tool.ServiceDirectoryConfig):
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

    class ConnectorTool(proto.Message):
        r"""A ConnectorTool enabling using Integration Connectors
        Connections as tools.

        Attributes:
            name (str):
                Required. The full resource name of the referenced
                Integration Connectors Connection. Format:
                'projects/*/locations/*/connections/\*'
            actions (MutableSequence[google.cloud.dialogflow_v2beta1.types.Tool.ConnectorTool.Action]):
                Required. Actions for the tool to use.
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
                entity_operation (google.cloud.dialogflow_v2beta1.types.Tool.ConnectorTool.Action.EntityOperation):
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
                    operation (google.cloud.dialogflow_v2beta1.types.Tool.ConnectorTool.Action.EntityOperation.OperationType):
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

    class Authentication(proto.Message):
        r"""Authentication information required for API calls

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            api_key_config (google.cloud.dialogflow_v2beta1.types.Tool.Authentication.ApiKeyConfig):
                Config for API key auth.

                This field is a member of `oneof`_ ``auth_config``.
            oauth_config (google.cloud.dialogflow_v2beta1.types.Tool.Authentication.OAuthConfig):
                Config for OAuth.

                This field is a member of `oneof`_ ``auth_config``.
            service_agent_auth_config (google.cloud.dialogflow_v2beta1.types.Tool.Authentication.ServiceAgentAuthConfig):
                Config for `Diglogflow service
                agent <https://cloud.google.com/iam/docs/service-agents#dialogflow-service-agent>`__
                auth.

                This field is a member of `oneof`_ ``auth_config``.
            bearer_token_config (google.cloud.dialogflow_v2beta1.types.Tool.Authentication.BearerTokenConfig):
                Config for bearer token auth.

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
                request_location (google.cloud.dialogflow_v2beta1.types.Tool.Authentication.RequestLocation):
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
                oauth_grant_type (google.cloud.dialogflow_v2beta1.types.Tool.Authentication.OAuthConfig.OauthGrantType):
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
            r"""Config for auth using `Dialogflow service
            agent <https://cloud.google.com/iam/docs/service-agents#dialogflow-service-agent>`__.

            Attributes:
                service_agent_auth (google.cloud.dialogflow_v2beta1.types.Tool.Authentication.ServiceAgentAuthConfig.ServiceAgentAuth):
                    Optional. Indicate the auth token type generated from the
                    `Diglogflow service
                    agent <https://cloud.google.com/iam/docs/service-agents#dialogflow-service-agent>`__.
                    The generated token is sent in the Authorization header.
            """

            class ServiceAgentAuth(proto.Enum):
                r"""Indicate the auth token type generated from the `Diaglogflow service
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

    class TLSConfig(proto.Message):
        r"""The TLS configuration.

        Attributes:
            ca_certs (MutableSequence[google.cloud.dialogflow_v2beta1.types.Tool.TLSConfig.CACert]):
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
                    self-signed using the following command,

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
                the location of the tool.
        """

        service: str = proto.Field(
            proto.STRING,
            number=1,
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    tool_key: str = proto.Field(
        proto.STRING,
        number=2,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=19,
    )
    description: str = proto.Field(
        proto.STRING,
        number=3,
    )
    action_confirmation_requirement: MutableMapping[str, ConfirmationRequirement] = (
        proto.MapField(
            proto.STRING,
            proto.ENUM,
            number=17,
            enum=ConfirmationRequirement,
        )
    )
    extension_spec: ExtensionTool = proto.Field(
        proto.MESSAGE,
        number=4,
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
        number=18,
        oneof="specification",
        message=ConnectorTool,
    )
    open_api_spec: OpenApiTool = proto.Field(
        proto.MESSAGE,
        number=20,
        oneof="specification",
        message=OpenApiTool,
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
    satisfies_pzs: bool = proto.Field(
        proto.BOOL,
        number=14,
        optional=True,
    )
    satisfies_pzi: bool = proto.Field(
        proto.BOOL,
        number=15,
        optional=True,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
