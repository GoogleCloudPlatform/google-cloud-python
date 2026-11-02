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
import dataclasses
import json  # type: ignore
import logging
import warnings
from typing import Any, Callable, Dict, List, Optional, Sequence, Tuple, Union

import google.iam.v1.iam_policy_pb2 as iam_policy_pb2  # type: ignore
import google.iam.v1.policy_pb2 as policy_pb2  # type: ignore
import google.protobuf
import google.protobuf.empty_pb2 as empty_pb2  # type: ignore
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1, operations_v1, rest_helpers, rest_streaming
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.auth.transport.requests import AuthorizedSession  # type: ignore
from google.cloud.location import locations_pb2  # type: ignore
from google.iam.v1 import (
    iam_policy_pb2,  # type: ignore
    policy_pb2,  # type: ignore
)
from google.longrunning import operations_pb2  # type: ignore
from google.protobuf import json_format
from requests import __version__ as requests_version

from google.cloud.dataform_v1._compat import transcode_request
from google.cloud.dataform_v1.types import dataform

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseDataformRestTransport

try:
    OptionalRetry = Union[retries.Retry, gapic_v1.method._MethodDefault, None]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.Retry, object, None]  # type: ignore

try:
    from google.api_core import client_logging  # type: ignore

    CLIENT_LOGGING_SUPPORTED = True  # pragma: NO COVER
except ImportError:  # pragma: NO COVER
    CLIENT_LOGGING_SUPPORTED = False

_LOGGER = logging.getLogger(__name__)

DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=BASE_DEFAULT_CLIENT_INFO.gapic_version,
    grpc_version=None,
    rest_version=f"requests@{requests_version}",
)

DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


class DataformRestInterceptor:
    """Interceptor for Dataform.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the DataformRestTransport.

    .. code-block:: python
        class MyCustomDataformInterceptor(DataformRestInterceptor):
            def pre_cancel_workflow_invocation(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_cancel_workflow_invocation(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_commit_repository_changes(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_commit_repository_changes(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_commit_workspace_changes(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_commit_workspace_changes(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_compute_repository_access_token_status(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_compute_repository_access_token_status(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_compilation_result(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_compilation_result(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_folder(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_folder(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_release_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_release_config(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_repository(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_repository(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_team_folder(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_team_folder(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_workflow_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_workflow_config(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_workflow_invocation(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_workflow_invocation(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_workspace(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_workspace(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_folder(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_delete_folder_tree(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_folder_tree(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_release_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_delete_repository(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_delete_team_folder(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_delete_team_folder_tree(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_team_folder_tree(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_workflow_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_delete_workflow_invocation(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_delete_workspace(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_fetch_file_diff(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_fetch_file_diff(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_fetch_file_git_statuses(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_fetch_file_git_statuses(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_fetch_git_ahead_behind(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_fetch_git_ahead_behind(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_fetch_remote_branches(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_fetch_remote_branches(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_fetch_repository_history(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_fetch_repository_history(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_compilation_result(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_compilation_result(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_config(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_folder(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_folder(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_iam_policy(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_iam_policy(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_release_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_release_config(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_repository(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_repository(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_team_folder(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_team_folder(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_workflow_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_workflow_config(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_workflow_invocation(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_workflow_invocation(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_workspace(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_workspace(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_install_npm_packages(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_install_npm_packages(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_compilation_results(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_compilation_results(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_release_configs(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_release_configs(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_repositories(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_repositories(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_workflow_configs(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_workflow_configs(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_workflow_invocations(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_workflow_invocations(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_workspaces(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_workspaces(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_make_directory(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_make_directory(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_move_directory(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_move_directory(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_move_file(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_move_file(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_move_folder(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_move_folder(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_move_repository(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_move_repository(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_pull_git_commits(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_pull_git_commits(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_push_git_commits(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_push_git_commits(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_query_compilation_result_actions(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_query_compilation_result_actions(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_query_directory_contents(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_query_directory_contents(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_query_folder_contents(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_query_folder_contents(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_query_repository_directory_contents(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_query_repository_directory_contents(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_query_team_folder_contents(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_query_team_folder_contents(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_query_user_root_contents(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_query_user_root_contents(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_query_workflow_invocation_actions(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_query_workflow_invocation_actions(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_read_file(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_read_file(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_read_repository_file(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_read_repository_file(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_remove_directory(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_remove_directory(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_remove_file(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_remove_file(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_reset_workspace_changes(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_reset_workspace_changes(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_search_files(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_search_files(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_search_team_folders(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_search_team_folders(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_set_iam_policy(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_set_iam_policy(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_test_iam_permissions(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_test_iam_permissions(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_config(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_folder(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_folder(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_release_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_release_config(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_repository(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_repository(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_team_folder(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_team_folder(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_workflow_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_workflow_config(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_write_file(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_write_file(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = DataformRestTransport(interceptor=MyCustomDataformInterceptor())
        client = DataformClient(transport=transport)


    """

    def pre_cancel_workflow_invocation(
        self,
        request: dataform.CancelWorkflowInvocationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dataform.CancelWorkflowInvocationRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for cancel_workflow_invocation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Dataform server.
        """
        return request, metadata

    def post_cancel_workflow_invocation(
        self, response: dataform.CancelWorkflowInvocationResponse
    ) -> dataform.CancelWorkflowInvocationResponse:
        """Post-rpc interceptor for cancel_workflow_invocation

        DEPRECATED. Please use the `post_cancel_workflow_invocation_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Dataform server but before
        it is returned to user code. This `post_cancel_workflow_invocation` interceptor runs
        before the `post_cancel_workflow_invocation_with_metadata` interceptor.
        """
        return response

    def post_cancel_workflow_invocation_with_metadata(
        self,
        response: dataform.CancelWorkflowInvocationResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dataform.CancelWorkflowInvocationResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for cancel_workflow_invocation

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Dataform server but before it is returned to user code.

        We recommend only using this `post_cancel_workflow_invocation_with_metadata`
        interceptor in new development instead of the `post_cancel_workflow_invocation` interceptor.
        When both interceptors are used, this `post_cancel_workflow_invocation_with_metadata` interceptor runs after the
        `post_cancel_workflow_invocation` interceptor. The (possibly modified) response returned by
        `post_cancel_workflow_invocation` will be passed to
        `post_cancel_workflow_invocation_with_metadata`.
        """
        return response, metadata

    def pre_commit_repository_changes(
        self,
        request: dataform.CommitRepositoryChangesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dataform.CommitRepositoryChangesRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for commit_repository_changes

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Dataform server.
        """
        return request, metadata

    def post_commit_repository_changes(
        self, response: dataform.CommitRepositoryChangesResponse
    ) -> dataform.CommitRepositoryChangesResponse:
        """Post-rpc interceptor for commit_repository_changes

        DEPRECATED. Please use the `post_commit_repository_changes_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Dataform server but before
        it is returned to user code. This `post_commit_repository_changes` interceptor runs
        before the `post_commit_repository_changes_with_metadata` interceptor.
        """
        return response

    def post_commit_repository_changes_with_metadata(
        self,
        response: dataform.CommitRepositoryChangesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dataform.CommitRepositoryChangesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for commit_repository_changes

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Dataform server but before it is returned to user code.

        We recommend only using this `post_commit_repository_changes_with_metadata`
        interceptor in new development instead of the `post_commit_repository_changes` interceptor.
        When both interceptors are used, this `post_commit_repository_changes_with_metadata` interceptor runs after the
        `post_commit_repository_changes` interceptor. The (possibly modified) response returned by
        `post_commit_repository_changes` will be passed to
        `post_commit_repository_changes_with_metadata`.
        """
        return response, metadata

    def pre_commit_workspace_changes(
        self,
        request: dataform.CommitWorkspaceChangesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dataform.CommitWorkspaceChangesRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for commit_workspace_changes

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Dataform server.
        """
        return request, metadata

    def post_commit_workspace_changes(
        self, response: dataform.CommitWorkspaceChangesResponse
    ) -> dataform.CommitWorkspaceChangesResponse:
        """Post-rpc interceptor for commit_workspace_changes

        DEPRECATED. Please use the `post_commit_workspace_changes_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Dataform server but before
        it is returned to user code. This `post_commit_workspace_changes` interceptor runs
        before the `post_commit_workspace_changes_with_metadata` interceptor.
        """
        return response

    def post_commit_workspace_changes_with_metadata(
        self,
        response: dataform.CommitWorkspaceChangesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dataform.CommitWorkspaceChangesResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for commit_workspace_changes

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Dataform server but before it is returned to user code.

        We recommend only using this `post_commit_workspace_changes_with_metadata`
        interceptor in new development instead of the `post_commit_workspace_changes` interceptor.
        When both interceptors are used, this `post_commit_workspace_changes_with_metadata` interceptor runs after the
        `post_commit_workspace_changes` interceptor. The (possibly modified) response returned by
        `post_commit_workspace_changes` will be passed to
        `post_commit_workspace_changes_with_metadata`.
        """
        return response, metadata

    def pre_compute_repository_access_token_status(
        self,
        request: dataform.ComputeRepositoryAccessTokenStatusRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dataform.ComputeRepositoryAccessTokenStatusRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for compute_repository_access_token_status

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Dataform server.
        """
        return request, metadata

    def post_compute_repository_access_token_status(
        self, response: dataform.ComputeRepositoryAccessTokenStatusResponse
    ) -> dataform.ComputeRepositoryAccessTokenStatusResponse:
        """Post-rpc interceptor for compute_repository_access_token_status

        DEPRECATED. Please use the `post_compute_repository_access_token_status_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Dataform server but before
        it is returned to user code. This `post_compute_repository_access_token_status` interceptor runs
        before the `post_compute_repository_access_token_status_with_metadata` interceptor.
        """
        return response

    def post_compute_repository_access_token_status_with_metadata(
        self,
        response: dataform.ComputeRepositoryAccessTokenStatusResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dataform.ComputeRepositoryAccessTokenStatusResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for compute_repository_access_token_status

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Dataform server but before it is returned to user code.

        We recommend only using this `post_compute_repository_access_token_status_with_metadata`
        interceptor in new development instead of the `post_compute_repository_access_token_status` interceptor.
        When both interceptors are used, this `post_compute_repository_access_token_status_with_metadata` interceptor runs after the
        `post_compute_repository_access_token_status` interceptor. The (possibly modified) response returned by
        `post_compute_repository_access_token_status` will be passed to
        `post_compute_repository_access_token_status_with_metadata`.
        """
        return response, metadata

    def pre_create_compilation_result(
        self,
        request: dataform.CreateCompilationResultRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dataform.CreateCompilationResultRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_compilation_result

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Dataform server.
        """
        return request, metadata

    def post_create_compilation_result(
        self, response: dataform.CompilationResult
    ) -> dataform.CompilationResult:
        """Post-rpc interceptor for create_compilation_result

        DEPRECATED. Please use the `post_create_compilation_result_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Dataform server but before
        it is returned to user code. This `post_create_compilation_result` interceptor runs
        before the `post_create_compilation_result_with_metadata` interceptor.
        """
        return response

    def post_create_compilation_result_with_metadata(
        self,
        response: dataform.CompilationResult,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[dataform.CompilationResult, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_compilation_result

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Dataform server but before it is returned to user code.

        We recommend only using this `post_create_compilation_result_with_metadata`
        interceptor in new development instead of the `post_create_compilation_result` interceptor.
        When both interceptors are used, this `post_create_compilation_result_with_metadata` interceptor runs after the
        `post_create_compilation_result` interceptor. The (possibly modified) response returned by
        `post_create_compilation_result` will be passed to
        `post_create_compilation_result_with_metadata`.
        """
        return response, metadata

    def pre_create_folder(
        self,
        request: dataform.CreateFolderRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[dataform.CreateFolderRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for create_folder

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Dataform server.
        """
        return request, metadata

    def post_create_folder(self, response: dataform.Folder) -> dataform.Folder:
        """Post-rpc interceptor for create_folder

        DEPRECATED. Please use the `post_create_folder_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Dataform server but before
        it is returned to user code. This `post_create_folder` interceptor runs
        before the `post_create_folder_with_metadata` interceptor.
        """
        return response

    def post_create_folder_with_metadata(
        self,
        response: dataform.Folder,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[dataform.Folder, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_folder

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Dataform server but before it is returned to user code.

        We recommend only using this `post_create_folder_with_metadata`
        interceptor in new development instead of the `post_create_folder` interceptor.
        When both interceptors are used, this `post_create_folder_with_metadata` interceptor runs after the
        `post_create_folder` interceptor. The (possibly modified) response returned by
        `post_create_folder` will be passed to
        `post_create_folder_with_metadata`.
        """
        return response, metadata

    def pre_create_release_config(
        self,
        request: dataform.CreateReleaseConfigRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dataform.CreateReleaseConfigRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_release_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Dataform server.
        """
        return request, metadata

    def post_create_release_config(
        self, response: dataform.ReleaseConfig
    ) -> dataform.ReleaseConfig:
        """Post-rpc interceptor for create_release_config

        DEPRECATED. Please use the `post_create_release_config_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Dataform server but before
        it is returned to user code. This `post_create_release_config` interceptor runs
        before the `post_create_release_config_with_metadata` interceptor.
        """
        return response

    def post_create_release_config_with_metadata(
        self,
        response: dataform.ReleaseConfig,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[dataform.ReleaseConfig, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_release_config

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Dataform server but before it is returned to user code.

        We recommend only using this `post_create_release_config_with_metadata`
        interceptor in new development instead of the `post_create_release_config` interceptor.
        When both interceptors are used, this `post_create_release_config_with_metadata` interceptor runs after the
        `post_create_release_config` interceptor. The (possibly modified) response returned by
        `post_create_release_config` will be passed to
        `post_create_release_config_with_metadata`.
        """
        return response, metadata

    def pre_create_repository(
        self,
        request: dataform.CreateRepositoryRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dataform.CreateRepositoryRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_repository

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Dataform server.
        """
        return request, metadata

    def post_create_repository(
        self, response: dataform.Repository
    ) -> dataform.Repository:
        """Post-rpc interceptor for create_repository

        DEPRECATED. Please use the `post_create_repository_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Dataform server but before
        it is returned to user code. This `post_create_repository` interceptor runs
        before the `post_create_repository_with_metadata` interceptor.
        """
        return response

    def post_create_repository_with_metadata(
        self,
        response: dataform.Repository,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[dataform.Repository, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_repository

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Dataform server but before it is returned to user code.

        We recommend only using this `post_create_repository_with_metadata`
        interceptor in new development instead of the `post_create_repository` interceptor.
        When both interceptors are used, this `post_create_repository_with_metadata` interceptor runs after the
        `post_create_repository` interceptor. The (possibly modified) response returned by
        `post_create_repository` will be passed to
        `post_create_repository_with_metadata`.
        """
        return response, metadata

    def pre_create_team_folder(
        self,
        request: dataform.CreateTeamFolderRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dataform.CreateTeamFolderRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_team_folder

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Dataform server.
        """
        return request, metadata

    def post_create_team_folder(
        self, response: dataform.TeamFolder
    ) -> dataform.TeamFolder:
        """Post-rpc interceptor for create_team_folder

        DEPRECATED. Please use the `post_create_team_folder_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Dataform server but before
        it is returned to user code. This `post_create_team_folder` interceptor runs
        before the `post_create_team_folder_with_metadata` interceptor.
        """
        return response

    def post_create_team_folder_with_metadata(
        self,
        response: dataform.TeamFolder,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[dataform.TeamFolder, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_team_folder

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Dataform server but before it is returned to user code.

        We recommend only using this `post_create_team_folder_with_metadata`
        interceptor in new development instead of the `post_create_team_folder` interceptor.
        When both interceptors are used, this `post_create_team_folder_with_metadata` interceptor runs after the
        `post_create_team_folder` interceptor. The (possibly modified) response returned by
        `post_create_team_folder` will be passed to
        `post_create_team_folder_with_metadata`.
        """
        return response, metadata

    def pre_create_workflow_config(
        self,
        request: dataform.CreateWorkflowConfigRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dataform.CreateWorkflowConfigRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_workflow_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Dataform server.
        """
        return request, metadata

    def post_create_workflow_config(
        self, response: dataform.WorkflowConfig
    ) -> dataform.WorkflowConfig:
        """Post-rpc interceptor for create_workflow_config

        DEPRECATED. Please use the `post_create_workflow_config_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Dataform server but before
        it is returned to user code. This `post_create_workflow_config` interceptor runs
        before the `post_create_workflow_config_with_metadata` interceptor.
        """
        return response

    def post_create_workflow_config_with_metadata(
        self,
        response: dataform.WorkflowConfig,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[dataform.WorkflowConfig, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_workflow_config

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Dataform server but before it is returned to user code.

        We recommend only using this `post_create_workflow_config_with_metadata`
        interceptor in new development instead of the `post_create_workflow_config` interceptor.
        When both interceptors are used, this `post_create_workflow_config_with_metadata` interceptor runs after the
        `post_create_workflow_config` interceptor. The (possibly modified) response returned by
        `post_create_workflow_config` will be passed to
        `post_create_workflow_config_with_metadata`.
        """
        return response, metadata

    def pre_create_workflow_invocation(
        self,
        request: dataform.CreateWorkflowInvocationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dataform.CreateWorkflowInvocationRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_workflow_invocation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Dataform server.
        """
        return request, metadata

    def post_create_workflow_invocation(
        self, response: dataform.WorkflowInvocation
    ) -> dataform.WorkflowInvocation:
        """Post-rpc interceptor for create_workflow_invocation

        DEPRECATED. Please use the `post_create_workflow_invocation_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Dataform server but before
        it is returned to user code. This `post_create_workflow_invocation` interceptor runs
        before the `post_create_workflow_invocation_with_metadata` interceptor.
        """
        return response

    def post_create_workflow_invocation_with_metadata(
        self,
        response: dataform.WorkflowInvocation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[dataform.WorkflowInvocation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_workflow_invocation

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Dataform server but before it is returned to user code.

        We recommend only using this `post_create_workflow_invocation_with_metadata`
        interceptor in new development instead of the `post_create_workflow_invocation` interceptor.
        When both interceptors are used, this `post_create_workflow_invocation_with_metadata` interceptor runs after the
        `post_create_workflow_invocation` interceptor. The (possibly modified) response returned by
        `post_create_workflow_invocation` will be passed to
        `post_create_workflow_invocation_with_metadata`.
        """
        return response, metadata

    def pre_create_workspace(
        self,
        request: dataform.CreateWorkspaceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dataform.CreateWorkspaceRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_workspace

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Dataform server.
        """
        return request, metadata

    def post_create_workspace(self, response: dataform.Workspace) -> dataform.Workspace:
        """Post-rpc interceptor for create_workspace

        DEPRECATED. Please use the `post_create_workspace_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Dataform server but before
        it is returned to user code. This `post_create_workspace` interceptor runs
        before the `post_create_workspace_with_metadata` interceptor.
        """
        return response

    def post_create_workspace_with_metadata(
        self,
        response: dataform.Workspace,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[dataform.Workspace, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_workspace

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Dataform server but before it is returned to user code.

        We recommend only using this `post_create_workspace_with_metadata`
        interceptor in new development instead of the `post_create_workspace` interceptor.
        When both interceptors are used, this `post_create_workspace_with_metadata` interceptor runs after the
        `post_create_workspace` interceptor. The (possibly modified) response returned by
        `post_create_workspace` will be passed to
        `post_create_workspace_with_metadata`.
        """
        return response, metadata

    def pre_delete_folder(
        self,
        request: dataform.DeleteFolderRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[dataform.DeleteFolderRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for delete_folder

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Dataform server.
        """
        return request, metadata

    def pre_delete_folder_tree(
        self,
        request: dataform.DeleteFolderTreeRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dataform.DeleteFolderTreeRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_folder_tree

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Dataform server.
        """
        return request, metadata

    def post_delete_folder_tree(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_folder_tree

        DEPRECATED. Please use the `post_delete_folder_tree_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Dataform server but before
        it is returned to user code. This `post_delete_folder_tree` interceptor runs
        before the `post_delete_folder_tree_with_metadata` interceptor.
        """
        return response

    def post_delete_folder_tree_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_folder_tree

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Dataform server but before it is returned to user code.

        We recommend only using this `post_delete_folder_tree_with_metadata`
        interceptor in new development instead of the `post_delete_folder_tree` interceptor.
        When both interceptors are used, this `post_delete_folder_tree_with_metadata` interceptor runs after the
        `post_delete_folder_tree` interceptor. The (possibly modified) response returned by
        `post_delete_folder_tree` will be passed to
        `post_delete_folder_tree_with_metadata`.
        """
        return response, metadata

    def pre_delete_release_config(
        self,
        request: dataform.DeleteReleaseConfigRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dataform.DeleteReleaseConfigRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_release_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Dataform server.
        """
        return request, metadata

    def pre_delete_repository(
        self,
        request: dataform.DeleteRepositoryRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dataform.DeleteRepositoryRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_repository

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Dataform server.
        """
        return request, metadata

    def pre_delete_team_folder(
        self,
        request: dataform.DeleteTeamFolderRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dataform.DeleteTeamFolderRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_team_folder

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Dataform server.
        """
        return request, metadata

    def pre_delete_team_folder_tree(
        self,
        request: dataform.DeleteTeamFolderTreeRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dataform.DeleteTeamFolderTreeRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_team_folder_tree

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Dataform server.
        """
        return request, metadata

    def post_delete_team_folder_tree(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_team_folder_tree

        DEPRECATED. Please use the `post_delete_team_folder_tree_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Dataform server but before
        it is returned to user code. This `post_delete_team_folder_tree` interceptor runs
        before the `post_delete_team_folder_tree_with_metadata` interceptor.
        """
        return response

    def post_delete_team_folder_tree_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_team_folder_tree

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Dataform server but before it is returned to user code.

        We recommend only using this `post_delete_team_folder_tree_with_metadata`
        interceptor in new development instead of the `post_delete_team_folder_tree` interceptor.
        When both interceptors are used, this `post_delete_team_folder_tree_with_metadata` interceptor runs after the
        `post_delete_team_folder_tree` interceptor. The (possibly modified) response returned by
        `post_delete_team_folder_tree` will be passed to
        `post_delete_team_folder_tree_with_metadata`.
        """
        return response, metadata

    def pre_delete_workflow_config(
        self,
        request: dataform.DeleteWorkflowConfigRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dataform.DeleteWorkflowConfigRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_workflow_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Dataform server.
        """
        return request, metadata

    def pre_delete_workflow_invocation(
        self,
        request: dataform.DeleteWorkflowInvocationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dataform.DeleteWorkflowInvocationRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_workflow_invocation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Dataform server.
        """
        return request, metadata

    def pre_delete_workspace(
        self,
        request: dataform.DeleteWorkspaceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dataform.DeleteWorkspaceRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_workspace

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Dataform server.
        """
        return request, metadata

    def pre_fetch_file_diff(
        self,
        request: dataform.FetchFileDiffRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[dataform.FetchFileDiffRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for fetch_file_diff

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Dataform server.
        """
        return request, metadata

    def post_fetch_file_diff(
        self, response: dataform.FetchFileDiffResponse
    ) -> dataform.FetchFileDiffResponse:
        """Post-rpc interceptor for fetch_file_diff

        DEPRECATED. Please use the `post_fetch_file_diff_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Dataform server but before
        it is returned to user code. This `post_fetch_file_diff` interceptor runs
        before the `post_fetch_file_diff_with_metadata` interceptor.
        """
        return response

    def post_fetch_file_diff_with_metadata(
        self,
        response: dataform.FetchFileDiffResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[dataform.FetchFileDiffResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for fetch_file_diff

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Dataform server but before it is returned to user code.

        We recommend only using this `post_fetch_file_diff_with_metadata`
        interceptor in new development instead of the `post_fetch_file_diff` interceptor.
        When both interceptors are used, this `post_fetch_file_diff_with_metadata` interceptor runs after the
        `post_fetch_file_diff` interceptor. The (possibly modified) response returned by
        `post_fetch_file_diff` will be passed to
        `post_fetch_file_diff_with_metadata`.
        """
        return response, metadata

    def pre_fetch_file_git_statuses(
        self,
        request: dataform.FetchFileGitStatusesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dataform.FetchFileGitStatusesRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for fetch_file_git_statuses

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Dataform server.
        """
        return request, metadata

    def post_fetch_file_git_statuses(
        self, response: dataform.FetchFileGitStatusesResponse
    ) -> dataform.FetchFileGitStatusesResponse:
        """Post-rpc interceptor for fetch_file_git_statuses

        DEPRECATED. Please use the `post_fetch_file_git_statuses_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Dataform server but before
        it is returned to user code. This `post_fetch_file_git_statuses` interceptor runs
        before the `post_fetch_file_git_statuses_with_metadata` interceptor.
        """
        return response

    def post_fetch_file_git_statuses_with_metadata(
        self,
        response: dataform.FetchFileGitStatusesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dataform.FetchFileGitStatusesResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for fetch_file_git_statuses

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Dataform server but before it is returned to user code.

        We recommend only using this `post_fetch_file_git_statuses_with_metadata`
        interceptor in new development instead of the `post_fetch_file_git_statuses` interceptor.
        When both interceptors are used, this `post_fetch_file_git_statuses_with_metadata` interceptor runs after the
        `post_fetch_file_git_statuses` interceptor. The (possibly modified) response returned by
        `post_fetch_file_git_statuses` will be passed to
        `post_fetch_file_git_statuses_with_metadata`.
        """
        return response, metadata

    def pre_fetch_git_ahead_behind(
        self,
        request: dataform.FetchGitAheadBehindRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dataform.FetchGitAheadBehindRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for fetch_git_ahead_behind

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Dataform server.
        """
        return request, metadata

    def post_fetch_git_ahead_behind(
        self, response: dataform.FetchGitAheadBehindResponse
    ) -> dataform.FetchGitAheadBehindResponse:
        """Post-rpc interceptor for fetch_git_ahead_behind

        DEPRECATED. Please use the `post_fetch_git_ahead_behind_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Dataform server but before
        it is returned to user code. This `post_fetch_git_ahead_behind` interceptor runs
        before the `post_fetch_git_ahead_behind_with_metadata` interceptor.
        """
        return response

    def post_fetch_git_ahead_behind_with_metadata(
        self,
        response: dataform.FetchGitAheadBehindResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dataform.FetchGitAheadBehindResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for fetch_git_ahead_behind

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Dataform server but before it is returned to user code.

        We recommend only using this `post_fetch_git_ahead_behind_with_metadata`
        interceptor in new development instead of the `post_fetch_git_ahead_behind` interceptor.
        When both interceptors are used, this `post_fetch_git_ahead_behind_with_metadata` interceptor runs after the
        `post_fetch_git_ahead_behind` interceptor. The (possibly modified) response returned by
        `post_fetch_git_ahead_behind` will be passed to
        `post_fetch_git_ahead_behind_with_metadata`.
        """
        return response, metadata

    def pre_fetch_remote_branches(
        self,
        request: dataform.FetchRemoteBranchesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dataform.FetchRemoteBranchesRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for fetch_remote_branches

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Dataform server.
        """
        return request, metadata

    def post_fetch_remote_branches(
        self, response: dataform.FetchRemoteBranchesResponse
    ) -> dataform.FetchRemoteBranchesResponse:
        """Post-rpc interceptor for fetch_remote_branches

        DEPRECATED. Please use the `post_fetch_remote_branches_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Dataform server but before
        it is returned to user code. This `post_fetch_remote_branches` interceptor runs
        before the `post_fetch_remote_branches_with_metadata` interceptor.
        """
        return response

    def post_fetch_remote_branches_with_metadata(
        self,
        response: dataform.FetchRemoteBranchesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dataform.FetchRemoteBranchesResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for fetch_remote_branches

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Dataform server but before it is returned to user code.

        We recommend only using this `post_fetch_remote_branches_with_metadata`
        interceptor in new development instead of the `post_fetch_remote_branches` interceptor.
        When both interceptors are used, this `post_fetch_remote_branches_with_metadata` interceptor runs after the
        `post_fetch_remote_branches` interceptor. The (possibly modified) response returned by
        `post_fetch_remote_branches` will be passed to
        `post_fetch_remote_branches_with_metadata`.
        """
        return response, metadata

    def pre_fetch_repository_history(
        self,
        request: dataform.FetchRepositoryHistoryRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dataform.FetchRepositoryHistoryRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for fetch_repository_history

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Dataform server.
        """
        return request, metadata

    def post_fetch_repository_history(
        self, response: dataform.FetchRepositoryHistoryResponse
    ) -> dataform.FetchRepositoryHistoryResponse:
        """Post-rpc interceptor for fetch_repository_history

        DEPRECATED. Please use the `post_fetch_repository_history_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Dataform server but before
        it is returned to user code. This `post_fetch_repository_history` interceptor runs
        before the `post_fetch_repository_history_with_metadata` interceptor.
        """
        return response

    def post_fetch_repository_history_with_metadata(
        self,
        response: dataform.FetchRepositoryHistoryResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dataform.FetchRepositoryHistoryResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for fetch_repository_history

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Dataform server but before it is returned to user code.

        We recommend only using this `post_fetch_repository_history_with_metadata`
        interceptor in new development instead of the `post_fetch_repository_history` interceptor.
        When both interceptors are used, this `post_fetch_repository_history_with_metadata` interceptor runs after the
        `post_fetch_repository_history` interceptor. The (possibly modified) response returned by
        `post_fetch_repository_history` will be passed to
        `post_fetch_repository_history_with_metadata`.
        """
        return response, metadata

    def pre_get_compilation_result(
        self,
        request: dataform.GetCompilationResultRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dataform.GetCompilationResultRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_compilation_result

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Dataform server.
        """
        return request, metadata

    def post_get_compilation_result(
        self, response: dataform.CompilationResult
    ) -> dataform.CompilationResult:
        """Post-rpc interceptor for get_compilation_result

        DEPRECATED. Please use the `post_get_compilation_result_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Dataform server but before
        it is returned to user code. This `post_get_compilation_result` interceptor runs
        before the `post_get_compilation_result_with_metadata` interceptor.
        """
        return response

    def post_get_compilation_result_with_metadata(
        self,
        response: dataform.CompilationResult,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[dataform.CompilationResult, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_compilation_result

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Dataform server but before it is returned to user code.

        We recommend only using this `post_get_compilation_result_with_metadata`
        interceptor in new development instead of the `post_get_compilation_result` interceptor.
        When both interceptors are used, this `post_get_compilation_result_with_metadata` interceptor runs after the
        `post_get_compilation_result` interceptor. The (possibly modified) response returned by
        `post_get_compilation_result` will be passed to
        `post_get_compilation_result_with_metadata`.
        """
        return response, metadata

    def pre_get_config(
        self,
        request: dataform.GetConfigRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[dataform.GetConfigRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Dataform server.
        """
        return request, metadata

    def post_get_config(self, response: dataform.Config) -> dataform.Config:
        """Post-rpc interceptor for get_config

        DEPRECATED. Please use the `post_get_config_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Dataform server but before
        it is returned to user code. This `post_get_config` interceptor runs
        before the `post_get_config_with_metadata` interceptor.
        """
        return response

    def post_get_config_with_metadata(
        self,
        response: dataform.Config,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[dataform.Config, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_config

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Dataform server but before it is returned to user code.

        We recommend only using this `post_get_config_with_metadata`
        interceptor in new development instead of the `post_get_config` interceptor.
        When both interceptors are used, this `post_get_config_with_metadata` interceptor runs after the
        `post_get_config` interceptor. The (possibly modified) response returned by
        `post_get_config` will be passed to
        `post_get_config_with_metadata`.
        """
        return response, metadata

    def pre_get_folder(
        self,
        request: dataform.GetFolderRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[dataform.GetFolderRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_folder

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Dataform server.
        """
        return request, metadata

    def post_get_folder(self, response: dataform.Folder) -> dataform.Folder:
        """Post-rpc interceptor for get_folder

        DEPRECATED. Please use the `post_get_folder_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Dataform server but before
        it is returned to user code. This `post_get_folder` interceptor runs
        before the `post_get_folder_with_metadata` interceptor.
        """
        return response

    def post_get_folder_with_metadata(
        self,
        response: dataform.Folder,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[dataform.Folder, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_folder

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Dataform server but before it is returned to user code.

        We recommend only using this `post_get_folder_with_metadata`
        interceptor in new development instead of the `post_get_folder` interceptor.
        When both interceptors are used, this `post_get_folder_with_metadata` interceptor runs after the
        `post_get_folder` interceptor. The (possibly modified) response returned by
        `post_get_folder` will be passed to
        `post_get_folder_with_metadata`.
        """
        return response, metadata

    def pre_get_iam_policy(
        self,
        request: iam_policy_pb2.GetIamPolicyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        iam_policy_pb2.GetIamPolicyRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_iam_policy

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Dataform server.
        """
        return request, metadata

    def post_get_iam_policy(self, response: policy_pb2.Policy) -> policy_pb2.Policy:
        """Post-rpc interceptor for get_iam_policy

        DEPRECATED. Please use the `post_get_iam_policy_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Dataform server but before
        it is returned to user code. This `post_get_iam_policy` interceptor runs
        before the `post_get_iam_policy_with_metadata` interceptor.
        """
        return response

    def post_get_iam_policy_with_metadata(
        self,
        response: policy_pb2.Policy,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[policy_pb2.Policy, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_iam_policy

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Dataform server but before it is returned to user code.

        We recommend only using this `post_get_iam_policy_with_metadata`
        interceptor in new development instead of the `post_get_iam_policy` interceptor.
        When both interceptors are used, this `post_get_iam_policy_with_metadata` interceptor runs after the
        `post_get_iam_policy` interceptor. The (possibly modified) response returned by
        `post_get_iam_policy` will be passed to
        `post_get_iam_policy_with_metadata`.
        """
        return response, metadata

    def pre_get_release_config(
        self,
        request: dataform.GetReleaseConfigRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dataform.GetReleaseConfigRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_release_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Dataform server.
        """
        return request, metadata

    def post_get_release_config(
        self, response: dataform.ReleaseConfig
    ) -> dataform.ReleaseConfig:
        """Post-rpc interceptor for get_release_config

        DEPRECATED. Please use the `post_get_release_config_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Dataform server but before
        it is returned to user code. This `post_get_release_config` interceptor runs
        before the `post_get_release_config_with_metadata` interceptor.
        """
        return response

    def post_get_release_config_with_metadata(
        self,
        response: dataform.ReleaseConfig,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[dataform.ReleaseConfig, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_release_config

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Dataform server but before it is returned to user code.

        We recommend only using this `post_get_release_config_with_metadata`
        interceptor in new development instead of the `post_get_release_config` interceptor.
        When both interceptors are used, this `post_get_release_config_with_metadata` interceptor runs after the
        `post_get_release_config` interceptor. The (possibly modified) response returned by
        `post_get_release_config` will be passed to
        `post_get_release_config_with_metadata`.
        """
        return response, metadata

    def pre_get_repository(
        self,
        request: dataform.GetRepositoryRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[dataform.GetRepositoryRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_repository

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Dataform server.
        """
        return request, metadata

    def post_get_repository(self, response: dataform.Repository) -> dataform.Repository:
        """Post-rpc interceptor for get_repository

        DEPRECATED. Please use the `post_get_repository_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Dataform server but before
        it is returned to user code. This `post_get_repository` interceptor runs
        before the `post_get_repository_with_metadata` interceptor.
        """
        return response

    def post_get_repository_with_metadata(
        self,
        response: dataform.Repository,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[dataform.Repository, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_repository

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Dataform server but before it is returned to user code.

        We recommend only using this `post_get_repository_with_metadata`
        interceptor in new development instead of the `post_get_repository` interceptor.
        When both interceptors are used, this `post_get_repository_with_metadata` interceptor runs after the
        `post_get_repository` interceptor. The (possibly modified) response returned by
        `post_get_repository` will be passed to
        `post_get_repository_with_metadata`.
        """
        return response, metadata

    def pre_get_team_folder(
        self,
        request: dataform.GetTeamFolderRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[dataform.GetTeamFolderRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_team_folder

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Dataform server.
        """
        return request, metadata

    def post_get_team_folder(
        self, response: dataform.TeamFolder
    ) -> dataform.TeamFolder:
        """Post-rpc interceptor for get_team_folder

        DEPRECATED. Please use the `post_get_team_folder_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Dataform server but before
        it is returned to user code. This `post_get_team_folder` interceptor runs
        before the `post_get_team_folder_with_metadata` interceptor.
        """
        return response

    def post_get_team_folder_with_metadata(
        self,
        response: dataform.TeamFolder,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[dataform.TeamFolder, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_team_folder

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Dataform server but before it is returned to user code.

        We recommend only using this `post_get_team_folder_with_metadata`
        interceptor in new development instead of the `post_get_team_folder` interceptor.
        When both interceptors are used, this `post_get_team_folder_with_metadata` interceptor runs after the
        `post_get_team_folder` interceptor. The (possibly modified) response returned by
        `post_get_team_folder` will be passed to
        `post_get_team_folder_with_metadata`.
        """
        return response, metadata

    def pre_get_workflow_config(
        self,
        request: dataform.GetWorkflowConfigRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dataform.GetWorkflowConfigRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_workflow_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Dataform server.
        """
        return request, metadata

    def post_get_workflow_config(
        self, response: dataform.WorkflowConfig
    ) -> dataform.WorkflowConfig:
        """Post-rpc interceptor for get_workflow_config

        DEPRECATED. Please use the `post_get_workflow_config_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Dataform server but before
        it is returned to user code. This `post_get_workflow_config` interceptor runs
        before the `post_get_workflow_config_with_metadata` interceptor.
        """
        return response

    def post_get_workflow_config_with_metadata(
        self,
        response: dataform.WorkflowConfig,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[dataform.WorkflowConfig, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_workflow_config

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Dataform server but before it is returned to user code.

        We recommend only using this `post_get_workflow_config_with_metadata`
        interceptor in new development instead of the `post_get_workflow_config` interceptor.
        When both interceptors are used, this `post_get_workflow_config_with_metadata` interceptor runs after the
        `post_get_workflow_config` interceptor. The (possibly modified) response returned by
        `post_get_workflow_config` will be passed to
        `post_get_workflow_config_with_metadata`.
        """
        return response, metadata

    def pre_get_workflow_invocation(
        self,
        request: dataform.GetWorkflowInvocationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dataform.GetWorkflowInvocationRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_workflow_invocation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Dataform server.
        """
        return request, metadata

    def post_get_workflow_invocation(
        self, response: dataform.WorkflowInvocation
    ) -> dataform.WorkflowInvocation:
        """Post-rpc interceptor for get_workflow_invocation

        DEPRECATED. Please use the `post_get_workflow_invocation_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Dataform server but before
        it is returned to user code. This `post_get_workflow_invocation` interceptor runs
        before the `post_get_workflow_invocation_with_metadata` interceptor.
        """
        return response

    def post_get_workflow_invocation_with_metadata(
        self,
        response: dataform.WorkflowInvocation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[dataform.WorkflowInvocation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_workflow_invocation

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Dataform server but before it is returned to user code.

        We recommend only using this `post_get_workflow_invocation_with_metadata`
        interceptor in new development instead of the `post_get_workflow_invocation` interceptor.
        When both interceptors are used, this `post_get_workflow_invocation_with_metadata` interceptor runs after the
        `post_get_workflow_invocation` interceptor. The (possibly modified) response returned by
        `post_get_workflow_invocation` will be passed to
        `post_get_workflow_invocation_with_metadata`.
        """
        return response, metadata

    def pre_get_workspace(
        self,
        request: dataform.GetWorkspaceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[dataform.GetWorkspaceRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_workspace

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Dataform server.
        """
        return request, metadata

    def post_get_workspace(self, response: dataform.Workspace) -> dataform.Workspace:
        """Post-rpc interceptor for get_workspace

        DEPRECATED. Please use the `post_get_workspace_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Dataform server but before
        it is returned to user code. This `post_get_workspace` interceptor runs
        before the `post_get_workspace_with_metadata` interceptor.
        """
        return response

    def post_get_workspace_with_metadata(
        self,
        response: dataform.Workspace,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[dataform.Workspace, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_workspace

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Dataform server but before it is returned to user code.

        We recommend only using this `post_get_workspace_with_metadata`
        interceptor in new development instead of the `post_get_workspace` interceptor.
        When both interceptors are used, this `post_get_workspace_with_metadata` interceptor runs after the
        `post_get_workspace` interceptor. The (possibly modified) response returned by
        `post_get_workspace` will be passed to
        `post_get_workspace_with_metadata`.
        """
        return response, metadata

    def pre_install_npm_packages(
        self,
        request: dataform.InstallNpmPackagesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dataform.InstallNpmPackagesRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for install_npm_packages

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Dataform server.
        """
        return request, metadata

    def post_install_npm_packages(
        self, response: dataform.InstallNpmPackagesResponse
    ) -> dataform.InstallNpmPackagesResponse:
        """Post-rpc interceptor for install_npm_packages

        DEPRECATED. Please use the `post_install_npm_packages_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Dataform server but before
        it is returned to user code. This `post_install_npm_packages` interceptor runs
        before the `post_install_npm_packages_with_metadata` interceptor.
        """
        return response

    def post_install_npm_packages_with_metadata(
        self,
        response: dataform.InstallNpmPackagesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dataform.InstallNpmPackagesResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for install_npm_packages

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Dataform server but before it is returned to user code.

        We recommend only using this `post_install_npm_packages_with_metadata`
        interceptor in new development instead of the `post_install_npm_packages` interceptor.
        When both interceptors are used, this `post_install_npm_packages_with_metadata` interceptor runs after the
        `post_install_npm_packages` interceptor. The (possibly modified) response returned by
        `post_install_npm_packages` will be passed to
        `post_install_npm_packages_with_metadata`.
        """
        return response, metadata

    def pre_list_compilation_results(
        self,
        request: dataform.ListCompilationResultsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dataform.ListCompilationResultsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_compilation_results

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Dataform server.
        """
        return request, metadata

    def post_list_compilation_results(
        self, response: dataform.ListCompilationResultsResponse
    ) -> dataform.ListCompilationResultsResponse:
        """Post-rpc interceptor for list_compilation_results

        DEPRECATED. Please use the `post_list_compilation_results_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Dataform server but before
        it is returned to user code. This `post_list_compilation_results` interceptor runs
        before the `post_list_compilation_results_with_metadata` interceptor.
        """
        return response

    def post_list_compilation_results_with_metadata(
        self,
        response: dataform.ListCompilationResultsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dataform.ListCompilationResultsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_compilation_results

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Dataform server but before it is returned to user code.

        We recommend only using this `post_list_compilation_results_with_metadata`
        interceptor in new development instead of the `post_list_compilation_results` interceptor.
        When both interceptors are used, this `post_list_compilation_results_with_metadata` interceptor runs after the
        `post_list_compilation_results` interceptor. The (possibly modified) response returned by
        `post_list_compilation_results` will be passed to
        `post_list_compilation_results_with_metadata`.
        """
        return response, metadata

    def pre_list_release_configs(
        self,
        request: dataform.ListReleaseConfigsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dataform.ListReleaseConfigsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_release_configs

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Dataform server.
        """
        return request, metadata

    def post_list_release_configs(
        self, response: dataform.ListReleaseConfigsResponse
    ) -> dataform.ListReleaseConfigsResponse:
        """Post-rpc interceptor for list_release_configs

        DEPRECATED. Please use the `post_list_release_configs_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Dataform server but before
        it is returned to user code. This `post_list_release_configs` interceptor runs
        before the `post_list_release_configs_with_metadata` interceptor.
        """
        return response

    def post_list_release_configs_with_metadata(
        self,
        response: dataform.ListReleaseConfigsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dataform.ListReleaseConfigsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_release_configs

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Dataform server but before it is returned to user code.

        We recommend only using this `post_list_release_configs_with_metadata`
        interceptor in new development instead of the `post_list_release_configs` interceptor.
        When both interceptors are used, this `post_list_release_configs_with_metadata` interceptor runs after the
        `post_list_release_configs` interceptor. The (possibly modified) response returned by
        `post_list_release_configs` will be passed to
        `post_list_release_configs_with_metadata`.
        """
        return response, metadata

    def pre_list_repositories(
        self,
        request: dataform.ListRepositoriesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dataform.ListRepositoriesRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_repositories

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Dataform server.
        """
        return request, metadata

    def post_list_repositories(
        self, response: dataform.ListRepositoriesResponse
    ) -> dataform.ListRepositoriesResponse:
        """Post-rpc interceptor for list_repositories

        DEPRECATED. Please use the `post_list_repositories_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Dataform server but before
        it is returned to user code. This `post_list_repositories` interceptor runs
        before the `post_list_repositories_with_metadata` interceptor.
        """
        return response

    def post_list_repositories_with_metadata(
        self,
        response: dataform.ListRepositoriesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dataform.ListRepositoriesResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_repositories

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Dataform server but before it is returned to user code.

        We recommend only using this `post_list_repositories_with_metadata`
        interceptor in new development instead of the `post_list_repositories` interceptor.
        When both interceptors are used, this `post_list_repositories_with_metadata` interceptor runs after the
        `post_list_repositories` interceptor. The (possibly modified) response returned by
        `post_list_repositories` will be passed to
        `post_list_repositories_with_metadata`.
        """
        return response, metadata

    def pre_list_workflow_configs(
        self,
        request: dataform.ListWorkflowConfigsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dataform.ListWorkflowConfigsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_workflow_configs

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Dataform server.
        """
        return request, metadata

    def post_list_workflow_configs(
        self, response: dataform.ListWorkflowConfigsResponse
    ) -> dataform.ListWorkflowConfigsResponse:
        """Post-rpc interceptor for list_workflow_configs

        DEPRECATED. Please use the `post_list_workflow_configs_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Dataform server but before
        it is returned to user code. This `post_list_workflow_configs` interceptor runs
        before the `post_list_workflow_configs_with_metadata` interceptor.
        """
        return response

    def post_list_workflow_configs_with_metadata(
        self,
        response: dataform.ListWorkflowConfigsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dataform.ListWorkflowConfigsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_workflow_configs

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Dataform server but before it is returned to user code.

        We recommend only using this `post_list_workflow_configs_with_metadata`
        interceptor in new development instead of the `post_list_workflow_configs` interceptor.
        When both interceptors are used, this `post_list_workflow_configs_with_metadata` interceptor runs after the
        `post_list_workflow_configs` interceptor. The (possibly modified) response returned by
        `post_list_workflow_configs` will be passed to
        `post_list_workflow_configs_with_metadata`.
        """
        return response, metadata

    def pre_list_workflow_invocations(
        self,
        request: dataform.ListWorkflowInvocationsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dataform.ListWorkflowInvocationsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_workflow_invocations

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Dataform server.
        """
        return request, metadata

    def post_list_workflow_invocations(
        self, response: dataform.ListWorkflowInvocationsResponse
    ) -> dataform.ListWorkflowInvocationsResponse:
        """Post-rpc interceptor for list_workflow_invocations

        DEPRECATED. Please use the `post_list_workflow_invocations_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Dataform server but before
        it is returned to user code. This `post_list_workflow_invocations` interceptor runs
        before the `post_list_workflow_invocations_with_metadata` interceptor.
        """
        return response

    def post_list_workflow_invocations_with_metadata(
        self,
        response: dataform.ListWorkflowInvocationsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dataform.ListWorkflowInvocationsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_workflow_invocations

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Dataform server but before it is returned to user code.

        We recommend only using this `post_list_workflow_invocations_with_metadata`
        interceptor in new development instead of the `post_list_workflow_invocations` interceptor.
        When both interceptors are used, this `post_list_workflow_invocations_with_metadata` interceptor runs after the
        `post_list_workflow_invocations` interceptor. The (possibly modified) response returned by
        `post_list_workflow_invocations` will be passed to
        `post_list_workflow_invocations_with_metadata`.
        """
        return response, metadata

    def pre_list_workspaces(
        self,
        request: dataform.ListWorkspacesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[dataform.ListWorkspacesRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for list_workspaces

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Dataform server.
        """
        return request, metadata

    def post_list_workspaces(
        self, response: dataform.ListWorkspacesResponse
    ) -> dataform.ListWorkspacesResponse:
        """Post-rpc interceptor for list_workspaces

        DEPRECATED. Please use the `post_list_workspaces_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Dataform server but before
        it is returned to user code. This `post_list_workspaces` interceptor runs
        before the `post_list_workspaces_with_metadata` interceptor.
        """
        return response

    def post_list_workspaces_with_metadata(
        self,
        response: dataform.ListWorkspacesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dataform.ListWorkspacesResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_workspaces

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Dataform server but before it is returned to user code.

        We recommend only using this `post_list_workspaces_with_metadata`
        interceptor in new development instead of the `post_list_workspaces` interceptor.
        When both interceptors are used, this `post_list_workspaces_with_metadata` interceptor runs after the
        `post_list_workspaces` interceptor. The (possibly modified) response returned by
        `post_list_workspaces` will be passed to
        `post_list_workspaces_with_metadata`.
        """
        return response, metadata

    def pre_make_directory(
        self,
        request: dataform.MakeDirectoryRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[dataform.MakeDirectoryRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for make_directory

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Dataform server.
        """
        return request, metadata

    def post_make_directory(
        self, response: dataform.MakeDirectoryResponse
    ) -> dataform.MakeDirectoryResponse:
        """Post-rpc interceptor for make_directory

        DEPRECATED. Please use the `post_make_directory_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Dataform server but before
        it is returned to user code. This `post_make_directory` interceptor runs
        before the `post_make_directory_with_metadata` interceptor.
        """
        return response

    def post_make_directory_with_metadata(
        self,
        response: dataform.MakeDirectoryResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[dataform.MakeDirectoryResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for make_directory

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Dataform server but before it is returned to user code.

        We recommend only using this `post_make_directory_with_metadata`
        interceptor in new development instead of the `post_make_directory` interceptor.
        When both interceptors are used, this `post_make_directory_with_metadata` interceptor runs after the
        `post_make_directory` interceptor. The (possibly modified) response returned by
        `post_make_directory` will be passed to
        `post_make_directory_with_metadata`.
        """
        return response, metadata

    def pre_move_directory(
        self,
        request: dataform.MoveDirectoryRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[dataform.MoveDirectoryRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for move_directory

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Dataform server.
        """
        return request, metadata

    def post_move_directory(
        self, response: dataform.MoveDirectoryResponse
    ) -> dataform.MoveDirectoryResponse:
        """Post-rpc interceptor for move_directory

        DEPRECATED. Please use the `post_move_directory_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Dataform server but before
        it is returned to user code. This `post_move_directory` interceptor runs
        before the `post_move_directory_with_metadata` interceptor.
        """
        return response

    def post_move_directory_with_metadata(
        self,
        response: dataform.MoveDirectoryResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[dataform.MoveDirectoryResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for move_directory

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Dataform server but before it is returned to user code.

        We recommend only using this `post_move_directory_with_metadata`
        interceptor in new development instead of the `post_move_directory` interceptor.
        When both interceptors are used, this `post_move_directory_with_metadata` interceptor runs after the
        `post_move_directory` interceptor. The (possibly modified) response returned by
        `post_move_directory` will be passed to
        `post_move_directory_with_metadata`.
        """
        return response, metadata

    def pre_move_file(
        self,
        request: dataform.MoveFileRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[dataform.MoveFileRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for move_file

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Dataform server.
        """
        return request, metadata

    def post_move_file(
        self, response: dataform.MoveFileResponse
    ) -> dataform.MoveFileResponse:
        """Post-rpc interceptor for move_file

        DEPRECATED. Please use the `post_move_file_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Dataform server but before
        it is returned to user code. This `post_move_file` interceptor runs
        before the `post_move_file_with_metadata` interceptor.
        """
        return response

    def post_move_file_with_metadata(
        self,
        response: dataform.MoveFileResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[dataform.MoveFileResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for move_file

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Dataform server but before it is returned to user code.

        We recommend only using this `post_move_file_with_metadata`
        interceptor in new development instead of the `post_move_file` interceptor.
        When both interceptors are used, this `post_move_file_with_metadata` interceptor runs after the
        `post_move_file` interceptor. The (possibly modified) response returned by
        `post_move_file` will be passed to
        `post_move_file_with_metadata`.
        """
        return response, metadata

    def pre_move_folder(
        self,
        request: dataform.MoveFolderRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[dataform.MoveFolderRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for move_folder

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Dataform server.
        """
        return request, metadata

    def post_move_folder(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for move_folder

        DEPRECATED. Please use the `post_move_folder_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Dataform server but before
        it is returned to user code. This `post_move_folder` interceptor runs
        before the `post_move_folder_with_metadata` interceptor.
        """
        return response

    def post_move_folder_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for move_folder

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Dataform server but before it is returned to user code.

        We recommend only using this `post_move_folder_with_metadata`
        interceptor in new development instead of the `post_move_folder` interceptor.
        When both interceptors are used, this `post_move_folder_with_metadata` interceptor runs after the
        `post_move_folder` interceptor. The (possibly modified) response returned by
        `post_move_folder` will be passed to
        `post_move_folder_with_metadata`.
        """
        return response, metadata

    def pre_move_repository(
        self,
        request: dataform.MoveRepositoryRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[dataform.MoveRepositoryRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for move_repository

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Dataform server.
        """
        return request, metadata

    def post_move_repository(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for move_repository

        DEPRECATED. Please use the `post_move_repository_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Dataform server but before
        it is returned to user code. This `post_move_repository` interceptor runs
        before the `post_move_repository_with_metadata` interceptor.
        """
        return response

    def post_move_repository_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for move_repository

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Dataform server but before it is returned to user code.

        We recommend only using this `post_move_repository_with_metadata`
        interceptor in new development instead of the `post_move_repository` interceptor.
        When both interceptors are used, this `post_move_repository_with_metadata` interceptor runs after the
        `post_move_repository` interceptor. The (possibly modified) response returned by
        `post_move_repository` will be passed to
        `post_move_repository_with_metadata`.
        """
        return response, metadata

    def pre_pull_git_commits(
        self,
        request: dataform.PullGitCommitsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[dataform.PullGitCommitsRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for pull_git_commits

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Dataform server.
        """
        return request, metadata

    def post_pull_git_commits(
        self, response: dataform.PullGitCommitsResponse
    ) -> dataform.PullGitCommitsResponse:
        """Post-rpc interceptor for pull_git_commits

        DEPRECATED. Please use the `post_pull_git_commits_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Dataform server but before
        it is returned to user code. This `post_pull_git_commits` interceptor runs
        before the `post_pull_git_commits_with_metadata` interceptor.
        """
        return response

    def post_pull_git_commits_with_metadata(
        self,
        response: dataform.PullGitCommitsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dataform.PullGitCommitsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for pull_git_commits

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Dataform server but before it is returned to user code.

        We recommend only using this `post_pull_git_commits_with_metadata`
        interceptor in new development instead of the `post_pull_git_commits` interceptor.
        When both interceptors are used, this `post_pull_git_commits_with_metadata` interceptor runs after the
        `post_pull_git_commits` interceptor. The (possibly modified) response returned by
        `post_pull_git_commits` will be passed to
        `post_pull_git_commits_with_metadata`.
        """
        return response, metadata

    def pre_push_git_commits(
        self,
        request: dataform.PushGitCommitsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[dataform.PushGitCommitsRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for push_git_commits

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Dataform server.
        """
        return request, metadata

    def post_push_git_commits(
        self, response: dataform.PushGitCommitsResponse
    ) -> dataform.PushGitCommitsResponse:
        """Post-rpc interceptor for push_git_commits

        DEPRECATED. Please use the `post_push_git_commits_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Dataform server but before
        it is returned to user code. This `post_push_git_commits` interceptor runs
        before the `post_push_git_commits_with_metadata` interceptor.
        """
        return response

    def post_push_git_commits_with_metadata(
        self,
        response: dataform.PushGitCommitsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dataform.PushGitCommitsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for push_git_commits

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Dataform server but before it is returned to user code.

        We recommend only using this `post_push_git_commits_with_metadata`
        interceptor in new development instead of the `post_push_git_commits` interceptor.
        When both interceptors are used, this `post_push_git_commits_with_metadata` interceptor runs after the
        `post_push_git_commits` interceptor. The (possibly modified) response returned by
        `post_push_git_commits` will be passed to
        `post_push_git_commits_with_metadata`.
        """
        return response, metadata

    def pre_query_compilation_result_actions(
        self,
        request: dataform.QueryCompilationResultActionsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dataform.QueryCompilationResultActionsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for query_compilation_result_actions

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Dataform server.
        """
        return request, metadata

    def post_query_compilation_result_actions(
        self, response: dataform.QueryCompilationResultActionsResponse
    ) -> dataform.QueryCompilationResultActionsResponse:
        """Post-rpc interceptor for query_compilation_result_actions

        DEPRECATED. Please use the `post_query_compilation_result_actions_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Dataform server but before
        it is returned to user code. This `post_query_compilation_result_actions` interceptor runs
        before the `post_query_compilation_result_actions_with_metadata` interceptor.
        """
        return response

    def post_query_compilation_result_actions_with_metadata(
        self,
        response: dataform.QueryCompilationResultActionsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dataform.QueryCompilationResultActionsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for query_compilation_result_actions

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Dataform server but before it is returned to user code.

        We recommend only using this `post_query_compilation_result_actions_with_metadata`
        interceptor in new development instead of the `post_query_compilation_result_actions` interceptor.
        When both interceptors are used, this `post_query_compilation_result_actions_with_metadata` interceptor runs after the
        `post_query_compilation_result_actions` interceptor. The (possibly modified) response returned by
        `post_query_compilation_result_actions` will be passed to
        `post_query_compilation_result_actions_with_metadata`.
        """
        return response, metadata

    def pre_query_directory_contents(
        self,
        request: dataform.QueryDirectoryContentsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dataform.QueryDirectoryContentsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for query_directory_contents

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Dataform server.
        """
        return request, metadata

    def post_query_directory_contents(
        self, response: dataform.QueryDirectoryContentsResponse
    ) -> dataform.QueryDirectoryContentsResponse:
        """Post-rpc interceptor for query_directory_contents

        DEPRECATED. Please use the `post_query_directory_contents_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Dataform server but before
        it is returned to user code. This `post_query_directory_contents` interceptor runs
        before the `post_query_directory_contents_with_metadata` interceptor.
        """
        return response

    def post_query_directory_contents_with_metadata(
        self,
        response: dataform.QueryDirectoryContentsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dataform.QueryDirectoryContentsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for query_directory_contents

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Dataform server but before it is returned to user code.

        We recommend only using this `post_query_directory_contents_with_metadata`
        interceptor in new development instead of the `post_query_directory_contents` interceptor.
        When both interceptors are used, this `post_query_directory_contents_with_metadata` interceptor runs after the
        `post_query_directory_contents` interceptor. The (possibly modified) response returned by
        `post_query_directory_contents` will be passed to
        `post_query_directory_contents_with_metadata`.
        """
        return response, metadata

    def pre_query_folder_contents(
        self,
        request: dataform.QueryFolderContentsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dataform.QueryFolderContentsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for query_folder_contents

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Dataform server.
        """
        return request, metadata

    def post_query_folder_contents(
        self, response: dataform.QueryFolderContentsResponse
    ) -> dataform.QueryFolderContentsResponse:
        """Post-rpc interceptor for query_folder_contents

        DEPRECATED. Please use the `post_query_folder_contents_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Dataform server but before
        it is returned to user code. This `post_query_folder_contents` interceptor runs
        before the `post_query_folder_contents_with_metadata` interceptor.
        """
        return response

    def post_query_folder_contents_with_metadata(
        self,
        response: dataform.QueryFolderContentsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dataform.QueryFolderContentsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for query_folder_contents

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Dataform server but before it is returned to user code.

        We recommend only using this `post_query_folder_contents_with_metadata`
        interceptor in new development instead of the `post_query_folder_contents` interceptor.
        When both interceptors are used, this `post_query_folder_contents_with_metadata` interceptor runs after the
        `post_query_folder_contents` interceptor. The (possibly modified) response returned by
        `post_query_folder_contents` will be passed to
        `post_query_folder_contents_with_metadata`.
        """
        return response, metadata

    def pre_query_repository_directory_contents(
        self,
        request: dataform.QueryRepositoryDirectoryContentsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dataform.QueryRepositoryDirectoryContentsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for query_repository_directory_contents

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Dataform server.
        """
        return request, metadata

    def post_query_repository_directory_contents(
        self, response: dataform.QueryRepositoryDirectoryContentsResponse
    ) -> dataform.QueryRepositoryDirectoryContentsResponse:
        """Post-rpc interceptor for query_repository_directory_contents

        DEPRECATED. Please use the `post_query_repository_directory_contents_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Dataform server but before
        it is returned to user code. This `post_query_repository_directory_contents` interceptor runs
        before the `post_query_repository_directory_contents_with_metadata` interceptor.
        """
        return response

    def post_query_repository_directory_contents_with_metadata(
        self,
        response: dataform.QueryRepositoryDirectoryContentsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dataform.QueryRepositoryDirectoryContentsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for query_repository_directory_contents

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Dataform server but before it is returned to user code.

        We recommend only using this `post_query_repository_directory_contents_with_metadata`
        interceptor in new development instead of the `post_query_repository_directory_contents` interceptor.
        When both interceptors are used, this `post_query_repository_directory_contents_with_metadata` interceptor runs after the
        `post_query_repository_directory_contents` interceptor. The (possibly modified) response returned by
        `post_query_repository_directory_contents` will be passed to
        `post_query_repository_directory_contents_with_metadata`.
        """
        return response, metadata

    def pre_query_team_folder_contents(
        self,
        request: dataform.QueryTeamFolderContentsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dataform.QueryTeamFolderContentsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for query_team_folder_contents

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Dataform server.
        """
        return request, metadata

    def post_query_team_folder_contents(
        self, response: dataform.QueryTeamFolderContentsResponse
    ) -> dataform.QueryTeamFolderContentsResponse:
        """Post-rpc interceptor for query_team_folder_contents

        DEPRECATED. Please use the `post_query_team_folder_contents_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Dataform server but before
        it is returned to user code. This `post_query_team_folder_contents` interceptor runs
        before the `post_query_team_folder_contents_with_metadata` interceptor.
        """
        return response

    def post_query_team_folder_contents_with_metadata(
        self,
        response: dataform.QueryTeamFolderContentsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dataform.QueryTeamFolderContentsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for query_team_folder_contents

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Dataform server but before it is returned to user code.

        We recommend only using this `post_query_team_folder_contents_with_metadata`
        interceptor in new development instead of the `post_query_team_folder_contents` interceptor.
        When both interceptors are used, this `post_query_team_folder_contents_with_metadata` interceptor runs after the
        `post_query_team_folder_contents` interceptor. The (possibly modified) response returned by
        `post_query_team_folder_contents` will be passed to
        `post_query_team_folder_contents_with_metadata`.
        """
        return response, metadata

    def pre_query_user_root_contents(
        self,
        request: dataform.QueryUserRootContentsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dataform.QueryUserRootContentsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for query_user_root_contents

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Dataform server.
        """
        return request, metadata

    def post_query_user_root_contents(
        self, response: dataform.QueryUserRootContentsResponse
    ) -> dataform.QueryUserRootContentsResponse:
        """Post-rpc interceptor for query_user_root_contents

        DEPRECATED. Please use the `post_query_user_root_contents_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Dataform server but before
        it is returned to user code. This `post_query_user_root_contents` interceptor runs
        before the `post_query_user_root_contents_with_metadata` interceptor.
        """
        return response

    def post_query_user_root_contents_with_metadata(
        self,
        response: dataform.QueryUserRootContentsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dataform.QueryUserRootContentsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for query_user_root_contents

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Dataform server but before it is returned to user code.

        We recommend only using this `post_query_user_root_contents_with_metadata`
        interceptor in new development instead of the `post_query_user_root_contents` interceptor.
        When both interceptors are used, this `post_query_user_root_contents_with_metadata` interceptor runs after the
        `post_query_user_root_contents` interceptor. The (possibly modified) response returned by
        `post_query_user_root_contents` will be passed to
        `post_query_user_root_contents_with_metadata`.
        """
        return response, metadata

    def pre_query_workflow_invocation_actions(
        self,
        request: dataform.QueryWorkflowInvocationActionsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dataform.QueryWorkflowInvocationActionsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for query_workflow_invocation_actions

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Dataform server.
        """
        return request, metadata

    def post_query_workflow_invocation_actions(
        self, response: dataform.QueryWorkflowInvocationActionsResponse
    ) -> dataform.QueryWorkflowInvocationActionsResponse:
        """Post-rpc interceptor for query_workflow_invocation_actions

        DEPRECATED. Please use the `post_query_workflow_invocation_actions_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Dataform server but before
        it is returned to user code. This `post_query_workflow_invocation_actions` interceptor runs
        before the `post_query_workflow_invocation_actions_with_metadata` interceptor.
        """
        return response

    def post_query_workflow_invocation_actions_with_metadata(
        self,
        response: dataform.QueryWorkflowInvocationActionsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dataform.QueryWorkflowInvocationActionsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for query_workflow_invocation_actions

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Dataform server but before it is returned to user code.

        We recommend only using this `post_query_workflow_invocation_actions_with_metadata`
        interceptor in new development instead of the `post_query_workflow_invocation_actions` interceptor.
        When both interceptors are used, this `post_query_workflow_invocation_actions_with_metadata` interceptor runs after the
        `post_query_workflow_invocation_actions` interceptor. The (possibly modified) response returned by
        `post_query_workflow_invocation_actions` will be passed to
        `post_query_workflow_invocation_actions_with_metadata`.
        """
        return response, metadata

    def pre_read_file(
        self,
        request: dataform.ReadFileRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[dataform.ReadFileRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for read_file

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Dataform server.
        """
        return request, metadata

    def post_read_file(
        self, response: dataform.ReadFileResponse
    ) -> dataform.ReadFileResponse:
        """Post-rpc interceptor for read_file

        DEPRECATED. Please use the `post_read_file_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Dataform server but before
        it is returned to user code. This `post_read_file` interceptor runs
        before the `post_read_file_with_metadata` interceptor.
        """
        return response

    def post_read_file_with_metadata(
        self,
        response: dataform.ReadFileResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[dataform.ReadFileResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for read_file

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Dataform server but before it is returned to user code.

        We recommend only using this `post_read_file_with_metadata`
        interceptor in new development instead of the `post_read_file` interceptor.
        When both interceptors are used, this `post_read_file_with_metadata` interceptor runs after the
        `post_read_file` interceptor. The (possibly modified) response returned by
        `post_read_file` will be passed to
        `post_read_file_with_metadata`.
        """
        return response, metadata

    def pre_read_repository_file(
        self,
        request: dataform.ReadRepositoryFileRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dataform.ReadRepositoryFileRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for read_repository_file

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Dataform server.
        """
        return request, metadata

    def post_read_repository_file(
        self, response: dataform.ReadRepositoryFileResponse
    ) -> dataform.ReadRepositoryFileResponse:
        """Post-rpc interceptor for read_repository_file

        DEPRECATED. Please use the `post_read_repository_file_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Dataform server but before
        it is returned to user code. This `post_read_repository_file` interceptor runs
        before the `post_read_repository_file_with_metadata` interceptor.
        """
        return response

    def post_read_repository_file_with_metadata(
        self,
        response: dataform.ReadRepositoryFileResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dataform.ReadRepositoryFileResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for read_repository_file

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Dataform server but before it is returned to user code.

        We recommend only using this `post_read_repository_file_with_metadata`
        interceptor in new development instead of the `post_read_repository_file` interceptor.
        When both interceptors are used, this `post_read_repository_file_with_metadata` interceptor runs after the
        `post_read_repository_file` interceptor. The (possibly modified) response returned by
        `post_read_repository_file` will be passed to
        `post_read_repository_file_with_metadata`.
        """
        return response, metadata

    def pre_remove_directory(
        self,
        request: dataform.RemoveDirectoryRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dataform.RemoveDirectoryRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for remove_directory

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Dataform server.
        """
        return request, metadata

    def post_remove_directory(
        self, response: dataform.RemoveDirectoryResponse
    ) -> dataform.RemoveDirectoryResponse:
        """Post-rpc interceptor for remove_directory

        DEPRECATED. Please use the `post_remove_directory_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Dataform server but before
        it is returned to user code. This `post_remove_directory` interceptor runs
        before the `post_remove_directory_with_metadata` interceptor.
        """
        return response

    def post_remove_directory_with_metadata(
        self,
        response: dataform.RemoveDirectoryResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dataform.RemoveDirectoryResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for remove_directory

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Dataform server but before it is returned to user code.

        We recommend only using this `post_remove_directory_with_metadata`
        interceptor in new development instead of the `post_remove_directory` interceptor.
        When both interceptors are used, this `post_remove_directory_with_metadata` interceptor runs after the
        `post_remove_directory` interceptor. The (possibly modified) response returned by
        `post_remove_directory` will be passed to
        `post_remove_directory_with_metadata`.
        """
        return response, metadata

    def pre_remove_file(
        self,
        request: dataform.RemoveFileRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[dataform.RemoveFileRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for remove_file

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Dataform server.
        """
        return request, metadata

    def post_remove_file(
        self, response: dataform.RemoveFileResponse
    ) -> dataform.RemoveFileResponse:
        """Post-rpc interceptor for remove_file

        DEPRECATED. Please use the `post_remove_file_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Dataform server but before
        it is returned to user code. This `post_remove_file` interceptor runs
        before the `post_remove_file_with_metadata` interceptor.
        """
        return response

    def post_remove_file_with_metadata(
        self,
        response: dataform.RemoveFileResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[dataform.RemoveFileResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for remove_file

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Dataform server but before it is returned to user code.

        We recommend only using this `post_remove_file_with_metadata`
        interceptor in new development instead of the `post_remove_file` interceptor.
        When both interceptors are used, this `post_remove_file_with_metadata` interceptor runs after the
        `post_remove_file` interceptor. The (possibly modified) response returned by
        `post_remove_file` will be passed to
        `post_remove_file_with_metadata`.
        """
        return response, metadata

    def pre_reset_workspace_changes(
        self,
        request: dataform.ResetWorkspaceChangesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dataform.ResetWorkspaceChangesRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for reset_workspace_changes

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Dataform server.
        """
        return request, metadata

    def post_reset_workspace_changes(
        self, response: dataform.ResetWorkspaceChangesResponse
    ) -> dataform.ResetWorkspaceChangesResponse:
        """Post-rpc interceptor for reset_workspace_changes

        DEPRECATED. Please use the `post_reset_workspace_changes_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Dataform server but before
        it is returned to user code. This `post_reset_workspace_changes` interceptor runs
        before the `post_reset_workspace_changes_with_metadata` interceptor.
        """
        return response

    def post_reset_workspace_changes_with_metadata(
        self,
        response: dataform.ResetWorkspaceChangesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dataform.ResetWorkspaceChangesResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for reset_workspace_changes

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Dataform server but before it is returned to user code.

        We recommend only using this `post_reset_workspace_changes_with_metadata`
        interceptor in new development instead of the `post_reset_workspace_changes` interceptor.
        When both interceptors are used, this `post_reset_workspace_changes_with_metadata` interceptor runs after the
        `post_reset_workspace_changes` interceptor. The (possibly modified) response returned by
        `post_reset_workspace_changes` will be passed to
        `post_reset_workspace_changes_with_metadata`.
        """
        return response, metadata

    def pre_search_files(
        self,
        request: dataform.SearchFilesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[dataform.SearchFilesRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for search_files

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Dataform server.
        """
        return request, metadata

    def post_search_files(
        self, response: dataform.SearchFilesResponse
    ) -> dataform.SearchFilesResponse:
        """Post-rpc interceptor for search_files

        DEPRECATED. Please use the `post_search_files_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Dataform server but before
        it is returned to user code. This `post_search_files` interceptor runs
        before the `post_search_files_with_metadata` interceptor.
        """
        return response

    def post_search_files_with_metadata(
        self,
        response: dataform.SearchFilesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[dataform.SearchFilesResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for search_files

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Dataform server but before it is returned to user code.

        We recommend only using this `post_search_files_with_metadata`
        interceptor in new development instead of the `post_search_files` interceptor.
        When both interceptors are used, this `post_search_files_with_metadata` interceptor runs after the
        `post_search_files` interceptor. The (possibly modified) response returned by
        `post_search_files` will be passed to
        `post_search_files_with_metadata`.
        """
        return response, metadata

    def pre_search_team_folders(
        self,
        request: dataform.SearchTeamFoldersRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dataform.SearchTeamFoldersRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for search_team_folders

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Dataform server.
        """
        return request, metadata

    def post_search_team_folders(
        self, response: dataform.SearchTeamFoldersResponse
    ) -> dataform.SearchTeamFoldersResponse:
        """Post-rpc interceptor for search_team_folders

        DEPRECATED. Please use the `post_search_team_folders_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Dataform server but before
        it is returned to user code. This `post_search_team_folders` interceptor runs
        before the `post_search_team_folders_with_metadata` interceptor.
        """
        return response

    def post_search_team_folders_with_metadata(
        self,
        response: dataform.SearchTeamFoldersResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dataform.SearchTeamFoldersResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for search_team_folders

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Dataform server but before it is returned to user code.

        We recommend only using this `post_search_team_folders_with_metadata`
        interceptor in new development instead of the `post_search_team_folders` interceptor.
        When both interceptors are used, this `post_search_team_folders_with_metadata` interceptor runs after the
        `post_search_team_folders` interceptor. The (possibly modified) response returned by
        `post_search_team_folders` will be passed to
        `post_search_team_folders_with_metadata`.
        """
        return response, metadata

    def pre_set_iam_policy(
        self,
        request: iam_policy_pb2.SetIamPolicyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        iam_policy_pb2.SetIamPolicyRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for set_iam_policy

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Dataform server.
        """
        return request, metadata

    def post_set_iam_policy(self, response: policy_pb2.Policy) -> policy_pb2.Policy:
        """Post-rpc interceptor for set_iam_policy

        DEPRECATED. Please use the `post_set_iam_policy_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Dataform server but before
        it is returned to user code. This `post_set_iam_policy` interceptor runs
        before the `post_set_iam_policy_with_metadata` interceptor.
        """
        return response

    def post_set_iam_policy_with_metadata(
        self,
        response: policy_pb2.Policy,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[policy_pb2.Policy, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for set_iam_policy

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Dataform server but before it is returned to user code.

        We recommend only using this `post_set_iam_policy_with_metadata`
        interceptor in new development instead of the `post_set_iam_policy` interceptor.
        When both interceptors are used, this `post_set_iam_policy_with_metadata` interceptor runs after the
        `post_set_iam_policy` interceptor. The (possibly modified) response returned by
        `post_set_iam_policy` will be passed to
        `post_set_iam_policy_with_metadata`.
        """
        return response, metadata

    def pre_test_iam_permissions(
        self,
        request: iam_policy_pb2.TestIamPermissionsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        iam_policy_pb2.TestIamPermissionsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for test_iam_permissions

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Dataform server.
        """
        return request, metadata

    def post_test_iam_permissions(
        self, response: iam_policy_pb2.TestIamPermissionsResponse
    ) -> iam_policy_pb2.TestIamPermissionsResponse:
        """Post-rpc interceptor for test_iam_permissions

        DEPRECATED. Please use the `post_test_iam_permissions_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Dataform server but before
        it is returned to user code. This `post_test_iam_permissions` interceptor runs
        before the `post_test_iam_permissions_with_metadata` interceptor.
        """
        return response

    def post_test_iam_permissions_with_metadata(
        self,
        response: iam_policy_pb2.TestIamPermissionsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        iam_policy_pb2.TestIamPermissionsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for test_iam_permissions

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Dataform server but before it is returned to user code.

        We recommend only using this `post_test_iam_permissions_with_metadata`
        interceptor in new development instead of the `post_test_iam_permissions` interceptor.
        When both interceptors are used, this `post_test_iam_permissions_with_metadata` interceptor runs after the
        `post_test_iam_permissions` interceptor. The (possibly modified) response returned by
        `post_test_iam_permissions` will be passed to
        `post_test_iam_permissions_with_metadata`.
        """
        return response, metadata

    def pre_update_config(
        self,
        request: dataform.UpdateConfigRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[dataform.UpdateConfigRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for update_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Dataform server.
        """
        return request, metadata

    def post_update_config(self, response: dataform.Config) -> dataform.Config:
        """Post-rpc interceptor for update_config

        DEPRECATED. Please use the `post_update_config_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Dataform server but before
        it is returned to user code. This `post_update_config` interceptor runs
        before the `post_update_config_with_metadata` interceptor.
        """
        return response

    def post_update_config_with_metadata(
        self,
        response: dataform.Config,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[dataform.Config, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_config

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Dataform server but before it is returned to user code.

        We recommend only using this `post_update_config_with_metadata`
        interceptor in new development instead of the `post_update_config` interceptor.
        When both interceptors are used, this `post_update_config_with_metadata` interceptor runs after the
        `post_update_config` interceptor. The (possibly modified) response returned by
        `post_update_config` will be passed to
        `post_update_config_with_metadata`.
        """
        return response, metadata

    def pre_update_folder(
        self,
        request: dataform.UpdateFolderRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[dataform.UpdateFolderRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for update_folder

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Dataform server.
        """
        return request, metadata

    def post_update_folder(self, response: dataform.Folder) -> dataform.Folder:
        """Post-rpc interceptor for update_folder

        DEPRECATED. Please use the `post_update_folder_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Dataform server but before
        it is returned to user code. This `post_update_folder` interceptor runs
        before the `post_update_folder_with_metadata` interceptor.
        """
        return response

    def post_update_folder_with_metadata(
        self,
        response: dataform.Folder,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[dataform.Folder, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_folder

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Dataform server but before it is returned to user code.

        We recommend only using this `post_update_folder_with_metadata`
        interceptor in new development instead of the `post_update_folder` interceptor.
        When both interceptors are used, this `post_update_folder_with_metadata` interceptor runs after the
        `post_update_folder` interceptor. The (possibly modified) response returned by
        `post_update_folder` will be passed to
        `post_update_folder_with_metadata`.
        """
        return response, metadata

    def pre_update_release_config(
        self,
        request: dataform.UpdateReleaseConfigRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dataform.UpdateReleaseConfigRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_release_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Dataform server.
        """
        return request, metadata

    def post_update_release_config(
        self, response: dataform.ReleaseConfig
    ) -> dataform.ReleaseConfig:
        """Post-rpc interceptor for update_release_config

        DEPRECATED. Please use the `post_update_release_config_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Dataform server but before
        it is returned to user code. This `post_update_release_config` interceptor runs
        before the `post_update_release_config_with_metadata` interceptor.
        """
        return response

    def post_update_release_config_with_metadata(
        self,
        response: dataform.ReleaseConfig,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[dataform.ReleaseConfig, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_release_config

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Dataform server but before it is returned to user code.

        We recommend only using this `post_update_release_config_with_metadata`
        interceptor in new development instead of the `post_update_release_config` interceptor.
        When both interceptors are used, this `post_update_release_config_with_metadata` interceptor runs after the
        `post_update_release_config` interceptor. The (possibly modified) response returned by
        `post_update_release_config` will be passed to
        `post_update_release_config_with_metadata`.
        """
        return response, metadata

    def pre_update_repository(
        self,
        request: dataform.UpdateRepositoryRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dataform.UpdateRepositoryRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_repository

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Dataform server.
        """
        return request, metadata

    def post_update_repository(
        self, response: dataform.Repository
    ) -> dataform.Repository:
        """Post-rpc interceptor for update_repository

        DEPRECATED. Please use the `post_update_repository_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Dataform server but before
        it is returned to user code. This `post_update_repository` interceptor runs
        before the `post_update_repository_with_metadata` interceptor.
        """
        return response

    def post_update_repository_with_metadata(
        self,
        response: dataform.Repository,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[dataform.Repository, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_repository

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Dataform server but before it is returned to user code.

        We recommend only using this `post_update_repository_with_metadata`
        interceptor in new development instead of the `post_update_repository` interceptor.
        When both interceptors are used, this `post_update_repository_with_metadata` interceptor runs after the
        `post_update_repository` interceptor. The (possibly modified) response returned by
        `post_update_repository` will be passed to
        `post_update_repository_with_metadata`.
        """
        return response, metadata

    def pre_update_team_folder(
        self,
        request: dataform.UpdateTeamFolderRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dataform.UpdateTeamFolderRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_team_folder

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Dataform server.
        """
        return request, metadata

    def post_update_team_folder(
        self, response: dataform.TeamFolder
    ) -> dataform.TeamFolder:
        """Post-rpc interceptor for update_team_folder

        DEPRECATED. Please use the `post_update_team_folder_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Dataform server but before
        it is returned to user code. This `post_update_team_folder` interceptor runs
        before the `post_update_team_folder_with_metadata` interceptor.
        """
        return response

    def post_update_team_folder_with_metadata(
        self,
        response: dataform.TeamFolder,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[dataform.TeamFolder, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_team_folder

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Dataform server but before it is returned to user code.

        We recommend only using this `post_update_team_folder_with_metadata`
        interceptor in new development instead of the `post_update_team_folder` interceptor.
        When both interceptors are used, this `post_update_team_folder_with_metadata` interceptor runs after the
        `post_update_team_folder` interceptor. The (possibly modified) response returned by
        `post_update_team_folder` will be passed to
        `post_update_team_folder_with_metadata`.
        """
        return response, metadata

    def pre_update_workflow_config(
        self,
        request: dataform.UpdateWorkflowConfigRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dataform.UpdateWorkflowConfigRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_workflow_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Dataform server.
        """
        return request, metadata

    def post_update_workflow_config(
        self, response: dataform.WorkflowConfig
    ) -> dataform.WorkflowConfig:
        """Post-rpc interceptor for update_workflow_config

        DEPRECATED. Please use the `post_update_workflow_config_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Dataform server but before
        it is returned to user code. This `post_update_workflow_config` interceptor runs
        before the `post_update_workflow_config_with_metadata` interceptor.
        """
        return response

    def post_update_workflow_config_with_metadata(
        self,
        response: dataform.WorkflowConfig,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[dataform.WorkflowConfig, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_workflow_config

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Dataform server but before it is returned to user code.

        We recommend only using this `post_update_workflow_config_with_metadata`
        interceptor in new development instead of the `post_update_workflow_config` interceptor.
        When both interceptors are used, this `post_update_workflow_config_with_metadata` interceptor runs after the
        `post_update_workflow_config` interceptor. The (possibly modified) response returned by
        `post_update_workflow_config` will be passed to
        `post_update_workflow_config_with_metadata`.
        """
        return response, metadata

    def pre_write_file(
        self,
        request: dataform.WriteFileRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[dataform.WriteFileRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for write_file

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Dataform server.
        """
        return request, metadata

    def post_write_file(
        self, response: dataform.WriteFileResponse
    ) -> dataform.WriteFileResponse:
        """Post-rpc interceptor for write_file

        DEPRECATED. Please use the `post_write_file_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Dataform server but before
        it is returned to user code. This `post_write_file` interceptor runs
        before the `post_write_file_with_metadata` interceptor.
        """
        return response

    def post_write_file_with_metadata(
        self,
        response: dataform.WriteFileResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[dataform.WriteFileResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for write_file

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Dataform server but before it is returned to user code.

        We recommend only using this `post_write_file_with_metadata`
        interceptor in new development instead of the `post_write_file` interceptor.
        When both interceptors are used, this `post_write_file_with_metadata` interceptor runs after the
        `post_write_file` interceptor. The (possibly modified) response returned by
        `post_write_file` will be passed to
        `post_write_file_with_metadata`.
        """
        return response, metadata

    def pre_get_location(
        self,
        request: locations_pb2.GetLocationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        locations_pb2.GetLocationRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_location

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Dataform server.
        """
        return request, metadata

    def post_get_location(
        self, response: locations_pb2.Location
    ) -> locations_pb2.Location:
        """Post-rpc interceptor for get_location

        Override in a subclass to manipulate the response
        after it is returned by the Dataform server but before
        it is returned to user code.
        """
        return response

    def pre_list_locations(
        self,
        request: locations_pb2.ListLocationsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        locations_pb2.ListLocationsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_locations

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Dataform server.
        """
        return request, metadata

    def post_list_locations(
        self, response: locations_pb2.ListLocationsResponse
    ) -> locations_pb2.ListLocationsResponse:
        """Post-rpc interceptor for list_locations

        Override in a subclass to manipulate the response
        after it is returned by the Dataform server but before
        it is returned to user code.
        """
        return response

    def pre_cancel_operation(
        self,
        request: operations_pb2.CancelOperationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        operations_pb2.CancelOperationRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Dataform server.
        """
        return request, metadata

    def post_cancel_operation(self, response: None) -> None:
        """Post-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the response
        after it is returned by the Dataform server but before
        it is returned to user code.
        """
        return response

    def pre_delete_operation(
        self,
        request: operations_pb2.DeleteOperationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        operations_pb2.DeleteOperationRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_operation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Dataform server.
        """
        return request, metadata

    def post_delete_operation(self, response: None) -> None:
        """Post-rpc interceptor for delete_operation

        Override in a subclass to manipulate the response
        after it is returned by the Dataform server but before
        it is returned to user code.
        """
        return response

    def pre_get_operation(
        self,
        request: operations_pb2.GetOperationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        operations_pb2.GetOperationRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_operation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Dataform server.
        """
        return request, metadata

    def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the Dataform server but before
        it is returned to user code.
        """
        return response

    def pre_list_operations(
        self,
        request: operations_pb2.ListOperationsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        operations_pb2.ListOperationsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_operations

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Dataform server.
        """
        return request, metadata

    def post_list_operations(
        self, response: operations_pb2.ListOperationsResponse
    ) -> operations_pb2.ListOperationsResponse:
        """Post-rpc interceptor for list_operations

        Override in a subclass to manipulate the response
        after it is returned by the Dataform server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class DataformRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: DataformRestInterceptor


class DataformRestTransport(_BaseDataformRestTransport):
    """REST backend synchronous transport for Dataform.

    Dataform is a service to develop, create, document, test, and
    update curated tables in BigQuery.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "dataform.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[DataformRestInterceptor] = None,
        api_audience: Optional[str] = None,
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
                This argument is ignored if ``channel`` is provided. This argument will be
                removed in the next major version of this library.
            scopes (Optional(Sequence[str])): A list of scopes. This argument is
                ignored if ``channel`` is provided.
            client_cert_source_for_mtls (Callable[[], Tuple[bytes, bytes]]): Client
                certificate to configure mutual TLS HTTP channel. It is ignored
                if ``channel`` is provided.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you are developing
                your own client library.
            always_use_jwt_access (Optional[bool]): Whether self signed JWT should
                be used for service account credentials.
            url_scheme: the protocol scheme for the API endpoint.  Normally
                "https", but for testing or local servers,
                "http" can be specified.
            interceptor (Optional[DataformRestInterceptor]): Interceptor used
                to manipulate requests, request metadata, and responses.
            api_audience (Optional[str]): The intended audience for the API calls
                to the service that will be set when using certain 3rd party
                authentication flows. Audience is typically a resource identifier.
                If not set, the host value will be used as a default.
        """
        # Run the base constructor
        # TODO(yon-mg): resolve other ctor params i.e. scopes, quota, etc.
        # TODO: When custom host (api_endpoint) is set, `scopes` must *also* be set on the
        # credentials object
        super().__init__(
            host=host,
            credentials=credentials,
            client_info=client_info,
            always_use_jwt_access=always_use_jwt_access,
            url_scheme=url_scheme,
            api_audience=api_audience,
        )
        self._session = AuthorizedSession(
            self._credentials, default_host=self.DEFAULT_HOST
        )
        self._operations_client: Optional[operations_v1.AbstractOperationsClient] = None
        if client_cert_source_for_mtls:
            self._session.configure_mtls_channel(client_cert_source_for_mtls)
        self._interceptor = interceptor or DataformRestInterceptor()
        self._prep_wrapped_messages(client_info)

    @property
    def operations_client(self) -> operations_v1.AbstractOperationsClient:
        """Create the client designed to process long-running operations.

        This property caches on the instance; repeated calls return the same
        client.
        """
        # Only create a new client if we do not already have one.
        if self._operations_client is None:
            http_options: Dict[str, List[Dict[str, str]]] = {
                "google.longrunning.Operations.CancelOperation": [
                    {
                        "method": "post",
                        "uri": "/v1/{name=projects/*/locations/*/operations/*}:cancel",
                        "body": "*",
                    },
                ],
                "google.longrunning.Operations.DeleteOperation": [
                    {
                        "method": "delete",
                        "uri": "/v1/{name=projects/*/locations/*/operations/*}",
                    },
                ],
                "google.longrunning.Operations.GetOperation": [
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/operations/*}",
                    },
                ],
                "google.longrunning.Operations.ListOperations": [
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*}/operations",
                    },
                ],
            }

            rest_transport = operations_v1.OperationsRestTransport(
                host=self._host,
                # use the credentials which are saved
                credentials=self._credentials,
                scopes=self._scopes,
                http_options=http_options,
                path_prefix="v1",
            )

            self._operations_client = operations_v1.AbstractOperationsClient(
                transport=rest_transport
            )

        # Return the client from cache.
        return self._operations_client

    class _CancelWorkflowInvocation(
        _BaseDataformRestTransport._BaseCancelWorkflowInvocation, DataformRestStub
    ):
        def __hash__(self):
            return hash("DataformRestTransport.CancelWorkflowInvocation")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )
            return response

        def __call__(
            self,
            request: dataform.CancelWorkflowInvocationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> dataform.CancelWorkflowInvocationResponse:
            r"""Call the cancel workflow
            invocation method over HTTP.

                Args:
                    request (~.dataform.CancelWorkflowInvocationRequest):
                        The request object. ``CancelWorkflowInvocation`` request message.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.dataform.CancelWorkflowInvocationResponse:
                        ``CancelWorkflowInvocation`` response message.
            """

            http_options = _BaseDataformRestTransport._BaseCancelWorkflowInvocation._get_http_options()
            request, metadata = self._interceptor.pre_cancel_workflow_invocation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataformRestTransport._BaseCancelWorkflowInvocation,
                    "_BaseCancelWorkflowInvocation__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.dataform_v1.DataformClient.CancelWorkflowInvocation",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "CancelWorkflowInvocation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DataformRestTransport._CancelWorkflowInvocation._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = dataform.CancelWorkflowInvocationResponse()
            pb_resp = dataform.CancelWorkflowInvocationResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_cancel_workflow_invocation(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_cancel_workflow_invocation_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        dataform.CancelWorkflowInvocationResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.dataform_v1.DataformClient.cancel_workflow_invocation",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "CancelWorkflowInvocation",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CommitRepositoryChanges(
        _BaseDataformRestTransport._BaseCommitRepositoryChanges, DataformRestStub
    ):
        def __hash__(self):
            return hash("DataformRestTransport.CommitRepositoryChanges")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )
            return response

        def __call__(
            self,
            request: dataform.CommitRepositoryChangesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> dataform.CommitRepositoryChangesResponse:
            r"""Call the commit repository changes method over HTTP.

            Args:
                request (~.dataform.CommitRepositoryChangesRequest):
                    The request object. ``CommitRepositoryChanges`` request message.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.dataform.CommitRepositoryChangesResponse:
                    ``CommitRepositoryChanges`` response message.
            """

            http_options = _BaseDataformRestTransport._BaseCommitRepositoryChanges._get_http_options()
            request, metadata = self._interceptor.pre_commit_repository_changes(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataformRestTransport._BaseCommitRepositoryChanges,
                    "_BaseCommitRepositoryChanges__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.dataform_v1.DataformClient.CommitRepositoryChanges",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "CommitRepositoryChanges",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DataformRestTransport._CommitRepositoryChanges._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = dataform.CommitRepositoryChangesResponse()
            pb_resp = dataform.CommitRepositoryChangesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_commit_repository_changes(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_commit_repository_changes_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = dataform.CommitRepositoryChangesResponse.to_json(
                        response
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.dataform_v1.DataformClient.commit_repository_changes",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "CommitRepositoryChanges",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CommitWorkspaceChanges(
        _BaseDataformRestTransport._BaseCommitWorkspaceChanges, DataformRestStub
    ):
        def __hash__(self):
            return hash("DataformRestTransport.CommitWorkspaceChanges")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )
            return response

        def __call__(
            self,
            request: dataform.CommitWorkspaceChangesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> dataform.CommitWorkspaceChangesResponse:
            r"""Call the commit workspace changes method over HTTP.

            Args:
                request (~.dataform.CommitWorkspaceChangesRequest):
                    The request object. ``CommitWorkspaceChanges`` request message.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.dataform.CommitWorkspaceChangesResponse:
                    ``CommitWorkspaceChanges`` response message.
            """

            http_options = _BaseDataformRestTransport._BaseCommitWorkspaceChanges._get_http_options()
            request, metadata = self._interceptor.pre_commit_workspace_changes(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataformRestTransport._BaseCommitWorkspaceChanges,
                    "_BaseCommitWorkspaceChanges__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.dataform_v1.DataformClient.CommitWorkspaceChanges",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "CommitWorkspaceChanges",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DataformRestTransport._CommitWorkspaceChanges._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = dataform.CommitWorkspaceChangesResponse()
            pb_resp = dataform.CommitWorkspaceChangesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_commit_workspace_changes(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_commit_workspace_changes_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = dataform.CommitWorkspaceChangesResponse.to_json(
                        response
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.dataform_v1.DataformClient.commit_workspace_changes",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "CommitWorkspaceChanges",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ComputeRepositoryAccessTokenStatus(
        _BaseDataformRestTransport._BaseComputeRepositoryAccessTokenStatus,
        DataformRestStub,
    ):
        def __hash__(self):
            return hash("DataformRestTransport.ComputeRepositoryAccessTokenStatus")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: dataform.ComputeRepositoryAccessTokenStatusRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> dataform.ComputeRepositoryAccessTokenStatusResponse:
            r"""Call the compute repository access
            token status method over HTTP.

                Args:
                    request (~.dataform.ComputeRepositoryAccessTokenStatusRequest):
                        The request object. ``ComputeRepositoryAccessTokenStatus`` request message.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.dataform.ComputeRepositoryAccessTokenStatusResponse:
                        ``ComputeRepositoryAccessTokenStatus`` response message.
            """

            http_options = _BaseDataformRestTransport._BaseComputeRepositoryAccessTokenStatus._get_http_options()
            request, metadata = (
                self._interceptor.pre_compute_repository_access_token_status(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataformRestTransport._BaseComputeRepositoryAccessTokenStatus,
                    "_BaseComputeRepositoryAccessTokenStatus__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.dataform_v1.DataformClient.ComputeRepositoryAccessTokenStatus",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "ComputeRepositoryAccessTokenStatus",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                DataformRestTransport._ComputeRepositoryAccessTokenStatus._get_response(
                    self._host,
                    metadata,
                    query_params,
                    self._session,
                    timeout,
                    transcoded_request,
                )
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = dataform.ComputeRepositoryAccessTokenStatusResponse()
            pb_resp = dataform.ComputeRepositoryAccessTokenStatusResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_compute_repository_access_token_status(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_compute_repository_access_token_status_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        dataform.ComputeRepositoryAccessTokenStatusResponse.to_json(
                            response
                        )
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.dataform_v1.DataformClient.compute_repository_access_token_status",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "ComputeRepositoryAccessTokenStatus",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateCompilationResult(
        _BaseDataformRestTransport._BaseCreateCompilationResult, DataformRestStub
    ):
        def __hash__(self):
            return hash("DataformRestTransport.CreateCompilationResult")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )
            return response

        def __call__(
            self,
            request: dataform.CreateCompilationResultRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> dataform.CompilationResult:
            r"""Call the create compilation result method over HTTP.

            Args:
                request (~.dataform.CreateCompilationResultRequest):
                    The request object. ``CreateCompilationResult`` request message.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.dataform.CompilationResult:
                    Represents the result of compiling a
                Dataform project.

            """

            http_options = _BaseDataformRestTransport._BaseCreateCompilationResult._get_http_options()
            request, metadata = self._interceptor.pre_create_compilation_result(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataformRestTransport._BaseCreateCompilationResult,
                    "_BaseCreateCompilationResult__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.dataform_v1.DataformClient.CreateCompilationResult",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "CreateCompilationResult",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DataformRestTransport._CreateCompilationResult._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = dataform.CompilationResult()
            pb_resp = dataform.CompilationResult.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_compilation_result(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_compilation_result_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = dataform.CompilationResult.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.dataform_v1.DataformClient.create_compilation_result",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "CreateCompilationResult",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateFolder(_BaseDataformRestTransport._BaseCreateFolder, DataformRestStub):
        def __hash__(self):
            return hash("DataformRestTransport.CreateFolder")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )
            return response

        def __call__(
            self,
            request: dataform.CreateFolderRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> dataform.Folder:
            r"""Call the create folder method over HTTP.

            Args:
                request (~.dataform.CreateFolderRequest):
                    The request object. ``CreateFolder`` request message.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.dataform.Folder:
                    Represents a Dataform Folder. This is
                a resource that is used to organize
                Files and other Folders and provide
                hierarchical access controls.

            """

            http_options = (
                _BaseDataformRestTransport._BaseCreateFolder._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_folder(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataformRestTransport._BaseCreateFolder,
                    "_BaseCreateFolder__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.dataform_v1.DataformClient.CreateFolder",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "CreateFolder",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DataformRestTransport._CreateFolder._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = dataform.Folder()
            pb_resp = dataform.Folder.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_folder(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_folder_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = dataform.Folder.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.dataform_v1.DataformClient.create_folder",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "CreateFolder",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateReleaseConfig(
        _BaseDataformRestTransport._BaseCreateReleaseConfig, DataformRestStub
    ):
        def __hash__(self):
            return hash("DataformRestTransport.CreateReleaseConfig")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )
            return response

        def __call__(
            self,
            request: dataform.CreateReleaseConfigRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> dataform.ReleaseConfig:
            r"""Call the create release config method over HTTP.

            Args:
                request (~.dataform.CreateReleaseConfigRequest):
                    The request object. ``CreateReleaseConfig`` request message.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.dataform.ReleaseConfig:
                    Represents a Dataform release
                configuration.

            """

            http_options = (
                _BaseDataformRestTransport._BaseCreateReleaseConfig._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_release_config(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataformRestTransport._BaseCreateReleaseConfig,
                    "_BaseCreateReleaseConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.dataform_v1.DataformClient.CreateReleaseConfig",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "CreateReleaseConfig",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DataformRestTransport._CreateReleaseConfig._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = dataform.ReleaseConfig()
            pb_resp = dataform.ReleaseConfig.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_release_config(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_release_config_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = dataform.ReleaseConfig.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.dataform_v1.DataformClient.create_release_config",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "CreateReleaseConfig",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateRepository(
        _BaseDataformRestTransport._BaseCreateRepository, DataformRestStub
    ):
        def __hash__(self):
            return hash("DataformRestTransport.CreateRepository")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )
            return response

        def __call__(
            self,
            request: dataform.CreateRepositoryRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> dataform.Repository:
            r"""Call the create repository method over HTTP.

            Args:
                request (~.dataform.CreateRepositoryRequest):
                    The request object. ``CreateRepository`` request message.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.dataform.Repository:
                    Represents a Dataform Git repository.
            """

            http_options = (
                _BaseDataformRestTransport._BaseCreateRepository._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_repository(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataformRestTransport._BaseCreateRepository,
                    "_BaseCreateRepository__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.dataform_v1.DataformClient.CreateRepository",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "CreateRepository",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DataformRestTransport._CreateRepository._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = dataform.Repository()
            pb_resp = dataform.Repository.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_repository(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_repository_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = dataform.Repository.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.dataform_v1.DataformClient.create_repository",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "CreateRepository",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateTeamFolder(
        _BaseDataformRestTransport._BaseCreateTeamFolder, DataformRestStub
    ):
        def __hash__(self):
            return hash("DataformRestTransport.CreateTeamFolder")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )
            return response

        def __call__(
            self,
            request: dataform.CreateTeamFolderRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> dataform.TeamFolder:
            r"""Call the create team folder method over HTTP.

            Args:
                request (~.dataform.CreateTeamFolderRequest):
                    The request object. ``CreateTeamFolder`` request message.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.dataform.TeamFolder:
                    Represents a Dataform TeamFolder.
                This is a resource that sits at the
                project level and is used to organize
                Repositories and Folders with
                hierarchical access controls. They
                provide a team context and stricter
                access controls.

            """

            http_options = (
                _BaseDataformRestTransport._BaseCreateTeamFolder._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_team_folder(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataformRestTransport._BaseCreateTeamFolder,
                    "_BaseCreateTeamFolder__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.dataform_v1.DataformClient.CreateTeamFolder",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "CreateTeamFolder",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DataformRestTransport._CreateTeamFolder._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = dataform.TeamFolder()
            pb_resp = dataform.TeamFolder.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_team_folder(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_team_folder_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = dataform.TeamFolder.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.dataform_v1.DataformClient.create_team_folder",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "CreateTeamFolder",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateWorkflowConfig(
        _BaseDataformRestTransport._BaseCreateWorkflowConfig, DataformRestStub
    ):
        def __hash__(self):
            return hash("DataformRestTransport.CreateWorkflowConfig")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )
            return response

        def __call__(
            self,
            request: dataform.CreateWorkflowConfigRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> dataform.WorkflowConfig:
            r"""Call the create workflow config method over HTTP.

            Args:
                request (~.dataform.CreateWorkflowConfigRequest):
                    The request object. ``CreateWorkflowConfig`` request message.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.dataform.WorkflowConfig:
                    Represents a Dataform workflow
                configuration.

            """

            http_options = (
                _BaseDataformRestTransport._BaseCreateWorkflowConfig._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_workflow_config(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataformRestTransport._BaseCreateWorkflowConfig,
                    "_BaseCreateWorkflowConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.dataform_v1.DataformClient.CreateWorkflowConfig",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "CreateWorkflowConfig",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DataformRestTransport._CreateWorkflowConfig._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = dataform.WorkflowConfig()
            pb_resp = dataform.WorkflowConfig.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_workflow_config(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_workflow_config_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = dataform.WorkflowConfig.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.dataform_v1.DataformClient.create_workflow_config",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "CreateWorkflowConfig",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateWorkflowInvocation(
        _BaseDataformRestTransport._BaseCreateWorkflowInvocation, DataformRestStub
    ):
        def __hash__(self):
            return hash("DataformRestTransport.CreateWorkflowInvocation")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )
            return response

        def __call__(
            self,
            request: dataform.CreateWorkflowInvocationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> dataform.WorkflowInvocation:
            r"""Call the create workflow
            invocation method over HTTP.

                Args:
                    request (~.dataform.CreateWorkflowInvocationRequest):
                        The request object. ``CreateWorkflowInvocation`` request message.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.dataform.WorkflowInvocation:
                        Represents a single invocation of a
                    compilation result.

            """

            http_options = _BaseDataformRestTransport._BaseCreateWorkflowInvocation._get_http_options()
            request, metadata = self._interceptor.pre_create_workflow_invocation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataformRestTransport._BaseCreateWorkflowInvocation,
                    "_BaseCreateWorkflowInvocation__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.dataform_v1.DataformClient.CreateWorkflowInvocation",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "CreateWorkflowInvocation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DataformRestTransport._CreateWorkflowInvocation._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = dataform.WorkflowInvocation()
            pb_resp = dataform.WorkflowInvocation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_workflow_invocation(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_workflow_invocation_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = dataform.WorkflowInvocation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.dataform_v1.DataformClient.create_workflow_invocation",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "CreateWorkflowInvocation",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateWorkspace(
        _BaseDataformRestTransport._BaseCreateWorkspace, DataformRestStub
    ):
        def __hash__(self):
            return hash("DataformRestTransport.CreateWorkspace")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )
            return response

        def __call__(
            self,
            request: dataform.CreateWorkspaceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> dataform.Workspace:
            r"""Call the create workspace method over HTTP.

            Args:
                request (~.dataform.CreateWorkspaceRequest):
                    The request object. ``CreateWorkspace`` request message.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.dataform.Workspace:
                    Represents a Dataform Git workspace.
            """

            http_options = (
                _BaseDataformRestTransport._BaseCreateWorkspace._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_workspace(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataformRestTransport._BaseCreateWorkspace,
                    "_BaseCreateWorkspace__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.dataform_v1.DataformClient.CreateWorkspace",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "CreateWorkspace",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DataformRestTransport._CreateWorkspace._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = dataform.Workspace()
            pb_resp = dataform.Workspace.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_workspace(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_workspace_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = dataform.Workspace.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.dataform_v1.DataformClient.create_workspace",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "CreateWorkspace",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteFolder(_BaseDataformRestTransport._BaseDeleteFolder, DataformRestStub):
        def __hash__(self):
            return hash("DataformRestTransport.DeleteFolder")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: dataform.DeleteFolderRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete folder method over HTTP.

            Args:
                request (~.dataform.DeleteFolderRequest):
                    The request object. ``DeleteFolder`` request message.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = (
                _BaseDataformRestTransport._BaseDeleteFolder._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_folder(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataformRestTransport._BaseDeleteFolder,
                    "_BaseDeleteFolder__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.dataform_v1.DataformClient.DeleteFolder",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "DeleteFolder",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DataformRestTransport._DeleteFolder._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

    class _DeleteFolderTree(
        _BaseDataformRestTransport._BaseDeleteFolderTree, DataformRestStub
    ):
        def __hash__(self):
            return hash("DataformRestTransport.DeleteFolderTree")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )
            return response

        def __call__(
            self,
            request: dataform.DeleteFolderTreeRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete folder tree method over HTTP.

            Args:
                request (~.dataform.DeleteFolderTreeRequest):
                    The request object. ``DeleteFolderTree`` request message.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.operations_pb2.Operation:
                    This resource represents a
                long-running operation that is the
                result of a network API call.

            """

            http_options = (
                _BaseDataformRestTransport._BaseDeleteFolderTree._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_folder_tree(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataformRestTransport._BaseDeleteFolderTree,
                    "_BaseDeleteFolderTree__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.dataform_v1.DataformClient.DeleteFolderTree",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "DeleteFolderTree",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DataformRestTransport._DeleteFolderTree._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_delete_folder_tree(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_folder_tree_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = json_format.MessageToJson(resp)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.dataform_v1.DataformClient.delete_folder_tree",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "DeleteFolderTree",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteReleaseConfig(
        _BaseDataformRestTransport._BaseDeleteReleaseConfig, DataformRestStub
    ):
        def __hash__(self):
            return hash("DataformRestTransport.DeleteReleaseConfig")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: dataform.DeleteReleaseConfigRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete release config method over HTTP.

            Args:
                request (~.dataform.DeleteReleaseConfigRequest):
                    The request object. ``DeleteReleaseConfig`` request message.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = (
                _BaseDataformRestTransport._BaseDeleteReleaseConfig._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_release_config(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataformRestTransport._BaseDeleteReleaseConfig,
                    "_BaseDeleteReleaseConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.dataform_v1.DataformClient.DeleteReleaseConfig",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "DeleteReleaseConfig",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DataformRestTransport._DeleteReleaseConfig._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

    class _DeleteRepository(
        _BaseDataformRestTransport._BaseDeleteRepository, DataformRestStub
    ):
        def __hash__(self):
            return hash("DataformRestTransport.DeleteRepository")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: dataform.DeleteRepositoryRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete repository method over HTTP.

            Args:
                request (~.dataform.DeleteRepositoryRequest):
                    The request object. ``DeleteRepository`` request message.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = (
                _BaseDataformRestTransport._BaseDeleteRepository._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_repository(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataformRestTransport._BaseDeleteRepository,
                    "_BaseDeleteRepository__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.dataform_v1.DataformClient.DeleteRepository",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "DeleteRepository",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DataformRestTransport._DeleteRepository._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

    class _DeleteTeamFolder(
        _BaseDataformRestTransport._BaseDeleteTeamFolder, DataformRestStub
    ):
        def __hash__(self):
            return hash("DataformRestTransport.DeleteTeamFolder")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: dataform.DeleteTeamFolderRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete team folder method over HTTP.

            Args:
                request (~.dataform.DeleteTeamFolderRequest):
                    The request object. ``DeleteTeamFolder`` request message.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = (
                _BaseDataformRestTransport._BaseDeleteTeamFolder._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_team_folder(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataformRestTransport._BaseDeleteTeamFolder,
                    "_BaseDeleteTeamFolder__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.dataform_v1.DataformClient.DeleteTeamFolder",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "DeleteTeamFolder",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DataformRestTransport._DeleteTeamFolder._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

    class _DeleteTeamFolderTree(
        _BaseDataformRestTransport._BaseDeleteTeamFolderTree, DataformRestStub
    ):
        def __hash__(self):
            return hash("DataformRestTransport.DeleteTeamFolderTree")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )
            return response

        def __call__(
            self,
            request: dataform.DeleteTeamFolderTreeRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete team folder tree method over HTTP.

            Args:
                request (~.dataform.DeleteTeamFolderTreeRequest):
                    The request object. ``DeleteTeamFolderTree`` request message.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.operations_pb2.Operation:
                    This resource represents a
                long-running operation that is the
                result of a network API call.

            """

            http_options = (
                _BaseDataformRestTransport._BaseDeleteTeamFolderTree._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_team_folder_tree(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataformRestTransport._BaseDeleteTeamFolderTree,
                    "_BaseDeleteTeamFolderTree__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.dataform_v1.DataformClient.DeleteTeamFolderTree",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "DeleteTeamFolderTree",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DataformRestTransport._DeleteTeamFolderTree._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_delete_team_folder_tree(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_team_folder_tree_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = json_format.MessageToJson(resp)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.dataform_v1.DataformClient.delete_team_folder_tree",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "DeleteTeamFolderTree",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteWorkflowConfig(
        _BaseDataformRestTransport._BaseDeleteWorkflowConfig, DataformRestStub
    ):
        def __hash__(self):
            return hash("DataformRestTransport.DeleteWorkflowConfig")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: dataform.DeleteWorkflowConfigRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete workflow config method over HTTP.

            Args:
                request (~.dataform.DeleteWorkflowConfigRequest):
                    The request object. ``DeleteWorkflowConfig`` request message.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = (
                _BaseDataformRestTransport._BaseDeleteWorkflowConfig._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_workflow_config(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataformRestTransport._BaseDeleteWorkflowConfig,
                    "_BaseDeleteWorkflowConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.dataform_v1.DataformClient.DeleteWorkflowConfig",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "DeleteWorkflowConfig",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DataformRestTransport._DeleteWorkflowConfig._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

    class _DeleteWorkflowInvocation(
        _BaseDataformRestTransport._BaseDeleteWorkflowInvocation, DataformRestStub
    ):
        def __hash__(self):
            return hash("DataformRestTransport.DeleteWorkflowInvocation")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: dataform.DeleteWorkflowInvocationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete workflow
            invocation method over HTTP.

                Args:
                    request (~.dataform.DeleteWorkflowInvocationRequest):
                        The request object. ``DeleteWorkflowInvocation`` request message.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.
            """

            http_options = _BaseDataformRestTransport._BaseDeleteWorkflowInvocation._get_http_options()
            request, metadata = self._interceptor.pre_delete_workflow_invocation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataformRestTransport._BaseDeleteWorkflowInvocation,
                    "_BaseDeleteWorkflowInvocation__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.dataform_v1.DataformClient.DeleteWorkflowInvocation",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "DeleteWorkflowInvocation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DataformRestTransport._DeleteWorkflowInvocation._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

    class _DeleteWorkspace(
        _BaseDataformRestTransport._BaseDeleteWorkspace, DataformRestStub
    ):
        def __hash__(self):
            return hash("DataformRestTransport.DeleteWorkspace")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: dataform.DeleteWorkspaceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete workspace method over HTTP.

            Args:
                request (~.dataform.DeleteWorkspaceRequest):
                    The request object. ``DeleteWorkspace`` request message.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = (
                _BaseDataformRestTransport._BaseDeleteWorkspace._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_workspace(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataformRestTransport._BaseDeleteWorkspace,
                    "_BaseDeleteWorkspace__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.dataform_v1.DataformClient.DeleteWorkspace",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "DeleteWorkspace",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DataformRestTransport._DeleteWorkspace._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

    class _FetchFileDiff(
        _BaseDataformRestTransport._BaseFetchFileDiff, DataformRestStub
    ):
        def __hash__(self):
            return hash("DataformRestTransport.FetchFileDiff")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: dataform.FetchFileDiffRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> dataform.FetchFileDiffResponse:
            r"""Call the fetch file diff method over HTTP.

            Args:
                request (~.dataform.FetchFileDiffRequest):
                    The request object. ``FetchFileDiff`` request message.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.dataform.FetchFileDiffResponse:
                    ``FetchFileDiff`` response message.
            """

            http_options = (
                _BaseDataformRestTransport._BaseFetchFileDiff._get_http_options()
            )
            request, metadata = self._interceptor.pre_fetch_file_diff(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataformRestTransport._BaseFetchFileDiff,
                    "_BaseFetchFileDiff__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.dataform_v1.DataformClient.FetchFileDiff",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "FetchFileDiff",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DataformRestTransport._FetchFileDiff._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = dataform.FetchFileDiffResponse()
            pb_resp = dataform.FetchFileDiffResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_fetch_file_diff(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_fetch_file_diff_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = dataform.FetchFileDiffResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.dataform_v1.DataformClient.fetch_file_diff",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "FetchFileDiff",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _FetchFileGitStatuses(
        _BaseDataformRestTransport._BaseFetchFileGitStatuses, DataformRestStub
    ):
        def __hash__(self):
            return hash("DataformRestTransport.FetchFileGitStatuses")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: dataform.FetchFileGitStatusesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> dataform.FetchFileGitStatusesResponse:
            r"""Call the fetch file git statuses method over HTTP.

            Args:
                request (~.dataform.FetchFileGitStatusesRequest):
                    The request object. ``FetchFileGitStatuses`` request message.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.dataform.FetchFileGitStatusesResponse:
                    ``FetchFileGitStatuses`` response message.
            """

            http_options = (
                _BaseDataformRestTransport._BaseFetchFileGitStatuses._get_http_options()
            )
            request, metadata = self._interceptor.pre_fetch_file_git_statuses(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataformRestTransport._BaseFetchFileGitStatuses,
                    "_BaseFetchFileGitStatuses__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.dataform_v1.DataformClient.FetchFileGitStatuses",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "FetchFileGitStatuses",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DataformRestTransport._FetchFileGitStatuses._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = dataform.FetchFileGitStatusesResponse()
            pb_resp = dataform.FetchFileGitStatusesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_fetch_file_git_statuses(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_fetch_file_git_statuses_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = dataform.FetchFileGitStatusesResponse.to_json(
                        response
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.dataform_v1.DataformClient.fetch_file_git_statuses",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "FetchFileGitStatuses",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _FetchGitAheadBehind(
        _BaseDataformRestTransport._BaseFetchGitAheadBehind, DataformRestStub
    ):
        def __hash__(self):
            return hash("DataformRestTransport.FetchGitAheadBehind")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: dataform.FetchGitAheadBehindRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> dataform.FetchGitAheadBehindResponse:
            r"""Call the fetch git ahead behind method over HTTP.

            Args:
                request (~.dataform.FetchGitAheadBehindRequest):
                    The request object. ``FetchGitAheadBehind`` request message.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.dataform.FetchGitAheadBehindResponse:
                    ``FetchGitAheadBehind`` response message.
            """

            http_options = (
                _BaseDataformRestTransport._BaseFetchGitAheadBehind._get_http_options()
            )
            request, metadata = self._interceptor.pre_fetch_git_ahead_behind(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataformRestTransport._BaseFetchGitAheadBehind,
                    "_BaseFetchGitAheadBehind__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.dataform_v1.DataformClient.FetchGitAheadBehind",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "FetchGitAheadBehind",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DataformRestTransport._FetchGitAheadBehind._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = dataform.FetchGitAheadBehindResponse()
            pb_resp = dataform.FetchGitAheadBehindResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_fetch_git_ahead_behind(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_fetch_git_ahead_behind_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = dataform.FetchGitAheadBehindResponse.to_json(
                        response
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.dataform_v1.DataformClient.fetch_git_ahead_behind",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "FetchGitAheadBehind",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _FetchRemoteBranches(
        _BaseDataformRestTransport._BaseFetchRemoteBranches, DataformRestStub
    ):
        def __hash__(self):
            return hash("DataformRestTransport.FetchRemoteBranches")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: dataform.FetchRemoteBranchesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> dataform.FetchRemoteBranchesResponse:
            r"""Call the fetch remote branches method over HTTP.

            Args:
                request (~.dataform.FetchRemoteBranchesRequest):
                    The request object. ``FetchRemoteBranches`` request message.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.dataform.FetchRemoteBranchesResponse:
                    ``FetchRemoteBranches`` response message.
            """

            http_options = (
                _BaseDataformRestTransport._BaseFetchRemoteBranches._get_http_options()
            )
            request, metadata = self._interceptor.pre_fetch_remote_branches(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataformRestTransport._BaseFetchRemoteBranches,
                    "_BaseFetchRemoteBranches__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.dataform_v1.DataformClient.FetchRemoteBranches",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "FetchRemoteBranches",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DataformRestTransport._FetchRemoteBranches._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = dataform.FetchRemoteBranchesResponse()
            pb_resp = dataform.FetchRemoteBranchesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_fetch_remote_branches(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_fetch_remote_branches_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = dataform.FetchRemoteBranchesResponse.to_json(
                        response
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.dataform_v1.DataformClient.fetch_remote_branches",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "FetchRemoteBranches",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _FetchRepositoryHistory(
        _BaseDataformRestTransport._BaseFetchRepositoryHistory, DataformRestStub
    ):
        def __hash__(self):
            return hash("DataformRestTransport.FetchRepositoryHistory")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: dataform.FetchRepositoryHistoryRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> dataform.FetchRepositoryHistoryResponse:
            r"""Call the fetch repository history method over HTTP.

            Args:
                request (~.dataform.FetchRepositoryHistoryRequest):
                    The request object. ``FetchRepositoryHistory`` request message.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.dataform.FetchRepositoryHistoryResponse:
                    ``FetchRepositoryHistory`` response message.
            """

            http_options = _BaseDataformRestTransport._BaseFetchRepositoryHistory._get_http_options()
            request, metadata = self._interceptor.pre_fetch_repository_history(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataformRestTransport._BaseFetchRepositoryHistory,
                    "_BaseFetchRepositoryHistory__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.dataform_v1.DataformClient.FetchRepositoryHistory",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "FetchRepositoryHistory",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DataformRestTransport._FetchRepositoryHistory._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = dataform.FetchRepositoryHistoryResponse()
            pb_resp = dataform.FetchRepositoryHistoryResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_fetch_repository_history(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_fetch_repository_history_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = dataform.FetchRepositoryHistoryResponse.to_json(
                        response
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.dataform_v1.DataformClient.fetch_repository_history",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "FetchRepositoryHistory",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetCompilationResult(
        _BaseDataformRestTransport._BaseGetCompilationResult, DataformRestStub
    ):
        def __hash__(self):
            return hash("DataformRestTransport.GetCompilationResult")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: dataform.GetCompilationResultRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> dataform.CompilationResult:
            r"""Call the get compilation result method over HTTP.

            Args:
                request (~.dataform.GetCompilationResultRequest):
                    The request object. ``GetCompilationResult`` request message.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.dataform.CompilationResult:
                    Represents the result of compiling a
                Dataform project.

            """

            http_options = (
                _BaseDataformRestTransport._BaseGetCompilationResult._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_compilation_result(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataformRestTransport._BaseGetCompilationResult,
                    "_BaseGetCompilationResult__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.dataform_v1.DataformClient.GetCompilationResult",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "GetCompilationResult",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DataformRestTransport._GetCompilationResult._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = dataform.CompilationResult()
            pb_resp = dataform.CompilationResult.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_compilation_result(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_compilation_result_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = dataform.CompilationResult.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.dataform_v1.DataformClient.get_compilation_result",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "GetCompilationResult",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetConfig(_BaseDataformRestTransport._BaseGetConfig, DataformRestStub):
        def __hash__(self):
            return hash("DataformRestTransport.GetConfig")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: dataform.GetConfigRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> dataform.Config:
            r"""Call the get config method over HTTP.

            Args:
                request (~.dataform.GetConfigRequest):
                    The request object. ``GetConfig`` request message.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.dataform.Config:
                    Config for all repositories in a
                given project and location.

            """

            http_options = _BaseDataformRestTransport._BaseGetConfig._get_http_options()
            request, metadata = self._interceptor.pre_get_config(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataformRestTransport._BaseGetConfig,
                    "_BaseGetConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.dataform_v1.DataformClient.GetConfig",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "GetConfig",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DataformRestTransport._GetConfig._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = dataform.Config()
            pb_resp = dataform.Config.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_config(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_config_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = dataform.Config.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.dataform_v1.DataformClient.get_config",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "GetConfig",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetFolder(_BaseDataformRestTransport._BaseGetFolder, DataformRestStub):
        def __hash__(self):
            return hash("DataformRestTransport.GetFolder")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: dataform.GetFolderRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> dataform.Folder:
            r"""Call the get folder method over HTTP.

            Args:
                request (~.dataform.GetFolderRequest):
                    The request object. ``GetFolder`` request message.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.dataform.Folder:
                    Represents a Dataform Folder. This is
                a resource that is used to organize
                Files and other Folders and provide
                hierarchical access controls.

            """

            http_options = _BaseDataformRestTransport._BaseGetFolder._get_http_options()
            request, metadata = self._interceptor.pre_get_folder(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataformRestTransport._BaseGetFolder,
                    "_BaseGetFolder__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.dataform_v1.DataformClient.GetFolder",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "GetFolder",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DataformRestTransport._GetFolder._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = dataform.Folder()
            pb_resp = dataform.Folder.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_folder(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_folder_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = dataform.Folder.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.dataform_v1.DataformClient.get_folder",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "GetFolder",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetIamPolicy(_BaseDataformRestTransport._BaseGetIamPolicy, DataformRestStub):
        def __hash__(self):
            return hash("DataformRestTransport.GetIamPolicy")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: iam_policy_pb2.GetIamPolicyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> policy_pb2.Policy:
            r"""Call the get iam policy method over HTTP.

            Args:
                request (~.iam_policy_pb2.GetIamPolicyRequest):
                    The request object. Request message for ``GetIamPolicy`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.policy_pb2.Policy:
                    An Identity and Access Management (IAM) policy, which
                specifies access controls for Google Cloud resources.

                A ``Policy`` is a collection of ``bindings``. A
                ``binding`` binds one or more ``members``, or
                principals, to a single ``role``. Principals can be user
                accounts, service accounts, Google groups, and domains
                (such as G Suite). A ``role`` is a named list of
                permissions; each ``role`` can be an IAM predefined role
                or a user-created custom role.

                For some types of Google Cloud resources, a ``binding``
                can also specify a ``condition``, which is a logical
                expression that allows access to a resource only if the
                expression evaluates to ``true``. A condition can add
                constraints based on attributes of the request, the
                resource, or both. To learn which resources support
                conditions in their IAM policies, see the `IAM
                documentation <https://cloud.google.com/iam/help/conditions/resource-policies>`__.

                **JSON example:**

                ::

                       {
                         "bindings": [
                           {
                             "role": "roles/resourcemanager.organizationAdmin",
                             "members": [
                               "user:mike@example.com",
                               "group:admins@example.com",
                               "domain:google.com",
                               "serviceAccount:my-project-id@appspot.gserviceaccount.com"
                             ]
                           },
                           {
                             "role": "roles/resourcemanager.organizationViewer",
                             "members": [
                               "user:eve@example.com"
                             ],
                             "condition": {
                               "title": "expirable access",
                               "description": "Does not grant access after Sep 2020",
                               "expression": "request.time <
                               timestamp('2020-10-01T00:00:00.000Z')",
                             }
                           }
                         ],
                         "etag": "BwWWja0YfJA=",
                         "version": 3
                       }

                **YAML example:**

                ::

                       bindings:
                       - members:
                         - user:mike@example.com
                         - group:admins@example.com
                         - domain:google.com
                         - serviceAccount:my-project-id@appspot.gserviceaccount.com
                         role: roles/resourcemanager.organizationAdmin
                       - members:
                         - user:eve@example.com
                         role: roles/resourcemanager.organizationViewer
                         condition:
                           title: expirable access
                           description: Does not grant access after Sep 2020
                           expression: request.time < timestamp('2020-10-01T00:00:00.000Z')
                       etag: BwWWja0YfJA=
                       version: 3

                For a description of IAM and its features, see the `IAM
                documentation <https://cloud.google.com/iam/docs/>`__.

            """

            http_options = (
                _BaseDataformRestTransport._BaseGetIamPolicy._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_iam_policy(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataformRestTransport._BaseGetIamPolicy,
                    "_BaseGetIamPolicy__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = json_format.MessageToJson(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.dataform_v1.DataformClient.GetIamPolicy",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "GetIamPolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DataformRestTransport._GetIamPolicy._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = policy_pb2.Policy()
            pb_resp = resp

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_iam_policy(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_iam_policy_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = json_format.MessageToJson(resp)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.dataform_v1.DataformClient.get_iam_policy",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "GetIamPolicy",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetReleaseConfig(
        _BaseDataformRestTransport._BaseGetReleaseConfig, DataformRestStub
    ):
        def __hash__(self):
            return hash("DataformRestTransport.GetReleaseConfig")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: dataform.GetReleaseConfigRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> dataform.ReleaseConfig:
            r"""Call the get release config method over HTTP.

            Args:
                request (~.dataform.GetReleaseConfigRequest):
                    The request object. ``GetReleaseConfig`` request message.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.dataform.ReleaseConfig:
                    Represents a Dataform release
                configuration.

            """

            http_options = (
                _BaseDataformRestTransport._BaseGetReleaseConfig._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_release_config(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataformRestTransport._BaseGetReleaseConfig,
                    "_BaseGetReleaseConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.dataform_v1.DataformClient.GetReleaseConfig",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "GetReleaseConfig",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DataformRestTransport._GetReleaseConfig._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = dataform.ReleaseConfig()
            pb_resp = dataform.ReleaseConfig.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_release_config(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_release_config_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = dataform.ReleaseConfig.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.dataform_v1.DataformClient.get_release_config",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "GetReleaseConfig",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetRepository(
        _BaseDataformRestTransport._BaseGetRepository, DataformRestStub
    ):
        def __hash__(self):
            return hash("DataformRestTransport.GetRepository")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: dataform.GetRepositoryRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> dataform.Repository:
            r"""Call the get repository method over HTTP.

            Args:
                request (~.dataform.GetRepositoryRequest):
                    The request object. ``GetRepository`` request message.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.dataform.Repository:
                    Represents a Dataform Git repository.
            """

            http_options = (
                _BaseDataformRestTransport._BaseGetRepository._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_repository(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataformRestTransport._BaseGetRepository,
                    "_BaseGetRepository__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.dataform_v1.DataformClient.GetRepository",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "GetRepository",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DataformRestTransport._GetRepository._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = dataform.Repository()
            pb_resp = dataform.Repository.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_repository(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_repository_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = dataform.Repository.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.dataform_v1.DataformClient.get_repository",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "GetRepository",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetTeamFolder(
        _BaseDataformRestTransport._BaseGetTeamFolder, DataformRestStub
    ):
        def __hash__(self):
            return hash("DataformRestTransport.GetTeamFolder")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: dataform.GetTeamFolderRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> dataform.TeamFolder:
            r"""Call the get team folder method over HTTP.

            Args:
                request (~.dataform.GetTeamFolderRequest):
                    The request object. ``GetTeamFolder`` request message.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.dataform.TeamFolder:
                    Represents a Dataform TeamFolder.
                This is a resource that sits at the
                project level and is used to organize
                Repositories and Folders with
                hierarchical access controls. They
                provide a team context and stricter
                access controls.

            """

            http_options = (
                _BaseDataformRestTransport._BaseGetTeamFolder._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_team_folder(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataformRestTransport._BaseGetTeamFolder,
                    "_BaseGetTeamFolder__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.dataform_v1.DataformClient.GetTeamFolder",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "GetTeamFolder",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DataformRestTransport._GetTeamFolder._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = dataform.TeamFolder()
            pb_resp = dataform.TeamFolder.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_team_folder(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_team_folder_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = dataform.TeamFolder.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.dataform_v1.DataformClient.get_team_folder",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "GetTeamFolder",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetWorkflowConfig(
        _BaseDataformRestTransport._BaseGetWorkflowConfig, DataformRestStub
    ):
        def __hash__(self):
            return hash("DataformRestTransport.GetWorkflowConfig")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: dataform.GetWorkflowConfigRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> dataform.WorkflowConfig:
            r"""Call the get workflow config method over HTTP.

            Args:
                request (~.dataform.GetWorkflowConfigRequest):
                    The request object. ``GetWorkflowConfig`` request message.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.dataform.WorkflowConfig:
                    Represents a Dataform workflow
                configuration.

            """

            http_options = (
                _BaseDataformRestTransport._BaseGetWorkflowConfig._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_workflow_config(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataformRestTransport._BaseGetWorkflowConfig,
                    "_BaseGetWorkflowConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.dataform_v1.DataformClient.GetWorkflowConfig",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "GetWorkflowConfig",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DataformRestTransport._GetWorkflowConfig._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = dataform.WorkflowConfig()
            pb_resp = dataform.WorkflowConfig.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_workflow_config(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_workflow_config_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = dataform.WorkflowConfig.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.dataform_v1.DataformClient.get_workflow_config",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "GetWorkflowConfig",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetWorkflowInvocation(
        _BaseDataformRestTransport._BaseGetWorkflowInvocation, DataformRestStub
    ):
        def __hash__(self):
            return hash("DataformRestTransport.GetWorkflowInvocation")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: dataform.GetWorkflowInvocationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> dataform.WorkflowInvocation:
            r"""Call the get workflow invocation method over HTTP.

            Args:
                request (~.dataform.GetWorkflowInvocationRequest):
                    The request object. ``GetWorkflowInvocation`` request message.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.dataform.WorkflowInvocation:
                    Represents a single invocation of a
                compilation result.

            """

            http_options = _BaseDataformRestTransport._BaseGetWorkflowInvocation._get_http_options()
            request, metadata = self._interceptor.pre_get_workflow_invocation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataformRestTransport._BaseGetWorkflowInvocation,
                    "_BaseGetWorkflowInvocation__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.dataform_v1.DataformClient.GetWorkflowInvocation",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "GetWorkflowInvocation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DataformRestTransport._GetWorkflowInvocation._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = dataform.WorkflowInvocation()
            pb_resp = dataform.WorkflowInvocation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_workflow_invocation(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_workflow_invocation_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = dataform.WorkflowInvocation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.dataform_v1.DataformClient.get_workflow_invocation",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "GetWorkflowInvocation",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetWorkspace(_BaseDataformRestTransport._BaseGetWorkspace, DataformRestStub):
        def __hash__(self):
            return hash("DataformRestTransport.GetWorkspace")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: dataform.GetWorkspaceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> dataform.Workspace:
            r"""Call the get workspace method over HTTP.

            Args:
                request (~.dataform.GetWorkspaceRequest):
                    The request object. ``GetWorkspace`` request message.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.dataform.Workspace:
                    Represents a Dataform Git workspace.
            """

            http_options = (
                _BaseDataformRestTransport._BaseGetWorkspace._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_workspace(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataformRestTransport._BaseGetWorkspace,
                    "_BaseGetWorkspace__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.dataform_v1.DataformClient.GetWorkspace",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "GetWorkspace",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DataformRestTransport._GetWorkspace._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = dataform.Workspace()
            pb_resp = dataform.Workspace.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_workspace(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_workspace_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = dataform.Workspace.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.dataform_v1.DataformClient.get_workspace",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "GetWorkspace",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _InstallNpmPackages(
        _BaseDataformRestTransport._BaseInstallNpmPackages, DataformRestStub
    ):
        def __hash__(self):
            return hash("DataformRestTransport.InstallNpmPackages")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )
            return response

        def __call__(
            self,
            request: dataform.InstallNpmPackagesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> dataform.InstallNpmPackagesResponse:
            r"""Call the install npm packages method over HTTP.

            Args:
                request (~.dataform.InstallNpmPackagesRequest):
                    The request object. ``InstallNpmPackages`` request message.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.dataform.InstallNpmPackagesResponse:
                    ``InstallNpmPackages`` response message.
            """

            http_options = (
                _BaseDataformRestTransport._BaseInstallNpmPackages._get_http_options()
            )
            request, metadata = self._interceptor.pre_install_npm_packages(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataformRestTransport._BaseInstallNpmPackages,
                    "_BaseInstallNpmPackages__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.dataform_v1.DataformClient.InstallNpmPackages",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "InstallNpmPackages",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DataformRestTransport._InstallNpmPackages._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = dataform.InstallNpmPackagesResponse()
            pb_resp = dataform.InstallNpmPackagesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_install_npm_packages(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_install_npm_packages_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = dataform.InstallNpmPackagesResponse.to_json(
                        response
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.dataform_v1.DataformClient.install_npm_packages",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "InstallNpmPackages",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListCompilationResults(
        _BaseDataformRestTransport._BaseListCompilationResults, DataformRestStub
    ):
        def __hash__(self):
            return hash("DataformRestTransport.ListCompilationResults")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: dataform.ListCompilationResultsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> dataform.ListCompilationResultsResponse:
            r"""Call the list compilation results method over HTTP.

            Args:
                request (~.dataform.ListCompilationResultsRequest):
                    The request object. ``ListCompilationResults`` request message.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.dataform.ListCompilationResultsResponse:
                    ``ListCompilationResults`` response message.
            """

            http_options = _BaseDataformRestTransport._BaseListCompilationResults._get_http_options()
            request, metadata = self._interceptor.pre_list_compilation_results(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataformRestTransport._BaseListCompilationResults,
                    "_BaseListCompilationResults__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.dataform_v1.DataformClient.ListCompilationResults",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "ListCompilationResults",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DataformRestTransport._ListCompilationResults._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = dataform.ListCompilationResultsResponse()
            pb_resp = dataform.ListCompilationResultsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_compilation_results(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_compilation_results_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = dataform.ListCompilationResultsResponse.to_json(
                        response
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.dataform_v1.DataformClient.list_compilation_results",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "ListCompilationResults",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListReleaseConfigs(
        _BaseDataformRestTransport._BaseListReleaseConfigs, DataformRestStub
    ):
        def __hash__(self):
            return hash("DataformRestTransport.ListReleaseConfigs")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: dataform.ListReleaseConfigsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> dataform.ListReleaseConfigsResponse:
            r"""Call the list release configs method over HTTP.

            Args:
                request (~.dataform.ListReleaseConfigsRequest):
                    The request object. ``ListReleaseConfigs`` request message.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.dataform.ListReleaseConfigsResponse:
                    ``ListReleaseConfigs`` response message.
            """

            http_options = (
                _BaseDataformRestTransport._BaseListReleaseConfigs._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_release_configs(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataformRestTransport._BaseListReleaseConfigs,
                    "_BaseListReleaseConfigs__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.dataform_v1.DataformClient.ListReleaseConfigs",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "ListReleaseConfigs",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DataformRestTransport._ListReleaseConfigs._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = dataform.ListReleaseConfigsResponse()
            pb_resp = dataform.ListReleaseConfigsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_release_configs(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_release_configs_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = dataform.ListReleaseConfigsResponse.to_json(
                        response
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.dataform_v1.DataformClient.list_release_configs",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "ListReleaseConfigs",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListRepositories(
        _BaseDataformRestTransport._BaseListRepositories, DataformRestStub
    ):
        def __hash__(self):
            return hash("DataformRestTransport.ListRepositories")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: dataform.ListRepositoriesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> dataform.ListRepositoriesResponse:
            r"""Call the list repositories method over HTTP.

            Args:
                request (~.dataform.ListRepositoriesRequest):
                    The request object. ``ListRepositories`` request message.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.dataform.ListRepositoriesResponse:
                    ``ListRepositories`` response message.
            """

            http_options = (
                _BaseDataformRestTransport._BaseListRepositories._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_repositories(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataformRestTransport._BaseListRepositories,
                    "_BaseListRepositories__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.dataform_v1.DataformClient.ListRepositories",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "ListRepositories",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DataformRestTransport._ListRepositories._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = dataform.ListRepositoriesResponse()
            pb_resp = dataform.ListRepositoriesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_repositories(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_repositories_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = dataform.ListRepositoriesResponse.to_json(
                        response
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.dataform_v1.DataformClient.list_repositories",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "ListRepositories",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListWorkflowConfigs(
        _BaseDataformRestTransport._BaseListWorkflowConfigs, DataformRestStub
    ):
        def __hash__(self):
            return hash("DataformRestTransport.ListWorkflowConfigs")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: dataform.ListWorkflowConfigsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> dataform.ListWorkflowConfigsResponse:
            r"""Call the list workflow configs method over HTTP.

            Args:
                request (~.dataform.ListWorkflowConfigsRequest):
                    The request object. ``ListWorkflowConfigs`` request message.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.dataform.ListWorkflowConfigsResponse:
                    ``ListWorkflowConfigs`` response message.
            """

            http_options = (
                _BaseDataformRestTransport._BaseListWorkflowConfigs._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_workflow_configs(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataformRestTransport._BaseListWorkflowConfigs,
                    "_BaseListWorkflowConfigs__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.dataform_v1.DataformClient.ListWorkflowConfigs",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "ListWorkflowConfigs",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DataformRestTransport._ListWorkflowConfigs._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = dataform.ListWorkflowConfigsResponse()
            pb_resp = dataform.ListWorkflowConfigsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_workflow_configs(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_workflow_configs_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = dataform.ListWorkflowConfigsResponse.to_json(
                        response
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.dataform_v1.DataformClient.list_workflow_configs",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "ListWorkflowConfigs",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListWorkflowInvocations(
        _BaseDataformRestTransport._BaseListWorkflowInvocations, DataformRestStub
    ):
        def __hash__(self):
            return hash("DataformRestTransport.ListWorkflowInvocations")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: dataform.ListWorkflowInvocationsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> dataform.ListWorkflowInvocationsResponse:
            r"""Call the list workflow invocations method over HTTP.

            Args:
                request (~.dataform.ListWorkflowInvocationsRequest):
                    The request object. ``ListWorkflowInvocations`` request message.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.dataform.ListWorkflowInvocationsResponse:
                    ``ListWorkflowInvocations`` response message.
            """

            http_options = _BaseDataformRestTransport._BaseListWorkflowInvocations._get_http_options()
            request, metadata = self._interceptor.pre_list_workflow_invocations(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataformRestTransport._BaseListWorkflowInvocations,
                    "_BaseListWorkflowInvocations__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.dataform_v1.DataformClient.ListWorkflowInvocations",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "ListWorkflowInvocations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DataformRestTransport._ListWorkflowInvocations._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = dataform.ListWorkflowInvocationsResponse()
            pb_resp = dataform.ListWorkflowInvocationsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_workflow_invocations(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_workflow_invocations_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = dataform.ListWorkflowInvocationsResponse.to_json(
                        response
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.dataform_v1.DataformClient.list_workflow_invocations",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "ListWorkflowInvocations",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListWorkspaces(
        _BaseDataformRestTransport._BaseListWorkspaces, DataformRestStub
    ):
        def __hash__(self):
            return hash("DataformRestTransport.ListWorkspaces")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: dataform.ListWorkspacesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> dataform.ListWorkspacesResponse:
            r"""Call the list workspaces method over HTTP.

            Args:
                request (~.dataform.ListWorkspacesRequest):
                    The request object. ``ListWorkspaces`` request message.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.dataform.ListWorkspacesResponse:
                    ``ListWorkspaces`` response message.
            """

            http_options = (
                _BaseDataformRestTransport._BaseListWorkspaces._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_workspaces(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataformRestTransport._BaseListWorkspaces,
                    "_BaseListWorkspaces__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.dataform_v1.DataformClient.ListWorkspaces",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "ListWorkspaces",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DataformRestTransport._ListWorkspaces._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = dataform.ListWorkspacesResponse()
            pb_resp = dataform.ListWorkspacesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_workspaces(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_workspaces_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = dataform.ListWorkspacesResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.dataform_v1.DataformClient.list_workspaces",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "ListWorkspaces",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _MakeDirectory(
        _BaseDataformRestTransport._BaseMakeDirectory, DataformRestStub
    ):
        def __hash__(self):
            return hash("DataformRestTransport.MakeDirectory")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )
            return response

        def __call__(
            self,
            request: dataform.MakeDirectoryRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> dataform.MakeDirectoryResponse:
            r"""Call the make directory method over HTTP.

            Args:
                request (~.dataform.MakeDirectoryRequest):
                    The request object. ``MakeDirectory`` request message.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.dataform.MakeDirectoryResponse:
                    ``MakeDirectory`` response message.
            """

            http_options = (
                _BaseDataformRestTransport._BaseMakeDirectory._get_http_options()
            )
            request, metadata = self._interceptor.pre_make_directory(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataformRestTransport._BaseMakeDirectory,
                    "_BaseMakeDirectory__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.dataform_v1.DataformClient.MakeDirectory",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "MakeDirectory",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DataformRestTransport._MakeDirectory._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = dataform.MakeDirectoryResponse()
            pb_resp = dataform.MakeDirectoryResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_make_directory(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_make_directory_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = dataform.MakeDirectoryResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.dataform_v1.DataformClient.make_directory",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "MakeDirectory",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _MoveDirectory(
        _BaseDataformRestTransport._BaseMoveDirectory, DataformRestStub
    ):
        def __hash__(self):
            return hash("DataformRestTransport.MoveDirectory")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )
            return response

        def __call__(
            self,
            request: dataform.MoveDirectoryRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> dataform.MoveDirectoryResponse:
            r"""Call the move directory method over HTTP.

            Args:
                request (~.dataform.MoveDirectoryRequest):
                    The request object. ``MoveDirectory`` request message.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.dataform.MoveDirectoryResponse:
                    ``MoveDirectory`` response message.
            """

            http_options = (
                _BaseDataformRestTransport._BaseMoveDirectory._get_http_options()
            )
            request, metadata = self._interceptor.pre_move_directory(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataformRestTransport._BaseMoveDirectory,
                    "_BaseMoveDirectory__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.dataform_v1.DataformClient.MoveDirectory",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "MoveDirectory",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DataformRestTransport._MoveDirectory._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = dataform.MoveDirectoryResponse()
            pb_resp = dataform.MoveDirectoryResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_move_directory(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_move_directory_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = dataform.MoveDirectoryResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.dataform_v1.DataformClient.move_directory",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "MoveDirectory",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _MoveFile(_BaseDataformRestTransport._BaseMoveFile, DataformRestStub):
        def __hash__(self):
            return hash("DataformRestTransport.MoveFile")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )
            return response

        def __call__(
            self,
            request: dataform.MoveFileRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> dataform.MoveFileResponse:
            r"""Call the move file method over HTTP.

            Args:
                request (~.dataform.MoveFileRequest):
                    The request object. ``MoveFile`` request message.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.dataform.MoveFileResponse:
                    ``MoveFile`` response message.
            """

            http_options = _BaseDataformRestTransport._BaseMoveFile._get_http_options()
            request, metadata = self._interceptor.pre_move_file(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataformRestTransport._BaseMoveFile,
                    "_BaseMoveFile__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.dataform_v1.DataformClient.MoveFile",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "MoveFile",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DataformRestTransport._MoveFile._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = dataform.MoveFileResponse()
            pb_resp = dataform.MoveFileResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_move_file(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_move_file_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = dataform.MoveFileResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.dataform_v1.DataformClient.move_file",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "MoveFile",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _MoveFolder(_BaseDataformRestTransport._BaseMoveFolder, DataformRestStub):
        def __hash__(self):
            return hash("DataformRestTransport.MoveFolder")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )
            return response

        def __call__(
            self,
            request: dataform.MoveFolderRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the move folder method over HTTP.

            Args:
                request (~.dataform.MoveFolderRequest):
                    The request object. ``MoveFolder`` request message.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.operations_pb2.Operation:
                    This resource represents a
                long-running operation that is the
                result of a network API call.

            """

            http_options = (
                _BaseDataformRestTransport._BaseMoveFolder._get_http_options()
            )
            request, metadata = self._interceptor.pre_move_folder(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataformRestTransport._BaseMoveFolder,
                    "_BaseMoveFolder__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.dataform_v1.DataformClient.MoveFolder",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "MoveFolder",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DataformRestTransport._MoveFolder._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_move_folder(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_move_folder_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = json_format.MessageToJson(resp)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.dataform_v1.DataformClient.move_folder",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "MoveFolder",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _MoveRepository(
        _BaseDataformRestTransport._BaseMoveRepository, DataformRestStub
    ):
        def __hash__(self):
            return hash("DataformRestTransport.MoveRepository")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )
            return response

        def __call__(
            self,
            request: dataform.MoveRepositoryRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the move repository method over HTTP.

            Args:
                request (~.dataform.MoveRepositoryRequest):
                    The request object. ``MoveRepository`` request message.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.operations_pb2.Operation:
                    This resource represents a
                long-running operation that is the
                result of a network API call.

            """

            http_options = (
                _BaseDataformRestTransport._BaseMoveRepository._get_http_options()
            )
            request, metadata = self._interceptor.pre_move_repository(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataformRestTransport._BaseMoveRepository,
                    "_BaseMoveRepository__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.dataform_v1.DataformClient.MoveRepository",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "MoveRepository",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DataformRestTransport._MoveRepository._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_move_repository(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_move_repository_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = json_format.MessageToJson(resp)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.dataform_v1.DataformClient.move_repository",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "MoveRepository",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _PullGitCommits(
        _BaseDataformRestTransport._BasePullGitCommits, DataformRestStub
    ):
        def __hash__(self):
            return hash("DataformRestTransport.PullGitCommits")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )
            return response

        def __call__(
            self,
            request: dataform.PullGitCommitsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> dataform.PullGitCommitsResponse:
            r"""Call the pull git commits method over HTTP.

            Args:
                request (~.dataform.PullGitCommitsRequest):
                    The request object. ``PullGitCommits`` request message.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.dataform.PullGitCommitsResponse:
                    ``PullGitCommits`` response message.
            """

            http_options = (
                _BaseDataformRestTransport._BasePullGitCommits._get_http_options()
            )
            request, metadata = self._interceptor.pre_pull_git_commits(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataformRestTransport._BasePullGitCommits,
                    "_BasePullGitCommits__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.dataform_v1.DataformClient.PullGitCommits",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "PullGitCommits",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DataformRestTransport._PullGitCommits._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = dataform.PullGitCommitsResponse()
            pb_resp = dataform.PullGitCommitsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_pull_git_commits(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_pull_git_commits_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = dataform.PullGitCommitsResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.dataform_v1.DataformClient.pull_git_commits",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "PullGitCommits",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _PushGitCommits(
        _BaseDataformRestTransport._BasePushGitCommits, DataformRestStub
    ):
        def __hash__(self):
            return hash("DataformRestTransport.PushGitCommits")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )
            return response

        def __call__(
            self,
            request: dataform.PushGitCommitsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> dataform.PushGitCommitsResponse:
            r"""Call the push git commits method over HTTP.

            Args:
                request (~.dataform.PushGitCommitsRequest):
                    The request object. ``PushGitCommits`` request message.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.dataform.PushGitCommitsResponse:
                    ``PushGitCommits`` response message.
            """

            http_options = (
                _BaseDataformRestTransport._BasePushGitCommits._get_http_options()
            )
            request, metadata = self._interceptor.pre_push_git_commits(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataformRestTransport._BasePushGitCommits,
                    "_BasePushGitCommits__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.dataform_v1.DataformClient.PushGitCommits",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "PushGitCommits",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DataformRestTransport._PushGitCommits._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = dataform.PushGitCommitsResponse()
            pb_resp = dataform.PushGitCommitsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_push_git_commits(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_push_git_commits_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = dataform.PushGitCommitsResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.dataform_v1.DataformClient.push_git_commits",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "PushGitCommits",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _QueryCompilationResultActions(
        _BaseDataformRestTransport._BaseQueryCompilationResultActions, DataformRestStub
    ):
        def __hash__(self):
            return hash("DataformRestTransport.QueryCompilationResultActions")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: dataform.QueryCompilationResultActionsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> dataform.QueryCompilationResultActionsResponse:
            r"""Call the query compilation result
            actions method over HTTP.

                Args:
                    request (~.dataform.QueryCompilationResultActionsRequest):
                        The request object. ``QueryCompilationResultActions`` request message.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.dataform.QueryCompilationResultActionsResponse:
                        ``QueryCompilationResultActions`` response message.
            """

            http_options = _BaseDataformRestTransport._BaseQueryCompilationResultActions._get_http_options()
            request, metadata = self._interceptor.pre_query_compilation_result_actions(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataformRestTransport._BaseQueryCompilationResultActions,
                    "_BaseQueryCompilationResultActions__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.dataform_v1.DataformClient.QueryCompilationResultActions",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "QueryCompilationResultActions",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                DataformRestTransport._QueryCompilationResultActions._get_response(
                    self._host,
                    metadata,
                    query_params,
                    self._session,
                    timeout,
                    transcoded_request,
                )
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = dataform.QueryCompilationResultActionsResponse()
            pb_resp = dataform.QueryCompilationResultActionsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_query_compilation_result_actions(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_query_compilation_result_actions_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        dataform.QueryCompilationResultActionsResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.dataform_v1.DataformClient.query_compilation_result_actions",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "QueryCompilationResultActions",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _QueryDirectoryContents(
        _BaseDataformRestTransport._BaseQueryDirectoryContents, DataformRestStub
    ):
        def __hash__(self):
            return hash("DataformRestTransport.QueryDirectoryContents")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: dataform.QueryDirectoryContentsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> dataform.QueryDirectoryContentsResponse:
            r"""Call the query directory contents method over HTTP.

            Args:
                request (~.dataform.QueryDirectoryContentsRequest):
                    The request object. ``QueryDirectoryContents`` request message.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.dataform.QueryDirectoryContentsResponse:
                    ``QueryDirectoryContents`` response message.
            """

            http_options = _BaseDataformRestTransport._BaseQueryDirectoryContents._get_http_options()
            request, metadata = self._interceptor.pre_query_directory_contents(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataformRestTransport._BaseQueryDirectoryContents,
                    "_BaseQueryDirectoryContents__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.dataform_v1.DataformClient.QueryDirectoryContents",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "QueryDirectoryContents",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DataformRestTransport._QueryDirectoryContents._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = dataform.QueryDirectoryContentsResponse()
            pb_resp = dataform.QueryDirectoryContentsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_query_directory_contents(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_query_directory_contents_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = dataform.QueryDirectoryContentsResponse.to_json(
                        response
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.dataform_v1.DataformClient.query_directory_contents",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "QueryDirectoryContents",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _QueryFolderContents(
        _BaseDataformRestTransport._BaseQueryFolderContents, DataformRestStub
    ):
        def __hash__(self):
            return hash("DataformRestTransport.QueryFolderContents")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: dataform.QueryFolderContentsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> dataform.QueryFolderContentsResponse:
            r"""Call the query folder contents method over HTTP.

            Args:
                request (~.dataform.QueryFolderContentsRequest):
                    The request object. ``QueryFolderContents`` request message.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.dataform.QueryFolderContentsResponse:
                    ``QueryFolderContents`` response message.
            """

            http_options = (
                _BaseDataformRestTransport._BaseQueryFolderContents._get_http_options()
            )
            request, metadata = self._interceptor.pre_query_folder_contents(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataformRestTransport._BaseQueryFolderContents,
                    "_BaseQueryFolderContents__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.dataform_v1.DataformClient.QueryFolderContents",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "QueryFolderContents",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DataformRestTransport._QueryFolderContents._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = dataform.QueryFolderContentsResponse()
            pb_resp = dataform.QueryFolderContentsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_query_folder_contents(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_query_folder_contents_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = dataform.QueryFolderContentsResponse.to_json(
                        response
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.dataform_v1.DataformClient.query_folder_contents",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "QueryFolderContents",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _QueryRepositoryDirectoryContents(
        _BaseDataformRestTransport._BaseQueryRepositoryDirectoryContents,
        DataformRestStub,
    ):
        def __hash__(self):
            return hash("DataformRestTransport.QueryRepositoryDirectoryContents")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: dataform.QueryRepositoryDirectoryContentsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> dataform.QueryRepositoryDirectoryContentsResponse:
            r"""Call the query repository
            directory contents method over HTTP.

                Args:
                    request (~.dataform.QueryRepositoryDirectoryContentsRequest):
                        The request object. ``QueryRepositoryDirectoryContents`` request message.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.dataform.QueryRepositoryDirectoryContentsResponse:
                        ``QueryRepositoryDirectoryContents`` response message.
            """

            http_options = _BaseDataformRestTransport._BaseQueryRepositoryDirectoryContents._get_http_options()
            request, metadata = (
                self._interceptor.pre_query_repository_directory_contents(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataformRestTransport._BaseQueryRepositoryDirectoryContents,
                    "_BaseQueryRepositoryDirectoryContents__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.dataform_v1.DataformClient.QueryRepositoryDirectoryContents",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "QueryRepositoryDirectoryContents",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                DataformRestTransport._QueryRepositoryDirectoryContents._get_response(
                    self._host,
                    metadata,
                    query_params,
                    self._session,
                    timeout,
                    transcoded_request,
                )
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = dataform.QueryRepositoryDirectoryContentsResponse()
            pb_resp = dataform.QueryRepositoryDirectoryContentsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_query_repository_directory_contents(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_query_repository_directory_contents_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        dataform.QueryRepositoryDirectoryContentsResponse.to_json(
                            response
                        )
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.dataform_v1.DataformClient.query_repository_directory_contents",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "QueryRepositoryDirectoryContents",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _QueryTeamFolderContents(
        _BaseDataformRestTransport._BaseQueryTeamFolderContents, DataformRestStub
    ):
        def __hash__(self):
            return hash("DataformRestTransport.QueryTeamFolderContents")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: dataform.QueryTeamFolderContentsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> dataform.QueryTeamFolderContentsResponse:
            r"""Call the query team folder
            contents method over HTTP.

                Args:
                    request (~.dataform.QueryTeamFolderContentsRequest):
                        The request object. ``QueryTeamFolderContents`` request message.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.dataform.QueryTeamFolderContentsResponse:
                        ``QueryTeamFolderContents`` response message.
            """

            http_options = _BaseDataformRestTransport._BaseQueryTeamFolderContents._get_http_options()
            request, metadata = self._interceptor.pre_query_team_folder_contents(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataformRestTransport._BaseQueryTeamFolderContents,
                    "_BaseQueryTeamFolderContents__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.dataform_v1.DataformClient.QueryTeamFolderContents",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "QueryTeamFolderContents",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DataformRestTransport._QueryTeamFolderContents._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = dataform.QueryTeamFolderContentsResponse()
            pb_resp = dataform.QueryTeamFolderContentsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_query_team_folder_contents(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_query_team_folder_contents_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = dataform.QueryTeamFolderContentsResponse.to_json(
                        response
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.dataform_v1.DataformClient.query_team_folder_contents",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "QueryTeamFolderContents",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _QueryUserRootContents(
        _BaseDataformRestTransport._BaseQueryUserRootContents, DataformRestStub
    ):
        def __hash__(self):
            return hash("DataformRestTransport.QueryUserRootContents")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: dataform.QueryUserRootContentsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> dataform.QueryUserRootContentsResponse:
            r"""Call the query user root contents method over HTTP.

            Args:
                request (~.dataform.QueryUserRootContentsRequest):
                    The request object. ``QueryUserRootContents`` request message.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.dataform.QueryUserRootContentsResponse:
                    ``QueryUserRootContents`` response message.
            """

            http_options = _BaseDataformRestTransport._BaseQueryUserRootContents._get_http_options()
            request, metadata = self._interceptor.pre_query_user_root_contents(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataformRestTransport._BaseQueryUserRootContents,
                    "_BaseQueryUserRootContents__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.dataform_v1.DataformClient.QueryUserRootContents",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "QueryUserRootContents",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DataformRestTransport._QueryUserRootContents._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = dataform.QueryUserRootContentsResponse()
            pb_resp = dataform.QueryUserRootContentsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_query_user_root_contents(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_query_user_root_contents_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = dataform.QueryUserRootContentsResponse.to_json(
                        response
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.dataform_v1.DataformClient.query_user_root_contents",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "QueryUserRootContents",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _QueryWorkflowInvocationActions(
        _BaseDataformRestTransport._BaseQueryWorkflowInvocationActions, DataformRestStub
    ):
        def __hash__(self):
            return hash("DataformRestTransport.QueryWorkflowInvocationActions")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: dataform.QueryWorkflowInvocationActionsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> dataform.QueryWorkflowInvocationActionsResponse:
            r"""Call the query workflow invocation
            actions method over HTTP.

                Args:
                    request (~.dataform.QueryWorkflowInvocationActionsRequest):
                        The request object. ``QueryWorkflowInvocationActions`` request message.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.dataform.QueryWorkflowInvocationActionsResponse:
                        ``QueryWorkflowInvocationActions`` response message.
            """

            http_options = _BaseDataformRestTransport._BaseQueryWorkflowInvocationActions._get_http_options()
            request, metadata = self._interceptor.pre_query_workflow_invocation_actions(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataformRestTransport._BaseQueryWorkflowInvocationActions,
                    "_BaseQueryWorkflowInvocationActions__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.dataform_v1.DataformClient.QueryWorkflowInvocationActions",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "QueryWorkflowInvocationActions",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                DataformRestTransport._QueryWorkflowInvocationActions._get_response(
                    self._host,
                    metadata,
                    query_params,
                    self._session,
                    timeout,
                    transcoded_request,
                )
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = dataform.QueryWorkflowInvocationActionsResponse()
            pb_resp = dataform.QueryWorkflowInvocationActionsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_query_workflow_invocation_actions(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_query_workflow_invocation_actions_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        dataform.QueryWorkflowInvocationActionsResponse.to_json(
                            response
                        )
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.dataform_v1.DataformClient.query_workflow_invocation_actions",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "QueryWorkflowInvocationActions",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ReadFile(_BaseDataformRestTransport._BaseReadFile, DataformRestStub):
        def __hash__(self):
            return hash("DataformRestTransport.ReadFile")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: dataform.ReadFileRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> dataform.ReadFileResponse:
            r"""Call the read file method over HTTP.

            Args:
                request (~.dataform.ReadFileRequest):
                    The request object. ``ReadFile`` request message.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.dataform.ReadFileResponse:
                    ``ReadFile`` response message.
            """

            http_options = _BaseDataformRestTransport._BaseReadFile._get_http_options()
            request, metadata = self._interceptor.pre_read_file(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataformRestTransport._BaseReadFile,
                    "_BaseReadFile__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.dataform_v1.DataformClient.ReadFile",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "ReadFile",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DataformRestTransport._ReadFile._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = dataform.ReadFileResponse()
            pb_resp = dataform.ReadFileResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_read_file(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_read_file_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = dataform.ReadFileResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.dataform_v1.DataformClient.read_file",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "ReadFile",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ReadRepositoryFile(
        _BaseDataformRestTransport._BaseReadRepositoryFile, DataformRestStub
    ):
        def __hash__(self):
            return hash("DataformRestTransport.ReadRepositoryFile")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: dataform.ReadRepositoryFileRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> dataform.ReadRepositoryFileResponse:
            r"""Call the read repository file method over HTTP.

            Args:
                request (~.dataform.ReadRepositoryFileRequest):
                    The request object. ``ReadRepositoryFile`` request message.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.dataform.ReadRepositoryFileResponse:
                    ``ReadRepositoryFile`` response message.
            """

            http_options = (
                _BaseDataformRestTransport._BaseReadRepositoryFile._get_http_options()
            )
            request, metadata = self._interceptor.pre_read_repository_file(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataformRestTransport._BaseReadRepositoryFile,
                    "_BaseReadRepositoryFile__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.dataform_v1.DataformClient.ReadRepositoryFile",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "ReadRepositoryFile",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DataformRestTransport._ReadRepositoryFile._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = dataform.ReadRepositoryFileResponse()
            pb_resp = dataform.ReadRepositoryFileResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_read_repository_file(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_read_repository_file_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = dataform.ReadRepositoryFileResponse.to_json(
                        response
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.dataform_v1.DataformClient.read_repository_file",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "ReadRepositoryFile",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _RemoveDirectory(
        _BaseDataformRestTransport._BaseRemoveDirectory, DataformRestStub
    ):
        def __hash__(self):
            return hash("DataformRestTransport.RemoveDirectory")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )
            return response

        def __call__(
            self,
            request: dataform.RemoveDirectoryRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> dataform.RemoveDirectoryResponse:
            r"""Call the remove directory method over HTTP.

            Args:
                request (~.dataform.RemoveDirectoryRequest):
                    The request object. ``RemoveDirectory`` request message.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.dataform.RemoveDirectoryResponse:
                    ``RemoveDirectory`` response message.
            """

            http_options = (
                _BaseDataformRestTransport._BaseRemoveDirectory._get_http_options()
            )
            request, metadata = self._interceptor.pre_remove_directory(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataformRestTransport._BaseRemoveDirectory,
                    "_BaseRemoveDirectory__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.dataform_v1.DataformClient.RemoveDirectory",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "RemoveDirectory",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DataformRestTransport._RemoveDirectory._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = dataform.RemoveDirectoryResponse()
            pb_resp = dataform.RemoveDirectoryResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_remove_directory(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_remove_directory_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = dataform.RemoveDirectoryResponse.to_json(
                        response
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.dataform_v1.DataformClient.remove_directory",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "RemoveDirectory",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _RemoveFile(_BaseDataformRestTransport._BaseRemoveFile, DataformRestStub):
        def __hash__(self):
            return hash("DataformRestTransport.RemoveFile")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )
            return response

        def __call__(
            self,
            request: dataform.RemoveFileRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> dataform.RemoveFileResponse:
            r"""Call the remove file method over HTTP.

            Args:
                request (~.dataform.RemoveFileRequest):
                    The request object. ``RemoveFile`` request message.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.dataform.RemoveFileResponse:
                    ``RemoveFile`` response message.
            """

            http_options = (
                _BaseDataformRestTransport._BaseRemoveFile._get_http_options()
            )
            request, metadata = self._interceptor.pre_remove_file(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataformRestTransport._BaseRemoveFile,
                    "_BaseRemoveFile__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.dataform_v1.DataformClient.RemoveFile",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "RemoveFile",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DataformRestTransport._RemoveFile._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = dataform.RemoveFileResponse()
            pb_resp = dataform.RemoveFileResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_remove_file(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_remove_file_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = dataform.RemoveFileResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.dataform_v1.DataformClient.remove_file",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "RemoveFile",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ResetWorkspaceChanges(
        _BaseDataformRestTransport._BaseResetWorkspaceChanges, DataformRestStub
    ):
        def __hash__(self):
            return hash("DataformRestTransport.ResetWorkspaceChanges")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )
            return response

        def __call__(
            self,
            request: dataform.ResetWorkspaceChangesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> dataform.ResetWorkspaceChangesResponse:
            r"""Call the reset workspace changes method over HTTP.

            Args:
                request (~.dataform.ResetWorkspaceChangesRequest):
                    The request object. ``ResetWorkspaceChanges`` request message.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.dataform.ResetWorkspaceChangesResponse:
                    ``ResetWorkspaceChanges`` response message.
            """

            http_options = _BaseDataformRestTransport._BaseResetWorkspaceChanges._get_http_options()
            request, metadata = self._interceptor.pre_reset_workspace_changes(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataformRestTransport._BaseResetWorkspaceChanges,
                    "_BaseResetWorkspaceChanges__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.dataform_v1.DataformClient.ResetWorkspaceChanges",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "ResetWorkspaceChanges",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DataformRestTransport._ResetWorkspaceChanges._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = dataform.ResetWorkspaceChangesResponse()
            pb_resp = dataform.ResetWorkspaceChangesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_reset_workspace_changes(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_reset_workspace_changes_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = dataform.ResetWorkspaceChangesResponse.to_json(
                        response
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.dataform_v1.DataformClient.reset_workspace_changes",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "ResetWorkspaceChanges",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _SearchFiles(_BaseDataformRestTransport._BaseSearchFiles, DataformRestStub):
        def __hash__(self):
            return hash("DataformRestTransport.SearchFiles")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: dataform.SearchFilesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> dataform.SearchFilesResponse:
            r"""Call the search files method over HTTP.

            Args:
                request (~.dataform.SearchFilesRequest):
                    The request object. Configuration containing file search
                request parameters.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.dataform.SearchFilesResponse:
                    Client-facing representation of a
                file search response.

            """

            http_options = (
                _BaseDataformRestTransport._BaseSearchFiles._get_http_options()
            )
            request, metadata = self._interceptor.pre_search_files(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataformRestTransport._BaseSearchFiles,
                    "_BaseSearchFiles__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.dataform_v1.DataformClient.SearchFiles",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "SearchFiles",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DataformRestTransport._SearchFiles._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = dataform.SearchFilesResponse()
            pb_resp = dataform.SearchFilesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_search_files(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_search_files_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = dataform.SearchFilesResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.dataform_v1.DataformClient.search_files",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "SearchFiles",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _SearchTeamFolders(
        _BaseDataformRestTransport._BaseSearchTeamFolders, DataformRestStub
    ):
        def __hash__(self):
            return hash("DataformRestTransport.SearchTeamFolders")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: dataform.SearchTeamFoldersRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> dataform.SearchTeamFoldersResponse:
            r"""Call the search team folders method over HTTP.

            Args:
                request (~.dataform.SearchTeamFoldersRequest):
                    The request object. ``SearchTeamFolders`` request message.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.dataform.SearchTeamFoldersResponse:
                    ``SearchTeamFolders`` response message.
            """

            http_options = (
                _BaseDataformRestTransport._BaseSearchTeamFolders._get_http_options()
            )
            request, metadata = self._interceptor.pre_search_team_folders(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataformRestTransport._BaseSearchTeamFolders,
                    "_BaseSearchTeamFolders__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.dataform_v1.DataformClient.SearchTeamFolders",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "SearchTeamFolders",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DataformRestTransport._SearchTeamFolders._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = dataform.SearchTeamFoldersResponse()
            pb_resp = dataform.SearchTeamFoldersResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_search_team_folders(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_search_team_folders_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = dataform.SearchTeamFoldersResponse.to_json(
                        response
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.dataform_v1.DataformClient.search_team_folders",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "SearchTeamFolders",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _SetIamPolicy(_BaseDataformRestTransport._BaseSetIamPolicy, DataformRestStub):
        def __hash__(self):
            return hash("DataformRestTransport.SetIamPolicy")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )
            return response

        def __call__(
            self,
            request: iam_policy_pb2.SetIamPolicyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> policy_pb2.Policy:
            r"""Call the set iam policy method over HTTP.

            Args:
                request (~.iam_policy_pb2.SetIamPolicyRequest):
                    The request object. Request message for ``SetIamPolicy`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.policy_pb2.Policy:
                    An Identity and Access Management (IAM) policy, which
                specifies access controls for Google Cloud resources.

                A ``Policy`` is a collection of ``bindings``. A
                ``binding`` binds one or more ``members``, or
                principals, to a single ``role``. Principals can be user
                accounts, service accounts, Google groups, and domains
                (such as G Suite). A ``role`` is a named list of
                permissions; each ``role`` can be an IAM predefined role
                or a user-created custom role.

                For some types of Google Cloud resources, a ``binding``
                can also specify a ``condition``, which is a logical
                expression that allows access to a resource only if the
                expression evaluates to ``true``. A condition can add
                constraints based on attributes of the request, the
                resource, or both. To learn which resources support
                conditions in their IAM policies, see the `IAM
                documentation <https://cloud.google.com/iam/help/conditions/resource-policies>`__.

                **JSON example:**

                ::

                       {
                         "bindings": [
                           {
                             "role": "roles/resourcemanager.organizationAdmin",
                             "members": [
                               "user:mike@example.com",
                               "group:admins@example.com",
                               "domain:google.com",
                               "serviceAccount:my-project-id@appspot.gserviceaccount.com"
                             ]
                           },
                           {
                             "role": "roles/resourcemanager.organizationViewer",
                             "members": [
                               "user:eve@example.com"
                             ],
                             "condition": {
                               "title": "expirable access",
                               "description": "Does not grant access after Sep 2020",
                               "expression": "request.time <
                               timestamp('2020-10-01T00:00:00.000Z')",
                             }
                           }
                         ],
                         "etag": "BwWWja0YfJA=",
                         "version": 3
                       }

                **YAML example:**

                ::

                       bindings:
                       - members:
                         - user:mike@example.com
                         - group:admins@example.com
                         - domain:google.com
                         - serviceAccount:my-project-id@appspot.gserviceaccount.com
                         role: roles/resourcemanager.organizationAdmin
                       - members:
                         - user:eve@example.com
                         role: roles/resourcemanager.organizationViewer
                         condition:
                           title: expirable access
                           description: Does not grant access after Sep 2020
                           expression: request.time < timestamp('2020-10-01T00:00:00.000Z')
                       etag: BwWWja0YfJA=
                       version: 3

                For a description of IAM and its features, see the `IAM
                documentation <https://cloud.google.com/iam/docs/>`__.

            """

            http_options = (
                _BaseDataformRestTransport._BaseSetIamPolicy._get_http_options()
            )
            request, metadata = self._interceptor.pre_set_iam_policy(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataformRestTransport._BaseSetIamPolicy,
                    "_BaseSetIamPolicy__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = json_format.MessageToJson(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.dataform_v1.DataformClient.SetIamPolicy",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "SetIamPolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DataformRestTransport._SetIamPolicy._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = policy_pb2.Policy()
            pb_resp = resp

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_set_iam_policy(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_set_iam_policy_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = json_format.MessageToJson(resp)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.dataform_v1.DataformClient.set_iam_policy",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "SetIamPolicy",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _TestIamPermissions(
        _BaseDataformRestTransport._BaseTestIamPermissions, DataformRestStub
    ):
        def __hash__(self):
            return hash("DataformRestTransport.TestIamPermissions")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )
            return response

        def __call__(
            self,
            request: iam_policy_pb2.TestIamPermissionsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> iam_policy_pb2.TestIamPermissionsResponse:
            r"""Call the test iam permissions method over HTTP.

            Args:
                request (~.iam_policy_pb2.TestIamPermissionsRequest):
                    The request object. Request message for ``TestIamPermissions`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.iam_policy_pb2.TestIamPermissionsResponse:
                    Response message for ``TestIamPermissions`` method.
            """

            http_options = (
                _BaseDataformRestTransport._BaseTestIamPermissions._get_http_options()
            )
            request, metadata = self._interceptor.pre_test_iam_permissions(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataformRestTransport._BaseTestIamPermissions,
                    "_BaseTestIamPermissions__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = json_format.MessageToJson(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.dataform_v1.DataformClient.TestIamPermissions",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "TestIamPermissions",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DataformRestTransport._TestIamPermissions._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = iam_policy_pb2.TestIamPermissionsResponse()
            pb_resp = resp

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_test_iam_permissions(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_test_iam_permissions_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = json_format.MessageToJson(resp)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.dataform_v1.DataformClient.test_iam_permissions",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "TestIamPermissions",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateConfig(_BaseDataformRestTransport._BaseUpdateConfig, DataformRestStub):
        def __hash__(self):
            return hash("DataformRestTransport.UpdateConfig")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )
            return response

        def __call__(
            self,
            request: dataform.UpdateConfigRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> dataform.Config:
            r"""Call the update config method over HTTP.

            Args:
                request (~.dataform.UpdateConfigRequest):
                    The request object. ``UpdateConfig`` request message.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.dataform.Config:
                    Config for all repositories in a
                given project and location.

            """

            http_options = (
                _BaseDataformRestTransport._BaseUpdateConfig._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_config(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataformRestTransport._BaseUpdateConfig,
                    "_BaseUpdateConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.dataform_v1.DataformClient.UpdateConfig",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "UpdateConfig",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DataformRestTransport._UpdateConfig._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = dataform.Config()
            pb_resp = dataform.Config.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_config(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_config_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = dataform.Config.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.dataform_v1.DataformClient.update_config",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "UpdateConfig",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateFolder(_BaseDataformRestTransport._BaseUpdateFolder, DataformRestStub):
        def __hash__(self):
            return hash("DataformRestTransport.UpdateFolder")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )
            return response

        def __call__(
            self,
            request: dataform.UpdateFolderRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> dataform.Folder:
            r"""Call the update folder method over HTTP.

            Args:
                request (~.dataform.UpdateFolderRequest):
                    The request object. ``UpdateFolder`` request message.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.dataform.Folder:
                    Represents a Dataform Folder. This is
                a resource that is used to organize
                Files and other Folders and provide
                hierarchical access controls.

            """

            http_options = (
                _BaseDataformRestTransport._BaseUpdateFolder._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_folder(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataformRestTransport._BaseUpdateFolder,
                    "_BaseUpdateFolder__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.dataform_v1.DataformClient.UpdateFolder",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "UpdateFolder",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DataformRestTransport._UpdateFolder._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = dataform.Folder()
            pb_resp = dataform.Folder.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_folder(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_folder_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = dataform.Folder.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.dataform_v1.DataformClient.update_folder",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "UpdateFolder",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateReleaseConfig(
        _BaseDataformRestTransport._BaseUpdateReleaseConfig, DataformRestStub
    ):
        def __hash__(self):
            return hash("DataformRestTransport.UpdateReleaseConfig")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )
            return response

        def __call__(
            self,
            request: dataform.UpdateReleaseConfigRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> dataform.ReleaseConfig:
            r"""Call the update release config method over HTTP.

            Args:
                request (~.dataform.UpdateReleaseConfigRequest):
                    The request object. ``UpdateReleaseConfig`` request message.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.dataform.ReleaseConfig:
                    Represents a Dataform release
                configuration.

            """

            http_options = (
                _BaseDataformRestTransport._BaseUpdateReleaseConfig._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_release_config(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataformRestTransport._BaseUpdateReleaseConfig,
                    "_BaseUpdateReleaseConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.dataform_v1.DataformClient.UpdateReleaseConfig",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "UpdateReleaseConfig",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DataformRestTransport._UpdateReleaseConfig._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = dataform.ReleaseConfig()
            pb_resp = dataform.ReleaseConfig.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_release_config(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_release_config_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = dataform.ReleaseConfig.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.dataform_v1.DataformClient.update_release_config",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "UpdateReleaseConfig",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateRepository(
        _BaseDataformRestTransport._BaseUpdateRepository, DataformRestStub
    ):
        def __hash__(self):
            return hash("DataformRestTransport.UpdateRepository")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )
            return response

        def __call__(
            self,
            request: dataform.UpdateRepositoryRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> dataform.Repository:
            r"""Call the update repository method over HTTP.

            Args:
                request (~.dataform.UpdateRepositoryRequest):
                    The request object. ``UpdateRepository`` request message.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.dataform.Repository:
                    Represents a Dataform Git repository.
            """

            http_options = (
                _BaseDataformRestTransport._BaseUpdateRepository._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_repository(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataformRestTransport._BaseUpdateRepository,
                    "_BaseUpdateRepository__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.dataform_v1.DataformClient.UpdateRepository",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "UpdateRepository",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DataformRestTransport._UpdateRepository._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = dataform.Repository()
            pb_resp = dataform.Repository.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_repository(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_repository_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = dataform.Repository.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.dataform_v1.DataformClient.update_repository",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "UpdateRepository",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateTeamFolder(
        _BaseDataformRestTransport._BaseUpdateTeamFolder, DataformRestStub
    ):
        def __hash__(self):
            return hash("DataformRestTransport.UpdateTeamFolder")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )
            return response

        def __call__(
            self,
            request: dataform.UpdateTeamFolderRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> dataform.TeamFolder:
            r"""Call the update team folder method over HTTP.

            Args:
                request (~.dataform.UpdateTeamFolderRequest):
                    The request object. ``UpdateTeamFolder`` request message.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.dataform.TeamFolder:
                    Represents a Dataform TeamFolder.
                This is a resource that sits at the
                project level and is used to organize
                Repositories and Folders with
                hierarchical access controls. They
                provide a team context and stricter
                access controls.

            """

            http_options = (
                _BaseDataformRestTransport._BaseUpdateTeamFolder._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_team_folder(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataformRestTransport._BaseUpdateTeamFolder,
                    "_BaseUpdateTeamFolder__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.dataform_v1.DataformClient.UpdateTeamFolder",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "UpdateTeamFolder",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DataformRestTransport._UpdateTeamFolder._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = dataform.TeamFolder()
            pb_resp = dataform.TeamFolder.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_team_folder(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_team_folder_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = dataform.TeamFolder.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.dataform_v1.DataformClient.update_team_folder",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "UpdateTeamFolder",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateWorkflowConfig(
        _BaseDataformRestTransport._BaseUpdateWorkflowConfig, DataformRestStub
    ):
        def __hash__(self):
            return hash("DataformRestTransport.UpdateWorkflowConfig")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )
            return response

        def __call__(
            self,
            request: dataform.UpdateWorkflowConfigRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> dataform.WorkflowConfig:
            r"""Call the update workflow config method over HTTP.

            Args:
                request (~.dataform.UpdateWorkflowConfigRequest):
                    The request object. ``UpdateWorkflowConfig`` request message.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.dataform.WorkflowConfig:
                    Represents a Dataform workflow
                configuration.

            """

            http_options = (
                _BaseDataformRestTransport._BaseUpdateWorkflowConfig._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_workflow_config(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataformRestTransport._BaseUpdateWorkflowConfig,
                    "_BaseUpdateWorkflowConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.dataform_v1.DataformClient.UpdateWorkflowConfig",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "UpdateWorkflowConfig",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DataformRestTransport._UpdateWorkflowConfig._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = dataform.WorkflowConfig()
            pb_resp = dataform.WorkflowConfig.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_workflow_config(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_workflow_config_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = dataform.WorkflowConfig.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.dataform_v1.DataformClient.update_workflow_config",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "UpdateWorkflowConfig",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _WriteFile(_BaseDataformRestTransport._BaseWriteFile, DataformRestStub):
        def __hash__(self):
            return hash("DataformRestTransport.WriteFile")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )
            return response

        def __call__(
            self,
            request: dataform.WriteFileRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> dataform.WriteFileResponse:
            r"""Call the write file method over HTTP.

            Args:
                request (~.dataform.WriteFileRequest):
                    The request object. ``WriteFile`` request message.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.dataform.WriteFileResponse:
                    ``WriteFile`` response message.
            """

            http_options = _BaseDataformRestTransport._BaseWriteFile._get_http_options()
            request, metadata = self._interceptor.pre_write_file(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataformRestTransport._BaseWriteFile,
                    "_BaseWriteFile__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.dataform_v1.DataformClient.WriteFile",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "WriteFile",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DataformRestTransport._WriteFile._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = dataform.WriteFileResponse()
            pb_resp = dataform.WriteFileResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_write_file(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_write_file_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = dataform.WriteFileResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.dataform_v1.DataformClient.write_file",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "WriteFile",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def cancel_workflow_invocation(
        self,
    ) -> Callable[
        [dataform.CancelWorkflowInvocationRequest],
        dataform.CancelWorkflowInvocationResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CancelWorkflowInvocation(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def commit_repository_changes(
        self,
    ) -> Callable[
        [dataform.CommitRepositoryChangesRequest],
        dataform.CommitRepositoryChangesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CommitRepositoryChanges(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def commit_workspace_changes(
        self,
    ) -> Callable[
        [dataform.CommitWorkspaceChangesRequest],
        dataform.CommitWorkspaceChangesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CommitWorkspaceChanges(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def compute_repository_access_token_status(
        self,
    ) -> Callable[
        [dataform.ComputeRepositoryAccessTokenStatusRequest],
        dataform.ComputeRepositoryAccessTokenStatusResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ComputeRepositoryAccessTokenStatus(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def create_compilation_result(
        self,
    ) -> Callable[
        [dataform.CreateCompilationResultRequest], dataform.CompilationResult
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateCompilationResult(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def create_folder(
        self,
    ) -> Callable[[dataform.CreateFolderRequest], dataform.Folder]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateFolder(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_release_config(
        self,
    ) -> Callable[[dataform.CreateReleaseConfigRequest], dataform.ReleaseConfig]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateReleaseConfig(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_repository(
        self,
    ) -> Callable[[dataform.CreateRepositoryRequest], dataform.Repository]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateRepository(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_team_folder(
        self,
    ) -> Callable[[dataform.CreateTeamFolderRequest], dataform.TeamFolder]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateTeamFolder(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_workflow_config(
        self,
    ) -> Callable[[dataform.CreateWorkflowConfigRequest], dataform.WorkflowConfig]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateWorkflowConfig(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_workflow_invocation(
        self,
    ) -> Callable[
        [dataform.CreateWorkflowInvocationRequest], dataform.WorkflowInvocation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateWorkflowInvocation(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def create_workspace(
        self,
    ) -> Callable[[dataform.CreateWorkspaceRequest], dataform.Workspace]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateWorkspace(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_folder(
        self,
    ) -> Callable[[dataform.DeleteFolderRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteFolder(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_folder_tree(
        self,
    ) -> Callable[[dataform.DeleteFolderTreeRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteFolderTree(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_release_config(
        self,
    ) -> Callable[[dataform.DeleteReleaseConfigRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteReleaseConfig(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_repository(
        self,
    ) -> Callable[[dataform.DeleteRepositoryRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteRepository(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_team_folder(
        self,
    ) -> Callable[[dataform.DeleteTeamFolderRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteTeamFolder(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_team_folder_tree(
        self,
    ) -> Callable[[dataform.DeleteTeamFolderTreeRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteTeamFolderTree(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_workflow_config(
        self,
    ) -> Callable[[dataform.DeleteWorkflowConfigRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteWorkflowConfig(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_workflow_invocation(
        self,
    ) -> Callable[[dataform.DeleteWorkflowInvocationRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteWorkflowInvocation(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def delete_workspace(
        self,
    ) -> Callable[[dataform.DeleteWorkspaceRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteWorkspace(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def fetch_file_diff(
        self,
    ) -> Callable[[dataform.FetchFileDiffRequest], dataform.FetchFileDiffResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._FetchFileDiff(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def fetch_file_git_statuses(
        self,
    ) -> Callable[
        [dataform.FetchFileGitStatusesRequest], dataform.FetchFileGitStatusesResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._FetchFileGitStatuses(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def fetch_git_ahead_behind(
        self,
    ) -> Callable[
        [dataform.FetchGitAheadBehindRequest], dataform.FetchGitAheadBehindResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._FetchGitAheadBehind(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def fetch_remote_branches(
        self,
    ) -> Callable[
        [dataform.FetchRemoteBranchesRequest], dataform.FetchRemoteBranchesResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._FetchRemoteBranches(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def fetch_repository_history(
        self,
    ) -> Callable[
        [dataform.FetchRepositoryHistoryRequest],
        dataform.FetchRepositoryHistoryResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._FetchRepositoryHistory(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def get_compilation_result(
        self,
    ) -> Callable[[dataform.GetCompilationResultRequest], dataform.CompilationResult]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetCompilationResult(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_config(self) -> Callable[[dataform.GetConfigRequest], dataform.Config]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetConfig(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_folder(self) -> Callable[[dataform.GetFolderRequest], dataform.Folder]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetFolder(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_iam_policy(
        self,
    ) -> Callable[[iam_policy_pb2.GetIamPolicyRequest], policy_pb2.Policy]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetIamPolicy(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_release_config(
        self,
    ) -> Callable[[dataform.GetReleaseConfigRequest], dataform.ReleaseConfig]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetReleaseConfig(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_repository(
        self,
    ) -> Callable[[dataform.GetRepositoryRequest], dataform.Repository]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetRepository(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_team_folder(
        self,
    ) -> Callable[[dataform.GetTeamFolderRequest], dataform.TeamFolder]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetTeamFolder(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_workflow_config(
        self,
    ) -> Callable[[dataform.GetWorkflowConfigRequest], dataform.WorkflowConfig]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetWorkflowConfig(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_workflow_invocation(
        self,
    ) -> Callable[[dataform.GetWorkflowInvocationRequest], dataform.WorkflowInvocation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetWorkflowInvocation(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_workspace(
        self,
    ) -> Callable[[dataform.GetWorkspaceRequest], dataform.Workspace]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetWorkspace(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def install_npm_packages(
        self,
    ) -> Callable[
        [dataform.InstallNpmPackagesRequest], dataform.InstallNpmPackagesResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._InstallNpmPackages(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_compilation_results(
        self,
    ) -> Callable[
        [dataform.ListCompilationResultsRequest],
        dataform.ListCompilationResultsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListCompilationResults(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def list_release_configs(
        self,
    ) -> Callable[
        [dataform.ListReleaseConfigsRequest], dataform.ListReleaseConfigsResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListReleaseConfigs(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_repositories(
        self,
    ) -> Callable[
        [dataform.ListRepositoriesRequest], dataform.ListRepositoriesResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListRepositories(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_workflow_configs(
        self,
    ) -> Callable[
        [dataform.ListWorkflowConfigsRequest], dataform.ListWorkflowConfigsResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListWorkflowConfigs(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_workflow_invocations(
        self,
    ) -> Callable[
        [dataform.ListWorkflowInvocationsRequest],
        dataform.ListWorkflowInvocationsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListWorkflowInvocations(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def list_workspaces(
        self,
    ) -> Callable[[dataform.ListWorkspacesRequest], dataform.ListWorkspacesResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListWorkspaces(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def make_directory(
        self,
    ) -> Callable[[dataform.MakeDirectoryRequest], dataform.MakeDirectoryResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._MakeDirectory(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def move_directory(
        self,
    ) -> Callable[[dataform.MoveDirectoryRequest], dataform.MoveDirectoryResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._MoveDirectory(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def move_file(
        self,
    ) -> Callable[[dataform.MoveFileRequest], dataform.MoveFileResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._MoveFile(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def move_folder(
        self,
    ) -> Callable[[dataform.MoveFolderRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._MoveFolder(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def move_repository(
        self,
    ) -> Callable[[dataform.MoveRepositoryRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._MoveRepository(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def pull_git_commits(
        self,
    ) -> Callable[[dataform.PullGitCommitsRequest], dataform.PullGitCommitsResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._PullGitCommits(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def push_git_commits(
        self,
    ) -> Callable[[dataform.PushGitCommitsRequest], dataform.PushGitCommitsResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._PushGitCommits(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def query_compilation_result_actions(
        self,
    ) -> Callable[
        [dataform.QueryCompilationResultActionsRequest],
        dataform.QueryCompilationResultActionsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._QueryCompilationResultActions(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def query_directory_contents(
        self,
    ) -> Callable[
        [dataform.QueryDirectoryContentsRequest],
        dataform.QueryDirectoryContentsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._QueryDirectoryContents(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def query_folder_contents(
        self,
    ) -> Callable[
        [dataform.QueryFolderContentsRequest], dataform.QueryFolderContentsResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._QueryFolderContents(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def query_repository_directory_contents(
        self,
    ) -> Callable[
        [dataform.QueryRepositoryDirectoryContentsRequest],
        dataform.QueryRepositoryDirectoryContentsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._QueryRepositoryDirectoryContents(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def query_team_folder_contents(
        self,
    ) -> Callable[
        [dataform.QueryTeamFolderContentsRequest],
        dataform.QueryTeamFolderContentsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._QueryTeamFolderContents(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def query_user_root_contents(
        self,
    ) -> Callable[
        [dataform.QueryUserRootContentsRequest], dataform.QueryUserRootContentsResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._QueryUserRootContents(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def query_workflow_invocation_actions(
        self,
    ) -> Callable[
        [dataform.QueryWorkflowInvocationActionsRequest],
        dataform.QueryWorkflowInvocationActionsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._QueryWorkflowInvocationActions(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def read_file(
        self,
    ) -> Callable[[dataform.ReadFileRequest], dataform.ReadFileResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ReadFile(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def read_repository_file(
        self,
    ) -> Callable[
        [dataform.ReadRepositoryFileRequest], dataform.ReadRepositoryFileResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ReadRepositoryFile(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def remove_directory(
        self,
    ) -> Callable[[dataform.RemoveDirectoryRequest], dataform.RemoveDirectoryResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._RemoveDirectory(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def remove_file(
        self,
    ) -> Callable[[dataform.RemoveFileRequest], dataform.RemoveFileResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._RemoveFile(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def reset_workspace_changes(
        self,
    ) -> Callable[
        [dataform.ResetWorkspaceChangesRequest], dataform.ResetWorkspaceChangesResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ResetWorkspaceChanges(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def search_files(
        self,
    ) -> Callable[[dataform.SearchFilesRequest], dataform.SearchFilesResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._SearchFiles(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def search_team_folders(
        self,
    ) -> Callable[
        [dataform.SearchTeamFoldersRequest], dataform.SearchTeamFoldersResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._SearchTeamFolders(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def set_iam_policy(
        self,
    ) -> Callable[[iam_policy_pb2.SetIamPolicyRequest], policy_pb2.Policy]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._SetIamPolicy(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def test_iam_permissions(
        self,
    ) -> Callable[
        [iam_policy_pb2.TestIamPermissionsRequest],
        iam_policy_pb2.TestIamPermissionsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._TestIamPermissions(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_config(
        self,
    ) -> Callable[[dataform.UpdateConfigRequest], dataform.Config]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateConfig(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_folder(
        self,
    ) -> Callable[[dataform.UpdateFolderRequest], dataform.Folder]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateFolder(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_release_config(
        self,
    ) -> Callable[[dataform.UpdateReleaseConfigRequest], dataform.ReleaseConfig]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateReleaseConfig(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_repository(
        self,
    ) -> Callable[[dataform.UpdateRepositoryRequest], dataform.Repository]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateRepository(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_team_folder(
        self,
    ) -> Callable[[dataform.UpdateTeamFolderRequest], dataform.TeamFolder]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateTeamFolder(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_workflow_config(
        self,
    ) -> Callable[[dataform.UpdateWorkflowConfigRequest], dataform.WorkflowConfig]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateWorkflowConfig(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def write_file(
        self,
    ) -> Callable[[dataform.WriteFileRequest], dataform.WriteFileResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._WriteFile(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_location(self):
        return self._GetLocation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetLocation(_BaseDataformRestTransport._BaseGetLocation, DataformRestStub):
        def __hash__(self):
            return hash("DataformRestTransport.GetLocation")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: locations_pb2.GetLocationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> locations_pb2.Location:
            r"""Call the get location method over HTTP.

            Args:
                request (locations_pb2.GetLocationRequest):
                    The request object for GetLocation method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                locations_pb2.Location: Response from GetLocation method.
            """

            http_options = (
                _BaseDataformRestTransport._BaseGetLocation._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_location(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataformRestTransport._BaseGetLocation,
                    "_BaseGetLocation__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=False,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = json_format.MessageToJson(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.dataform_v1.DataformClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "GetLocation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DataformRestTransport._GetLocation._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            content = response.content.decode("utf-8")
            resp = locations_pb2.Location()
            resp = json_format.Parse(content, resp)
            resp = self._interceptor.post_get_location(resp)
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = json_format.MessageToJson(resp)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.dataform_v1.DataformAsyncClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "GetLocation",
                        "httpResponse": http_response,
                        "metadata": http_response["headers"],
                    },
                )
            return resp

    @property
    def list_locations(self):
        return self._ListLocations(self._session, self._host, self._interceptor)  # type: ignore

    class _ListLocations(
        _BaseDataformRestTransport._BaseListLocations, DataformRestStub
    ):
        def __hash__(self):
            return hash("DataformRestTransport.ListLocations")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: locations_pb2.ListLocationsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> locations_pb2.ListLocationsResponse:
            r"""Call the list locations method over HTTP.

            Args:
                request (locations_pb2.ListLocationsRequest):
                    The request object for ListLocations method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                locations_pb2.ListLocationsResponse: Response from ListLocations method.
            """

            http_options = (
                _BaseDataformRestTransport._BaseListLocations._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_locations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataformRestTransport._BaseListLocations,
                    "_BaseListLocations__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=False,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = json_format.MessageToJson(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.dataform_v1.DataformClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "ListLocations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DataformRestTransport._ListLocations._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            content = response.content.decode("utf-8")
            resp = locations_pb2.ListLocationsResponse()
            resp = json_format.Parse(content, resp)
            resp = self._interceptor.post_list_locations(resp)
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = json_format.MessageToJson(resp)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.dataform_v1.DataformAsyncClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "ListLocations",
                        "httpResponse": http_response,
                        "metadata": http_response["headers"],
                    },
                )
            return resp

    @property
    def cancel_operation(self):
        return self._CancelOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _CancelOperation(
        _BaseDataformRestTransport._BaseCancelOperation, DataformRestStub
    ):
        def __hash__(self):
            return hash("DataformRestTransport.CancelOperation")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )
            return response

        def __call__(
            self,
            request: operations_pb2.CancelOperationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> None:
            r"""Call the cancel operation method over HTTP.

            Args:
                request (operations_pb2.CancelOperationRequest):
                    The request object for CancelOperation method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = (
                _BaseDataformRestTransport._BaseCancelOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_cancel_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataformRestTransport._BaseCancelOperation,
                    "_BaseCancelOperation__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=False,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = json_format.MessageToJson(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.dataform_v1.DataformClient.CancelOperation",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "CancelOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DataformRestTransport._CancelOperation._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            return self._interceptor.post_cancel_operation(None)

    @property
    def delete_operation(self):
        return self._DeleteOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _DeleteOperation(
        _BaseDataformRestTransport._BaseDeleteOperation, DataformRestStub
    ):
        def __hash__(self):
            return hash("DataformRestTransport.DeleteOperation")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: operations_pb2.DeleteOperationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> None:
            r"""Call the delete operation method over HTTP.

            Args:
                request (operations_pb2.DeleteOperationRequest):
                    The request object for DeleteOperation method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = (
                _BaseDataformRestTransport._BaseDeleteOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataformRestTransport._BaseDeleteOperation,
                    "_BaseDeleteOperation__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=False,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = json_format.MessageToJson(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.dataform_v1.DataformClient.DeleteOperation",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "DeleteOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DataformRestTransport._DeleteOperation._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            return self._interceptor.post_delete_operation(None)

    @property
    def get_operation(self):
        return self._GetOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetOperation(_BaseDataformRestTransport._BaseGetOperation, DataformRestStub):
        def __hash__(self):
            return hash("DataformRestTransport.GetOperation")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: operations_pb2.GetOperationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the get operation method over HTTP.

            Args:
                request (operations_pb2.GetOperationRequest):
                    The request object for GetOperation method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                operations_pb2.Operation: Response from GetOperation method.
            """

            http_options = (
                _BaseDataformRestTransport._BaseGetOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_operation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataformRestTransport._BaseGetOperation,
                    "_BaseGetOperation__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=False,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = json_format.MessageToJson(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.dataform_v1.DataformClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "GetOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DataformRestTransport._GetOperation._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            content = response.content.decode("utf-8")
            resp = operations_pb2.Operation()
            resp = json_format.Parse(content, resp)
            resp = self._interceptor.post_get_operation(resp)
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = json_format.MessageToJson(resp)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.dataform_v1.DataformAsyncClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "GetOperation",
                        "httpResponse": http_response,
                        "metadata": http_response["headers"],
                    },
                )
            return resp

    @property
    def list_operations(self):
        return self._ListOperations(self._session, self._host, self._interceptor)  # type: ignore

    class _ListOperations(
        _BaseDataformRestTransport._BaseListOperations, DataformRestStub
    ):
        def __hash__(self):
            return hash("DataformRestTransport.ListOperations")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: operations_pb2.ListOperationsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.ListOperationsResponse:
            r"""Call the list operations method over HTTP.

            Args:
                request (operations_pb2.ListOperationsRequest):
                    The request object for ListOperations method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                operations_pb2.ListOperationsResponse: Response from ListOperations method.
            """

            http_options = (
                _BaseDataformRestTransport._BaseListOperations._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_operations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataformRestTransport._BaseListOperations,
                    "_BaseListOperations__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=False,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = json_format.MessageToJson(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.dataform_v1.DataformClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "ListOperations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DataformRestTransport._ListOperations._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            content = response.content.decode("utf-8")
            resp = operations_pb2.ListOperationsResponse()
            resp = json_format.Parse(content, resp)
            resp = self._interceptor.post_list_operations(resp)
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = json_format.MessageToJson(resp)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.dataform_v1.DataformAsyncClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.dataform.v1.Dataform",
                        "rpcName": "ListOperations",
                        "httpResponse": http_response,
                        "metadata": http_response["headers"],
                    },
                )
            return resp

    @property
    def kind(self) -> str:
        return "rest"

    def close(self):
        self._session.close()


__all__ = ("DataformRestTransport",)
