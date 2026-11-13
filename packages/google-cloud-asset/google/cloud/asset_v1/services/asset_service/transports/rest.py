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

import google.protobuf
import google.protobuf.empty_pb2 as empty_pb2  # type: ignore
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1, operations_v1, rest_helpers, rest_streaming
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.auth.transport.requests import AuthorizedSession  # type: ignore
from google.longrunning import operations_pb2  # type: ignore
from google.protobuf import json_format
from requests import __version__ as requests_version

from google.cloud.asset_v1._compat import transcode_request
from google.cloud.asset_v1.types import asset_service

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseAssetServiceRestTransport

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


class AssetServiceRestInterceptor:
    """Interceptor for AssetService.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the AssetServiceRestTransport.

    .. code-block:: python
        class MyCustomAssetServiceInterceptor(AssetServiceRestInterceptor):
            def pre_analyze_iam_policy(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_analyze_iam_policy(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_analyze_iam_policy_longrunning(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_analyze_iam_policy_longrunning(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_analyze_move(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_analyze_move(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_analyze_org_policies(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_analyze_org_policies(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_analyze_org_policy_governed_assets(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_analyze_org_policy_governed_assets(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_analyze_org_policy_governed_containers(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_analyze_org_policy_governed_containers(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_batch_get_assets_history(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_get_assets_history(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_batch_get_effective_iam_policies(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_get_effective_iam_policies(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_feed(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_feed(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_saved_query(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_saved_query(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_feed(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_delete_saved_query(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_export_assets(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_export_assets(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_feed(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_feed(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_saved_query(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_saved_query(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_assets(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_assets(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_feeds(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_feeds(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_saved_queries(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_saved_queries(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_query_assets(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_query_assets(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_search_all_iam_policies(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_search_all_iam_policies(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_search_all_resources(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_search_all_resources(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_feed(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_feed(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_saved_query(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_saved_query(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = AssetServiceRestTransport(interceptor=MyCustomAssetServiceInterceptor())
        client = AssetServiceClient(transport=transport)


    """

    def pre_analyze_iam_policy(
        self,
        request: asset_service.AnalyzeIamPolicyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        asset_service.AnalyzeIamPolicyRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for analyze_iam_policy

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AssetService server.
        """
        return request, metadata

    def post_analyze_iam_policy(
        self, response: asset_service.AnalyzeIamPolicyResponse
    ) -> asset_service.AnalyzeIamPolicyResponse:
        """Post-rpc interceptor for analyze_iam_policy

        DEPRECATED. Please use the `post_analyze_iam_policy_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AssetService server but before
        it is returned to user code. This `post_analyze_iam_policy` interceptor runs
        before the `post_analyze_iam_policy_with_metadata` interceptor.
        """
        return response

    def post_analyze_iam_policy_with_metadata(
        self,
        response: asset_service.AnalyzeIamPolicyResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        asset_service.AnalyzeIamPolicyResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for analyze_iam_policy

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AssetService server but before it is returned to user code.

        We recommend only using this `post_analyze_iam_policy_with_metadata`
        interceptor in new development instead of the `post_analyze_iam_policy` interceptor.
        When both interceptors are used, this `post_analyze_iam_policy_with_metadata` interceptor runs after the
        `post_analyze_iam_policy` interceptor. The (possibly modified) response returned by
        `post_analyze_iam_policy` will be passed to
        `post_analyze_iam_policy_with_metadata`.
        """
        return response, metadata

    def pre_analyze_iam_policy_longrunning(
        self,
        request: asset_service.AnalyzeIamPolicyLongrunningRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        asset_service.AnalyzeIamPolicyLongrunningRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for analyze_iam_policy_longrunning

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AssetService server.
        """
        return request, metadata

    def post_analyze_iam_policy_longrunning(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for analyze_iam_policy_longrunning

        DEPRECATED. Please use the `post_analyze_iam_policy_longrunning_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AssetService server but before
        it is returned to user code. This `post_analyze_iam_policy_longrunning` interceptor runs
        before the `post_analyze_iam_policy_longrunning_with_metadata` interceptor.
        """
        return response

    def post_analyze_iam_policy_longrunning_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for analyze_iam_policy_longrunning

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AssetService server but before it is returned to user code.

        We recommend only using this `post_analyze_iam_policy_longrunning_with_metadata`
        interceptor in new development instead of the `post_analyze_iam_policy_longrunning` interceptor.
        When both interceptors are used, this `post_analyze_iam_policy_longrunning_with_metadata` interceptor runs after the
        `post_analyze_iam_policy_longrunning` interceptor. The (possibly modified) response returned by
        `post_analyze_iam_policy_longrunning` will be passed to
        `post_analyze_iam_policy_longrunning_with_metadata`.
        """
        return response, metadata

    def pre_analyze_move(
        self,
        request: asset_service.AnalyzeMoveRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        asset_service.AnalyzeMoveRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for analyze_move

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AssetService server.
        """
        return request, metadata

    def post_analyze_move(
        self, response: asset_service.AnalyzeMoveResponse
    ) -> asset_service.AnalyzeMoveResponse:
        """Post-rpc interceptor for analyze_move

        DEPRECATED. Please use the `post_analyze_move_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AssetService server but before
        it is returned to user code. This `post_analyze_move` interceptor runs
        before the `post_analyze_move_with_metadata` interceptor.
        """
        return response

    def post_analyze_move_with_metadata(
        self,
        response: asset_service.AnalyzeMoveResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        asset_service.AnalyzeMoveResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for analyze_move

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AssetService server but before it is returned to user code.

        We recommend only using this `post_analyze_move_with_metadata`
        interceptor in new development instead of the `post_analyze_move` interceptor.
        When both interceptors are used, this `post_analyze_move_with_metadata` interceptor runs after the
        `post_analyze_move` interceptor. The (possibly modified) response returned by
        `post_analyze_move` will be passed to
        `post_analyze_move_with_metadata`.
        """
        return response, metadata

    def pre_analyze_org_policies(
        self,
        request: asset_service.AnalyzeOrgPoliciesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        asset_service.AnalyzeOrgPoliciesRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for analyze_org_policies

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AssetService server.
        """
        return request, metadata

    def post_analyze_org_policies(
        self, response: asset_service.AnalyzeOrgPoliciesResponse
    ) -> asset_service.AnalyzeOrgPoliciesResponse:
        """Post-rpc interceptor for analyze_org_policies

        DEPRECATED. Please use the `post_analyze_org_policies_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AssetService server but before
        it is returned to user code. This `post_analyze_org_policies` interceptor runs
        before the `post_analyze_org_policies_with_metadata` interceptor.
        """
        return response

    def post_analyze_org_policies_with_metadata(
        self,
        response: asset_service.AnalyzeOrgPoliciesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        asset_service.AnalyzeOrgPoliciesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for analyze_org_policies

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AssetService server but before it is returned to user code.

        We recommend only using this `post_analyze_org_policies_with_metadata`
        interceptor in new development instead of the `post_analyze_org_policies` interceptor.
        When both interceptors are used, this `post_analyze_org_policies_with_metadata` interceptor runs after the
        `post_analyze_org_policies` interceptor. The (possibly modified) response returned by
        `post_analyze_org_policies` will be passed to
        `post_analyze_org_policies_with_metadata`.
        """
        return response, metadata

    def pre_analyze_org_policy_governed_assets(
        self,
        request: asset_service.AnalyzeOrgPolicyGovernedAssetsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        asset_service.AnalyzeOrgPolicyGovernedAssetsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for analyze_org_policy_governed_assets

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AssetService server.
        """
        return request, metadata

    def post_analyze_org_policy_governed_assets(
        self, response: asset_service.AnalyzeOrgPolicyGovernedAssetsResponse
    ) -> asset_service.AnalyzeOrgPolicyGovernedAssetsResponse:
        """Post-rpc interceptor for analyze_org_policy_governed_assets

        DEPRECATED. Please use the `post_analyze_org_policy_governed_assets_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AssetService server but before
        it is returned to user code. This `post_analyze_org_policy_governed_assets` interceptor runs
        before the `post_analyze_org_policy_governed_assets_with_metadata` interceptor.
        """
        return response

    def post_analyze_org_policy_governed_assets_with_metadata(
        self,
        response: asset_service.AnalyzeOrgPolicyGovernedAssetsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        asset_service.AnalyzeOrgPolicyGovernedAssetsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for analyze_org_policy_governed_assets

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AssetService server but before it is returned to user code.

        We recommend only using this `post_analyze_org_policy_governed_assets_with_metadata`
        interceptor in new development instead of the `post_analyze_org_policy_governed_assets` interceptor.
        When both interceptors are used, this `post_analyze_org_policy_governed_assets_with_metadata` interceptor runs after the
        `post_analyze_org_policy_governed_assets` interceptor. The (possibly modified) response returned by
        `post_analyze_org_policy_governed_assets` will be passed to
        `post_analyze_org_policy_governed_assets_with_metadata`.
        """
        return response, metadata

    def pre_analyze_org_policy_governed_containers(
        self,
        request: asset_service.AnalyzeOrgPolicyGovernedContainersRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        asset_service.AnalyzeOrgPolicyGovernedContainersRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for analyze_org_policy_governed_containers

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AssetService server.
        """
        return request, metadata

    def post_analyze_org_policy_governed_containers(
        self, response: asset_service.AnalyzeOrgPolicyGovernedContainersResponse
    ) -> asset_service.AnalyzeOrgPolicyGovernedContainersResponse:
        """Post-rpc interceptor for analyze_org_policy_governed_containers

        DEPRECATED. Please use the `post_analyze_org_policy_governed_containers_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AssetService server but before
        it is returned to user code. This `post_analyze_org_policy_governed_containers` interceptor runs
        before the `post_analyze_org_policy_governed_containers_with_metadata` interceptor.
        """
        return response

    def post_analyze_org_policy_governed_containers_with_metadata(
        self,
        response: asset_service.AnalyzeOrgPolicyGovernedContainersResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        asset_service.AnalyzeOrgPolicyGovernedContainersResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for analyze_org_policy_governed_containers

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AssetService server but before it is returned to user code.

        We recommend only using this `post_analyze_org_policy_governed_containers_with_metadata`
        interceptor in new development instead of the `post_analyze_org_policy_governed_containers` interceptor.
        When both interceptors are used, this `post_analyze_org_policy_governed_containers_with_metadata` interceptor runs after the
        `post_analyze_org_policy_governed_containers` interceptor. The (possibly modified) response returned by
        `post_analyze_org_policy_governed_containers` will be passed to
        `post_analyze_org_policy_governed_containers_with_metadata`.
        """
        return response, metadata

    def pre_batch_get_assets_history(
        self,
        request: asset_service.BatchGetAssetsHistoryRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        asset_service.BatchGetAssetsHistoryRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_get_assets_history

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AssetService server.
        """
        return request, metadata

    def post_batch_get_assets_history(
        self, response: asset_service.BatchGetAssetsHistoryResponse
    ) -> asset_service.BatchGetAssetsHistoryResponse:
        """Post-rpc interceptor for batch_get_assets_history

        DEPRECATED. Please use the `post_batch_get_assets_history_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AssetService server but before
        it is returned to user code. This `post_batch_get_assets_history` interceptor runs
        before the `post_batch_get_assets_history_with_metadata` interceptor.
        """
        return response

    def post_batch_get_assets_history_with_metadata(
        self,
        response: asset_service.BatchGetAssetsHistoryResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        asset_service.BatchGetAssetsHistoryResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_get_assets_history

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AssetService server but before it is returned to user code.

        We recommend only using this `post_batch_get_assets_history_with_metadata`
        interceptor in new development instead of the `post_batch_get_assets_history` interceptor.
        When both interceptors are used, this `post_batch_get_assets_history_with_metadata` interceptor runs after the
        `post_batch_get_assets_history` interceptor. The (possibly modified) response returned by
        `post_batch_get_assets_history` will be passed to
        `post_batch_get_assets_history_with_metadata`.
        """
        return response, metadata

    def pre_batch_get_effective_iam_policies(
        self,
        request: asset_service.BatchGetEffectiveIamPoliciesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        asset_service.BatchGetEffectiveIamPoliciesRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_get_effective_iam_policies

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AssetService server.
        """
        return request, metadata

    def post_batch_get_effective_iam_policies(
        self, response: asset_service.BatchGetEffectiveIamPoliciesResponse
    ) -> asset_service.BatchGetEffectiveIamPoliciesResponse:
        """Post-rpc interceptor for batch_get_effective_iam_policies

        DEPRECATED. Please use the `post_batch_get_effective_iam_policies_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AssetService server but before
        it is returned to user code. This `post_batch_get_effective_iam_policies` interceptor runs
        before the `post_batch_get_effective_iam_policies_with_metadata` interceptor.
        """
        return response

    def post_batch_get_effective_iam_policies_with_metadata(
        self,
        response: asset_service.BatchGetEffectiveIamPoliciesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        asset_service.BatchGetEffectiveIamPoliciesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_get_effective_iam_policies

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AssetService server but before it is returned to user code.

        We recommend only using this `post_batch_get_effective_iam_policies_with_metadata`
        interceptor in new development instead of the `post_batch_get_effective_iam_policies` interceptor.
        When both interceptors are used, this `post_batch_get_effective_iam_policies_with_metadata` interceptor runs after the
        `post_batch_get_effective_iam_policies` interceptor. The (possibly modified) response returned by
        `post_batch_get_effective_iam_policies` will be passed to
        `post_batch_get_effective_iam_policies_with_metadata`.
        """
        return response, metadata

    def pre_create_feed(
        self,
        request: asset_service.CreateFeedRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        asset_service.CreateFeedRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_feed

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AssetService server.
        """
        return request, metadata

    def post_create_feed(self, response: asset_service.Feed) -> asset_service.Feed:
        """Post-rpc interceptor for create_feed

        DEPRECATED. Please use the `post_create_feed_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AssetService server but before
        it is returned to user code. This `post_create_feed` interceptor runs
        before the `post_create_feed_with_metadata` interceptor.
        """
        return response

    def post_create_feed_with_metadata(
        self,
        response: asset_service.Feed,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[asset_service.Feed, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_feed

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AssetService server but before it is returned to user code.

        We recommend only using this `post_create_feed_with_metadata`
        interceptor in new development instead of the `post_create_feed` interceptor.
        When both interceptors are used, this `post_create_feed_with_metadata` interceptor runs after the
        `post_create_feed` interceptor. The (possibly modified) response returned by
        `post_create_feed` will be passed to
        `post_create_feed_with_metadata`.
        """
        return response, metadata

    def pre_create_saved_query(
        self,
        request: asset_service.CreateSavedQueryRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        asset_service.CreateSavedQueryRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_saved_query

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AssetService server.
        """
        return request, metadata

    def post_create_saved_query(
        self, response: asset_service.SavedQuery
    ) -> asset_service.SavedQuery:
        """Post-rpc interceptor for create_saved_query

        DEPRECATED. Please use the `post_create_saved_query_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AssetService server but before
        it is returned to user code. This `post_create_saved_query` interceptor runs
        before the `post_create_saved_query_with_metadata` interceptor.
        """
        return response

    def post_create_saved_query_with_metadata(
        self,
        response: asset_service.SavedQuery,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[asset_service.SavedQuery, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_saved_query

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AssetService server but before it is returned to user code.

        We recommend only using this `post_create_saved_query_with_metadata`
        interceptor in new development instead of the `post_create_saved_query` interceptor.
        When both interceptors are used, this `post_create_saved_query_with_metadata` interceptor runs after the
        `post_create_saved_query` interceptor. The (possibly modified) response returned by
        `post_create_saved_query` will be passed to
        `post_create_saved_query_with_metadata`.
        """
        return response, metadata

    def pre_delete_feed(
        self,
        request: asset_service.DeleteFeedRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        asset_service.DeleteFeedRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_feed

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AssetService server.
        """
        return request, metadata

    def pre_delete_saved_query(
        self,
        request: asset_service.DeleteSavedQueryRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        asset_service.DeleteSavedQueryRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_saved_query

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AssetService server.
        """
        return request, metadata

    def pre_export_assets(
        self,
        request: asset_service.ExportAssetsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        asset_service.ExportAssetsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for export_assets

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AssetService server.
        """
        return request, metadata

    def post_export_assets(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for export_assets

        DEPRECATED. Please use the `post_export_assets_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AssetService server but before
        it is returned to user code. This `post_export_assets` interceptor runs
        before the `post_export_assets_with_metadata` interceptor.
        """
        return response

    def post_export_assets_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for export_assets

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AssetService server but before it is returned to user code.

        We recommend only using this `post_export_assets_with_metadata`
        interceptor in new development instead of the `post_export_assets` interceptor.
        When both interceptors are used, this `post_export_assets_with_metadata` interceptor runs after the
        `post_export_assets` interceptor. The (possibly modified) response returned by
        `post_export_assets` will be passed to
        `post_export_assets_with_metadata`.
        """
        return response, metadata

    def pre_get_feed(
        self,
        request: asset_service.GetFeedRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[asset_service.GetFeedRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_feed

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AssetService server.
        """
        return request, metadata

    def post_get_feed(self, response: asset_service.Feed) -> asset_service.Feed:
        """Post-rpc interceptor for get_feed

        DEPRECATED. Please use the `post_get_feed_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AssetService server but before
        it is returned to user code. This `post_get_feed` interceptor runs
        before the `post_get_feed_with_metadata` interceptor.
        """
        return response

    def post_get_feed_with_metadata(
        self,
        response: asset_service.Feed,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[asset_service.Feed, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_feed

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AssetService server but before it is returned to user code.

        We recommend only using this `post_get_feed_with_metadata`
        interceptor in new development instead of the `post_get_feed` interceptor.
        When both interceptors are used, this `post_get_feed_with_metadata` interceptor runs after the
        `post_get_feed` interceptor. The (possibly modified) response returned by
        `post_get_feed` will be passed to
        `post_get_feed_with_metadata`.
        """
        return response, metadata

    def pre_get_saved_query(
        self,
        request: asset_service.GetSavedQueryRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        asset_service.GetSavedQueryRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_saved_query

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AssetService server.
        """
        return request, metadata

    def post_get_saved_query(
        self, response: asset_service.SavedQuery
    ) -> asset_service.SavedQuery:
        """Post-rpc interceptor for get_saved_query

        DEPRECATED. Please use the `post_get_saved_query_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AssetService server but before
        it is returned to user code. This `post_get_saved_query` interceptor runs
        before the `post_get_saved_query_with_metadata` interceptor.
        """
        return response

    def post_get_saved_query_with_metadata(
        self,
        response: asset_service.SavedQuery,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[asset_service.SavedQuery, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_saved_query

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AssetService server but before it is returned to user code.

        We recommend only using this `post_get_saved_query_with_metadata`
        interceptor in new development instead of the `post_get_saved_query` interceptor.
        When both interceptors are used, this `post_get_saved_query_with_metadata` interceptor runs after the
        `post_get_saved_query` interceptor. The (possibly modified) response returned by
        `post_get_saved_query` will be passed to
        `post_get_saved_query_with_metadata`.
        """
        return response, metadata

    def pre_list_assets(
        self,
        request: asset_service.ListAssetsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        asset_service.ListAssetsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_assets

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AssetService server.
        """
        return request, metadata

    def post_list_assets(
        self, response: asset_service.ListAssetsResponse
    ) -> asset_service.ListAssetsResponse:
        """Post-rpc interceptor for list_assets

        DEPRECATED. Please use the `post_list_assets_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AssetService server but before
        it is returned to user code. This `post_list_assets` interceptor runs
        before the `post_list_assets_with_metadata` interceptor.
        """
        return response

    def post_list_assets_with_metadata(
        self,
        response: asset_service.ListAssetsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        asset_service.ListAssetsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_assets

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AssetService server but before it is returned to user code.

        We recommend only using this `post_list_assets_with_metadata`
        interceptor in new development instead of the `post_list_assets` interceptor.
        When both interceptors are used, this `post_list_assets_with_metadata` interceptor runs after the
        `post_list_assets` interceptor. The (possibly modified) response returned by
        `post_list_assets` will be passed to
        `post_list_assets_with_metadata`.
        """
        return response, metadata

    def pre_list_feeds(
        self,
        request: asset_service.ListFeedsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[asset_service.ListFeedsRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for list_feeds

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AssetService server.
        """
        return request, metadata

    def post_list_feeds(
        self, response: asset_service.ListFeedsResponse
    ) -> asset_service.ListFeedsResponse:
        """Post-rpc interceptor for list_feeds

        DEPRECATED. Please use the `post_list_feeds_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AssetService server but before
        it is returned to user code. This `post_list_feeds` interceptor runs
        before the `post_list_feeds_with_metadata` interceptor.
        """
        return response

    def post_list_feeds_with_metadata(
        self,
        response: asset_service.ListFeedsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        asset_service.ListFeedsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_feeds

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AssetService server but before it is returned to user code.

        We recommend only using this `post_list_feeds_with_metadata`
        interceptor in new development instead of the `post_list_feeds` interceptor.
        When both interceptors are used, this `post_list_feeds_with_metadata` interceptor runs after the
        `post_list_feeds` interceptor. The (possibly modified) response returned by
        `post_list_feeds` will be passed to
        `post_list_feeds_with_metadata`.
        """
        return response, metadata

    def pre_list_saved_queries(
        self,
        request: asset_service.ListSavedQueriesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        asset_service.ListSavedQueriesRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_saved_queries

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AssetService server.
        """
        return request, metadata

    def post_list_saved_queries(
        self, response: asset_service.ListSavedQueriesResponse
    ) -> asset_service.ListSavedQueriesResponse:
        """Post-rpc interceptor for list_saved_queries

        DEPRECATED. Please use the `post_list_saved_queries_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AssetService server but before
        it is returned to user code. This `post_list_saved_queries` interceptor runs
        before the `post_list_saved_queries_with_metadata` interceptor.
        """
        return response

    def post_list_saved_queries_with_metadata(
        self,
        response: asset_service.ListSavedQueriesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        asset_service.ListSavedQueriesResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_saved_queries

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AssetService server but before it is returned to user code.

        We recommend only using this `post_list_saved_queries_with_metadata`
        interceptor in new development instead of the `post_list_saved_queries` interceptor.
        When both interceptors are used, this `post_list_saved_queries_with_metadata` interceptor runs after the
        `post_list_saved_queries` interceptor. The (possibly modified) response returned by
        `post_list_saved_queries` will be passed to
        `post_list_saved_queries_with_metadata`.
        """
        return response, metadata

    def pre_query_assets(
        self,
        request: asset_service.QueryAssetsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        asset_service.QueryAssetsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for query_assets

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AssetService server.
        """
        return request, metadata

    def post_query_assets(
        self, response: asset_service.QueryAssetsResponse
    ) -> asset_service.QueryAssetsResponse:
        """Post-rpc interceptor for query_assets

        DEPRECATED. Please use the `post_query_assets_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AssetService server but before
        it is returned to user code. This `post_query_assets` interceptor runs
        before the `post_query_assets_with_metadata` interceptor.
        """
        return response

    def post_query_assets_with_metadata(
        self,
        response: asset_service.QueryAssetsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        asset_service.QueryAssetsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for query_assets

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AssetService server but before it is returned to user code.

        We recommend only using this `post_query_assets_with_metadata`
        interceptor in new development instead of the `post_query_assets` interceptor.
        When both interceptors are used, this `post_query_assets_with_metadata` interceptor runs after the
        `post_query_assets` interceptor. The (possibly modified) response returned by
        `post_query_assets` will be passed to
        `post_query_assets_with_metadata`.
        """
        return response, metadata

    def pre_search_all_iam_policies(
        self,
        request: asset_service.SearchAllIamPoliciesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        asset_service.SearchAllIamPoliciesRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for search_all_iam_policies

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AssetService server.
        """
        return request, metadata

    def post_search_all_iam_policies(
        self, response: asset_service.SearchAllIamPoliciesResponse
    ) -> asset_service.SearchAllIamPoliciesResponse:
        """Post-rpc interceptor for search_all_iam_policies

        DEPRECATED. Please use the `post_search_all_iam_policies_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AssetService server but before
        it is returned to user code. This `post_search_all_iam_policies` interceptor runs
        before the `post_search_all_iam_policies_with_metadata` interceptor.
        """
        return response

    def post_search_all_iam_policies_with_metadata(
        self,
        response: asset_service.SearchAllIamPoliciesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        asset_service.SearchAllIamPoliciesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for search_all_iam_policies

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AssetService server but before it is returned to user code.

        We recommend only using this `post_search_all_iam_policies_with_metadata`
        interceptor in new development instead of the `post_search_all_iam_policies` interceptor.
        When both interceptors are used, this `post_search_all_iam_policies_with_metadata` interceptor runs after the
        `post_search_all_iam_policies` interceptor. The (possibly modified) response returned by
        `post_search_all_iam_policies` will be passed to
        `post_search_all_iam_policies_with_metadata`.
        """
        return response, metadata

    def pre_search_all_resources(
        self,
        request: asset_service.SearchAllResourcesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        asset_service.SearchAllResourcesRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for search_all_resources

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AssetService server.
        """
        return request, metadata

    def post_search_all_resources(
        self, response: asset_service.SearchAllResourcesResponse
    ) -> asset_service.SearchAllResourcesResponse:
        """Post-rpc interceptor for search_all_resources

        DEPRECATED. Please use the `post_search_all_resources_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AssetService server but before
        it is returned to user code. This `post_search_all_resources` interceptor runs
        before the `post_search_all_resources_with_metadata` interceptor.
        """
        return response

    def post_search_all_resources_with_metadata(
        self,
        response: asset_service.SearchAllResourcesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        asset_service.SearchAllResourcesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for search_all_resources

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AssetService server but before it is returned to user code.

        We recommend only using this `post_search_all_resources_with_metadata`
        interceptor in new development instead of the `post_search_all_resources` interceptor.
        When both interceptors are used, this `post_search_all_resources_with_metadata` interceptor runs after the
        `post_search_all_resources` interceptor. The (possibly modified) response returned by
        `post_search_all_resources` will be passed to
        `post_search_all_resources_with_metadata`.
        """
        return response, metadata

    def pre_update_feed(
        self,
        request: asset_service.UpdateFeedRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        asset_service.UpdateFeedRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_feed

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AssetService server.
        """
        return request, metadata

    def post_update_feed(self, response: asset_service.Feed) -> asset_service.Feed:
        """Post-rpc interceptor for update_feed

        DEPRECATED. Please use the `post_update_feed_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AssetService server but before
        it is returned to user code. This `post_update_feed` interceptor runs
        before the `post_update_feed_with_metadata` interceptor.
        """
        return response

    def post_update_feed_with_metadata(
        self,
        response: asset_service.Feed,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[asset_service.Feed, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_feed

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AssetService server but before it is returned to user code.

        We recommend only using this `post_update_feed_with_metadata`
        interceptor in new development instead of the `post_update_feed` interceptor.
        When both interceptors are used, this `post_update_feed_with_metadata` interceptor runs after the
        `post_update_feed` interceptor. The (possibly modified) response returned by
        `post_update_feed` will be passed to
        `post_update_feed_with_metadata`.
        """
        return response, metadata

    def pre_update_saved_query(
        self,
        request: asset_service.UpdateSavedQueryRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        asset_service.UpdateSavedQueryRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_saved_query

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AssetService server.
        """
        return request, metadata

    def post_update_saved_query(
        self, response: asset_service.SavedQuery
    ) -> asset_service.SavedQuery:
        """Post-rpc interceptor for update_saved_query

        DEPRECATED. Please use the `post_update_saved_query_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AssetService server but before
        it is returned to user code. This `post_update_saved_query` interceptor runs
        before the `post_update_saved_query_with_metadata` interceptor.
        """
        return response

    def post_update_saved_query_with_metadata(
        self,
        response: asset_service.SavedQuery,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[asset_service.SavedQuery, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_saved_query

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AssetService server but before it is returned to user code.

        We recommend only using this `post_update_saved_query_with_metadata`
        interceptor in new development instead of the `post_update_saved_query` interceptor.
        When both interceptors are used, this `post_update_saved_query_with_metadata` interceptor runs after the
        `post_update_saved_query` interceptor. The (possibly modified) response returned by
        `post_update_saved_query` will be passed to
        `post_update_saved_query_with_metadata`.
        """
        return response, metadata

    def pre_get_operation(
        self,
        request: operations_pb2.GetOperationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        operations_pb2.GetOperationRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_operation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AssetService server.
        """
        return request, metadata

    def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the AssetService server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class AssetServiceRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: AssetServiceRestInterceptor


class AssetServiceRestTransport(_BaseAssetServiceRestTransport):
    """REST backend synchronous transport for AssetService.

    Asset service definition.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "cloudasset.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[AssetServiceRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'cloudasset.googleapis.com').
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
            interceptor (Optional[AssetServiceRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or AssetServiceRestInterceptor()
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
                "google.longrunning.Operations.GetOperation": [
                    {
                        "method": "get",
                        "uri": "/v1/{name=*/*/operations/*/**}",
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

    class _AnalyzeIamPolicy(
        _BaseAssetServiceRestTransport._BaseAnalyzeIamPolicy, AssetServiceRestStub
    ):
        def __hash__(self):
            return hash("AssetServiceRestTransport.AnalyzeIamPolicy")

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
            request: asset_service.AnalyzeIamPolicyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> asset_service.AnalyzeIamPolicyResponse:
            r"""Call the analyze iam policy method over HTTP.

            Args:
                request (~.asset_service.AnalyzeIamPolicyRequest):
                    The request object. A request message for
                [AssetService.AnalyzeIamPolicy][google.cloud.asset.v1.AssetService.AnalyzeIamPolicy].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.asset_service.AnalyzeIamPolicyResponse:
                    A response message for
                [AssetService.AnalyzeIamPolicy][google.cloud.asset.v1.AssetService.AnalyzeIamPolicy].

            """

            http_options = (
                _BaseAssetServiceRestTransport._BaseAnalyzeIamPolicy._get_http_options()
            )
            request, metadata = self._interceptor.pre_analyze_iam_policy(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAssetServiceRestTransport._BaseAnalyzeIamPolicy,
                    "_BaseAnalyzeIamPolicy__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.asset_v1.AssetServiceClient.AnalyzeIamPolicy",
                    extra={
                        "serviceName": "google.cloud.asset.v1.AssetService",
                        "rpcName": "AnalyzeIamPolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AssetServiceRestTransport._AnalyzeIamPolicy._get_response(
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
            resp = asset_service.AnalyzeIamPolicyResponse()
            pb_resp = asset_service.AnalyzeIamPolicyResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_analyze_iam_policy(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_analyze_iam_policy_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = asset_service.AnalyzeIamPolicyResponse.to_json(
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
                    "Received response for google.cloud.asset_v1.AssetServiceClient.analyze_iam_policy",
                    extra={
                        "serviceName": "google.cloud.asset.v1.AssetService",
                        "rpcName": "AnalyzeIamPolicy",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _AnalyzeIamPolicyLongrunning(
        _BaseAssetServiceRestTransport._BaseAnalyzeIamPolicyLongrunning,
        AssetServiceRestStub,
    ):
        def __hash__(self):
            return hash("AssetServiceRestTransport.AnalyzeIamPolicyLongrunning")

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
            request: asset_service.AnalyzeIamPolicyLongrunningRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the analyze iam policy
            longrunning method over HTTP.

                Args:
                    request (~.asset_service.AnalyzeIamPolicyLongrunningRequest):
                        The request object. A request message for
                    [AssetService.AnalyzeIamPolicyLongrunning][google.cloud.asset.v1.AssetService.AnalyzeIamPolicyLongrunning].
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

            http_options = _BaseAssetServiceRestTransport._BaseAnalyzeIamPolicyLongrunning._get_http_options()
            request, metadata = self._interceptor.pre_analyze_iam_policy_longrunning(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAssetServiceRestTransport._BaseAnalyzeIamPolicyLongrunning,
                    "_BaseAnalyzeIamPolicyLongrunning__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.asset_v1.AssetServiceClient.AnalyzeIamPolicyLongrunning",
                    extra={
                        "serviceName": "google.cloud.asset.v1.AssetService",
                        "rpcName": "AnalyzeIamPolicyLongrunning",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                AssetServiceRestTransport._AnalyzeIamPolicyLongrunning._get_response(
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

            resp = self._interceptor.post_analyze_iam_policy_longrunning(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_analyze_iam_policy_longrunning_with_metadata(
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
                    "Received response for google.cloud.asset_v1.AssetServiceClient.analyze_iam_policy_longrunning",
                    extra={
                        "serviceName": "google.cloud.asset.v1.AssetService",
                        "rpcName": "AnalyzeIamPolicyLongrunning",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _AnalyzeMove(
        _BaseAssetServiceRestTransport._BaseAnalyzeMove, AssetServiceRestStub
    ):
        def __hash__(self):
            return hash("AssetServiceRestTransport.AnalyzeMove")

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
            request: asset_service.AnalyzeMoveRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> asset_service.AnalyzeMoveResponse:
            r"""Call the analyze move method over HTTP.

            Args:
                request (~.asset_service.AnalyzeMoveRequest):
                    The request object. The request message for performing
                resource move analysis.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.asset_service.AnalyzeMoveResponse:
                    The response message for resource
                move analysis.

            """

            http_options = (
                _BaseAssetServiceRestTransport._BaseAnalyzeMove._get_http_options()
            )
            request, metadata = self._interceptor.pre_analyze_move(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAssetServiceRestTransport._BaseAnalyzeMove,
                    "_BaseAnalyzeMove__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.asset_v1.AssetServiceClient.AnalyzeMove",
                    extra={
                        "serviceName": "google.cloud.asset.v1.AssetService",
                        "rpcName": "AnalyzeMove",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AssetServiceRestTransport._AnalyzeMove._get_response(
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
            resp = asset_service.AnalyzeMoveResponse()
            pb_resp = asset_service.AnalyzeMoveResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_analyze_move(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_analyze_move_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = asset_service.AnalyzeMoveResponse.to_json(
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
                    "Received response for google.cloud.asset_v1.AssetServiceClient.analyze_move",
                    extra={
                        "serviceName": "google.cloud.asset.v1.AssetService",
                        "rpcName": "AnalyzeMove",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _AnalyzeOrgPolicies(
        _BaseAssetServiceRestTransport._BaseAnalyzeOrgPolicies, AssetServiceRestStub
    ):
        def __hash__(self):
            return hash("AssetServiceRestTransport.AnalyzeOrgPolicies")

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
            request: asset_service.AnalyzeOrgPoliciesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> asset_service.AnalyzeOrgPoliciesResponse:
            r"""Call the analyze org policies method over HTTP.

            Args:
                request (~.asset_service.AnalyzeOrgPoliciesRequest):
                    The request object. A request message for
                [AssetService.AnalyzeOrgPolicies][google.cloud.asset.v1.AssetService.AnalyzeOrgPolicies].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.asset_service.AnalyzeOrgPoliciesResponse:
                    The response message for
                [AssetService.AnalyzeOrgPolicies][google.cloud.asset.v1.AssetService.AnalyzeOrgPolicies].

            """

            http_options = _BaseAssetServiceRestTransport._BaseAnalyzeOrgPolicies._get_http_options()
            request, metadata = self._interceptor.pre_analyze_org_policies(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAssetServiceRestTransport._BaseAnalyzeOrgPolicies,
                    "_BaseAnalyzeOrgPolicies__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.asset_v1.AssetServiceClient.AnalyzeOrgPolicies",
                    extra={
                        "serviceName": "google.cloud.asset.v1.AssetService",
                        "rpcName": "AnalyzeOrgPolicies",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AssetServiceRestTransport._AnalyzeOrgPolicies._get_response(
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
            resp = asset_service.AnalyzeOrgPoliciesResponse()
            pb_resp = asset_service.AnalyzeOrgPoliciesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_analyze_org_policies(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_analyze_org_policies_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = asset_service.AnalyzeOrgPoliciesResponse.to_json(
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
                    "Received response for google.cloud.asset_v1.AssetServiceClient.analyze_org_policies",
                    extra={
                        "serviceName": "google.cloud.asset.v1.AssetService",
                        "rpcName": "AnalyzeOrgPolicies",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _AnalyzeOrgPolicyGovernedAssets(
        _BaseAssetServiceRestTransport._BaseAnalyzeOrgPolicyGovernedAssets,
        AssetServiceRestStub,
    ):
        def __hash__(self):
            return hash("AssetServiceRestTransport.AnalyzeOrgPolicyGovernedAssets")

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
            request: asset_service.AnalyzeOrgPolicyGovernedAssetsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> asset_service.AnalyzeOrgPolicyGovernedAssetsResponse:
            r"""Call the analyze org policy
            governed assets method over HTTP.

                Args:
                    request (~.asset_service.AnalyzeOrgPolicyGovernedAssetsRequest):
                        The request object. A request message for
                    [AssetService.AnalyzeOrgPolicyGovernedAssets][google.cloud.asset.v1.AssetService.AnalyzeOrgPolicyGovernedAssets].
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.asset_service.AnalyzeOrgPolicyGovernedAssetsResponse:
                        The response message for
                    [AssetService.AnalyzeOrgPolicyGovernedAssets][google.cloud.asset.v1.AssetService.AnalyzeOrgPolicyGovernedAssets].

            """

            http_options = _BaseAssetServiceRestTransport._BaseAnalyzeOrgPolicyGovernedAssets._get_http_options()
            request, metadata = (
                self._interceptor.pre_analyze_org_policy_governed_assets(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAssetServiceRestTransport._BaseAnalyzeOrgPolicyGovernedAssets,
                    "_BaseAnalyzeOrgPolicyGovernedAssets__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.asset_v1.AssetServiceClient.AnalyzeOrgPolicyGovernedAssets",
                    extra={
                        "serviceName": "google.cloud.asset.v1.AssetService",
                        "rpcName": "AnalyzeOrgPolicyGovernedAssets",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                AssetServiceRestTransport._AnalyzeOrgPolicyGovernedAssets._get_response(
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
            resp = asset_service.AnalyzeOrgPolicyGovernedAssetsResponse()
            pb_resp = asset_service.AnalyzeOrgPolicyGovernedAssetsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_analyze_org_policy_governed_assets(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_analyze_org_policy_governed_assets_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        asset_service.AnalyzeOrgPolicyGovernedAssetsResponse.to_json(
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
                    "Received response for google.cloud.asset_v1.AssetServiceClient.analyze_org_policy_governed_assets",
                    extra={
                        "serviceName": "google.cloud.asset.v1.AssetService",
                        "rpcName": "AnalyzeOrgPolicyGovernedAssets",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _AnalyzeOrgPolicyGovernedContainers(
        _BaseAssetServiceRestTransport._BaseAnalyzeOrgPolicyGovernedContainers,
        AssetServiceRestStub,
    ):
        def __hash__(self):
            return hash("AssetServiceRestTransport.AnalyzeOrgPolicyGovernedContainers")

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
            request: asset_service.AnalyzeOrgPolicyGovernedContainersRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> asset_service.AnalyzeOrgPolicyGovernedContainersResponse:
            r"""Call the analyze org policy
            governed containers method over HTTP.

                Args:
                    request (~.asset_service.AnalyzeOrgPolicyGovernedContainersRequest):
                        The request object. A request message for
                    [AssetService.AnalyzeOrgPolicyGovernedContainers][google.cloud.asset.v1.AssetService.AnalyzeOrgPolicyGovernedContainers].
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.asset_service.AnalyzeOrgPolicyGovernedContainersResponse:
                        The response message for
                    [AssetService.AnalyzeOrgPolicyGovernedContainers][google.cloud.asset.v1.AssetService.AnalyzeOrgPolicyGovernedContainers].

            """

            http_options = _BaseAssetServiceRestTransport._BaseAnalyzeOrgPolicyGovernedContainers._get_http_options()
            request, metadata = (
                self._interceptor.pre_analyze_org_policy_governed_containers(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAssetServiceRestTransport._BaseAnalyzeOrgPolicyGovernedContainers,
                    "_BaseAnalyzeOrgPolicyGovernedContainers__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.asset_v1.AssetServiceClient.AnalyzeOrgPolicyGovernedContainers",
                    extra={
                        "serviceName": "google.cloud.asset.v1.AssetService",
                        "rpcName": "AnalyzeOrgPolicyGovernedContainers",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AssetServiceRestTransport._AnalyzeOrgPolicyGovernedContainers._get_response(
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
            resp = asset_service.AnalyzeOrgPolicyGovernedContainersResponse()
            pb_resp = asset_service.AnalyzeOrgPolicyGovernedContainersResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_analyze_org_policy_governed_containers(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_analyze_org_policy_governed_containers_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = asset_service.AnalyzeOrgPolicyGovernedContainersResponse.to_json(
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
                    "Received response for google.cloud.asset_v1.AssetServiceClient.analyze_org_policy_governed_containers",
                    extra={
                        "serviceName": "google.cloud.asset.v1.AssetService",
                        "rpcName": "AnalyzeOrgPolicyGovernedContainers",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BatchGetAssetsHistory(
        _BaseAssetServiceRestTransport._BaseBatchGetAssetsHistory, AssetServiceRestStub
    ):
        def __hash__(self):
            return hash("AssetServiceRestTransport.BatchGetAssetsHistory")

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
            request: asset_service.BatchGetAssetsHistoryRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> asset_service.BatchGetAssetsHistoryResponse:
            r"""Call the batch get assets history method over HTTP.

            Args:
                request (~.asset_service.BatchGetAssetsHistoryRequest):
                    The request object. Batch get assets history request.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.asset_service.BatchGetAssetsHistoryResponse:
                    Batch get assets history response.
            """

            http_options = _BaseAssetServiceRestTransport._BaseBatchGetAssetsHistory._get_http_options()
            request, metadata = self._interceptor.pre_batch_get_assets_history(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAssetServiceRestTransport._BaseBatchGetAssetsHistory,
                    "_BaseBatchGetAssetsHistory__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.asset_v1.AssetServiceClient.BatchGetAssetsHistory",
                    extra={
                        "serviceName": "google.cloud.asset.v1.AssetService",
                        "rpcName": "BatchGetAssetsHistory",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AssetServiceRestTransport._BatchGetAssetsHistory._get_response(
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
            resp = asset_service.BatchGetAssetsHistoryResponse()
            pb_resp = asset_service.BatchGetAssetsHistoryResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_get_assets_history(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_batch_get_assets_history_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        asset_service.BatchGetAssetsHistoryResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.asset_v1.AssetServiceClient.batch_get_assets_history",
                    extra={
                        "serviceName": "google.cloud.asset.v1.AssetService",
                        "rpcName": "BatchGetAssetsHistory",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BatchGetEffectiveIamPolicies(
        _BaseAssetServiceRestTransport._BaseBatchGetEffectiveIamPolicies,
        AssetServiceRestStub,
    ):
        def __hash__(self):
            return hash("AssetServiceRestTransport.BatchGetEffectiveIamPolicies")

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
            request: asset_service.BatchGetEffectiveIamPoliciesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> asset_service.BatchGetEffectiveIamPoliciesResponse:
            r"""Call the batch get effective iam
            policies method over HTTP.

                Args:
                    request (~.asset_service.BatchGetEffectiveIamPoliciesRequest):
                        The request object. A request message for
                    [AssetService.BatchGetEffectiveIamPolicies][google.cloud.asset.v1.AssetService.BatchGetEffectiveIamPolicies].
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.asset_service.BatchGetEffectiveIamPoliciesResponse:
                        A response message for
                    [AssetService.BatchGetEffectiveIamPolicies][google.cloud.asset.v1.AssetService.BatchGetEffectiveIamPolicies].

            """

            http_options = _BaseAssetServiceRestTransport._BaseBatchGetEffectiveIamPolicies._get_http_options()
            request, metadata = self._interceptor.pre_batch_get_effective_iam_policies(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAssetServiceRestTransport._BaseBatchGetEffectiveIamPolicies,
                    "_BaseBatchGetEffectiveIamPolicies__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.asset_v1.AssetServiceClient.BatchGetEffectiveIamPolicies",
                    extra={
                        "serviceName": "google.cloud.asset.v1.AssetService",
                        "rpcName": "BatchGetEffectiveIamPolicies",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                AssetServiceRestTransport._BatchGetEffectiveIamPolicies._get_response(
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
            resp = asset_service.BatchGetEffectiveIamPoliciesResponse()
            pb_resp = asset_service.BatchGetEffectiveIamPoliciesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_get_effective_iam_policies(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_batch_get_effective_iam_policies_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        asset_service.BatchGetEffectiveIamPoliciesResponse.to_json(
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
                    "Received response for google.cloud.asset_v1.AssetServiceClient.batch_get_effective_iam_policies",
                    extra={
                        "serviceName": "google.cloud.asset.v1.AssetService",
                        "rpcName": "BatchGetEffectiveIamPolicies",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateFeed(
        _BaseAssetServiceRestTransport._BaseCreateFeed, AssetServiceRestStub
    ):
        def __hash__(self):
            return hash("AssetServiceRestTransport.CreateFeed")

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
            request: asset_service.CreateFeedRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> asset_service.Feed:
            r"""Call the create feed method over HTTP.

            Args:
                request (~.asset_service.CreateFeedRequest):
                    The request object. Create asset feed request.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.asset_service.Feed:
                    An asset feed used to export asset
                updates to a destinations. An asset feed
                filter controls what updates are
                exported. The asset feed must be created
                within a project, organization, or
                folder. Supported destinations are:

                Pub/Sub topics.

            """

            http_options = (
                _BaseAssetServiceRestTransport._BaseCreateFeed._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_feed(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAssetServiceRestTransport._BaseCreateFeed,
                    "_BaseCreateFeed__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.asset_v1.AssetServiceClient.CreateFeed",
                    extra={
                        "serviceName": "google.cloud.asset.v1.AssetService",
                        "rpcName": "CreateFeed",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AssetServiceRestTransport._CreateFeed._get_response(
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
            resp = asset_service.Feed()
            pb_resp = asset_service.Feed.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_feed(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_feed_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = asset_service.Feed.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.asset_v1.AssetServiceClient.create_feed",
                    extra={
                        "serviceName": "google.cloud.asset.v1.AssetService",
                        "rpcName": "CreateFeed",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateSavedQuery(
        _BaseAssetServiceRestTransport._BaseCreateSavedQuery, AssetServiceRestStub
    ):
        def __hash__(self):
            return hash("AssetServiceRestTransport.CreateSavedQuery")

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
            request: asset_service.CreateSavedQueryRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> asset_service.SavedQuery:
            r"""Call the create saved query method over HTTP.

            Args:
                request (~.asset_service.CreateSavedQueryRequest):
                    The request object. Request to create a saved query.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.asset_service.SavedQuery:
                    A saved query which can be shared
                with others or used later.

            """

            http_options = (
                _BaseAssetServiceRestTransport._BaseCreateSavedQuery._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_saved_query(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAssetServiceRestTransport._BaseCreateSavedQuery,
                    "_BaseCreateSavedQuery__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.asset_v1.AssetServiceClient.CreateSavedQuery",
                    extra={
                        "serviceName": "google.cloud.asset.v1.AssetService",
                        "rpcName": "CreateSavedQuery",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AssetServiceRestTransport._CreateSavedQuery._get_response(
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
            resp = asset_service.SavedQuery()
            pb_resp = asset_service.SavedQuery.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_saved_query(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_saved_query_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = asset_service.SavedQuery.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.asset_v1.AssetServiceClient.create_saved_query",
                    extra={
                        "serviceName": "google.cloud.asset.v1.AssetService",
                        "rpcName": "CreateSavedQuery",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteFeed(
        _BaseAssetServiceRestTransport._BaseDeleteFeed, AssetServiceRestStub
    ):
        def __hash__(self):
            return hash("AssetServiceRestTransport.DeleteFeed")

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
            request: asset_service.DeleteFeedRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete feed method over HTTP.

            Args:
                request (~.asset_service.DeleteFeedRequest):
                    The request object.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = (
                _BaseAssetServiceRestTransport._BaseDeleteFeed._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_feed(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAssetServiceRestTransport._BaseDeleteFeed,
                    "_BaseDeleteFeed__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.asset_v1.AssetServiceClient.DeleteFeed",
                    extra={
                        "serviceName": "google.cloud.asset.v1.AssetService",
                        "rpcName": "DeleteFeed",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AssetServiceRestTransport._DeleteFeed._get_response(
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

    class _DeleteSavedQuery(
        _BaseAssetServiceRestTransport._BaseDeleteSavedQuery, AssetServiceRestStub
    ):
        def __hash__(self):
            return hash("AssetServiceRestTransport.DeleteSavedQuery")

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
            request: asset_service.DeleteSavedQueryRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete saved query method over HTTP.

            Args:
                request (~.asset_service.DeleteSavedQueryRequest):
                    The request object. Request to delete a saved query.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = (
                _BaseAssetServiceRestTransport._BaseDeleteSavedQuery._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_saved_query(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAssetServiceRestTransport._BaseDeleteSavedQuery,
                    "_BaseDeleteSavedQuery__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.asset_v1.AssetServiceClient.DeleteSavedQuery",
                    extra={
                        "serviceName": "google.cloud.asset.v1.AssetService",
                        "rpcName": "DeleteSavedQuery",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AssetServiceRestTransport._DeleteSavedQuery._get_response(
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

    class _ExportAssets(
        _BaseAssetServiceRestTransport._BaseExportAssets, AssetServiceRestStub
    ):
        def __hash__(self):
            return hash("AssetServiceRestTransport.ExportAssets")

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
            request: asset_service.ExportAssetsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the export assets method over HTTP.

            Args:
                request (~.asset_service.ExportAssetsRequest):
                    The request object. Export asset request.
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
                _BaseAssetServiceRestTransport._BaseExportAssets._get_http_options()
            )
            request, metadata = self._interceptor.pre_export_assets(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAssetServiceRestTransport._BaseExportAssets,
                    "_BaseExportAssets__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.asset_v1.AssetServiceClient.ExportAssets",
                    extra={
                        "serviceName": "google.cloud.asset.v1.AssetService",
                        "rpcName": "ExportAssets",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AssetServiceRestTransport._ExportAssets._get_response(
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

            resp = self._interceptor.post_export_assets(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_export_assets_with_metadata(
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
                    "Received response for google.cloud.asset_v1.AssetServiceClient.export_assets",
                    extra={
                        "serviceName": "google.cloud.asset.v1.AssetService",
                        "rpcName": "ExportAssets",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetFeed(_BaseAssetServiceRestTransport._BaseGetFeed, AssetServiceRestStub):
        def __hash__(self):
            return hash("AssetServiceRestTransport.GetFeed")

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
            request: asset_service.GetFeedRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> asset_service.Feed:
            r"""Call the get feed method over HTTP.

            Args:
                request (~.asset_service.GetFeedRequest):
                    The request object. Get asset feed request.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.asset_service.Feed:
                    An asset feed used to export asset
                updates to a destinations. An asset feed
                filter controls what updates are
                exported. The asset feed must be created
                within a project, organization, or
                folder. Supported destinations are:

                Pub/Sub topics.

            """

            http_options = (
                _BaseAssetServiceRestTransport._BaseGetFeed._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_feed(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAssetServiceRestTransport._BaseGetFeed,
                    "_BaseGetFeed__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.asset_v1.AssetServiceClient.GetFeed",
                    extra={
                        "serviceName": "google.cloud.asset.v1.AssetService",
                        "rpcName": "GetFeed",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AssetServiceRestTransport._GetFeed._get_response(
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
            resp = asset_service.Feed()
            pb_resp = asset_service.Feed.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_feed(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_feed_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = asset_service.Feed.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.asset_v1.AssetServiceClient.get_feed",
                    extra={
                        "serviceName": "google.cloud.asset.v1.AssetService",
                        "rpcName": "GetFeed",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetSavedQuery(
        _BaseAssetServiceRestTransport._BaseGetSavedQuery, AssetServiceRestStub
    ):
        def __hash__(self):
            return hash("AssetServiceRestTransport.GetSavedQuery")

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
            request: asset_service.GetSavedQueryRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> asset_service.SavedQuery:
            r"""Call the get saved query method over HTTP.

            Args:
                request (~.asset_service.GetSavedQueryRequest):
                    The request object. Request to get a saved query.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.asset_service.SavedQuery:
                    A saved query which can be shared
                with others or used later.

            """

            http_options = (
                _BaseAssetServiceRestTransport._BaseGetSavedQuery._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_saved_query(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAssetServiceRestTransport._BaseGetSavedQuery,
                    "_BaseGetSavedQuery__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.asset_v1.AssetServiceClient.GetSavedQuery",
                    extra={
                        "serviceName": "google.cloud.asset.v1.AssetService",
                        "rpcName": "GetSavedQuery",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AssetServiceRestTransport._GetSavedQuery._get_response(
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
            resp = asset_service.SavedQuery()
            pb_resp = asset_service.SavedQuery.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_saved_query(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_saved_query_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = asset_service.SavedQuery.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.asset_v1.AssetServiceClient.get_saved_query",
                    extra={
                        "serviceName": "google.cloud.asset.v1.AssetService",
                        "rpcName": "GetSavedQuery",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListAssets(
        _BaseAssetServiceRestTransport._BaseListAssets, AssetServiceRestStub
    ):
        def __hash__(self):
            return hash("AssetServiceRestTransport.ListAssets")

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
            request: asset_service.ListAssetsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> asset_service.ListAssetsResponse:
            r"""Call the list assets method over HTTP.

            Args:
                request (~.asset_service.ListAssetsRequest):
                    The request object. ListAssets request.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.asset_service.ListAssetsResponse:
                    ListAssets response.
            """

            http_options = (
                _BaseAssetServiceRestTransport._BaseListAssets._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_assets(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAssetServiceRestTransport._BaseListAssets,
                    "_BaseListAssets__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.asset_v1.AssetServiceClient.ListAssets",
                    extra={
                        "serviceName": "google.cloud.asset.v1.AssetService",
                        "rpcName": "ListAssets",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AssetServiceRestTransport._ListAssets._get_response(
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
            resp = asset_service.ListAssetsResponse()
            pb_resp = asset_service.ListAssetsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_assets(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_assets_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = asset_service.ListAssetsResponse.to_json(
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
                    "Received response for google.cloud.asset_v1.AssetServiceClient.list_assets",
                    extra={
                        "serviceName": "google.cloud.asset.v1.AssetService",
                        "rpcName": "ListAssets",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListFeeds(
        _BaseAssetServiceRestTransport._BaseListFeeds, AssetServiceRestStub
    ):
        def __hash__(self):
            return hash("AssetServiceRestTransport.ListFeeds")

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
            request: asset_service.ListFeedsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> asset_service.ListFeedsResponse:
            r"""Call the list feeds method over HTTP.

            Args:
                request (~.asset_service.ListFeedsRequest):
                    The request object. List asset feeds request.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.asset_service.ListFeedsResponse:

            """

            http_options = (
                _BaseAssetServiceRestTransport._BaseListFeeds._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_feeds(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAssetServiceRestTransport._BaseListFeeds,
                    "_BaseListFeeds__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.asset_v1.AssetServiceClient.ListFeeds",
                    extra={
                        "serviceName": "google.cloud.asset.v1.AssetService",
                        "rpcName": "ListFeeds",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AssetServiceRestTransport._ListFeeds._get_response(
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
            resp = asset_service.ListFeedsResponse()
            pb_resp = asset_service.ListFeedsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_feeds(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_feeds_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = asset_service.ListFeedsResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.asset_v1.AssetServiceClient.list_feeds",
                    extra={
                        "serviceName": "google.cloud.asset.v1.AssetService",
                        "rpcName": "ListFeeds",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListSavedQueries(
        _BaseAssetServiceRestTransport._BaseListSavedQueries, AssetServiceRestStub
    ):
        def __hash__(self):
            return hash("AssetServiceRestTransport.ListSavedQueries")

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
            request: asset_service.ListSavedQueriesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> asset_service.ListSavedQueriesResponse:
            r"""Call the list saved queries method over HTTP.

            Args:
                request (~.asset_service.ListSavedQueriesRequest):
                    The request object. Request to list saved queries.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.asset_service.ListSavedQueriesResponse:
                    Response of listing saved queries.
            """

            http_options = (
                _BaseAssetServiceRestTransport._BaseListSavedQueries._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_saved_queries(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAssetServiceRestTransport._BaseListSavedQueries,
                    "_BaseListSavedQueries__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.asset_v1.AssetServiceClient.ListSavedQueries",
                    extra={
                        "serviceName": "google.cloud.asset.v1.AssetService",
                        "rpcName": "ListSavedQueries",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AssetServiceRestTransport._ListSavedQueries._get_response(
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
            resp = asset_service.ListSavedQueriesResponse()
            pb_resp = asset_service.ListSavedQueriesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_saved_queries(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_saved_queries_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = asset_service.ListSavedQueriesResponse.to_json(
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
                    "Received response for google.cloud.asset_v1.AssetServiceClient.list_saved_queries",
                    extra={
                        "serviceName": "google.cloud.asset.v1.AssetService",
                        "rpcName": "ListSavedQueries",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _QueryAssets(
        _BaseAssetServiceRestTransport._BaseQueryAssets, AssetServiceRestStub
    ):
        def __hash__(self):
            return hash("AssetServiceRestTransport.QueryAssets")

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
            request: asset_service.QueryAssetsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> asset_service.QueryAssetsResponse:
            r"""Call the query assets method over HTTP.

            Args:
                request (~.asset_service.QueryAssetsRequest):
                    The request object. QueryAssets request.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.asset_service.QueryAssetsResponse:
                    QueryAssets response.
            """

            http_options = (
                _BaseAssetServiceRestTransport._BaseQueryAssets._get_http_options()
            )
            request, metadata = self._interceptor.pre_query_assets(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAssetServiceRestTransport._BaseQueryAssets,
                    "_BaseQueryAssets__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.asset_v1.AssetServiceClient.QueryAssets",
                    extra={
                        "serviceName": "google.cloud.asset.v1.AssetService",
                        "rpcName": "QueryAssets",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AssetServiceRestTransport._QueryAssets._get_response(
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
            resp = asset_service.QueryAssetsResponse()
            pb_resp = asset_service.QueryAssetsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_query_assets(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_query_assets_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = asset_service.QueryAssetsResponse.to_json(
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
                    "Received response for google.cloud.asset_v1.AssetServiceClient.query_assets",
                    extra={
                        "serviceName": "google.cloud.asset.v1.AssetService",
                        "rpcName": "QueryAssets",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _SearchAllIamPolicies(
        _BaseAssetServiceRestTransport._BaseSearchAllIamPolicies, AssetServiceRestStub
    ):
        def __hash__(self):
            return hash("AssetServiceRestTransport.SearchAllIamPolicies")

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
            request: asset_service.SearchAllIamPoliciesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> asset_service.SearchAllIamPoliciesResponse:
            r"""Call the search all iam policies method over HTTP.

            Args:
                request (~.asset_service.SearchAllIamPoliciesRequest):
                    The request object. Search all IAM policies request.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.asset_service.SearchAllIamPoliciesResponse:
                    Search all IAM policies response.
            """

            http_options = _BaseAssetServiceRestTransport._BaseSearchAllIamPolicies._get_http_options()
            request, metadata = self._interceptor.pre_search_all_iam_policies(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAssetServiceRestTransport._BaseSearchAllIamPolicies,
                    "_BaseSearchAllIamPolicies__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.asset_v1.AssetServiceClient.SearchAllIamPolicies",
                    extra={
                        "serviceName": "google.cloud.asset.v1.AssetService",
                        "rpcName": "SearchAllIamPolicies",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AssetServiceRestTransport._SearchAllIamPolicies._get_response(
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
            resp = asset_service.SearchAllIamPoliciesResponse()
            pb_resp = asset_service.SearchAllIamPoliciesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_search_all_iam_policies(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_search_all_iam_policies_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        asset_service.SearchAllIamPoliciesResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.asset_v1.AssetServiceClient.search_all_iam_policies",
                    extra={
                        "serviceName": "google.cloud.asset.v1.AssetService",
                        "rpcName": "SearchAllIamPolicies",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _SearchAllResources(
        _BaseAssetServiceRestTransport._BaseSearchAllResources, AssetServiceRestStub
    ):
        def __hash__(self):
            return hash("AssetServiceRestTransport.SearchAllResources")

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
            request: asset_service.SearchAllResourcesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> asset_service.SearchAllResourcesResponse:
            r"""Call the search all resources method over HTTP.

            Args:
                request (~.asset_service.SearchAllResourcesRequest):
                    The request object. Search all resources request.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.asset_service.SearchAllResourcesResponse:
                    Search all resources response.
            """

            http_options = _BaseAssetServiceRestTransport._BaseSearchAllResources._get_http_options()
            request, metadata = self._interceptor.pre_search_all_resources(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAssetServiceRestTransport._BaseSearchAllResources,
                    "_BaseSearchAllResources__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.asset_v1.AssetServiceClient.SearchAllResources",
                    extra={
                        "serviceName": "google.cloud.asset.v1.AssetService",
                        "rpcName": "SearchAllResources",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AssetServiceRestTransport._SearchAllResources._get_response(
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
            resp = asset_service.SearchAllResourcesResponse()
            pb_resp = asset_service.SearchAllResourcesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_search_all_resources(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_search_all_resources_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = asset_service.SearchAllResourcesResponse.to_json(
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
                    "Received response for google.cloud.asset_v1.AssetServiceClient.search_all_resources",
                    extra={
                        "serviceName": "google.cloud.asset.v1.AssetService",
                        "rpcName": "SearchAllResources",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateFeed(
        _BaseAssetServiceRestTransport._BaseUpdateFeed, AssetServiceRestStub
    ):
        def __hash__(self):
            return hash("AssetServiceRestTransport.UpdateFeed")

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
            request: asset_service.UpdateFeedRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> asset_service.Feed:
            r"""Call the update feed method over HTTP.

            Args:
                request (~.asset_service.UpdateFeedRequest):
                    The request object. Update asset feed request.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.asset_service.Feed:
                    An asset feed used to export asset
                updates to a destinations. An asset feed
                filter controls what updates are
                exported. The asset feed must be created
                within a project, organization, or
                folder. Supported destinations are:

                Pub/Sub topics.

            """

            http_options = (
                _BaseAssetServiceRestTransport._BaseUpdateFeed._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_feed(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAssetServiceRestTransport._BaseUpdateFeed,
                    "_BaseUpdateFeed__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.asset_v1.AssetServiceClient.UpdateFeed",
                    extra={
                        "serviceName": "google.cloud.asset.v1.AssetService",
                        "rpcName": "UpdateFeed",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AssetServiceRestTransport._UpdateFeed._get_response(
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
            resp = asset_service.Feed()
            pb_resp = asset_service.Feed.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_feed(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_feed_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = asset_service.Feed.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.asset_v1.AssetServiceClient.update_feed",
                    extra={
                        "serviceName": "google.cloud.asset.v1.AssetService",
                        "rpcName": "UpdateFeed",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateSavedQuery(
        _BaseAssetServiceRestTransport._BaseUpdateSavedQuery, AssetServiceRestStub
    ):
        def __hash__(self):
            return hash("AssetServiceRestTransport.UpdateSavedQuery")

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
            request: asset_service.UpdateSavedQueryRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> asset_service.SavedQuery:
            r"""Call the update saved query method over HTTP.

            Args:
                request (~.asset_service.UpdateSavedQueryRequest):
                    The request object. Request to update a saved query.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.asset_service.SavedQuery:
                    A saved query which can be shared
                with others or used later.

            """

            http_options = (
                _BaseAssetServiceRestTransport._BaseUpdateSavedQuery._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_saved_query(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAssetServiceRestTransport._BaseUpdateSavedQuery,
                    "_BaseUpdateSavedQuery__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.asset_v1.AssetServiceClient.UpdateSavedQuery",
                    extra={
                        "serviceName": "google.cloud.asset.v1.AssetService",
                        "rpcName": "UpdateSavedQuery",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AssetServiceRestTransport._UpdateSavedQuery._get_response(
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
            resp = asset_service.SavedQuery()
            pb_resp = asset_service.SavedQuery.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_saved_query(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_saved_query_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = asset_service.SavedQuery.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.asset_v1.AssetServiceClient.update_saved_query",
                    extra={
                        "serviceName": "google.cloud.asset.v1.AssetService",
                        "rpcName": "UpdateSavedQuery",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def analyze_iam_policy(
        self,
    ) -> Callable[
        [asset_service.AnalyzeIamPolicyRequest], asset_service.AnalyzeIamPolicyResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._AnalyzeIamPolicy(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def analyze_iam_policy_longrunning(
        self,
    ) -> Callable[
        [asset_service.AnalyzeIamPolicyLongrunningRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._AnalyzeIamPolicyLongrunning(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def analyze_move(
        self,
    ) -> Callable[
        [asset_service.AnalyzeMoveRequest], asset_service.AnalyzeMoveResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._AnalyzeMove(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def analyze_org_policies(
        self,
    ) -> Callable[
        [asset_service.AnalyzeOrgPoliciesRequest],
        asset_service.AnalyzeOrgPoliciesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._AnalyzeOrgPolicies(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def analyze_org_policy_governed_assets(
        self,
    ) -> Callable[
        [asset_service.AnalyzeOrgPolicyGovernedAssetsRequest],
        asset_service.AnalyzeOrgPolicyGovernedAssetsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._AnalyzeOrgPolicyGovernedAssets(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def analyze_org_policy_governed_containers(
        self,
    ) -> Callable[
        [asset_service.AnalyzeOrgPolicyGovernedContainersRequest],
        asset_service.AnalyzeOrgPolicyGovernedContainersResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._AnalyzeOrgPolicyGovernedContainers(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def batch_get_assets_history(
        self,
    ) -> Callable[
        [asset_service.BatchGetAssetsHistoryRequest],
        asset_service.BatchGetAssetsHistoryResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchGetAssetsHistory(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def batch_get_effective_iam_policies(
        self,
    ) -> Callable[
        [asset_service.BatchGetEffectiveIamPoliciesRequest],
        asset_service.BatchGetEffectiveIamPoliciesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchGetEffectiveIamPolicies(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def create_feed(
        self,
    ) -> Callable[[asset_service.CreateFeedRequest], asset_service.Feed]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateFeed(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_saved_query(
        self,
    ) -> Callable[[asset_service.CreateSavedQueryRequest], asset_service.SavedQuery]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateSavedQuery(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_feed(
        self,
    ) -> Callable[[asset_service.DeleteFeedRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteFeed(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_saved_query(
        self,
    ) -> Callable[[asset_service.DeleteSavedQueryRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteSavedQuery(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def export_assets(
        self,
    ) -> Callable[[asset_service.ExportAssetsRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ExportAssets(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_feed(self) -> Callable[[asset_service.GetFeedRequest], asset_service.Feed]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetFeed(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_saved_query(
        self,
    ) -> Callable[[asset_service.GetSavedQueryRequest], asset_service.SavedQuery]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetSavedQuery(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_assets(
        self,
    ) -> Callable[[asset_service.ListAssetsRequest], asset_service.ListAssetsResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListAssets(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_feeds(
        self,
    ) -> Callable[[asset_service.ListFeedsRequest], asset_service.ListFeedsResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListFeeds(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_saved_queries(
        self,
    ) -> Callable[
        [asset_service.ListSavedQueriesRequest], asset_service.ListSavedQueriesResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListSavedQueries(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def query_assets(
        self,
    ) -> Callable[
        [asset_service.QueryAssetsRequest], asset_service.QueryAssetsResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._QueryAssets(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def search_all_iam_policies(
        self,
    ) -> Callable[
        [asset_service.SearchAllIamPoliciesRequest],
        asset_service.SearchAllIamPoliciesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._SearchAllIamPolicies(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def search_all_resources(
        self,
    ) -> Callable[
        [asset_service.SearchAllResourcesRequest],
        asset_service.SearchAllResourcesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._SearchAllResources(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_feed(
        self,
    ) -> Callable[[asset_service.UpdateFeedRequest], asset_service.Feed]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateFeed(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_saved_query(
        self,
    ) -> Callable[[asset_service.UpdateSavedQueryRequest], asset_service.SavedQuery]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateSavedQuery(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_operation(self):
        return self._GetOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetOperation(
        _BaseAssetServiceRestTransport._BaseGetOperation, AssetServiceRestStub
    ):
        def __hash__(self):
            return hash("AssetServiceRestTransport.GetOperation")

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
                _BaseAssetServiceRestTransport._BaseGetOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_operation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAssetServiceRestTransport._BaseGetOperation,
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
                    f"Sending request for google.cloud.asset_v1.AssetServiceClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.asset.v1.AssetService",
                        "rpcName": "GetOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AssetServiceRestTransport._GetOperation._get_response(
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
                    "Received response for google.cloud.asset_v1.AssetServiceAsyncClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.asset.v1.AssetService",
                        "rpcName": "GetOperation",
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


__all__ = ("AssetServiceRestTransport",)
