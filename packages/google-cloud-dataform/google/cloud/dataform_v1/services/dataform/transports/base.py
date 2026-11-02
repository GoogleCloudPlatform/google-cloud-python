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
import abc
from typing import Awaitable, Callable, Dict, Optional, Sequence, Union

import google.api_core
import google.auth  # type: ignore
import google.iam.v1.iam_policy_pb2 as iam_policy_pb2  # type: ignore
import google.iam.v1.policy_pb2 as policy_pb2  # type: ignore
import google.protobuf
import google.protobuf.empty_pb2 as empty_pb2  # type: ignore
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1, operations_v1
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.cloud.location import locations_pb2  # type: ignore
from google.iam.v1 import (
    iam_policy_pb2,  # type: ignore
    policy_pb2,  # type: ignore
)
from google.longrunning import operations_pb2  # type: ignore
from google.oauth2 import service_account  # type: ignore

from google.cloud.dataform_v1 import gapic_version as package_version
from google.cloud.dataform_v1.types import dataform

DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)
DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


class DataformTransport(abc.ABC):
    """Abstract transport class for Dataform."""

    AUTH_SCOPES = (
        "https://www.googleapis.com/auth/bigquery",
        "https://www.googleapis.com/auth/cloud-platform",
    )

    DEFAULT_HOST: str = "dataform.googleapis.com"

    def __init__(
        self,
        *,
        host: str = DEFAULT_HOST,
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        api_audience: Optional[str] = None,
        **kwargs,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'dataform.googleapis.com').
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            credentials_file (Optional[str]): Deprecated. A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is mutually exclusive with credentials. This argument will be
                removed in the next major version of this library.
            scopes (Optional[Sequence[str]]): A list of scopes.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.
            always_use_jwt_access (Optional[bool]): Whether self signed JWT should
                be used for service account credentials.
            api_audience (Optional[str]): The intended audience for the API calls
                to the service that will be set when using certain 3rd party
                authentication flows. Audience is typically a resource identifier.
                If not set, the host value will be used as a default.
        """

        # Save the scopes.
        self._scopes = scopes
        if not hasattr(self, "_ignore_credentials"):
            self._ignore_credentials: bool = False

        # If no credentials are provided, then determine the appropriate
        # defaults.
        if credentials and credentials_file:
            raise core_exceptions.DuplicateCredentialArgs(
                "'credentials_file' and 'credentials' are mutually exclusive"
            )

        if credentials_file is not None:
            credentials, _ = google.auth.load_credentials_from_file(
                credentials_file,
                scopes=scopes,
                quota_project_id=quota_project_id,
                default_scopes=self.AUTH_SCOPES,
            )
        elif credentials is None and not self._ignore_credentials:
            credentials, _ = google.auth.default(
                scopes=scopes,
                quota_project_id=quota_project_id,
                default_scopes=self.AUTH_SCOPES,
            )
            # Don't apply audience if the credentials file passed from user.
            if hasattr(credentials, "with_gdch_audience"):
                credentials = credentials.with_gdch_audience(
                    api_audience if api_audience else host
                )

        # If the credentials are service account credentials, then always try to use self signed JWT.
        if (
            always_use_jwt_access
            and isinstance(credentials, service_account.Credentials)
            and hasattr(service_account.Credentials, "with_always_use_jwt_access")
        ):
            credentials = credentials.with_always_use_jwt_access(True)

        # Save the credentials.
        self._credentials = credentials

        # Save the hostname. Default to port 443 (HTTPS) if none is specified.
        if ":" not in host:
            host += ":443"
        self._host = host

        self._wrapped_methods: Dict[Callable, Callable] = {}

    @property
    def host(self):
        return self._host

    def _prep_wrapped_messages(self, client_info):
        # Precompute the wrapped methods.
        self._wrapped_methods = {
            self.get_team_folder: gapic_v1.method.wrap_method(
                self.get_team_folder,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_team_folder: gapic_v1.method.wrap_method(
                self.create_team_folder,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_team_folder: gapic_v1.method.wrap_method(
                self.update_team_folder,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_team_folder: gapic_v1.method.wrap_method(
                self.delete_team_folder,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_team_folder_tree: gapic_v1.method.wrap_method(
                self.delete_team_folder_tree,
                default_timeout=None,
                client_info=client_info,
            ),
            self.query_team_folder_contents: gapic_v1.method.wrap_method(
                self.query_team_folder_contents,
                default_timeout=None,
                client_info=client_info,
            ),
            self.search_team_folders: gapic_v1.method.wrap_method(
                self.search_team_folders,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_folder: gapic_v1.method.wrap_method(
                self.get_folder,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_folder: gapic_v1.method.wrap_method(
                self.create_folder,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_folder: gapic_v1.method.wrap_method(
                self.update_folder,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_folder: gapic_v1.method.wrap_method(
                self.delete_folder,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_folder_tree: gapic_v1.method.wrap_method(
                self.delete_folder_tree,
                default_timeout=None,
                client_info=client_info,
            ),
            self.query_folder_contents: gapic_v1.method.wrap_method(
                self.query_folder_contents,
                default_timeout=None,
                client_info=client_info,
            ),
            self.query_user_root_contents: gapic_v1.method.wrap_method(
                self.query_user_root_contents,
                default_timeout=None,
                client_info=client_info,
            ),
            self.move_folder: gapic_v1.method.wrap_method(
                self.move_folder,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_repositories: gapic_v1.method.wrap_method(
                self.list_repositories,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_repository: gapic_v1.method.wrap_method(
                self.get_repository,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_repository: gapic_v1.method.wrap_method(
                self.create_repository,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_repository: gapic_v1.method.wrap_method(
                self.update_repository,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_repository: gapic_v1.method.wrap_method(
                self.delete_repository,
                default_timeout=None,
                client_info=client_info,
            ),
            self.move_repository: gapic_v1.method.wrap_method(
                self.move_repository,
                default_timeout=None,
                client_info=client_info,
            ),
            self.commit_repository_changes: gapic_v1.method.wrap_method(
                self.commit_repository_changes,
                default_timeout=None,
                client_info=client_info,
            ),
            self.read_repository_file: gapic_v1.method.wrap_method(
                self.read_repository_file,
                default_timeout=None,
                client_info=client_info,
            ),
            self.query_repository_directory_contents: gapic_v1.method.wrap_method(
                self.query_repository_directory_contents,
                default_timeout=None,
                client_info=client_info,
            ),
            self.fetch_repository_history: gapic_v1.method.wrap_method(
                self.fetch_repository_history,
                default_timeout=None,
                client_info=client_info,
            ),
            self.compute_repository_access_token_status: gapic_v1.method.wrap_method(
                self.compute_repository_access_token_status,
                default_timeout=None,
                client_info=client_info,
            ),
            self.fetch_remote_branches: gapic_v1.method.wrap_method(
                self.fetch_remote_branches,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_workspaces: gapic_v1.method.wrap_method(
                self.list_workspaces,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_workspace: gapic_v1.method.wrap_method(
                self.get_workspace,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_workspace: gapic_v1.method.wrap_method(
                self.create_workspace,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_workspace: gapic_v1.method.wrap_method(
                self.delete_workspace,
                default_timeout=None,
                client_info=client_info,
            ),
            self.install_npm_packages: gapic_v1.method.wrap_method(
                self.install_npm_packages,
                default_timeout=None,
                client_info=client_info,
            ),
            self.pull_git_commits: gapic_v1.method.wrap_method(
                self.pull_git_commits,
                default_timeout=None,
                client_info=client_info,
            ),
            self.push_git_commits: gapic_v1.method.wrap_method(
                self.push_git_commits,
                default_timeout=None,
                client_info=client_info,
            ),
            self.fetch_file_git_statuses: gapic_v1.method.wrap_method(
                self.fetch_file_git_statuses,
                default_timeout=None,
                client_info=client_info,
            ),
            self.fetch_git_ahead_behind: gapic_v1.method.wrap_method(
                self.fetch_git_ahead_behind,
                default_timeout=None,
                client_info=client_info,
            ),
            self.commit_workspace_changes: gapic_v1.method.wrap_method(
                self.commit_workspace_changes,
                default_timeout=None,
                client_info=client_info,
            ),
            self.reset_workspace_changes: gapic_v1.method.wrap_method(
                self.reset_workspace_changes,
                default_timeout=None,
                client_info=client_info,
            ),
            self.fetch_file_diff: gapic_v1.method.wrap_method(
                self.fetch_file_diff,
                default_timeout=None,
                client_info=client_info,
            ),
            self.query_directory_contents: gapic_v1.method.wrap_method(
                self.query_directory_contents,
                default_timeout=None,
                client_info=client_info,
            ),
            self.search_files: gapic_v1.method.wrap_method(
                self.search_files,
                default_timeout=None,
                client_info=client_info,
            ),
            self.make_directory: gapic_v1.method.wrap_method(
                self.make_directory,
                default_timeout=None,
                client_info=client_info,
            ),
            self.remove_directory: gapic_v1.method.wrap_method(
                self.remove_directory,
                default_timeout=None,
                client_info=client_info,
            ),
            self.move_directory: gapic_v1.method.wrap_method(
                self.move_directory,
                default_timeout=None,
                client_info=client_info,
            ),
            self.read_file: gapic_v1.method.wrap_method(
                self.read_file,
                default_timeout=None,
                client_info=client_info,
            ),
            self.remove_file: gapic_v1.method.wrap_method(
                self.remove_file,
                default_timeout=None,
                client_info=client_info,
            ),
            self.move_file: gapic_v1.method.wrap_method(
                self.move_file,
                default_timeout=None,
                client_info=client_info,
            ),
            self.write_file: gapic_v1.method.wrap_method(
                self.write_file,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_release_configs: gapic_v1.method.wrap_method(
                self.list_release_configs,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_release_config: gapic_v1.method.wrap_method(
                self.get_release_config,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_release_config: gapic_v1.method.wrap_method(
                self.create_release_config,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_release_config: gapic_v1.method.wrap_method(
                self.update_release_config,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_release_config: gapic_v1.method.wrap_method(
                self.delete_release_config,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_compilation_results: gapic_v1.method.wrap_method(
                self.list_compilation_results,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_compilation_result: gapic_v1.method.wrap_method(
                self.get_compilation_result,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_compilation_result: gapic_v1.method.wrap_method(
                self.create_compilation_result,
                default_timeout=None,
                client_info=client_info,
            ),
            self.query_compilation_result_actions: gapic_v1.method.wrap_method(
                self.query_compilation_result_actions,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_workflow_configs: gapic_v1.method.wrap_method(
                self.list_workflow_configs,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_workflow_config: gapic_v1.method.wrap_method(
                self.get_workflow_config,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_workflow_config: gapic_v1.method.wrap_method(
                self.create_workflow_config,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_workflow_config: gapic_v1.method.wrap_method(
                self.update_workflow_config,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_workflow_config: gapic_v1.method.wrap_method(
                self.delete_workflow_config,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_workflow_invocations: gapic_v1.method.wrap_method(
                self.list_workflow_invocations,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_workflow_invocation: gapic_v1.method.wrap_method(
                self.get_workflow_invocation,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_workflow_invocation: gapic_v1.method.wrap_method(
                self.create_workflow_invocation,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_workflow_invocation: gapic_v1.method.wrap_method(
                self.delete_workflow_invocation,
                default_timeout=None,
                client_info=client_info,
            ),
            self.cancel_workflow_invocation: gapic_v1.method.wrap_method(
                self.cancel_workflow_invocation,
                default_timeout=None,
                client_info=client_info,
            ),
            self.query_workflow_invocation_actions: gapic_v1.method.wrap_method(
                self.query_workflow_invocation_actions,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_config: gapic_v1.method.wrap_method(
                self.get_config,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_config: gapic_v1.method.wrap_method(
                self.update_config,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_iam_policy: gapic_v1.method.wrap_method(
                self.get_iam_policy,
                default_timeout=None,
                client_info=client_info,
            ),
            self.set_iam_policy: gapic_v1.method.wrap_method(
                self.set_iam_policy,
                default_timeout=None,
                client_info=client_info,
            ),
            self.test_iam_permissions: gapic_v1.method.wrap_method(
                self.test_iam_permissions,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_location: gapic_v1.method.wrap_method(
                self.get_location,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_locations: gapic_v1.method.wrap_method(
                self.list_locations,
                default_timeout=None,
                client_info=client_info,
            ),
            self.cancel_operation: gapic_v1.method.wrap_method(
                self.cancel_operation,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_operation: gapic_v1.method.wrap_method(
                self.delete_operation,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_operation: gapic_v1.method.wrap_method(
                self.get_operation,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_operations: gapic_v1.method.wrap_method(
                self.list_operations,
                default_timeout=None,
                client_info=client_info,
            ),
        }

    def close(self):
        """Closes resources associated with the transport.

        .. warning::
             Only call this method if the transport is NOT shared
             with other clients - this may cause errors in other clients!
        """
        raise NotImplementedError()

    @property
    def operations_client(self):
        """Return the client designed to process long-running operations."""
        raise NotImplementedError()

    @property
    def get_team_folder(
        self,
    ) -> Callable[
        [dataform.GetTeamFolderRequest],
        Union[dataform.TeamFolder, Awaitable[dataform.TeamFolder]],
    ]:
        raise NotImplementedError()

    @property
    def create_team_folder(
        self,
    ) -> Callable[
        [dataform.CreateTeamFolderRequest],
        Union[dataform.TeamFolder, Awaitable[dataform.TeamFolder]],
    ]:
        raise NotImplementedError()

    @property
    def update_team_folder(
        self,
    ) -> Callable[
        [dataform.UpdateTeamFolderRequest],
        Union[dataform.TeamFolder, Awaitable[dataform.TeamFolder]],
    ]:
        raise NotImplementedError()

    @property
    def delete_team_folder(
        self,
    ) -> Callable[
        [dataform.DeleteTeamFolderRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def delete_team_folder_tree(
        self,
    ) -> Callable[
        [dataform.DeleteTeamFolderTreeRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def query_team_folder_contents(
        self,
    ) -> Callable[
        [dataform.QueryTeamFolderContentsRequest],
        Union[
            dataform.QueryTeamFolderContentsResponse,
            Awaitable[dataform.QueryTeamFolderContentsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def search_team_folders(
        self,
    ) -> Callable[
        [dataform.SearchTeamFoldersRequest],
        Union[
            dataform.SearchTeamFoldersResponse,
            Awaitable[dataform.SearchTeamFoldersResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_folder(
        self,
    ) -> Callable[
        [dataform.GetFolderRequest], Union[dataform.Folder, Awaitable[dataform.Folder]]
    ]:
        raise NotImplementedError()

    @property
    def create_folder(
        self,
    ) -> Callable[
        [dataform.CreateFolderRequest],
        Union[dataform.Folder, Awaitable[dataform.Folder]],
    ]:
        raise NotImplementedError()

    @property
    def update_folder(
        self,
    ) -> Callable[
        [dataform.UpdateFolderRequest],
        Union[dataform.Folder, Awaitable[dataform.Folder]],
    ]:
        raise NotImplementedError()

    @property
    def delete_folder(
        self,
    ) -> Callable[
        [dataform.DeleteFolderRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def delete_folder_tree(
        self,
    ) -> Callable[
        [dataform.DeleteFolderTreeRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def query_folder_contents(
        self,
    ) -> Callable[
        [dataform.QueryFolderContentsRequest],
        Union[
            dataform.QueryFolderContentsResponse,
            Awaitable[dataform.QueryFolderContentsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def query_user_root_contents(
        self,
    ) -> Callable[
        [dataform.QueryUserRootContentsRequest],
        Union[
            dataform.QueryUserRootContentsResponse,
            Awaitable[dataform.QueryUserRootContentsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def move_folder(
        self,
    ) -> Callable[
        [dataform.MoveFolderRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_repositories(
        self,
    ) -> Callable[
        [dataform.ListRepositoriesRequest],
        Union[
            dataform.ListRepositoriesResponse,
            Awaitable[dataform.ListRepositoriesResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_repository(
        self,
    ) -> Callable[
        [dataform.GetRepositoryRequest],
        Union[dataform.Repository, Awaitable[dataform.Repository]],
    ]:
        raise NotImplementedError()

    @property
    def create_repository(
        self,
    ) -> Callable[
        [dataform.CreateRepositoryRequest],
        Union[dataform.Repository, Awaitable[dataform.Repository]],
    ]:
        raise NotImplementedError()

    @property
    def update_repository(
        self,
    ) -> Callable[
        [dataform.UpdateRepositoryRequest],
        Union[dataform.Repository, Awaitable[dataform.Repository]],
    ]:
        raise NotImplementedError()

    @property
    def delete_repository(
        self,
    ) -> Callable[
        [dataform.DeleteRepositoryRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def move_repository(
        self,
    ) -> Callable[
        [dataform.MoveRepositoryRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def commit_repository_changes(
        self,
    ) -> Callable[
        [dataform.CommitRepositoryChangesRequest],
        Union[
            dataform.CommitRepositoryChangesResponse,
            Awaitable[dataform.CommitRepositoryChangesResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def read_repository_file(
        self,
    ) -> Callable[
        [dataform.ReadRepositoryFileRequest],
        Union[
            dataform.ReadRepositoryFileResponse,
            Awaitable[dataform.ReadRepositoryFileResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def query_repository_directory_contents(
        self,
    ) -> Callable[
        [dataform.QueryRepositoryDirectoryContentsRequest],
        Union[
            dataform.QueryRepositoryDirectoryContentsResponse,
            Awaitable[dataform.QueryRepositoryDirectoryContentsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def fetch_repository_history(
        self,
    ) -> Callable[
        [dataform.FetchRepositoryHistoryRequest],
        Union[
            dataform.FetchRepositoryHistoryResponse,
            Awaitable[dataform.FetchRepositoryHistoryResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def compute_repository_access_token_status(
        self,
    ) -> Callable[
        [dataform.ComputeRepositoryAccessTokenStatusRequest],
        Union[
            dataform.ComputeRepositoryAccessTokenStatusResponse,
            Awaitable[dataform.ComputeRepositoryAccessTokenStatusResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def fetch_remote_branches(
        self,
    ) -> Callable[
        [dataform.FetchRemoteBranchesRequest],
        Union[
            dataform.FetchRemoteBranchesResponse,
            Awaitable[dataform.FetchRemoteBranchesResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_workspaces(
        self,
    ) -> Callable[
        [dataform.ListWorkspacesRequest],
        Union[
            dataform.ListWorkspacesResponse, Awaitable[dataform.ListWorkspacesResponse]
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_workspace(
        self,
    ) -> Callable[
        [dataform.GetWorkspaceRequest],
        Union[dataform.Workspace, Awaitable[dataform.Workspace]],
    ]:
        raise NotImplementedError()

    @property
    def create_workspace(
        self,
    ) -> Callable[
        [dataform.CreateWorkspaceRequest],
        Union[dataform.Workspace, Awaitable[dataform.Workspace]],
    ]:
        raise NotImplementedError()

    @property
    def delete_workspace(
        self,
    ) -> Callable[
        [dataform.DeleteWorkspaceRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def install_npm_packages(
        self,
    ) -> Callable[
        [dataform.InstallNpmPackagesRequest],
        Union[
            dataform.InstallNpmPackagesResponse,
            Awaitable[dataform.InstallNpmPackagesResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def pull_git_commits(
        self,
    ) -> Callable[
        [dataform.PullGitCommitsRequest],
        Union[
            dataform.PullGitCommitsResponse, Awaitable[dataform.PullGitCommitsResponse]
        ],
    ]:
        raise NotImplementedError()

    @property
    def push_git_commits(
        self,
    ) -> Callable[
        [dataform.PushGitCommitsRequest],
        Union[
            dataform.PushGitCommitsResponse, Awaitable[dataform.PushGitCommitsResponse]
        ],
    ]:
        raise NotImplementedError()

    @property
    def fetch_file_git_statuses(
        self,
    ) -> Callable[
        [dataform.FetchFileGitStatusesRequest],
        Union[
            dataform.FetchFileGitStatusesResponse,
            Awaitable[dataform.FetchFileGitStatusesResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def fetch_git_ahead_behind(
        self,
    ) -> Callable[
        [dataform.FetchGitAheadBehindRequest],
        Union[
            dataform.FetchGitAheadBehindResponse,
            Awaitable[dataform.FetchGitAheadBehindResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def commit_workspace_changes(
        self,
    ) -> Callable[
        [dataform.CommitWorkspaceChangesRequest],
        Union[
            dataform.CommitWorkspaceChangesResponse,
            Awaitable[dataform.CommitWorkspaceChangesResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def reset_workspace_changes(
        self,
    ) -> Callable[
        [dataform.ResetWorkspaceChangesRequest],
        Union[
            dataform.ResetWorkspaceChangesResponse,
            Awaitable[dataform.ResetWorkspaceChangesResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def fetch_file_diff(
        self,
    ) -> Callable[
        [dataform.FetchFileDiffRequest],
        Union[
            dataform.FetchFileDiffResponse, Awaitable[dataform.FetchFileDiffResponse]
        ],
    ]:
        raise NotImplementedError()

    @property
    def query_directory_contents(
        self,
    ) -> Callable[
        [dataform.QueryDirectoryContentsRequest],
        Union[
            dataform.QueryDirectoryContentsResponse,
            Awaitable[dataform.QueryDirectoryContentsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def search_files(
        self,
    ) -> Callable[
        [dataform.SearchFilesRequest],
        Union[dataform.SearchFilesResponse, Awaitable[dataform.SearchFilesResponse]],
    ]:
        raise NotImplementedError()

    @property
    def make_directory(
        self,
    ) -> Callable[
        [dataform.MakeDirectoryRequest],
        Union[
            dataform.MakeDirectoryResponse, Awaitable[dataform.MakeDirectoryResponse]
        ],
    ]:
        raise NotImplementedError()

    @property
    def remove_directory(
        self,
    ) -> Callable[
        [dataform.RemoveDirectoryRequest],
        Union[
            dataform.RemoveDirectoryResponse,
            Awaitable[dataform.RemoveDirectoryResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def move_directory(
        self,
    ) -> Callable[
        [dataform.MoveDirectoryRequest],
        Union[
            dataform.MoveDirectoryResponse, Awaitable[dataform.MoveDirectoryResponse]
        ],
    ]:
        raise NotImplementedError()

    @property
    def read_file(
        self,
    ) -> Callable[
        [dataform.ReadFileRequest],
        Union[dataform.ReadFileResponse, Awaitable[dataform.ReadFileResponse]],
    ]:
        raise NotImplementedError()

    @property
    def remove_file(
        self,
    ) -> Callable[
        [dataform.RemoveFileRequest],
        Union[dataform.RemoveFileResponse, Awaitable[dataform.RemoveFileResponse]],
    ]:
        raise NotImplementedError()

    @property
    def move_file(
        self,
    ) -> Callable[
        [dataform.MoveFileRequest],
        Union[dataform.MoveFileResponse, Awaitable[dataform.MoveFileResponse]],
    ]:
        raise NotImplementedError()

    @property
    def write_file(
        self,
    ) -> Callable[
        [dataform.WriteFileRequest],
        Union[dataform.WriteFileResponse, Awaitable[dataform.WriteFileResponse]],
    ]:
        raise NotImplementedError()

    @property
    def list_release_configs(
        self,
    ) -> Callable[
        [dataform.ListReleaseConfigsRequest],
        Union[
            dataform.ListReleaseConfigsResponse,
            Awaitable[dataform.ListReleaseConfigsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_release_config(
        self,
    ) -> Callable[
        [dataform.GetReleaseConfigRequest],
        Union[dataform.ReleaseConfig, Awaitable[dataform.ReleaseConfig]],
    ]:
        raise NotImplementedError()

    @property
    def create_release_config(
        self,
    ) -> Callable[
        [dataform.CreateReleaseConfigRequest],
        Union[dataform.ReleaseConfig, Awaitable[dataform.ReleaseConfig]],
    ]:
        raise NotImplementedError()

    @property
    def update_release_config(
        self,
    ) -> Callable[
        [dataform.UpdateReleaseConfigRequest],
        Union[dataform.ReleaseConfig, Awaitable[dataform.ReleaseConfig]],
    ]:
        raise NotImplementedError()

    @property
    def delete_release_config(
        self,
    ) -> Callable[
        [dataform.DeleteReleaseConfigRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def list_compilation_results(
        self,
    ) -> Callable[
        [dataform.ListCompilationResultsRequest],
        Union[
            dataform.ListCompilationResultsResponse,
            Awaitable[dataform.ListCompilationResultsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_compilation_result(
        self,
    ) -> Callable[
        [dataform.GetCompilationResultRequest],
        Union[dataform.CompilationResult, Awaitable[dataform.CompilationResult]],
    ]:
        raise NotImplementedError()

    @property
    def create_compilation_result(
        self,
    ) -> Callable[
        [dataform.CreateCompilationResultRequest],
        Union[dataform.CompilationResult, Awaitable[dataform.CompilationResult]],
    ]:
        raise NotImplementedError()

    @property
    def query_compilation_result_actions(
        self,
    ) -> Callable[
        [dataform.QueryCompilationResultActionsRequest],
        Union[
            dataform.QueryCompilationResultActionsResponse,
            Awaitable[dataform.QueryCompilationResultActionsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_workflow_configs(
        self,
    ) -> Callable[
        [dataform.ListWorkflowConfigsRequest],
        Union[
            dataform.ListWorkflowConfigsResponse,
            Awaitable[dataform.ListWorkflowConfigsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_workflow_config(
        self,
    ) -> Callable[
        [dataform.GetWorkflowConfigRequest],
        Union[dataform.WorkflowConfig, Awaitable[dataform.WorkflowConfig]],
    ]:
        raise NotImplementedError()

    @property
    def create_workflow_config(
        self,
    ) -> Callable[
        [dataform.CreateWorkflowConfigRequest],
        Union[dataform.WorkflowConfig, Awaitable[dataform.WorkflowConfig]],
    ]:
        raise NotImplementedError()

    @property
    def update_workflow_config(
        self,
    ) -> Callable[
        [dataform.UpdateWorkflowConfigRequest],
        Union[dataform.WorkflowConfig, Awaitable[dataform.WorkflowConfig]],
    ]:
        raise NotImplementedError()

    @property
    def delete_workflow_config(
        self,
    ) -> Callable[
        [dataform.DeleteWorkflowConfigRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def list_workflow_invocations(
        self,
    ) -> Callable[
        [dataform.ListWorkflowInvocationsRequest],
        Union[
            dataform.ListWorkflowInvocationsResponse,
            Awaitable[dataform.ListWorkflowInvocationsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_workflow_invocation(
        self,
    ) -> Callable[
        [dataform.GetWorkflowInvocationRequest],
        Union[dataform.WorkflowInvocation, Awaitable[dataform.WorkflowInvocation]],
    ]:
        raise NotImplementedError()

    @property
    def create_workflow_invocation(
        self,
    ) -> Callable[
        [dataform.CreateWorkflowInvocationRequest],
        Union[dataform.WorkflowInvocation, Awaitable[dataform.WorkflowInvocation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_workflow_invocation(
        self,
    ) -> Callable[
        [dataform.DeleteWorkflowInvocationRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def cancel_workflow_invocation(
        self,
    ) -> Callable[
        [dataform.CancelWorkflowInvocationRequest],
        Union[
            dataform.CancelWorkflowInvocationResponse,
            Awaitable[dataform.CancelWorkflowInvocationResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def query_workflow_invocation_actions(
        self,
    ) -> Callable[
        [dataform.QueryWorkflowInvocationActionsRequest],
        Union[
            dataform.QueryWorkflowInvocationActionsResponse,
            Awaitable[dataform.QueryWorkflowInvocationActionsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_config(
        self,
    ) -> Callable[
        [dataform.GetConfigRequest], Union[dataform.Config, Awaitable[dataform.Config]]
    ]:
        raise NotImplementedError()

    @property
    def update_config(
        self,
    ) -> Callable[
        [dataform.UpdateConfigRequest],
        Union[dataform.Config, Awaitable[dataform.Config]],
    ]:
        raise NotImplementedError()

    @property
    def get_iam_policy(
        self,
    ) -> Callable[
        [iam_policy_pb2.GetIamPolicyRequest],
        Union[policy_pb2.Policy, Awaitable[policy_pb2.Policy]],
    ]:
        raise NotImplementedError()

    @property
    def set_iam_policy(
        self,
    ) -> Callable[
        [iam_policy_pb2.SetIamPolicyRequest],
        Union[policy_pb2.Policy, Awaitable[policy_pb2.Policy]],
    ]:
        raise NotImplementedError()

    @property
    def test_iam_permissions(
        self,
    ) -> Callable[
        [iam_policy_pb2.TestIamPermissionsRequest],
        Union[
            iam_policy_pb2.TestIamPermissionsResponse,
            Awaitable[iam_policy_pb2.TestIamPermissionsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_operations(
        self,
    ) -> Callable[
        [operations_pb2.ListOperationsRequest],
        Union[
            operations_pb2.ListOperationsResponse,
            Awaitable[operations_pb2.ListOperationsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_operation(
        self,
    ) -> Callable[
        [operations_pb2.GetOperationRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def cancel_operation(
        self,
    ) -> Callable[
        [operations_pb2.CancelOperationRequest],
        None,
    ]:
        raise NotImplementedError()

    @property
    def delete_operation(
        self,
    ) -> Callable[
        [operations_pb2.DeleteOperationRequest],
        None,
    ]:
        raise NotImplementedError()

    @property
    def get_location(
        self,
    ) -> Callable[
        [locations_pb2.GetLocationRequest],
        Union[locations_pb2.Location, Awaitable[locations_pb2.Location]],
    ]:
        raise NotImplementedError()

    @property
    def list_locations(
        self,
    ) -> Callable[
        [locations_pb2.ListLocationsRequest],
        Union[
            locations_pb2.ListLocationsResponse,
            Awaitable[locations_pb2.ListLocationsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def kind(self) -> str:
        raise NotImplementedError()


__all__ = ("DataformTransport",)
