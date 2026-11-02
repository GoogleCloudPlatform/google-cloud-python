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

import google.api.httpbody_pb2 as httpbody_pb2  # type: ignore
import google.protobuf.field_mask_pb2 as field_mask_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.devtools.cloudbuild.v2",
    manifest={
        "Connection",
        "InstallationState",
        "FetchLinkableRepositoriesRequest",
        "FetchLinkableRepositoriesResponse",
        "GitHubConfig",
        "GitHubEnterpriseConfig",
        "GitLabConfig",
        "BitbucketDataCenterConfig",
        "BitbucketCloudConfig",
        "ServiceDirectoryConfig",
        "Repository",
        "OAuthCredential",
        "UserCredential",
        "CreateConnectionRequest",
        "GetConnectionRequest",
        "ListConnectionsRequest",
        "ListConnectionsResponse",
        "UpdateConnectionRequest",
        "DeleteConnectionRequest",
        "CreateRepositoryRequest",
        "BatchCreateRepositoriesRequest",
        "BatchCreateRepositoriesResponse",
        "GetRepositoryRequest",
        "ListRepositoriesRequest",
        "ListRepositoriesResponse",
        "DeleteRepositoryRequest",
        "FetchReadWriteTokenRequest",
        "FetchReadTokenRequest",
        "FetchReadTokenResponse",
        "FetchReadWriteTokenResponse",
        "ProcessWebhookRequest",
        "FetchGitRefsRequest",
        "FetchGitRefsResponse",
    },
)


class Connection(proto.Message):
    r"""A connection to a SCM like GitHub, GitHub Enterprise,
    Bitbucket Data Center, Bitbucket Cloud or GitLab.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Immutable. The resource name of the connection, in the
            format
            ``projects/{project}/locations/{location}/connections/{connection_id}``.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Server assigned timestamp for
            when the connection was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Server assigned timestamp for
            when the connection was updated.
        github_config (google.cloud.devtools.cloudbuild_v2.types.GitHubConfig):
            Configuration for connections to github.com.

            This field is a member of `oneof`_ ``connection_config``.
        github_enterprise_config (google.cloud.devtools.cloudbuild_v2.types.GitHubEnterpriseConfig):
            Configuration for connections to an instance
            of GitHub Enterprise.

            This field is a member of `oneof`_ ``connection_config``.
        gitlab_config (google.cloud.devtools.cloudbuild_v2.types.GitLabConfig):
            Configuration for connections to gitlab.com
            or an instance of GitLab Enterprise.

            This field is a member of `oneof`_ ``connection_config``.
        bitbucket_data_center_config (google.cloud.devtools.cloudbuild_v2.types.BitbucketDataCenterConfig):
            Configuration for connections to Bitbucket
            Data Center.

            This field is a member of `oneof`_ ``connection_config``.
        bitbucket_cloud_config (google.cloud.devtools.cloudbuild_v2.types.BitbucketCloudConfig):
            Configuration for connections to Bitbucket
            Cloud.

            This field is a member of `oneof`_ ``connection_config``.
        installation_state (google.cloud.devtools.cloudbuild_v2.types.InstallationState):
            Output only. Installation state of the
            Connection.
        disabled (bool):
            If disabled is set to true, functionality is
            disabled for this connection. Repository based
            API methods and webhooks processing for
            repositories in this connection will be
            disabled.
        reconciling (bool):
            Output only. Set to true when the connection
            is being set up or updated in the background.
        annotations (MutableMapping[str, str]):
            Allows clients to store small amounts of
            arbitrary data.
        etag (str):
            This checksum is computed by the server based
            on the value of other fields, and may be sent on
            update and delete requests to ensure the client
            has an up-to-date value before proceeding.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
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
    github_config: "GitHubConfig" = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="connection_config",
        message="GitHubConfig",
    )
    github_enterprise_config: "GitHubEnterpriseConfig" = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="connection_config",
        message="GitHubEnterpriseConfig",
    )
    gitlab_config: "GitLabConfig" = proto.Field(
        proto.MESSAGE,
        number=7,
        oneof="connection_config",
        message="GitLabConfig",
    )
    bitbucket_data_center_config: "BitbucketDataCenterConfig" = proto.Field(
        proto.MESSAGE,
        number=8,
        oneof="connection_config",
        message="BitbucketDataCenterConfig",
    )
    bitbucket_cloud_config: "BitbucketCloudConfig" = proto.Field(
        proto.MESSAGE,
        number=9,
        oneof="connection_config",
        message="BitbucketCloudConfig",
    )
    installation_state: "InstallationState" = proto.Field(
        proto.MESSAGE,
        number=12,
        message="InstallationState",
    )
    disabled: bool = proto.Field(
        proto.BOOL,
        number=13,
    )
    reconciling: bool = proto.Field(
        proto.BOOL,
        number=14,
    )
    annotations: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=15,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=16,
    )


class InstallationState(proto.Message):
    r"""Describes stage and necessary actions to be taken by the
    user to complete the installation. Used for GitHub and GitHub
    Enterprise based connections.

    Attributes:
        stage (google.cloud.devtools.cloudbuild_v2.types.InstallationState.Stage):
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


class FetchLinkableRepositoriesRequest(proto.Message):
    r"""Request message for FetchLinkableRepositories.

    Attributes:
        connection (str):
            Required. The name of the Connection. Format:
            ``projects/*/locations/*/connections/*``.
        page_size (int):
            Number of results to return in the list.
            Default to 20.
        page_token (str):
            Page start.
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


class FetchLinkableRepositoriesResponse(proto.Message):
    r"""Response message for FetchLinkableRepositories.

    Attributes:
        repositories (MutableSequence[google.cloud.devtools.cloudbuild_v2.types.Repository]):
            repositories ready to be created.
        next_page_token (str):
            A token identifying a page of results the
            server should return.
    """

    @property
    def raw_page(self):
        return self

    repositories: MutableSequence["Repository"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Repository",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GitHubConfig(proto.Message):
    r"""Configuration for connections to github.com.

    Attributes:
        authorizer_credential (google.cloud.devtools.cloudbuild_v2.types.OAuthCredential):
            OAuth credential of the account that
            authorized the Cloud Build GitHub App. It is
            recommended to use a robot account instead of a
            human user account. The OAuth token must be tied
            to the Cloud Build GitHub App.
        app_installation_id (int):
            GitHub App installation id.
    """

    authorizer_credential: "OAuthCredential" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="OAuthCredential",
    )
    app_installation_id: int = proto.Field(
        proto.INT64,
        number=2,
    )


class GitHubEnterpriseConfig(proto.Message):
    r"""Configuration for connections to an instance of GitHub
    Enterprise.

    Attributes:
        host_uri (str):
            Required. The URI of the GitHub Enterprise
            host this connection is for.
        api_key (str):
            Required. API Key used for authentication of
            webhook events.
        app_id (int):
            Id of the GitHub App created from the
            manifest.
        app_slug (str):
            The URL-friendly name of the GitHub App.
        private_key_secret_version (str):
            SecretManager resource containing the private key of the
            GitHub App, formatted as
            ``projects/*/secrets/*/versions/*``.
        webhook_secret_secret_version (str):
            SecretManager resource containing the webhook secret of the
            GitHub App, formatted as
            ``projects/*/secrets/*/versions/*``.
        app_installation_id (int):
            ID of the installation of the GitHub App.
        service_directory_config (google.cloud.devtools.cloudbuild_v2.types.ServiceDirectoryConfig):
            Configuration for using Service Directory to
            privately connect to a GitHub Enterprise server.
            This should only be set if the GitHub Enterprise
            server is hosted on-premises and not reachable
            by public internet. If this field is left empty,
            calls to the GitHub Enterprise server will be
            made over the public internet.
        ssl_ca (str):
            SSL certificate to use for requests to GitHub
            Enterprise.
        server_version (str):
            Output only. GitHub Enterprise version installed at the
            host_uri.
    """

    host_uri: str = proto.Field(
        proto.STRING,
        number=1,
    )
    api_key: str = proto.Field(
        proto.STRING,
        number=12,
    )
    app_id: int = proto.Field(
        proto.INT64,
        number=2,
    )
    app_slug: str = proto.Field(
        proto.STRING,
        number=13,
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
        number=9,
    )
    service_directory_config: "ServiceDirectoryConfig" = proto.Field(
        proto.MESSAGE,
        number=10,
        message="ServiceDirectoryConfig",
    )
    ssl_ca: str = proto.Field(
        proto.STRING,
        number=11,
    )
    server_version: str = proto.Field(
        proto.STRING,
        number=14,
    )


class GitLabConfig(proto.Message):
    r"""Configuration for connections to gitlab.com or an instance of
    GitLab Enterprise.

    Attributes:
        host_uri (str):
            The URI of the GitLab Enterprise host this
            connection is for. If not specified, the default
            value is https://gitlab.com.
        webhook_secret_secret_version (str):
            Required. Immutable. SecretManager resource containing the
            webhook secret of a GitLab Enterprise project, formatted as
            ``projects/*/secrets/*/versions/*``.
        read_authorizer_credential (google.cloud.devtools.cloudbuild_v2.types.UserCredential):
            Required. A GitLab personal access token with the minimum
            ``read_api`` scope access.
        authorizer_credential (google.cloud.devtools.cloudbuild_v2.types.UserCredential):
            Required. A GitLab personal access token with the ``api``
            scope access.
        service_directory_config (google.cloud.devtools.cloudbuild_v2.types.ServiceDirectoryConfig):
            Configuration for using Service Directory to
            privately connect to a GitLab Enterprise server.
            This should only be set if the GitLab Enterprise
            server is hosted on-premises and not reachable
            by public internet. If this field is left empty,
            calls to the GitLab Enterprise server will be
            made over the public internet.
        ssl_ca (str):
            SSL certificate to use for requests to GitLab
            Enterprise.
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
    ssl_ca: str = proto.Field(
        proto.STRING,
        number=6,
    )
    server_version: str = proto.Field(
        proto.STRING,
        number=7,
    )


class BitbucketDataCenterConfig(proto.Message):
    r"""Configuration for connections to Bitbucket Data Center.

    Attributes:
        host_uri (str):
            Required. The URI of the Bitbucket Data
            Center instance or cluster this connection is
            for.
        webhook_secret_secret_version (str):
            Required. Immutable. SecretManager resource containing the
            webhook secret used to verify webhook events, formatted as
            ``projects/*/secrets/*/versions/*``.
        read_authorizer_credential (google.cloud.devtools.cloudbuild_v2.types.UserCredential):
            Required. A http access token with the ``REPO_READ`` access.
        authorizer_credential (google.cloud.devtools.cloudbuild_v2.types.UserCredential):
            Required. A http access token with the ``REPO_ADMIN`` scope
            access.
        service_directory_config (google.cloud.devtools.cloudbuild_v2.types.ServiceDirectoryConfig):
            Optional. Configuration for using Service
            Directory to privately connect to a Bitbucket
            Data Center. This should only be set if the
            Bitbucket Data Center is hosted on-premises and
            not reachable by public internet. If this field
            is left empty, calls to the Bitbucket Data
            Center will be made over the public internet.
        ssl_ca (str):
            Optional. SSL certificate to use for requests
            to the Bitbucket Data Center.
        server_version (str):
            Output only. Version of the Bitbucket Data Center running on
            the ``host_uri``.
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
    ssl_ca: str = proto.Field(
        proto.STRING,
        number=6,
    )
    server_version: str = proto.Field(
        proto.STRING,
        number=7,
    )


class BitbucketCloudConfig(proto.Message):
    r"""Configuration for connections to Bitbucket Cloud.

    Attributes:
        workspace (str):
            Required. The Bitbucket Cloud Workspace ID to
            be connected to Google Cloud Platform.
        webhook_secret_secret_version (str):
            Required. SecretManager resource containing the webhook
            secret used to verify webhook events, formatted as
            ``projects/*/secrets/*/versions/*``.
        read_authorizer_credential (google.cloud.devtools.cloudbuild_v2.types.UserCredential):
            Required. An access token with the ``repository`` access. It
            can be either a workspace, project or repository access
            token. It's recommended to use a system account to generate
            the credentials.
        authorizer_credential (google.cloud.devtools.cloudbuild_v2.types.UserCredential):
            Required. An access token with the ``webhook``,
            ``repository``, ``repository:admin`` and ``pullrequest``
            scope access. It can be either a workspace, project or
            repository access token. It's recommended to use a system
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


class Repository(proto.Message):
    r"""A repository associated to a parent connection.

    Attributes:
        name (str):
            Immutable. Resource name of the repository, in the format
            ``projects/*/locations/*/connections/*/repositories/*``.
        remote_uri (str):
            Required. Git Clone HTTPS URI.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Server assigned timestamp for
            when the connection was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Server assigned timestamp for
            when the connection was updated.
        annotations (MutableMapping[str, str]):
            Allows clients to store small amounts of
            arbitrary data.
        etag (str):
            This checksum is computed by the server based
            on the value of other fields, and may be sent on
            update and delete requests to ensure the client
            has an up-to-date value before proceeding.
        webhook_id (str):
            Output only. External ID of the webhook
            created for the repository.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    remote_uri: str = proto.Field(
        proto.STRING,
        number=2,
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
    annotations: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=6,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=7,
    )
    webhook_id: str = proto.Field(
        proto.STRING,
        number=8,
    )


class OAuthCredential(proto.Message):
    r"""Represents an OAuth token of the account that authorized the
    Connection, and associated metadata.

    Attributes:
        oauth_token_secret_version (str):
            A SecretManager resource containing the OAuth token that
            authorizes the Cloud Build connection. Format:
            ``projects/*/secrets/*/versions/*``.
        username (str):
            Output only. The username associated to this
            token.
    """

    oauth_token_secret_version: str = proto.Field(
        proto.STRING,
        number=1,
    )
    username: str = proto.Field(
        proto.STRING,
        number=2,
    )


class UserCredential(proto.Message):
    r"""Represents a personal access token that authorized the
    Connection, and associated metadata.

    Attributes:
        user_token_secret_version (str):
            Required. A SecretManager resource containing the user token
            that authorizes the Cloud Build connection. Format:
            ``projects/*/secrets/*/versions/*``.
        username (str):
            Output only. The username associated to this
            token.
    """

    user_token_secret_version: str = proto.Field(
        proto.STRING,
        number=1,
    )
    username: str = proto.Field(
        proto.STRING,
        number=2,
    )


class CreateConnectionRequest(proto.Message):
    r"""Message for creating a Connection

    Attributes:
        parent (str):
            Required. Project and location where the connection will be
            created. Format: ``projects/*/locations/*``.
        connection (google.cloud.devtools.cloudbuild_v2.types.Connection):
            Required. The Connection to create.
        connection_id (str):
            Required. The ID to use for the Connection, which will
            become the final component of the Connection's resource
            name. Names must be unique per-project per-location. Allows
            alphanumeric characters and any of -.\_~%!$&'()*+,;=@.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    connection: "Connection" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Connection",
    )
    connection_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class GetConnectionRequest(proto.Message):
    r"""Message for getting the details of a Connection.

    Attributes:
        name (str):
            Required. The name of the Connection to retrieve. Format:
            ``projects/*/locations/*/connections/*``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListConnectionsRequest(proto.Message):
    r"""Message for requesting list of Connections.

    Attributes:
        parent (str):
            Required. The parent, which owns this collection of
            Connections. Format: ``projects/*/locations/*``.
        page_size (int):
            Number of results to return in the list.
        page_token (str):
            Page start.
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


class ListConnectionsResponse(proto.Message):
    r"""Message for response to listing Connections.

    Attributes:
        connections (MutableSequence[google.cloud.devtools.cloudbuild_v2.types.Connection]):
            The list of Connections.
        next_page_token (str):
            A token identifying a page of results the
            server should return.
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


class UpdateConnectionRequest(proto.Message):
    r"""Message for updating a Connection.

    Attributes:
        connection (google.cloud.devtools.cloudbuild_v2.types.Connection):
            Required. The Connection to update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            The list of fields to be updated.
        allow_missing (bool):
            If set to true, and the connection is not found a new
            connection will be created. In this situation
            ``update_mask`` is ignored. The creation will succeed only
            if the input connection has all the necessary information
            (e.g a github_config with both user_oauth_token and
            installation_id properties).
        etag (str):
            The current etag of the connection.
            If an etag is provided and does not match the
            current etag of the connection, update will be
            blocked and an ABORTED error will be returned.
    """

    connection: "Connection" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Connection",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )
    allow_missing: bool = proto.Field(
        proto.BOOL,
        number=3,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=4,
    )


class DeleteConnectionRequest(proto.Message):
    r"""Message for deleting a Connection.

    Attributes:
        name (str):
            Required. The name of the Connection to delete. Format:
            ``projects/*/locations/*/connections/*``.
        etag (str):
            The current etag of the connection.
            If an etag is provided and does not match the
            current etag of the connection, deletion will be
            blocked and an ABORTED error will be returned.
        validate_only (bool):
            If set, validate the request, but do not
            actually post it.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=2,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


class CreateRepositoryRequest(proto.Message):
    r"""Message for creating a Repository.

    Attributes:
        parent (str):
            Required. The connection to contain the
            repository. If the request is part of a
            BatchCreateRepositoriesRequest, this field
            should be empty or match the parent specified
            there.
        repository (google.cloud.devtools.cloudbuild_v2.types.Repository):
            Required. The repository to create.
        repository_id (str):
            Required. The ID to use for the repository, which will
            become the final component of the repository's resource
            name. This ID should be unique in the connection. Allows
            alphanumeric characters and any of -.\_~%!$&'()*+,;=@.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    repository: "Repository" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Repository",
    )
    repository_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class BatchCreateRepositoriesRequest(proto.Message):
    r"""Message for creating repositoritories in batch.

    Attributes:
        parent (str):
            Required. The connection to contain all the repositories
            being created. Format: projects/*/locations/*/connections/\*
            The parent field in the CreateRepositoryRequest messages
            must either be empty or match this field.
        requests (MutableSequence[google.cloud.devtools.cloudbuild_v2.types.CreateRepositoryRequest]):
            Required. The request messages specifying the
            repositories to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    requests: MutableSequence["CreateRepositoryRequest"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="CreateRepositoryRequest",
    )


class BatchCreateRepositoriesResponse(proto.Message):
    r"""Message for response of creating repositories in batch.

    Attributes:
        repositories (MutableSequence[google.cloud.devtools.cloudbuild_v2.types.Repository]):
            Repository resources created.
    """

    repositories: MutableSequence["Repository"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Repository",
    )


class GetRepositoryRequest(proto.Message):
    r"""Message for getting the details of a Repository.

    Attributes:
        name (str):
            Required. The name of the Repository to retrieve. Format:
            ``projects/*/locations/*/connections/*/repositories/*``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListRepositoriesRequest(proto.Message):
    r"""Message for requesting list of Repositories.

    Attributes:
        parent (str):
            Required. The parent, which owns this collection of
            Repositories. Format:
            ``projects/*/locations/*/connections/*``.
        page_size (int):
            Number of results to return in the list.
        page_token (str):
            Page start.
        filter (str):
            A filter expression that filters resources listed in the
            response. Expressions must follow API improvement proposal
            `AIP-160 <https://google.aip.dev/160>`__. e.g.
            ``remote_uri:"https://github.com*"``.
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


class ListRepositoriesResponse(proto.Message):
    r"""Message for response to listing Repositories.

    Attributes:
        repositories (MutableSequence[google.cloud.devtools.cloudbuild_v2.types.Repository]):
            The list of Repositories.
        next_page_token (str):
            A token identifying a page of results the
            server should return.
    """

    @property
    def raw_page(self):
        return self

    repositories: MutableSequence["Repository"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Repository",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class DeleteRepositoryRequest(proto.Message):
    r"""Message for deleting a Repository.

    Attributes:
        name (str):
            Required. The name of the Repository to delete. Format:
            ``projects/*/locations/*/connections/*/repositories/*``.
        etag (str):
            The current etag of the repository.
            If an etag is provided and does not match the
            current etag of the repository, deletion will be
            blocked and an ABORTED error will be returned.
        validate_only (bool):
            If set, validate the request, but do not
            actually post it.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=2,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


class FetchReadWriteTokenRequest(proto.Message):
    r"""Message for fetching SCM read/write token.

    Attributes:
        repository (str):
            Required. The resource name of the repository in the format
            ``projects/*/locations/*/connections/*/repositories/*``.
    """

    repository: str = proto.Field(
        proto.STRING,
        number=1,
    )


class FetchReadTokenRequest(proto.Message):
    r"""Message for fetching SCM read token.

    Attributes:
        repository (str):
            Required. The resource name of the repository in the format
            ``projects/*/locations/*/connections/*/repositories/*``.
    """

    repository: str = proto.Field(
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


class FetchReadWriteTokenResponse(proto.Message):
    r"""Message for responding to get read/write token.

    Attributes:
        token (str):
            The token content.
        expiration_time (google.protobuf.timestamp_pb2.Timestamp):
            Expiration timestamp. Can be empty if unknown
            or non-expiring.
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


class ProcessWebhookRequest(proto.Message):
    r"""RPC request object accepted by the ProcessWebhook RPC method.

    Attributes:
        parent (str):
            Required. Project and location where the webhook will be
            received. Format: ``projects/*/locations/*``.
        body (google.api.httpbody_pb2.HttpBody):
            HTTP request body.
        webhook_key (str):
            Arbitrary additional key to find the maching
            repository for a webhook event if needed.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    body: httpbody_pb2.HttpBody = proto.Field(
        proto.MESSAGE,
        number=2,
        message=httpbody_pb2.HttpBody,
    )
    webhook_key: str = proto.Field(
        proto.STRING,
        number=3,
    )


class FetchGitRefsRequest(proto.Message):
    r"""Request for fetching git refs

    Attributes:
        repository (str):
            Required. The resource name of the repository in the format
            ``projects/*/locations/*/connections/*/repositories/*``.
        ref_type (google.cloud.devtools.cloudbuild_v2.types.FetchGitRefsRequest.RefType):
            Type of refs to fetch
    """

    class RefType(proto.Enum):
        r"""Type of refs

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

    repository: str = proto.Field(
        proto.STRING,
        number=1,
    )
    ref_type: RefType = proto.Field(
        proto.ENUM,
        number=2,
        enum=RefType,
    )


class FetchGitRefsResponse(proto.Message):
    r"""Response for fetching git refs

    Attributes:
        ref_names (MutableSequence[str]):
            Name of the refs fetched.
    """

    ref_names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
