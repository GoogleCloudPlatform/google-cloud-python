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

import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.ces.v1beta",
    manifest={
        "ApiKeyConfig",
        "OAuthConfig",
        "ServiceAgentIdTokenAuthConfig",
        "ServiceAccountAuthConfig",
        "BearerTokenConfig",
        "EndUserAuthConfig",
        "ApiAuthentication",
    },
)


class ApiKeyConfig(proto.Message):
    r"""Configurations for authentication with API key.

    Attributes:
        key_name (str):
            Required. The parameter name or the header
            name of the API key. E.g., If the API request is
            "https://example.com/act?X-Api-Key=<API KEY>",
            "X-Api-Key" would be the parameter name.
        api_key_secret_version (str):
            Required. The name of the SecretManager secret version
            resource storing the API key. Format:
            ``projects/{project}/secrets/{secret}/versions/{version}``

            Note: You should grant
            ``roles/secretmanager.secretAccessor`` role to the CES
            service agent
            ``service-<PROJECT-NUMBER>@gcp-sa-ces.iam.gserviceaccount.com``.
        request_location (google.cloud.ces_v1beta.types.ApiKeyConfig.RequestLocation):
            Required. Key location in the request.
    """

    class RequestLocation(proto.Enum):
        r"""The location of the API key in the request.

        Values:
            REQUEST_LOCATION_UNSPECIFIED (0):
                Unspecified. This value should not be used.
            HEADER (1):
                Represents the key in http header.
            QUERY_STRING (2):
                Represents the key in query string.
        """

        REQUEST_LOCATION_UNSPECIFIED = 0
        HEADER = 1
        QUERY_STRING = 2

    key_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    api_key_secret_version: str = proto.Field(
        proto.STRING,
        number=2,
    )
    request_location: RequestLocation = proto.Field(
        proto.ENUM,
        number=3,
        enum=RequestLocation,
    )


class OAuthConfig(proto.Message):
    r"""Configurations for authentication with OAuth.

    Attributes:
        oauth_grant_type (google.cloud.ces_v1beta.types.OAuthConfig.OauthGrantType):
            Required. OAuth grant types.
        client_id (str):
            Required. The client ID from the OAuth
            provider.
        client_secret_version (str):
            Required. The name of the SecretManager secret version
            resource storing the client secret. Format:
            ``projects/{project}/secrets/{secret}/versions/{version}``

            Note: You should grant
            ``roles/secretmanager.secretAccessor`` role to the CES
            service agent
            ``service-<PROJECT-NUMBER>@gcp-sa-ces.iam.gserviceaccount.com``.
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
                Unspecified. Defaults to CLIENT_CREDENTIAL.
            CLIENT_CREDENTIAL (1):
                Represents the `client credential
                flow <https://oauth.net/2/grant-types/client-credentials>`__.
        """

        OAUTH_GRANT_TYPE_UNSPECIFIED = 0
        CLIENT_CREDENTIAL = 1

    oauth_grant_type: OauthGrantType = proto.Field(
        proto.ENUM,
        number=1,
        enum=OauthGrantType,
    )
    client_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    client_secret_version: str = proto.Field(
        proto.STRING,
        number=3,
    )
    token_endpoint: str = proto.Field(
        proto.STRING,
        number=4,
    )
    scopes: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=5,
    )


class ServiceAgentIdTokenAuthConfig(proto.Message):
    r"""Configurations for authentication with `ID
    token <https://cloud.google.com/docs/authentication/token-types#id>`__
    generated from service agent.

    """


class ServiceAccountAuthConfig(proto.Message):
    r"""Configurations for authentication using a custom service
    account.

    Attributes:
        service_account (str):
            Required. The email address of the service account used for
            authentication. CES uses this service account to exchange an
            access token and the access token is then sent in the
            ``Authorization`` header of the request.

            The service account must have the
            ``roles/iam.serviceAccountTokenCreator`` role granted to the
            CES service agent
            ``service-<PROJECT-NUMBER>@gcp-sa-ces.iam.gserviceaccount.com``.
        scopes (MutableSequence[str]):
            Optional. The OAuth scopes to grant. If not specified, the
            default scope
            ``https://www.googleapis.com/auth/cloud-platform`` is used.
    """

    service_account: str = proto.Field(
        proto.STRING,
        number=1,
    )
    scopes: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class BearerTokenConfig(proto.Message):
    r"""Configurations for authentication with a bearer token.

    Attributes:
        token (str):
            Required. The bearer token. Must be in the format
            ``$context.variables.<name_of_variable>``.
    """

    token: str = proto.Field(
        proto.STRING,
        number=1,
    )


class EndUserAuthConfig(proto.Message):
    r"""End-user authentication configuration used for Connection calls. The
    field values must be the names of context variables in the format
    ``$context.variables.<name_of_variable>``.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        oauth2_auth_code_config (google.cloud.ces_v1beta.types.EndUserAuthConfig.Oauth2AuthCodeConfig):
            Oauth 2.0 Authorization Code authentication.

            This field is a member of `oneof`_ ``auth_config``.
        oauth2_jwt_bearer_config (google.cloud.ces_v1beta.types.EndUserAuthConfig.Oauth2JwtBearerConfig):
            JWT Profile Oauth 2.0 Authorization Grant
            authentication.

            This field is a member of `oneof`_ ``auth_config``.
    """

    class Oauth2AuthCodeConfig(proto.Message):
        r"""Oauth 2.0 Authorization Code authentication configuration.

        Attributes:
            oauth_token (str):
                Required. Oauth token parameter name to pass through. Must
                be in the format ``$context.variables.<name_of_variable>``.
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
                Required. Issuer parameter name to pass through. Must be in
                the format ``$context.variables.<name_of_variable>``.
            subject (str):
                Required. Subject parameter name to pass through. Must be in
                the format ``$context.variables.<name_of_variable>``.
            client_key (str):
                Required. Client parameter name to pass through. Must be in
                the format ``$context.variables.<name_of_variable>``.
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

    oauth2_auth_code_config: Oauth2AuthCodeConfig = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="auth_config",
        message=Oauth2AuthCodeConfig,
    )
    oauth2_jwt_bearer_config: Oauth2JwtBearerConfig = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="auth_config",
        message=Oauth2JwtBearerConfig,
    )


class ApiAuthentication(proto.Message):
    r"""Authentication information required for API calls.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        api_key_config (google.cloud.ces_v1beta.types.ApiKeyConfig):
            Optional. Config for API key auth.

            This field is a member of `oneof`_ ``auth_config``.
        oauth_config (google.cloud.ces_v1beta.types.OAuthConfig):
            Optional. Config for OAuth.

            This field is a member of `oneof`_ ``auth_config``.
        service_agent_id_token_auth_config (google.cloud.ces_v1beta.types.ServiceAgentIdTokenAuthConfig):
            Optional. Config for ID token auth generated
            from CES service agent.

            This field is a member of `oneof`_ ``auth_config``.
        service_account_auth_config (google.cloud.ces_v1beta.types.ServiceAccountAuthConfig):
            Optional. Config for service account
            authentication.

            This field is a member of `oneof`_ ``auth_config``.
        bearer_token_config (google.cloud.ces_v1beta.types.BearerTokenConfig):
            Optional. Config for bearer token auth.

            This field is a member of `oneof`_ ``auth_config``.
    """

    api_key_config: "ApiKeyConfig" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="auth_config",
        message="ApiKeyConfig",
    )
    oauth_config: "OAuthConfig" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="auth_config",
        message="OAuthConfig",
    )
    service_agent_id_token_auth_config: "ServiceAgentIdTokenAuthConfig" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="auth_config",
        message="ServiceAgentIdTokenAuthConfig",
    )
    service_account_auth_config: "ServiceAccountAuthConfig" = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="auth_config",
        message="ServiceAccountAuthConfig",
    )
    bearer_token_config: "BearerTokenConfig" = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="auth_config",
        message="BearerTokenConfig",
    )


__all__ = tuple(sorted(__protobuf__.manifest))
