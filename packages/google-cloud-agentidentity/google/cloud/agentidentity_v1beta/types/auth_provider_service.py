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
    package="google.cloud.agentidentity.v1beta",
    manifest={
        "AuthProviderType",
        "AuthProvider",
        "ThreeLeggedOAuth",
        "TwoLeggedOAuth",
        "ApiKeyParams",
        "GeminiEnterpriseAuthProviderParams",
        "ListAuthProvidersRequest",
        "ListAuthProvidersResponse",
        "GetAuthProviderRequest",
        "CreateAuthProviderRequest",
        "UpdateAuthProviderRequest",
        "DeleteAuthProviderRequest",
        "UndeleteAuthProviderRequest",
        "EnableAuthProviderRequest",
        "DisableAuthProviderRequest",
        "Authorization",
        "ListAuthorizationsRequest",
        "ListAuthorizationsResponse",
        "GetAuthorizationRequest",
        "DeleteAuthorizationRequest",
        "AccessSummary",
        "ListAccessSummariesRequest",
        "ListAccessSummariesResponse",
        "GetAccessSummaryRequest",
        "QueryAuthProvidersRequest",
        "QueryAuthProvidersResponse",
        "QueryWorkloadsRequest",
        "QueryWorkloadsResponse",
        "RevokeAuthorizationRequest",
        "RevokeAuthorizationResponse",
    },
)


class AuthProviderType(proto.Enum):
    r"""The type of the AuthProvider.

    Values:
        AUTH_PROVIDER_TYPE_UNSPECIFIED (0):
            Unspecified auth-provider type.
        AUTH_PROVIDER_TYPE_THREE_LEGGED_OAUTH (1):
            Three Legged OAuth auth-provider type.
        AUTH_PROVIDER_TYPE_TWO_LEGGED_OAUTH (2):
            Two Legged OAuth auth-provider type.
        AUTH_PROVIDER_TYPE_API_KEY (3):
            API Key auth-provider type.
        AUTH_PROVIDER_TYPE_GEMINI_ENTERPRISE (4):
            Gemini Enterprise auth-provider type.
    """

    AUTH_PROVIDER_TYPE_UNSPECIFIED = 0
    AUTH_PROVIDER_TYPE_THREE_LEGGED_OAUTH = 1
    AUTH_PROVIDER_TYPE_TWO_LEGGED_OAUTH = 2
    AUTH_PROVIDER_TYPE_API_KEY = 3
    AUTH_PROVIDER_TYPE_GEMINI_ENTERPRISE = 4


class AuthProvider(proto.Message):
    r"""Message describing AuthProvider object

    Attributes:
        name (str):
            Identifier. The full resource name of the auth_provider.
            Format:
            projects/{project}/locations/{location}/authProviders/{auth_provider}
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. [Output only] Create time stamp
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. [Output only] Update time stamp
        labels (MutableMapping[str, str]):
            Optional. Labels as key value pairs
        auth_provider_type_params (google.cloud.agentidentity_v1beta.types.AuthProvider.AuthProviderTypeParams):
            Required. AuthProvider type specific
            parameters.
        allowed_scopes (MutableSequence[str]):
            Optional. List of scopes that are allowed to be requested
            for this auth_provider. If this list is non-empty, only
            scopes within this list may be requested. If this list is
            empty, all scopes may be requested. Scopes appearing in
            ``blocked_scopes`` are disallowed even if they appear in
            ``allowed_scopes``. The number of allowed scopes is limited
            to 200.
        blocked_scopes (MutableSequence[str]):
            Optional. List of scopes that are blocked from being
            requested for this auth_provider. If a scope appears in this
            list, it will not be requested, even if it also appears in
            ``allowed_scopes``. ``blocked_scopes`` takes precedence over
            ``allowed_scopes``. The number of blocked scopes is limited
            to 200.
        description (str):
            Optional. Description of the resource.
            Must be less than 256 characters.
        deleted (bool):
            Output only. This is set to true if the auth_provider is
            deleted.
        expire_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the auth_provider will expire.
        state (google.cloud.agentidentity_v1beta.types.AuthProvider.State):
            Output only. The state of the auth_provider.
        workload_ids (MutableSequence[str]):
            Optional. Input only. Represents the workload identity in
            IAM ``principal://`` format of the agent(s) that will use
            this AuthProvider. Example:
            ``principal://agents.global.org-${ORG_ID}.system.id.goog/resources/aiplatform/projects/{PROJECT_ID}/locations/{LOCATIONS}/reasoningEngines/{ID}``
    """

    class State(proto.Enum):
        r"""Represents the state of the auth_provider.

        Values:
            STATE_UNSPECIFIED (0):
                Unspecified state.
            ENABLED (1):
                Enabled and can be used.
            DISABLED (2):
                Disabled and cannot be used.
        """

        STATE_UNSPECIFIED = 0
        ENABLED = 1
        DISABLED = 2

    class AuthProviderTypeParams(proto.Message):
        r"""AuthProvider type specific parameters. Required when creating an
        auth_provider.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            three_legged_oauth (google.cloud.agentidentity_v1beta.types.ThreeLeggedOAuth):
                ThreeLeggedOAuth AuthProvider type
                parameters.

                This field is a member of `oneof`_ ``type``.
            two_legged_oauth (google.cloud.agentidentity_v1beta.types.TwoLeggedOAuth):
                TwoLeggedOAuth AuthProvider type parameters.

                This field is a member of `oneof`_ ``type``.
            api_key (google.cloud.agentidentity_v1beta.types.ApiKeyParams):
                ApiKey AuthProvider type parameters.

                This field is a member of `oneof`_ ``type``.
            ge_auth_provider (google.cloud.agentidentity_v1beta.types.GeminiEnterpriseAuthProviderParams):
                GeminiEnterprise auth_provider type parameters.

                This field is a member of `oneof`_ ``type``.
        """

        three_legged_oauth: "ThreeLeggedOAuth" = proto.Field(
            proto.MESSAGE,
            number=1,
            oneof="type",
            message="ThreeLeggedOAuth",
        )
        two_legged_oauth: "TwoLeggedOAuth" = proto.Field(
            proto.MESSAGE,
            number=2,
            oneof="type",
            message="TwoLeggedOAuth",
        )
        api_key: "ApiKeyParams" = proto.Field(
            proto.MESSAGE,
            number=3,
            oneof="type",
            message="ApiKeyParams",
        )
        ge_auth_provider: "GeminiEnterpriseAuthProviderParams" = proto.Field(
            proto.MESSAGE,
            number=4,
            oneof="type",
            message="GeminiEnterpriseAuthProviderParams",
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=4,
    )
    auth_provider_type_params: AuthProviderTypeParams = proto.Field(
        proto.MESSAGE,
        number=5,
        message=AuthProviderTypeParams,
    )
    allowed_scopes: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=6,
    )
    blocked_scopes: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=7,
    )
    description: str = proto.Field(
        proto.STRING,
        number=8,
    )
    deleted: bool = proto.Field(
        proto.BOOL,
        number=9,
    )
    expire_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=10,
        message=timestamp_pb2.Timestamp,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=11,
        enum=State,
    )
    workload_ids: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=12,
    )


class ThreeLeggedOAuth(proto.Message):
    r"""Message describing ThreeLeggedOAuth object.

    Attributes:
        client_secret (str):
            Optional. Input only. The client secret of
            the OAuth client.
        client_id (str):
            Optional. The client ID of the OAuth client.
        redirect_url (str):
            Output only. The redirect URL this auth_provider uses for
            the OAuth exchange. This is deterministic based on the name
            of the auth_provider.
        authorization_url (str):
            Optional. The authorization endpoint to send
            users to for consenting to delegate to the
            agent. eg. "https://auth.example.com/authorize".
        token_url (str):
            Optional. The token endpoint for requesting
            tokens on behalf of an end user. eg.
            "https://auth.example.com/oauth/token".
        enable_pkce (bool):
            Optional. Enables Proof Key for Code Exchange
            (PKCE) for the OAuth flow to prevent
            authorization code interception attacks.
        default_continue_uri (str):
            Optional. The default continue URI for 3LO
            flow and it will be used when no continue URI is
            provided in the RetrieveCredentials request.
    """

    client_secret: str = proto.Field(
        proto.STRING,
        number=1,
    )
    client_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    redirect_url: str = proto.Field(
        proto.STRING,
        number=3,
    )
    authorization_url: str = proto.Field(
        proto.STRING,
        number=4,
    )
    token_url: str = proto.Field(
        proto.STRING,
        number=5,
    )
    enable_pkce: bool = proto.Field(
        proto.BOOL,
        number=6,
    )
    default_continue_uri: str = proto.Field(
        proto.STRING,
        number=7,
    )


class TwoLeggedOAuth(proto.Message):
    r"""Message describing TwoLeggedOAuth object.

    Attributes:
        client_secret (str):
            Optional. Input only. The client secret of
            the OAuth client.
        client_id (str):
            Optional. The client ID of the OAuth client.
        token_url (str):
            Optional. The token endpoint of the OAuth
            client.
    """

    client_secret: str = proto.Field(
        proto.STRING,
        number=1,
    )
    client_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    token_url: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ApiKeyParams(proto.Message):
    r"""Message describing ApiKeyParams object.

    Attributes:
        api_key (str):
            Optional. Input only. The API key for this auth_provider.
    """

    api_key: str = proto.Field(
        proto.STRING,
        number=1,
    )


class GeminiEnterpriseAuthProviderParams(proto.Message):
    r"""Message describing GeminiEnterpriseAuthProviderParams object."""


class ListAuthProvidersRequest(proto.Message):
    r"""Message for requesting list of AuthProviders

    Attributes:
        parent (str):
            Required. The parent resource where the
            search is performed. Format:
            projects/{project}/locations/{location}
        page_size (int):
            Optional. Requested page size. Server may
            return fewer items than requested. If
            unspecified, server will pick an appropriate
            default.
        page_token (str):
            Optional. A token, which can be sent as ``page_token`` to
            retrieve the next page. If this field is omitted, the first
            page is returned.
        filter (str):
            Optional. Filter results. This field is
            currently ignored.
        order_by (str):
            Optional. Currently ignored. Defaults to ordering by
            auth_provider_id in ascending order.
        show_deleted (bool):
            Optional. Deleted auth_providers will be kept with a
            soft-delete for 30 days before being purged. If this field
            is set to true, deleted auth_providers will also be
            returned.
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
    show_deleted: bool = proto.Field(
        proto.BOOL,
        number=6,
    )


class ListAuthProvidersResponse(proto.Message):
    r"""Message for response to listing AuthProviders

    Attributes:
        auth_providers (MutableSequence[google.cloud.agentidentity_v1beta.types.AuthProvider]):
            The list of AuthProvider
        next_page_token (str):
            A token identifying a page of results the
            server should return.
        unreachable (MutableSequence[str]):
            Unordered list. Locations that could not be
            reached.
    """

    @property
    def raw_page(self):
        return self

    auth_providers: MutableSequence["AuthProvider"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="AuthProvider",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetAuthProviderRequest(proto.Message):
    r"""Message for getting a AuthProvider

    Attributes:
        name (str):
            Required. Name of the resource
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateAuthProviderRequest(proto.Message):
    r"""Message for creating a AuthProvider

    Attributes:
        parent (str):
            Required. The parent resource where the
            AuthProvider is created. Format:
            projects/{project}/locations/{location}
        auth_provider_id (str):
            Required. The ID to use for the AuthProvider, which will
            become the final segment of the AuthProvider's resource
            name. This value should be 1-63 characters, and valid
            characters are /[a-z][0-9]-/. The first character must be a
            lowercase letter, and the last character must be a lowercase
            letter or a number.
        auth_provider (google.cloud.agentidentity_v1beta.types.AuthProvider):
            Required. The AuthProvider to create.
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
    auth_provider_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    auth_provider: "AuthProvider" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="AuthProvider",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class UpdateAuthProviderRequest(proto.Message):
    r"""Message for updating a AuthProvider

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. Field mask is used to specify the fields to be
            overwritten in the AuthProvider resource by the update. The
            fields specified in the update_mask are relative to the
            resource, not the full request. A field will be overwritten
            if it is in the mask. If the user does not provide a mask
            then all fields present in the request will be overwritten.
        auth_provider (google.cloud.agentidentity_v1beta.types.AuthProvider):
            Required. The AuthProvider resource which
            replaces the resource on the server.
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

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    auth_provider: "AuthProvider" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="AuthProvider",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class DeleteAuthProviderRequest(proto.Message):
    r"""Message for deleting a AuthProvider

    Attributes:
        name (str):
            Required. Name of the resource
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
        number=2,
    )


class UndeleteAuthProviderRequest(proto.Message):
    r"""Message for undeleting a AuthProvider

    Attributes:
        name (str):
            Required. Name of the resource Format:
            projects/{project}/locations/{location}/authProviders/{auth_provider}
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server will
            know to ignore the request if it has already
            been completed. The server will guarantee that
            for at least 60 minutes after the first request.

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
        number=2,
    )


class EnableAuthProviderRequest(proto.Message):
    r"""Message for enabling an AuthProvider

    Attributes:
        name (str):
            Required. Name of the resource Format:
            projects/{project}/locations/{location}/authProviders/{auth_provider}
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server will
            know to ignore the request if it has already
            been completed. The server will guarantee that
            for at least 60 minutes after the first request.

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
        number=2,
    )


class DisableAuthProviderRequest(proto.Message):
    r"""Message for disabling an AuthProvider

    Attributes:
        name (str):
            Required. Name of the resource Format:
            projects/{project}/locations/{location}/authProviders/{auth_provider}
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server will
            know to ignore the request if it has already
            been completed. The server will guarantee that
            for at least 60 minutes after the first request.

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
        number=2,
    )


class Authorization(proto.Message):
    r"""Message describing Authorization object

    Attributes:
        name (str):
            Identifier. name of resource
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. [Output only] Create time stamp
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. [Output only] Update time stamp
        client_user_id (str):
            Output only. The client_user_id provided by the client
            application for their end user. Not verified by Google.
        scopes (MutableSequence[str]):
            Output only. The scopes actually granted by
            the end user during the consent flow.
        state (google.cloud.agentidentity_v1beta.types.Authorization.State):
            Output only. The state of the authorization.
    """

    class State(proto.Enum):
        r"""Represents the state of the authorization.

        Values:
            STATE_UNSPECIFIED (0):
                Unspecified state.
            ACTIVE (1):
                Active.
            SUSPENDED (2):
                Suspended.
        """

        STATE_UNSPECIFIED = 0
        ACTIVE = 1
        SUSPENDED = 2

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    client_user_id: str = proto.Field(
        proto.STRING,
        number=5,
    )
    scopes: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=6,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=7,
        enum=State,
    )


class ListAuthorizationsRequest(proto.Message):
    r"""Message for requesting list of Authorizations

    Attributes:
        parent (str):
            Required. The parent resource where the search is performed.
            Format:
            projects/{project}/locations/{location}/authProviders/{auth_provider}
        page_size (int):
            Optional. Requested page size. Server may
            return fewer items than requested. If
            unspecified, server will pick an appropriate
            default.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListAuthorizations`` call. Provide this to retrieve the
            subsequent page. When paginating, all other parameters
            provided to ``ListAuthorizations`` must match the call that
            provided the page token.
        filter (str):
            Optional. Filter string to restrict the results. Currently
            supports filtering by ``client_user_id`` only. Format:
            ``client_user_id="<value>"``
        order_by (str):
            Optional. This field is currently ignored. Defaults to
            ordering by authorization_id in ascending order.
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


class ListAuthorizationsResponse(proto.Message):
    r"""Message for response to listing Authorizations

    Attributes:
        authorizations (MutableSequence[google.cloud.agentidentity_v1beta.types.Authorization]):
            The list of Authorization
        next_page_token (str):
            A token identifying a page of results the
            server should return.
        unreachable (MutableSequence[str]):
            Unordered list. Locations that could not be
            reached.
    """

    @property
    def raw_page(self):
        return self

    authorizations: MutableSequence["Authorization"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Authorization",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetAuthorizationRequest(proto.Message):
    r"""Message for getting a Authorization

    Attributes:
        name (str):
            Required. Name of the resource
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class DeleteAuthorizationRequest(proto.Message):
    r"""Message for deleting an Authorization

    Attributes:
        name (str):
            Required. The name of the Authorization to delete. Format:
            projects/{project}/locations/{location}/authProviders/{auth_provider}/authorizations/{authorization}
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
        number=2,
    )


class AccessSummary(proto.Message):
    r"""Message describing AccessSummary object

    Attributes:
        name (str):
            Output only. Identifier. Name of the
            AccessSummary
        first_access_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The first time this user has
            interacted with this workload. Rounded to the
            previous hour.
        last_access_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The most recent time this user
            has interacted with this workload. Rounded to
            the previous hour.
        labels (MutableMapping[str, str]):
            Optional. Labels as key value pairs
        user_id (str):
            Output only. The user_id provided by the workload
            application for this user. Not verified by Google.
        workload_id (str):
            Output only. The identity bound to the
            workload that this user interacted with to
            produce this AccessSummary. Will typically be an
            agentic spiffe id
        token_url (str):
            Output only. The url of the authentication
            server that was accessed.
        scopes (MutableSequence[str]):
            Output only. All scopes that have been used
            by this user with this workload. The number of
            scopes is limited to 200.
        auth_provider (str):
            Output only. The auth_provider that this access summary is
            associated with.
        purge_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when this access
            summary is permanently deleted.
        auth_provider_type (google.cloud.agentidentity_v1beta.types.AuthProviderType):
            Output only. The type of the connector that
            was used to create this access summary.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    first_access_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    last_access_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=4,
    )
    user_id: str = proto.Field(
        proto.STRING,
        number=5,
    )
    workload_id: str = proto.Field(
        proto.STRING,
        number=6,
    )
    token_url: str = proto.Field(
        proto.STRING,
        number=7,
    )
    scopes: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=8,
    )
    auth_provider: str = proto.Field(
        proto.STRING,
        number=9,
    )
    purge_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=10,
        message=timestamp_pb2.Timestamp,
    )
    auth_provider_type: "AuthProviderType" = proto.Field(
        proto.ENUM,
        number=11,
        enum="AuthProviderType",
    )


class ListAccessSummariesRequest(proto.Message):
    r"""Message for requesting list of AccessSummaries

    Attributes:
        parent (str):
            Required. The parent resource where the
            search is performed. Format:
            projects/{project}/locations/{location}
        page_size (int):
            Optional. Requested page size. Server may
            return fewer items than requested. If
            unspecified, server will pick an appropriate
            default.
        page_token (str):
            Optional. A token identifying a page of
            results the server should return.
        filter (str):
            Optional. Filter string to restrict the results.

            Currently supports filtering by ``workload_id`` or
            ``auth_provider_name``. If no filter is provided, returns
            all access summaries for the requested project and location.
            Format: ``workload_id="<value>"`` or
            ``auth_provider_name="<value>"``
        order_by (str):
            Optional. This field is currently ignored. Defaults to
            ordering by (auth_provider_id, user_id) in ascending order.
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


class ListAccessSummariesResponse(proto.Message):
    r"""Message for response to listing AccessSummaries

    Attributes:
        access_summaries (MutableSequence[google.cloud.agentidentity_v1beta.types.AccessSummary]):
            The list of AccessSummary
        next_page_token (str):
            A token identifying a page of results the
            server should return.
        unreachable (MutableSequence[str]):
            Unordered list. Locations that could not be
            reached.
    """

    @property
    def raw_page(self):
        return self

    access_summaries: MutableSequence["AccessSummary"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="AccessSummary",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetAccessSummaryRequest(proto.Message):
    r"""Message for getting a AccessSummary

    Attributes:
        name (str):
            Required. Name of the resource
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class QueryAuthProvidersRequest(proto.Message):
    r"""Request message for QueryAuthProviders.

    Attributes:
        parent (str):
            Required. The parent resource where the
            search is performed. Format:
            projects/{project}/locations/{location}
        workload_id (str):
            Required. The workload identifier to filter
            by.
        page_size (int):
            Optional. Requested page size. Server may
            return fewer items than requested. If
            unspecified, server will pick an appropriate
            default. The maximum page size is 1000.
        page_token (str):
            Optional. A token, which can be sent as ``page_token`` to
            retrieve the next page. If this field is omitted, the first
            page is returned.

            A page token, received from a previous QueryAuthProviders
            call. Provide this to retrieve the subsequent page. When
            paginating, all other parameters provided to
            QueryAuthProviders must match the call that provided the
            page token.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    workload_id: str = proto.Field(
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


class QueryAuthProvidersResponse(proto.Message):
    r"""Response message for QueryAuthProviders.

    Attributes:
        auth_provider_names (MutableSequence[str]):
            The unique list of auth_provider resource names used by the
            workload.
        next_page_token (str):
            A token identifying a page of results the
            server should return. If this field is omitted,
            there are no subsequent pages.
    """

    @property
    def raw_page(self):
        return self

    auth_provider_names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class QueryWorkloadsRequest(proto.Message):
    r"""Request message for QueryWorkloads.

    Attributes:
        name (str):
            Required. The name of the auth_provider to query. Format:
            projects/{project}/locations/{location}/authProviders/{auth_provider}
        page_size (int):
            Optional. Requested page size. Server may
            return fewer items than requested. If
            unspecified, server will pick an appropriate
            default.
        page_token (str):
            Optional. A token, which can be sent as ``page_token`` to
            retrieve the next page. When paginating, all other
            parameters provided to QueryWorkloads must match the call
            that provided the page token. If this field is omitted, the
            first page is returned.
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


class QueryWorkloadsResponse(proto.Message):
    r"""Response message for QueryWorkloads.

    Attributes:
        workload_ids (MutableSequence[str]):
            The unique list of workload identifiers (agents) that used
            the auth_provider.
        next_page_token (str):
            A token to retrieve the next page of results.
    """

    @property
    def raw_page(self):
        return self

    workload_ids: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class RevokeAuthorizationRequest(proto.Message):
    r"""Request message for RevokeAuthorization.

    Attributes:
        name (str):
            Required. The resource name of the AuthProvider. Format:
            projects/{project}/locations/{location}/authProviders/{auth_provider}
        user_id (str):
            Required. The identity of the user to revoke
            authorization for.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    user_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class RevokeAuthorizationResponse(proto.Message):
    r"""Response message for RevokeAuthorization."""


__all__ = tuple(sorted(__protobuf__.manifest))
