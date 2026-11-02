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
    package="google.cloud.developerconnect.v1",
    manifest={
        "SystemProvider",
        "ListUsersRequest",
        "ListUsersResponse",
        "Connection",
        "CryptoKeyConfig",
        "GitProxyConfig",
        "InstallationState",
        "GenericHTTPEndpointConfig",
        "GitHubConfig",
        "GitHubEnterpriseConfig",
        "ServiceDirectoryConfig",
        "OAuthCredential",
        "GitLabConfig",
        "UserCredential",
        "GitLabEnterpriseConfig",
        "BitbucketDataCenterConfig",
        "BitbucketCloudConfig",
        "SecureSourceManagerInstanceConfig",
        "ListConnectionsRequest",
        "ListConnectionsResponse",
        "GetConnectionRequest",
        "CreateConnectionRequest",
        "UpdateConnectionRequest",
        "DeleteConnectionRequest",
        "ListAccountConnectorsRequest",
        "ListAccountConnectorsResponse",
        "GetAccountConnectorRequest",
        "CreateAccountConnectorRequest",
        "UpdateAccountConnectorRequest",
        "DeleteAccountConnectorRequest",
        "DeleteUserRequest",
        "OperationMetadata",
        "FetchSelfRequest",
        "DeleteSelfRequest",
        "FetchAccessTokenRequest",
        "FetchAccessTokenResponse",
        "StartOAuthRequest",
        "StartOAuthResponse",
        "FinishOAuthRequest",
        "FinishOAuthResponse",
        "ExchangeError",
        "GitRepositoryLink",
        "CreateGitRepositoryLinkRequest",
        "DeleteGitRepositoryLinkRequest",
        "ListGitRepositoryLinksRequest",
        "ListGitRepositoryLinksResponse",
        "GetGitRepositoryLinkRequest",
        "FetchReadWriteTokenRequest",
        "FetchReadTokenRequest",
        "FetchReadTokenResponse",
        "FetchReadWriteTokenResponse",
        "FetchLinkableGitRepositoriesRequest",
        "FetchLinkableGitRepositoriesResponse",
        "LinkableGitRepository",
        "FetchGitHubInstallationsRequest",
        "FetchGitHubInstallationsResponse",
        "FetchGitRefsRequest",
        "FetchGitRefsResponse",
        "AccountConnector",
        "User",
        "ProviderOAuthConfig",
    },
)


class SystemProvider(proto.Enum):
    r"""SystemProvider is a list of providers that are owned by
    Developer Connect.

    Values:
        SYSTEM_PROVIDER_UNSPECIFIED (0):
            No system provider specified.
        GITHUB (1):
            GitHub provider.
            Scopes can be found at
            https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/scopes-for-oauth-apps#available-scopes
        GITLAB (2):
            GitLab provider. Scopes can be found at
            https://docs.gitlab.com/user/profile/personal_access_tokens/#personal-access-token-scopes
        GOOGLE (3):
            Google provider.
            Recommended scopes:

            "https://www.googleapis.com/auth/drive.readonly",
            "https://www.googleapis.com/auth/documents.readonly".
        SENTRY (4):
            Sentry provider.
            Scopes can be found at
            https://docs.sentry.io/api/permissions/
        ROVO (5):
            Rovo provider.
            Must select the "rovo" scope.
        NEW_RELIC (6):
            New Relic provider.
            No scopes are allowed.
        DATASTAX (7):
            Datastax provider.
            No scopes are allowed.
        DYNATRACE (8):
            Dynatrace provider.
    """

    SYSTEM_PROVIDER_UNSPECIFIED = 0
    GITHUB = 1
    GITLAB = 2
    GOOGLE = 3
    SENTRY = 4
    ROVO = 5
    NEW_RELIC = 6
    DATASTAX = 7
    DYNATRACE = 8


class ListUsersRequest(proto.Message):
    r"""Message for requesting a list of Users

    Attributes:
        parent (str):
            Required. Parent value for ListUsersRequest
        page_size (int):
            Optional. Requested page size. Server may
            return fewer items than requested. If
            unspecified, server will pick an appropriate
            default.
        page_token (str):
            Optional. A token identifying a page of
            results the server should return.
        filter (str):
            Optional. Filtering results
        order_by (str):
            Optional. Hint for how to order the results
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


class ListUsersResponse(proto.Message):
    r"""Message for response to listing Users

    Attributes:
        users (MutableSequence[google.cloud.developerconnect_v1.types.User]):
            The list of Users
        next_page_token (str):
            A token identifying a page of results the
            server should return.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    users: MutableSequence["User"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="User",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class Connection(proto.Message):
    r"""Message describing Connection object

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        github_config (google.cloud.developerconnect_v1.types.GitHubConfig):
            Configuration for connections to github.com.

            This field is a member of `oneof`_ ``connection_config``.
        github_enterprise_config (google.cloud.developerconnect_v1.types.GitHubEnterpriseConfig):
            Configuration for connections to an instance
            of GitHub Enterprise.

            This field is a member of `oneof`_ ``connection_config``.
        gitlab_config (google.cloud.developerconnect_v1.types.GitLabConfig):
            Configuration for connections to gitlab.com.

            This field is a member of `oneof`_ ``connection_config``.
        gitlab_enterprise_config (google.cloud.developerconnect_v1.types.GitLabEnterpriseConfig):
            Configuration for connections to an instance
            of GitLab Enterprise.

            This field is a member of `oneof`_ ``connection_config``.
        bitbucket_data_center_config (google.cloud.developerconnect_v1.types.BitbucketDataCenterConfig):
            Configuration for connections to an instance
            of Bitbucket Data Center.

            This field is a member of `oneof`_ ``connection_config``.
        bitbucket_cloud_config (google.cloud.developerconnect_v1.types.BitbucketCloudConfig):
            Configuration for connections to an instance
            of Bitbucket Clouds.

            This field is a member of `oneof`_ ``connection_config``.
        secure_source_manager_instance_config (google.cloud.developerconnect_v1.types.SecureSourceManagerInstanceConfig):
            Configuration for connections to an instance
            of Secure Source Manager.

            This field is a member of `oneof`_ ``connection_config``.
        http_config (google.cloud.developerconnect_v1.types.GenericHTTPEndpointConfig):
            Optional. Configuration for connections to an
            HTTP service provider.

            This field is a member of `oneof`_ ``connection_config``.
        name (str):
            Identifier. The resource name of the connection, in the
            format
            ``projects/{project}/locations/{location}/connections/{connection_id}``.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. [Output only] Create timestamp
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. [Output only] Update timestamp
        delete_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. [Output only] Delete timestamp
        labels (MutableMapping[str, str]):
            Optional. Labels as key value pairs
        installation_state (google.cloud.developerconnect_v1.types.InstallationState):
            Output only. Installation state of the
            Connection.
        disabled (bool):
            Optional. If disabled is set to true,
            functionality is disabled for this connection.
            Repository based API methods and webhooks
            processing for repositories in this connection
            will be disabled.
        reconciling (bool):
            Output only. Set to true when the connection
            is being set up or updated in the background.
        annotations (MutableMapping[str, str]):
            Optional. Allows clients to store small
            amounts of arbitrary data.
        etag (str):
            Optional. This checksum is computed by the
            server based on the value of other fields, and
            may be sent on update and delete requests to
            ensure the client has an up-to-date value before
            proceeding.
        uid (str):
            Output only. A system-assigned unique
            identifier for the Connection.
        crypto_key_config (google.cloud.developerconnect_v1.types.CryptoKeyConfig):
            Optional. The crypto key configuration. This
            field is used by the Customer-Managed Encryption
            Keys (CMEK) feature.
        git_proxy_config (google.cloud.developerconnect_v1.types.GitProxyConfig):
            Optional. Configuration for the git proxy
            feature. Enabling the git proxy allows clients
            to perform git operations on the repositories
            linked in the connection.
    """

    github_config: "GitHubConfig" = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="connection_config",
        message="GitHubConfig",
    )
    github_enterprise_config: "GitHubEnterpriseConfig" = proto.Field(
        proto.MESSAGE,
        number=13,
        oneof="connection_config",
        message="GitHubEnterpriseConfig",
    )
    gitlab_config: "GitLabConfig" = proto.Field(
        proto.MESSAGE,
        number=14,
        oneof="connection_config",
        message="GitLabConfig",
    )
    gitlab_enterprise_config: "GitLabEnterpriseConfig" = proto.Field(
        proto.MESSAGE,
        number=16,
        oneof="connection_config",
        message="GitLabEnterpriseConfig",
    )
    bitbucket_data_center_config: "BitbucketDataCenterConfig" = proto.Field(
        proto.MESSAGE,
        number=17,
        oneof="connection_config",
        message="BitbucketDataCenterConfig",
    )
    bitbucket_cloud_config: "BitbucketCloudConfig" = proto.Field(
        proto.MESSAGE,
        number=18,
        oneof="connection_config",
        message="BitbucketCloudConfig",
    )
    secure_source_manager_instance_config: "SecureSourceManagerInstanceConfig" = (
        proto.Field(
            proto.MESSAGE,
            number=20,
            oneof="connection_config",
            message="SecureSourceManagerInstanceConfig",
        )
    )
    http_config: "GenericHTTPEndpointConfig" = proto.Field(
        proto.MESSAGE,
        number=21,
        oneof="connection_config",
        message="GenericHTTPEndpointConfig",
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
    delete_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=11,
        message=timestamp_pb2.Timestamp,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=4,
    )
    installation_state: "InstallationState" = proto.Field(
        proto.MESSAGE,
        number=6,
        message="InstallationState",
    )
    disabled: bool = proto.Field(
        proto.BOOL,
        number=7,
    )
    reconciling: bool = proto.Field(
        proto.BOOL,
        number=8,
    )
    annotations: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=9,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=10,
    )
    uid: str = proto.Field(
        proto.STRING,
        number=12,
    )
    crypto_key_config: "CryptoKeyConfig" = proto.Field(
        proto.MESSAGE,
        number=15,
        message="CryptoKeyConfig",
    )
    git_proxy_config: "GitProxyConfig" = proto.Field(
        proto.MESSAGE,
        number=19,
        message="GitProxyConfig",
    )


class CryptoKeyConfig(proto.Message):
    r"""The crypto key configuration. This field is used by the
    Customer-managed encryption keys (CMEK) feature.

    Attributes:
        key_reference (str):
            Required. The name of the key which is used to
            encrypt/decrypt customer data. For key in Cloud KMS, the key
            should be in the format of
            ``projects/*/locations/*/keyRings/*/cryptoKeys/*``.
    """

    key_reference: str = proto.Field(
        proto.STRING,
        number=1,
    )


class GitProxyConfig(proto.Message):
    r"""The git proxy configuration.

    Attributes:
        enabled (bool):
            Optional. Setting this to true allows the git
            proxy to be used for performing git operations
            on the repositories linked in the connection.
        http_proxy_base_uri (str):
            Output only. The base URI for the HTTP proxy endpoint. Has
            the format
            ``https://{generatedID}-c-h-{shortRegion}.developerconnect.dev``
            Populated only when enabled is set to true. This endpoint is
            used by other Google services that integrate with Developer
            Connect.
    """

    enabled: bool = proto.Field(
        proto.BOOL,
        number=1,
    )
    http_proxy_base_uri: str = proto.Field(
        proto.STRING,
        number=2,
    )


class InstallationState(proto.Message):
    r"""Describes stage and necessary actions to be taken by the
    user to complete the installation. Used for GitHub and GitHub
    Enterprise based connections.

    Attributes:
        stage (google.cloud.developerconnect_v1.types.InstallationState.Stage):
            Output only. Current step of the installation
            process.
        message (str):
            Output only. Message of what the user should
            do next to continue the installation. Empty
            string if the installation is already complete.
        action_uri (str):
            Output only. Link to follow for next action.
            Empty string if the installation is already
            complete.
    """

    class Stage(proto.Enum):
        r"""Stage of the installation process.

        Values:
            STAGE_UNSPECIFIED (0):
                No stage specified.
            PENDING_CREATE_APP (1):
                Only for GitHub Enterprise. An App creation
                has been requested. The user needs to confirm
                the creation in their GitHub enterprise host.
            PENDING_USER_OAUTH (2):
                User needs to authorize the GitHub (or
                Enterprise) App via OAuth.
            PENDING_INSTALL_APP (3):
                User needs to follow the link to install the
                GitHub (or Enterprise) App.
            COMPLETE (10):
                Installation process has been completed.
        """

        STAGE_UNSPECIFIED = 0
        PENDING_CREATE_APP = 1
        PENDING_USER_OAUTH = 2
        PENDING_INSTALL_APP = 3
        COMPLETE = 10

    stage: Stage = proto.Field(
        proto.ENUM,
        number=1,
        enum=Stage,
    )
    message: str = proto.Field(
        proto.STRING,
        number=2,
    )
    action_uri: str = proto.Field(
        proto.STRING,
        number=3,
    )


class GenericHTTPEndpointConfig(proto.Message):
    r"""Defines the configuration for connections to an HTTP service
    provider.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        basic_authentication (google.cloud.developerconnect_v1.types.GenericHTTPEndpointConfig.BasicAuthentication):
            Optional. Basic authentication with username
            and password.

            This field is a member of `oneof`_ ``authentication``.
        bearer_token_authentication (google.cloud.developerconnect_v1.types.GenericHTTPEndpointConfig.BearerTokenAuthentication):
            Optional. Bearer token authentication with a
            token.

            This field is a member of `oneof`_ ``authentication``.
        host_uri (str):
            Required. Immutable. The service provider's
            https endpoint.
        service_directory_config (google.cloud.developerconnect_v1.types.ServiceDirectoryConfig):
            Optional. Configuration for using Service
            Directory to privately connect to a HTTP service
            provider. This should only be set if the Http
            service provider is hosted on-premises and not
            reachable by public internet. If this field is
            left empty, calls to the HTTP service provider
            will be made over the public internet.
        ssl_ca_certificate (str):
            Optional. The SSL certificate to use for
            requests to the HTTP service provider.
    """

    class BasicAuthentication(proto.Message):
        r"""Basic authentication with username and password.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            password_secret_version (str):
                The password SecretManager secret version to
                authenticate as.

                This field is a member of `oneof`_ ``password``.
            username (str):
                Required. The username to authenticate as.
        """

        password_secret_version: str = proto.Field(
            proto.STRING,
            number=2,
            oneof="password",
        )
        username: str = proto.Field(
            proto.STRING,
            number=1,
        )

    class BearerTokenAuthentication(proto.Message):
        r"""Bearer token authentication with a token.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            token_secret_version (str):
                Optional. The token SecretManager secret
                version to authenticate as.

                This field is a member of `oneof`_ ``token``.
        """

        token_secret_version: str = proto.Field(
            proto.STRING,
            number=1,
            oneof="token",
        )

    basic_authentication: BasicAuthentication = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="authentication",
        message=BasicAuthentication,
    )
    bearer_token_authentication: BearerTokenAuthentication = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="authentication",
        message=BearerTokenAuthentication,
    )
    host_uri: str = proto.Field(
        proto.STRING,
        number=3,
    )
    service_directory_config: "ServiceDirectoryConfig" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="ServiceDirectoryConfig",
    )
    ssl_ca_certificate: str = proto.Field(
        proto.STRING,
        number=5,
    )


class GitHubConfig(proto.Message):
    r"""Configuration for connections to github.com.

    Attributes:
        github_app (google.cloud.developerconnect_v1.types.GitHubConfig.GitHubApp):
            Required. Immutable. The GitHub Application
            that was installed to the GitHub user or
            organization.
        authorizer_credential (google.cloud.developerconnect_v1.types.OAuthCredential):
            Optional. OAuth credential of the account
            that authorized the GitHub App. It is
            recommended to use a robot account instead of a
            human user account. The OAuth token must be tied
            to the GitHub App of this config.
        app_installation_id (int):
            Optional. GitHub App installation id.
        installation_uri (str):
            Output only. The URI to navigate to in order
            to manage the installation associated with this
            GitHubConfig.
    """

    class GitHubApp(proto.Enum):
        r"""Represents the various GitHub Applications that can be
        installed to a GitHub user or organization and used with
        Developer Connect.

        Values:
            GIT_HUB_APP_UNSPECIFIED (0):
                GitHub App not specified.
            DEVELOPER_CONNECT (1):
                The Developer Connect GitHub Application.
            FIREBASE (2):
                The Firebase GitHub Application.
            GEMINI_CODE_ASSIST (3):
                The Gemini Code Assist Application.
        """

        GIT_HUB_APP_UNSPECIFIED = 0
        DEVELOPER_CONNECT = 1
        FIREBASE = 2
        GEMINI_CODE_ASSIST = 3

    github_app: GitHubApp = proto.Field(
        proto.ENUM,
        number=1,
        enum=GitHubApp,
    )
    authorizer_credential: "OAuthCredential" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="OAuthCredential",
    )
    app_installation_id: int = proto.Field(
        proto.INT64,
        number=3,
    )
    installation_uri: str = proto.Field(
        proto.STRING,
        number=4,
    )


class GitHubEnterpriseConfig(proto.Message):
    r"""Configuration for connections to an instance of GitHub
    Enterprise.

    Attributes:
        host_uri (str):
            Required. The URI of the GitHub Enterprise
            host this connection is for.
        app_id (int):
            Optional. ID of the GitHub App created from
            the manifest.
        app_slug (str):
            Output only. The URL-friendly name of the
            GitHub App.
        private_key_secret_version (str):
            Optional. SecretManager resource containing the private key
            of the GitHub App, formatted as
            ``projects/*/secrets/*/versions/*`` or
            ``projects/*/locations/*/secrets/*/versions/*`` (if regional
            secrets are supported in that location).
        webhook_secret_secret_version (str):
            Optional. SecretManager resource containing the webhook
            secret of the GitHub App, formatted as
            ``projects/*/secrets/*/versions/*`` or
            ``projects/*/locations/*/secrets/*/versions/*`` (if regional
            secrets are supported in that location).
        app_installation_id (int):
            Optional. ID of the installation of the
            GitHub App.
        installation_uri (str):
            Output only. The URI to navigate to in order
            to manage the installation associated with this
            GitHubEnterpriseConfig.
        service_directory_config (google.cloud.developerconnect_v1.types.ServiceDirectoryConfig):
            Optional. Configuration for using Service
            Directory to privately connect to a GitHub
            Enterprise server. This should only be set if
            the GitHub Enterprise server is hosted
            on-premises and not reachable by public
            internet. If this field is left empty, calls to
            the GitHub Enterprise server will be made over
            the public internet.
        server_version (str):
            Output only. GitHub Enterprise version installed at the
            host_uri.
        ssl_ca_certificate (str):
            Optional. SSL certificate to use for requests
            to GitHub Enterprise.
        organization (str):
            Optional. Immutable. GitHub Enterprise
            organization in which the GitHub App is created.
    """

    host_uri: str = proto.Field(
        proto.STRING,
        number=1,
    )
    app_id: int = proto.Field(
        proto.INT64,
        number=2,
    )
    app_slug: str = proto.Field(
        proto.STRING,
        number=3,
    )
    private_key_secret_version: str = proto.Field(
        proto.STRING,
        number=4,
    )
    webhook_secret_secret_version: str = proto.Field(
        proto.STRING,
        number=5,
    )
    app_installation_id: int = proto.Field(
        proto.INT64,
        number=8,
    )
    installation_uri: str = proto.Field(
        proto.STRING,
        number=9,
    )
    service_directory_config: "ServiceDirectoryConfig" = proto.Field(
        proto.MESSAGE,
        number=10,
        message="ServiceDirectoryConfig",
    )
    server_version: str = proto.Field(
        proto.STRING,
        number=12,
    )
    ssl_ca_certificate: str = proto.Field(
        proto.STRING,
        number=14,
    )
    organization: str = proto.Field(
        proto.STRING,
        number=15,
    )


class ServiceDirectoryConfig(proto.Message):
    r"""ServiceDirectoryConfig represents Service Directory
    configuration for a connection.

    Attributes:
        service (str):
            Required. The Service Directory service name.
            Format:

            projects/{project}/locations/{location}/namespaces/{namespace}/services/{service}.
    """

    service: str = proto.Field(
        proto.STRING,
        number=1,
    )


class OAuthCredential(proto.Message):
    r"""Represents an OAuth token of the account that authorized the
    Connection, and associated metadata.

    Attributes:
        oauth_token_secret_version (str):
            Required. A SecretManager resource containing the OAuth
            token that authorizes the connection. Format:
            ``projects/*/secrets/*/versions/*`` or
            ``projects/*/locations/*/secrets/*/versions/*`` (if regional
            secrets are supported in that location).
        username (str):
            Output only. The username associated with
            this token.
    """

    oauth_token_secret_version: str = proto.Field(
        proto.STRING,
        number=1,
    )
    username: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GitLabConfig(proto.Message):
    r"""Configuration for connections to gitlab.com.

    Attributes:
        webhook_secret_secret_version (str):
            Required. Immutable. SecretManager resource containing the
            webhook secret of a GitLab project, formatted as
            ``projects/*/secrets/*/versions/*`` or
            ``projects/*/locations/*/secrets/*/versions/*`` (if regional
            secrets are supported in that location). This is used to
            validate webhooks.
        read_authorizer_credential (google.cloud.developerconnect_v1.types.UserCredential):
            Required. A GitLab personal access token with the minimum
            ``read_api`` scope access and a minimum role of
            ``reporter``. The GitLab Projects visible to this Personal
            Access Token will control which Projects Developer Connect
            has access to.
        authorizer_credential (google.cloud.developerconnect_v1.types.UserCredential):
            Required. A GitLab personal access token with the minimum
            ``api`` scope access and a minimum role of ``maintainer``.
            The GitLab Projects visible to this Personal Access Token
            will control which Projects Developer Connect has access to.
    """

    webhook_secret_secret_version: str = proto.Field(
        proto.STRING,
        number=1,
    )
    read_authorizer_credential: "UserCredential" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="UserCredential",
    )
    authorizer_credential: "UserCredential" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="UserCredential",
    )


class UserCredential(proto.Message):
    r"""Represents a personal access token that authorized the
    Connection, and associated metadata.

    Attributes:
        user_token_secret_version (str):
            Required. A SecretManager resource containing the user token
            that authorizes the Developer Connect connection. Format:
            ``projects/*/secrets/*/versions/*`` or
            ``projects/*/locations/*/secrets/*/versions/*`` (if regional
            secrets are supported in that location).
        username (str):
            Output only. The username associated with
            this token.
    """

    user_token_secret_version: str = proto.Field(
        proto.STRING,
        number=1,
    )
    username: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GitLabEnterpriseConfig(proto.Message):
    r"""Configuration for connections to an instance of GitLab
    Enterprise.

    Attributes:
        host_uri (str):
            Required. The URI of the GitLab Enterprise
            host this connection is for.
        webhook_secret_secret_version (str):
            Required. Immutable. SecretManager resource containing the
            webhook secret of a GitLab project, formatted as
            ``projects/*/secrets/*/versions/*`` or
            ``projects/*/locations/*/secrets/*/versions/*`` (if regional
            secrets are supported in that location). This is used to
            validate webhooks.
        read_authorizer_credential (google.cloud.developerconnect_v1.types.UserCredential):
            Required. A GitLab personal access token with the minimum
            ``read_api`` scope access and a minimum role of
            ``reporter``. The GitLab Projects visible to this Personal
            Access Token will control which Projects Developer Connect
            has access to.
        authorizer_credential (google.cloud.developerconnect_v1.types.UserCredential):
            Required. A GitLab personal access token with the minimum
            ``api`` scope access and a minimum role of ``maintainer``.
            The GitLab Projects visible to this Personal Access Token
            will control which Projects Developer Connect has access to.
        service_directory_config (google.cloud.developerconnect_v1.types.ServiceDirectoryConfig):
            Optional. Configuration for using Service
            Directory to privately connect to a GitLab
            Enterprise instance. This should only be set if
            the GitLab Enterprise server is hosted
            on-premises and not reachable by public
            internet. If this field is left empty, calls to
            the GitLab Enterprise server will be made over
            the public internet.
        ssl_ca_certificate (str):
            Optional. SSL Certificate Authority
            certificate to use for requests to GitLab
            Enterprise instance.
        server_version (str):
            Output only. Version of the GitLab Enterprise server running
            on the ``host_uri``.
    """

    host_uri: str = proto.Field(
        proto.STRING,
        number=1,
    )
    webhook_secret_secret_version: str = proto.Field(
        proto.STRING,
        number=2,
    )
    read_authorizer_credential: "UserCredential" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="UserCredential",
    )
    authorizer_credential: "UserCredential" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="UserCredential",
    )
    service_directory_config: "ServiceDirectoryConfig" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="ServiceDirectoryConfig",
    )
    ssl_ca_certificate: str = proto.Field(
        proto.STRING,
        number=6,
    )
    server_version: str = proto.Field(
        proto.STRING,
        number=7,
    )


class BitbucketDataCenterConfig(proto.Message):
    r"""Configuration for connections to an instance of Bitbucket
    Data Center.

    Attributes:
        host_uri (str):
            Required. The URI of the Bitbucket Data
            Center host this connection is for.
        webhook_secret_secret_version (str):
            Required. Immutable. SecretManager resource containing the
            webhook secret used to verify webhook events, formatted as
            ``projects/*/secrets/*/versions/*`` or
            ``projects/*/locations/*/secrets/*/versions/*`` (if regional
            secrets are supported in that location). This is used to
            validate webhooks.
        read_authorizer_credential (google.cloud.developerconnect_v1.types.UserCredential):
            Required. An http access token with the minimum
            ``Repository read`` access. It's recommended to use a system
            account to generate the credentials.
        authorizer_credential (google.cloud.developerconnect_v1.types.UserCredential):
            Required. An http access token with the minimum
            ``Repository admin`` scope access. This is needed to create
            webhooks. It's recommended to use a system account to
            generate these credentials.
        service_directory_config (google.cloud.developerconnect_v1.types.ServiceDirectoryConfig):
            Optional. Configuration for using Service
            Directory to privately connect to a Bitbucket
            Data Center instance. This should only be set if
            the Bitbucket Data Center is hosted on-premises
            and not reachable by public internet. If this
            field is left empty, calls to the Bitbucket Data
            Center will be made over the public internet.
        ssl_ca_certificate (str):
            Optional. SSL certificate authority to trust
            when making requests to Bitbucket Data Center.
        server_version (str):
            Output only. Version of the Bitbucket Data Center server
            running on the ``host_uri``.
    """

    host_uri: str = proto.Field(
        proto.STRING,
        number=1,
    )
    webhook_secret_secret_version: str = proto.Field(
        proto.STRING,
        number=2,
    )
    read_authorizer_credential: "UserCredential" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="UserCredential",
    )
    authorizer_credential: "UserCredential" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="UserCredential",
    )
    service_directory_config: "ServiceDirectoryConfig" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="ServiceDirectoryConfig",
    )
    ssl_ca_certificate: str = proto.Field(
        proto.STRING,
        number=6,
    )
    server_version: str = proto.Field(
        proto.STRING,
        number=7,
    )


class BitbucketCloudConfig(proto.Message):
    r"""Configuration for connections to an instance of Bitbucket
    Cloud.

    Attributes:
        workspace (str):
            Required. The Bitbucket Cloud Workspace ID to
            be connected to Google Cloud Platform.
        webhook_secret_secret_version (str):
            Required. Immutable. SecretManager resource containing the
            webhook secret used to verify webhook events, formatted as
            ``projects/*/secrets/*/versions/*`` or
            ``projects/*/locations/*/secrets/*/versions/*`` (if regional
            secrets are supported in that location). This is used to
            validate and create webhooks.
        read_authorizer_credential (google.cloud.developerconnect_v1.types.UserCredential):
            Required. An access token with the minimum ``repository``
            access. It can either be a workspace, project or repository
            access token. It's recommended to use a system account to
            generate the credentials.
        authorizer_credential (google.cloud.developerconnect_v1.types.UserCredential):
            Required. An access token with the minimum ``repository``,
            ``pullrequest`` and ``webhook`` scope access. It can either
            be a workspace, project or repository access token. This is
            needed to create webhooks. It's recommended to use a system
            account to generate these credentials.
    """

    workspace: str = proto.Field(
        proto.STRING,
        number=1,
    )
    webhook_secret_secret_version: str = proto.Field(
        proto.STRING,
        number=2,
    )
    read_authorizer_credential: "UserCredential" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="UserCredential",
    )
    authorizer_credential: "UserCredential" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="UserCredential",
    )


class SecureSourceManagerInstanceConfig(proto.Message):
    r"""Configuration for connections to Secure Source Manager
    instance

    Attributes:
        instance (str):
            Required. Immutable. Secure Source Manager instance
            resource, formatted as
            ``projects/*/locations/*/instances/*``
    """

    instance: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListConnectionsRequest(proto.Message):
    r"""Message for requesting list of Connections

    Attributes:
        parent (str):
            Required. Parent value for
            ListConnectionsRequest
        page_size (int):
            Optional. Requested page size. Server may
            return fewer items than requested. If
            unspecified, server will pick an appropriate
            default.
        page_token (str):
            Optional. A token identifying a page of
            results the server should return.
        filter (str):
            Optional. Filtering results
        order_by (str):
            Optional. Hint for how to order the results
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


class ListConnectionsResponse(proto.Message):
    r"""Message for response to listing Connections

    Attributes:
        connections (MutableSequence[google.cloud.developerconnect_v1.types.Connection]):
            The list of Connection
        next_page_token (str):
            A token identifying a page of results the
            server should return.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    connections: MutableSequence["Connection"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Connection",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetConnectionRequest(proto.Message):
    r"""Message for getting a Connection

    Attributes:
        name (str):
            Required. Name of the resource
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateConnectionRequest(proto.Message):
    r"""Message for creating a Connection

    Attributes:
        parent (str):
            Required. Value for parent.
        connection_id (str):
            Required. Id of the requesting object If auto-generating Id
            server-side, remove this field and connection_id from the
            method_signature of Create RPC
        connection (google.cloud.developerconnect_v1.types.Connection):
            Required. The resource being created
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
        validate_only (bool):
            Optional. If set, validate the request, but
            do not actually post it.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    connection_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    connection: "Connection" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="Connection",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=5,
    )


class UpdateConnectionRequest(proto.Message):
    r"""Message for updating a Connection

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. Field mask is used to specify the fields to be
            overwritten in the Connection resource by the update. The
            fields specified in the update_mask are relative to the
            resource, not the full request. A field will be overwritten
            if it is in the mask. If the user does not provide a mask
            then all fields will be overwritten.
        connection (google.cloud.developerconnect_v1.types.Connection):
            Required. The resource being updated
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
        allow_missing (bool):
            Optional. If set to true, and the connection is not found a
            new connection will be created. In this situation
            ``update_mask`` is ignored. The creation will succeed only
            if the input connection has all the necessary information
            (e.g a github_config with both user_oauth_token and
            installation_id properties).
        validate_only (bool):
            Optional. If set, validate the request, but
            do not actually post it.
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    connection: "Connection" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Connection",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )
    allow_missing: bool = proto.Field(
        proto.BOOL,
        number=4,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=5,
    )


class DeleteConnectionRequest(proto.Message):
    r"""Message for deleting a Connection

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
        validate_only (bool):
            Optional. If set, validate the request, but
            do not actually post it.
        etag (str):
            Optional. The current etag of the Connection.
            If an etag is provided and does not match the
            current etag of the Connection, deletion will be
            blocked and an ABORTED error will be returned.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=3,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=4,
    )


class ListAccountConnectorsRequest(proto.Message):
    r"""Message for requesting list of AccountConnectors

    Attributes:
        parent (str):
            Required. Parent value for
            ListAccountConnectorsRequest
        page_size (int):
            Optional. Requested page size. Server may
            return fewer items than requested. If
            unspecified, server will pick an appropriate
            default.
        page_token (str):
            Optional. A token identifying a page of
            results the server should return.
        filter (str):
            Optional. Filtering results
        order_by (str):
            Optional. Hint for how to order the results
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


class ListAccountConnectorsResponse(proto.Message):
    r"""Message for response to listing AccountConnectors

    Attributes:
        account_connectors (MutableSequence[google.cloud.developerconnect_v1.types.AccountConnector]):
            The list of AccountConnectors
        next_page_token (str):
            A token identifying a page of results the
            server should return.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    account_connectors: MutableSequence["AccountConnector"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="AccountConnector",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetAccountConnectorRequest(proto.Message):
    r"""Message for getting a AccountConnector

    Attributes:
        name (str):
            Required. Name of the resource
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateAccountConnectorRequest(proto.Message):
    r"""

    Attributes:
        parent (str):
            Required. Location resource name as the account_connector’s
            parent.
        account_connector_id (str):
            Required. The ID to use for the
            AccountConnector, which will become the final
            component of the AccountConnector's resource
            name. Its format should adhere to
            https://google.aip.dev/122#resource-id-segments
            Names must be unique per-project per-location.
        account_connector (google.cloud.developerconnect_v1.types.AccountConnector):
            Required. The AccountConnector to create.
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
        validate_only (bool):
            Optional. If set, validate the request, but
            do not actually post it.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    account_connector_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    account_connector: "AccountConnector" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="AccountConnector",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=5,
    )


class UpdateAccountConnectorRequest(proto.Message):
    r"""Message for updating a AccountConnector

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. The list of fields to be updated.
        account_connector (google.cloud.developerconnect_v1.types.AccountConnector):
            Required. The AccountConnector to update.
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
        allow_missing (bool):
            Optional. If set to true, and the accountConnector is not
            found a new accountConnector will be created. In this
            situation ``update_mask`` is ignored. The creation will
            succeed only if the input accountConnector has all the
            necessary
        validate_only (bool):
            Optional. If set, validate the request, but
            do not actually post it.
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    account_connector: "AccountConnector" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="AccountConnector",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )
    allow_missing: bool = proto.Field(
        proto.BOOL,
        number=4,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=5,
    )


class DeleteAccountConnectorRequest(proto.Message):
    r"""Message for deleting a AccountConnector

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
        validate_only (bool):
            Optional. If set, validate the request, but
            do not actually post it.
        etag (str):
            Optional. The current etag of the
            AccountConnectorn. If an etag is provided and
            does not match the current etag of the
            AccountConnector, deletion will be blocked and
            an ABORTED error will be returned.
        force (bool):
            Optional. If set to true, any Users from this
            AccountConnector will also be deleted.
            (Otherwise, the request will only work if the
            AccountConnector has no Users.)
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=3,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=4,
    )
    force: bool = proto.Field(
        proto.BOOL,
        number=5,
    )


class DeleteUserRequest(proto.Message):
    r"""Message for deleting a User

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
        validate_only (bool):
            Optional. If set, validate the request, but
            do not actually post it.
        etag (str):
            Optional. This checksum is computed by the
            server based on the value of other fields, and
            may be sent on update and delete requests to
            ensure the client has an up-to-date value before
            proceeding.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=3,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=4,
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
        target (str):
            Output only. Server-defined resource path for
            the target of the operation.
        verb (str):
            Output only. Name of the verb executed by the
            operation.
        status_message (str):
            Output only. Human-readable status of the
            operation, if any.
        requested_cancellation (bool):
            Output only. Identifies whether the user has requested
            cancellation of the operation. Operations that have been
            cancelled successfully have
            [google.longrunning.Operation.error][google.longrunning.Operation.error]
            value with a
            [google.rpc.Status.code][google.rpc.Status.code] of 1,
            corresponding to ``Code.CANCELLED``.
        api_version (str):
            Output only. API version used to start the
            operation.
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
    status_message: str = proto.Field(
        proto.STRING,
        number=5,
    )
    requested_cancellation: bool = proto.Field(
        proto.BOOL,
        number=6,
    )
    api_version: str = proto.Field(
        proto.STRING,
        number=7,
    )


class FetchSelfRequest(proto.Message):
    r"""Message for fetching a User of the user themselves.

    Attributes:
        name (str):
            Required. Name of the AccountConnector
            resource
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class DeleteSelfRequest(proto.Message):
    r"""Message for deleting a User of the user themselves.

    Attributes:
        name (str):
            Required. Name of the AccountConnector
            resource
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class FetchAccessTokenRequest(proto.Message):
    r"""Message for fetching an OAuth access token.

    Attributes:
        account_connector (str):
            Required. The resource name of the AccountConnector in the
            format ``projects/*/locations/*/accountConnectors/*``.
    """

    account_connector: str = proto.Field(
        proto.STRING,
        number=1,
    )


class FetchAccessTokenResponse(proto.Message):
    r"""Message for responding to getting an OAuth access token.

    Attributes:
        token (str):
            The token content.
        expiration_time (google.protobuf.timestamp_pb2.Timestamp):
            Expiration timestamp. Can be empty if unknown
            or non-expiring.
        scopes (MutableSequence[str]):
            The scopes of the access token.
        exchange_error (google.cloud.developerconnect_v1.types.ExchangeError):
            The error resulted from exchanging OAuth
            tokens from the service provider.
    """

    token: str = proto.Field(
        proto.STRING,
        number=1,
    )
    expiration_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    scopes: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )
    exchange_error: "ExchangeError" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="ExchangeError",
    )


class StartOAuthRequest(proto.Message):
    r"""Message for starting an OAuth flow.

    Attributes:
        account_connector (str):
            Required. The resource name of the AccountConnector in the
            format ``projects/*/locations/*/accountConnectors/*``.
    """

    account_connector: str = proto.Field(
        proto.STRING,
        number=1,
    )


class StartOAuthResponse(proto.Message):
    r"""Message for responding to starting an OAuth flow.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        system_provider_id (google.cloud.developerconnect_v1.types.SystemProvider):
            The ID of the system provider.

            This field is a member of `oneof`_ ``id``.
        ticket (str):
            The ticket to be used for post processing the
            callback from the service provider.
        code_challenge (str):
            Please refer to
            https://datatracker.ietf.org/doc/html/rfc7636#section-4.1
        code_challenge_method (str):
            Please refer to
            https://datatracker.ietf.org/doc/html/rfc7636#section-4.2
        client_id (str):
            The client ID to the OAuth App of the service
            provider.
        scopes (MutableSequence[str]):
            The list of scopes requested by the
            application.
        auth_uri (str):
            The authorization server URL to the OAuth
            flow of the service provider.
    """

    system_provider_id: "SystemProvider" = proto.Field(
        proto.ENUM,
        number=7,
        oneof="id",
        enum="SystemProvider",
    )
    ticket: str = proto.Field(
        proto.STRING,
        number=1,
    )
    code_challenge: str = proto.Field(
        proto.STRING,
        number=2,
    )
    code_challenge_method: str = proto.Field(
        proto.STRING,
        number=3,
    )
    client_id: str = proto.Field(
        proto.STRING,
        number=4,
    )
    scopes: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=5,
    )
    auth_uri: str = proto.Field(
        proto.STRING,
        number=6,
    )


class FinishOAuthRequest(proto.Message):
    r"""Message for finishing an OAuth flow.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        oauth_params (google.cloud.developerconnect_v1.types.FinishOAuthRequest.OAuthParams):
            The params returned by non-Google OAuth 2.0
            flow redirect.

            This field is a member of `oneof`_ ``params``.
        google_oauth_params (google.cloud.developerconnect_v1.types.FinishOAuthRequest.GoogleOAuthParams):
            The params returned by Google OAuth flow
            redirects.

            This field is a member of `oneof`_ ``params``.
        account_connector (str):
            Required. The resource name of the AccountConnector in the
            format ``projects/*/locations/*/accountConnectors/*``.
    """

    class OAuthParams(proto.Message):
        r"""The params returned by non-Google OAuth 2.0 flow redirect.

        Attributes:
            code (str):
                Required. The code to be used for getting the
                token from SCM provider.
            ticket (str):
                Required. The ticket to be used for post
                processing the callback from SCM provider.
        """

        code: str = proto.Field(
            proto.STRING,
            number=1,
        )
        ticket: str = proto.Field(
            proto.STRING,
            number=2,
        )

    class GoogleOAuthParams(proto.Message):
        r"""The params returned by Google OAuth flow redirects.

        Attributes:
            scopes (MutableSequence[str]):
                Required. The scopes returned by Google OAuth
                flow.
            version_info (str):
                Optional. The version info returned by Google
                OAuth flow.
            ticket (str):
                Required. The ticket to be used for post
                processing the callback from Google OAuth flow.
        """

        scopes: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=1,
        )
        version_info: str = proto.Field(
            proto.STRING,
            number=2,
        )
        ticket: str = proto.Field(
            proto.STRING,
            number=3,
        )

    oauth_params: OAuthParams = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="params",
        message=OAuthParams,
    )
    google_oauth_params: GoogleOAuthParams = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="params",
        message=GoogleOAuthParams,
    )
    account_connector: str = proto.Field(
        proto.STRING,
        number=1,
    )


class FinishOAuthResponse(proto.Message):
    r"""Message for responding to finishing an OAuth flow.

    Attributes:
        exchange_error (google.cloud.developerconnect_v1.types.ExchangeError):
            The error resulted from exchanging OAuth
            tokens from the service provider.
    """

    exchange_error: "ExchangeError" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="ExchangeError",
    )


class ExchangeError(proto.Message):
    r"""Message for representing an error from exchanging OAuth
    tokens.

    Attributes:
        code (str):
            https://datatracker.ietf.org/doc/html/rfc6749#section-5.2
            - error
        description (str):
            https://datatracker.ietf.org/doc/html/rfc6749#section-5.2 -
            error_description
    """

    code: str = proto.Field(
        proto.STRING,
        number=1,
    )
    description: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GitRepositoryLink(proto.Message):
    r"""Message describing the GitRepositoryLink object

    Attributes:
        name (str):
            Identifier. Resource name of the repository, in the format
            ``projects/*/locations/*/connections/*/gitRepositoryLinks/*``.
        clone_uri (str):
            Required. Git Clone URI.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. [Output only] Create timestamp
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. [Output only] Update timestamp
        delete_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. [Output only] Delete timestamp
        labels (MutableMapping[str, str]):
            Optional. Labels as key value pairs
        etag (str):
            Optional. This checksum is computed by the
            server based on the value of other fields, and
            may be sent on update and delete requests to
            ensure the client has an up-to-date value before
            proceeding.
        reconciling (bool):
            Output only. Set to true when the connection
            is being set up or updated in the background.
        annotations (MutableMapping[str, str]):
            Optional. Allows clients to store small
            amounts of arbitrary data.
        uid (str):
            Output only. A system-assigned unique
            identifier for the GitRepositoryLink.
        webhook_id (str):
            Output only. External ID of the webhook
            created for the repository.
        git_proxy_uri (str):
            Output only. URI to access the linked
            repository through the Git Proxy. This field is
            only populated if the git proxy is enabled for
            the connection.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    clone_uri: str = proto.Field(
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
    delete_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=6,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=7,
    )
    reconciling: bool = proto.Field(
        proto.BOOL,
        number=8,
    )
    annotations: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=9,
    )
    uid: str = proto.Field(
        proto.STRING,
        number=10,
    )
    webhook_id: str = proto.Field(
        proto.STRING,
        number=11,
    )
    git_proxy_uri: str = proto.Field(
        proto.STRING,
        number=12,
    )


class CreateGitRepositoryLinkRequest(proto.Message):
    r"""Message for creating a GitRepositoryLink

    Attributes:
        parent (str):
            Required. Value for parent.
        git_repository_link (google.cloud.developerconnect_v1.types.GitRepositoryLink):
            Required. The resource being created
        git_repository_link_id (str):
            Required. The ID to use for the repository, which will
            become the final component of the repository's resource
            name. This ID should be unique in the connection. Allows
            alphanumeric characters and any of -.\_~%!$&'()*+,;=@.
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
        validate_only (bool):
            Optional. If set, validate the request, but
            do not actually post it.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    git_repository_link: "GitRepositoryLink" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="GitRepositoryLink",
    )
    git_repository_link_id: str = proto.Field(
        proto.STRING,
        number=3,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=5,
    )


class DeleteGitRepositoryLinkRequest(proto.Message):
    r"""Message for deleting a GitRepositoryLink

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
        validate_only (bool):
            Optional. If set, validate the request, but
            do not actually post it.
        etag (str):
            Optional. This checksum is computed by the
            server based on the value of other fields, and
            may be sent on update and delete requests to
            ensure the client has an up-to-date value before
            proceeding.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=3,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=4,
    )


class ListGitRepositoryLinksRequest(proto.Message):
    r"""Message for requesting a list of GitRepositoryLinks

    Attributes:
        parent (str):
            Required. Parent value for
            ListGitRepositoryLinksRequest
        page_size (int):
            Optional. Requested page size. Server may
            return fewer items than requested. If
            unspecified, server will pick an appropriate
            default.
        page_token (str):
            Optional. A token identifying a page of
            results the server should return.
        filter (str):
            Optional. Filtering results
        order_by (str):
            Optional. Hint for how to order the results
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


class ListGitRepositoryLinksResponse(proto.Message):
    r"""Message for response to listing GitRepositoryLinks

    Attributes:
        git_repository_links (MutableSequence[google.cloud.developerconnect_v1.types.GitRepositoryLink]):
            The list of GitRepositoryLinks
        next_page_token (str):
            A token identifying a page of results the
            server should return.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    git_repository_links: MutableSequence["GitRepositoryLink"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="GitRepositoryLink",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetGitRepositoryLinkRequest(proto.Message):
    r"""Message for getting a GitRepositoryLink

    Attributes:
        name (str):
            Required. Name of the resource
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class FetchReadWriteTokenRequest(proto.Message):
    r"""Message for fetching SCM read/write token.

    Attributes:
        git_repository_link (str):
            Required. The resource name of the gitRepositoryLink in the
            format
            ``projects/*/locations/*/connections/*/gitRepositoryLinks/*``.
    """

    git_repository_link: str = proto.Field(
        proto.STRING,
        number=1,
    )


class FetchReadTokenRequest(proto.Message):
    r"""Message for fetching SCM read token.

    Attributes:
        git_repository_link (str):
            Required. The resource name of the gitRepositoryLink in the
            format
            ``projects/*/locations/*/connections/*/gitRepositoryLinks/*``.
    """

    git_repository_link: str = proto.Field(
        proto.STRING,
        number=1,
    )


class FetchReadTokenResponse(proto.Message):
    r"""Message for responding to get read token.

    Attributes:
        token (str):
            The token content.
        expiration_time (google.protobuf.timestamp_pb2.Timestamp):
            Expiration timestamp. Can be empty if unknown
            or non-expiring.
        git_username (str):
            The git_username to specify when making a git clone with the
            token. For example, for GitHub GitRepositoryLinks, this
            would be "x-access-token".
    """

    token: str = proto.Field(
        proto.STRING,
        number=1,
    )
    expiration_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    git_username: str = proto.Field(
        proto.STRING,
        number=3,
    )


class FetchReadWriteTokenResponse(proto.Message):
    r"""Message for responding to get read/write token.

    Attributes:
        token (str):
            The token content.
        expiration_time (google.protobuf.timestamp_pb2.Timestamp):
            Expiration timestamp. Can be empty if unknown
            or non-expiring.
        git_username (str):
            The git_username to specify when making a git clone with the
            token. For example, for GitHub GitRepositoryLinks, this
            would be "x-access-token".
    """

    token: str = proto.Field(
        proto.STRING,
        number=1,
    )
    expiration_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    git_username: str = proto.Field(
        proto.STRING,
        number=3,
    )


class FetchLinkableGitRepositoriesRequest(proto.Message):
    r"""Request message for FetchLinkableGitRepositoriesRequest.

    Attributes:
        connection (str):
            Required. The name of the Connection. Format:
            ``projects/*/locations/*/connections/*``.
        page_size (int):
            Optional. Number of results to return in the
            list. Defaults to 20.
        page_token (str):
            Optional. Page start.
    """

    connection: str = proto.Field(
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


class FetchLinkableGitRepositoriesResponse(proto.Message):
    r"""Response message for FetchLinkableGitRepositories.

    Attributes:
        linkable_git_repositories (MutableSequence[google.cloud.developerconnect_v1.types.LinkableGitRepository]):
            The git repositories that can be linked to
            the connection.
        next_page_token (str):
            A token identifying a page of results the
            server should return.
    """

    @property
    def raw_page(self):
        return self

    linkable_git_repositories: MutableSequence["LinkableGitRepository"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="LinkableGitRepository",
        )
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class LinkableGitRepository(proto.Message):
    r"""LinkableGitRepository represents a git repository that can be
    linked to a connection.

    Attributes:
        clone_uri (str):
            The clone uri of the repository.
    """

    clone_uri: str = proto.Field(
        proto.STRING,
        number=1,
    )


class FetchGitHubInstallationsRequest(proto.Message):
    r"""Request for fetching github installations.

    Attributes:
        connection (str):
            Required. The resource name of the connection in the format
            ``projects/*/locations/*/connections/*``.
    """

    connection: str = proto.Field(
        proto.STRING,
        number=1,
    )


class FetchGitHubInstallationsResponse(proto.Message):
    r"""Response of fetching github installations.

    Attributes:
        installations (MutableSequence[google.cloud.developerconnect_v1.types.FetchGitHubInstallationsResponse.Installation]):
            List of installations available to the OAuth
            user (for github.com) or all the installations
            (for GitHub enterprise).
    """

    class Installation(proto.Message):
        r"""Represents an installation of the GitHub App.

        Attributes:
            id (int):
                ID of the installation in GitHub.
            name (str):
                Name of the GitHub user or organization that
                owns this installation.
            type_ (str):
                Either "user" or "organization".
        """

        id: int = proto.Field(
            proto.INT64,
            number=1,
        )
        name: str = proto.Field(
            proto.STRING,
            number=2,
        )
        type_: str = proto.Field(
            proto.STRING,
            number=3,
        )

    installations: MutableSequence[Installation] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=Installation,
    )


class FetchGitRefsRequest(proto.Message):
    r"""Request for fetching git refs.

    Attributes:
        git_repository_link (str):
            Required. The resource name of GitRepositoryLink in the
            format
            ``projects/*/locations/*/connections/*/gitRepositoryLinks/*``.
        ref_type (google.cloud.developerconnect_v1.types.FetchGitRefsRequest.RefType):
            Required. Type of refs to fetch.
        page_size (int):
            Optional. Number of results to return in the
            list. Default to 20.
        page_token (str):
            Optional. Page start.
    """

    class RefType(proto.Enum):
        r"""Type of refs.

        Values:
            REF_TYPE_UNSPECIFIED (0):
                No type specified.
            TAG (1):
                To fetch tags.
            BRANCH (2):
                To fetch branches.
        """

        REF_TYPE_UNSPECIFIED = 0
        TAG = 1
        BRANCH = 2

    git_repository_link: str = proto.Field(
        proto.STRING,
        number=1,
    )
    ref_type: RefType = proto.Field(
        proto.ENUM,
        number=2,
        enum=RefType,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=4,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=5,
    )


class FetchGitRefsResponse(proto.Message):
    r"""Response for fetching git refs.

    Attributes:
        ref_names (MutableSequence[str]):
            Name of the refs fetched.
        next_page_token (str):
            A token identifying a page of results the
            server should return.
    """

    @property
    def raw_page(self):
        return self

    ref_names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class AccountConnector(proto.Message):
    r"""AccountConnector encapsulates what a platform administrator
    needs to configure for users to connect to the service
    providers, which includes, among other fields, the OAuth client
    ID, client secret, and authorization and token endpoints.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        provider_oauth_config (google.cloud.developerconnect_v1.types.ProviderOAuthConfig):
            Optional. Provider OAuth config.

            This field is a member of `oneof`_ ``account_connector_config``.
        name (str):
            Identifier. The resource name of the accountConnector, in
            the format
            ``projects/{project}/locations/{location}/accountConnectors/{account_connector_id}``.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp when the
            accountConnector was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp when the
            accountConnector was updated.
        annotations (MutableMapping[str, str]):
            Optional. Allows users to store small amounts
            of arbitrary data.
        etag (str):
            Optional. This checksum is computed by the
            server based on the value of other fields, and
            may be sent on update and delete requests to
            ensure the client has an up-to-date value before
            proceeding.
        labels (MutableMapping[str, str]):
            Optional. Labels as key value pairs
        oauth_start_uri (str):
            Output only. Start OAuth flow by clicking on
            this URL.
    """

    provider_oauth_config: "ProviderOAuthConfig" = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="account_connector_config",
        message="ProviderOAuthConfig",
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
    annotations: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=6,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=7,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=8,
    )
    oauth_start_uri: str = proto.Field(
        proto.STRING,
        number=10,
    )


class User(proto.Message):
    r"""User represents a user connected to the service providers
    through a AccountConnector.

    Attributes:
        name (str):
            Identifier. Resource name of the user, in the format
            ``projects/*/locations/*/accountConnectors/*/users/*``.
        display_name (str):
            Output only. Developer Connect automatically
            converts user identity to some human readable
            description, e.g., email address.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp when the user was
            created.
        last_token_request_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp when the token was
            last requested.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    last_token_request_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )


class ProviderOAuthConfig(proto.Message):
    r"""ProviderOAuthConfig is the OAuth config for a provider.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        system_provider_id (google.cloud.developerconnect_v1.types.SystemProvider):
            Optional. Immutable. Developer Connect
            provided OAuth.

            This field is a member of `oneof`_ ``oauth_provider_id``.
        scopes (MutableSequence[str]):
            Required. User selected scopes to apply to
            the Oauth config In the event of changing
            scopes, user records under AccountConnector will
            be deleted and users will re-auth again.
    """

    system_provider_id: "SystemProvider" = proto.Field(
        proto.ENUM,
        number=1,
        oneof="oauth_provider_id",
        enum="SystemProvider",
    )
    scopes: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
