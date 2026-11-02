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

from google.cloud.securesourcemanager_v1._compat import transcode_request
from google.cloud.securesourcemanager_v1.types import secure_source_manager

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseSecureSourceManagerRestTransport

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


class SecureSourceManagerRestInterceptor:
    """Interceptor for SecureSourceManager.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the SecureSourceManagerRestTransport.

    .. code-block:: python
        class MyCustomSecureSourceManagerInterceptor(SecureSourceManagerRestInterceptor):
            def pre_batch_create_pull_request_comments(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_create_pull_request_comments(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_close_issue(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_close_issue(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_close_pull_request(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_close_pull_request(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_branch_rule(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_branch_rule(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_hook(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_hook(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_instance(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_instance(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_issue(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_issue(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_issue_comment(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_issue_comment(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_pull_request(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_pull_request(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_pull_request_comment(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_pull_request_comment(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_repository(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_repository(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_branch_rule(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_branch_rule(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_hook(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_hook(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_instance(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_instance(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_issue(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_issue(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_issue_comment(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_issue_comment(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_pull_request_comment(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_pull_request_comment(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_repository(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_repository(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_fetch_blob(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_fetch_blob(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_fetch_refs(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_fetch_refs(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_fetch_tree(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_fetch_tree(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_branch_rule(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_branch_rule(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_hook(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_hook(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_iam_policy_repo(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_iam_policy_repo(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_instance(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_instance(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_issue(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_issue(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_issue_comment(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_issue_comment(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_pull_request(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_pull_request(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_pull_request_comment(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_pull_request_comment(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_repository(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_repository(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_branch_rules(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_branch_rules(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_hooks(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_hooks(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_instances(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_instances(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_issue_comments(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_issue_comments(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_issues(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_issues(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_pull_request_comments(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_pull_request_comments(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_pull_request_file_diffs(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_pull_request_file_diffs(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_pull_requests(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_pull_requests(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_repositories(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_repositories(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_merge_pull_request(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_merge_pull_request(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_open_issue(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_open_issue(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_open_pull_request(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_open_pull_request(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_resolve_pull_request_comments(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_resolve_pull_request_comments(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_set_iam_policy_repo(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_set_iam_policy_repo(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_test_iam_permissions_repo(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_test_iam_permissions_repo(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_unresolve_pull_request_comments(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_unresolve_pull_request_comments(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_branch_rule(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_branch_rule(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_hook(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_hook(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_issue(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_issue(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_issue_comment(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_issue_comment(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_pull_request(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_pull_request(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_pull_request_comment(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_pull_request_comment(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_repository(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_repository(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = SecureSourceManagerRestTransport(interceptor=MyCustomSecureSourceManagerInterceptor())
        client = SecureSourceManagerClient(transport=transport)


    """

    def pre_batch_create_pull_request_comments(
        self,
        request: secure_source_manager.BatchCreatePullRequestCommentsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        secure_source_manager.BatchCreatePullRequestCommentsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_create_pull_request_comments

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SecureSourceManager server.
        """
        return request, metadata

    def post_batch_create_pull_request_comments(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for batch_create_pull_request_comments

        DEPRECATED. Please use the `post_batch_create_pull_request_comments_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SecureSourceManager server but before
        it is returned to user code. This `post_batch_create_pull_request_comments` interceptor runs
        before the `post_batch_create_pull_request_comments_with_metadata` interceptor.
        """
        return response

    def post_batch_create_pull_request_comments_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for batch_create_pull_request_comments

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SecureSourceManager server but before it is returned to user code.

        We recommend only using this `post_batch_create_pull_request_comments_with_metadata`
        interceptor in new development instead of the `post_batch_create_pull_request_comments` interceptor.
        When both interceptors are used, this `post_batch_create_pull_request_comments_with_metadata` interceptor runs after the
        `post_batch_create_pull_request_comments` interceptor. The (possibly modified) response returned by
        `post_batch_create_pull_request_comments` will be passed to
        `post_batch_create_pull_request_comments_with_metadata`.
        """
        return response, metadata

    def pre_close_issue(
        self,
        request: secure_source_manager.CloseIssueRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        secure_source_manager.CloseIssueRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for close_issue

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SecureSourceManager server.
        """
        return request, metadata

    def post_close_issue(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for close_issue

        DEPRECATED. Please use the `post_close_issue_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SecureSourceManager server but before
        it is returned to user code. This `post_close_issue` interceptor runs
        before the `post_close_issue_with_metadata` interceptor.
        """
        return response

    def post_close_issue_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for close_issue

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SecureSourceManager server but before it is returned to user code.

        We recommend only using this `post_close_issue_with_metadata`
        interceptor in new development instead of the `post_close_issue` interceptor.
        When both interceptors are used, this `post_close_issue_with_metadata` interceptor runs after the
        `post_close_issue` interceptor. The (possibly modified) response returned by
        `post_close_issue` will be passed to
        `post_close_issue_with_metadata`.
        """
        return response, metadata

    def pre_close_pull_request(
        self,
        request: secure_source_manager.ClosePullRequestRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        secure_source_manager.ClosePullRequestRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for close_pull_request

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SecureSourceManager server.
        """
        return request, metadata

    def post_close_pull_request(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for close_pull_request

        DEPRECATED. Please use the `post_close_pull_request_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SecureSourceManager server but before
        it is returned to user code. This `post_close_pull_request` interceptor runs
        before the `post_close_pull_request_with_metadata` interceptor.
        """
        return response

    def post_close_pull_request_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for close_pull_request

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SecureSourceManager server but before it is returned to user code.

        We recommend only using this `post_close_pull_request_with_metadata`
        interceptor in new development instead of the `post_close_pull_request` interceptor.
        When both interceptors are used, this `post_close_pull_request_with_metadata` interceptor runs after the
        `post_close_pull_request` interceptor. The (possibly modified) response returned by
        `post_close_pull_request` will be passed to
        `post_close_pull_request_with_metadata`.
        """
        return response, metadata

    def pre_create_branch_rule(
        self,
        request: secure_source_manager.CreateBranchRuleRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        secure_source_manager.CreateBranchRuleRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_branch_rule

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SecureSourceManager server.
        """
        return request, metadata

    def post_create_branch_rule(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_branch_rule

        DEPRECATED. Please use the `post_create_branch_rule_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SecureSourceManager server but before
        it is returned to user code. This `post_create_branch_rule` interceptor runs
        before the `post_create_branch_rule_with_metadata` interceptor.
        """
        return response

    def post_create_branch_rule_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_branch_rule

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SecureSourceManager server but before it is returned to user code.

        We recommend only using this `post_create_branch_rule_with_metadata`
        interceptor in new development instead of the `post_create_branch_rule` interceptor.
        When both interceptors are used, this `post_create_branch_rule_with_metadata` interceptor runs after the
        `post_create_branch_rule` interceptor. The (possibly modified) response returned by
        `post_create_branch_rule` will be passed to
        `post_create_branch_rule_with_metadata`.
        """
        return response, metadata

    def pre_create_hook(
        self,
        request: secure_source_manager.CreateHookRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        secure_source_manager.CreateHookRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_hook

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SecureSourceManager server.
        """
        return request, metadata

    def post_create_hook(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_hook

        DEPRECATED. Please use the `post_create_hook_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SecureSourceManager server but before
        it is returned to user code. This `post_create_hook` interceptor runs
        before the `post_create_hook_with_metadata` interceptor.
        """
        return response

    def post_create_hook_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_hook

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SecureSourceManager server but before it is returned to user code.

        We recommend only using this `post_create_hook_with_metadata`
        interceptor in new development instead of the `post_create_hook` interceptor.
        When both interceptors are used, this `post_create_hook_with_metadata` interceptor runs after the
        `post_create_hook` interceptor. The (possibly modified) response returned by
        `post_create_hook` will be passed to
        `post_create_hook_with_metadata`.
        """
        return response, metadata

    def pre_create_instance(
        self,
        request: secure_source_manager.CreateInstanceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        secure_source_manager.CreateInstanceRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_instance

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SecureSourceManager server.
        """
        return request, metadata

    def post_create_instance(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_instance

        DEPRECATED. Please use the `post_create_instance_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SecureSourceManager server but before
        it is returned to user code. This `post_create_instance` interceptor runs
        before the `post_create_instance_with_metadata` interceptor.
        """
        return response

    def post_create_instance_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_instance

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SecureSourceManager server but before it is returned to user code.

        We recommend only using this `post_create_instance_with_metadata`
        interceptor in new development instead of the `post_create_instance` interceptor.
        When both interceptors are used, this `post_create_instance_with_metadata` interceptor runs after the
        `post_create_instance` interceptor. The (possibly modified) response returned by
        `post_create_instance` will be passed to
        `post_create_instance_with_metadata`.
        """
        return response, metadata

    def pre_create_issue(
        self,
        request: secure_source_manager.CreateIssueRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        secure_source_manager.CreateIssueRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_issue

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SecureSourceManager server.
        """
        return request, metadata

    def post_create_issue(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_issue

        DEPRECATED. Please use the `post_create_issue_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SecureSourceManager server but before
        it is returned to user code. This `post_create_issue` interceptor runs
        before the `post_create_issue_with_metadata` interceptor.
        """
        return response

    def post_create_issue_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_issue

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SecureSourceManager server but before it is returned to user code.

        We recommend only using this `post_create_issue_with_metadata`
        interceptor in new development instead of the `post_create_issue` interceptor.
        When both interceptors are used, this `post_create_issue_with_metadata` interceptor runs after the
        `post_create_issue` interceptor. The (possibly modified) response returned by
        `post_create_issue` will be passed to
        `post_create_issue_with_metadata`.
        """
        return response, metadata

    def pre_create_issue_comment(
        self,
        request: secure_source_manager.CreateIssueCommentRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        secure_source_manager.CreateIssueCommentRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_issue_comment

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SecureSourceManager server.
        """
        return request, metadata

    def post_create_issue_comment(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_issue_comment

        DEPRECATED. Please use the `post_create_issue_comment_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SecureSourceManager server but before
        it is returned to user code. This `post_create_issue_comment` interceptor runs
        before the `post_create_issue_comment_with_metadata` interceptor.
        """
        return response

    def post_create_issue_comment_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_issue_comment

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SecureSourceManager server but before it is returned to user code.

        We recommend only using this `post_create_issue_comment_with_metadata`
        interceptor in new development instead of the `post_create_issue_comment` interceptor.
        When both interceptors are used, this `post_create_issue_comment_with_metadata` interceptor runs after the
        `post_create_issue_comment` interceptor. The (possibly modified) response returned by
        `post_create_issue_comment` will be passed to
        `post_create_issue_comment_with_metadata`.
        """
        return response, metadata

    def pre_create_pull_request(
        self,
        request: secure_source_manager.CreatePullRequestRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        secure_source_manager.CreatePullRequestRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_pull_request

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SecureSourceManager server.
        """
        return request, metadata

    def post_create_pull_request(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_pull_request

        DEPRECATED. Please use the `post_create_pull_request_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SecureSourceManager server but before
        it is returned to user code. This `post_create_pull_request` interceptor runs
        before the `post_create_pull_request_with_metadata` interceptor.
        """
        return response

    def post_create_pull_request_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_pull_request

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SecureSourceManager server but before it is returned to user code.

        We recommend only using this `post_create_pull_request_with_metadata`
        interceptor in new development instead of the `post_create_pull_request` interceptor.
        When both interceptors are used, this `post_create_pull_request_with_metadata` interceptor runs after the
        `post_create_pull_request` interceptor. The (possibly modified) response returned by
        `post_create_pull_request` will be passed to
        `post_create_pull_request_with_metadata`.
        """
        return response, metadata

    def pre_create_pull_request_comment(
        self,
        request: secure_source_manager.CreatePullRequestCommentRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        secure_source_manager.CreatePullRequestCommentRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_pull_request_comment

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SecureSourceManager server.
        """
        return request, metadata

    def post_create_pull_request_comment(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_pull_request_comment

        DEPRECATED. Please use the `post_create_pull_request_comment_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SecureSourceManager server but before
        it is returned to user code. This `post_create_pull_request_comment` interceptor runs
        before the `post_create_pull_request_comment_with_metadata` interceptor.
        """
        return response

    def post_create_pull_request_comment_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_pull_request_comment

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SecureSourceManager server but before it is returned to user code.

        We recommend only using this `post_create_pull_request_comment_with_metadata`
        interceptor in new development instead of the `post_create_pull_request_comment` interceptor.
        When both interceptors are used, this `post_create_pull_request_comment_with_metadata` interceptor runs after the
        `post_create_pull_request_comment` interceptor. The (possibly modified) response returned by
        `post_create_pull_request_comment` will be passed to
        `post_create_pull_request_comment_with_metadata`.
        """
        return response, metadata

    def pre_create_repository(
        self,
        request: secure_source_manager.CreateRepositoryRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        secure_source_manager.CreateRepositoryRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_repository

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SecureSourceManager server.
        """
        return request, metadata

    def post_create_repository(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_repository

        DEPRECATED. Please use the `post_create_repository_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SecureSourceManager server but before
        it is returned to user code. This `post_create_repository` interceptor runs
        before the `post_create_repository_with_metadata` interceptor.
        """
        return response

    def post_create_repository_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_repository

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SecureSourceManager server but before it is returned to user code.

        We recommend only using this `post_create_repository_with_metadata`
        interceptor in new development instead of the `post_create_repository` interceptor.
        When both interceptors are used, this `post_create_repository_with_metadata` interceptor runs after the
        `post_create_repository` interceptor. The (possibly modified) response returned by
        `post_create_repository` will be passed to
        `post_create_repository_with_metadata`.
        """
        return response, metadata

    def pre_delete_branch_rule(
        self,
        request: secure_source_manager.DeleteBranchRuleRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        secure_source_manager.DeleteBranchRuleRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_branch_rule

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SecureSourceManager server.
        """
        return request, metadata

    def post_delete_branch_rule(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_branch_rule

        DEPRECATED. Please use the `post_delete_branch_rule_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SecureSourceManager server but before
        it is returned to user code. This `post_delete_branch_rule` interceptor runs
        before the `post_delete_branch_rule_with_metadata` interceptor.
        """
        return response

    def post_delete_branch_rule_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_branch_rule

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SecureSourceManager server but before it is returned to user code.

        We recommend only using this `post_delete_branch_rule_with_metadata`
        interceptor in new development instead of the `post_delete_branch_rule` interceptor.
        When both interceptors are used, this `post_delete_branch_rule_with_metadata` interceptor runs after the
        `post_delete_branch_rule` interceptor. The (possibly modified) response returned by
        `post_delete_branch_rule` will be passed to
        `post_delete_branch_rule_with_metadata`.
        """
        return response, metadata

    def pre_delete_hook(
        self,
        request: secure_source_manager.DeleteHookRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        secure_source_manager.DeleteHookRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_hook

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SecureSourceManager server.
        """
        return request, metadata

    def post_delete_hook(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_hook

        DEPRECATED. Please use the `post_delete_hook_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SecureSourceManager server but before
        it is returned to user code. This `post_delete_hook` interceptor runs
        before the `post_delete_hook_with_metadata` interceptor.
        """
        return response

    def post_delete_hook_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_hook

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SecureSourceManager server but before it is returned to user code.

        We recommend only using this `post_delete_hook_with_metadata`
        interceptor in new development instead of the `post_delete_hook` interceptor.
        When both interceptors are used, this `post_delete_hook_with_metadata` interceptor runs after the
        `post_delete_hook` interceptor. The (possibly modified) response returned by
        `post_delete_hook` will be passed to
        `post_delete_hook_with_metadata`.
        """
        return response, metadata

    def pre_delete_instance(
        self,
        request: secure_source_manager.DeleteInstanceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        secure_source_manager.DeleteInstanceRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_instance

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SecureSourceManager server.
        """
        return request, metadata

    def post_delete_instance(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_instance

        DEPRECATED. Please use the `post_delete_instance_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SecureSourceManager server but before
        it is returned to user code. This `post_delete_instance` interceptor runs
        before the `post_delete_instance_with_metadata` interceptor.
        """
        return response

    def post_delete_instance_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_instance

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SecureSourceManager server but before it is returned to user code.

        We recommend only using this `post_delete_instance_with_metadata`
        interceptor in new development instead of the `post_delete_instance` interceptor.
        When both interceptors are used, this `post_delete_instance_with_metadata` interceptor runs after the
        `post_delete_instance` interceptor. The (possibly modified) response returned by
        `post_delete_instance` will be passed to
        `post_delete_instance_with_metadata`.
        """
        return response, metadata

    def pre_delete_issue(
        self,
        request: secure_source_manager.DeleteIssueRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        secure_source_manager.DeleteIssueRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_issue

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SecureSourceManager server.
        """
        return request, metadata

    def post_delete_issue(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_issue

        DEPRECATED. Please use the `post_delete_issue_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SecureSourceManager server but before
        it is returned to user code. This `post_delete_issue` interceptor runs
        before the `post_delete_issue_with_metadata` interceptor.
        """
        return response

    def post_delete_issue_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_issue

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SecureSourceManager server but before it is returned to user code.

        We recommend only using this `post_delete_issue_with_metadata`
        interceptor in new development instead of the `post_delete_issue` interceptor.
        When both interceptors are used, this `post_delete_issue_with_metadata` interceptor runs after the
        `post_delete_issue` interceptor. The (possibly modified) response returned by
        `post_delete_issue` will be passed to
        `post_delete_issue_with_metadata`.
        """
        return response, metadata

    def pre_delete_issue_comment(
        self,
        request: secure_source_manager.DeleteIssueCommentRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        secure_source_manager.DeleteIssueCommentRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_issue_comment

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SecureSourceManager server.
        """
        return request, metadata

    def post_delete_issue_comment(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_issue_comment

        DEPRECATED. Please use the `post_delete_issue_comment_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SecureSourceManager server but before
        it is returned to user code. This `post_delete_issue_comment` interceptor runs
        before the `post_delete_issue_comment_with_metadata` interceptor.
        """
        return response

    def post_delete_issue_comment_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_issue_comment

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SecureSourceManager server but before it is returned to user code.

        We recommend only using this `post_delete_issue_comment_with_metadata`
        interceptor in new development instead of the `post_delete_issue_comment` interceptor.
        When both interceptors are used, this `post_delete_issue_comment_with_metadata` interceptor runs after the
        `post_delete_issue_comment` interceptor. The (possibly modified) response returned by
        `post_delete_issue_comment` will be passed to
        `post_delete_issue_comment_with_metadata`.
        """
        return response, metadata

    def pre_delete_pull_request_comment(
        self,
        request: secure_source_manager.DeletePullRequestCommentRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        secure_source_manager.DeletePullRequestCommentRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_pull_request_comment

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SecureSourceManager server.
        """
        return request, metadata

    def post_delete_pull_request_comment(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_pull_request_comment

        DEPRECATED. Please use the `post_delete_pull_request_comment_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SecureSourceManager server but before
        it is returned to user code. This `post_delete_pull_request_comment` interceptor runs
        before the `post_delete_pull_request_comment_with_metadata` interceptor.
        """
        return response

    def post_delete_pull_request_comment_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_pull_request_comment

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SecureSourceManager server but before it is returned to user code.

        We recommend only using this `post_delete_pull_request_comment_with_metadata`
        interceptor in new development instead of the `post_delete_pull_request_comment` interceptor.
        When both interceptors are used, this `post_delete_pull_request_comment_with_metadata` interceptor runs after the
        `post_delete_pull_request_comment` interceptor. The (possibly modified) response returned by
        `post_delete_pull_request_comment` will be passed to
        `post_delete_pull_request_comment_with_metadata`.
        """
        return response, metadata

    def pre_delete_repository(
        self,
        request: secure_source_manager.DeleteRepositoryRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        secure_source_manager.DeleteRepositoryRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_repository

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SecureSourceManager server.
        """
        return request, metadata

    def post_delete_repository(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_repository

        DEPRECATED. Please use the `post_delete_repository_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SecureSourceManager server but before
        it is returned to user code. This `post_delete_repository` interceptor runs
        before the `post_delete_repository_with_metadata` interceptor.
        """
        return response

    def post_delete_repository_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_repository

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SecureSourceManager server but before it is returned to user code.

        We recommend only using this `post_delete_repository_with_metadata`
        interceptor in new development instead of the `post_delete_repository` interceptor.
        When both interceptors are used, this `post_delete_repository_with_metadata` interceptor runs after the
        `post_delete_repository` interceptor. The (possibly modified) response returned by
        `post_delete_repository` will be passed to
        `post_delete_repository_with_metadata`.
        """
        return response, metadata

    def pre_fetch_blob(
        self,
        request: secure_source_manager.FetchBlobRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        secure_source_manager.FetchBlobRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for fetch_blob

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SecureSourceManager server.
        """
        return request, metadata

    def post_fetch_blob(
        self, response: secure_source_manager.FetchBlobResponse
    ) -> secure_source_manager.FetchBlobResponse:
        """Post-rpc interceptor for fetch_blob

        DEPRECATED. Please use the `post_fetch_blob_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SecureSourceManager server but before
        it is returned to user code. This `post_fetch_blob` interceptor runs
        before the `post_fetch_blob_with_metadata` interceptor.
        """
        return response

    def post_fetch_blob_with_metadata(
        self,
        response: secure_source_manager.FetchBlobResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        secure_source_manager.FetchBlobResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for fetch_blob

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SecureSourceManager server but before it is returned to user code.

        We recommend only using this `post_fetch_blob_with_metadata`
        interceptor in new development instead of the `post_fetch_blob` interceptor.
        When both interceptors are used, this `post_fetch_blob_with_metadata` interceptor runs after the
        `post_fetch_blob` interceptor. The (possibly modified) response returned by
        `post_fetch_blob` will be passed to
        `post_fetch_blob_with_metadata`.
        """
        return response, metadata

    def pre_fetch_refs(
        self,
        request: secure_source_manager.FetchRefsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        secure_source_manager.FetchRefsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for fetch_refs

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SecureSourceManager server.
        """
        return request, metadata

    def post_fetch_refs(
        self, response: secure_source_manager.FetchRefsResponse
    ) -> secure_source_manager.FetchRefsResponse:
        """Post-rpc interceptor for fetch_refs

        DEPRECATED. Please use the `post_fetch_refs_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SecureSourceManager server but before
        it is returned to user code. This `post_fetch_refs` interceptor runs
        before the `post_fetch_refs_with_metadata` interceptor.
        """
        return response

    def post_fetch_refs_with_metadata(
        self,
        response: secure_source_manager.FetchRefsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        secure_source_manager.FetchRefsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for fetch_refs

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SecureSourceManager server but before it is returned to user code.

        We recommend only using this `post_fetch_refs_with_metadata`
        interceptor in new development instead of the `post_fetch_refs` interceptor.
        When both interceptors are used, this `post_fetch_refs_with_metadata` interceptor runs after the
        `post_fetch_refs` interceptor. The (possibly modified) response returned by
        `post_fetch_refs` will be passed to
        `post_fetch_refs_with_metadata`.
        """
        return response, metadata

    def pre_fetch_tree(
        self,
        request: secure_source_manager.FetchTreeRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        secure_source_manager.FetchTreeRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for fetch_tree

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SecureSourceManager server.
        """
        return request, metadata

    def post_fetch_tree(
        self, response: secure_source_manager.FetchTreeResponse
    ) -> secure_source_manager.FetchTreeResponse:
        """Post-rpc interceptor for fetch_tree

        DEPRECATED. Please use the `post_fetch_tree_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SecureSourceManager server but before
        it is returned to user code. This `post_fetch_tree` interceptor runs
        before the `post_fetch_tree_with_metadata` interceptor.
        """
        return response

    def post_fetch_tree_with_metadata(
        self,
        response: secure_source_manager.FetchTreeResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        secure_source_manager.FetchTreeResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for fetch_tree

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SecureSourceManager server but before it is returned to user code.

        We recommend only using this `post_fetch_tree_with_metadata`
        interceptor in new development instead of the `post_fetch_tree` interceptor.
        When both interceptors are used, this `post_fetch_tree_with_metadata` interceptor runs after the
        `post_fetch_tree` interceptor. The (possibly modified) response returned by
        `post_fetch_tree` will be passed to
        `post_fetch_tree_with_metadata`.
        """
        return response, metadata

    def pre_get_branch_rule(
        self,
        request: secure_source_manager.GetBranchRuleRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        secure_source_manager.GetBranchRuleRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_branch_rule

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SecureSourceManager server.
        """
        return request, metadata

    def post_get_branch_rule(
        self, response: secure_source_manager.BranchRule
    ) -> secure_source_manager.BranchRule:
        """Post-rpc interceptor for get_branch_rule

        DEPRECATED. Please use the `post_get_branch_rule_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SecureSourceManager server but before
        it is returned to user code. This `post_get_branch_rule` interceptor runs
        before the `post_get_branch_rule_with_metadata` interceptor.
        """
        return response

    def post_get_branch_rule_with_metadata(
        self,
        response: secure_source_manager.BranchRule,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        secure_source_manager.BranchRule, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for get_branch_rule

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SecureSourceManager server but before it is returned to user code.

        We recommend only using this `post_get_branch_rule_with_metadata`
        interceptor in new development instead of the `post_get_branch_rule` interceptor.
        When both interceptors are used, this `post_get_branch_rule_with_metadata` interceptor runs after the
        `post_get_branch_rule` interceptor. The (possibly modified) response returned by
        `post_get_branch_rule` will be passed to
        `post_get_branch_rule_with_metadata`.
        """
        return response, metadata

    def pre_get_hook(
        self,
        request: secure_source_manager.GetHookRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        secure_source_manager.GetHookRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_hook

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SecureSourceManager server.
        """
        return request, metadata

    def post_get_hook(
        self, response: secure_source_manager.Hook
    ) -> secure_source_manager.Hook:
        """Post-rpc interceptor for get_hook

        DEPRECATED. Please use the `post_get_hook_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SecureSourceManager server but before
        it is returned to user code. This `post_get_hook` interceptor runs
        before the `post_get_hook_with_metadata` interceptor.
        """
        return response

    def post_get_hook_with_metadata(
        self,
        response: secure_source_manager.Hook,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[secure_source_manager.Hook, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_hook

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SecureSourceManager server but before it is returned to user code.

        We recommend only using this `post_get_hook_with_metadata`
        interceptor in new development instead of the `post_get_hook` interceptor.
        When both interceptors are used, this `post_get_hook_with_metadata` interceptor runs after the
        `post_get_hook` interceptor. The (possibly modified) response returned by
        `post_get_hook` will be passed to
        `post_get_hook_with_metadata`.
        """
        return response, metadata

    def pre_get_iam_policy_repo(
        self,
        request: iam_policy_pb2.GetIamPolicyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        iam_policy_pb2.GetIamPolicyRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_iam_policy_repo

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SecureSourceManager server.
        """
        return request, metadata

    def post_get_iam_policy_repo(
        self, response: policy_pb2.Policy
    ) -> policy_pb2.Policy:
        """Post-rpc interceptor for get_iam_policy_repo

        DEPRECATED. Please use the `post_get_iam_policy_repo_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SecureSourceManager server but before
        it is returned to user code. This `post_get_iam_policy_repo` interceptor runs
        before the `post_get_iam_policy_repo_with_metadata` interceptor.
        """
        return response

    def post_get_iam_policy_repo_with_metadata(
        self,
        response: policy_pb2.Policy,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[policy_pb2.Policy, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_iam_policy_repo

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SecureSourceManager server but before it is returned to user code.

        We recommend only using this `post_get_iam_policy_repo_with_metadata`
        interceptor in new development instead of the `post_get_iam_policy_repo` interceptor.
        When both interceptors are used, this `post_get_iam_policy_repo_with_metadata` interceptor runs after the
        `post_get_iam_policy_repo` interceptor. The (possibly modified) response returned by
        `post_get_iam_policy_repo` will be passed to
        `post_get_iam_policy_repo_with_metadata`.
        """
        return response, metadata

    def pre_get_instance(
        self,
        request: secure_source_manager.GetInstanceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        secure_source_manager.GetInstanceRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_instance

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SecureSourceManager server.
        """
        return request, metadata

    def post_get_instance(
        self, response: secure_source_manager.Instance
    ) -> secure_source_manager.Instance:
        """Post-rpc interceptor for get_instance

        DEPRECATED. Please use the `post_get_instance_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SecureSourceManager server but before
        it is returned to user code. This `post_get_instance` interceptor runs
        before the `post_get_instance_with_metadata` interceptor.
        """
        return response

    def post_get_instance_with_metadata(
        self,
        response: secure_source_manager.Instance,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[secure_source_manager.Instance, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_instance

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SecureSourceManager server but before it is returned to user code.

        We recommend only using this `post_get_instance_with_metadata`
        interceptor in new development instead of the `post_get_instance` interceptor.
        When both interceptors are used, this `post_get_instance_with_metadata` interceptor runs after the
        `post_get_instance` interceptor. The (possibly modified) response returned by
        `post_get_instance` will be passed to
        `post_get_instance_with_metadata`.
        """
        return response, metadata

    def pre_get_issue(
        self,
        request: secure_source_manager.GetIssueRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        secure_source_manager.GetIssueRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_issue

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SecureSourceManager server.
        """
        return request, metadata

    def post_get_issue(
        self, response: secure_source_manager.Issue
    ) -> secure_source_manager.Issue:
        """Post-rpc interceptor for get_issue

        DEPRECATED. Please use the `post_get_issue_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SecureSourceManager server but before
        it is returned to user code. This `post_get_issue` interceptor runs
        before the `post_get_issue_with_metadata` interceptor.
        """
        return response

    def post_get_issue_with_metadata(
        self,
        response: secure_source_manager.Issue,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[secure_source_manager.Issue, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_issue

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SecureSourceManager server but before it is returned to user code.

        We recommend only using this `post_get_issue_with_metadata`
        interceptor in new development instead of the `post_get_issue` interceptor.
        When both interceptors are used, this `post_get_issue_with_metadata` interceptor runs after the
        `post_get_issue` interceptor. The (possibly modified) response returned by
        `post_get_issue` will be passed to
        `post_get_issue_with_metadata`.
        """
        return response, metadata

    def pre_get_issue_comment(
        self,
        request: secure_source_manager.GetIssueCommentRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        secure_source_manager.GetIssueCommentRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_issue_comment

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SecureSourceManager server.
        """
        return request, metadata

    def post_get_issue_comment(
        self, response: secure_source_manager.IssueComment
    ) -> secure_source_manager.IssueComment:
        """Post-rpc interceptor for get_issue_comment

        DEPRECATED. Please use the `post_get_issue_comment_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SecureSourceManager server but before
        it is returned to user code. This `post_get_issue_comment` interceptor runs
        before the `post_get_issue_comment_with_metadata` interceptor.
        """
        return response

    def post_get_issue_comment_with_metadata(
        self,
        response: secure_source_manager.IssueComment,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        secure_source_manager.IssueComment, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for get_issue_comment

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SecureSourceManager server but before it is returned to user code.

        We recommend only using this `post_get_issue_comment_with_metadata`
        interceptor in new development instead of the `post_get_issue_comment` interceptor.
        When both interceptors are used, this `post_get_issue_comment_with_metadata` interceptor runs after the
        `post_get_issue_comment` interceptor. The (possibly modified) response returned by
        `post_get_issue_comment` will be passed to
        `post_get_issue_comment_with_metadata`.
        """
        return response, metadata

    def pre_get_pull_request(
        self,
        request: secure_source_manager.GetPullRequestRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        secure_source_manager.GetPullRequestRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_pull_request

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SecureSourceManager server.
        """
        return request, metadata

    def post_get_pull_request(
        self, response: secure_source_manager.PullRequest
    ) -> secure_source_manager.PullRequest:
        """Post-rpc interceptor for get_pull_request

        DEPRECATED. Please use the `post_get_pull_request_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SecureSourceManager server but before
        it is returned to user code. This `post_get_pull_request` interceptor runs
        before the `post_get_pull_request_with_metadata` interceptor.
        """
        return response

    def post_get_pull_request_with_metadata(
        self,
        response: secure_source_manager.PullRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        secure_source_manager.PullRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for get_pull_request

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SecureSourceManager server but before it is returned to user code.

        We recommend only using this `post_get_pull_request_with_metadata`
        interceptor in new development instead of the `post_get_pull_request` interceptor.
        When both interceptors are used, this `post_get_pull_request_with_metadata` interceptor runs after the
        `post_get_pull_request` interceptor. The (possibly modified) response returned by
        `post_get_pull_request` will be passed to
        `post_get_pull_request_with_metadata`.
        """
        return response, metadata

    def pre_get_pull_request_comment(
        self,
        request: secure_source_manager.GetPullRequestCommentRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        secure_source_manager.GetPullRequestCommentRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_pull_request_comment

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SecureSourceManager server.
        """
        return request, metadata

    def post_get_pull_request_comment(
        self, response: secure_source_manager.PullRequestComment
    ) -> secure_source_manager.PullRequestComment:
        """Post-rpc interceptor for get_pull_request_comment

        DEPRECATED. Please use the `post_get_pull_request_comment_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SecureSourceManager server but before
        it is returned to user code. This `post_get_pull_request_comment` interceptor runs
        before the `post_get_pull_request_comment_with_metadata` interceptor.
        """
        return response

    def post_get_pull_request_comment_with_metadata(
        self,
        response: secure_source_manager.PullRequestComment,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        secure_source_manager.PullRequestComment,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for get_pull_request_comment

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SecureSourceManager server but before it is returned to user code.

        We recommend only using this `post_get_pull_request_comment_with_metadata`
        interceptor in new development instead of the `post_get_pull_request_comment` interceptor.
        When both interceptors are used, this `post_get_pull_request_comment_with_metadata` interceptor runs after the
        `post_get_pull_request_comment` interceptor. The (possibly modified) response returned by
        `post_get_pull_request_comment` will be passed to
        `post_get_pull_request_comment_with_metadata`.
        """
        return response, metadata

    def pre_get_repository(
        self,
        request: secure_source_manager.GetRepositoryRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        secure_source_manager.GetRepositoryRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_repository

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SecureSourceManager server.
        """
        return request, metadata

    def post_get_repository(
        self, response: secure_source_manager.Repository
    ) -> secure_source_manager.Repository:
        """Post-rpc interceptor for get_repository

        DEPRECATED. Please use the `post_get_repository_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SecureSourceManager server but before
        it is returned to user code. This `post_get_repository` interceptor runs
        before the `post_get_repository_with_metadata` interceptor.
        """
        return response

    def post_get_repository_with_metadata(
        self,
        response: secure_source_manager.Repository,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        secure_source_manager.Repository, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for get_repository

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SecureSourceManager server but before it is returned to user code.

        We recommend only using this `post_get_repository_with_metadata`
        interceptor in new development instead of the `post_get_repository` interceptor.
        When both interceptors are used, this `post_get_repository_with_metadata` interceptor runs after the
        `post_get_repository` interceptor. The (possibly modified) response returned by
        `post_get_repository` will be passed to
        `post_get_repository_with_metadata`.
        """
        return response, metadata

    def pre_list_branch_rules(
        self,
        request: secure_source_manager.ListBranchRulesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        secure_source_manager.ListBranchRulesRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_branch_rules

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SecureSourceManager server.
        """
        return request, metadata

    def post_list_branch_rules(
        self, response: secure_source_manager.ListBranchRulesResponse
    ) -> secure_source_manager.ListBranchRulesResponse:
        """Post-rpc interceptor for list_branch_rules

        DEPRECATED. Please use the `post_list_branch_rules_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SecureSourceManager server but before
        it is returned to user code. This `post_list_branch_rules` interceptor runs
        before the `post_list_branch_rules_with_metadata` interceptor.
        """
        return response

    def post_list_branch_rules_with_metadata(
        self,
        response: secure_source_manager.ListBranchRulesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        secure_source_manager.ListBranchRulesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_branch_rules

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SecureSourceManager server but before it is returned to user code.

        We recommend only using this `post_list_branch_rules_with_metadata`
        interceptor in new development instead of the `post_list_branch_rules` interceptor.
        When both interceptors are used, this `post_list_branch_rules_with_metadata` interceptor runs after the
        `post_list_branch_rules` interceptor. The (possibly modified) response returned by
        `post_list_branch_rules` will be passed to
        `post_list_branch_rules_with_metadata`.
        """
        return response, metadata

    def pre_list_hooks(
        self,
        request: secure_source_manager.ListHooksRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        secure_source_manager.ListHooksRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_hooks

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SecureSourceManager server.
        """
        return request, metadata

    def post_list_hooks(
        self, response: secure_source_manager.ListHooksResponse
    ) -> secure_source_manager.ListHooksResponse:
        """Post-rpc interceptor for list_hooks

        DEPRECATED. Please use the `post_list_hooks_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SecureSourceManager server but before
        it is returned to user code. This `post_list_hooks` interceptor runs
        before the `post_list_hooks_with_metadata` interceptor.
        """
        return response

    def post_list_hooks_with_metadata(
        self,
        response: secure_source_manager.ListHooksResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        secure_source_manager.ListHooksResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_hooks

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SecureSourceManager server but before it is returned to user code.

        We recommend only using this `post_list_hooks_with_metadata`
        interceptor in new development instead of the `post_list_hooks` interceptor.
        When both interceptors are used, this `post_list_hooks_with_metadata` interceptor runs after the
        `post_list_hooks` interceptor. The (possibly modified) response returned by
        `post_list_hooks` will be passed to
        `post_list_hooks_with_metadata`.
        """
        return response, metadata

    def pre_list_instances(
        self,
        request: secure_source_manager.ListInstancesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        secure_source_manager.ListInstancesRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_instances

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SecureSourceManager server.
        """
        return request, metadata

    def post_list_instances(
        self, response: secure_source_manager.ListInstancesResponse
    ) -> secure_source_manager.ListInstancesResponse:
        """Post-rpc interceptor for list_instances

        DEPRECATED. Please use the `post_list_instances_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SecureSourceManager server but before
        it is returned to user code. This `post_list_instances` interceptor runs
        before the `post_list_instances_with_metadata` interceptor.
        """
        return response

    def post_list_instances_with_metadata(
        self,
        response: secure_source_manager.ListInstancesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        secure_source_manager.ListInstancesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_instances

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SecureSourceManager server but before it is returned to user code.

        We recommend only using this `post_list_instances_with_metadata`
        interceptor in new development instead of the `post_list_instances` interceptor.
        When both interceptors are used, this `post_list_instances_with_metadata` interceptor runs after the
        `post_list_instances` interceptor. The (possibly modified) response returned by
        `post_list_instances` will be passed to
        `post_list_instances_with_metadata`.
        """
        return response, metadata

    def pre_list_issue_comments(
        self,
        request: secure_source_manager.ListIssueCommentsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        secure_source_manager.ListIssueCommentsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_issue_comments

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SecureSourceManager server.
        """
        return request, metadata

    def post_list_issue_comments(
        self, response: secure_source_manager.ListIssueCommentsResponse
    ) -> secure_source_manager.ListIssueCommentsResponse:
        """Post-rpc interceptor for list_issue_comments

        DEPRECATED. Please use the `post_list_issue_comments_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SecureSourceManager server but before
        it is returned to user code. This `post_list_issue_comments` interceptor runs
        before the `post_list_issue_comments_with_metadata` interceptor.
        """
        return response

    def post_list_issue_comments_with_metadata(
        self,
        response: secure_source_manager.ListIssueCommentsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        secure_source_manager.ListIssueCommentsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_issue_comments

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SecureSourceManager server but before it is returned to user code.

        We recommend only using this `post_list_issue_comments_with_metadata`
        interceptor in new development instead of the `post_list_issue_comments` interceptor.
        When both interceptors are used, this `post_list_issue_comments_with_metadata` interceptor runs after the
        `post_list_issue_comments` interceptor. The (possibly modified) response returned by
        `post_list_issue_comments` will be passed to
        `post_list_issue_comments_with_metadata`.
        """
        return response, metadata

    def pre_list_issues(
        self,
        request: secure_source_manager.ListIssuesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        secure_source_manager.ListIssuesRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_issues

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SecureSourceManager server.
        """
        return request, metadata

    def post_list_issues(
        self, response: secure_source_manager.ListIssuesResponse
    ) -> secure_source_manager.ListIssuesResponse:
        """Post-rpc interceptor for list_issues

        DEPRECATED. Please use the `post_list_issues_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SecureSourceManager server but before
        it is returned to user code. This `post_list_issues` interceptor runs
        before the `post_list_issues_with_metadata` interceptor.
        """
        return response

    def post_list_issues_with_metadata(
        self,
        response: secure_source_manager.ListIssuesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        secure_source_manager.ListIssuesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_issues

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SecureSourceManager server but before it is returned to user code.

        We recommend only using this `post_list_issues_with_metadata`
        interceptor in new development instead of the `post_list_issues` interceptor.
        When both interceptors are used, this `post_list_issues_with_metadata` interceptor runs after the
        `post_list_issues` interceptor. The (possibly modified) response returned by
        `post_list_issues` will be passed to
        `post_list_issues_with_metadata`.
        """
        return response, metadata

    def pre_list_pull_request_comments(
        self,
        request: secure_source_manager.ListPullRequestCommentsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        secure_source_manager.ListPullRequestCommentsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_pull_request_comments

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SecureSourceManager server.
        """
        return request, metadata

    def post_list_pull_request_comments(
        self, response: secure_source_manager.ListPullRequestCommentsResponse
    ) -> secure_source_manager.ListPullRequestCommentsResponse:
        """Post-rpc interceptor for list_pull_request_comments

        DEPRECATED. Please use the `post_list_pull_request_comments_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SecureSourceManager server but before
        it is returned to user code. This `post_list_pull_request_comments` interceptor runs
        before the `post_list_pull_request_comments_with_metadata` interceptor.
        """
        return response

    def post_list_pull_request_comments_with_metadata(
        self,
        response: secure_source_manager.ListPullRequestCommentsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        secure_source_manager.ListPullRequestCommentsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_pull_request_comments

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SecureSourceManager server but before it is returned to user code.

        We recommend only using this `post_list_pull_request_comments_with_metadata`
        interceptor in new development instead of the `post_list_pull_request_comments` interceptor.
        When both interceptors are used, this `post_list_pull_request_comments_with_metadata` interceptor runs after the
        `post_list_pull_request_comments` interceptor. The (possibly modified) response returned by
        `post_list_pull_request_comments` will be passed to
        `post_list_pull_request_comments_with_metadata`.
        """
        return response, metadata

    def pre_list_pull_request_file_diffs(
        self,
        request: secure_source_manager.ListPullRequestFileDiffsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        secure_source_manager.ListPullRequestFileDiffsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_pull_request_file_diffs

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SecureSourceManager server.
        """
        return request, metadata

    def post_list_pull_request_file_diffs(
        self, response: secure_source_manager.ListPullRequestFileDiffsResponse
    ) -> secure_source_manager.ListPullRequestFileDiffsResponse:
        """Post-rpc interceptor for list_pull_request_file_diffs

        DEPRECATED. Please use the `post_list_pull_request_file_diffs_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SecureSourceManager server but before
        it is returned to user code. This `post_list_pull_request_file_diffs` interceptor runs
        before the `post_list_pull_request_file_diffs_with_metadata` interceptor.
        """
        return response

    def post_list_pull_request_file_diffs_with_metadata(
        self,
        response: secure_source_manager.ListPullRequestFileDiffsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        secure_source_manager.ListPullRequestFileDiffsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_pull_request_file_diffs

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SecureSourceManager server but before it is returned to user code.

        We recommend only using this `post_list_pull_request_file_diffs_with_metadata`
        interceptor in new development instead of the `post_list_pull_request_file_diffs` interceptor.
        When both interceptors are used, this `post_list_pull_request_file_diffs_with_metadata` interceptor runs after the
        `post_list_pull_request_file_diffs` interceptor. The (possibly modified) response returned by
        `post_list_pull_request_file_diffs` will be passed to
        `post_list_pull_request_file_diffs_with_metadata`.
        """
        return response, metadata

    def pre_list_pull_requests(
        self,
        request: secure_source_manager.ListPullRequestsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        secure_source_manager.ListPullRequestsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_pull_requests

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SecureSourceManager server.
        """
        return request, metadata

    def post_list_pull_requests(
        self, response: secure_source_manager.ListPullRequestsResponse
    ) -> secure_source_manager.ListPullRequestsResponse:
        """Post-rpc interceptor for list_pull_requests

        DEPRECATED. Please use the `post_list_pull_requests_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SecureSourceManager server but before
        it is returned to user code. This `post_list_pull_requests` interceptor runs
        before the `post_list_pull_requests_with_metadata` interceptor.
        """
        return response

    def post_list_pull_requests_with_metadata(
        self,
        response: secure_source_manager.ListPullRequestsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        secure_source_manager.ListPullRequestsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_pull_requests

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SecureSourceManager server but before it is returned to user code.

        We recommend only using this `post_list_pull_requests_with_metadata`
        interceptor in new development instead of the `post_list_pull_requests` interceptor.
        When both interceptors are used, this `post_list_pull_requests_with_metadata` interceptor runs after the
        `post_list_pull_requests` interceptor. The (possibly modified) response returned by
        `post_list_pull_requests` will be passed to
        `post_list_pull_requests_with_metadata`.
        """
        return response, metadata

    def pre_list_repositories(
        self,
        request: secure_source_manager.ListRepositoriesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        secure_source_manager.ListRepositoriesRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_repositories

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SecureSourceManager server.
        """
        return request, metadata

    def post_list_repositories(
        self, response: secure_source_manager.ListRepositoriesResponse
    ) -> secure_source_manager.ListRepositoriesResponse:
        """Post-rpc interceptor for list_repositories

        DEPRECATED. Please use the `post_list_repositories_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SecureSourceManager server but before
        it is returned to user code. This `post_list_repositories` interceptor runs
        before the `post_list_repositories_with_metadata` interceptor.
        """
        return response

    def post_list_repositories_with_metadata(
        self,
        response: secure_source_manager.ListRepositoriesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        secure_source_manager.ListRepositoriesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_repositories

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SecureSourceManager server but before it is returned to user code.

        We recommend only using this `post_list_repositories_with_metadata`
        interceptor in new development instead of the `post_list_repositories` interceptor.
        When both interceptors are used, this `post_list_repositories_with_metadata` interceptor runs after the
        `post_list_repositories` interceptor. The (possibly modified) response returned by
        `post_list_repositories` will be passed to
        `post_list_repositories_with_metadata`.
        """
        return response, metadata

    def pre_merge_pull_request(
        self,
        request: secure_source_manager.MergePullRequestRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        secure_source_manager.MergePullRequestRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for merge_pull_request

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SecureSourceManager server.
        """
        return request, metadata

    def post_merge_pull_request(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for merge_pull_request

        DEPRECATED. Please use the `post_merge_pull_request_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SecureSourceManager server but before
        it is returned to user code. This `post_merge_pull_request` interceptor runs
        before the `post_merge_pull_request_with_metadata` interceptor.
        """
        return response

    def post_merge_pull_request_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for merge_pull_request

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SecureSourceManager server but before it is returned to user code.

        We recommend only using this `post_merge_pull_request_with_metadata`
        interceptor in new development instead of the `post_merge_pull_request` interceptor.
        When both interceptors are used, this `post_merge_pull_request_with_metadata` interceptor runs after the
        `post_merge_pull_request` interceptor. The (possibly modified) response returned by
        `post_merge_pull_request` will be passed to
        `post_merge_pull_request_with_metadata`.
        """
        return response, metadata

    def pre_open_issue(
        self,
        request: secure_source_manager.OpenIssueRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        secure_source_manager.OpenIssueRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for open_issue

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SecureSourceManager server.
        """
        return request, metadata

    def post_open_issue(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for open_issue

        DEPRECATED. Please use the `post_open_issue_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SecureSourceManager server but before
        it is returned to user code. This `post_open_issue` interceptor runs
        before the `post_open_issue_with_metadata` interceptor.
        """
        return response

    def post_open_issue_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for open_issue

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SecureSourceManager server but before it is returned to user code.

        We recommend only using this `post_open_issue_with_metadata`
        interceptor in new development instead of the `post_open_issue` interceptor.
        When both interceptors are used, this `post_open_issue_with_metadata` interceptor runs after the
        `post_open_issue` interceptor. The (possibly modified) response returned by
        `post_open_issue` will be passed to
        `post_open_issue_with_metadata`.
        """
        return response, metadata

    def pre_open_pull_request(
        self,
        request: secure_source_manager.OpenPullRequestRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        secure_source_manager.OpenPullRequestRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for open_pull_request

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SecureSourceManager server.
        """
        return request, metadata

    def post_open_pull_request(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for open_pull_request

        DEPRECATED. Please use the `post_open_pull_request_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SecureSourceManager server but before
        it is returned to user code. This `post_open_pull_request` interceptor runs
        before the `post_open_pull_request_with_metadata` interceptor.
        """
        return response

    def post_open_pull_request_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for open_pull_request

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SecureSourceManager server but before it is returned to user code.

        We recommend only using this `post_open_pull_request_with_metadata`
        interceptor in new development instead of the `post_open_pull_request` interceptor.
        When both interceptors are used, this `post_open_pull_request_with_metadata` interceptor runs after the
        `post_open_pull_request` interceptor. The (possibly modified) response returned by
        `post_open_pull_request` will be passed to
        `post_open_pull_request_with_metadata`.
        """
        return response, metadata

    def pre_resolve_pull_request_comments(
        self,
        request: secure_source_manager.ResolvePullRequestCommentsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        secure_source_manager.ResolvePullRequestCommentsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for resolve_pull_request_comments

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SecureSourceManager server.
        """
        return request, metadata

    def post_resolve_pull_request_comments(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for resolve_pull_request_comments

        DEPRECATED. Please use the `post_resolve_pull_request_comments_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SecureSourceManager server but before
        it is returned to user code. This `post_resolve_pull_request_comments` interceptor runs
        before the `post_resolve_pull_request_comments_with_metadata` interceptor.
        """
        return response

    def post_resolve_pull_request_comments_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for resolve_pull_request_comments

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SecureSourceManager server but before it is returned to user code.

        We recommend only using this `post_resolve_pull_request_comments_with_metadata`
        interceptor in new development instead of the `post_resolve_pull_request_comments` interceptor.
        When both interceptors are used, this `post_resolve_pull_request_comments_with_metadata` interceptor runs after the
        `post_resolve_pull_request_comments` interceptor. The (possibly modified) response returned by
        `post_resolve_pull_request_comments` will be passed to
        `post_resolve_pull_request_comments_with_metadata`.
        """
        return response, metadata

    def pre_set_iam_policy_repo(
        self,
        request: iam_policy_pb2.SetIamPolicyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        iam_policy_pb2.SetIamPolicyRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for set_iam_policy_repo

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SecureSourceManager server.
        """
        return request, metadata

    def post_set_iam_policy_repo(
        self, response: policy_pb2.Policy
    ) -> policy_pb2.Policy:
        """Post-rpc interceptor for set_iam_policy_repo

        DEPRECATED. Please use the `post_set_iam_policy_repo_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SecureSourceManager server but before
        it is returned to user code. This `post_set_iam_policy_repo` interceptor runs
        before the `post_set_iam_policy_repo_with_metadata` interceptor.
        """
        return response

    def post_set_iam_policy_repo_with_metadata(
        self,
        response: policy_pb2.Policy,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[policy_pb2.Policy, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for set_iam_policy_repo

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SecureSourceManager server but before it is returned to user code.

        We recommend only using this `post_set_iam_policy_repo_with_metadata`
        interceptor in new development instead of the `post_set_iam_policy_repo` interceptor.
        When both interceptors are used, this `post_set_iam_policy_repo_with_metadata` interceptor runs after the
        `post_set_iam_policy_repo` interceptor. The (possibly modified) response returned by
        `post_set_iam_policy_repo` will be passed to
        `post_set_iam_policy_repo_with_metadata`.
        """
        return response, metadata

    def pre_test_iam_permissions_repo(
        self,
        request: iam_policy_pb2.TestIamPermissionsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        iam_policy_pb2.TestIamPermissionsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for test_iam_permissions_repo

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SecureSourceManager server.
        """
        return request, metadata

    def post_test_iam_permissions_repo(
        self, response: iam_policy_pb2.TestIamPermissionsResponse
    ) -> iam_policy_pb2.TestIamPermissionsResponse:
        """Post-rpc interceptor for test_iam_permissions_repo

        DEPRECATED. Please use the `post_test_iam_permissions_repo_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SecureSourceManager server but before
        it is returned to user code. This `post_test_iam_permissions_repo` interceptor runs
        before the `post_test_iam_permissions_repo_with_metadata` interceptor.
        """
        return response

    def post_test_iam_permissions_repo_with_metadata(
        self,
        response: iam_policy_pb2.TestIamPermissionsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        iam_policy_pb2.TestIamPermissionsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for test_iam_permissions_repo

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SecureSourceManager server but before it is returned to user code.

        We recommend only using this `post_test_iam_permissions_repo_with_metadata`
        interceptor in new development instead of the `post_test_iam_permissions_repo` interceptor.
        When both interceptors are used, this `post_test_iam_permissions_repo_with_metadata` interceptor runs after the
        `post_test_iam_permissions_repo` interceptor. The (possibly modified) response returned by
        `post_test_iam_permissions_repo` will be passed to
        `post_test_iam_permissions_repo_with_metadata`.
        """
        return response, metadata

    def pre_unresolve_pull_request_comments(
        self,
        request: secure_source_manager.UnresolvePullRequestCommentsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        secure_source_manager.UnresolvePullRequestCommentsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for unresolve_pull_request_comments

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SecureSourceManager server.
        """
        return request, metadata

    def post_unresolve_pull_request_comments(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for unresolve_pull_request_comments

        DEPRECATED. Please use the `post_unresolve_pull_request_comments_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SecureSourceManager server but before
        it is returned to user code. This `post_unresolve_pull_request_comments` interceptor runs
        before the `post_unresolve_pull_request_comments_with_metadata` interceptor.
        """
        return response

    def post_unresolve_pull_request_comments_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for unresolve_pull_request_comments

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SecureSourceManager server but before it is returned to user code.

        We recommend only using this `post_unresolve_pull_request_comments_with_metadata`
        interceptor in new development instead of the `post_unresolve_pull_request_comments` interceptor.
        When both interceptors are used, this `post_unresolve_pull_request_comments_with_metadata` interceptor runs after the
        `post_unresolve_pull_request_comments` interceptor. The (possibly modified) response returned by
        `post_unresolve_pull_request_comments` will be passed to
        `post_unresolve_pull_request_comments_with_metadata`.
        """
        return response, metadata

    def pre_update_branch_rule(
        self,
        request: secure_source_manager.UpdateBranchRuleRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        secure_source_manager.UpdateBranchRuleRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_branch_rule

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SecureSourceManager server.
        """
        return request, metadata

    def post_update_branch_rule(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_branch_rule

        DEPRECATED. Please use the `post_update_branch_rule_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SecureSourceManager server but before
        it is returned to user code. This `post_update_branch_rule` interceptor runs
        before the `post_update_branch_rule_with_metadata` interceptor.
        """
        return response

    def post_update_branch_rule_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_branch_rule

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SecureSourceManager server but before it is returned to user code.

        We recommend only using this `post_update_branch_rule_with_metadata`
        interceptor in new development instead of the `post_update_branch_rule` interceptor.
        When both interceptors are used, this `post_update_branch_rule_with_metadata` interceptor runs after the
        `post_update_branch_rule` interceptor. The (possibly modified) response returned by
        `post_update_branch_rule` will be passed to
        `post_update_branch_rule_with_metadata`.
        """
        return response, metadata

    def pre_update_hook(
        self,
        request: secure_source_manager.UpdateHookRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        secure_source_manager.UpdateHookRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_hook

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SecureSourceManager server.
        """
        return request, metadata

    def post_update_hook(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_hook

        DEPRECATED. Please use the `post_update_hook_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SecureSourceManager server but before
        it is returned to user code. This `post_update_hook` interceptor runs
        before the `post_update_hook_with_metadata` interceptor.
        """
        return response

    def post_update_hook_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_hook

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SecureSourceManager server but before it is returned to user code.

        We recommend only using this `post_update_hook_with_metadata`
        interceptor in new development instead of the `post_update_hook` interceptor.
        When both interceptors are used, this `post_update_hook_with_metadata` interceptor runs after the
        `post_update_hook` interceptor. The (possibly modified) response returned by
        `post_update_hook` will be passed to
        `post_update_hook_with_metadata`.
        """
        return response, metadata

    def pre_update_issue(
        self,
        request: secure_source_manager.UpdateIssueRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        secure_source_manager.UpdateIssueRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_issue

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SecureSourceManager server.
        """
        return request, metadata

    def post_update_issue(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_issue

        DEPRECATED. Please use the `post_update_issue_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SecureSourceManager server but before
        it is returned to user code. This `post_update_issue` interceptor runs
        before the `post_update_issue_with_metadata` interceptor.
        """
        return response

    def post_update_issue_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_issue

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SecureSourceManager server but before it is returned to user code.

        We recommend only using this `post_update_issue_with_metadata`
        interceptor in new development instead of the `post_update_issue` interceptor.
        When both interceptors are used, this `post_update_issue_with_metadata` interceptor runs after the
        `post_update_issue` interceptor. The (possibly modified) response returned by
        `post_update_issue` will be passed to
        `post_update_issue_with_metadata`.
        """
        return response, metadata

    def pre_update_issue_comment(
        self,
        request: secure_source_manager.UpdateIssueCommentRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        secure_source_manager.UpdateIssueCommentRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_issue_comment

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SecureSourceManager server.
        """
        return request, metadata

    def post_update_issue_comment(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_issue_comment

        DEPRECATED. Please use the `post_update_issue_comment_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SecureSourceManager server but before
        it is returned to user code. This `post_update_issue_comment` interceptor runs
        before the `post_update_issue_comment_with_metadata` interceptor.
        """
        return response

    def post_update_issue_comment_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_issue_comment

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SecureSourceManager server but before it is returned to user code.

        We recommend only using this `post_update_issue_comment_with_metadata`
        interceptor in new development instead of the `post_update_issue_comment` interceptor.
        When both interceptors are used, this `post_update_issue_comment_with_metadata` interceptor runs after the
        `post_update_issue_comment` interceptor. The (possibly modified) response returned by
        `post_update_issue_comment` will be passed to
        `post_update_issue_comment_with_metadata`.
        """
        return response, metadata

    def pre_update_pull_request(
        self,
        request: secure_source_manager.UpdatePullRequestRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        secure_source_manager.UpdatePullRequestRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_pull_request

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SecureSourceManager server.
        """
        return request, metadata

    def post_update_pull_request(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_pull_request

        DEPRECATED. Please use the `post_update_pull_request_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SecureSourceManager server but before
        it is returned to user code. This `post_update_pull_request` interceptor runs
        before the `post_update_pull_request_with_metadata` interceptor.
        """
        return response

    def post_update_pull_request_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_pull_request

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SecureSourceManager server but before it is returned to user code.

        We recommend only using this `post_update_pull_request_with_metadata`
        interceptor in new development instead of the `post_update_pull_request` interceptor.
        When both interceptors are used, this `post_update_pull_request_with_metadata` interceptor runs after the
        `post_update_pull_request` interceptor. The (possibly modified) response returned by
        `post_update_pull_request` will be passed to
        `post_update_pull_request_with_metadata`.
        """
        return response, metadata

    def pre_update_pull_request_comment(
        self,
        request: secure_source_manager.UpdatePullRequestCommentRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        secure_source_manager.UpdatePullRequestCommentRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_pull_request_comment

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SecureSourceManager server.
        """
        return request, metadata

    def post_update_pull_request_comment(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_pull_request_comment

        DEPRECATED. Please use the `post_update_pull_request_comment_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SecureSourceManager server but before
        it is returned to user code. This `post_update_pull_request_comment` interceptor runs
        before the `post_update_pull_request_comment_with_metadata` interceptor.
        """
        return response

    def post_update_pull_request_comment_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_pull_request_comment

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SecureSourceManager server but before it is returned to user code.

        We recommend only using this `post_update_pull_request_comment_with_metadata`
        interceptor in new development instead of the `post_update_pull_request_comment` interceptor.
        When both interceptors are used, this `post_update_pull_request_comment_with_metadata` interceptor runs after the
        `post_update_pull_request_comment` interceptor. The (possibly modified) response returned by
        `post_update_pull_request_comment` will be passed to
        `post_update_pull_request_comment_with_metadata`.
        """
        return response, metadata

    def pre_update_repository(
        self,
        request: secure_source_manager.UpdateRepositoryRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        secure_source_manager.UpdateRepositoryRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_repository

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SecureSourceManager server.
        """
        return request, metadata

    def post_update_repository(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_repository

        DEPRECATED. Please use the `post_update_repository_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SecureSourceManager server but before
        it is returned to user code. This `post_update_repository` interceptor runs
        before the `post_update_repository_with_metadata` interceptor.
        """
        return response

    def post_update_repository_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_repository

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SecureSourceManager server but before it is returned to user code.

        We recommend only using this `post_update_repository_with_metadata`
        interceptor in new development instead of the `post_update_repository` interceptor.
        When both interceptors are used, this `post_update_repository_with_metadata` interceptor runs after the
        `post_update_repository` interceptor. The (possibly modified) response returned by
        `post_update_repository` will be passed to
        `post_update_repository_with_metadata`.
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
        before they are sent to the SecureSourceManager server.
        """
        return request, metadata

    def post_get_location(
        self, response: locations_pb2.Location
    ) -> locations_pb2.Location:
        """Post-rpc interceptor for get_location

        Override in a subclass to manipulate the response
        after it is returned by the SecureSourceManager server but before
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
        before they are sent to the SecureSourceManager server.
        """
        return request, metadata

    def post_list_locations(
        self, response: locations_pb2.ListLocationsResponse
    ) -> locations_pb2.ListLocationsResponse:
        """Post-rpc interceptor for list_locations

        Override in a subclass to manipulate the response
        after it is returned by the SecureSourceManager server but before
        it is returned to user code.
        """
        return response

    def pre_get_iam_policy(
        self,
        request: iam_policy_pb2.GetIamPolicyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        iam_policy_pb2.GetIamPolicyRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_iam_policy

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SecureSourceManager server.
        """
        return request, metadata

    def post_get_iam_policy(self, response: policy_pb2.Policy) -> policy_pb2.Policy:
        """Post-rpc interceptor for get_iam_policy

        Override in a subclass to manipulate the response
        after it is returned by the SecureSourceManager server but before
        it is returned to user code.
        """
        return response

    def pre_set_iam_policy(
        self,
        request: iam_policy_pb2.SetIamPolicyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        iam_policy_pb2.SetIamPolicyRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for set_iam_policy

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SecureSourceManager server.
        """
        return request, metadata

    def post_set_iam_policy(self, response: policy_pb2.Policy) -> policy_pb2.Policy:
        """Post-rpc interceptor for set_iam_policy

        Override in a subclass to manipulate the response
        after it is returned by the SecureSourceManager server but before
        it is returned to user code.
        """
        return response

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
        before they are sent to the SecureSourceManager server.
        """
        return request, metadata

    def post_test_iam_permissions(
        self, response: iam_policy_pb2.TestIamPermissionsResponse
    ) -> iam_policy_pb2.TestIamPermissionsResponse:
        """Post-rpc interceptor for test_iam_permissions

        Override in a subclass to manipulate the response
        after it is returned by the SecureSourceManager server but before
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
        before they are sent to the SecureSourceManager server.
        """
        return request, metadata

    def post_cancel_operation(self, response: None) -> None:
        """Post-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the response
        after it is returned by the SecureSourceManager server but before
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
        before they are sent to the SecureSourceManager server.
        """
        return request, metadata

    def post_delete_operation(self, response: None) -> None:
        """Post-rpc interceptor for delete_operation

        Override in a subclass to manipulate the response
        after it is returned by the SecureSourceManager server but before
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
        before they are sent to the SecureSourceManager server.
        """
        return request, metadata

    def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the SecureSourceManager server but before
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
        before they are sent to the SecureSourceManager server.
        """
        return request, metadata

    def post_list_operations(
        self, response: operations_pb2.ListOperationsResponse
    ) -> operations_pb2.ListOperationsResponse:
        """Post-rpc interceptor for list_operations

        Override in a subclass to manipulate the response
        after it is returned by the SecureSourceManager server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class SecureSourceManagerRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: SecureSourceManagerRestInterceptor


class SecureSourceManagerRestTransport(_BaseSecureSourceManagerRestTransport):
    """REST backend synchronous transport for SecureSourceManager.

    Secure Source Manager API

    Access Secure Source Manager instances, resources, and
    repositories.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "securesourcemanager.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[SecureSourceManagerRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'securesourcemanager.googleapis.com').
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
            interceptor (Optional[SecureSourceManagerRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or SecureSourceManagerRestInterceptor()
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

    class _BatchCreatePullRequestComments(
        _BaseSecureSourceManagerRestTransport._BaseBatchCreatePullRequestComments,
        SecureSourceManagerRestStub,
    ):
        def __hash__(self):
            return hash(
                "SecureSourceManagerRestTransport.BatchCreatePullRequestComments"
            )

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
            request: secure_source_manager.BatchCreatePullRequestCommentsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the batch create pull request
            comments method over HTTP.

                Args:
                    request (~.secure_source_manager.BatchCreatePullRequestCommentsRequest):
                        The request object. The request to batch create pull
                    request comments.
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

            http_options = _BaseSecureSourceManagerRestTransport._BaseBatchCreatePullRequestComments._get_http_options()
            request, metadata = (
                self._interceptor.pre_batch_create_pull_request_comments(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecureSourceManagerRestTransport._BaseBatchCreatePullRequestComments,
                    "_BaseBatchCreatePullRequestComments__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.securesourcemanager_v1.SecureSourceManagerClient.BatchCreatePullRequestComments",
                    extra={
                        "serviceName": "google.cloud.securesourcemanager.v1.SecureSourceManager",
                        "rpcName": "BatchCreatePullRequestComments",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SecureSourceManagerRestTransport._BatchCreatePullRequestComments._get_response(
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

            resp = self._interceptor.post_batch_create_pull_request_comments(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_batch_create_pull_request_comments_with_metadata(
                    resp, response_metadata
                )
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
                    "Received response for google.cloud.securesourcemanager_v1.SecureSourceManagerClient.batch_create_pull_request_comments",
                    extra={
                        "serviceName": "google.cloud.securesourcemanager.v1.SecureSourceManager",
                        "rpcName": "BatchCreatePullRequestComments",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CloseIssue(
        _BaseSecureSourceManagerRestTransport._BaseCloseIssue,
        SecureSourceManagerRestStub,
    ):
        def __hash__(self):
            return hash("SecureSourceManagerRestTransport.CloseIssue")

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
            request: secure_source_manager.CloseIssueRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the close issue method over HTTP.

            Args:
                request (~.secure_source_manager.CloseIssueRequest):
                    The request object. The request to close an issue.
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

            http_options = _BaseSecureSourceManagerRestTransport._BaseCloseIssue._get_http_options()
            request, metadata = self._interceptor.pre_close_issue(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecureSourceManagerRestTransport._BaseCloseIssue,
                    "_BaseCloseIssue__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.securesourcemanager_v1.SecureSourceManagerClient.CloseIssue",
                    extra={
                        "serviceName": "google.cloud.securesourcemanager.v1.SecureSourceManager",
                        "rpcName": "CloseIssue",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SecureSourceManagerRestTransport._CloseIssue._get_response(
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

            resp = self._interceptor.post_close_issue(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_close_issue_with_metadata(
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
                    "Received response for google.cloud.securesourcemanager_v1.SecureSourceManagerClient.close_issue",
                    extra={
                        "serviceName": "google.cloud.securesourcemanager.v1.SecureSourceManager",
                        "rpcName": "CloseIssue",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ClosePullRequest(
        _BaseSecureSourceManagerRestTransport._BaseClosePullRequest,
        SecureSourceManagerRestStub,
    ):
        def __hash__(self):
            return hash("SecureSourceManagerRestTransport.ClosePullRequest")

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
            request: secure_source_manager.ClosePullRequestRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the close pull request method over HTTP.

            Args:
                request (~.secure_source_manager.ClosePullRequestRequest):
                    The request object. ClosePullRequestRequest is the
                request to close a pull request.
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

            http_options = _BaseSecureSourceManagerRestTransport._BaseClosePullRequest._get_http_options()
            request, metadata = self._interceptor.pre_close_pull_request(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecureSourceManagerRestTransport._BaseClosePullRequest,
                    "_BaseClosePullRequest__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.securesourcemanager_v1.SecureSourceManagerClient.ClosePullRequest",
                    extra={
                        "serviceName": "google.cloud.securesourcemanager.v1.SecureSourceManager",
                        "rpcName": "ClosePullRequest",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SecureSourceManagerRestTransport._ClosePullRequest._get_response(
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

            resp = self._interceptor.post_close_pull_request(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_close_pull_request_with_metadata(
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
                    "Received response for google.cloud.securesourcemanager_v1.SecureSourceManagerClient.close_pull_request",
                    extra={
                        "serviceName": "google.cloud.securesourcemanager.v1.SecureSourceManager",
                        "rpcName": "ClosePullRequest",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateBranchRule(
        _BaseSecureSourceManagerRestTransport._BaseCreateBranchRule,
        SecureSourceManagerRestStub,
    ):
        def __hash__(self):
            return hash("SecureSourceManagerRestTransport.CreateBranchRule")

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
            request: secure_source_manager.CreateBranchRuleRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create branch rule method over HTTP.

            Args:
                request (~.secure_source_manager.CreateBranchRuleRequest):
                    The request object. CreateBranchRuleRequest is the
                request to create a branch rule.
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

            http_options = _BaseSecureSourceManagerRestTransport._BaseCreateBranchRule._get_http_options()
            request, metadata = self._interceptor.pre_create_branch_rule(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecureSourceManagerRestTransport._BaseCreateBranchRule,
                    "_BaseCreateBranchRule__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.securesourcemanager_v1.SecureSourceManagerClient.CreateBranchRule",
                    extra={
                        "serviceName": "google.cloud.securesourcemanager.v1.SecureSourceManager",
                        "rpcName": "CreateBranchRule",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SecureSourceManagerRestTransport._CreateBranchRule._get_response(
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

            resp = self._interceptor.post_create_branch_rule(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_branch_rule_with_metadata(
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
                    "Received response for google.cloud.securesourcemanager_v1.SecureSourceManagerClient.create_branch_rule",
                    extra={
                        "serviceName": "google.cloud.securesourcemanager.v1.SecureSourceManager",
                        "rpcName": "CreateBranchRule",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateHook(
        _BaseSecureSourceManagerRestTransport._BaseCreateHook,
        SecureSourceManagerRestStub,
    ):
        def __hash__(self):
            return hash("SecureSourceManagerRestTransport.CreateHook")

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
            request: secure_source_manager.CreateHookRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create hook method over HTTP.

            Args:
                request (~.secure_source_manager.CreateHookRequest):
                    The request object. CreateHookRequest is the request for
                creating a hook.
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

            http_options = _BaseSecureSourceManagerRestTransport._BaseCreateHook._get_http_options()
            request, metadata = self._interceptor.pre_create_hook(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecureSourceManagerRestTransport._BaseCreateHook,
                    "_BaseCreateHook__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.securesourcemanager_v1.SecureSourceManagerClient.CreateHook",
                    extra={
                        "serviceName": "google.cloud.securesourcemanager.v1.SecureSourceManager",
                        "rpcName": "CreateHook",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SecureSourceManagerRestTransport._CreateHook._get_response(
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

            resp = self._interceptor.post_create_hook(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_hook_with_metadata(
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
                    "Received response for google.cloud.securesourcemanager_v1.SecureSourceManagerClient.create_hook",
                    extra={
                        "serviceName": "google.cloud.securesourcemanager.v1.SecureSourceManager",
                        "rpcName": "CreateHook",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateInstance(
        _BaseSecureSourceManagerRestTransport._BaseCreateInstance,
        SecureSourceManagerRestStub,
    ):
        def __hash__(self):
            return hash("SecureSourceManagerRestTransport.CreateInstance")

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
            request: secure_source_manager.CreateInstanceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create instance method over HTTP.

            Args:
                request (~.secure_source_manager.CreateInstanceRequest):
                    The request object. CreateInstanceRequest is the request
                for creating an instance.
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

            http_options = _BaseSecureSourceManagerRestTransport._BaseCreateInstance._get_http_options()
            request, metadata = self._interceptor.pre_create_instance(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecureSourceManagerRestTransport._BaseCreateInstance,
                    "_BaseCreateInstance__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.securesourcemanager_v1.SecureSourceManagerClient.CreateInstance",
                    extra={
                        "serviceName": "google.cloud.securesourcemanager.v1.SecureSourceManager",
                        "rpcName": "CreateInstance",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SecureSourceManagerRestTransport._CreateInstance._get_response(
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

            resp = self._interceptor.post_create_instance(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_instance_with_metadata(
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
                    "Received response for google.cloud.securesourcemanager_v1.SecureSourceManagerClient.create_instance",
                    extra={
                        "serviceName": "google.cloud.securesourcemanager.v1.SecureSourceManager",
                        "rpcName": "CreateInstance",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateIssue(
        _BaseSecureSourceManagerRestTransport._BaseCreateIssue,
        SecureSourceManagerRestStub,
    ):
        def __hash__(self):
            return hash("SecureSourceManagerRestTransport.CreateIssue")

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
            request: secure_source_manager.CreateIssueRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create issue method over HTTP.

            Args:
                request (~.secure_source_manager.CreateIssueRequest):
                    The request object. The request to create an issue.
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

            http_options = _BaseSecureSourceManagerRestTransport._BaseCreateIssue._get_http_options()
            request, metadata = self._interceptor.pre_create_issue(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecureSourceManagerRestTransport._BaseCreateIssue,
                    "_BaseCreateIssue__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.securesourcemanager_v1.SecureSourceManagerClient.CreateIssue",
                    extra={
                        "serviceName": "google.cloud.securesourcemanager.v1.SecureSourceManager",
                        "rpcName": "CreateIssue",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SecureSourceManagerRestTransport._CreateIssue._get_response(
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

            resp = self._interceptor.post_create_issue(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_issue_with_metadata(
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
                    "Received response for google.cloud.securesourcemanager_v1.SecureSourceManagerClient.create_issue",
                    extra={
                        "serviceName": "google.cloud.securesourcemanager.v1.SecureSourceManager",
                        "rpcName": "CreateIssue",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateIssueComment(
        _BaseSecureSourceManagerRestTransport._BaseCreateIssueComment,
        SecureSourceManagerRestStub,
    ):
        def __hash__(self):
            return hash("SecureSourceManagerRestTransport.CreateIssueComment")

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
            request: secure_source_manager.CreateIssueCommentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create issue comment method over HTTP.

            Args:
                request (~.secure_source_manager.CreateIssueCommentRequest):
                    The request object. The request to create an issue
                comment.
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

            http_options = _BaseSecureSourceManagerRestTransport._BaseCreateIssueComment._get_http_options()
            request, metadata = self._interceptor.pre_create_issue_comment(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecureSourceManagerRestTransport._BaseCreateIssueComment,
                    "_BaseCreateIssueComment__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.securesourcemanager_v1.SecureSourceManagerClient.CreateIssueComment",
                    extra={
                        "serviceName": "google.cloud.securesourcemanager.v1.SecureSourceManager",
                        "rpcName": "CreateIssueComment",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                SecureSourceManagerRestTransport._CreateIssueComment._get_response(
                    self._host,
                    metadata,
                    query_params,
                    self._session,
                    timeout,
                    transcoded_request,
                    body,
                )
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_issue_comment(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_issue_comment_with_metadata(
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
                    "Received response for google.cloud.securesourcemanager_v1.SecureSourceManagerClient.create_issue_comment",
                    extra={
                        "serviceName": "google.cloud.securesourcemanager.v1.SecureSourceManager",
                        "rpcName": "CreateIssueComment",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreatePullRequest(
        _BaseSecureSourceManagerRestTransport._BaseCreatePullRequest,
        SecureSourceManagerRestStub,
    ):
        def __hash__(self):
            return hash("SecureSourceManagerRestTransport.CreatePullRequest")

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
            request: secure_source_manager.CreatePullRequestRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create pull request method over HTTP.

            Args:
                request (~.secure_source_manager.CreatePullRequestRequest):
                    The request object. CreatePullRequestRequest is the
                request to create a pull request.
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

            http_options = _BaseSecureSourceManagerRestTransport._BaseCreatePullRequest._get_http_options()
            request, metadata = self._interceptor.pre_create_pull_request(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecureSourceManagerRestTransport._BaseCreatePullRequest,
                    "_BaseCreatePullRequest__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.securesourcemanager_v1.SecureSourceManagerClient.CreatePullRequest",
                    extra={
                        "serviceName": "google.cloud.securesourcemanager.v1.SecureSourceManager",
                        "rpcName": "CreatePullRequest",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                SecureSourceManagerRestTransport._CreatePullRequest._get_response(
                    self._host,
                    metadata,
                    query_params,
                    self._session,
                    timeout,
                    transcoded_request,
                    body,
                )
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_pull_request(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_pull_request_with_metadata(
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
                    "Received response for google.cloud.securesourcemanager_v1.SecureSourceManagerClient.create_pull_request",
                    extra={
                        "serviceName": "google.cloud.securesourcemanager.v1.SecureSourceManager",
                        "rpcName": "CreatePullRequest",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreatePullRequestComment(
        _BaseSecureSourceManagerRestTransport._BaseCreatePullRequestComment,
        SecureSourceManagerRestStub,
    ):
        def __hash__(self):
            return hash("SecureSourceManagerRestTransport.CreatePullRequestComment")

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
            request: secure_source_manager.CreatePullRequestCommentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create pull request
            comment method over HTTP.

                Args:
                    request (~.secure_source_manager.CreatePullRequestCommentRequest):
                        The request object. The request to create a pull request
                    comment.
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

            http_options = _BaseSecureSourceManagerRestTransport._BaseCreatePullRequestComment._get_http_options()
            request, metadata = self._interceptor.pre_create_pull_request_comment(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecureSourceManagerRestTransport._BaseCreatePullRequestComment,
                    "_BaseCreatePullRequestComment__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.securesourcemanager_v1.SecureSourceManagerClient.CreatePullRequestComment",
                    extra={
                        "serviceName": "google.cloud.securesourcemanager.v1.SecureSourceManager",
                        "rpcName": "CreatePullRequestComment",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SecureSourceManagerRestTransport._CreatePullRequestComment._get_response(
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

            resp = self._interceptor.post_create_pull_request_comment(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_pull_request_comment_with_metadata(
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
                    "Received response for google.cloud.securesourcemanager_v1.SecureSourceManagerClient.create_pull_request_comment",
                    extra={
                        "serviceName": "google.cloud.securesourcemanager.v1.SecureSourceManager",
                        "rpcName": "CreatePullRequestComment",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateRepository(
        _BaseSecureSourceManagerRestTransport._BaseCreateRepository,
        SecureSourceManagerRestStub,
    ):
        def __hash__(self):
            return hash("SecureSourceManagerRestTransport.CreateRepository")

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
            request: secure_source_manager.CreateRepositoryRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create repository method over HTTP.

            Args:
                request (~.secure_source_manager.CreateRepositoryRequest):
                    The request object. CreateRepositoryRequest is the
                request for creating a repository.
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

            http_options = _BaseSecureSourceManagerRestTransport._BaseCreateRepository._get_http_options()
            request, metadata = self._interceptor.pre_create_repository(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecureSourceManagerRestTransport._BaseCreateRepository,
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
                    f"Sending request for google.cloud.securesourcemanager_v1.SecureSourceManagerClient.CreateRepository",
                    extra={
                        "serviceName": "google.cloud.securesourcemanager.v1.SecureSourceManager",
                        "rpcName": "CreateRepository",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SecureSourceManagerRestTransport._CreateRepository._get_response(
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

            resp = self._interceptor.post_create_repository(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_repository_with_metadata(
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
                    "Received response for google.cloud.securesourcemanager_v1.SecureSourceManagerClient.create_repository",
                    extra={
                        "serviceName": "google.cloud.securesourcemanager.v1.SecureSourceManager",
                        "rpcName": "CreateRepository",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteBranchRule(
        _BaseSecureSourceManagerRestTransport._BaseDeleteBranchRule,
        SecureSourceManagerRestStub,
    ):
        def __hash__(self):
            return hash("SecureSourceManagerRestTransport.DeleteBranchRule")

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
            request: secure_source_manager.DeleteBranchRuleRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete branch rule method over HTTP.

            Args:
                request (~.secure_source_manager.DeleteBranchRuleRequest):
                    The request object. DeleteBranchRuleRequest is the
                request to delete a branch rule.
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

            http_options = _BaseSecureSourceManagerRestTransport._BaseDeleteBranchRule._get_http_options()
            request, metadata = self._interceptor.pre_delete_branch_rule(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecureSourceManagerRestTransport._BaseDeleteBranchRule,
                    "_BaseDeleteBranchRule__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.securesourcemanager_v1.SecureSourceManagerClient.DeleteBranchRule",
                    extra={
                        "serviceName": "google.cloud.securesourcemanager.v1.SecureSourceManager",
                        "rpcName": "DeleteBranchRule",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SecureSourceManagerRestTransport._DeleteBranchRule._get_response(
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
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_delete_branch_rule(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_branch_rule_with_metadata(
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
                    "Received response for google.cloud.securesourcemanager_v1.SecureSourceManagerClient.delete_branch_rule",
                    extra={
                        "serviceName": "google.cloud.securesourcemanager.v1.SecureSourceManager",
                        "rpcName": "DeleteBranchRule",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteHook(
        _BaseSecureSourceManagerRestTransport._BaseDeleteHook,
        SecureSourceManagerRestStub,
    ):
        def __hash__(self):
            return hash("SecureSourceManagerRestTransport.DeleteHook")

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
            request: secure_source_manager.DeleteHookRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete hook method over HTTP.

            Args:
                request (~.secure_source_manager.DeleteHookRequest):
                    The request object. DeleteHookRequest is the request to
                delete a hook.
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

            http_options = _BaseSecureSourceManagerRestTransport._BaseDeleteHook._get_http_options()
            request, metadata = self._interceptor.pre_delete_hook(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecureSourceManagerRestTransport._BaseDeleteHook,
                    "_BaseDeleteHook__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.securesourcemanager_v1.SecureSourceManagerClient.DeleteHook",
                    extra={
                        "serviceName": "google.cloud.securesourcemanager.v1.SecureSourceManager",
                        "rpcName": "DeleteHook",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SecureSourceManagerRestTransport._DeleteHook._get_response(
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
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_delete_hook(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_hook_with_metadata(
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
                    "Received response for google.cloud.securesourcemanager_v1.SecureSourceManagerClient.delete_hook",
                    extra={
                        "serviceName": "google.cloud.securesourcemanager.v1.SecureSourceManager",
                        "rpcName": "DeleteHook",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteInstance(
        _BaseSecureSourceManagerRestTransport._BaseDeleteInstance,
        SecureSourceManagerRestStub,
    ):
        def __hash__(self):
            return hash("SecureSourceManagerRestTransport.DeleteInstance")

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
            request: secure_source_manager.DeleteInstanceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete instance method over HTTP.

            Args:
                request (~.secure_source_manager.DeleteInstanceRequest):
                    The request object. DeleteInstanceRequest is the request
                for deleting an instance.
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

            http_options = _BaseSecureSourceManagerRestTransport._BaseDeleteInstance._get_http_options()
            request, metadata = self._interceptor.pre_delete_instance(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecureSourceManagerRestTransport._BaseDeleteInstance,
                    "_BaseDeleteInstance__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.securesourcemanager_v1.SecureSourceManagerClient.DeleteInstance",
                    extra={
                        "serviceName": "google.cloud.securesourcemanager.v1.SecureSourceManager",
                        "rpcName": "DeleteInstance",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SecureSourceManagerRestTransport._DeleteInstance._get_response(
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
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_delete_instance(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_instance_with_metadata(
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
                    "Received response for google.cloud.securesourcemanager_v1.SecureSourceManagerClient.delete_instance",
                    extra={
                        "serviceName": "google.cloud.securesourcemanager.v1.SecureSourceManager",
                        "rpcName": "DeleteInstance",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteIssue(
        _BaseSecureSourceManagerRestTransport._BaseDeleteIssue,
        SecureSourceManagerRestStub,
    ):
        def __hash__(self):
            return hash("SecureSourceManagerRestTransport.DeleteIssue")

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
            request: secure_source_manager.DeleteIssueRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete issue method over HTTP.

            Args:
                request (~.secure_source_manager.DeleteIssueRequest):
                    The request object. The request to delete an issue.
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

            http_options = _BaseSecureSourceManagerRestTransport._BaseDeleteIssue._get_http_options()
            request, metadata = self._interceptor.pre_delete_issue(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecureSourceManagerRestTransport._BaseDeleteIssue,
                    "_BaseDeleteIssue__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.securesourcemanager_v1.SecureSourceManagerClient.DeleteIssue",
                    extra={
                        "serviceName": "google.cloud.securesourcemanager.v1.SecureSourceManager",
                        "rpcName": "DeleteIssue",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SecureSourceManagerRestTransport._DeleteIssue._get_response(
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
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_delete_issue(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_issue_with_metadata(
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
                    "Received response for google.cloud.securesourcemanager_v1.SecureSourceManagerClient.delete_issue",
                    extra={
                        "serviceName": "google.cloud.securesourcemanager.v1.SecureSourceManager",
                        "rpcName": "DeleteIssue",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteIssueComment(
        _BaseSecureSourceManagerRestTransport._BaseDeleteIssueComment,
        SecureSourceManagerRestStub,
    ):
        def __hash__(self):
            return hash("SecureSourceManagerRestTransport.DeleteIssueComment")

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
            request: secure_source_manager.DeleteIssueCommentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete issue comment method over HTTP.

            Args:
                request (~.secure_source_manager.DeleteIssueCommentRequest):
                    The request object. The request to delete an issue
                comment.
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

            http_options = _BaseSecureSourceManagerRestTransport._BaseDeleteIssueComment._get_http_options()
            request, metadata = self._interceptor.pre_delete_issue_comment(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecureSourceManagerRestTransport._BaseDeleteIssueComment,
                    "_BaseDeleteIssueComment__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.securesourcemanager_v1.SecureSourceManagerClient.DeleteIssueComment",
                    extra={
                        "serviceName": "google.cloud.securesourcemanager.v1.SecureSourceManager",
                        "rpcName": "DeleteIssueComment",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                SecureSourceManagerRestTransport._DeleteIssueComment._get_response(
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
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_delete_issue_comment(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_issue_comment_with_metadata(
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
                    "Received response for google.cloud.securesourcemanager_v1.SecureSourceManagerClient.delete_issue_comment",
                    extra={
                        "serviceName": "google.cloud.securesourcemanager.v1.SecureSourceManager",
                        "rpcName": "DeleteIssueComment",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeletePullRequestComment(
        _BaseSecureSourceManagerRestTransport._BaseDeletePullRequestComment,
        SecureSourceManagerRestStub,
    ):
        def __hash__(self):
            return hash("SecureSourceManagerRestTransport.DeletePullRequestComment")

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
            request: secure_source_manager.DeletePullRequestCommentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete pull request
            comment method over HTTP.

                Args:
                    request (~.secure_source_manager.DeletePullRequestCommentRequest):
                        The request object. The request to delete a pull request
                    comment. A Review PullRequestComment
                    cannot be deleted.
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

            http_options = _BaseSecureSourceManagerRestTransport._BaseDeletePullRequestComment._get_http_options()
            request, metadata = self._interceptor.pre_delete_pull_request_comment(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecureSourceManagerRestTransport._BaseDeletePullRequestComment,
                    "_BaseDeletePullRequestComment__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.securesourcemanager_v1.SecureSourceManagerClient.DeletePullRequestComment",
                    extra={
                        "serviceName": "google.cloud.securesourcemanager.v1.SecureSourceManager",
                        "rpcName": "DeletePullRequestComment",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SecureSourceManagerRestTransport._DeletePullRequestComment._get_response(
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
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_delete_pull_request_comment(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_pull_request_comment_with_metadata(
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
                    "Received response for google.cloud.securesourcemanager_v1.SecureSourceManagerClient.delete_pull_request_comment",
                    extra={
                        "serviceName": "google.cloud.securesourcemanager.v1.SecureSourceManager",
                        "rpcName": "DeletePullRequestComment",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteRepository(
        _BaseSecureSourceManagerRestTransport._BaseDeleteRepository,
        SecureSourceManagerRestStub,
    ):
        def __hash__(self):
            return hash("SecureSourceManagerRestTransport.DeleteRepository")

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
            request: secure_source_manager.DeleteRepositoryRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete repository method over HTTP.

            Args:
                request (~.secure_source_manager.DeleteRepositoryRequest):
                    The request object. DeleteRepositoryRequest is the
                request to delete a repository.
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

            http_options = _BaseSecureSourceManagerRestTransport._BaseDeleteRepository._get_http_options()
            request, metadata = self._interceptor.pre_delete_repository(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecureSourceManagerRestTransport._BaseDeleteRepository,
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
                    f"Sending request for google.cloud.securesourcemanager_v1.SecureSourceManagerClient.DeleteRepository",
                    extra={
                        "serviceName": "google.cloud.securesourcemanager.v1.SecureSourceManager",
                        "rpcName": "DeleteRepository",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SecureSourceManagerRestTransport._DeleteRepository._get_response(
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
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_delete_repository(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_repository_with_metadata(
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
                    "Received response for google.cloud.securesourcemanager_v1.SecureSourceManagerClient.delete_repository",
                    extra={
                        "serviceName": "google.cloud.securesourcemanager.v1.SecureSourceManager",
                        "rpcName": "DeleteRepository",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _FetchBlob(
        _BaseSecureSourceManagerRestTransport._BaseFetchBlob,
        SecureSourceManagerRestStub,
    ):
        def __hash__(self):
            return hash("SecureSourceManagerRestTransport.FetchBlob")

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
            request: secure_source_manager.FetchBlobRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> secure_source_manager.FetchBlobResponse:
            r"""Call the fetch blob method over HTTP.

            Args:
                request (~.secure_source_manager.FetchBlobRequest):
                    The request object. Request message for fetching a blob
                (file content) from a repository.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.secure_source_manager.FetchBlobResponse:
                    Response message containing the
                content of a blob.

            """

            http_options = (
                _BaseSecureSourceManagerRestTransport._BaseFetchBlob._get_http_options()
            )
            request, metadata = self._interceptor.pre_fetch_blob(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecureSourceManagerRestTransport._BaseFetchBlob,
                    "_BaseFetchBlob__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.securesourcemanager_v1.SecureSourceManagerClient.FetchBlob",
                    extra={
                        "serviceName": "google.cloud.securesourcemanager.v1.SecureSourceManager",
                        "rpcName": "FetchBlob",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SecureSourceManagerRestTransport._FetchBlob._get_response(
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
            resp = secure_source_manager.FetchBlobResponse()
            pb_resp = secure_source_manager.FetchBlobResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_fetch_blob(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_fetch_blob_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = secure_source_manager.FetchBlobResponse.to_json(
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
                    "Received response for google.cloud.securesourcemanager_v1.SecureSourceManagerClient.fetch_blob",
                    extra={
                        "serviceName": "google.cloud.securesourcemanager.v1.SecureSourceManager",
                        "rpcName": "FetchBlob",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _FetchRefs(
        _BaseSecureSourceManagerRestTransport._BaseFetchRefs,
        SecureSourceManagerRestStub,
    ):
        def __hash__(self):
            return hash("SecureSourceManagerRestTransport.FetchRefs")

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
            request: secure_source_manager.FetchRefsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> secure_source_manager.FetchRefsResponse:
            r"""Call the fetch refs method over HTTP.

            Args:
                request (~.secure_source_manager.FetchRefsRequest):
                    The request object. Request message for fetching git
                references from a repository.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.secure_source_manager.FetchRefsResponse:
                    Response message containing a list of
                git references.

            """

            http_options = (
                _BaseSecureSourceManagerRestTransport._BaseFetchRefs._get_http_options()
            )
            request, metadata = self._interceptor.pre_fetch_refs(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecureSourceManagerRestTransport._BaseFetchRefs,
                    "_BaseFetchRefs__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.securesourcemanager_v1.SecureSourceManagerClient.FetchRefs",
                    extra={
                        "serviceName": "google.cloud.securesourcemanager.v1.SecureSourceManager",
                        "rpcName": "FetchRefs",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SecureSourceManagerRestTransport._FetchRefs._get_response(
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
            resp = secure_source_manager.FetchRefsResponse()
            pb_resp = secure_source_manager.FetchRefsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_fetch_refs(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_fetch_refs_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = secure_source_manager.FetchRefsResponse.to_json(
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
                    "Received response for google.cloud.securesourcemanager_v1.SecureSourceManagerClient.fetch_refs",
                    extra={
                        "serviceName": "google.cloud.securesourcemanager.v1.SecureSourceManager",
                        "rpcName": "FetchRefs",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _FetchTree(
        _BaseSecureSourceManagerRestTransport._BaseFetchTree,
        SecureSourceManagerRestStub,
    ):
        def __hash__(self):
            return hash("SecureSourceManagerRestTransport.FetchTree")

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
            request: secure_source_manager.FetchTreeRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> secure_source_manager.FetchTreeResponse:
            r"""Call the fetch tree method over HTTP.

            Args:
                request (~.secure_source_manager.FetchTreeRequest):
                    The request object. Request message for fetching a tree
                structure from a repository.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.secure_source_manager.FetchTreeResponse:
                    Response message containing a list of
                TreeEntry objects.

            """

            http_options = (
                _BaseSecureSourceManagerRestTransport._BaseFetchTree._get_http_options()
            )
            request, metadata = self._interceptor.pre_fetch_tree(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecureSourceManagerRestTransport._BaseFetchTree,
                    "_BaseFetchTree__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.securesourcemanager_v1.SecureSourceManagerClient.FetchTree",
                    extra={
                        "serviceName": "google.cloud.securesourcemanager.v1.SecureSourceManager",
                        "rpcName": "FetchTree",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SecureSourceManagerRestTransport._FetchTree._get_response(
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
            resp = secure_source_manager.FetchTreeResponse()
            pb_resp = secure_source_manager.FetchTreeResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_fetch_tree(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_fetch_tree_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = secure_source_manager.FetchTreeResponse.to_json(
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
                    "Received response for google.cloud.securesourcemanager_v1.SecureSourceManagerClient.fetch_tree",
                    extra={
                        "serviceName": "google.cloud.securesourcemanager.v1.SecureSourceManager",
                        "rpcName": "FetchTree",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetBranchRule(
        _BaseSecureSourceManagerRestTransport._BaseGetBranchRule,
        SecureSourceManagerRestStub,
    ):
        def __hash__(self):
            return hash("SecureSourceManagerRestTransport.GetBranchRule")

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
            request: secure_source_manager.GetBranchRuleRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> secure_source_manager.BranchRule:
            r"""Call the get branch rule method over HTTP.

            Args:
                request (~.secure_source_manager.GetBranchRuleRequest):
                    The request object. GetBranchRuleRequest is the request
                for getting a branch rule.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.secure_source_manager.BranchRule:
                    Metadata of a BranchRule. BranchRule
                is the protection rule to enforce
                pre-defined rules on designated branches
                within a repository.

            """

            http_options = _BaseSecureSourceManagerRestTransport._BaseGetBranchRule._get_http_options()
            request, metadata = self._interceptor.pre_get_branch_rule(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecureSourceManagerRestTransport._BaseGetBranchRule,
                    "_BaseGetBranchRule__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.securesourcemanager_v1.SecureSourceManagerClient.GetBranchRule",
                    extra={
                        "serviceName": "google.cloud.securesourcemanager.v1.SecureSourceManager",
                        "rpcName": "GetBranchRule",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SecureSourceManagerRestTransport._GetBranchRule._get_response(
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
            resp = secure_source_manager.BranchRule()
            pb_resp = secure_source_manager.BranchRule.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_branch_rule(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_branch_rule_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = secure_source_manager.BranchRule.to_json(
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
                    "Received response for google.cloud.securesourcemanager_v1.SecureSourceManagerClient.get_branch_rule",
                    extra={
                        "serviceName": "google.cloud.securesourcemanager.v1.SecureSourceManager",
                        "rpcName": "GetBranchRule",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetHook(
        _BaseSecureSourceManagerRestTransport._BaseGetHook, SecureSourceManagerRestStub
    ):
        def __hash__(self):
            return hash("SecureSourceManagerRestTransport.GetHook")

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
            request: secure_source_manager.GetHookRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> secure_source_manager.Hook:
            r"""Call the get hook method over HTTP.

            Args:
                request (~.secure_source_manager.GetHookRequest):
                    The request object. GetHookRequest is the request for
                getting a hook.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.secure_source_manager.Hook:
                    Metadata of a Secure Source Manager
                Hook.

            """

            http_options = (
                _BaseSecureSourceManagerRestTransport._BaseGetHook._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_hook(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecureSourceManagerRestTransport._BaseGetHook,
                    "_BaseGetHook__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.securesourcemanager_v1.SecureSourceManagerClient.GetHook",
                    extra={
                        "serviceName": "google.cloud.securesourcemanager.v1.SecureSourceManager",
                        "rpcName": "GetHook",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SecureSourceManagerRestTransport._GetHook._get_response(
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
            resp = secure_source_manager.Hook()
            pb_resp = secure_source_manager.Hook.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_hook(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_hook_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = secure_source_manager.Hook.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.securesourcemanager_v1.SecureSourceManagerClient.get_hook",
                    extra={
                        "serviceName": "google.cloud.securesourcemanager.v1.SecureSourceManager",
                        "rpcName": "GetHook",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetIamPolicyRepo(
        _BaseSecureSourceManagerRestTransport._BaseGetIamPolicyRepo,
        SecureSourceManagerRestStub,
    ):
        def __hash__(self):
            return hash("SecureSourceManagerRestTransport.GetIamPolicyRepo")

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
            r"""Call the get iam policy repo method over HTTP.

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

            http_options = _BaseSecureSourceManagerRestTransport._BaseGetIamPolicyRepo._get_http_options()
            request, metadata = self._interceptor.pre_get_iam_policy_repo(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecureSourceManagerRestTransport._BaseGetIamPolicyRepo,
                    "_BaseGetIamPolicyRepo__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.securesourcemanager_v1.SecureSourceManagerClient.GetIamPolicyRepo",
                    extra={
                        "serviceName": "google.cloud.securesourcemanager.v1.SecureSourceManager",
                        "rpcName": "GetIamPolicyRepo",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SecureSourceManagerRestTransport._GetIamPolicyRepo._get_response(
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

            resp = self._interceptor.post_get_iam_policy_repo(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_iam_policy_repo_with_metadata(
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
                    "Received response for google.cloud.securesourcemanager_v1.SecureSourceManagerClient.get_iam_policy_repo",
                    extra={
                        "serviceName": "google.cloud.securesourcemanager.v1.SecureSourceManager",
                        "rpcName": "GetIamPolicyRepo",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetInstance(
        _BaseSecureSourceManagerRestTransport._BaseGetInstance,
        SecureSourceManagerRestStub,
    ):
        def __hash__(self):
            return hash("SecureSourceManagerRestTransport.GetInstance")

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
            request: secure_source_manager.GetInstanceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> secure_source_manager.Instance:
            r"""Call the get instance method over HTTP.

            Args:
                request (~.secure_source_manager.GetInstanceRequest):
                    The request object. GetInstanceRequest is the request for
                getting an instance.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.secure_source_manager.Instance:
                    A resource that represents a Secure
                Source Manager instance.

            """

            http_options = _BaseSecureSourceManagerRestTransport._BaseGetInstance._get_http_options()
            request, metadata = self._interceptor.pre_get_instance(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecureSourceManagerRestTransport._BaseGetInstance,
                    "_BaseGetInstance__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.securesourcemanager_v1.SecureSourceManagerClient.GetInstance",
                    extra={
                        "serviceName": "google.cloud.securesourcemanager.v1.SecureSourceManager",
                        "rpcName": "GetInstance",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SecureSourceManagerRestTransport._GetInstance._get_response(
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
            resp = secure_source_manager.Instance()
            pb_resp = secure_source_manager.Instance.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_instance(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_instance_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = secure_source_manager.Instance.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.securesourcemanager_v1.SecureSourceManagerClient.get_instance",
                    extra={
                        "serviceName": "google.cloud.securesourcemanager.v1.SecureSourceManager",
                        "rpcName": "GetInstance",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetIssue(
        _BaseSecureSourceManagerRestTransport._BaseGetIssue, SecureSourceManagerRestStub
    ):
        def __hash__(self):
            return hash("SecureSourceManagerRestTransport.GetIssue")

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
            request: secure_source_manager.GetIssueRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> secure_source_manager.Issue:
            r"""Call the get issue method over HTTP.

            Args:
                request (~.secure_source_manager.GetIssueRequest):
                    The request object. The request to get an issue.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.secure_source_manager.Issue:
                    Metadata of an Issue.
            """

            http_options = (
                _BaseSecureSourceManagerRestTransport._BaseGetIssue._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_issue(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecureSourceManagerRestTransport._BaseGetIssue,
                    "_BaseGetIssue__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.securesourcemanager_v1.SecureSourceManagerClient.GetIssue",
                    extra={
                        "serviceName": "google.cloud.securesourcemanager.v1.SecureSourceManager",
                        "rpcName": "GetIssue",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SecureSourceManagerRestTransport._GetIssue._get_response(
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
            resp = secure_source_manager.Issue()
            pb_resp = secure_source_manager.Issue.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_issue(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_issue_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = secure_source_manager.Issue.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.securesourcemanager_v1.SecureSourceManagerClient.get_issue",
                    extra={
                        "serviceName": "google.cloud.securesourcemanager.v1.SecureSourceManager",
                        "rpcName": "GetIssue",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetIssueComment(
        _BaseSecureSourceManagerRestTransport._BaseGetIssueComment,
        SecureSourceManagerRestStub,
    ):
        def __hash__(self):
            return hash("SecureSourceManagerRestTransport.GetIssueComment")

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
            request: secure_source_manager.GetIssueCommentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> secure_source_manager.IssueComment:
            r"""Call the get issue comment method over HTTP.

            Args:
                request (~.secure_source_manager.GetIssueCommentRequest):
                    The request object. The request to get an issue comment.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.secure_source_manager.IssueComment:
                    IssueComment represents a comment on
                an issue.

            """

            http_options = _BaseSecureSourceManagerRestTransport._BaseGetIssueComment._get_http_options()
            request, metadata = self._interceptor.pre_get_issue_comment(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecureSourceManagerRestTransport._BaseGetIssueComment,
                    "_BaseGetIssueComment__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.securesourcemanager_v1.SecureSourceManagerClient.GetIssueComment",
                    extra={
                        "serviceName": "google.cloud.securesourcemanager.v1.SecureSourceManager",
                        "rpcName": "GetIssueComment",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SecureSourceManagerRestTransport._GetIssueComment._get_response(
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
            resp = secure_source_manager.IssueComment()
            pb_resp = secure_source_manager.IssueComment.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_issue_comment(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_issue_comment_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = secure_source_manager.IssueComment.to_json(
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
                    "Received response for google.cloud.securesourcemanager_v1.SecureSourceManagerClient.get_issue_comment",
                    extra={
                        "serviceName": "google.cloud.securesourcemanager.v1.SecureSourceManager",
                        "rpcName": "GetIssueComment",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetPullRequest(
        _BaseSecureSourceManagerRestTransport._BaseGetPullRequest,
        SecureSourceManagerRestStub,
    ):
        def __hash__(self):
            return hash("SecureSourceManagerRestTransport.GetPullRequest")

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
            request: secure_source_manager.GetPullRequestRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> secure_source_manager.PullRequest:
            r"""Call the get pull request method over HTTP.

            Args:
                request (~.secure_source_manager.GetPullRequestRequest):
                    The request object. GetPullRequestRequest is the request
                to get a pull request.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.secure_source_manager.PullRequest:
                    Metadata of a PullRequest.
                PullRequest is the request from a user
                to merge a branch (head) into another
                branch (base).

            """

            http_options = _BaseSecureSourceManagerRestTransport._BaseGetPullRequest._get_http_options()
            request, metadata = self._interceptor.pre_get_pull_request(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecureSourceManagerRestTransport._BaseGetPullRequest,
                    "_BaseGetPullRequest__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.securesourcemanager_v1.SecureSourceManagerClient.GetPullRequest",
                    extra={
                        "serviceName": "google.cloud.securesourcemanager.v1.SecureSourceManager",
                        "rpcName": "GetPullRequest",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SecureSourceManagerRestTransport._GetPullRequest._get_response(
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
            resp = secure_source_manager.PullRequest()
            pb_resp = secure_source_manager.PullRequest.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_pull_request(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_pull_request_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = secure_source_manager.PullRequest.to_json(
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
                    "Received response for google.cloud.securesourcemanager_v1.SecureSourceManagerClient.get_pull_request",
                    extra={
                        "serviceName": "google.cloud.securesourcemanager.v1.SecureSourceManager",
                        "rpcName": "GetPullRequest",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetPullRequestComment(
        _BaseSecureSourceManagerRestTransport._BaseGetPullRequestComment,
        SecureSourceManagerRestStub,
    ):
        def __hash__(self):
            return hash("SecureSourceManagerRestTransport.GetPullRequestComment")

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
            request: secure_source_manager.GetPullRequestCommentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> secure_source_manager.PullRequestComment:
            r"""Call the get pull request comment method over HTTP.

            Args:
                request (~.secure_source_manager.GetPullRequestCommentRequest):
                    The request object. The request to get a pull request
                comment.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.secure_source_manager.PullRequestComment:
                    PullRequestComment represents a
                comment on a pull request.

            """

            http_options = _BaseSecureSourceManagerRestTransport._BaseGetPullRequestComment._get_http_options()
            request, metadata = self._interceptor.pre_get_pull_request_comment(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecureSourceManagerRestTransport._BaseGetPullRequestComment,
                    "_BaseGetPullRequestComment__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.securesourcemanager_v1.SecureSourceManagerClient.GetPullRequestComment",
                    extra={
                        "serviceName": "google.cloud.securesourcemanager.v1.SecureSourceManager",
                        "rpcName": "GetPullRequestComment",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                SecureSourceManagerRestTransport._GetPullRequestComment._get_response(
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
            resp = secure_source_manager.PullRequestComment()
            pb_resp = secure_source_manager.PullRequestComment.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_pull_request_comment(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_pull_request_comment_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = secure_source_manager.PullRequestComment.to_json(
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
                    "Received response for google.cloud.securesourcemanager_v1.SecureSourceManagerClient.get_pull_request_comment",
                    extra={
                        "serviceName": "google.cloud.securesourcemanager.v1.SecureSourceManager",
                        "rpcName": "GetPullRequestComment",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetRepository(
        _BaseSecureSourceManagerRestTransport._BaseGetRepository,
        SecureSourceManagerRestStub,
    ):
        def __hash__(self):
            return hash("SecureSourceManagerRestTransport.GetRepository")

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
            request: secure_source_manager.GetRepositoryRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> secure_source_manager.Repository:
            r"""Call the get repository method over HTTP.

            Args:
                request (~.secure_source_manager.GetRepositoryRequest):
                    The request object. GetRepositoryRequest is the request
                for getting a repository.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.secure_source_manager.Repository:
                    Metadata of a Secure Source Manager
                repository.

            """

            http_options = _BaseSecureSourceManagerRestTransport._BaseGetRepository._get_http_options()
            request, metadata = self._interceptor.pre_get_repository(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecureSourceManagerRestTransport._BaseGetRepository,
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
                    f"Sending request for google.cloud.securesourcemanager_v1.SecureSourceManagerClient.GetRepository",
                    extra={
                        "serviceName": "google.cloud.securesourcemanager.v1.SecureSourceManager",
                        "rpcName": "GetRepository",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SecureSourceManagerRestTransport._GetRepository._get_response(
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
            resp = secure_source_manager.Repository()
            pb_resp = secure_source_manager.Repository.pb(resp)

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
                    response_payload = secure_source_manager.Repository.to_json(
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
                    "Received response for google.cloud.securesourcemanager_v1.SecureSourceManagerClient.get_repository",
                    extra={
                        "serviceName": "google.cloud.securesourcemanager.v1.SecureSourceManager",
                        "rpcName": "GetRepository",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListBranchRules(
        _BaseSecureSourceManagerRestTransport._BaseListBranchRules,
        SecureSourceManagerRestStub,
    ):
        def __hash__(self):
            return hash("SecureSourceManagerRestTransport.ListBranchRules")

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
            request: secure_source_manager.ListBranchRulesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> secure_source_manager.ListBranchRulesResponse:
            r"""Call the list branch rules method over HTTP.

            Args:
                request (~.secure_source_manager.ListBranchRulesRequest):
                    The request object. ListBranchRulesRequest is the request
                to list branch rules.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.secure_source_manager.ListBranchRulesResponse:
                    ListBranchRulesResponse is the
                response to listing branchRules.

            """

            http_options = _BaseSecureSourceManagerRestTransport._BaseListBranchRules._get_http_options()
            request, metadata = self._interceptor.pre_list_branch_rules(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecureSourceManagerRestTransport._BaseListBranchRules,
                    "_BaseListBranchRules__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.securesourcemanager_v1.SecureSourceManagerClient.ListBranchRules",
                    extra={
                        "serviceName": "google.cloud.securesourcemanager.v1.SecureSourceManager",
                        "rpcName": "ListBranchRules",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SecureSourceManagerRestTransport._ListBranchRules._get_response(
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
            resp = secure_source_manager.ListBranchRulesResponse()
            pb_resp = secure_source_manager.ListBranchRulesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_branch_rules(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_branch_rules_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        secure_source_manager.ListBranchRulesResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.securesourcemanager_v1.SecureSourceManagerClient.list_branch_rules",
                    extra={
                        "serviceName": "google.cloud.securesourcemanager.v1.SecureSourceManager",
                        "rpcName": "ListBranchRules",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListHooks(
        _BaseSecureSourceManagerRestTransport._BaseListHooks,
        SecureSourceManagerRestStub,
    ):
        def __hash__(self):
            return hash("SecureSourceManagerRestTransport.ListHooks")

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
            request: secure_source_manager.ListHooksRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> secure_source_manager.ListHooksResponse:
            r"""Call the list hooks method over HTTP.

            Args:
                request (~.secure_source_manager.ListHooksRequest):
                    The request object. ListHooksRequest is request to list
                hooks.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.secure_source_manager.ListHooksResponse:
                    ListHooksResponse is response to list
                hooks.

            """

            http_options = (
                _BaseSecureSourceManagerRestTransport._BaseListHooks._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_hooks(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecureSourceManagerRestTransport._BaseListHooks,
                    "_BaseListHooks__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.securesourcemanager_v1.SecureSourceManagerClient.ListHooks",
                    extra={
                        "serviceName": "google.cloud.securesourcemanager.v1.SecureSourceManager",
                        "rpcName": "ListHooks",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SecureSourceManagerRestTransport._ListHooks._get_response(
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
            resp = secure_source_manager.ListHooksResponse()
            pb_resp = secure_source_manager.ListHooksResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_hooks(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_hooks_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = secure_source_manager.ListHooksResponse.to_json(
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
                    "Received response for google.cloud.securesourcemanager_v1.SecureSourceManagerClient.list_hooks",
                    extra={
                        "serviceName": "google.cloud.securesourcemanager.v1.SecureSourceManager",
                        "rpcName": "ListHooks",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListInstances(
        _BaseSecureSourceManagerRestTransport._BaseListInstances,
        SecureSourceManagerRestStub,
    ):
        def __hash__(self):
            return hash("SecureSourceManagerRestTransport.ListInstances")

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
            request: secure_source_manager.ListInstancesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> secure_source_manager.ListInstancesResponse:
            r"""Call the list instances method over HTTP.

            Args:
                request (~.secure_source_manager.ListInstancesRequest):
                    The request object. ListInstancesRequest is the request
                to list instances.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.secure_source_manager.ListInstancesResponse:

            """

            http_options = _BaseSecureSourceManagerRestTransport._BaseListInstances._get_http_options()
            request, metadata = self._interceptor.pre_list_instances(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecureSourceManagerRestTransport._BaseListInstances,
                    "_BaseListInstances__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.securesourcemanager_v1.SecureSourceManagerClient.ListInstances",
                    extra={
                        "serviceName": "google.cloud.securesourcemanager.v1.SecureSourceManager",
                        "rpcName": "ListInstances",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SecureSourceManagerRestTransport._ListInstances._get_response(
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
            resp = secure_source_manager.ListInstancesResponse()
            pb_resp = secure_source_manager.ListInstancesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_instances(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_instances_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        secure_source_manager.ListInstancesResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.securesourcemanager_v1.SecureSourceManagerClient.list_instances",
                    extra={
                        "serviceName": "google.cloud.securesourcemanager.v1.SecureSourceManager",
                        "rpcName": "ListInstances",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListIssueComments(
        _BaseSecureSourceManagerRestTransport._BaseListIssueComments,
        SecureSourceManagerRestStub,
    ):
        def __hash__(self):
            return hash("SecureSourceManagerRestTransport.ListIssueComments")

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
            request: secure_source_manager.ListIssueCommentsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> secure_source_manager.ListIssueCommentsResponse:
            r"""Call the list issue comments method over HTTP.

            Args:
                request (~.secure_source_manager.ListIssueCommentsRequest):
                    The request object. The request to list issue comments.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.secure_source_manager.ListIssueCommentsResponse:
                    The response to list issue comments.
            """

            http_options = _BaseSecureSourceManagerRestTransport._BaseListIssueComments._get_http_options()
            request, metadata = self._interceptor.pre_list_issue_comments(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecureSourceManagerRestTransport._BaseListIssueComments,
                    "_BaseListIssueComments__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.securesourcemanager_v1.SecureSourceManagerClient.ListIssueComments",
                    extra={
                        "serviceName": "google.cloud.securesourcemanager.v1.SecureSourceManager",
                        "rpcName": "ListIssueComments",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                SecureSourceManagerRestTransport._ListIssueComments._get_response(
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
            resp = secure_source_manager.ListIssueCommentsResponse()
            pb_resp = secure_source_manager.ListIssueCommentsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_issue_comments(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_issue_comments_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        secure_source_manager.ListIssueCommentsResponse.to_json(
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
                    "Received response for google.cloud.securesourcemanager_v1.SecureSourceManagerClient.list_issue_comments",
                    extra={
                        "serviceName": "google.cloud.securesourcemanager.v1.SecureSourceManager",
                        "rpcName": "ListIssueComments",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListIssues(
        _BaseSecureSourceManagerRestTransport._BaseListIssues,
        SecureSourceManagerRestStub,
    ):
        def __hash__(self):
            return hash("SecureSourceManagerRestTransport.ListIssues")

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
            request: secure_source_manager.ListIssuesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> secure_source_manager.ListIssuesResponse:
            r"""Call the list issues method over HTTP.

            Args:
                request (~.secure_source_manager.ListIssuesRequest):
                    The request object. The request to list issues.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.secure_source_manager.ListIssuesResponse:
                    The response to list issues.
            """

            http_options = _BaseSecureSourceManagerRestTransport._BaseListIssues._get_http_options()
            request, metadata = self._interceptor.pre_list_issues(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecureSourceManagerRestTransport._BaseListIssues,
                    "_BaseListIssues__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.securesourcemanager_v1.SecureSourceManagerClient.ListIssues",
                    extra={
                        "serviceName": "google.cloud.securesourcemanager.v1.SecureSourceManager",
                        "rpcName": "ListIssues",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SecureSourceManagerRestTransport._ListIssues._get_response(
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
            resp = secure_source_manager.ListIssuesResponse()
            pb_resp = secure_source_manager.ListIssuesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_issues(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_issues_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = secure_source_manager.ListIssuesResponse.to_json(
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
                    "Received response for google.cloud.securesourcemanager_v1.SecureSourceManagerClient.list_issues",
                    extra={
                        "serviceName": "google.cloud.securesourcemanager.v1.SecureSourceManager",
                        "rpcName": "ListIssues",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListPullRequestComments(
        _BaseSecureSourceManagerRestTransport._BaseListPullRequestComments,
        SecureSourceManagerRestStub,
    ):
        def __hash__(self):
            return hash("SecureSourceManagerRestTransport.ListPullRequestComments")

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
            request: secure_source_manager.ListPullRequestCommentsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> secure_source_manager.ListPullRequestCommentsResponse:
            r"""Call the list pull request
            comments method over HTTP.

                Args:
                    request (~.secure_source_manager.ListPullRequestCommentsRequest):
                        The request object. The request to list pull request
                    comments.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.secure_source_manager.ListPullRequestCommentsResponse:
                        The response to list pull request
                    comments.

            """

            http_options = _BaseSecureSourceManagerRestTransport._BaseListPullRequestComments._get_http_options()
            request, metadata = self._interceptor.pre_list_pull_request_comments(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecureSourceManagerRestTransport._BaseListPullRequestComments,
                    "_BaseListPullRequestComments__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.securesourcemanager_v1.SecureSourceManagerClient.ListPullRequestComments",
                    extra={
                        "serviceName": "google.cloud.securesourcemanager.v1.SecureSourceManager",
                        "rpcName": "ListPullRequestComments",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                SecureSourceManagerRestTransport._ListPullRequestComments._get_response(
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
            resp = secure_source_manager.ListPullRequestCommentsResponse()
            pb_resp = secure_source_manager.ListPullRequestCommentsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_pull_request_comments(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_pull_request_comments_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        secure_source_manager.ListPullRequestCommentsResponse.to_json(
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
                    "Received response for google.cloud.securesourcemanager_v1.SecureSourceManagerClient.list_pull_request_comments",
                    extra={
                        "serviceName": "google.cloud.securesourcemanager.v1.SecureSourceManager",
                        "rpcName": "ListPullRequestComments",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListPullRequestFileDiffs(
        _BaseSecureSourceManagerRestTransport._BaseListPullRequestFileDiffs,
        SecureSourceManagerRestStub,
    ):
        def __hash__(self):
            return hash("SecureSourceManagerRestTransport.ListPullRequestFileDiffs")

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
            request: secure_source_manager.ListPullRequestFileDiffsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> secure_source_manager.ListPullRequestFileDiffsResponse:
            r"""Call the list pull request file
            diffs method over HTTP.

                Args:
                    request (~.secure_source_manager.ListPullRequestFileDiffsRequest):
                        The request object. ListPullRequestFileDiffsRequest is
                    the request to list pull request file
                    diffs.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.secure_source_manager.ListPullRequestFileDiffsResponse:
                        ListPullRequestFileDiffsResponse is
                    the response containing file diffs
                    returned from ListPullRequestFileDiffs.

            """

            http_options = _BaseSecureSourceManagerRestTransport._BaseListPullRequestFileDiffs._get_http_options()
            request, metadata = self._interceptor.pre_list_pull_request_file_diffs(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecureSourceManagerRestTransport._BaseListPullRequestFileDiffs,
                    "_BaseListPullRequestFileDiffs__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.securesourcemanager_v1.SecureSourceManagerClient.ListPullRequestFileDiffs",
                    extra={
                        "serviceName": "google.cloud.securesourcemanager.v1.SecureSourceManager",
                        "rpcName": "ListPullRequestFileDiffs",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SecureSourceManagerRestTransport._ListPullRequestFileDiffs._get_response(
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
            resp = secure_source_manager.ListPullRequestFileDiffsResponse()
            pb_resp = secure_source_manager.ListPullRequestFileDiffsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_pull_request_file_diffs(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_pull_request_file_diffs_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        secure_source_manager.ListPullRequestFileDiffsResponse.to_json(
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
                    "Received response for google.cloud.securesourcemanager_v1.SecureSourceManagerClient.list_pull_request_file_diffs",
                    extra={
                        "serviceName": "google.cloud.securesourcemanager.v1.SecureSourceManager",
                        "rpcName": "ListPullRequestFileDiffs",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListPullRequests(
        _BaseSecureSourceManagerRestTransport._BaseListPullRequests,
        SecureSourceManagerRestStub,
    ):
        def __hash__(self):
            return hash("SecureSourceManagerRestTransport.ListPullRequests")

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
            request: secure_source_manager.ListPullRequestsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> secure_source_manager.ListPullRequestsResponse:
            r"""Call the list pull requests method over HTTP.

            Args:
                request (~.secure_source_manager.ListPullRequestsRequest):
                    The request object. ListPullRequestsRequest is the
                request to list pull requests.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.secure_source_manager.ListPullRequestsResponse:
                    ListPullRequestsResponse is the
                response to list pull requests.

            """

            http_options = _BaseSecureSourceManagerRestTransport._BaseListPullRequests._get_http_options()
            request, metadata = self._interceptor.pre_list_pull_requests(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecureSourceManagerRestTransport._BaseListPullRequests,
                    "_BaseListPullRequests__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.securesourcemanager_v1.SecureSourceManagerClient.ListPullRequests",
                    extra={
                        "serviceName": "google.cloud.securesourcemanager.v1.SecureSourceManager",
                        "rpcName": "ListPullRequests",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SecureSourceManagerRestTransport._ListPullRequests._get_response(
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
            resp = secure_source_manager.ListPullRequestsResponse()
            pb_resp = secure_source_manager.ListPullRequestsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_pull_requests(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_pull_requests_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        secure_source_manager.ListPullRequestsResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.securesourcemanager_v1.SecureSourceManagerClient.list_pull_requests",
                    extra={
                        "serviceName": "google.cloud.securesourcemanager.v1.SecureSourceManager",
                        "rpcName": "ListPullRequests",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListRepositories(
        _BaseSecureSourceManagerRestTransport._BaseListRepositories,
        SecureSourceManagerRestStub,
    ):
        def __hash__(self):
            return hash("SecureSourceManagerRestTransport.ListRepositories")

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
            request: secure_source_manager.ListRepositoriesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> secure_source_manager.ListRepositoriesResponse:
            r"""Call the list repositories method over HTTP.

            Args:
                request (~.secure_source_manager.ListRepositoriesRequest):
                    The request object. ListRepositoriesRequest is request to
                list repositories.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.secure_source_manager.ListRepositoriesResponse:

            """

            http_options = _BaseSecureSourceManagerRestTransport._BaseListRepositories._get_http_options()
            request, metadata = self._interceptor.pre_list_repositories(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecureSourceManagerRestTransport._BaseListRepositories,
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
                    f"Sending request for google.cloud.securesourcemanager_v1.SecureSourceManagerClient.ListRepositories",
                    extra={
                        "serviceName": "google.cloud.securesourcemanager.v1.SecureSourceManager",
                        "rpcName": "ListRepositories",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SecureSourceManagerRestTransport._ListRepositories._get_response(
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
            resp = secure_source_manager.ListRepositoriesResponse()
            pb_resp = secure_source_manager.ListRepositoriesResponse.pb(resp)

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
                    response_payload = (
                        secure_source_manager.ListRepositoriesResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.securesourcemanager_v1.SecureSourceManagerClient.list_repositories",
                    extra={
                        "serviceName": "google.cloud.securesourcemanager.v1.SecureSourceManager",
                        "rpcName": "ListRepositories",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _MergePullRequest(
        _BaseSecureSourceManagerRestTransport._BaseMergePullRequest,
        SecureSourceManagerRestStub,
    ):
        def __hash__(self):
            return hash("SecureSourceManagerRestTransport.MergePullRequest")

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
            request: secure_source_manager.MergePullRequestRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the merge pull request method over HTTP.

            Args:
                request (~.secure_source_manager.MergePullRequestRequest):
                    The request object. MergePullRequestRequest is the
                request to merge a pull request.
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

            http_options = _BaseSecureSourceManagerRestTransport._BaseMergePullRequest._get_http_options()
            request, metadata = self._interceptor.pre_merge_pull_request(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecureSourceManagerRestTransport._BaseMergePullRequest,
                    "_BaseMergePullRequest__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.securesourcemanager_v1.SecureSourceManagerClient.MergePullRequest",
                    extra={
                        "serviceName": "google.cloud.securesourcemanager.v1.SecureSourceManager",
                        "rpcName": "MergePullRequest",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SecureSourceManagerRestTransport._MergePullRequest._get_response(
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

            resp = self._interceptor.post_merge_pull_request(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_merge_pull_request_with_metadata(
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
                    "Received response for google.cloud.securesourcemanager_v1.SecureSourceManagerClient.merge_pull_request",
                    extra={
                        "serviceName": "google.cloud.securesourcemanager.v1.SecureSourceManager",
                        "rpcName": "MergePullRequest",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _OpenIssue(
        _BaseSecureSourceManagerRestTransport._BaseOpenIssue,
        SecureSourceManagerRestStub,
    ):
        def __hash__(self):
            return hash("SecureSourceManagerRestTransport.OpenIssue")

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
            request: secure_source_manager.OpenIssueRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the open issue method over HTTP.

            Args:
                request (~.secure_source_manager.OpenIssueRequest):
                    The request object. The request to open an issue.
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
                _BaseSecureSourceManagerRestTransport._BaseOpenIssue._get_http_options()
            )
            request, metadata = self._interceptor.pre_open_issue(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecureSourceManagerRestTransport._BaseOpenIssue,
                    "_BaseOpenIssue__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.securesourcemanager_v1.SecureSourceManagerClient.OpenIssue",
                    extra={
                        "serviceName": "google.cloud.securesourcemanager.v1.SecureSourceManager",
                        "rpcName": "OpenIssue",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SecureSourceManagerRestTransport._OpenIssue._get_response(
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

            resp = self._interceptor.post_open_issue(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_open_issue_with_metadata(
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
                    "Received response for google.cloud.securesourcemanager_v1.SecureSourceManagerClient.open_issue",
                    extra={
                        "serviceName": "google.cloud.securesourcemanager.v1.SecureSourceManager",
                        "rpcName": "OpenIssue",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _OpenPullRequest(
        _BaseSecureSourceManagerRestTransport._BaseOpenPullRequest,
        SecureSourceManagerRestStub,
    ):
        def __hash__(self):
            return hash("SecureSourceManagerRestTransport.OpenPullRequest")

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
            request: secure_source_manager.OpenPullRequestRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the open pull request method over HTTP.

            Args:
                request (~.secure_source_manager.OpenPullRequestRequest):
                    The request object. OpenPullRequestRequest is the request
                to open a pull request.
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

            http_options = _BaseSecureSourceManagerRestTransport._BaseOpenPullRequest._get_http_options()
            request, metadata = self._interceptor.pre_open_pull_request(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecureSourceManagerRestTransport._BaseOpenPullRequest,
                    "_BaseOpenPullRequest__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.securesourcemanager_v1.SecureSourceManagerClient.OpenPullRequest",
                    extra={
                        "serviceName": "google.cloud.securesourcemanager.v1.SecureSourceManager",
                        "rpcName": "OpenPullRequest",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SecureSourceManagerRestTransport._OpenPullRequest._get_response(
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

            resp = self._interceptor.post_open_pull_request(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_open_pull_request_with_metadata(
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
                    "Received response for google.cloud.securesourcemanager_v1.SecureSourceManagerClient.open_pull_request",
                    extra={
                        "serviceName": "google.cloud.securesourcemanager.v1.SecureSourceManager",
                        "rpcName": "OpenPullRequest",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ResolvePullRequestComments(
        _BaseSecureSourceManagerRestTransport._BaseResolvePullRequestComments,
        SecureSourceManagerRestStub,
    ):
        def __hash__(self):
            return hash("SecureSourceManagerRestTransport.ResolvePullRequestComments")

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
            request: secure_source_manager.ResolvePullRequestCommentsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the resolve pull request
            comments method over HTTP.

                Args:
                    request (~.secure_source_manager.ResolvePullRequestCommentsRequest):
                        The request object. The request to resolve multiple pull
                    request comments.
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

            http_options = _BaseSecureSourceManagerRestTransport._BaseResolvePullRequestComments._get_http_options()
            request, metadata = self._interceptor.pre_resolve_pull_request_comments(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecureSourceManagerRestTransport._BaseResolvePullRequestComments,
                    "_BaseResolvePullRequestComments__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.securesourcemanager_v1.SecureSourceManagerClient.ResolvePullRequestComments",
                    extra={
                        "serviceName": "google.cloud.securesourcemanager.v1.SecureSourceManager",
                        "rpcName": "ResolvePullRequestComments",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SecureSourceManagerRestTransport._ResolvePullRequestComments._get_response(
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

            resp = self._interceptor.post_resolve_pull_request_comments(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_resolve_pull_request_comments_with_metadata(
                    resp, response_metadata
                )
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
                    "Received response for google.cloud.securesourcemanager_v1.SecureSourceManagerClient.resolve_pull_request_comments",
                    extra={
                        "serviceName": "google.cloud.securesourcemanager.v1.SecureSourceManager",
                        "rpcName": "ResolvePullRequestComments",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _SetIamPolicyRepo(
        _BaseSecureSourceManagerRestTransport._BaseSetIamPolicyRepo,
        SecureSourceManagerRestStub,
    ):
        def __hash__(self):
            return hash("SecureSourceManagerRestTransport.SetIamPolicyRepo")

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
            r"""Call the set iam policy repo method over HTTP.

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

            http_options = _BaseSecureSourceManagerRestTransport._BaseSetIamPolicyRepo._get_http_options()
            request, metadata = self._interceptor.pre_set_iam_policy_repo(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecureSourceManagerRestTransport._BaseSetIamPolicyRepo,
                    "_BaseSetIamPolicyRepo__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.securesourcemanager_v1.SecureSourceManagerClient.SetIamPolicyRepo",
                    extra={
                        "serviceName": "google.cloud.securesourcemanager.v1.SecureSourceManager",
                        "rpcName": "SetIamPolicyRepo",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SecureSourceManagerRestTransport._SetIamPolicyRepo._get_response(
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

            resp = self._interceptor.post_set_iam_policy_repo(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_set_iam_policy_repo_with_metadata(
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
                    "Received response for google.cloud.securesourcemanager_v1.SecureSourceManagerClient.set_iam_policy_repo",
                    extra={
                        "serviceName": "google.cloud.securesourcemanager.v1.SecureSourceManager",
                        "rpcName": "SetIamPolicyRepo",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _TestIamPermissionsRepo(
        _BaseSecureSourceManagerRestTransport._BaseTestIamPermissionsRepo,
        SecureSourceManagerRestStub,
    ):
        def __hash__(self):
            return hash("SecureSourceManagerRestTransport.TestIamPermissionsRepo")

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
            r"""Call the test iam permissions repo method over HTTP.

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

            http_options = _BaseSecureSourceManagerRestTransport._BaseTestIamPermissionsRepo._get_http_options()
            request, metadata = self._interceptor.pre_test_iam_permissions_repo(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecureSourceManagerRestTransport._BaseTestIamPermissionsRepo,
                    "_BaseTestIamPermissionsRepo__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.securesourcemanager_v1.SecureSourceManagerClient.TestIamPermissionsRepo",
                    extra={
                        "serviceName": "google.cloud.securesourcemanager.v1.SecureSourceManager",
                        "rpcName": "TestIamPermissionsRepo",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                SecureSourceManagerRestTransport._TestIamPermissionsRepo._get_response(
                    self._host,
                    metadata,
                    query_params,
                    self._session,
                    timeout,
                    transcoded_request,
                    body,
                )
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = iam_policy_pb2.TestIamPermissionsResponse()
            pb_resp = resp

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_test_iam_permissions_repo(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_test_iam_permissions_repo_with_metadata(
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
                    "Received response for google.cloud.securesourcemanager_v1.SecureSourceManagerClient.test_iam_permissions_repo",
                    extra={
                        "serviceName": "google.cloud.securesourcemanager.v1.SecureSourceManager",
                        "rpcName": "TestIamPermissionsRepo",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UnresolvePullRequestComments(
        _BaseSecureSourceManagerRestTransport._BaseUnresolvePullRequestComments,
        SecureSourceManagerRestStub,
    ):
        def __hash__(self):
            return hash("SecureSourceManagerRestTransport.UnresolvePullRequestComments")

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
            request: secure_source_manager.UnresolvePullRequestCommentsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the unresolve pull request
            comments method over HTTP.

                Args:
                    request (~.secure_source_manager.UnresolvePullRequestCommentsRequest):
                        The request object. The request to unresolve multiple
                    pull request comments.
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

            http_options = _BaseSecureSourceManagerRestTransport._BaseUnresolvePullRequestComments._get_http_options()
            request, metadata = self._interceptor.pre_unresolve_pull_request_comments(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecureSourceManagerRestTransport._BaseUnresolvePullRequestComments,
                    "_BaseUnresolvePullRequestComments__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.securesourcemanager_v1.SecureSourceManagerClient.UnresolvePullRequestComments",
                    extra={
                        "serviceName": "google.cloud.securesourcemanager.v1.SecureSourceManager",
                        "rpcName": "UnresolvePullRequestComments",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SecureSourceManagerRestTransport._UnresolvePullRequestComments._get_response(
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

            resp = self._interceptor.post_unresolve_pull_request_comments(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_unresolve_pull_request_comments_with_metadata(
                    resp, response_metadata
                )
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
                    "Received response for google.cloud.securesourcemanager_v1.SecureSourceManagerClient.unresolve_pull_request_comments",
                    extra={
                        "serviceName": "google.cloud.securesourcemanager.v1.SecureSourceManager",
                        "rpcName": "UnresolvePullRequestComments",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateBranchRule(
        _BaseSecureSourceManagerRestTransport._BaseUpdateBranchRule,
        SecureSourceManagerRestStub,
    ):
        def __hash__(self):
            return hash("SecureSourceManagerRestTransport.UpdateBranchRule")

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
            request: secure_source_manager.UpdateBranchRuleRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update branch rule method over HTTP.

            Args:
                request (~.secure_source_manager.UpdateBranchRuleRequest):
                    The request object. UpdateBranchRuleRequest is the
                request to update a branchRule.
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

            http_options = _BaseSecureSourceManagerRestTransport._BaseUpdateBranchRule._get_http_options()
            request, metadata = self._interceptor.pre_update_branch_rule(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecureSourceManagerRestTransport._BaseUpdateBranchRule,
                    "_BaseUpdateBranchRule__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.securesourcemanager_v1.SecureSourceManagerClient.UpdateBranchRule",
                    extra={
                        "serviceName": "google.cloud.securesourcemanager.v1.SecureSourceManager",
                        "rpcName": "UpdateBranchRule",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SecureSourceManagerRestTransport._UpdateBranchRule._get_response(
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

            resp = self._interceptor.post_update_branch_rule(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_branch_rule_with_metadata(
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
                    "Received response for google.cloud.securesourcemanager_v1.SecureSourceManagerClient.update_branch_rule",
                    extra={
                        "serviceName": "google.cloud.securesourcemanager.v1.SecureSourceManager",
                        "rpcName": "UpdateBranchRule",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateHook(
        _BaseSecureSourceManagerRestTransport._BaseUpdateHook,
        SecureSourceManagerRestStub,
    ):
        def __hash__(self):
            return hash("SecureSourceManagerRestTransport.UpdateHook")

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
            request: secure_source_manager.UpdateHookRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update hook method over HTTP.

            Args:
                request (~.secure_source_manager.UpdateHookRequest):
                    The request object. UpdateHookRequest is the request to
                update a hook.
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

            http_options = _BaseSecureSourceManagerRestTransport._BaseUpdateHook._get_http_options()
            request, metadata = self._interceptor.pre_update_hook(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecureSourceManagerRestTransport._BaseUpdateHook,
                    "_BaseUpdateHook__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.securesourcemanager_v1.SecureSourceManagerClient.UpdateHook",
                    extra={
                        "serviceName": "google.cloud.securesourcemanager.v1.SecureSourceManager",
                        "rpcName": "UpdateHook",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SecureSourceManagerRestTransport._UpdateHook._get_response(
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

            resp = self._interceptor.post_update_hook(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_hook_with_metadata(
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
                    "Received response for google.cloud.securesourcemanager_v1.SecureSourceManagerClient.update_hook",
                    extra={
                        "serviceName": "google.cloud.securesourcemanager.v1.SecureSourceManager",
                        "rpcName": "UpdateHook",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateIssue(
        _BaseSecureSourceManagerRestTransport._BaseUpdateIssue,
        SecureSourceManagerRestStub,
    ):
        def __hash__(self):
            return hash("SecureSourceManagerRestTransport.UpdateIssue")

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
            request: secure_source_manager.UpdateIssueRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update issue method over HTTP.

            Args:
                request (~.secure_source_manager.UpdateIssueRequest):
                    The request object. The request to update an issue.
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

            http_options = _BaseSecureSourceManagerRestTransport._BaseUpdateIssue._get_http_options()
            request, metadata = self._interceptor.pre_update_issue(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecureSourceManagerRestTransport._BaseUpdateIssue,
                    "_BaseUpdateIssue__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.securesourcemanager_v1.SecureSourceManagerClient.UpdateIssue",
                    extra={
                        "serviceName": "google.cloud.securesourcemanager.v1.SecureSourceManager",
                        "rpcName": "UpdateIssue",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SecureSourceManagerRestTransport._UpdateIssue._get_response(
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

            resp = self._interceptor.post_update_issue(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_issue_with_metadata(
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
                    "Received response for google.cloud.securesourcemanager_v1.SecureSourceManagerClient.update_issue",
                    extra={
                        "serviceName": "google.cloud.securesourcemanager.v1.SecureSourceManager",
                        "rpcName": "UpdateIssue",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateIssueComment(
        _BaseSecureSourceManagerRestTransport._BaseUpdateIssueComment,
        SecureSourceManagerRestStub,
    ):
        def __hash__(self):
            return hash("SecureSourceManagerRestTransport.UpdateIssueComment")

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
            request: secure_source_manager.UpdateIssueCommentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update issue comment method over HTTP.

            Args:
                request (~.secure_source_manager.UpdateIssueCommentRequest):
                    The request object. The request to update an issue
                comment.
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

            http_options = _BaseSecureSourceManagerRestTransport._BaseUpdateIssueComment._get_http_options()
            request, metadata = self._interceptor.pre_update_issue_comment(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecureSourceManagerRestTransport._BaseUpdateIssueComment,
                    "_BaseUpdateIssueComment__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.securesourcemanager_v1.SecureSourceManagerClient.UpdateIssueComment",
                    extra={
                        "serviceName": "google.cloud.securesourcemanager.v1.SecureSourceManager",
                        "rpcName": "UpdateIssueComment",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                SecureSourceManagerRestTransport._UpdateIssueComment._get_response(
                    self._host,
                    metadata,
                    query_params,
                    self._session,
                    timeout,
                    transcoded_request,
                    body,
                )
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_issue_comment(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_issue_comment_with_metadata(
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
                    "Received response for google.cloud.securesourcemanager_v1.SecureSourceManagerClient.update_issue_comment",
                    extra={
                        "serviceName": "google.cloud.securesourcemanager.v1.SecureSourceManager",
                        "rpcName": "UpdateIssueComment",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdatePullRequest(
        _BaseSecureSourceManagerRestTransport._BaseUpdatePullRequest,
        SecureSourceManagerRestStub,
    ):
        def __hash__(self):
            return hash("SecureSourceManagerRestTransport.UpdatePullRequest")

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
            request: secure_source_manager.UpdatePullRequestRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update pull request method over HTTP.

            Args:
                request (~.secure_source_manager.UpdatePullRequestRequest):
                    The request object. UpdatePullRequestRequest is the
                request to update a pull request.
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

            http_options = _BaseSecureSourceManagerRestTransport._BaseUpdatePullRequest._get_http_options()
            request, metadata = self._interceptor.pre_update_pull_request(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecureSourceManagerRestTransport._BaseUpdatePullRequest,
                    "_BaseUpdatePullRequest__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.securesourcemanager_v1.SecureSourceManagerClient.UpdatePullRequest",
                    extra={
                        "serviceName": "google.cloud.securesourcemanager.v1.SecureSourceManager",
                        "rpcName": "UpdatePullRequest",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                SecureSourceManagerRestTransport._UpdatePullRequest._get_response(
                    self._host,
                    metadata,
                    query_params,
                    self._session,
                    timeout,
                    transcoded_request,
                    body,
                )
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_pull_request(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_pull_request_with_metadata(
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
                    "Received response for google.cloud.securesourcemanager_v1.SecureSourceManagerClient.update_pull_request",
                    extra={
                        "serviceName": "google.cloud.securesourcemanager.v1.SecureSourceManager",
                        "rpcName": "UpdatePullRequest",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdatePullRequestComment(
        _BaseSecureSourceManagerRestTransport._BaseUpdatePullRequestComment,
        SecureSourceManagerRestStub,
    ):
        def __hash__(self):
            return hash("SecureSourceManagerRestTransport.UpdatePullRequestComment")

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
            request: secure_source_manager.UpdatePullRequestCommentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update pull request
            comment method over HTTP.

                Args:
                    request (~.secure_source_manager.UpdatePullRequestCommentRequest):
                        The request object. The request to update a pull request
                    comment.
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

            http_options = _BaseSecureSourceManagerRestTransport._BaseUpdatePullRequestComment._get_http_options()
            request, metadata = self._interceptor.pre_update_pull_request_comment(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecureSourceManagerRestTransport._BaseUpdatePullRequestComment,
                    "_BaseUpdatePullRequestComment__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.securesourcemanager_v1.SecureSourceManagerClient.UpdatePullRequestComment",
                    extra={
                        "serviceName": "google.cloud.securesourcemanager.v1.SecureSourceManager",
                        "rpcName": "UpdatePullRequestComment",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SecureSourceManagerRestTransport._UpdatePullRequestComment._get_response(
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

            resp = self._interceptor.post_update_pull_request_comment(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_pull_request_comment_with_metadata(
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
                    "Received response for google.cloud.securesourcemanager_v1.SecureSourceManagerClient.update_pull_request_comment",
                    extra={
                        "serviceName": "google.cloud.securesourcemanager.v1.SecureSourceManager",
                        "rpcName": "UpdatePullRequestComment",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateRepository(
        _BaseSecureSourceManagerRestTransport._BaseUpdateRepository,
        SecureSourceManagerRestStub,
    ):
        def __hash__(self):
            return hash("SecureSourceManagerRestTransport.UpdateRepository")

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
            request: secure_source_manager.UpdateRepositoryRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update repository method over HTTP.

            Args:
                request (~.secure_source_manager.UpdateRepositoryRequest):
                    The request object. UpdateRepositoryRequest is the
                request to update a repository.
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

            http_options = _BaseSecureSourceManagerRestTransport._BaseUpdateRepository._get_http_options()
            request, metadata = self._interceptor.pre_update_repository(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecureSourceManagerRestTransport._BaseUpdateRepository,
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
                    f"Sending request for google.cloud.securesourcemanager_v1.SecureSourceManagerClient.UpdateRepository",
                    extra={
                        "serviceName": "google.cloud.securesourcemanager.v1.SecureSourceManager",
                        "rpcName": "UpdateRepository",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SecureSourceManagerRestTransport._UpdateRepository._get_response(
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

            resp = self._interceptor.post_update_repository(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_repository_with_metadata(
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
                    "Received response for google.cloud.securesourcemanager_v1.SecureSourceManagerClient.update_repository",
                    extra={
                        "serviceName": "google.cloud.securesourcemanager.v1.SecureSourceManager",
                        "rpcName": "UpdateRepository",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def batch_create_pull_request_comments(
        self,
    ) -> Callable[
        [secure_source_manager.BatchCreatePullRequestCommentsRequest],
        operations_pb2.Operation,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchCreatePullRequestComments(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def close_issue(
        self,
    ) -> Callable[[secure_source_manager.CloseIssueRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CloseIssue(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def close_pull_request(
        self,
    ) -> Callable[
        [secure_source_manager.ClosePullRequestRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ClosePullRequest(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_branch_rule(
        self,
    ) -> Callable[
        [secure_source_manager.CreateBranchRuleRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateBranchRule(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_hook(
        self,
    ) -> Callable[[secure_source_manager.CreateHookRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateHook(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_instance(
        self,
    ) -> Callable[
        [secure_source_manager.CreateInstanceRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateInstance(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_issue(
        self,
    ) -> Callable[[secure_source_manager.CreateIssueRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateIssue(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_issue_comment(
        self,
    ) -> Callable[
        [secure_source_manager.CreateIssueCommentRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateIssueComment(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_pull_request(
        self,
    ) -> Callable[
        [secure_source_manager.CreatePullRequestRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreatePullRequest(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_pull_request_comment(
        self,
    ) -> Callable[
        [secure_source_manager.CreatePullRequestCommentRequest],
        operations_pb2.Operation,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreatePullRequestComment(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def create_repository(
        self,
    ) -> Callable[
        [secure_source_manager.CreateRepositoryRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateRepository(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_branch_rule(
        self,
    ) -> Callable[
        [secure_source_manager.DeleteBranchRuleRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteBranchRule(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_hook(
        self,
    ) -> Callable[[secure_source_manager.DeleteHookRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteHook(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_instance(
        self,
    ) -> Callable[
        [secure_source_manager.DeleteInstanceRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteInstance(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_issue(
        self,
    ) -> Callable[[secure_source_manager.DeleteIssueRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteIssue(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_issue_comment(
        self,
    ) -> Callable[
        [secure_source_manager.DeleteIssueCommentRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteIssueComment(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_pull_request_comment(
        self,
    ) -> Callable[
        [secure_source_manager.DeletePullRequestCommentRequest],
        operations_pb2.Operation,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeletePullRequestComment(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def delete_repository(
        self,
    ) -> Callable[
        [secure_source_manager.DeleteRepositoryRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteRepository(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def fetch_blob(
        self,
    ) -> Callable[
        [secure_source_manager.FetchBlobRequest],
        secure_source_manager.FetchBlobResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._FetchBlob(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def fetch_refs(
        self,
    ) -> Callable[
        [secure_source_manager.FetchRefsRequest],
        secure_source_manager.FetchRefsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._FetchRefs(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def fetch_tree(
        self,
    ) -> Callable[
        [secure_source_manager.FetchTreeRequest],
        secure_source_manager.FetchTreeResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._FetchTree(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_branch_rule(
        self,
    ) -> Callable[
        [secure_source_manager.GetBranchRuleRequest], secure_source_manager.BranchRule
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetBranchRule(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_hook(
        self,
    ) -> Callable[[secure_source_manager.GetHookRequest], secure_source_manager.Hook]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetHook(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_iam_policy_repo(
        self,
    ) -> Callable[[iam_policy_pb2.GetIamPolicyRequest], policy_pb2.Policy]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetIamPolicyRepo(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_instance(
        self,
    ) -> Callable[
        [secure_source_manager.GetInstanceRequest], secure_source_manager.Instance
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetInstance(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_issue(
        self,
    ) -> Callable[[secure_source_manager.GetIssueRequest], secure_source_manager.Issue]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetIssue(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_issue_comment(
        self,
    ) -> Callable[
        [secure_source_manager.GetIssueCommentRequest],
        secure_source_manager.IssueComment,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetIssueComment(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_pull_request(
        self,
    ) -> Callable[
        [secure_source_manager.GetPullRequestRequest], secure_source_manager.PullRequest
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetPullRequest(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_pull_request_comment(
        self,
    ) -> Callable[
        [secure_source_manager.GetPullRequestCommentRequest],
        secure_source_manager.PullRequestComment,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetPullRequestComment(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_repository(
        self,
    ) -> Callable[
        [secure_source_manager.GetRepositoryRequest], secure_source_manager.Repository
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetRepository(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_branch_rules(
        self,
    ) -> Callable[
        [secure_source_manager.ListBranchRulesRequest],
        secure_source_manager.ListBranchRulesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListBranchRules(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_hooks(
        self,
    ) -> Callable[
        [secure_source_manager.ListHooksRequest],
        secure_source_manager.ListHooksResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListHooks(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_instances(
        self,
    ) -> Callable[
        [secure_source_manager.ListInstancesRequest],
        secure_source_manager.ListInstancesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListInstances(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_issue_comments(
        self,
    ) -> Callable[
        [secure_source_manager.ListIssueCommentsRequest],
        secure_source_manager.ListIssueCommentsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListIssueComments(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_issues(
        self,
    ) -> Callable[
        [secure_source_manager.ListIssuesRequest],
        secure_source_manager.ListIssuesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListIssues(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_pull_request_comments(
        self,
    ) -> Callable[
        [secure_source_manager.ListPullRequestCommentsRequest],
        secure_source_manager.ListPullRequestCommentsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListPullRequestComments(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def list_pull_request_file_diffs(
        self,
    ) -> Callable[
        [secure_source_manager.ListPullRequestFileDiffsRequest],
        secure_source_manager.ListPullRequestFileDiffsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListPullRequestFileDiffs(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def list_pull_requests(
        self,
    ) -> Callable[
        [secure_source_manager.ListPullRequestsRequest],
        secure_source_manager.ListPullRequestsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListPullRequests(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_repositories(
        self,
    ) -> Callable[
        [secure_source_manager.ListRepositoriesRequest],
        secure_source_manager.ListRepositoriesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListRepositories(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def merge_pull_request(
        self,
    ) -> Callable[
        [secure_source_manager.MergePullRequestRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._MergePullRequest(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def open_issue(
        self,
    ) -> Callable[[secure_source_manager.OpenIssueRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._OpenIssue(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def open_pull_request(
        self,
    ) -> Callable[
        [secure_source_manager.OpenPullRequestRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._OpenPullRequest(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def resolve_pull_request_comments(
        self,
    ) -> Callable[
        [secure_source_manager.ResolvePullRequestCommentsRequest],
        operations_pb2.Operation,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ResolvePullRequestComments(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def set_iam_policy_repo(
        self,
    ) -> Callable[[iam_policy_pb2.SetIamPolicyRequest], policy_pb2.Policy]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._SetIamPolicyRepo(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def test_iam_permissions_repo(
        self,
    ) -> Callable[
        [iam_policy_pb2.TestIamPermissionsRequest],
        iam_policy_pb2.TestIamPermissionsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._TestIamPermissionsRepo(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def unresolve_pull_request_comments(
        self,
    ) -> Callable[
        [secure_source_manager.UnresolvePullRequestCommentsRequest],
        operations_pb2.Operation,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UnresolvePullRequestComments(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def update_branch_rule(
        self,
    ) -> Callable[
        [secure_source_manager.UpdateBranchRuleRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateBranchRule(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_hook(
        self,
    ) -> Callable[[secure_source_manager.UpdateHookRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateHook(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_issue(
        self,
    ) -> Callable[[secure_source_manager.UpdateIssueRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateIssue(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_issue_comment(
        self,
    ) -> Callable[
        [secure_source_manager.UpdateIssueCommentRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateIssueComment(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_pull_request(
        self,
    ) -> Callable[
        [secure_source_manager.UpdatePullRequestRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdatePullRequest(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_pull_request_comment(
        self,
    ) -> Callable[
        [secure_source_manager.UpdatePullRequestCommentRequest],
        operations_pb2.Operation,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdatePullRequestComment(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def update_repository(
        self,
    ) -> Callable[
        [secure_source_manager.UpdateRepositoryRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateRepository(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_location(self):
        return self._GetLocation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetLocation(
        _BaseSecureSourceManagerRestTransport._BaseGetLocation,
        SecureSourceManagerRestStub,
    ):
        def __hash__(self):
            return hash("SecureSourceManagerRestTransport.GetLocation")

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

            http_options = _BaseSecureSourceManagerRestTransport._BaseGetLocation._get_http_options()
            request, metadata = self._interceptor.pre_get_location(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecureSourceManagerRestTransport._BaseGetLocation,
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
                    f"Sending request for google.cloud.securesourcemanager_v1.SecureSourceManagerClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.securesourcemanager.v1.SecureSourceManager",
                        "rpcName": "GetLocation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SecureSourceManagerRestTransport._GetLocation._get_response(
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
                    "Received response for google.cloud.securesourcemanager_v1.SecureSourceManagerAsyncClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.securesourcemanager.v1.SecureSourceManager",
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
        _BaseSecureSourceManagerRestTransport._BaseListLocations,
        SecureSourceManagerRestStub,
    ):
        def __hash__(self):
            return hash("SecureSourceManagerRestTransport.ListLocations")

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

            http_options = _BaseSecureSourceManagerRestTransport._BaseListLocations._get_http_options()
            request, metadata = self._interceptor.pre_list_locations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecureSourceManagerRestTransport._BaseListLocations,
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
                    f"Sending request for google.cloud.securesourcemanager_v1.SecureSourceManagerClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.securesourcemanager.v1.SecureSourceManager",
                        "rpcName": "ListLocations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SecureSourceManagerRestTransport._ListLocations._get_response(
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
                    "Received response for google.cloud.securesourcemanager_v1.SecureSourceManagerAsyncClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.securesourcemanager.v1.SecureSourceManager",
                        "rpcName": "ListLocations",
                        "httpResponse": http_response,
                        "metadata": http_response["headers"],
                    },
                )
            return resp

    @property
    def get_iam_policy(self):
        return self._GetIamPolicy(self._session, self._host, self._interceptor)  # type: ignore

    class _GetIamPolicy(
        _BaseSecureSourceManagerRestTransport._BaseGetIamPolicy,
        SecureSourceManagerRestStub,
    ):
        def __hash__(self):
            return hash("SecureSourceManagerRestTransport.GetIamPolicy")

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
                request (iam_policy_pb2.GetIamPolicyRequest):
                    The request object for GetIamPolicy method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                policy_pb2.Policy: Response from GetIamPolicy method.
            """

            http_options = _BaseSecureSourceManagerRestTransport._BaseGetIamPolicy._get_http_options()
            request, metadata = self._interceptor.pre_get_iam_policy(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecureSourceManagerRestTransport._BaseGetIamPolicy,
                    "_BaseGetIamPolicy__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.securesourcemanager_v1.SecureSourceManagerClient.GetIamPolicy",
                    extra={
                        "serviceName": "google.cloud.securesourcemanager.v1.SecureSourceManager",
                        "rpcName": "GetIamPolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SecureSourceManagerRestTransport._GetIamPolicy._get_response(
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
            resp = policy_pb2.Policy()
            resp = json_format.Parse(content, resp)
            resp = self._interceptor.post_get_iam_policy(resp)
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
                    "Received response for google.cloud.securesourcemanager_v1.SecureSourceManagerAsyncClient.GetIamPolicy",
                    extra={
                        "serviceName": "google.cloud.securesourcemanager.v1.SecureSourceManager",
                        "rpcName": "GetIamPolicy",
                        "httpResponse": http_response,
                        "metadata": http_response["headers"],
                    },
                )
            return resp

    @property
    def set_iam_policy(self):
        return self._SetIamPolicy(self._session, self._host, self._interceptor)  # type: ignore

    class _SetIamPolicy(
        _BaseSecureSourceManagerRestTransport._BaseSetIamPolicy,
        SecureSourceManagerRestStub,
    ):
        def __hash__(self):
            return hash("SecureSourceManagerRestTransport.SetIamPolicy")

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
                request (iam_policy_pb2.SetIamPolicyRequest):
                    The request object for SetIamPolicy method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                policy_pb2.Policy: Response from SetIamPolicy method.
            """

            http_options = _BaseSecureSourceManagerRestTransport._BaseSetIamPolicy._get_http_options()
            request, metadata = self._interceptor.pre_set_iam_policy(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecureSourceManagerRestTransport._BaseSetIamPolicy,
                    "_BaseSetIamPolicy__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.securesourcemanager_v1.SecureSourceManagerClient.SetIamPolicy",
                    extra={
                        "serviceName": "google.cloud.securesourcemanager.v1.SecureSourceManager",
                        "rpcName": "SetIamPolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SecureSourceManagerRestTransport._SetIamPolicy._get_response(
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

            content = response.content.decode("utf-8")
            resp = policy_pb2.Policy()
            resp = json_format.Parse(content, resp)
            resp = self._interceptor.post_set_iam_policy(resp)
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
                    "Received response for google.cloud.securesourcemanager_v1.SecureSourceManagerAsyncClient.SetIamPolicy",
                    extra={
                        "serviceName": "google.cloud.securesourcemanager.v1.SecureSourceManager",
                        "rpcName": "SetIamPolicy",
                        "httpResponse": http_response,
                        "metadata": http_response["headers"],
                    },
                )
            return resp

    @property
    def test_iam_permissions(self):
        return self._TestIamPermissions(self._session, self._host, self._interceptor)  # type: ignore

    class _TestIamPermissions(
        _BaseSecureSourceManagerRestTransport._BaseTestIamPermissions,
        SecureSourceManagerRestStub,
    ):
        def __hash__(self):
            return hash("SecureSourceManagerRestTransport.TestIamPermissions")

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
                request (iam_policy_pb2.TestIamPermissionsRequest):
                    The request object for TestIamPermissions method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                iam_policy_pb2.TestIamPermissionsResponse: Response from TestIamPermissions method.
            """

            http_options = _BaseSecureSourceManagerRestTransport._BaseTestIamPermissions._get_http_options()
            request, metadata = self._interceptor.pre_test_iam_permissions(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecureSourceManagerRestTransport._BaseTestIamPermissions,
                    "_BaseTestIamPermissions__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.securesourcemanager_v1.SecureSourceManagerClient.TestIamPermissions",
                    extra={
                        "serviceName": "google.cloud.securesourcemanager.v1.SecureSourceManager",
                        "rpcName": "TestIamPermissions",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                SecureSourceManagerRestTransport._TestIamPermissions._get_response(
                    self._host,
                    metadata,
                    query_params,
                    self._session,
                    timeout,
                    transcoded_request,
                    body,
                )
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            content = response.content.decode("utf-8")
            resp = iam_policy_pb2.TestIamPermissionsResponse()
            resp = json_format.Parse(content, resp)
            resp = self._interceptor.post_test_iam_permissions(resp)
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
                    "Received response for google.cloud.securesourcemanager_v1.SecureSourceManagerAsyncClient.TestIamPermissions",
                    extra={
                        "serviceName": "google.cloud.securesourcemanager.v1.SecureSourceManager",
                        "rpcName": "TestIamPermissions",
                        "httpResponse": http_response,
                        "metadata": http_response["headers"],
                    },
                )
            return resp

    @property
    def cancel_operation(self):
        return self._CancelOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _CancelOperation(
        _BaseSecureSourceManagerRestTransport._BaseCancelOperation,
        SecureSourceManagerRestStub,
    ):
        def __hash__(self):
            return hash("SecureSourceManagerRestTransport.CancelOperation")

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

            http_options = _BaseSecureSourceManagerRestTransport._BaseCancelOperation._get_http_options()
            request, metadata = self._interceptor.pre_cancel_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecureSourceManagerRestTransport._BaseCancelOperation,
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
                    f"Sending request for google.cloud.securesourcemanager_v1.SecureSourceManagerClient.CancelOperation",
                    extra={
                        "serviceName": "google.cloud.securesourcemanager.v1.SecureSourceManager",
                        "rpcName": "CancelOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SecureSourceManagerRestTransport._CancelOperation._get_response(
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
        _BaseSecureSourceManagerRestTransport._BaseDeleteOperation,
        SecureSourceManagerRestStub,
    ):
        def __hash__(self):
            return hash("SecureSourceManagerRestTransport.DeleteOperation")

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

            http_options = _BaseSecureSourceManagerRestTransport._BaseDeleteOperation._get_http_options()
            request, metadata = self._interceptor.pre_delete_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecureSourceManagerRestTransport._BaseDeleteOperation,
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
                    f"Sending request for google.cloud.securesourcemanager_v1.SecureSourceManagerClient.DeleteOperation",
                    extra={
                        "serviceName": "google.cloud.securesourcemanager.v1.SecureSourceManager",
                        "rpcName": "DeleteOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SecureSourceManagerRestTransport._DeleteOperation._get_response(
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

    class _GetOperation(
        _BaseSecureSourceManagerRestTransport._BaseGetOperation,
        SecureSourceManagerRestStub,
    ):
        def __hash__(self):
            return hash("SecureSourceManagerRestTransport.GetOperation")

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

            http_options = _BaseSecureSourceManagerRestTransport._BaseGetOperation._get_http_options()
            request, metadata = self._interceptor.pre_get_operation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecureSourceManagerRestTransport._BaseGetOperation,
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
                    f"Sending request for google.cloud.securesourcemanager_v1.SecureSourceManagerClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.securesourcemanager.v1.SecureSourceManager",
                        "rpcName": "GetOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SecureSourceManagerRestTransport._GetOperation._get_response(
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
                    "Received response for google.cloud.securesourcemanager_v1.SecureSourceManagerAsyncClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.securesourcemanager.v1.SecureSourceManager",
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
        _BaseSecureSourceManagerRestTransport._BaseListOperations,
        SecureSourceManagerRestStub,
    ):
        def __hash__(self):
            return hash("SecureSourceManagerRestTransport.ListOperations")

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

            http_options = _BaseSecureSourceManagerRestTransport._BaseListOperations._get_http_options()
            request, metadata = self._interceptor.pre_list_operations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecureSourceManagerRestTransport._BaseListOperations,
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
                    f"Sending request for google.cloud.securesourcemanager_v1.SecureSourceManagerClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.securesourcemanager.v1.SecureSourceManager",
                        "rpcName": "ListOperations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SecureSourceManagerRestTransport._ListOperations._get_response(
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
                    "Received response for google.cloud.securesourcemanager_v1.SecureSourceManagerAsyncClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.securesourcemanager.v1.SecureSourceManager",
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


__all__ = ("SecureSourceManagerRestTransport",)
