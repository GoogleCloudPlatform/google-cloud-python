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
import google.rpc.status_pb2 as status_pb2  # type: ignore
import google.type.interval_pb2 as interval_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.dataform.v1",
    manifest={
        "DirectoryContentsView",
        "DataEncryptionState",
        "Repository",
        "OAuthConfig",
        "PrivateResourceMetadata",
        "ListRepositoriesRequest",
        "ListRepositoriesResponse",
        "MoveRepositoryRequest",
        "GetRepositoryRequest",
        "CreateRepositoryRequest",
        "UpdateRepositoryRequest",
        "DeleteRepositoryRequest",
        "CommitRepositoryChangesRequest",
        "CommitRepositoryChangesResponse",
        "ReadRepositoryFileRequest",
        "ReadRepositoryFileResponse",
        "QueryRepositoryDirectoryContentsRequest",
        "QueryRepositoryDirectoryContentsResponse",
        "FetchRepositoryHistoryRequest",
        "FetchRepositoryHistoryResponse",
        "CommitLogEntry",
        "CommitMetadata",
        "ComputeRepositoryAccessTokenStatusRequest",
        "ComputeRepositoryAccessTokenStatusResponse",
        "FetchRemoteBranchesRequest",
        "FetchRemoteBranchesResponse",
        "Workspace",
        "ListWorkspacesRequest",
        "ListWorkspacesResponse",
        "GetWorkspaceRequest",
        "CreateWorkspaceRequest",
        "DeleteWorkspaceRequest",
        "CommitAuthor",
        "PullGitCommitsRequest",
        "PullGitCommitsResponse",
        "PushGitCommitsRequest",
        "PushGitCommitsResponse",
        "FetchFileGitStatusesRequest",
        "FetchFileGitStatusesResponse",
        "FetchGitAheadBehindRequest",
        "FetchGitAheadBehindResponse",
        "CommitWorkspaceChangesRequest",
        "CommitWorkspaceChangesResponse",
        "ResetWorkspaceChangesRequest",
        "ResetWorkspaceChangesResponse",
        "FetchFileDiffRequest",
        "FetchFileDiffResponse",
        "QueryDirectoryContentsRequest",
        "QueryDirectoryContentsResponse",
        "DirectoryEntry",
        "FilesystemEntryMetadata",
        "SearchFilesRequest",
        "SearchFilesResponse",
        "SearchResult",
        "FileSearchResult",
        "DirectorySearchResult",
        "MakeDirectoryRequest",
        "MakeDirectoryResponse",
        "RemoveDirectoryRequest",
        "RemoveDirectoryResponse",
        "MoveDirectoryRequest",
        "MoveDirectoryResponse",
        "ReadFileRequest",
        "ReadFileResponse",
        "RemoveFileRequest",
        "RemoveFileResponse",
        "MoveFileRequest",
        "MoveFileResponse",
        "WriteFileRequest",
        "WriteFileResponse",
        "InstallNpmPackagesRequest",
        "InstallNpmPackagesResponse",
        "ReleaseConfig",
        "ListReleaseConfigsRequest",
        "ListReleaseConfigsResponse",
        "GetReleaseConfigRequest",
        "CreateReleaseConfigRequest",
        "UpdateReleaseConfigRequest",
        "DeleteReleaseConfigRequest",
        "CompilationResult",
        "CodeCompilationConfig",
        "GcsRepositorySnapshotMetadata",
        "GcsRepositorySnapshotDestination",
        "NotebookRuntimeOptions",
        "PipelineConfig",
        "ListCompilationResultsRequest",
        "ListCompilationResultsResponse",
        "GetCompilationResultRequest",
        "CreateCompilationResultRequest",
        "Target",
        "RelationDescriptor",
        "CompilationResultAction",
        "QueryCompilationResultActionsRequest",
        "QueryCompilationResultActionsResponse",
        "WorkflowConfig",
        "InvocationConfig",
        "ListWorkflowConfigsRequest",
        "ListWorkflowConfigsResponse",
        "GetWorkflowConfigRequest",
        "CreateWorkflowConfigRequest",
        "UpdateWorkflowConfigRequest",
        "DeleteWorkflowConfigRequest",
        "WorkflowInvocation",
        "ListWorkflowInvocationsRequest",
        "ListWorkflowInvocationsResponse",
        "GetWorkflowInvocationRequest",
        "CreateWorkflowInvocationRequest",
        "DeleteWorkflowInvocationRequest",
        "CancelWorkflowInvocationRequest",
        "CancelWorkflowInvocationResponse",
        "WorkflowInvocationAction",
        "QueryWorkflowInvocationActionsRequest",
        "QueryWorkflowInvocationActionsResponse",
        "Config",
        "GetConfigRequest",
        "UpdateConfigRequest",
        "Folder",
        "CreateFolderRequest",
        "MoveFolderRequest",
        "GetFolderRequest",
        "UpdateFolderRequest",
        "DeleteFolderRequest",
        "DeleteFolderTreeRequest",
        "DeleteTeamFolderTreeRequest",
        "DeleteFolderTreeMetadata",
        "QueryFolderContentsRequest",
        "QueryFolderContentsResponse",
        "QueryUserRootContentsRequest",
        "QueryUserRootContentsResponse",
        "TeamFolder",
        "CreateTeamFolderRequest",
        "GetTeamFolderRequest",
        "UpdateTeamFolderRequest",
        "DeleteTeamFolderRequest",
        "QueryTeamFolderContentsRequest",
        "QueryTeamFolderContentsResponse",
        "SearchTeamFoldersRequest",
        "SearchTeamFoldersResponse",
        "MoveFolderMetadata",
        "MoveRepositoryMetadata",
    },
)


class DirectoryContentsView(proto.Enum):
    r"""Represents the level of detail to return for directory
    contents.

    Values:
        DIRECTORY_CONTENTS_VIEW_UNSPECIFIED (0):
            The default unset value. Defaults to
            DIRECTORY_CONTENTS_VIEW_BASIC.
        DIRECTORY_CONTENTS_VIEW_BASIC (1):
            Includes only the file or directory name.
            This is the default behavior.
        DIRECTORY_CONTENTS_VIEW_METADATA (2):
            Includes all metadata for each file or
            directory. Currently not supported by
            CMEK-protected workspaces.
    """

    DIRECTORY_CONTENTS_VIEW_UNSPECIFIED = 0
    DIRECTORY_CONTENTS_VIEW_BASIC = 1
    DIRECTORY_CONTENTS_VIEW_METADATA = 2


class DataEncryptionState(proto.Message):
    r"""Describes encryption state of a resource.

    Attributes:
        kms_key_version_name (str):
            Required. The KMS key version name with which
            data of a resource is encrypted.
    """

    kms_key_version_name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class Repository(proto.Message):
    r"""Represents a Dataform Git repository.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Identifier. The repository's name.
        containing_folder (str):
            Optional. The name of the containing folder of the
            repository. The field is immutable and it can be modified
            via a MoveRepository operation. Format:
            ``projects/*/locations/*/folders/*``. or
            ``projects/*/locations/*/teamFolders/*``.

            This field is a member of `oneof`_ ``_containing_folder``.
        team_folder_name (str):
            Output only. The resource name of the
            TeamFolder that this Repository is associated
            with. This should take the format:

            projects/{project}/locations/{location}/teamFolders/{teamFolder}.
            If this is not set, the Repository is not
            associated with a TeamFolder.

            This field is a member of `oneof`_ ``_team_folder_name``.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp of when the
            repository was created.
        display_name (str):
            Optional. The repository's user-friendly
            name.
        git_remote_settings (google.cloud.dataform_v1.types.Repository.GitRemoteSettings):
            Optional. If set, configures this repository
            to be linked to a Git remote.
        npmrc_environment_variables_secret_version (str):
            Optional. The name of the Secret Manager secret version to
            be used to interpolate variables into the .npmrc file for
            package installation operations. Must be in the format
            ``projects/*/secrets/*/versions/*``. The file itself must be
            in a JSON format.
        workspace_compilation_overrides (google.cloud.dataform_v1.types.Repository.WorkspaceCompilationOverrides):
            Optional. If set, fields of
            ``workspace_compilation_overrides`` override the default
            compilation settings that are specified in dataform.json
            when creating workspace-scoped compilation results. See
            documentation for ``WorkspaceCompilationOverrides`` for more
            information.
        labels (MutableMapping[str, str]):
            Optional. Repository user labels.
        set_authenticated_user_admin (bool):
            Optional. Input only. If set to true, the
            authenticated user will be granted the
            roles/dataform.admin role on the created
            repository.
        service_account (str):
            Optional. The service account to run workflow
            invocations under.
        kms_key_name (str):
            Optional. The reference to a KMS encryption key. If
            provided, it will be used to encrypt user data in the
            repository and all child resources. It is not possible to
            add or update the encryption key after the repository is
            created. Example:
            ``projects/{kms_project}/locations/{location}/keyRings/{key_location}/cryptoKeys/{key}``
        data_encryption_state (google.cloud.dataform_v1.types.DataEncryptionState):
            Output only. A data encryption state of a Git
            repository if this Repository is protected by a
            KMS key.
        internal_metadata (str):
            Output only. All the metadata information
            that is used internally to serve the resource.
            For example: timestamps, flags, status fields,
            etc. The format of this field is a JSON string.

            This field is a member of `oneof`_ ``_internal_metadata``.
        end_user_auth_config (google.cloud.dataform_v1.types.Repository.EndUserAuthConfig):
            Optional. Includes configuration options for
            end user authentication.
    """

    class GitRemoteSettings(proto.Message):
        r"""Controls Git remote configuration for a repository.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            url (str):
                Required. The Git remote's URL.
            default_branch (str):
                Optional. The Git remote's default branch name. If not set,
                ``main`` will be used.
            effective_default_branch (str):
                Output only. The Git remote's effective default branch name.
                This is the default branch name of the Git remote if it is
                set, otherwise it is ``main``.
            authentication_token_secret_version (str):
                Optional. The name of the Secret Manager secret version to
                use as an authentication token for Git operations. Must be
                in the format ``projects/*/secrets/*/versions/*``.
            ssh_authentication_config (google.cloud.dataform_v1.types.Repository.GitRemoteSettings.SshAuthenticationConfig):
                Optional. Authentication fields for remote
                uris using SSH protocol.
            git_repository_link (str):
                Optional. Resource name for the ``GitRepositoryLink`` used
                for machine credentials. Must be in the format
                ``projects/*/locations/*/connections/*/gitRepositoryLinks/*``

                This field is a member of `oneof`_ ``_git_repository_link``.
            token_status (google.cloud.dataform_v1.types.Repository.GitRemoteSettings.TokenStatus):
                Output only. Deprecated: The field does not
                contain any token status information.
        """

        class TokenStatus(proto.Enum):
            r"""The status of the authentication token.

            Values:
                TOKEN_STATUS_UNSPECIFIED (0):
                    Default value. This value is unused.
                NOT_FOUND (1):
                    The token could not be found in Secret
                    Manager (or the Dataform Service Account did not
                    have permission to access it).
                INVALID (2):
                    The token could not be used to authenticate
                    against the Git remote.
                VALID (3):
                    The token was used successfully to
                    authenticate against the Git remote.
            """

            TOKEN_STATUS_UNSPECIFIED = 0
            NOT_FOUND = 1
            INVALID = 2
            VALID = 3

        class SshAuthenticationConfig(proto.Message):
            r"""Configures fields for performing SSH authentication.

            Attributes:
                user_private_key_secret_version (str):
                    Required. The name of the Secret Manager secret version to
                    use as a ssh private key for Git operations. Must be in the
                    format ``projects/*/secrets/*/versions/*``.
                host_public_key (str):
                    Required. Content of a public SSH key to
                    verify an identity of a remote Git host.
            """

            user_private_key_secret_version: str = proto.Field(
                proto.STRING,
                number=1,
            )
            host_public_key: str = proto.Field(
                proto.STRING,
                number=2,
            )

        url: str = proto.Field(
            proto.STRING,
            number=1,
        )
        default_branch: str = proto.Field(
            proto.STRING,
            number=2,
        )
        effective_default_branch: str = proto.Field(
            proto.STRING,
            number=9,
        )
        authentication_token_secret_version: str = proto.Field(
            proto.STRING,
            number=3,
        )
        ssh_authentication_config: "Repository.GitRemoteSettings.SshAuthenticationConfig" = proto.Field(
            proto.MESSAGE,
            number=5,
            message="Repository.GitRemoteSettings.SshAuthenticationConfig",
        )
        git_repository_link: str = proto.Field(
            proto.STRING,
            number=7,
            optional=True,
        )
        token_status: "Repository.GitRemoteSettings.TokenStatus" = proto.Field(
            proto.ENUM,
            number=4,
            enum="Repository.GitRemoteSettings.TokenStatus",
        )

    class WorkspaceCompilationOverrides(proto.Message):
        r"""Configures workspace compilation overrides for a repository.

        Attributes:
            default_database (str):
                Optional. The default database (Google Cloud
                project ID).
            schema_suffix (str):
                Optional. The suffix that should be appended
                to all schema (BigQuery dataset ID) names.
            table_prefix (str):
                Optional. The prefix that should be prepended
                to all table names.
        """

        default_database: str = proto.Field(
            proto.STRING,
            number=1,
        )
        schema_suffix: str = proto.Field(
            proto.STRING,
            number=2,
        )
        table_prefix: str = proto.Field(
            proto.STRING,
            number=3,
        )

    class EndUserAuthConfig(proto.Message):
        r"""Includes configuration options for repository end user
        authentication.

        Attributes:
            oauth_config (google.cloud.dataform_v1.types.OAuthConfig):
                Optional. OAuth configuration for repository
                end user authentication.
        """

        oauth_config: "OAuthConfig" = proto.Field(
            proto.MESSAGE,
            number=1,
            message="OAuthConfig",
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    containing_folder: str = proto.Field(
        proto.STRING,
        number=16,
        optional=True,
    )
    team_folder_name: str = proto.Field(
        proto.STRING,
        number=18,
        optional=True,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=13,
        message=timestamp_pb2.Timestamp,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=8,
    )
    git_remote_settings: GitRemoteSettings = proto.Field(
        proto.MESSAGE,
        number=2,
        message=GitRemoteSettings,
    )
    npmrc_environment_variables_secret_version: str = proto.Field(
        proto.STRING,
        number=3,
    )
    workspace_compilation_overrides: WorkspaceCompilationOverrides = proto.Field(
        proto.MESSAGE,
        number=4,
        message=WorkspaceCompilationOverrides,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=5,
    )
    set_authenticated_user_admin: bool = proto.Field(
        proto.BOOL,
        number=9,
    )
    service_account: str = proto.Field(
        proto.STRING,
        number=10,
    )
    kms_key_name: str = proto.Field(
        proto.STRING,
        number=11,
    )
    data_encryption_state: "DataEncryptionState" = proto.Field(
        proto.MESSAGE,
        number=12,
        message="DataEncryptionState",
    )
    internal_metadata: str = proto.Field(
        proto.STRING,
        number=15,
        optional=True,
    )
    end_user_auth_config: EndUserAuthConfig = proto.Field(
        proto.MESSAGE,
        number=28,
        message=EndUserAuthConfig,
    )


class OAuthConfig(proto.Message):
    r"""OAuth configuration for end user authentication.

    Attributes:
        additional_oauth_scopes (MutableSequence[str]):
            Optional. Additional OAuth scopes to use for BigQuery
            executions. Scopes always in use:
            ``https://www.googleapis.com/auth/bigquery``
    """

    additional_oauth_scopes: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )


class PrivateResourceMetadata(proto.Message):
    r"""Metadata used to identify if a resource is user scoped.

    Attributes:
        user_scoped (bool):
            Output only. If true, this resource is
            user-scoped, meaning it is either a workspace or
            sourced from a workspace.
    """

    user_scoped: bool = proto.Field(
        proto.BOOL,
        number=1,
    )


class ListRepositoriesRequest(proto.Message):
    r"""``ListRepositories`` request message.

    Attributes:
        parent (str):
            Required. The location in which to list repositories. Must
            be in the format ``projects/*/locations/*``.
        page_size (int):
            Optional. Maximum number of repositories to
            return. The server may return fewer items than
            requested. If unspecified, the server will pick
            an appropriate default.
        page_token (str):
            Optional. Page token received from a previous
            ``ListRepositories`` call. Provide this to retrieve the
            subsequent page.

            When paginating, all other parameters provided to
            ``ListRepositories``, with the exception of ``page_size``,
            must match the call that provided the page token.
        order_by (str):
            Optional. This field only supports ordering by ``name``. If
            unspecified, the server will choose the ordering. If
            specified, the default order is ascending for the ``name``
            field.
        filter (str):
            Optional. Filter for the returned list.
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
    filter: str = proto.Field(
        proto.STRING,
        number=5,
    )


class ListRepositoriesResponse(proto.Message):
    r"""``ListRepositories`` response message.

    Attributes:
        repositories (MutableSequence[google.cloud.dataform_v1.types.Repository]):
            List of repositories.
        next_page_token (str):
            A token which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
        unreachable (MutableSequence[str]):
            Locations which could not be reached.
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
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class MoveRepositoryRequest(proto.Message):
    r"""``MoveRepository`` request message.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Required. The full resource name of the
            repository to move.
        destination_containing_folder (str):
            Optional. The name of the Folder, TeamFolder, or root
            location to move the repository to. Can be in the format of:
            "" to move into the root User folder,
            ``projects/*/locations/*/folders/*``,
            ``projects/*/locations/*/teamFolders/*``

            This field is a member of `oneof`_ ``_destination_containing_folder``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    destination_containing_folder: str = proto.Field(
        proto.STRING,
        number=2,
        optional=True,
    )


class GetRepositoryRequest(proto.Message):
    r"""``GetRepository`` request message.

    Attributes:
        name (str):
            Required. The repository's name.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateRepositoryRequest(proto.Message):
    r"""``CreateRepository`` request message.

    Attributes:
        parent (str):
            Required. The location in which to create the repository.
            Must be in the format ``projects/*/locations/*``.
        repository (google.cloud.dataform_v1.types.Repository):
            Required. The repository to create.
        repository_id (str):
            Required. The ID to use for the repository,
            which will become the final component of the
            repository's resource name.
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


class UpdateRepositoryRequest(proto.Message):
    r"""``UpdateRepository`` request message.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. Specifies the fields to be updated
            in the repository. If left unset, all fields
            will be updated.
        repository (google.cloud.dataform_v1.types.Repository):
            Required. The repository to update.
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    repository: "Repository" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Repository",
    )


class DeleteRepositoryRequest(proto.Message):
    r"""``DeleteRepository`` request message.

    Attributes:
        name (str):
            Required. The repository's name.
        force (bool):
            Optional. If set to true, child resources of this repository
            (compilation results and workflow invocations) will also be
            deleted. Otherwise, the request will only succeed if the
            repository has no child resources.

            **Note:** *This flag doesn't support deletion of workspaces,
            release configs or workflow configs. If any of such
            resources exists in the repository, the request will fail.*.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    force: bool = proto.Field(
        proto.BOOL,
        number=2,
    )


class CommitRepositoryChangesRequest(proto.Message):
    r"""``CommitRepositoryChanges`` request message.

    Attributes:
        name (str):
            Required. The repository's name.
        commit_metadata (google.cloud.dataform_v1.types.CommitMetadata):
            Required. The changes to commit to the
            repository.
        required_head_commit_sha (str):
            Optional. The commit SHA which must be the
            repository's current HEAD before applying this
            commit; otherwise this request will fail. If
            unset, no validation on the current HEAD commit
            SHA is performed.
        file_operations (MutableMapping[str, google.cloud.dataform_v1.types.CommitRepositoryChangesRequest.FileOperation]):
            Optional. A map to the path of the file to
            the operation. The path is the full file path
            including filename, from repository root.
    """

    class FileOperation(proto.Message):
        r"""Represents a single file operation to the repository.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            write_file (google.cloud.dataform_v1.types.CommitRepositoryChangesRequest.FileOperation.WriteFile):
                Represents the write operation.

                This field is a member of `oneof`_ ``operation``.
            delete_file (google.cloud.dataform_v1.types.CommitRepositoryChangesRequest.FileOperation.DeleteFile):
                Represents the delete operation.

                This field is a member of `oneof`_ ``operation``.
        """

        class WriteFile(proto.Message):
            r"""Represents the write file operation (for files added or
            modified).

            Attributes:
                contents (bytes):
                    The file's contents.
            """

            contents: bytes = proto.Field(
                proto.BYTES,
                number=1,
            )

        class DeleteFile(proto.Message):
            r"""Represents the delete file operation."""

        write_file: "CommitRepositoryChangesRequest.FileOperation.WriteFile" = (
            proto.Field(
                proto.MESSAGE,
                number=1,
                oneof="operation",
                message="CommitRepositoryChangesRequest.FileOperation.WriteFile",
            )
        )
        delete_file: "CommitRepositoryChangesRequest.FileOperation.DeleteFile" = (
            proto.Field(
                proto.MESSAGE,
                number=2,
                oneof="operation",
                message="CommitRepositoryChangesRequest.FileOperation.DeleteFile",
            )
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    commit_metadata: "CommitMetadata" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="CommitMetadata",
    )
    required_head_commit_sha: str = proto.Field(
        proto.STRING,
        number=4,
    )
    file_operations: MutableMapping[str, FileOperation] = proto.MapField(
        proto.STRING,
        proto.MESSAGE,
        number=3,
        message=FileOperation,
    )


class CommitRepositoryChangesResponse(proto.Message):
    r"""``CommitRepositoryChanges`` response message.

    Attributes:
        commit_sha (str):
            The commit SHA of the current commit.
    """

    commit_sha: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ReadRepositoryFileRequest(proto.Message):
    r"""``ReadRepositoryFile`` request message.

    Attributes:
        name (str):
            Required. The repository's name.
        commit_sha (str):
            Optional. The commit SHA for the commit to
            read from. If unset, the file will be read from
            HEAD.
        path (str):
            Required. Full file path to read including
            filename, from repository root.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    commit_sha: str = proto.Field(
        proto.STRING,
        number=2,
    )
    path: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ReadRepositoryFileResponse(proto.Message):
    r"""``ReadRepositoryFile`` response message.

    Attributes:
        contents (bytes):
            The file's contents.
    """

    contents: bytes = proto.Field(
        proto.BYTES,
        number=1,
    )


class QueryRepositoryDirectoryContentsRequest(proto.Message):
    r"""``QueryRepositoryDirectoryContents`` request message.

    Attributes:
        name (str):
            Required. The repository's name.
        commit_sha (str):
            Optional. The Commit SHA for the commit to
            query from. If unset, the directory will be
            queried from HEAD.
        path (str):
            Optional. The directory's full path including
            directory name, relative to root. If left unset,
            the root is used.
        page_size (int):
            Optional. Maximum number of paths to return.
            The server may return fewer items than
            requested. If unspecified, the server will pick
            an appropriate default.
        page_token (str):
            Optional. Page token received from a previous
            ``QueryRepositoryDirectoryContents`` call. Provide this to
            retrieve the subsequent page.

            When paginating, all other parameters provided to
            ``QueryRepositoryDirectoryContents``, with the exception of
            ``page_size``, must match the call that provided the page
            token.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    commit_sha: str = proto.Field(
        proto.STRING,
        number=2,
    )
    path: str = proto.Field(
        proto.STRING,
        number=3,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=4,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=5,
    )


class QueryRepositoryDirectoryContentsResponse(proto.Message):
    r"""``QueryRepositoryDirectoryContents`` response message.

    Attributes:
        directory_entries (MutableSequence[google.cloud.dataform_v1.types.DirectoryEntry]):
            List of entries in the directory.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    directory_entries: MutableSequence["DirectoryEntry"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="DirectoryEntry",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class FetchRepositoryHistoryRequest(proto.Message):
    r"""``FetchRepositoryHistory`` request message.

    Attributes:
        name (str):
            Required. The repository's name.
        page_size (int):
            Optional. Maximum number of commits to
            return. The server may return fewer items than
            requested. If unspecified, the server will pick
            an appropriate default.
        page_token (str):
            Optional. Page token received from a previous
            ``FetchRepositoryHistory`` call. Provide this to retrieve
            the subsequent page.

            When paginating, all other parameters provided to
            ``FetchRepositoryHistory``, with the exception of
            ``page_size``, must match the call that provided the page
            token.
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
        number=5,
    )


class FetchRepositoryHistoryResponse(proto.Message):
    r"""``FetchRepositoryHistory`` response message.

    Attributes:
        commits (MutableSequence[google.cloud.dataform_v1.types.CommitLogEntry]):
            A list of commit logs, ordered by 'git log'
            default order.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    commits: MutableSequence["CommitLogEntry"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="CommitLogEntry",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class CommitLogEntry(proto.Message):
    r"""Represents a single commit log.

    Attributes:
        commit_time (google.protobuf.timestamp_pb2.Timestamp):
            Commit timestamp.
        commit_sha (str):
            The commit SHA for this commit log entry.
        author (google.cloud.dataform_v1.types.CommitAuthor):
            The commit author for this commit log entry.
        commit_message (str):
            The commit message for this commit log entry.
    """

    commit_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )
    commit_sha: str = proto.Field(
        proto.STRING,
        number=2,
    )
    author: "CommitAuthor" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="CommitAuthor",
    )
    commit_message: str = proto.Field(
        proto.STRING,
        number=4,
    )


class CommitMetadata(proto.Message):
    r"""Represents a Dataform Git commit.

    Attributes:
        author (google.cloud.dataform_v1.types.CommitAuthor):
            Required. The commit's author.
        commit_message (str):
            Optional. The commit's message.
    """

    author: "CommitAuthor" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="CommitAuthor",
    )
    commit_message: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ComputeRepositoryAccessTokenStatusRequest(proto.Message):
    r"""``ComputeRepositoryAccessTokenStatus`` request message.

    Attributes:
        name (str):
            Required. The repository's name.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ComputeRepositoryAccessTokenStatusResponse(proto.Message):
    r"""``ComputeRepositoryAccessTokenStatus`` response message.

    Attributes:
        token_status (google.cloud.dataform_v1.types.ComputeRepositoryAccessTokenStatusResponse.TokenStatus):
            Indicates the status of the Git access token.
    """

    class TokenStatus(proto.Enum):
        r"""Indicates the status of a Git authentication token.

        Values:
            TOKEN_STATUS_UNSPECIFIED (0):
                Default value. This value is unused.
            NOT_FOUND (1):
                The token could not be found in Secret
                Manager (or the Dataform Service Account did not
                have permission to access it).
            INVALID (2):
                The token could not be used to authenticate
                against the Git remote.
            VALID (3):
                The token was used successfully to
                authenticate against the Git remote.
            PERMISSION_DENIED (4):
                The token is not accessible due to permission
                issues.
        """

        TOKEN_STATUS_UNSPECIFIED = 0
        NOT_FOUND = 1
        INVALID = 2
        VALID = 3
        PERMISSION_DENIED = 4

    token_status: TokenStatus = proto.Field(
        proto.ENUM,
        number=1,
        enum=TokenStatus,
    )


class FetchRemoteBranchesRequest(proto.Message):
    r"""``FetchRemoteBranches`` request message.

    Attributes:
        name (str):
            Required. The repository's name.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class FetchRemoteBranchesResponse(proto.Message):
    r"""``FetchRemoteBranches`` response message.

    Attributes:
        branches (MutableSequence[str]):
            The remote repository's branch names.
    """

    branches: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )


class Workspace(proto.Message):
    r"""Represents a Dataform Git workspace.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Identifier. The workspace's name.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp of when the
            workspace was created.
        data_encryption_state (google.cloud.dataform_v1.types.DataEncryptionState):
            Output only. A data encryption state of a Git
            repository if this Workspace is protected by a
            KMS key.
        internal_metadata (str):
            Output only. All the metadata information
            that is used internally to serve the resource.
            For example: timestamps, flags, status fields,
            etc. The format of this field is a JSON string.

            This field is a member of `oneof`_ ``_internal_metadata``.
        disable_moves (bool):
            Optional. If set to true, workspaces will not
            be moved if its linked Repository is moved.
            Instead, it will be deleted.

            This field is a member of `oneof`_ ``_disable_moves``.
        private_resource_metadata (google.cloud.dataform_v1.types.PrivateResourceMetadata):
            Output only. Metadata indicating whether this resource is
            user-scoped. For ``Workspace`` resources, the
            ``user_scoped`` field is always ``true``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    data_encryption_state: "DataEncryptionState" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="DataEncryptionState",
    )
    internal_metadata: str = proto.Field(
        proto.STRING,
        number=5,
        optional=True,
    )
    disable_moves: bool = proto.Field(
        proto.BOOL,
        number=6,
        optional=True,
    )
    private_resource_metadata: "PrivateResourceMetadata" = proto.Field(
        proto.MESSAGE,
        number=8,
        message="PrivateResourceMetadata",
    )


class ListWorkspacesRequest(proto.Message):
    r"""``ListWorkspaces`` request message.

    Attributes:
        parent (str):
            Required. The repository in which to list workspaces. Must
            be in the format ``projects/*/locations/*/repositories/*``.
        page_size (int):
            Optional. Maximum number of workspaces to
            return. The server may return fewer items than
            requested. If unspecified, the server will pick
            an appropriate default.
        page_token (str):
            Optional. Page token received from a previous
            ``ListWorkspaces`` call. Provide this to retrieve the
            subsequent page.

            When paginating, all other parameters provided to
            ``ListWorkspaces``, with the exception of ``page_size``,
            must match the call that provided the page token.
        order_by (str):
            Optional. This field only supports ordering by ``name``. If
            unspecified, the server will choose the ordering. If
            specified, the default order is ascending for the ``name``
            field.
        filter (str):
            Optional. Filter for the returned list.
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
    filter: str = proto.Field(
        proto.STRING,
        number=5,
    )


class ListWorkspacesResponse(proto.Message):
    r"""``ListWorkspaces`` response message.

    Attributes:
        workspaces (MutableSequence[google.cloud.dataform_v1.types.Workspace]):
            List of workspaces.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
        unreachable (MutableSequence[str]):
            Locations which could not be reached.
    """

    @property
    def raw_page(self):
        return self

    workspaces: MutableSequence["Workspace"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Workspace",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetWorkspaceRequest(proto.Message):
    r"""``GetWorkspace`` request message.

    Attributes:
        name (str):
            Required. The workspace's name.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateWorkspaceRequest(proto.Message):
    r"""``CreateWorkspace`` request message.

    Attributes:
        parent (str):
            Required. The repository in which to create the workspace.
            Must be in the format
            ``projects/*/locations/*/repositories/*``.
        workspace (google.cloud.dataform_v1.types.Workspace):
            Required. The workspace to create.
        workspace_id (str):
            Required. The ID to use for the workspace,
            which will become the final component of the
            workspace's resource name.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    workspace: "Workspace" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Workspace",
    )
    workspace_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class DeleteWorkspaceRequest(proto.Message):
    r"""``DeleteWorkspace`` request message.

    Attributes:
        name (str):
            Required. The workspace resource's name.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CommitAuthor(proto.Message):
    r"""Represents the author of a Git commit.

    Attributes:
        name (str):
            Required. The commit author's name.
        email_address (str):
            Required. The commit author's email address.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    email_address: str = proto.Field(
        proto.STRING,
        number=2,
    )


class PullGitCommitsRequest(proto.Message):
    r"""``PullGitCommits`` request message.

    Attributes:
        name (str):
            Required. The workspace's name.
        remote_branch (str):
            Optional. The name of the branch in the Git
            remote from which to pull commits. If left
            unset, the repository's default branch name will
            be used.
        author (google.cloud.dataform_v1.types.CommitAuthor):
            Required. The author of any merge commit
            which may be created as a result of merging
            fetched Git commits into this workspace.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    remote_branch: str = proto.Field(
        proto.STRING,
        number=2,
    )
    author: "CommitAuthor" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="CommitAuthor",
    )


class PullGitCommitsResponse(proto.Message):
    r"""``PullGitCommits`` response message."""


class PushGitCommitsRequest(proto.Message):
    r"""``PushGitCommits`` request message.

    Attributes:
        name (str):
            Required. The workspace's name.
        remote_branch (str):
            Optional. The name of the branch in the Git
            remote to which commits should be pushed. If
            left unset, the repository's default branch name
            will be used.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    remote_branch: str = proto.Field(
        proto.STRING,
        number=2,
    )


class PushGitCommitsResponse(proto.Message):
    r"""``PushGitCommits`` response message."""


class FetchFileGitStatusesRequest(proto.Message):
    r"""``FetchFileGitStatuses`` request message.

    Attributes:
        name (str):
            Required. The workspace's name.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class FetchFileGitStatusesResponse(proto.Message):
    r"""``FetchFileGitStatuses`` response message.

    Attributes:
        uncommitted_file_changes (MutableSequence[google.cloud.dataform_v1.types.FetchFileGitStatusesResponse.UncommittedFileChange]):
            A list of all files which have uncommitted
            Git changes. There will only be a single entry
            for any given file.
    """

    class UncommittedFileChange(proto.Message):
        r"""Represents the Git state of a file with uncommitted changes.

        Attributes:
            path (str):
                The file's full path including filename,
                relative to the workspace root.
            state (google.cloud.dataform_v1.types.FetchFileGitStatusesResponse.UncommittedFileChange.State):
                Output only. Indicates the status of the
                file.
        """

        class State(proto.Enum):
            r"""Indicates the status of an uncommitted file change.

            Values:
                STATE_UNSPECIFIED (0):
                    Default value. This value is unused.
                ADDED (1):
                    The file has been newly added.
                DELETED (2):
                    The file has been deleted.
                MODIFIED (3):
                    The file has been modified.
                HAS_CONFLICTS (4):
                    The file contains merge conflicts.
            """

            STATE_UNSPECIFIED = 0
            ADDED = 1
            DELETED = 2
            MODIFIED = 3
            HAS_CONFLICTS = 4

        path: str = proto.Field(
            proto.STRING,
            number=1,
        )
        state: "FetchFileGitStatusesResponse.UncommittedFileChange.State" = proto.Field(
            proto.ENUM,
            number=2,
            enum="FetchFileGitStatusesResponse.UncommittedFileChange.State",
        )

    uncommitted_file_changes: MutableSequence[UncommittedFileChange] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=UncommittedFileChange,
        )
    )


class FetchGitAheadBehindRequest(proto.Message):
    r"""``FetchGitAheadBehind`` request message.

    Attributes:
        name (str):
            Required. The workspace's name.
        remote_branch (str):
            Optional. The name of the branch in the Git
            remote against which this workspace should be
            compared. If left unset, the repository's
            default branch name will be used.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    remote_branch: str = proto.Field(
        proto.STRING,
        number=2,
    )


class FetchGitAheadBehindResponse(proto.Message):
    r"""``FetchGitAheadBehind`` response message.

    Attributes:
        commits_ahead (int):
            The number of commits in the remote branch
            that are not in the workspace.
        commits_behind (int):
            The number of commits in the workspace that
            are not in the remote branch.
    """

    commits_ahead: int = proto.Field(
        proto.INT32,
        number=1,
    )
    commits_behind: int = proto.Field(
        proto.INT32,
        number=2,
    )


class CommitWorkspaceChangesRequest(proto.Message):
    r"""``CommitWorkspaceChanges`` request message.

    Attributes:
        name (str):
            Required. The workspace's name.
        author (google.cloud.dataform_v1.types.CommitAuthor):
            Required. The commit's author.
        commit_message (str):
            Optional. The commit's message.
        paths (MutableSequence[str]):
            Optional. Full file paths to commit including
            filename, rooted at workspace root. If left
            empty, all files will be committed.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    author: "CommitAuthor" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="CommitAuthor",
    )
    commit_message: str = proto.Field(
        proto.STRING,
        number=2,
    )
    paths: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class CommitWorkspaceChangesResponse(proto.Message):
    r"""``CommitWorkspaceChanges`` response message."""


class ResetWorkspaceChangesRequest(proto.Message):
    r"""``ResetWorkspaceChanges`` request message.

    Attributes:
        name (str):
            Required. The workspace's name.
        paths (MutableSequence[str]):
            Optional. Full file paths to reset back to
            their committed state including filename, rooted
            at workspace root. If left empty, all files will
            be reset.
        clean (bool):
            Optional. If set to true, untracked files
            will be deleted.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    paths: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )
    clean: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


class ResetWorkspaceChangesResponse(proto.Message):
    r"""``ResetWorkspaceChanges`` response message."""


class FetchFileDiffRequest(proto.Message):
    r"""``FetchFileDiff`` request message.

    Attributes:
        workspace (str):
            Required. The workspace's name.
        path (str):
            Required. The file's full path including
            filename, relative to the workspace root.
    """

    workspace: str = proto.Field(
        proto.STRING,
        number=1,
    )
    path: str = proto.Field(
        proto.STRING,
        number=2,
    )


class FetchFileDiffResponse(proto.Message):
    r"""``FetchFileDiff`` response message.

    Attributes:
        formatted_diff (str):
            The raw formatted Git diff for the file.
    """

    formatted_diff: str = proto.Field(
        proto.STRING,
        number=1,
    )


class QueryDirectoryContentsRequest(proto.Message):
    r"""``QueryDirectoryContents`` request message.

    Attributes:
        workspace (str):
            Required. The workspace's name.
        path (str):
            Optional. The directory's full path including
            directory name, relative to the workspace root.
            If left unset, the workspace root is used.
        page_size (int):
            Optional. Maximum number of paths to return.
            The server may return fewer items than
            requested. If unspecified, the server will pick
            an appropriate default.
        page_token (str):
            Optional. Page token received from a previous
            ``QueryDirectoryContents`` call. Provide this to retrieve
            the subsequent page.

            When paginating, all other parameters provided to
            ``QueryDirectoryContents``, with the exception of
            ``page_size``, must match the call that provided the page
            token.
        view (google.cloud.dataform_v1.types.DirectoryContentsView):
            Optional. Specifies the metadata to return for each
            directory entry. If unspecified, the default is
            ``DIRECTORY_CONTENTS_VIEW_BASIC``. Currently the
            ``DIRECTORY_CONTENTS_VIEW_METADATA`` view is not supported
            by CMEK-protected workspaces.
    """

    workspace: str = proto.Field(
        proto.STRING,
        number=1,
    )
    path: str = proto.Field(
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
    view: "DirectoryContentsView" = proto.Field(
        proto.ENUM,
        number=5,
        enum="DirectoryContentsView",
    )


class QueryDirectoryContentsResponse(proto.Message):
    r"""``QueryDirectoryContents`` response message.

    Attributes:
        directory_entries (MutableSequence[google.cloud.dataform_v1.types.DirectoryEntry]):
            List of entries in the directory.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    directory_entries: MutableSequence["DirectoryEntry"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="DirectoryEntry",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class DirectoryEntry(proto.Message):
    r"""Represents a single entry in a directory.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        file (str):
            A file in the directory. The path is returned
            including the full folder structure from the
            root.

            This field is a member of `oneof`_ ``entry``.
        directory (str):
            A child directory in the directory. The path
            is returned including the full folder structure
            from the root.

            This field is a member of `oneof`_ ``entry``.
        metadata (google.cloud.dataform_v1.types.FilesystemEntryMetadata):
            Entry with metadata.
    """

    file: str = proto.Field(
        proto.STRING,
        number=1,
        oneof="entry",
    )
    directory: str = proto.Field(
        proto.STRING,
        number=2,
        oneof="entry",
    )
    metadata: "FilesystemEntryMetadata" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="FilesystemEntryMetadata",
    )


class FilesystemEntryMetadata(proto.Message):
    r"""Represents metadata for a single entry in a filesystem.

    Attributes:
        size_bytes (int):
            Output only. Provides the size of the entry
            in bytes. For directories, this will be 0.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Represents the time of the last
            modification of the entry.
    """

    size_bytes: int = proto.Field(
        proto.INT64,
        number=1,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )


class SearchFilesRequest(proto.Message):
    r"""Configuration containing file search request parameters.

    Attributes:
        workspace (str):
            Required. The workspace's name.
        page_size (int):
            Optional. Maximum number of search results to
            return. The server may return fewer items than
            requested. If unspecified, the server will pick
            an appropriate default.
        page_token (str):
            Optional. Page token received from a previous
            ``SearchFilesRequest`` call. Provide this to retrieve the
            subsequent page.

            When paginating, all other parameters provided to
            ``SearchFilesRequest``, with the exception of ``page_size``,
            must match the call that provided the page token.
        filter (str):
            Optional. Optional filter for the returned list in filtering
            format. Filtering is only currently supported on the
            ``path`` field. See https://google.aip.dev/160 for details.
    """

    workspace: str = proto.Field(
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


class SearchFilesResponse(proto.Message):
    r"""Client-facing representation of a file search response.

    Attributes:
        search_results (MutableSequence[google.cloud.dataform_v1.types.SearchResult]):
            List of matched results.
        next_page_token (str):
            Optional. A token, which can be sent as ``page_token`` to
            retrieve the next page. If this field is omitted, there are
            no subsequent pages.
    """

    @property
    def raw_page(self):
        return self

    search_results: MutableSequence["SearchResult"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="SearchResult",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class SearchResult(proto.Message):
    r"""Client-facing representation of a search result entry.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        file (google.cloud.dataform_v1.types.FileSearchResult):
            Details when search result is a file.

            This field is a member of `oneof`_ ``entry``.
        directory (google.cloud.dataform_v1.types.DirectorySearchResult):
            Details when search result is a directory.

            This field is a member of `oneof`_ ``entry``.
    """

    file: "FileSearchResult" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="entry",
        message="FileSearchResult",
    )
    directory: "DirectorySearchResult" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="entry",
        message="DirectorySearchResult",
    )


class FileSearchResult(proto.Message):
    r"""Client-facing representation of a file entry in search
    results.

    Attributes:
        path (str):
            File system path relative to the workspace
            root.
    """

    path: str = proto.Field(
        proto.STRING,
        number=1,
    )


class DirectorySearchResult(proto.Message):
    r"""Client-facing representation of a directory entry in search
    results.

    Attributes:
        path (str):
            File system path relative to the workspace
            root.
    """

    path: str = proto.Field(
        proto.STRING,
        number=1,
    )


class MakeDirectoryRequest(proto.Message):
    r"""``MakeDirectory`` request message.

    Attributes:
        workspace (str):
            Required. The workspace's name.
        path (str):
            Required. The directory's full path including
            directory name, relative to the workspace root.
    """

    workspace: str = proto.Field(
        proto.STRING,
        number=1,
    )
    path: str = proto.Field(
        proto.STRING,
        number=2,
    )


class MakeDirectoryResponse(proto.Message):
    r"""``MakeDirectory`` response message."""


class RemoveDirectoryRequest(proto.Message):
    r"""``RemoveDirectory`` request message.

    Attributes:
        workspace (str):
            Required. The workspace's name.
        path (str):
            Required. The directory's full path including
            directory name, relative to the workspace root.
    """

    workspace: str = proto.Field(
        proto.STRING,
        number=1,
    )
    path: str = proto.Field(
        proto.STRING,
        number=2,
    )


class RemoveDirectoryResponse(proto.Message):
    r"""``RemoveDirectory`` response message."""


class MoveDirectoryRequest(proto.Message):
    r"""``MoveDirectory`` request message.

    Attributes:
        workspace (str):
            Required. The workspace's name.
        path (str):
            Required. The directory's full path including
            directory name, relative to the workspace root.
        new_path (str):
            Required. The new path for the directory
            including directory name, rooted at workspace
            root.
    """

    workspace: str = proto.Field(
        proto.STRING,
        number=1,
    )
    path: str = proto.Field(
        proto.STRING,
        number=2,
    )
    new_path: str = proto.Field(
        proto.STRING,
        number=3,
    )


class MoveDirectoryResponse(proto.Message):
    r"""``MoveDirectory`` response message."""


class ReadFileRequest(proto.Message):
    r"""``ReadFile`` request message.

    Attributes:
        workspace (str):
            Required. The workspace's name.
        path (str):
            Required. The file's full path including
            filename, relative to the workspace root.
        revision (str):
            Optional. The Git revision of the file to return. If left
            empty, the current contents of ``path`` will be returned.
    """

    workspace: str = proto.Field(
        proto.STRING,
        number=1,
    )
    path: str = proto.Field(
        proto.STRING,
        number=2,
    )
    revision: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ReadFileResponse(proto.Message):
    r"""``ReadFile`` response message.

    Attributes:
        file_contents (bytes):
            The file's contents.
    """

    file_contents: bytes = proto.Field(
        proto.BYTES,
        number=1,
    )


class RemoveFileRequest(proto.Message):
    r"""``RemoveFile`` request message.

    Attributes:
        workspace (str):
            Required. The workspace's name.
        path (str):
            Required. The file's full path including
            filename, relative to the workspace root.
    """

    workspace: str = proto.Field(
        proto.STRING,
        number=1,
    )
    path: str = proto.Field(
        proto.STRING,
        number=2,
    )


class RemoveFileResponse(proto.Message):
    r"""``RemoveFile`` response message."""


class MoveFileRequest(proto.Message):
    r"""``MoveFile`` request message.

    Attributes:
        workspace (str):
            Required. The workspace's name.
        path (str):
            Required. The file's full path including
            filename, relative to the workspace root.
        new_path (str):
            Required. The file's new path including
            filename, relative to the workspace root.
    """

    workspace: str = proto.Field(
        proto.STRING,
        number=1,
    )
    path: str = proto.Field(
        proto.STRING,
        number=2,
    )
    new_path: str = proto.Field(
        proto.STRING,
        number=3,
    )


class MoveFileResponse(proto.Message):
    r"""``MoveFile`` response message."""


class WriteFileRequest(proto.Message):
    r"""``WriteFile`` request message.

    Attributes:
        workspace (str):
            Required. The workspace's name.
        path (str):
            Required. The file.
        contents (bytes):
            Required. The file's contents.
    """

    workspace: str = proto.Field(
        proto.STRING,
        number=1,
    )
    path: str = proto.Field(
        proto.STRING,
        number=2,
    )
    contents: bytes = proto.Field(
        proto.BYTES,
        number=3,
    )


class WriteFileResponse(proto.Message):
    r"""``WriteFile`` response message."""


class InstallNpmPackagesRequest(proto.Message):
    r"""``InstallNpmPackages`` request message.

    Attributes:
        workspace (str):
            Required. The workspace's name.
        pipeline_config (google.cloud.dataform_v1.types.PipelineConfig):
            Optional. The pipeline options which defines
            the pipeline type and path within the Git
            repository.
    """

    workspace: str = proto.Field(
        proto.STRING,
        number=1,
    )
    pipeline_config: "PipelineConfig" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="PipelineConfig",
    )


class InstallNpmPackagesResponse(proto.Message):
    r"""``InstallNpmPackages`` response message."""


class ReleaseConfig(proto.Message):
    r"""Represents a Dataform release configuration.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Identifier. The release config's name.
        git_commitish (str):
            Required. Git commit/tag/branch name at which the repository
            should be compiled. Must exist in the remote repository.
            Examples:

            - a commit SHA: ``12ade345``
            - a tag: ``tag1``
            - a branch name: ``branch1``
        code_compilation_config (google.cloud.dataform_v1.types.CodeCompilationConfig):
            Optional. If set, fields of ``code_compilation_config``
            override the default compilation settings that are specified
            in dataform.json.
        cron_schedule (str):
            Optional. Optional schedule (in cron format)
            for automatic creation of compilation results.
        time_zone (str):
            Optional. Specifies the time zone to be used when
            interpreting cron_schedule. Must be a time zone name from
            the `time zone
            database <https://en.wikipedia.org/wiki/List_of_tz_database_time_zones>`__.
            If left unspecified, the default is ``UTC``.
        recent_scheduled_release_records (MutableSequence[google.cloud.dataform_v1.types.ReleaseConfig.ScheduledReleaseRecord]):
            Output only. Records of the 10 most recent scheduled release
            attempts, ordered in descending order of ``release_time``.
            Updated whenever automatic creation of a compilation result
            is triggered by cron_schedule.
        release_compilation_result (str):
            Optional. The name of the currently released compilation
            result for this release config. This value is updated when a
            compilation result is automatically created from this
            release config (using cron_schedule), or when this resource
            is updated by API call (perhaps to roll back to an earlier
            release). The compilation result must have been created
            using this release config. Must be in the format
            ``projects/*/locations/*/repositories/*/compilationResults/*``.
        disabled (bool):
            Optional. Disables automatic creation of
            compilation results.
        internal_metadata (str):
            Output only. All the metadata information
            that is used internally to serve the resource.
            For example: timestamps, flags, status fields,
            etc. The format of this field is a JSON string.

            This field is a member of `oneof`_ ``_internal_metadata``.
    """

    class ScheduledReleaseRecord(proto.Message):
        r"""A record of an attempt to create a compilation result for
        this release config.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            compilation_result (str):
                The name of the created compilation result, if one was
                successfully created. Must be in the format
                ``projects/*/locations/*/repositories/*/compilationResults/*``.

                This field is a member of `oneof`_ ``result``.
            error_status (google.rpc.status_pb2.Status):
                The error status encountered upon this
                attempt to create the compilation result, if the
                attempt was unsuccessful.

                This field is a member of `oneof`_ ``result``.
            release_time (google.protobuf.timestamp_pb2.Timestamp):
                Output only. The timestamp of this release
                attempt.
        """

        compilation_result: str = proto.Field(
            proto.STRING,
            number=2,
            oneof="result",
        )
        error_status: status_pb2.Status = proto.Field(
            proto.MESSAGE,
            number=3,
            oneof="result",
            message=status_pb2.Status,
        )
        release_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=1,
            message=timestamp_pb2.Timestamp,
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    git_commitish: str = proto.Field(
        proto.STRING,
        number=2,
    )
    code_compilation_config: "CodeCompilationConfig" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="CodeCompilationConfig",
    )
    cron_schedule: str = proto.Field(
        proto.STRING,
        number=4,
    )
    time_zone: str = proto.Field(
        proto.STRING,
        number=7,
    )
    recent_scheduled_release_records: MutableSequence[ScheduledReleaseRecord] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=5,
            message=ScheduledReleaseRecord,
        )
    )
    release_compilation_result: str = proto.Field(
        proto.STRING,
        number=6,
    )
    disabled: bool = proto.Field(
        proto.BOOL,
        number=8,
    )
    internal_metadata: str = proto.Field(
        proto.STRING,
        number=9,
        optional=True,
    )


class ListReleaseConfigsRequest(proto.Message):
    r"""``ListReleaseConfigs`` request message.

    Attributes:
        parent (str):
            Required. The repository in which to list release configs.
            Must be in the format
            ``projects/*/locations/*/repositories/*``.
        page_size (int):
            Optional. Maximum number of release configs
            to return. The server may return fewer items
            than requested. If unspecified, the server will
            pick an appropriate default.
        page_token (str):
            Optional. Page token received from a previous
            ``ListReleaseConfigs`` call. Provide this to retrieve the
            subsequent page.

            When paginating, all other parameters provided to
            ``ListReleaseConfigs``, with the exception of ``page_size``,
            must match the call that provided the page token.
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


class ListReleaseConfigsResponse(proto.Message):
    r"""``ListReleaseConfigs`` response message.

    Attributes:
        release_configs (MutableSequence[google.cloud.dataform_v1.types.ReleaseConfig]):
            List of release configs.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
        unreachable (MutableSequence[str]):
            Locations which could not be reached.
    """

    @property
    def raw_page(self):
        return self

    release_configs: MutableSequence["ReleaseConfig"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="ReleaseConfig",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetReleaseConfigRequest(proto.Message):
    r"""``GetReleaseConfig`` request message.

    Attributes:
        name (str):
            Required. The release config's name.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateReleaseConfigRequest(proto.Message):
    r"""``CreateReleaseConfig`` request message.

    Attributes:
        parent (str):
            Required. The repository in which to create the release
            config. Must be in the format
            ``projects/*/locations/*/repositories/*``.
        release_config (google.cloud.dataform_v1.types.ReleaseConfig):
            Required. The release config to create.
        release_config_id (str):
            Required. The ID to use for the release
            config, which will become the final component of
            the release config's resource name.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    release_config: "ReleaseConfig" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="ReleaseConfig",
    )
    release_config_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class UpdateReleaseConfigRequest(proto.Message):
    r"""``UpdateReleaseConfig`` request message.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. Specifies the fields to be updated
            in the release config. If left unset, all fields
            will be updated.
        release_config (google.cloud.dataform_v1.types.ReleaseConfig):
            Required. The release config to update.
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    release_config: "ReleaseConfig" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="ReleaseConfig",
    )


class DeleteReleaseConfigRequest(proto.Message):
    r"""``DeleteReleaseConfig`` request message.

    Attributes:
        name (str):
            Required. The release config's name.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CompilationResult(proto.Message):
    r"""Represents the result of compiling a Dataform project.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        git_commitish (str):
            Immutable. Git commit/tag/branch name at which the
            repository should be compiled. Must exist in the remote
            repository. Examples:

            - a commit SHA: ``12ade345``
            - a tag: ``tag1``
            - a branch name: ``branch1``

            This field is a member of `oneof`_ ``source``.
        workspace (str):
            Immutable. The name of the workspace to compile. Must be in
            the format
            ``projects/*/locations/*/repositories/*/workspaces/*``.

            This field is a member of `oneof`_ ``source``.
        release_config (str):
            Immutable. The name of the release config to compile. Must
            be in the format
            ``projects/*/locations/*/repositories/*/releaseConfigs/*``.

            This field is a member of `oneof`_ ``source``.
        name (str):
            Output only. The compilation result's name.
        code_compilation_config (google.cloud.dataform_v1.types.CodeCompilationConfig):
            Immutable. If set, fields of ``code_compilation_config``
            override the default compilation settings that are specified
            in dataform.json.
        resolved_git_commit_sha (str):
            Output only. The fully resolved Git commit
            SHA of the code that was compiled. Not set for
            compilation results whose source is a workspace.
        dataform_core_version (str):
            Output only. The version of ``@dataform/core`` that was used
            for compilation.
        compilation_errors (MutableSequence[google.cloud.dataform_v1.types.CompilationResult.CompilationError]):
            Output only. Errors encountered during
            project compilation.
        data_encryption_state (google.cloud.dataform_v1.types.DataEncryptionState):
            Output only. Only set if the repository has a
            KMS Key.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp of when the
            compilation result was created.
        internal_metadata (str):
            Output only. All the metadata information
            that is used internally to serve the resource.
            For example: timestamps, flags, status fields,
            etc. The format of this field is a JSON string.

            This field is a member of `oneof`_ ``_internal_metadata``.
        private_resource_metadata (google.cloud.dataform_v1.types.PrivateResourceMetadata):
            Output only. Metadata indicating whether this resource is
            user-scoped. ``CompilationResult`` resource is
            ``user_scoped`` only if it is sourced from a workspace.
        gcs_repository_snapshot_metadata (google.cloud.dataform_v1.types.GcsRepositorySnapshotMetadata):
            Output only. Metadata about the repository
            snapshot used by scheduled notebooks.
    """

    class CompilationError(proto.Message):
        r"""An error encountered when attempting to compile a Dataform
        project.

        Attributes:
            message (str):
                Output only. The error's top level message.
            stack (str):
                Output only. The error's full stack trace.
            path (str):
                Output only. The path of the file where this
                error occurred, if available, relative to the
                project root.
            action_target (google.cloud.dataform_v1.types.Target):
                Output only. The identifier of the action
                where this error occurred, if available.
        """

        message: str = proto.Field(
            proto.STRING,
            number=1,
        )
        stack: str = proto.Field(
            proto.STRING,
            number=2,
        )
        path: str = proto.Field(
            proto.STRING,
            number=3,
        )
        action_target: "Target" = proto.Field(
            proto.MESSAGE,
            number=4,
            message="Target",
        )

    git_commitish: str = proto.Field(
        proto.STRING,
        number=2,
        oneof="source",
    )
    workspace: str = proto.Field(
        proto.STRING,
        number=3,
        oneof="source",
    )
    release_config: str = proto.Field(
        proto.STRING,
        number=7,
        oneof="source",
    )
    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    code_compilation_config: "CodeCompilationConfig" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="CodeCompilationConfig",
    )
    resolved_git_commit_sha: str = proto.Field(
        proto.STRING,
        number=8,
    )
    dataform_core_version: str = proto.Field(
        proto.STRING,
        number=5,
    )
    compilation_errors: MutableSequence[CompilationError] = proto.RepeatedField(
        proto.MESSAGE,
        number=6,
        message=CompilationError,
    )
    data_encryption_state: "DataEncryptionState" = proto.Field(
        proto.MESSAGE,
        number=9,
        message="DataEncryptionState",
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=10,
        message=timestamp_pb2.Timestamp,
    )
    internal_metadata: str = proto.Field(
        proto.STRING,
        number=11,
        optional=True,
    )
    private_resource_metadata: "PrivateResourceMetadata" = proto.Field(
        proto.MESSAGE,
        number=12,
        message="PrivateResourceMetadata",
    )
    gcs_repository_snapshot_metadata: "GcsRepositorySnapshotMetadata" = proto.Field(
        proto.MESSAGE,
        number=13,
        message="GcsRepositorySnapshotMetadata",
    )


class CodeCompilationConfig(proto.Message):
    r"""Configures various aspects of Dataform code compilation.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        default_database (str):
            Optional. The default database (Google Cloud
            project ID).
        default_schema (str):
            Optional. The default schema (BigQuery
            dataset ID).
        default_location (str):
            Optional. The default BigQuery location to
            use. Defaults to "US". See the BigQuery docs for
            a full list of locations:

            https://cloud.google.com/bigquery/docs/locations.
        assertion_schema (str):
            Optional. The default schema (BigQuery
            dataset ID) for assertions.
        vars (MutableMapping[str, str]):
            Optional. User-defined variables that are
            made available to project code during
            compilation.
        database_suffix (str):
            Optional. The suffix that should be appended
            to all database (Google Cloud project ID) names.
        schema_suffix (str):
            Optional. The suffix that should be appended
            to all schema (BigQuery dataset ID) names.
        table_prefix (str):
            Optional. The prefix that should be prepended
            to all table names.
        builtin_assertion_name_prefix (str):
            Optional. The prefix to prepend to built-in
            assertion names.
        default_notebook_runtime_options (google.cloud.dataform_v1.types.NotebookRuntimeOptions):
            Optional. The default notebook runtime
            options.
        pipeline_config (google.cloud.dataform_v1.types.PipelineConfig):
            Optional. The pipeline options which defines
            the pipeline type and path within the Git
            repository.
        lineage_enabled (bool):
            Output only. Whether OpenLineage events are emitted for
            actions in this workflow. Reflects the ``lineage.enabled``
            setting from ``workflow_settings.yaml``.

            This field is a member of `oneof`_ ``_lineage_enabled``.
    """

    default_database: str = proto.Field(
        proto.STRING,
        number=1,
    )
    default_schema: str = proto.Field(
        proto.STRING,
        number=2,
    )
    default_location: str = proto.Field(
        proto.STRING,
        number=8,
    )
    assertion_schema: str = proto.Field(
        proto.STRING,
        number=3,
    )
    vars: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=4,
    )
    database_suffix: str = proto.Field(
        proto.STRING,
        number=5,
    )
    schema_suffix: str = proto.Field(
        proto.STRING,
        number=6,
    )
    table_prefix: str = proto.Field(
        proto.STRING,
        number=7,
    )
    builtin_assertion_name_prefix: str = proto.Field(
        proto.STRING,
        number=10,
    )
    default_notebook_runtime_options: "NotebookRuntimeOptions" = proto.Field(
        proto.MESSAGE,
        number=9,
        message="NotebookRuntimeOptions",
    )
    pipeline_config: "PipelineConfig" = proto.Field(
        proto.MESSAGE,
        number=12,
        message="PipelineConfig",
    )
    lineage_enabled: bool = proto.Field(
        proto.BOOL,
        number=14,
        optional=True,
    )


class GcsRepositorySnapshotMetadata(proto.Message):
    r"""Metadata about a repository snapshot stored in Google Cloud
    Storage.

    Attributes:
        repository_snapshot_uri (str):
            Output only. The Google Cloud Storage URI of
            the repository snapshot.
        crc32c_checksum (str):
            Output only. The crc32c checksum of the
            repository snapshot, big-endian base64 encoded.
        generation (int):
            Output only. The generation number of the
            Cloud Storage object. See
            https://cloud.google.com/storage/docs/metadata#generation-number.
    """

    repository_snapshot_uri: str = proto.Field(
        proto.STRING,
        number=1,
    )
    crc32c_checksum: str = proto.Field(
        proto.STRING,
        number=2,
    )
    generation: int = proto.Field(
        proto.INT64,
        number=3,
    )


class GcsRepositorySnapshotDestination(proto.Message):
    r"""Configures the destination for a repository snapshot.

    Attributes:
        repository_snapshot_uri (str):
            Optional. The Google Cloud Storage destination to upload the
            repository snapshot to. Format: ``gs://bucket-name/path/``.
    """

    repository_snapshot_uri: str = proto.Field(
        proto.STRING,
        number=1,
    )


class NotebookRuntimeOptions(proto.Message):
    r"""Configures various aspects of Dataform notebook runtime.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        gcs_output_bucket (str):
            Optional. The Google Cloud Storage location to upload the
            result to. Format: ``gs://bucket-name``.

            This field is a member of `oneof`_ ``execution_sink``.
        gcs_repository_snapshot_destination (google.cloud.dataform_v1.types.GcsRepositorySnapshotDestination):
            Optional. The Google Cloud Storage destination to upload the
            snapshot to. For empty URI it defaults to the provided
            gcs_output_bucket. Format: ``gs://bucket-name/path/``.

            This field is a member of `oneof`_ ``repository_snapshot_storage``.
        ai_platform_notebook_runtime_template (str):
            Optional. The resource name of the [Colab runtime template]
            (https://cloud.google.com/colab/docs/runtimes), from which a
            runtime is created for notebook executions. If not
            specified, a runtime is created with Colab's default
            specifications.
    """

    gcs_output_bucket: str = proto.Field(
        proto.STRING,
        number=1,
        oneof="execution_sink",
    )
    gcs_repository_snapshot_destination: "GcsRepositorySnapshotDestination" = (
        proto.Field(
            proto.MESSAGE,
            number=3,
            oneof="repository_snapshot_storage",
            message="GcsRepositorySnapshotDestination",
        )
    )
    ai_platform_notebook_runtime_template: str = proto.Field(
        proto.STRING,
        number=2,
    )


class PipelineConfig(proto.Message):
    r"""Defines the pipeline type and path within the Git repository.

    Attributes:
        pipeline_type (google.cloud.dataform_v1.types.PipelineConfig.PipelineType):
            Required. The type of the pipeline.
        path (str):
            Required. The relative path within the Git repository where
            the pipeline is defined. For example, for a Dataform
            pipeline, it is a path to the folder where
            ``workflow_settings.yaml`` or ``dataform.json`` is located.
    """

    class PipelineType(proto.Enum):
        r"""The type of the pipeline. This may be extended in the future.
        In case of UNSPECIFIED, the error will be thrown.

        Values:
            PIPELINE_TYPE_UNSPECIFIED (0):
                Default value. This value is unused.
            DATAFORM (1):
                Regular Dataform pipeline.
            SQL (3):
                SQL single file asset.
            NOTEBOOK (4):
                Notebook single file asset.
        """

        PIPELINE_TYPE_UNSPECIFIED = 0
        DATAFORM = 1
        SQL = 3
        NOTEBOOK = 4

    pipeline_type: PipelineType = proto.Field(
        proto.ENUM,
        number=1,
        enum=PipelineType,
    )
    path: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ListCompilationResultsRequest(proto.Message):
    r"""``ListCompilationResults`` request message.

    Attributes:
        parent (str):
            Required. The repository in which to list compilation
            results. Must be in the format
            ``projects/*/locations/*/repositories/*``.
        page_size (int):
            Optional. Maximum number of compilation
            results to return. The server may return fewer
            items than requested. If unspecified, the server
            will pick an appropriate default.
        page_token (str):
            Optional. Page token received from a previous
            ``ListCompilationResults`` call. Provide this to retrieve
            the subsequent page.

            When paginating, all other parameters provided to
            ``ListCompilationResults``, with the exception of
            ``page_size``, must match the call that provided the page
            token.
        order_by (str):
            Optional. This field only supports ordering by ``name`` and
            ``create_time``. If unspecified, the server will choose the
            ordering. If specified, the default order is ascending for
            the ``name`` field.
        filter (str):
            Optional. Filter for the returned list.
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
    filter: str = proto.Field(
        proto.STRING,
        number=5,
    )


class ListCompilationResultsResponse(proto.Message):
    r"""``ListCompilationResults`` response message.

    Attributes:
        compilation_results (MutableSequence[google.cloud.dataform_v1.types.CompilationResult]):
            List of compilation results.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
        unreachable (MutableSequence[str]):
            Locations which could not be reached.
    """

    @property
    def raw_page(self):
        return self

    compilation_results: MutableSequence["CompilationResult"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="CompilationResult",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetCompilationResultRequest(proto.Message):
    r"""``GetCompilationResult`` request message.

    Attributes:
        name (str):
            Required. The compilation result's name.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateCompilationResultRequest(proto.Message):
    r"""``CreateCompilationResult`` request message.

    Attributes:
        parent (str):
            Required. The repository in which to create the compilation
            result. Must be in the format
            ``projects/*/locations/*/repositories/*``.
        compilation_result (google.cloud.dataform_v1.types.CompilationResult):
            Required. The compilation result to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    compilation_result: "CompilationResult" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="CompilationResult",
    )


class Target(proto.Message):
    r"""Represents an action identifier. If the action writes output,
    the output will be written to the referenced database object.

    Attributes:
        database (str):
            Optional. The action's database (Google Cloud
            project ID) .
        schema (str):
            Optional. The action's schema (BigQuery dataset ID), within
            ``database``.
        name (str):
            Optional. The action's name, within ``database`` and
            ``schema``.
    """

    database: str = proto.Field(
        proto.STRING,
        number=1,
    )
    schema: str = proto.Field(
        proto.STRING,
        number=2,
    )
    name: str = proto.Field(
        proto.STRING,
        number=3,
    )


class RelationDescriptor(proto.Message):
    r"""Describes a relation and its columns.

    Attributes:
        description (str):
            A text description of the relation.
        columns (MutableSequence[google.cloud.dataform_v1.types.RelationDescriptor.ColumnDescriptor]):
            A list of descriptions of columns within the
            relation.
        bigquery_labels (MutableMapping[str, str]):
            A set of BigQuery labels that should be
            applied to the relation.
    """

    class ColumnDescriptor(proto.Message):
        r"""Describes a column.

        Attributes:
            path (MutableSequence[str]):
                The identifier for the column. Each entry in ``path``
                represents one level of nesting.
            description (str):
                A textual description of the column.
            bigquery_policy_tags (MutableSequence[str]):
                A list of BigQuery policy tags that will be
                applied to the column.
        """

        path: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=1,
        )
        description: str = proto.Field(
            proto.STRING,
            number=2,
        )
        bigquery_policy_tags: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=3,
        )

    description: str = proto.Field(
        proto.STRING,
        number=1,
    )
    columns: MutableSequence[ColumnDescriptor] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message=ColumnDescriptor,
    )
    bigquery_labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=3,
    )


class CompilationResultAction(proto.Message):
    r"""Represents a single Dataform action in a compilation result.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        relation (google.cloud.dataform_v1.types.CompilationResultAction.Relation):
            The database relation created/updated by this
            action.

            This field is a member of `oneof`_ ``compiled_object``.
        operations (google.cloud.dataform_v1.types.CompilationResultAction.Operations):
            The database operations executed by this
            action.

            This field is a member of `oneof`_ ``compiled_object``.
        assertion (google.cloud.dataform_v1.types.CompilationResultAction.Assertion):
            The assertion executed by this action.

            This field is a member of `oneof`_ ``compiled_object``.
        declaration (google.cloud.dataform_v1.types.CompilationResultAction.Declaration):
            The declaration declared by this action.

            This field is a member of `oneof`_ ``compiled_object``.
        notebook (google.cloud.dataform_v1.types.CompilationResultAction.Notebook):
            The notebook executed by this action.

            This field is a member of `oneof`_ ``compiled_object``.
        data_preparation (google.cloud.dataform_v1.types.CompilationResultAction.DataPreparation):
            The data preparation executed by this action.

            This field is a member of `oneof`_ ``compiled_object``.
        target (google.cloud.dataform_v1.types.Target):
            This action's identifier. Unique within the
            compilation result.
        canonical_target (google.cloud.dataform_v1.types.Target):
            The action's identifier if the project had
            been compiled without any overrides configured.
            Unique within the compilation result.
        file_path (str):
            The full path including filename in which
            this action is located, relative to the
            workspace root.
        internal_metadata (str):
            Output only. All the metadata information
            that is used internally to serve the resource.
            For example: timestamps, flags, status fields,
            etc. The format of this field is a JSON string.

            This field is a member of `oneof`_ ``_internal_metadata``.
    """

    class Relation(proto.Message):
        r"""Represents a database relation.

        Attributes:
            dependency_targets (MutableSequence[google.cloud.dataform_v1.types.Target]):
                A list of actions that this action depends
                on.
            disabled (bool):
                Whether this action is disabled (i.e. should
                not be run).
            tags (MutableSequence[str]):
                Arbitrary, user-defined tags on this action.
            relation_descriptor (google.cloud.dataform_v1.types.RelationDescriptor):
                Descriptor for the relation and its columns.
            relation_type (google.cloud.dataform_v1.types.CompilationResultAction.Relation.RelationType):
                The type of this relation.
            select_query (str):
                The SELECT query which returns rows which
                this relation should contain.
            pre_operations (MutableSequence[str]):
                SQL statements to be executed before creating
                the relation.
            post_operations (MutableSequence[str]):
                SQL statements to be executed after creating
                the relation.
            incremental_table_config (google.cloud.dataform_v1.types.CompilationResultAction.Relation.IncrementalTableConfig):
                Configures ``INCREMENTAL_TABLE`` settings for this relation.
                Only set if ``relation_type`` is ``INCREMENTAL_TABLE``.
            partition_expression (str):
                The SQL expression used to partition the
                relation.
            cluster_expressions (MutableSequence[str]):
                A list of columns or SQL expressions used to
                cluster the table.
            partition_expiration_days (int):
                Sets the partition expiration in days.
            require_partition_filter (bool):
                Specifies whether queries on this table must
                include a predicate filter that filters on the
                partitioning column.
            additional_options (MutableMapping[str, str]):
                Additional options that will be provided as
                key/value pairs into the options clause of a
                create table/view statement. See
                https://cloud.google.com/bigquery/docs/reference/standard-sql/data-definition-language
                for more information on which options are
                supported.
            connection (str):
                Optional. The connection specifying the credentials to be
                used to read and write to external storage, such as Cloud
                Storage. The connection can have the form
                ``{project}.{location}.{connection_id}`` or
                ``projects/{project}/locations/{location}/connections/{connection_id}``,
                or be set to DEFAULT.
            table_format (google.cloud.dataform_v1.types.CompilationResultAction.Relation.TableFormat):
                Optional. The table format for the BigQuery
                table.
            file_format (google.cloud.dataform_v1.types.CompilationResultAction.Relation.FileFormat):
                Optional. The file format for the BigQuery
                table.
            storage_uri (str):
                Optional. The fully qualified location prefix of the
                external folder where table data is stored. The URI should
                be in the format ``gs://bucket/path_to_table/``.
        """

        class RelationType(proto.Enum):
            r"""Indicates the type of this relation.

            Values:
                RELATION_TYPE_UNSPECIFIED (0):
                    Default value. This value is unused.
                TABLE (1):
                    The relation is a table.
                VIEW (2):
                    The relation is a view.
                INCREMENTAL_TABLE (3):
                    The relation is an incrementalized table.
                MATERIALIZED_VIEW (4):
                    The relation is a materialized view.
            """

            RELATION_TYPE_UNSPECIFIED = 0
            TABLE = 1
            VIEW = 2
            INCREMENTAL_TABLE = 3
            MATERIALIZED_VIEW = 4

        class TableFormat(proto.Enum):
            r"""Supported table formats for BigQuery tables.

            Values:
                TABLE_FORMAT_UNSPECIFIED (0):
                    Default value.
                ICEBERG (1):
                    Apache Iceberg format.
            """

            TABLE_FORMAT_UNSPECIFIED = 0
            ICEBERG = 1

        class FileFormat(proto.Enum):
            r"""Supported file formats for BigQuery tables.

            Values:
                FILE_FORMAT_UNSPECIFIED (0):
                    Default value.
                PARQUET (1):
                    Apache Parquet format.
            """

            FILE_FORMAT_UNSPECIFIED = 0
            PARQUET = 1

        class IncrementalTableConfig(proto.Message):
            r"""Contains settings for relations of type ``INCREMENTAL_TABLE``.

            Attributes:
                incremental_select_query (str):
                    The SELECT query which returns rows which
                    should be inserted into the relation if it
                    already exists and is not being refreshed.
                refresh_disabled (bool):
                    Whether this table should be protected from
                    being refreshed.
                unique_key_parts (MutableSequence[str]):
                    A set of columns or SQL expressions used to define row
                    uniqueness. If any duplicates are discovered (as defined by
                    ``unique_key_parts``), only the newly selected rows (as
                    defined by ``incremental_select_query``) will be included in
                    the relation.
                update_partition_filter (str):
                    A SQL expression conditional used to limit the set of
                    existing rows considered for a merge operation (see
                    ``unique_key_parts`` for more information).
                incremental_pre_operations (MutableSequence[str]):
                    SQL statements to be executed before
                    inserting new rows into the relation.
                incremental_post_operations (MutableSequence[str]):
                    SQL statements to be executed after inserting
                    new rows into the relation.
            """

            incremental_select_query: str = proto.Field(
                proto.STRING,
                number=1,
            )
            refresh_disabled: bool = proto.Field(
                proto.BOOL,
                number=2,
            )
            unique_key_parts: MutableSequence[str] = proto.RepeatedField(
                proto.STRING,
                number=3,
            )
            update_partition_filter: str = proto.Field(
                proto.STRING,
                number=4,
            )
            incremental_pre_operations: MutableSequence[str] = proto.RepeatedField(
                proto.STRING,
                number=5,
            )
            incremental_post_operations: MutableSequence[str] = proto.RepeatedField(
                proto.STRING,
                number=6,
            )

        dependency_targets: MutableSequence["Target"] = proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="Target",
        )
        disabled: bool = proto.Field(
            proto.BOOL,
            number=2,
        )
        tags: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=3,
        )
        relation_descriptor: "RelationDescriptor" = proto.Field(
            proto.MESSAGE,
            number=4,
            message="RelationDescriptor",
        )
        relation_type: "CompilationResultAction.Relation.RelationType" = proto.Field(
            proto.ENUM,
            number=5,
            enum="CompilationResultAction.Relation.RelationType",
        )
        select_query: str = proto.Field(
            proto.STRING,
            number=6,
        )
        pre_operations: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=7,
        )
        post_operations: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=8,
        )
        incremental_table_config: "CompilationResultAction.Relation.IncrementalTableConfig" = proto.Field(
            proto.MESSAGE,
            number=9,
            message="CompilationResultAction.Relation.IncrementalTableConfig",
        )
        partition_expression: str = proto.Field(
            proto.STRING,
            number=10,
        )
        cluster_expressions: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=11,
        )
        partition_expiration_days: int = proto.Field(
            proto.INT32,
            number=12,
        )
        require_partition_filter: bool = proto.Field(
            proto.BOOL,
            number=13,
        )
        additional_options: MutableMapping[str, str] = proto.MapField(
            proto.STRING,
            proto.STRING,
            number=14,
        )
        connection: str = proto.Field(
            proto.STRING,
            number=15,
        )
        table_format: "CompilationResultAction.Relation.TableFormat" = proto.Field(
            proto.ENUM,
            number=16,
            enum="CompilationResultAction.Relation.TableFormat",
        )
        file_format: "CompilationResultAction.Relation.FileFormat" = proto.Field(
            proto.ENUM,
            number=17,
            enum="CompilationResultAction.Relation.FileFormat",
        )
        storage_uri: str = proto.Field(
            proto.STRING,
            number=18,
        )

    class Operations(proto.Message):
        r"""Represents a list of arbitrary database operations.

        Attributes:
            dependency_targets (MutableSequence[google.cloud.dataform_v1.types.Target]):
                A list of actions that this action depends
                on.
            disabled (bool):
                Whether this action is disabled (i.e. should
                not be run).
            tags (MutableSequence[str]):
                Arbitrary, user-defined tags on this action.
            relation_descriptor (google.cloud.dataform_v1.types.RelationDescriptor):
                Descriptor for any output relation and its columns. Only set
                if ``has_output`` is true.
            queries (MutableSequence[str]):
                A list of arbitrary SQL statements that will
                be executed without alteration.
            has_output (bool):
                Whether these operations produce an output
                relation.
        """

        dependency_targets: MutableSequence["Target"] = proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="Target",
        )
        disabled: bool = proto.Field(
            proto.BOOL,
            number=2,
        )
        tags: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=3,
        )
        relation_descriptor: "RelationDescriptor" = proto.Field(
            proto.MESSAGE,
            number=6,
            message="RelationDescriptor",
        )
        queries: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=4,
        )
        has_output: bool = proto.Field(
            proto.BOOL,
            number=5,
        )

    class Assertion(proto.Message):
        r"""Represents an assertion upon a SQL query which is required
        return zero rows.

        Attributes:
            dependency_targets (MutableSequence[google.cloud.dataform_v1.types.Target]):
                A list of actions that this action depends
                on.
            parent_action (google.cloud.dataform_v1.types.Target):
                The parent action of this assertion. Only set
                if this assertion was automatically generated.
            disabled (bool):
                Whether this action is disabled (i.e. should
                not be run).
            tags (MutableSequence[str]):
                Arbitrary, user-defined tags on this action.
            select_query (str):
                The SELECT query which must return zero rows
                in order for this assertion to succeed.
            relation_descriptor (google.cloud.dataform_v1.types.RelationDescriptor):
                Descriptor for the assertion's
                automatically-generated view and its columns.
        """

        dependency_targets: MutableSequence["Target"] = proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="Target",
        )
        parent_action: "Target" = proto.Field(
            proto.MESSAGE,
            number=5,
            message="Target",
        )
        disabled: bool = proto.Field(
            proto.BOOL,
            number=2,
        )
        tags: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=3,
        )
        select_query: str = proto.Field(
            proto.STRING,
            number=4,
        )
        relation_descriptor: "RelationDescriptor" = proto.Field(
            proto.MESSAGE,
            number=6,
            message="RelationDescriptor",
        )

    class Declaration(proto.Message):
        r"""Represents a relation which is not managed by Dataform but
        which may be referenced by Dataform actions.

        Attributes:
            relation_descriptor (google.cloud.dataform_v1.types.RelationDescriptor):
                Descriptor for the relation and its columns.
                Used as documentation only, i.e. values here
                will result in no changes to the relation's
                metadata.
        """

        relation_descriptor: "RelationDescriptor" = proto.Field(
            proto.MESSAGE,
            number=1,
            message="RelationDescriptor",
        )

    class Notebook(proto.Message):
        r"""Represents a notebook.

        Attributes:
            dependency_targets (MutableSequence[google.cloud.dataform_v1.types.Target]):
                A list of actions that this action depends
                on.
            disabled (bool):
                Whether this action is disabled (i.e. should
                not be run).
            contents (str):
                The contents of the notebook.
            tags (MutableSequence[str]):
                Arbitrary, user-defined tags on this action.
        """

        dependency_targets: MutableSequence["Target"] = proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="Target",
        )
        disabled: bool = proto.Field(
            proto.BOOL,
            number=2,
        )
        contents: str = proto.Field(
            proto.STRING,
            number=3,
        )
        tags: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=4,
        )

    class DataPreparation(proto.Message):
        r"""Defines a compiled Data Preparation entity

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            contents_yaml (str):
                The data preparation definition, stored as a
                YAML string.

                This field is a member of `oneof`_ ``definition``.
            contents_sql (google.cloud.dataform_v1.types.CompilationResultAction.DataPreparation.SqlDefinition):
                SQL definition for a Data Preparation.
                Contains a SQL query and additional context
                information.

                This field is a member of `oneof`_ ``definition``.
            dependency_targets (MutableSequence[google.cloud.dataform_v1.types.Target]):
                A list of actions that this action depends
                on.
            disabled (bool):
                Whether this action is disabled (i.e. should
                not be run).
            tags (MutableSequence[str]):
                Arbitrary, user-defined tags on this action.
        """

        class SqlDefinition(proto.Message):
            r"""Definition of a SQL Data Preparation

            Attributes:
                query (str):
                    The SQL query representing the data
                    preparation steps. Formatted as a Pipe SQL query
                    statement.
                error_table (google.cloud.dataform_v1.types.CompilationResultAction.DataPreparation.ErrorTable):
                    Error table configuration,
                load (google.cloud.dataform_v1.types.CompilationResultAction.LoadConfig):
                    Load configuration.
            """

            query: str = proto.Field(
                proto.STRING,
                number=1,
            )
            error_table: "CompilationResultAction.DataPreparation.ErrorTable" = (
                proto.Field(
                    proto.MESSAGE,
                    number=2,
                    message="CompilationResultAction.DataPreparation.ErrorTable",
                )
            )
            load: "CompilationResultAction.LoadConfig" = proto.Field(
                proto.MESSAGE,
                number=3,
                message="CompilationResultAction.LoadConfig",
            )

        class ErrorTable(proto.Message):
            r"""Error table information, used to write error data into a
            BigQuery table.

            Attributes:
                target (google.cloud.dataform_v1.types.Target):
                    Error Table target.
                retention_days (int):
                    Error table partition expiration in days.
                    Only positive values are allowed.
            """

            target: "Target" = proto.Field(
                proto.MESSAGE,
                number=1,
                message="Target",
            )
            retention_days: int = proto.Field(
                proto.INT32,
                number=2,
            )

        contents_yaml: str = proto.Field(
            proto.STRING,
            number=5,
            oneof="definition",
        )
        contents_sql: "CompilationResultAction.DataPreparation.SqlDefinition" = (
            proto.Field(
                proto.MESSAGE,
                number=6,
                oneof="definition",
                message="CompilationResultAction.DataPreparation.SqlDefinition",
            )
        )
        dependency_targets: MutableSequence["Target"] = proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="Target",
        )
        disabled: bool = proto.Field(
            proto.BOOL,
            number=2,
        )
        tags: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=4,
        )

    class LoadConfig(proto.Message):
        r"""Simplified load configuration for actions

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            replace (google.cloud.dataform_v1.types.CompilationResultAction.SimpleLoadMode):
                Replace destination table

                This field is a member of `oneof`_ ``mode``.
            append (google.cloud.dataform_v1.types.CompilationResultAction.SimpleLoadMode):
                Append into destination table

                This field is a member of `oneof`_ ``mode``.
            maximum (google.cloud.dataform_v1.types.CompilationResultAction.IncrementalLoadMode):
                Insert records where the value exceeds the
                previous maximum value for a column in the
                destination table

                This field is a member of `oneof`_ ``mode``.
            unique (google.cloud.dataform_v1.types.CompilationResultAction.IncrementalLoadMode):
                Insert records where the value of a column is
                not already present in the destination table

                This field is a member of `oneof`_ ``mode``.
        """

        replace: "CompilationResultAction.SimpleLoadMode" = proto.Field(
            proto.MESSAGE,
            number=1,
            oneof="mode",
            message="CompilationResultAction.SimpleLoadMode",
        )
        append: "CompilationResultAction.SimpleLoadMode" = proto.Field(
            proto.MESSAGE,
            number=2,
            oneof="mode",
            message="CompilationResultAction.SimpleLoadMode",
        )
        maximum: "CompilationResultAction.IncrementalLoadMode" = proto.Field(
            proto.MESSAGE,
            number=3,
            oneof="mode",
            message="CompilationResultAction.IncrementalLoadMode",
        )
        unique: "CompilationResultAction.IncrementalLoadMode" = proto.Field(
            proto.MESSAGE,
            number=4,
            oneof="mode",
            message="CompilationResultAction.IncrementalLoadMode",
        )

    class SimpleLoadMode(proto.Message):
        r"""Simple load definition"""

    class IncrementalLoadMode(proto.Message):
        r"""Load definition for incremental load modes

        Attributes:
            column (str):
                Column name for incremental load modes
        """

        column: str = proto.Field(
            proto.STRING,
            number=1,
        )

    relation: Relation = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="compiled_object",
        message=Relation,
    )
    operations: Operations = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="compiled_object",
        message=Operations,
    )
    assertion: Assertion = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="compiled_object",
        message=Assertion,
    )
    declaration: Declaration = proto.Field(
        proto.MESSAGE,
        number=7,
        oneof="compiled_object",
        message=Declaration,
    )
    notebook: Notebook = proto.Field(
        proto.MESSAGE,
        number=8,
        oneof="compiled_object",
        message=Notebook,
    )
    data_preparation: DataPreparation = proto.Field(
        proto.MESSAGE,
        number=9,
        oneof="compiled_object",
        message=DataPreparation,
    )
    target: "Target" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Target",
    )
    canonical_target: "Target" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Target",
    )
    file_path: str = proto.Field(
        proto.STRING,
        number=3,
    )
    internal_metadata: str = proto.Field(
        proto.STRING,
        number=10,
        optional=True,
    )


class QueryCompilationResultActionsRequest(proto.Message):
    r"""``QueryCompilationResultActions`` request message.

    Attributes:
        name (str):
            Required. The compilation result's name.
        page_size (int):
            Optional. Maximum number of compilation
            results to return. The server may return fewer
            items than requested. If unspecified, the server
            will pick an appropriate default.
        page_token (str):
            Optional. Page token received from a previous
            ``QueryCompilationResultActions`` call. Provide this to
            retrieve the subsequent page.

            When paginating, all other parameters provided to
            ``QueryCompilationResultActions``, with the exception of
            ``page_size``, must match the call that provided the page
            token.
        filter (str):
            Optional. Optional filter for the returned list. Filtering
            is only currently supported on the ``file_path`` field.
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
    filter: str = proto.Field(
        proto.STRING,
        number=4,
    )


class QueryCompilationResultActionsResponse(proto.Message):
    r"""``QueryCompilationResultActions`` response message.

    Attributes:
        compilation_result_actions (MutableSequence[google.cloud.dataform_v1.types.CompilationResultAction]):
            List of compilation result actions.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    compilation_result_actions: MutableSequence["CompilationResultAction"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="CompilationResultAction",
        )
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class WorkflowConfig(proto.Message):
    r"""Represents a Dataform workflow configuration.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Identifier. The workflow config's name.
        release_config (str):
            Required. The name of the release config whose
            release_compilation_result should be executed. Must be in
            the format
            ``projects/*/locations/*/repositories/*/releaseConfigs/*``.
        invocation_config (google.cloud.dataform_v1.types.InvocationConfig):
            Optional. If left unset, a default
            InvocationConfig will be used.
        cron_schedule (str):
            Optional. Optional schedule (in cron format)
            for automatic execution of this workflow config.
        time_zone (str):
            Optional. Specifies the time zone to be used when
            interpreting cron_schedule. Must be a time zone name from
            the `time zone
            database <https://en.wikipedia.org/wiki/List_of_tz_database_time_zones>`__.
            If left unspecified, the default is ``UTC``.
        recent_scheduled_execution_records (MutableSequence[google.cloud.dataform_v1.types.WorkflowConfig.ScheduledExecutionRecord]):
            Output only. Records of the 10 most recent scheduled
            execution attempts, ordered in descending order of
            ``execution_time``. Updated whenever automatic creation of a
            workflow invocation is triggered by cron_schedule.
        disabled (bool):
            Optional. Disables automatic creation of
            workflow invocations.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp of when the
            WorkflowConfig was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp of when the
            WorkflowConfig was last updated.
        internal_metadata (str):
            Output only. All the metadata information
            that is used internally to serve the resource.
            For example: timestamps, flags, status fields,
            etc. The format of this field is a JSON string.

            This field is a member of `oneof`_ ``_internal_metadata``.
    """

    class ScheduledExecutionRecord(proto.Message):
        r"""A record of an attempt to create a workflow invocation for
        this workflow config.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            workflow_invocation (str):
                The name of the created workflow invocation, if one was
                successfully created. Must be in the format
                ``projects/*/locations/*/repositories/*/workflowInvocations/*``.

                This field is a member of `oneof`_ ``result``.
            error_status (google.rpc.status_pb2.Status):
                The error status encountered upon this
                attempt to create the workflow invocation, if
                the attempt was unsuccessful.

                This field is a member of `oneof`_ ``result``.
            execution_time (google.protobuf.timestamp_pb2.Timestamp):
                Output only. The timestamp of this execution
                attempt.
        """

        workflow_invocation: str = proto.Field(
            proto.STRING,
            number=2,
            oneof="result",
        )
        error_status: status_pb2.Status = proto.Field(
            proto.MESSAGE,
            number=3,
            oneof="result",
            message=status_pb2.Status,
        )
        execution_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=1,
            message=timestamp_pb2.Timestamp,
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    release_config: str = proto.Field(
        proto.STRING,
        number=2,
    )
    invocation_config: "InvocationConfig" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="InvocationConfig",
    )
    cron_schedule: str = proto.Field(
        proto.STRING,
        number=4,
    )
    time_zone: str = proto.Field(
        proto.STRING,
        number=7,
    )
    recent_scheduled_execution_records: MutableSequence[ScheduledExecutionRecord] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=5,
            message=ScheduledExecutionRecord,
        )
    )
    disabled: bool = proto.Field(
        proto.BOOL,
        number=8,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=9,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=10,
        message=timestamp_pb2.Timestamp,
    )
    internal_metadata: str = proto.Field(
        proto.STRING,
        number=11,
        optional=True,
    )


class InvocationConfig(proto.Message):
    r"""Includes various configuration options for a workflow invocation. If
    both ``included_targets`` and ``included_tags`` are unset, all
    actions will be included.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        included_targets (MutableSequence[google.cloud.dataform_v1.types.Target]):
            Optional. The set of action identifiers to
            include.
        included_tags (MutableSequence[str]):
            Optional. The set of tags to include.
        transitive_dependencies_included (bool):
            Optional. When set to true, transitive
            dependencies of included actions will be
            executed.
        transitive_dependents_included (bool):
            Optional. When set to true, transitive
            dependents of included actions will be executed.
        fully_refresh_incremental_tables_enabled (bool):
            Optional. When set to true, any incremental
            tables will be fully refreshed.
        service_account (str):
            Optional. The service account to run workflow
            invocations under.
        end_user_auth_config (google.cloud.dataform_v1.types.InvocationConfig.EndUserAuthenticationConfig):
            Optional. Configuration for end user authentication. Note
            that this should not be set when ``service_account`` is
            used.
        query_priority (google.cloud.dataform_v1.types.InvocationConfig.QueryPriority):
            Optional. Specifies the priority for query
            execution in BigQuery. More information can be
            found at
            https://cloud.google.com/bigquery/docs/running-queries#queries.

            This field is a member of `oneof`_ ``_query_priority``.
    """

    class QueryPriority(proto.Enum):
        r"""Types of priority for query execution in BigQuery.

        Values:
            QUERY_PRIORITY_UNSPECIFIED (0):
                Default value. This value is unused.
            INTERACTIVE (1):
                Query will be executed in BigQuery with
                interactive priority. More information can be
                found at
                https://cloud.google.com/bigquery/docs/running-queries#queries.
            BATCH (2):
                Query will be executed in BigQuery with batch
                priority. More information can be found at
                https://cloud.google.com/bigquery/docs/running-queries#batchqueries.
        """

        QUERY_PRIORITY_UNSPECIFIED = 0
        INTERACTIVE = 1
        BATCH = 2

    class EndUserAuthenticationConfig(proto.Message):
        r"""Includes configuration options for end user authentication.

        Attributes:
            user_email (str):
                Output only. Email address of the user to run
                workflow invocations under.
            oauth_config (google.cloud.dataform_v1.types.OAuthConfig):
                Optional. OAuth configuration for end user
                authentication.
        """

        user_email: str = proto.Field(
            proto.STRING,
            number=2,
        )
        oauth_config: "OAuthConfig" = proto.Field(
            proto.MESSAGE,
            number=4,
            message="OAuthConfig",
        )

    included_targets: MutableSequence["Target"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Target",
    )
    included_tags: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )
    transitive_dependencies_included: bool = proto.Field(
        proto.BOOL,
        number=3,
    )
    transitive_dependents_included: bool = proto.Field(
        proto.BOOL,
        number=4,
    )
    fully_refresh_incremental_tables_enabled: bool = proto.Field(
        proto.BOOL,
        number=5,
    )
    service_account: str = proto.Field(
        proto.STRING,
        number=6,
    )
    end_user_auth_config: EndUserAuthenticationConfig = proto.Field(
        proto.MESSAGE,
        number=7,
        message=EndUserAuthenticationConfig,
    )
    query_priority: QueryPriority = proto.Field(
        proto.ENUM,
        number=9,
        optional=True,
        enum=QueryPriority,
    )


class ListWorkflowConfigsRequest(proto.Message):
    r"""``ListWorkflowConfigs`` request message.

    Attributes:
        parent (str):
            Required. The repository in which to list workflow configs.
            Must be in the format
            ``projects/*/locations/*/repositories/*``.
        page_size (int):
            Optional. Maximum number of workflow configs
            to return. The server may return fewer items
            than requested. If unspecified, the server will
            pick an appropriate default.
        page_token (str):
            Optional. Page token received from a previous
            ``ListWorkflowConfigs`` call. Provide this to retrieve the
            subsequent page.

            When paginating, all other parameters provided to
            ``ListWorkflowConfigs``, with the exception of
            ``page_size``, must match the call that provided the page
            token.
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


class ListWorkflowConfigsResponse(proto.Message):
    r"""``ListWorkflowConfigs`` response message.

    Attributes:
        workflow_configs (MutableSequence[google.cloud.dataform_v1.types.WorkflowConfig]):
            List of workflow configs.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
        unreachable (MutableSequence[str]):
            Locations which could not be reached.
    """

    @property
    def raw_page(self):
        return self

    workflow_configs: MutableSequence["WorkflowConfig"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="WorkflowConfig",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetWorkflowConfigRequest(proto.Message):
    r"""``GetWorkflowConfig`` request message.

    Attributes:
        name (str):
            Required. The workflow config's name.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateWorkflowConfigRequest(proto.Message):
    r"""``CreateWorkflowConfig`` request message.

    Attributes:
        parent (str):
            Required. The repository in which to create the workflow
            config. Must be in the format
            ``projects/*/locations/*/repositories/*``.
        workflow_config (google.cloud.dataform_v1.types.WorkflowConfig):
            Required. The workflow config to create.
        workflow_config_id (str):
            Required. The ID to use for the workflow
            config, which will become the final component of
            the workflow config's resource name.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    workflow_config: "WorkflowConfig" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="WorkflowConfig",
    )
    workflow_config_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class UpdateWorkflowConfigRequest(proto.Message):
    r"""``UpdateWorkflowConfig`` request message.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. Specifies the fields to be updated
            in the workflow config. If left unset, all
            fields will be updated.
        workflow_config (google.cloud.dataform_v1.types.WorkflowConfig):
            Required. The workflow config to update.
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    workflow_config: "WorkflowConfig" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="WorkflowConfig",
    )


class DeleteWorkflowConfigRequest(proto.Message):
    r"""``DeleteWorkflowConfig`` request message.

    Attributes:
        name (str):
            Required. The workflow config's name.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class WorkflowInvocation(proto.Message):
    r"""Represents a single invocation of a compilation result.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        compilation_result (str):
            Immutable. The name of the compilation result to use for
            this invocation. Must be in the format
            ``projects/*/locations/*/repositories/*/compilationResults/*``.

            This field is a member of `oneof`_ ``compilation_source``.
        workflow_config (str):
            Immutable. The name of the workflow config to invoke. Must
            be in the format
            ``projects/*/locations/*/repositories/*/workflowConfigs/*``.

            This field is a member of `oneof`_ ``compilation_source``.
        name (str):
            Output only. The workflow invocation's name.
        invocation_config (google.cloud.dataform_v1.types.InvocationConfig):
            Immutable. If left unset, a default
            InvocationConfig will be used.
        state (google.cloud.dataform_v1.types.WorkflowInvocation.State):
            Output only. This workflow invocation's
            current state.
        invocation_timing (google.type.interval_pb2.Interval):
            Output only. This workflow invocation's
            timing details.
        resolved_compilation_result (str):
            Output only. The resolved compilation result that was used
            to create this invocation. Will be in the format
            ``projects/*/locations/*/repositories/*/compilationResults/*``.
        data_encryption_state (google.cloud.dataform_v1.types.DataEncryptionState):
            Output only. Only set if the repository has a
            KMS Key.
        internal_metadata (str):
            Output only. All the metadata information
            that is used internally to serve the resource.
            For example: timestamps, flags, status fields,
            etc. The format of this field is a JSON string.

            This field is a member of `oneof`_ ``_internal_metadata``.
        private_resource_metadata (google.cloud.dataform_v1.types.PrivateResourceMetadata):
            Output only. Metadata indicating whether this resource is
            user-scoped. ``WorkflowInvocation`` resource is
            ``user_scoped`` only if it is sourced from a compilation
            result and the compilation result is user-scoped.
        pipeline_config (google.cloud.dataform_v1.types.PipelineConfig):
            Output only. The pipeline options which
            defines the pipeline type and path within the
            Git repository.
    """

    class State(proto.Enum):
        r"""Represents the current state of a workflow invocation.

        Values:
            STATE_UNSPECIFIED (0):
                Default value. This value is unused.
            RUNNING (1):
                The workflow invocation is currently running.
            SUCCEEDED (2):
                The workflow invocation succeeded. A terminal
                state.
            CANCELLED (3):
                The workflow invocation was cancelled. A
                terminal state.
            FAILED (4):
                The workflow invocation failed. A terminal
                state.
            CANCELING (5):
                The workflow invocation is being cancelled,
                but some actions are still running.
        """

        STATE_UNSPECIFIED = 0
        RUNNING = 1
        SUCCEEDED = 2
        CANCELLED = 3
        FAILED = 4
        CANCELING = 5

    compilation_result: str = proto.Field(
        proto.STRING,
        number=2,
        oneof="compilation_source",
    )
    workflow_config: str = proto.Field(
        proto.STRING,
        number=6,
        oneof="compilation_source",
    )
    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    invocation_config: "InvocationConfig" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="InvocationConfig",
    )
    state: State = proto.Field(
        proto.ENUM,
        number=4,
        enum=State,
    )
    invocation_timing: interval_pb2.Interval = proto.Field(
        proto.MESSAGE,
        number=5,
        message=interval_pb2.Interval,
    )
    resolved_compilation_result: str = proto.Field(
        proto.STRING,
        number=7,
    )
    data_encryption_state: "DataEncryptionState" = proto.Field(
        proto.MESSAGE,
        number=8,
        message="DataEncryptionState",
    )
    internal_metadata: str = proto.Field(
        proto.STRING,
        number=9,
        optional=True,
    )
    private_resource_metadata: "PrivateResourceMetadata" = proto.Field(
        proto.MESSAGE,
        number=10,
        message="PrivateResourceMetadata",
    )
    pipeline_config: "PipelineConfig" = proto.Field(
        proto.MESSAGE,
        number=11,
        message="PipelineConfig",
    )


class ListWorkflowInvocationsRequest(proto.Message):
    r"""``ListWorkflowInvocations`` request message.

    Attributes:
        parent (str):
            Required. The parent resource of the WorkflowInvocation
            type. Must be in the format
            ``projects/*/locations/*/repositories/*``.
        page_size (int):
            Optional. Maximum number of workflow
            invocations to return. The server may return
            fewer items than requested. If unspecified, the
            server will pick an appropriate default.
        page_token (str):
            Optional. Page token received from a previous
            ``ListWorkflowInvocations`` call. Provide this to retrieve
            the subsequent page.

            When paginating, all other parameters provided to
            ``ListWorkflowInvocations``, with the exception of
            ``page_size``, must match the call that provided the page
            token.
        order_by (str):
            Optional. This field only supports ordering by ``name``. If
            unspecified, the server will choose the ordering. If
            specified, the default order is ascending for the ``name``
            field.
        filter (str):
            Optional. Filter for the returned list.
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
    filter: str = proto.Field(
        proto.STRING,
        number=5,
    )


class ListWorkflowInvocationsResponse(proto.Message):
    r"""``ListWorkflowInvocations`` response message.

    Attributes:
        workflow_invocations (MutableSequence[google.cloud.dataform_v1.types.WorkflowInvocation]):
            List of workflow invocations.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
        unreachable (MutableSequence[str]):
            Locations which could not be reached.
    """

    @property
    def raw_page(self):
        return self

    workflow_invocations: MutableSequence["WorkflowInvocation"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="WorkflowInvocation",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetWorkflowInvocationRequest(proto.Message):
    r"""``GetWorkflowInvocation`` request message.

    Attributes:
        name (str):
            Required. The workflow invocation resource's
            name.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateWorkflowInvocationRequest(proto.Message):
    r"""``CreateWorkflowInvocation`` request message.

    Attributes:
        parent (str):
            Required. The repository in which to create the workflow
            invocation. Must be in the format
            ``projects/*/locations/*/repositories/*``.
        workflow_invocation (google.cloud.dataform_v1.types.WorkflowInvocation):
            Required. The workflow invocation resource to
            create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    workflow_invocation: "WorkflowInvocation" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="WorkflowInvocation",
    )


class DeleteWorkflowInvocationRequest(proto.Message):
    r"""``DeleteWorkflowInvocation`` request message.

    Attributes:
        name (str):
            Required. The workflow invocation resource's
            name.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CancelWorkflowInvocationRequest(proto.Message):
    r"""``CancelWorkflowInvocation`` request message.

    Attributes:
        name (str):
            Required. The workflow invocation resource's
            name.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CancelWorkflowInvocationResponse(proto.Message):
    r"""``CancelWorkflowInvocation`` response message."""


class WorkflowInvocationAction(proto.Message):
    r"""Represents a single action in a workflow invocation.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        bigquery_action (google.cloud.dataform_v1.types.WorkflowInvocationAction.BigQueryAction):
            Output only. The workflow action's bigquery
            action details.

            This field is a member of `oneof`_ ``action``.
        notebook_action (google.cloud.dataform_v1.types.WorkflowInvocationAction.NotebookAction):
            Output only. The workflow action's notebook
            action details.

            This field is a member of `oneof`_ ``action``.
        data_preparation_action (google.cloud.dataform_v1.types.WorkflowInvocationAction.DataPreparationAction):
            Output only. The workflow action's data
            preparation action details.

            This field is a member of `oneof`_ ``action``.
        target (google.cloud.dataform_v1.types.Target):
            Output only. This action's identifier. Unique
            within the workflow invocation.
        canonical_target (google.cloud.dataform_v1.types.Target):
            Output only. The action's identifier if the
            project had been compiled without any overrides
            configured. Unique within the compilation
            result.
        state (google.cloud.dataform_v1.types.WorkflowInvocationAction.State):
            Output only. This action's current state.
        failure_reason (str):
            Output only. If and only if action's state is
            FAILED a failure reason is set.
        invocation_timing (google.type.interval_pb2.Interval):
            Output only. This action's timing details. ``start_time``
            will be set if the action is in [RUNNING, SUCCEEDED,
            CANCELLED, FAILED] state. ``end_time`` will be set if the
            action is in [SUCCEEDED, CANCELLED, FAILED] state.
        internal_metadata (str):
            Output only. All the metadata information
            that is used internally to serve the resource.
            For example: timestamps, flags, status fields,
            etc. The format of this field is a JSON string.

            This field is a member of `oneof`_ ``_internal_metadata``.
    """

    class State(proto.Enum):
        r"""Represents the current state of a workflow invocation action.

        Values:
            PENDING (0):
                The action has not yet been considered for
                invocation.
            RUNNING (1):
                The action is currently running.
            SKIPPED (2):
                Execution of the action was skipped because
                upstream dependencies did not all complete
                successfully. A terminal state.
            DISABLED (3):
                Execution of the action was disabled as per
                the configuration of the corresponding
                compilation result action. A terminal state.
            SUCCEEDED (4):
                The action succeeded. A terminal state.
            CANCELLED (5):
                The action was cancelled. A terminal state.
            FAILED (6):
                The action failed. A terminal state.
        """

        PENDING = 0
        RUNNING = 1
        SKIPPED = 2
        DISABLED = 3
        SUCCEEDED = 4
        CANCELLED = 5
        FAILED = 6

    class BigQueryAction(proto.Message):
        r"""Represents a workflow action that will run against BigQuery.

        Attributes:
            sql_script (str):
                Output only. The generated BigQuery SQL
                script that will be executed.
            job_id (str):
                Output only. The ID of the BigQuery job that executed the
                SQL in sql_script. Only set once the job has started to run.
        """

        sql_script: str = proto.Field(
            proto.STRING,
            number=1,
        )
        job_id: str = proto.Field(
            proto.STRING,
            number=2,
        )

    class NotebookAction(proto.Message):
        r"""Represents a workflow action that will run against a Notebook
        runtime.

        Attributes:
            contents (str):
                Output only. The code contents of a Notebook
                to be run.
            job_id (str):
                Output only. The ID of the Gemini Enterprise
                Agent Platform job that executed the notebook in
                contents and also the ID used for the outputs
                created in Google Cloud Storage buckets. Only
                set once the job has started to run.
            file_path (str):
                Output only. The path to the notebook file in
                the repository.
        """

        contents: str = proto.Field(
            proto.STRING,
            number=1,
        )
        job_id: str = proto.Field(
            proto.STRING,
            number=2,
        )
        file_path: str = proto.Field(
            proto.STRING,
            number=3,
        )

    class DataPreparationAction(proto.Message):
        r"""Represents a workflow action that will run a Data
        Preparation.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            contents_yaml (str):
                Output only. YAML representing the contents
                of the data preparation. Can be used to show the
                customer what the input was to their workflow.

                This field is a member of `oneof`_ ``definition``.
            contents_sql (google.cloud.dataform_v1.types.WorkflowInvocationAction.DataPreparationAction.ActionSqlDefinition):
                SQL definition for a Data Preparation.
                Contains a SQL query and additional context
                information.

                This field is a member of `oneof`_ ``definition``.
            generated_sql (str):
                Output only. The generated BigQuery SQL
                script that will be executed. For reference
                only.
            job_id (str):
                Output only. The ID of the BigQuery job that executed the
                SQL in sql_script. Only set once the job has started to run.
        """

        class ActionSqlDefinition(proto.Message):
            r"""Definition of a SQL Data Preparation

            Attributes:
                query (str):
                    The SQL query representing the data
                    preparation steps. Formatted as a Pipe SQL query
                    statement.
                error_table (google.cloud.dataform_v1.types.WorkflowInvocationAction.DataPreparationAction.ActionErrorTable):
                    Error table configuration,
                load_config (google.cloud.dataform_v1.types.WorkflowInvocationAction.DataPreparationAction.ActionLoadConfig):
                    Load configuration.
            """

            query: str = proto.Field(
                proto.STRING,
                number=1,
            )
            error_table: "WorkflowInvocationAction.DataPreparationAction.ActionErrorTable" = proto.Field(
                proto.MESSAGE,
                number=2,
                message="WorkflowInvocationAction.DataPreparationAction.ActionErrorTable",
            )
            load_config: "WorkflowInvocationAction.DataPreparationAction.ActionLoadConfig" = proto.Field(
                proto.MESSAGE,
                number=3,
                message="WorkflowInvocationAction.DataPreparationAction.ActionLoadConfig",
            )

        class ActionErrorTable(proto.Message):
            r"""Error table information, used to write error data into a
            BigQuery table.

            Attributes:
                target (google.cloud.dataform_v1.types.Target):
                    Error Table target.
                retention_days (int):
                    Error table partition expiration in days.
                    Only positive values are allowed.
            """

            target: "Target" = proto.Field(
                proto.MESSAGE,
                number=1,
                message="Target",
            )
            retention_days: int = proto.Field(
                proto.INT32,
                number=2,
            )

        class ActionLoadConfig(proto.Message):
            r"""Simplified load configuration for actions

            This message has `oneof`_ fields (mutually exclusive fields).
            For each oneof, at most one member field can be set at the same time.
            Setting any member of the oneof automatically clears all other
            members.

            .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

            Attributes:
                replace (google.cloud.dataform_v1.types.WorkflowInvocationAction.DataPreparationAction.ActionSimpleLoadMode):
                    Replace destination table

                    This field is a member of `oneof`_ ``mode``.
                append (google.cloud.dataform_v1.types.WorkflowInvocationAction.DataPreparationAction.ActionSimpleLoadMode):
                    Append into destination table

                    This field is a member of `oneof`_ ``mode``.
                maximum (google.cloud.dataform_v1.types.WorkflowInvocationAction.DataPreparationAction.ActionIncrementalLoadMode):
                    Insert records where the value exceeds the
                    previous maximum value for a column in the
                    destination table

                    This field is a member of `oneof`_ ``mode``.
                unique (google.cloud.dataform_v1.types.WorkflowInvocationAction.DataPreparationAction.ActionIncrementalLoadMode):
                    Insert records where the value of a column is
                    not already present in the destination table

                    This field is a member of `oneof`_ ``mode``.
            """

            replace: "WorkflowInvocationAction.DataPreparationAction.ActionSimpleLoadMode" = proto.Field(
                proto.MESSAGE,
                number=1,
                oneof="mode",
                message="WorkflowInvocationAction.DataPreparationAction.ActionSimpleLoadMode",
            )
            append: "WorkflowInvocationAction.DataPreparationAction.ActionSimpleLoadMode" = proto.Field(
                proto.MESSAGE,
                number=2,
                oneof="mode",
                message="WorkflowInvocationAction.DataPreparationAction.ActionSimpleLoadMode",
            )
            maximum: "WorkflowInvocationAction.DataPreparationAction.ActionIncrementalLoadMode" = proto.Field(
                proto.MESSAGE,
                number=3,
                oneof="mode",
                message="WorkflowInvocationAction.DataPreparationAction.ActionIncrementalLoadMode",
            )
            unique: "WorkflowInvocationAction.DataPreparationAction.ActionIncrementalLoadMode" = proto.Field(
                proto.MESSAGE,
                number=4,
                oneof="mode",
                message="WorkflowInvocationAction.DataPreparationAction.ActionIncrementalLoadMode",
            )

        class ActionSimpleLoadMode(proto.Message):
            r"""Simple load definition"""

        class ActionIncrementalLoadMode(proto.Message):
            r"""Load definition for incremental load modes

            Attributes:
                column (str):
                    Column name for incremental load modes
            """

            column: str = proto.Field(
                proto.STRING,
                number=1,
            )

        contents_yaml: str = proto.Field(
            proto.STRING,
            number=2,
            oneof="definition",
        )
        contents_sql: "WorkflowInvocationAction.DataPreparationAction.ActionSqlDefinition" = proto.Field(
            proto.MESSAGE,
            number=6,
            oneof="definition",
            message="WorkflowInvocationAction.DataPreparationAction.ActionSqlDefinition",
        )
        generated_sql: str = proto.Field(
            proto.STRING,
            number=3,
        )
        job_id: str = proto.Field(
            proto.STRING,
            number=4,
        )

    bigquery_action: BigQueryAction = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="action",
        message=BigQueryAction,
    )
    notebook_action: NotebookAction = proto.Field(
        proto.MESSAGE,
        number=8,
        oneof="action",
        message=NotebookAction,
    )
    data_preparation_action: DataPreparationAction = proto.Field(
        proto.MESSAGE,
        number=9,
        oneof="action",
        message=DataPreparationAction,
    )
    target: "Target" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Target",
    )
    canonical_target: "Target" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Target",
    )
    state: State = proto.Field(
        proto.ENUM,
        number=4,
        enum=State,
    )
    failure_reason: str = proto.Field(
        proto.STRING,
        number=7,
    )
    invocation_timing: interval_pb2.Interval = proto.Field(
        proto.MESSAGE,
        number=5,
        message=interval_pb2.Interval,
    )
    internal_metadata: str = proto.Field(
        proto.STRING,
        number=10,
        optional=True,
    )


class QueryWorkflowInvocationActionsRequest(proto.Message):
    r"""``QueryWorkflowInvocationActions`` request message.

    Attributes:
        name (str):
            Required. The workflow invocation's name.
        page_size (int):
            Optional. Maximum number of workflow
            invocations to return. The server may return
            fewer items than requested. If unspecified, the
            server will pick an appropriate default.
        page_token (str):
            Optional. Page token received from a previous
            ``QueryWorkflowInvocationActions`` call. Provide this to
            retrieve the subsequent page.

            When paginating, all other parameters provided to
            ``QueryWorkflowInvocationActions``, with the exception of
            ``page_size``, must match the call that provided the page
            token.
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


class QueryWorkflowInvocationActionsResponse(proto.Message):
    r"""``QueryWorkflowInvocationActions`` response message.

    Attributes:
        workflow_invocation_actions (MutableSequence[google.cloud.dataform_v1.types.WorkflowInvocationAction]):
            List of workflow invocation actions.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    workflow_invocation_actions: MutableSequence["WorkflowInvocationAction"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="WorkflowInvocationAction",
        )
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class Config(proto.Message):
    r"""Config for all repositories in a given project and location.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Identifier. The config name.
        default_kms_key_name (str):
            Optional. The default KMS key that is used if
            no encryption key is provided when a repository
            is created.
        internal_metadata (str):
            Output only. All the metadata information
            that is used internally to serve the resource.
            For example: timestamps, flags, status fields,
            etc. The format of this field is a JSON string.

            This field is a member of `oneof`_ ``_internal_metadata``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    default_kms_key_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    internal_metadata: str = proto.Field(
        proto.STRING,
        number=7,
        optional=True,
    )


class GetConfigRequest(proto.Message):
    r"""``GetConfig`` request message.

    Attributes:
        name (str):
            Required. The config name.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateConfigRequest(proto.Message):
    r"""``UpdateConfig`` request message.

    Attributes:
        config (google.cloud.dataform_v1.types.Config):
            Required. The config to update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. Specifies the fields to be updated
            in the config.
    """

    config: "Config" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Config",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class Folder(proto.Message):
    r"""Represents a Dataform Folder. This is a resource that is used
    to organize Files and other Folders and provide hierarchical
    access controls.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Identifier. The Folder's name.
        display_name (str):
            Required. The Folder's user-friendly name.
        containing_folder (str):
            Optional. The containing Folder resource
            name. This should take the format:
            projects/{project}/locations/{location}/folders/{folder},
            projects/{project}/locations/{location}/teamFolders/{teamFolder},
            or just "" if this is a root Folder. This field
            can only be updated through MoveFolder.
        team_folder_name (str):
            Output only. The resource name of the
            TeamFolder that this Folder is associated with.
            This should take the format:

            projects/{project}/locations/{location}/teamFolders/{teamFolder}.
            If this is not set, the Folder is not associated
            with a TeamFolder and is a UserFolder.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp of when the Folder
            was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp of when the Folder
            was last updated.
        internal_metadata (str):
            Output only. All the metadata information
            that is used internally to serve the resource.
            For example: timestamps, flags, status fields,
            etc. The format of this field is a JSON string.

            This field is a member of `oneof`_ ``_internal_metadata``.
        creator_iam_principal (str):
            Output only. The IAM principal identifier of
            the creator of the Folder.

            This field is a member of `oneof`_ ``_creator_iam_principal``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    containing_folder: str = proto.Field(
        proto.STRING,
        number=3,
    )
    team_folder_name: str = proto.Field(
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
    internal_metadata: str = proto.Field(
        proto.STRING,
        number=7,
        optional=True,
    )
    creator_iam_principal: str = proto.Field(
        proto.STRING,
        number=8,
        optional=True,
    )


class CreateFolderRequest(proto.Message):
    r"""``CreateFolder`` request message.

    Attributes:
        parent (str):
            Required. The location in which to create the Folder. Must
            be in the format ``projects/*/locations/*``.
        folder (google.cloud.dataform_v1.types.Folder):
            Required. The Folder to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    folder: "Folder" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Folder",
    )


class MoveFolderRequest(proto.Message):
    r"""``MoveFolder`` request message.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Required. The full resource name of the
            Folder to move.
        destination_containing_folder (str):
            Optional. The name of the Folder, TeamFolder, or root
            location to move the Folder to. Can be in the format of: ""
            to move into the root User folder,
            ``projects/*/locations/*/folders/*``,
            ``projects/*/locations/*/teamFolders/*``

            This field is a member of `oneof`_ ``_destination_containing_folder``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    destination_containing_folder: str = proto.Field(
        proto.STRING,
        number=2,
        optional=True,
    )


class GetFolderRequest(proto.Message):
    r"""``GetFolder`` request message.

    Attributes:
        name (str):
            Required. The Folder's name.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateFolderRequest(proto.Message):
    r"""``UpdateFolder`` request message.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. Specifies the fields to be updated in the Folder.
            If left unset, all fields that can be updated, will be
            updated. A few fields cannot be updated and will be ignored
            if specified in the update_mask (e.g. parent_name,
            team_folder_name).
        folder (google.cloud.dataform_v1.types.Folder):
            Required. The updated Folder.
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    folder: "Folder" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Folder",
    )


class DeleteFolderRequest(proto.Message):
    r"""``DeleteFolder`` request message.

    Attributes:
        name (str):
            Required. The Folder's name.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class DeleteFolderTreeRequest(proto.Message):
    r"""``DeleteFolderTree`` request message.

    Attributes:
        name (str):
            Required. The Folder's name.
            Format:
            projects/{project}/locations/{location}/folders/{folder}
        force (bool):
            Optional. If ``false`` (default): The operation will fail if
            any Repository within the folder hierarchy has associated
            Release Configs or Workflow Configs.

            If ``true``: The operation will attempt to delete
            everything, including any Release Configs and Workflow
            Configs linked to Repositories within the folder hierarchy.
            This permanently removes schedules and resources.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    force: bool = proto.Field(
        proto.BOOL,
        number=2,
    )


class DeleteTeamFolderTreeRequest(proto.Message):
    r"""``DeleteTeamFolderTree`` request message.

    Attributes:
        name (str):
            Required. The TeamFolder's name. Format:
            projects/{project}/locations/{location}/teamFolders/{team_folder}
        force (bool):
            Optional. If ``false`` (default): The operation will fail if
            any Repository within the folder hierarchy has associated
            Release Configs or Workflow Configs.

            If ``true``: The operation will attempt to delete
            everything, including any Release Configs and Workflow
            Configs linked to Repositories within the folder hierarchy.
            This permanently removes schedules and resources.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    force: bool = proto.Field(
        proto.BOOL,
        number=2,
    )


class DeleteFolderTreeMetadata(proto.Message):
    r"""Contains metadata about the progress of the DeleteFolderTree
    Long-running operations.

    Attributes:
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the operation was
            created.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the operation finished
            running.
        target (str):
            Output only. Resource name of the target of the operation.
            Format:
            projects/{project}/locations/{location}/folders/{folder} or
            projects/{project}/locations/{location}/teamFolders/{team_folder}
        state (google.cloud.dataform_v1.types.DeleteFolderTreeMetadata.State):
            Output only. The state of the operation.
        percent_complete (int):
            Output only. Percent complete of the operation [0, 100].
    """

    class State(proto.Enum):
        r"""Different states of the DeleteFolderTree operation.

        Values:
            STATE_UNSPECIFIED (0):
                The state is unspecified.
            INITIALIZED (1):
                The operation was initialized and recorded by
                the server, but not yet started.
            IN_PROGRESS (2):
                The operation is in progress.
            SUCCEEDED (3):
                The operation has completed successfully.
            FAILED (4):
                The operation has failed.
        """

        STATE_UNSPECIFIED = 0
        INITIALIZED = 1
        IN_PROGRESS = 2
        SUCCEEDED = 3
        FAILED = 4

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
    state: State = proto.Field(
        proto.ENUM,
        number=4,
        enum=State,
    )
    percent_complete: int = proto.Field(
        proto.INT32,
        number=5,
    )


class QueryFolderContentsRequest(proto.Message):
    r"""``QueryFolderContents`` request message.

    Attributes:
        folder (str):
            Required. Resource name of the Folder to list contents for.
            Format: projects/*/locations/*/folders/\*
        page_size (int):
            Optional. Maximum number of paths to return.
            The server may return fewer items than
            requested. If unspecified, the server will pick
            an appropriate default.
        page_token (str):
            Optional. Page token received from a previous
            ``QueryFolderContents`` call. Provide this to retrieve the
            subsequent page.

            When paginating, all other parameters provided to
            ``QueryFolderContents``, with the exception of
            ``page_size``, must match the call that provided the page
            token.
        order_by (str):
            Optional. Field to additionally sort results by. Will order
            Folders before Repositories, and then by ``order_by`` in
            ascending order. Supported keywords: display_name (default),
            create_time, last_modified_time. Examples:

            - ``orderBy="display_name"``
            - ``orderBy="display_name desc"``
        filter (str):
            Optional. Optional filtering for the returned list.
            Filtering is currently only supported on the
            ``display_name`` field.

            Example:

            - ``filter="display_name="MyFolder""``
    """

    folder: str = proto.Field(
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
    filter: str = proto.Field(
        proto.STRING,
        number=5,
    )


class QueryFolderContentsResponse(proto.Message):
    r"""``QueryFolderContents`` response message.

    Attributes:
        entries (MutableSequence[google.cloud.dataform_v1.types.QueryFolderContentsResponse.FolderContentsEntry]):
            List of entries in the folder.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    class FolderContentsEntry(proto.Message):
        r"""Represents a single content entry.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            folder (google.cloud.dataform_v1.types.Folder):
                A subfolder.

                This field is a member of `oneof`_ ``entry``.
            repository (google.cloud.dataform_v1.types.Repository):
                A repository.

                This field is a member of `oneof`_ ``entry``.
        """

        folder: "Folder" = proto.Field(
            proto.MESSAGE,
            number=1,
            oneof="entry",
            message="Folder",
        )
        repository: "Repository" = proto.Field(
            proto.MESSAGE,
            number=2,
            oneof="entry",
            message="Repository",
        )

    @property
    def raw_page(self):
        return self

    entries: MutableSequence[FolderContentsEntry] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=FolderContentsEntry,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class QueryUserRootContentsRequest(proto.Message):
    r"""``QueryUserRootContents`` request message.

    Attributes:
        location (str):
            Required. Location of the user root folder to list contents
            for. Format: projects/*/locations/*
        page_size (int):
            Optional. Maximum number of paths to return.
            The server may return fewer items than
            requested. If unspecified, the server will pick
            an appropriate default.
        page_token (str):
            Optional. Page token received from a previous
            ``QueryUserRootContents`` call. Provide this to retrieve the
            subsequent page.

            When paginating, all other parameters provided to
            ``QueryUserRootFolderContents``, with the exception of
            ``page_size``, must match the call that provided the page
            token.
        order_by (str):
            Optional. Field to additionally sort results by. Will order
            Folders before Repositories, and then by ``order_by`` in
            ascending order. Supported keywords: display_name (default),
            created_at, last_modified_at. Examples:

            - ``orderBy="display_name"``
            - ``orderBy="display_name desc"``
        filter (str):
            Optional. Optional filtering for the returned list.
            Filtering is currently only supported on the
            ``display_name`` field.

            Example:

            - ``filter="display_name="MyFolder""``
    """

    location: str = proto.Field(
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
    filter: str = proto.Field(
        proto.STRING,
        number=5,
    )


class QueryUserRootContentsResponse(proto.Message):
    r"""``QueryUserRootContents`` response message.

    Attributes:
        entries (MutableSequence[google.cloud.dataform_v1.types.QueryUserRootContentsResponse.RootContentsEntry]):
            List of entries in the folder.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    class RootContentsEntry(proto.Message):
        r"""Represents a single content entry.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            folder (google.cloud.dataform_v1.types.Folder):
                A subfolder.

                This field is a member of `oneof`_ ``entry``.
            repository (google.cloud.dataform_v1.types.Repository):
                A repository.

                This field is a member of `oneof`_ ``entry``.
        """

        folder: "Folder" = proto.Field(
            proto.MESSAGE,
            number=1,
            oneof="entry",
            message="Folder",
        )
        repository: "Repository" = proto.Field(
            proto.MESSAGE,
            number=2,
            oneof="entry",
            message="Repository",
        )

    @property
    def raw_page(self):
        return self

    entries: MutableSequence[RootContentsEntry] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=RootContentsEntry,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class TeamFolder(proto.Message):
    r"""Represents a Dataform TeamFolder. This is a resource that
    sits at the project level and is used to organize Repositories
    and Folders with hierarchical access controls. They provide a
    team context and stricter access controls.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Identifier. The TeamFolder's name.
        display_name (str):
            Required. The TeamFolder's user-friendly
            name.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp of when the
            TeamFolder was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp of when the
            TeamFolder was last updated.
        internal_metadata (str):
            Output only. All the metadata information
            that is used internally to serve the resource.
            For example: timestamps, flags, status fields,
            etc. The format of this field is a JSON string.

            This field is a member of `oneof`_ ``_internal_metadata``.
        creator_iam_principal (str):
            Output only. The IAM principal identifier of
            the creator of the TeamFolder.

            This field is a member of `oneof`_ ``_creator_iam_principal``.
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
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    internal_metadata: str = proto.Field(
        proto.STRING,
        number=5,
        optional=True,
    )
    creator_iam_principal: str = proto.Field(
        proto.STRING,
        number=6,
        optional=True,
    )


class CreateTeamFolderRequest(proto.Message):
    r"""``CreateTeamFolder`` request message.

    Attributes:
        parent (str):
            Required. The location in which to create the TeamFolder.
            Must be in the format ``projects/*/locations/*``.
        team_folder (google.cloud.dataform_v1.types.TeamFolder):
            Required. The TeamFolder to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    team_folder: "TeamFolder" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="TeamFolder",
    )


class GetTeamFolderRequest(proto.Message):
    r"""``GetTeamFolder`` request message.

    Attributes:
        name (str):
            Required. The TeamFolder's name.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateTeamFolderRequest(proto.Message):
    r"""``UpdateTeamFolder`` request message.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. Specifies the fields to be updated
            in the Folder. If left unset, all fields will be
            updated.
        team_folder (google.cloud.dataform_v1.types.TeamFolder):
            Required. The updated TeamFolder.
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    team_folder: "TeamFolder" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="TeamFolder",
    )


class DeleteTeamFolderRequest(proto.Message):
    r"""``DeleteTeamFolder`` request message.

    Attributes:
        name (str):
            Required. The TeamFolder's name.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class QueryTeamFolderContentsRequest(proto.Message):
    r"""``QueryTeamFolderContents`` request message.

    Attributes:
        team_folder (str):
            Required. Resource name of the TeamFolder to list contents
            for. Format: ``projects/*/locations/*/teamFolders/*``.
        page_size (int):
            Optional. Maximum number of paths to return.
            The server may return fewer items than
            requested. If unspecified, the server will pick
            an appropriate default.
        page_token (str):
            Optional. Page token received from a previous
            ``QueryTeamFolderContents`` call. Provide this to retrieve
            the subsequent page.

            When paginating, all other parameters provided to
            ``QueryTeamFolderContents``, with the exception of
            ``page_size``, must match the call that provided the page
            token.
        order_by (str):
            Optional. Field to additionally sort results by. Will order
            Folders before Repositories, and then by ``order_by`` in
            ascending order. Supported keywords: ``display_name``
            (default), ``create_time``, last_modified_time. Examples:

            - ``orderBy="display_name"``
            - ``orderBy="display_name desc"``
        filter (str):
            Optional. Optional filtering for the returned list.
            Filtering is currently only supported on the
            ``display_name`` field.

            Example:

            - ``filter="display_name="MyFolder""``
    """

    team_folder: str = proto.Field(
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
    filter: str = proto.Field(
        proto.STRING,
        number=5,
    )


class QueryTeamFolderContentsResponse(proto.Message):
    r"""``QueryTeamFolderContents`` response message.

    Attributes:
        entries (MutableSequence[google.cloud.dataform_v1.types.QueryTeamFolderContentsResponse.TeamFolderContentsEntry]):
            List of entries in the TeamFolder.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    class TeamFolderContentsEntry(proto.Message):
        r"""Represents a single content entry.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            folder (google.cloud.dataform_v1.types.Folder):
                A subfolder.

                This field is a member of `oneof`_ ``entry``.
            repository (google.cloud.dataform_v1.types.Repository):
                A repository.

                This field is a member of `oneof`_ ``entry``.
        """

        folder: "Folder" = proto.Field(
            proto.MESSAGE,
            number=1,
            oneof="entry",
            message="Folder",
        )
        repository: "Repository" = proto.Field(
            proto.MESSAGE,
            number=2,
            oneof="entry",
            message="Repository",
        )

    @property
    def raw_page(self):
        return self

    entries: MutableSequence[TeamFolderContentsEntry] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=TeamFolderContentsEntry,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class SearchTeamFoldersRequest(proto.Message):
    r"""``SearchTeamFolders`` request message.

    Attributes:
        location (str):
            Required. Location in which to query TeamFolders. Format:
            ``projects/*/locations/*``.
        page_size (int):
            Optional. Maximum number of ``TeamFolders`` to return. The
            server may return fewer items than requested. If
            unspecified, the server will pick a default of ``page_size``
            = 50.
        page_token (str):
            Optional. Page token received from a previous
            ``SearchTeamFolders`` call. Provide this to retrieve the
            subsequent page.

            When paginating, all other parameters provided to
            ``SearchTeamFolders``, with the exception of ``page_size``,
            must match the call that provided the page token.
        order_by (str):
            Optional. Field to additionally sort results by. Supported
            keywords: ``display_name`` (default), ``create_time``,
            ``last_modified_time``. Examples:

            - ``orderBy="display_name"``
            - ``orderBy="display_name desc"``
        filter (str):
            Optional. Optional filtering for the returned list.
            Filtering is currently only supported on the
            ``display_name`` field.

            Example:

            - ``filter="display_name="MyFolder""``
    """

    location: str = proto.Field(
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
    filter: str = proto.Field(
        proto.STRING,
        number=5,
    )


class SearchTeamFoldersResponse(proto.Message):
    r"""``SearchTeamFolders`` response message.

    Attributes:
        results (MutableSequence[google.cloud.dataform_v1.types.SearchTeamFoldersResponse.TeamFolderSearchResult]):
            List of TeamFolders that match the search
            query.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    class TeamFolderSearchResult(proto.Message):
        r"""Represents a single content entry.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            team_folder (google.cloud.dataform_v1.types.TeamFolder):
                A TeamFolder resource that is in the project
                / location.

                This field is a member of `oneof`_ ``entry``.
        """

        team_folder: "TeamFolder" = proto.Field(
            proto.MESSAGE,
            number=2,
            oneof="entry",
            message="TeamFolder",
        )

    @property
    def raw_page(self):
        return self

    results: MutableSequence[TeamFolderSearchResult] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=TeamFolderSearchResult,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class MoveFolderMetadata(proto.Message):
    r"""Contains metadata about the progress of the MoveFolder
    Long-running operations.

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
        state (google.cloud.dataform_v1.types.MoveFolderMetadata.State):
            The state of the move.
        percent_complete (int):
            Percent complete of the move [0, 100].
    """

    class State(proto.Enum):
        r"""Different states of the move.

        Values:
            STATE_UNSPECIFIED (0):
                The state is unspecified.
            INITIALIZED (1):
                The move was initialized and recorded by the
                server, but not yet started.
            IN_PROGRESS (2):
                The move is in progress.
            SUCCESS (3):
                The move has completed successfully.
            FAILED (4):
                The move has failed.
        """

        STATE_UNSPECIFIED = 0
        INITIALIZED = 1
        IN_PROGRESS = 2
        SUCCESS = 3
        FAILED = 4

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
    state: State = proto.Field(
        proto.ENUM,
        number=4,
        enum=State,
    )
    percent_complete: int = proto.Field(
        proto.INT32,
        number=5,
    )


class MoveRepositoryMetadata(proto.Message):
    r"""Contains metadata about the progress of the MoveRepository
    Long-running operations.

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
        state (google.cloud.dataform_v1.types.MoveRepositoryMetadata.State):
            The state of the move.
        percent_complete (int):
            Percent complete of the move [0, 100].
    """

    class State(proto.Enum):
        r"""Different states of the move.

        Values:
            STATE_UNSPECIFIED (0):
                The state is unspecified.
            INITIALIZED (1):
                The move was initialized and recorded by the
                server, but not yet started.
            IN_PROGRESS (2):
                The move is in progress.
            SUCCESS (3):
                The move has completed successfully.
            FAILED (4):
                The move has failed.
        """

        STATE_UNSPECIFIED = 0
        INITIALIZED = 1
        IN_PROGRESS = 2
        SUCCESS = 3
        FAILED = 4

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
    state: State = proto.Field(
        proto.ENUM,
        number=4,
        enum=State,
    )
    percent_complete: int = proto.Field(
        proto.INT32,
        number=5,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
