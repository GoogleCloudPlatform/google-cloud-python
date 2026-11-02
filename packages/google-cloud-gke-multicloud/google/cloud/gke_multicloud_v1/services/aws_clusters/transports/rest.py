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
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1, operations_v1, rest_helpers, rest_streaming
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.auth.transport.requests import AuthorizedSession  # type: ignore
from google.longrunning import operations_pb2  # type: ignore
from google.protobuf import json_format
from requests import __version__ as requests_version

from google.cloud.gke_multicloud_v1._compat import transcode_request
from google.cloud.gke_multicloud_v1.types import aws_resources, aws_service

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseAwsClustersRestTransport

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


class AwsClustersRestInterceptor:
    """Interceptor for AwsClusters.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the AwsClustersRestTransport.

    .. code-block:: python
        class MyCustomAwsClustersInterceptor(AwsClustersRestInterceptor):
            def pre_create_aws_cluster(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_aws_cluster(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_aws_node_pool(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_aws_node_pool(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_aws_cluster(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_aws_cluster(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_aws_node_pool(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_aws_node_pool(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_generate_aws_access_token(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_generate_aws_access_token(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_generate_aws_cluster_agent_token(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_generate_aws_cluster_agent_token(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_aws_cluster(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_aws_cluster(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_aws_json_web_keys(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_aws_json_web_keys(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_aws_node_pool(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_aws_node_pool(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_aws_open_id_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_aws_open_id_config(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_aws_server_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_aws_server_config(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_aws_clusters(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_aws_clusters(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_aws_node_pools(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_aws_node_pools(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_rollback_aws_node_pool_update(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_rollback_aws_node_pool_update(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_aws_cluster(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_aws_cluster(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_aws_node_pool(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_aws_node_pool(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = AwsClustersRestTransport(interceptor=MyCustomAwsClustersInterceptor())
        client = AwsClustersClient(transport=transport)


    """

    def pre_create_aws_cluster(
        self,
        request: aws_service.CreateAwsClusterRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        aws_service.CreateAwsClusterRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_aws_cluster

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AwsClusters server.
        """
        return request, metadata

    def post_create_aws_cluster(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_aws_cluster

        DEPRECATED. Please use the `post_create_aws_cluster_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AwsClusters server but before
        it is returned to user code. This `post_create_aws_cluster` interceptor runs
        before the `post_create_aws_cluster_with_metadata` interceptor.
        """
        return response

    def post_create_aws_cluster_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_aws_cluster

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AwsClusters server but before it is returned to user code.

        We recommend only using this `post_create_aws_cluster_with_metadata`
        interceptor in new development instead of the `post_create_aws_cluster` interceptor.
        When both interceptors are used, this `post_create_aws_cluster_with_metadata` interceptor runs after the
        `post_create_aws_cluster` interceptor. The (possibly modified) response returned by
        `post_create_aws_cluster` will be passed to
        `post_create_aws_cluster_with_metadata`.
        """
        return response, metadata

    def pre_create_aws_node_pool(
        self,
        request: aws_service.CreateAwsNodePoolRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        aws_service.CreateAwsNodePoolRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_aws_node_pool

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AwsClusters server.
        """
        return request, metadata

    def post_create_aws_node_pool(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_aws_node_pool

        DEPRECATED. Please use the `post_create_aws_node_pool_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AwsClusters server but before
        it is returned to user code. This `post_create_aws_node_pool` interceptor runs
        before the `post_create_aws_node_pool_with_metadata` interceptor.
        """
        return response

    def post_create_aws_node_pool_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_aws_node_pool

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AwsClusters server but before it is returned to user code.

        We recommend only using this `post_create_aws_node_pool_with_metadata`
        interceptor in new development instead of the `post_create_aws_node_pool` interceptor.
        When both interceptors are used, this `post_create_aws_node_pool_with_metadata` interceptor runs after the
        `post_create_aws_node_pool` interceptor. The (possibly modified) response returned by
        `post_create_aws_node_pool` will be passed to
        `post_create_aws_node_pool_with_metadata`.
        """
        return response, metadata

    def pre_delete_aws_cluster(
        self,
        request: aws_service.DeleteAwsClusterRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        aws_service.DeleteAwsClusterRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_aws_cluster

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AwsClusters server.
        """
        return request, metadata

    def post_delete_aws_cluster(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_aws_cluster

        DEPRECATED. Please use the `post_delete_aws_cluster_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AwsClusters server but before
        it is returned to user code. This `post_delete_aws_cluster` interceptor runs
        before the `post_delete_aws_cluster_with_metadata` interceptor.
        """
        return response

    def post_delete_aws_cluster_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_aws_cluster

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AwsClusters server but before it is returned to user code.

        We recommend only using this `post_delete_aws_cluster_with_metadata`
        interceptor in new development instead of the `post_delete_aws_cluster` interceptor.
        When both interceptors are used, this `post_delete_aws_cluster_with_metadata` interceptor runs after the
        `post_delete_aws_cluster` interceptor. The (possibly modified) response returned by
        `post_delete_aws_cluster` will be passed to
        `post_delete_aws_cluster_with_metadata`.
        """
        return response, metadata

    def pre_delete_aws_node_pool(
        self,
        request: aws_service.DeleteAwsNodePoolRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        aws_service.DeleteAwsNodePoolRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_aws_node_pool

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AwsClusters server.
        """
        return request, metadata

    def post_delete_aws_node_pool(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_aws_node_pool

        DEPRECATED. Please use the `post_delete_aws_node_pool_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AwsClusters server but before
        it is returned to user code. This `post_delete_aws_node_pool` interceptor runs
        before the `post_delete_aws_node_pool_with_metadata` interceptor.
        """
        return response

    def post_delete_aws_node_pool_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_aws_node_pool

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AwsClusters server but before it is returned to user code.

        We recommend only using this `post_delete_aws_node_pool_with_metadata`
        interceptor in new development instead of the `post_delete_aws_node_pool` interceptor.
        When both interceptors are used, this `post_delete_aws_node_pool_with_metadata` interceptor runs after the
        `post_delete_aws_node_pool` interceptor. The (possibly modified) response returned by
        `post_delete_aws_node_pool` will be passed to
        `post_delete_aws_node_pool_with_metadata`.
        """
        return response, metadata

    def pre_generate_aws_access_token(
        self,
        request: aws_service.GenerateAwsAccessTokenRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        aws_service.GenerateAwsAccessTokenRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for generate_aws_access_token

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AwsClusters server.
        """
        return request, metadata

    def post_generate_aws_access_token(
        self, response: aws_service.GenerateAwsAccessTokenResponse
    ) -> aws_service.GenerateAwsAccessTokenResponse:
        """Post-rpc interceptor for generate_aws_access_token

        DEPRECATED. Please use the `post_generate_aws_access_token_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AwsClusters server but before
        it is returned to user code. This `post_generate_aws_access_token` interceptor runs
        before the `post_generate_aws_access_token_with_metadata` interceptor.
        """
        return response

    def post_generate_aws_access_token_with_metadata(
        self,
        response: aws_service.GenerateAwsAccessTokenResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        aws_service.GenerateAwsAccessTokenResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for generate_aws_access_token

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AwsClusters server but before it is returned to user code.

        We recommend only using this `post_generate_aws_access_token_with_metadata`
        interceptor in new development instead of the `post_generate_aws_access_token` interceptor.
        When both interceptors are used, this `post_generate_aws_access_token_with_metadata` interceptor runs after the
        `post_generate_aws_access_token` interceptor. The (possibly modified) response returned by
        `post_generate_aws_access_token` will be passed to
        `post_generate_aws_access_token_with_metadata`.
        """
        return response, metadata

    def pre_generate_aws_cluster_agent_token(
        self,
        request: aws_service.GenerateAwsClusterAgentTokenRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        aws_service.GenerateAwsClusterAgentTokenRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for generate_aws_cluster_agent_token

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AwsClusters server.
        """
        return request, metadata

    def post_generate_aws_cluster_agent_token(
        self, response: aws_service.GenerateAwsClusterAgentTokenResponse
    ) -> aws_service.GenerateAwsClusterAgentTokenResponse:
        """Post-rpc interceptor for generate_aws_cluster_agent_token

        DEPRECATED. Please use the `post_generate_aws_cluster_agent_token_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AwsClusters server but before
        it is returned to user code. This `post_generate_aws_cluster_agent_token` interceptor runs
        before the `post_generate_aws_cluster_agent_token_with_metadata` interceptor.
        """
        return response

    def post_generate_aws_cluster_agent_token_with_metadata(
        self,
        response: aws_service.GenerateAwsClusterAgentTokenResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        aws_service.GenerateAwsClusterAgentTokenResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for generate_aws_cluster_agent_token

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AwsClusters server but before it is returned to user code.

        We recommend only using this `post_generate_aws_cluster_agent_token_with_metadata`
        interceptor in new development instead of the `post_generate_aws_cluster_agent_token` interceptor.
        When both interceptors are used, this `post_generate_aws_cluster_agent_token_with_metadata` interceptor runs after the
        `post_generate_aws_cluster_agent_token` interceptor. The (possibly modified) response returned by
        `post_generate_aws_cluster_agent_token` will be passed to
        `post_generate_aws_cluster_agent_token_with_metadata`.
        """
        return response, metadata

    def pre_get_aws_cluster(
        self,
        request: aws_service.GetAwsClusterRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        aws_service.GetAwsClusterRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_aws_cluster

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AwsClusters server.
        """
        return request, metadata

    def post_get_aws_cluster(
        self, response: aws_resources.AwsCluster
    ) -> aws_resources.AwsCluster:
        """Post-rpc interceptor for get_aws_cluster

        DEPRECATED. Please use the `post_get_aws_cluster_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AwsClusters server but before
        it is returned to user code. This `post_get_aws_cluster` interceptor runs
        before the `post_get_aws_cluster_with_metadata` interceptor.
        """
        return response

    def post_get_aws_cluster_with_metadata(
        self,
        response: aws_resources.AwsCluster,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[aws_resources.AwsCluster, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_aws_cluster

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AwsClusters server but before it is returned to user code.

        We recommend only using this `post_get_aws_cluster_with_metadata`
        interceptor in new development instead of the `post_get_aws_cluster` interceptor.
        When both interceptors are used, this `post_get_aws_cluster_with_metadata` interceptor runs after the
        `post_get_aws_cluster` interceptor. The (possibly modified) response returned by
        `post_get_aws_cluster` will be passed to
        `post_get_aws_cluster_with_metadata`.
        """
        return response, metadata

    def pre_get_aws_json_web_keys(
        self,
        request: aws_service.GetAwsJsonWebKeysRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        aws_service.GetAwsJsonWebKeysRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_aws_json_web_keys

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AwsClusters server.
        """
        return request, metadata

    def post_get_aws_json_web_keys(
        self, response: aws_resources.AwsJsonWebKeys
    ) -> aws_resources.AwsJsonWebKeys:
        """Post-rpc interceptor for get_aws_json_web_keys

        DEPRECATED. Please use the `post_get_aws_json_web_keys_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AwsClusters server but before
        it is returned to user code. This `post_get_aws_json_web_keys` interceptor runs
        before the `post_get_aws_json_web_keys_with_metadata` interceptor.
        """
        return response

    def post_get_aws_json_web_keys_with_metadata(
        self,
        response: aws_resources.AwsJsonWebKeys,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[aws_resources.AwsJsonWebKeys, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_aws_json_web_keys

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AwsClusters server but before it is returned to user code.

        We recommend only using this `post_get_aws_json_web_keys_with_metadata`
        interceptor in new development instead of the `post_get_aws_json_web_keys` interceptor.
        When both interceptors are used, this `post_get_aws_json_web_keys_with_metadata` interceptor runs after the
        `post_get_aws_json_web_keys` interceptor. The (possibly modified) response returned by
        `post_get_aws_json_web_keys` will be passed to
        `post_get_aws_json_web_keys_with_metadata`.
        """
        return response, metadata

    def pre_get_aws_node_pool(
        self,
        request: aws_service.GetAwsNodePoolRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        aws_service.GetAwsNodePoolRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_aws_node_pool

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AwsClusters server.
        """
        return request, metadata

    def post_get_aws_node_pool(
        self, response: aws_resources.AwsNodePool
    ) -> aws_resources.AwsNodePool:
        """Post-rpc interceptor for get_aws_node_pool

        DEPRECATED. Please use the `post_get_aws_node_pool_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AwsClusters server but before
        it is returned to user code. This `post_get_aws_node_pool` interceptor runs
        before the `post_get_aws_node_pool_with_metadata` interceptor.
        """
        return response

    def post_get_aws_node_pool_with_metadata(
        self,
        response: aws_resources.AwsNodePool,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[aws_resources.AwsNodePool, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_aws_node_pool

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AwsClusters server but before it is returned to user code.

        We recommend only using this `post_get_aws_node_pool_with_metadata`
        interceptor in new development instead of the `post_get_aws_node_pool` interceptor.
        When both interceptors are used, this `post_get_aws_node_pool_with_metadata` interceptor runs after the
        `post_get_aws_node_pool` interceptor. The (possibly modified) response returned by
        `post_get_aws_node_pool` will be passed to
        `post_get_aws_node_pool_with_metadata`.
        """
        return response, metadata

    def pre_get_aws_open_id_config(
        self,
        request: aws_service.GetAwsOpenIdConfigRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        aws_service.GetAwsOpenIdConfigRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_aws_open_id_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AwsClusters server.
        """
        return request, metadata

    def post_get_aws_open_id_config(
        self, response: aws_resources.AwsOpenIdConfig
    ) -> aws_resources.AwsOpenIdConfig:
        """Post-rpc interceptor for get_aws_open_id_config

        DEPRECATED. Please use the `post_get_aws_open_id_config_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AwsClusters server but before
        it is returned to user code. This `post_get_aws_open_id_config` interceptor runs
        before the `post_get_aws_open_id_config_with_metadata` interceptor.
        """
        return response

    def post_get_aws_open_id_config_with_metadata(
        self,
        response: aws_resources.AwsOpenIdConfig,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[aws_resources.AwsOpenIdConfig, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_aws_open_id_config

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AwsClusters server but before it is returned to user code.

        We recommend only using this `post_get_aws_open_id_config_with_metadata`
        interceptor in new development instead of the `post_get_aws_open_id_config` interceptor.
        When both interceptors are used, this `post_get_aws_open_id_config_with_metadata` interceptor runs after the
        `post_get_aws_open_id_config` interceptor. The (possibly modified) response returned by
        `post_get_aws_open_id_config` will be passed to
        `post_get_aws_open_id_config_with_metadata`.
        """
        return response, metadata

    def pre_get_aws_server_config(
        self,
        request: aws_service.GetAwsServerConfigRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        aws_service.GetAwsServerConfigRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_aws_server_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AwsClusters server.
        """
        return request, metadata

    def post_get_aws_server_config(
        self, response: aws_resources.AwsServerConfig
    ) -> aws_resources.AwsServerConfig:
        """Post-rpc interceptor for get_aws_server_config

        DEPRECATED. Please use the `post_get_aws_server_config_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AwsClusters server but before
        it is returned to user code. This `post_get_aws_server_config` interceptor runs
        before the `post_get_aws_server_config_with_metadata` interceptor.
        """
        return response

    def post_get_aws_server_config_with_metadata(
        self,
        response: aws_resources.AwsServerConfig,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[aws_resources.AwsServerConfig, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_aws_server_config

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AwsClusters server but before it is returned to user code.

        We recommend only using this `post_get_aws_server_config_with_metadata`
        interceptor in new development instead of the `post_get_aws_server_config` interceptor.
        When both interceptors are used, this `post_get_aws_server_config_with_metadata` interceptor runs after the
        `post_get_aws_server_config` interceptor. The (possibly modified) response returned by
        `post_get_aws_server_config` will be passed to
        `post_get_aws_server_config_with_metadata`.
        """
        return response, metadata

    def pre_list_aws_clusters(
        self,
        request: aws_service.ListAwsClustersRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        aws_service.ListAwsClustersRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_aws_clusters

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AwsClusters server.
        """
        return request, metadata

    def post_list_aws_clusters(
        self, response: aws_service.ListAwsClustersResponse
    ) -> aws_service.ListAwsClustersResponse:
        """Post-rpc interceptor for list_aws_clusters

        DEPRECATED. Please use the `post_list_aws_clusters_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AwsClusters server but before
        it is returned to user code. This `post_list_aws_clusters` interceptor runs
        before the `post_list_aws_clusters_with_metadata` interceptor.
        """
        return response

    def post_list_aws_clusters_with_metadata(
        self,
        response: aws_service.ListAwsClustersResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        aws_service.ListAwsClustersResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_aws_clusters

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AwsClusters server but before it is returned to user code.

        We recommend only using this `post_list_aws_clusters_with_metadata`
        interceptor in new development instead of the `post_list_aws_clusters` interceptor.
        When both interceptors are used, this `post_list_aws_clusters_with_metadata` interceptor runs after the
        `post_list_aws_clusters` interceptor. The (possibly modified) response returned by
        `post_list_aws_clusters` will be passed to
        `post_list_aws_clusters_with_metadata`.
        """
        return response, metadata

    def pre_list_aws_node_pools(
        self,
        request: aws_service.ListAwsNodePoolsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        aws_service.ListAwsNodePoolsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_aws_node_pools

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AwsClusters server.
        """
        return request, metadata

    def post_list_aws_node_pools(
        self, response: aws_service.ListAwsNodePoolsResponse
    ) -> aws_service.ListAwsNodePoolsResponse:
        """Post-rpc interceptor for list_aws_node_pools

        DEPRECATED. Please use the `post_list_aws_node_pools_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AwsClusters server but before
        it is returned to user code. This `post_list_aws_node_pools` interceptor runs
        before the `post_list_aws_node_pools_with_metadata` interceptor.
        """
        return response

    def post_list_aws_node_pools_with_metadata(
        self,
        response: aws_service.ListAwsNodePoolsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        aws_service.ListAwsNodePoolsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_aws_node_pools

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AwsClusters server but before it is returned to user code.

        We recommend only using this `post_list_aws_node_pools_with_metadata`
        interceptor in new development instead of the `post_list_aws_node_pools` interceptor.
        When both interceptors are used, this `post_list_aws_node_pools_with_metadata` interceptor runs after the
        `post_list_aws_node_pools` interceptor. The (possibly modified) response returned by
        `post_list_aws_node_pools` will be passed to
        `post_list_aws_node_pools_with_metadata`.
        """
        return response, metadata

    def pre_rollback_aws_node_pool_update(
        self,
        request: aws_service.RollbackAwsNodePoolUpdateRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        aws_service.RollbackAwsNodePoolUpdateRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for rollback_aws_node_pool_update

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AwsClusters server.
        """
        return request, metadata

    def post_rollback_aws_node_pool_update(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for rollback_aws_node_pool_update

        DEPRECATED. Please use the `post_rollback_aws_node_pool_update_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AwsClusters server but before
        it is returned to user code. This `post_rollback_aws_node_pool_update` interceptor runs
        before the `post_rollback_aws_node_pool_update_with_metadata` interceptor.
        """
        return response

    def post_rollback_aws_node_pool_update_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for rollback_aws_node_pool_update

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AwsClusters server but before it is returned to user code.

        We recommend only using this `post_rollback_aws_node_pool_update_with_metadata`
        interceptor in new development instead of the `post_rollback_aws_node_pool_update` interceptor.
        When both interceptors are used, this `post_rollback_aws_node_pool_update_with_metadata` interceptor runs after the
        `post_rollback_aws_node_pool_update` interceptor. The (possibly modified) response returned by
        `post_rollback_aws_node_pool_update` will be passed to
        `post_rollback_aws_node_pool_update_with_metadata`.
        """
        return response, metadata

    def pre_update_aws_cluster(
        self,
        request: aws_service.UpdateAwsClusterRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        aws_service.UpdateAwsClusterRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_aws_cluster

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AwsClusters server.
        """
        return request, metadata

    def post_update_aws_cluster(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_aws_cluster

        DEPRECATED. Please use the `post_update_aws_cluster_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AwsClusters server but before
        it is returned to user code. This `post_update_aws_cluster` interceptor runs
        before the `post_update_aws_cluster_with_metadata` interceptor.
        """
        return response

    def post_update_aws_cluster_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_aws_cluster

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AwsClusters server but before it is returned to user code.

        We recommend only using this `post_update_aws_cluster_with_metadata`
        interceptor in new development instead of the `post_update_aws_cluster` interceptor.
        When both interceptors are used, this `post_update_aws_cluster_with_metadata` interceptor runs after the
        `post_update_aws_cluster` interceptor. The (possibly modified) response returned by
        `post_update_aws_cluster` will be passed to
        `post_update_aws_cluster_with_metadata`.
        """
        return response, metadata

    def pre_update_aws_node_pool(
        self,
        request: aws_service.UpdateAwsNodePoolRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        aws_service.UpdateAwsNodePoolRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_aws_node_pool

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AwsClusters server.
        """
        return request, metadata

    def post_update_aws_node_pool(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_aws_node_pool

        DEPRECATED. Please use the `post_update_aws_node_pool_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AwsClusters server but before
        it is returned to user code. This `post_update_aws_node_pool` interceptor runs
        before the `post_update_aws_node_pool_with_metadata` interceptor.
        """
        return response

    def post_update_aws_node_pool_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_aws_node_pool

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AwsClusters server but before it is returned to user code.

        We recommend only using this `post_update_aws_node_pool_with_metadata`
        interceptor in new development instead of the `post_update_aws_node_pool` interceptor.
        When both interceptors are used, this `post_update_aws_node_pool_with_metadata` interceptor runs after the
        `post_update_aws_node_pool` interceptor. The (possibly modified) response returned by
        `post_update_aws_node_pool` will be passed to
        `post_update_aws_node_pool_with_metadata`.
        """
        return response, metadata

    def pre_cancel_operation(
        self,
        request: operations_pb2.CancelOperationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        operations_pb2.CancelOperationRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AwsClusters server.
        """
        return request, metadata

    def post_cancel_operation(self, response: None) -> None:
        """Post-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the response
        after it is returned by the AwsClusters server but before
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
        before they are sent to the AwsClusters server.
        """
        return request, metadata

    def post_delete_operation(self, response: None) -> None:
        """Post-rpc interceptor for delete_operation

        Override in a subclass to manipulate the response
        after it is returned by the AwsClusters server but before
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
        before they are sent to the AwsClusters server.
        """
        return request, metadata

    def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the AwsClusters server but before
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
        before they are sent to the AwsClusters server.
        """
        return request, metadata

    def post_list_operations(
        self, response: operations_pb2.ListOperationsResponse
    ) -> operations_pb2.ListOperationsResponse:
        """Post-rpc interceptor for list_operations

        Override in a subclass to manipulate the response
        after it is returned by the AwsClusters server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class AwsClustersRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: AwsClustersRestInterceptor


class AwsClustersRestTransport(_BaseAwsClustersRestTransport):
    """REST backend synchronous transport for AwsClusters.

    The AwsClusters API provides a single centrally managed
    service to create and manage Anthos clusters that run on AWS
    infrastructure.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "gkemulticloud.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[AwsClustersRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        NOTE: This REST transport functionality is currently in a beta
        state (preview). We welcome your feedback via a GitHub issue in
        this library's repository. Thank you!

         Args:
             host (Optional[str]):
                  The hostname to connect to (default: 'gkemulticloud.googleapis.com').
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
             interceptor (Optional[AwsClustersRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or AwsClustersRestInterceptor()
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

    class _CreateAwsCluster(
        _BaseAwsClustersRestTransport._BaseCreateAwsCluster, AwsClustersRestStub
    ):
        def __hash__(self):
            return hash("AwsClustersRestTransport.CreateAwsCluster")

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
            request: aws_service.CreateAwsClusterRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create aws cluster method over HTTP.

            Args:
                request (~.aws_service.CreateAwsClusterRequest):
                    The request object. Request message for ``AwsClusters.CreateAwsCluster``
                method.
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
                _BaseAwsClustersRestTransport._BaseCreateAwsCluster._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_aws_cluster(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAwsClustersRestTransport._BaseCreateAwsCluster,
                    "_BaseCreateAwsCluster__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.gkemulticloud_v1.AwsClustersClient.CreateAwsCluster",
                    extra={
                        "serviceName": "google.cloud.gkemulticloud.v1.AwsClusters",
                        "rpcName": "CreateAwsCluster",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AwsClustersRestTransport._CreateAwsCluster._get_response(
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

            resp = self._interceptor.post_create_aws_cluster(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_aws_cluster_with_metadata(
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
                    "Received response for google.cloud.gkemulticloud_v1.AwsClustersClient.create_aws_cluster",
                    extra={
                        "serviceName": "google.cloud.gkemulticloud.v1.AwsClusters",
                        "rpcName": "CreateAwsCluster",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateAwsNodePool(
        _BaseAwsClustersRestTransport._BaseCreateAwsNodePool, AwsClustersRestStub
    ):
        def __hash__(self):
            return hash("AwsClustersRestTransport.CreateAwsNodePool")

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
            request: aws_service.CreateAwsNodePoolRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create aws node pool method over HTTP.

            Args:
                request (~.aws_service.CreateAwsNodePoolRequest):
                    The request object. Response message for ``AwsClusters.CreateAwsNodePool``
                method.
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
                _BaseAwsClustersRestTransport._BaseCreateAwsNodePool._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_aws_node_pool(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAwsClustersRestTransport._BaseCreateAwsNodePool,
                    "_BaseCreateAwsNodePool__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.gkemulticloud_v1.AwsClustersClient.CreateAwsNodePool",
                    extra={
                        "serviceName": "google.cloud.gkemulticloud.v1.AwsClusters",
                        "rpcName": "CreateAwsNodePool",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AwsClustersRestTransport._CreateAwsNodePool._get_response(
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

            resp = self._interceptor.post_create_aws_node_pool(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_aws_node_pool_with_metadata(
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
                    "Received response for google.cloud.gkemulticloud_v1.AwsClustersClient.create_aws_node_pool",
                    extra={
                        "serviceName": "google.cloud.gkemulticloud.v1.AwsClusters",
                        "rpcName": "CreateAwsNodePool",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteAwsCluster(
        _BaseAwsClustersRestTransport._BaseDeleteAwsCluster, AwsClustersRestStub
    ):
        def __hash__(self):
            return hash("AwsClustersRestTransport.DeleteAwsCluster")

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
            request: aws_service.DeleteAwsClusterRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete aws cluster method over HTTP.

            Args:
                request (~.aws_service.DeleteAwsClusterRequest):
                    The request object. Request message for ``AwsClusters.DeleteAwsCluster``
                method.
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
                _BaseAwsClustersRestTransport._BaseDeleteAwsCluster._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_aws_cluster(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAwsClustersRestTransport._BaseDeleteAwsCluster,
                    "_BaseDeleteAwsCluster__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.gkemulticloud_v1.AwsClustersClient.DeleteAwsCluster",
                    extra={
                        "serviceName": "google.cloud.gkemulticloud.v1.AwsClusters",
                        "rpcName": "DeleteAwsCluster",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AwsClustersRestTransport._DeleteAwsCluster._get_response(
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

            resp = self._interceptor.post_delete_aws_cluster(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_aws_cluster_with_metadata(
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
                    "Received response for google.cloud.gkemulticloud_v1.AwsClustersClient.delete_aws_cluster",
                    extra={
                        "serviceName": "google.cloud.gkemulticloud.v1.AwsClusters",
                        "rpcName": "DeleteAwsCluster",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteAwsNodePool(
        _BaseAwsClustersRestTransport._BaseDeleteAwsNodePool, AwsClustersRestStub
    ):
        def __hash__(self):
            return hash("AwsClustersRestTransport.DeleteAwsNodePool")

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
            request: aws_service.DeleteAwsNodePoolRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete aws node pool method over HTTP.

            Args:
                request (~.aws_service.DeleteAwsNodePoolRequest):
                    The request object. Request message for ``AwsClusters.DeleteAwsNodePool``
                method.
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
                _BaseAwsClustersRestTransport._BaseDeleteAwsNodePool._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_aws_node_pool(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAwsClustersRestTransport._BaseDeleteAwsNodePool,
                    "_BaseDeleteAwsNodePool__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.gkemulticloud_v1.AwsClustersClient.DeleteAwsNodePool",
                    extra={
                        "serviceName": "google.cloud.gkemulticloud.v1.AwsClusters",
                        "rpcName": "DeleteAwsNodePool",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AwsClustersRestTransport._DeleteAwsNodePool._get_response(
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

            resp = self._interceptor.post_delete_aws_node_pool(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_aws_node_pool_with_metadata(
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
                    "Received response for google.cloud.gkemulticloud_v1.AwsClustersClient.delete_aws_node_pool",
                    extra={
                        "serviceName": "google.cloud.gkemulticloud.v1.AwsClusters",
                        "rpcName": "DeleteAwsNodePool",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GenerateAwsAccessToken(
        _BaseAwsClustersRestTransport._BaseGenerateAwsAccessToken, AwsClustersRestStub
    ):
        def __hash__(self):
            return hash("AwsClustersRestTransport.GenerateAwsAccessToken")

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
            request: aws_service.GenerateAwsAccessTokenRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> aws_service.GenerateAwsAccessTokenResponse:
            r"""Call the generate aws access token method over HTTP.

            Args:
                request (~.aws_service.GenerateAwsAccessTokenRequest):
                    The request object. Request message for
                ``AwsClusters.GenerateAwsAccessToken`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.aws_service.GenerateAwsAccessTokenResponse:
                    Response message for
                ``AwsClusters.GenerateAwsAccessToken`` method.

            """

            http_options = _BaseAwsClustersRestTransport._BaseGenerateAwsAccessToken._get_http_options()
            request, metadata = self._interceptor.pre_generate_aws_access_token(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAwsClustersRestTransport._BaseGenerateAwsAccessToken,
                    "_BaseGenerateAwsAccessToken__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.gkemulticloud_v1.AwsClustersClient.GenerateAwsAccessToken",
                    extra={
                        "serviceName": "google.cloud.gkemulticloud.v1.AwsClusters",
                        "rpcName": "GenerateAwsAccessToken",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AwsClustersRestTransport._GenerateAwsAccessToken._get_response(
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
            resp = aws_service.GenerateAwsAccessTokenResponse()
            pb_resp = aws_service.GenerateAwsAccessTokenResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_generate_aws_access_token(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_generate_aws_access_token_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        aws_service.GenerateAwsAccessTokenResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.gkemulticloud_v1.AwsClustersClient.generate_aws_access_token",
                    extra={
                        "serviceName": "google.cloud.gkemulticloud.v1.AwsClusters",
                        "rpcName": "GenerateAwsAccessToken",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GenerateAwsClusterAgentToken(
        _BaseAwsClustersRestTransport._BaseGenerateAwsClusterAgentToken,
        AwsClustersRestStub,
    ):
        def __hash__(self):
            return hash("AwsClustersRestTransport.GenerateAwsClusterAgentToken")

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
            request: aws_service.GenerateAwsClusterAgentTokenRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> aws_service.GenerateAwsClusterAgentTokenResponse:
            r"""Call the generate aws cluster
            agent token method over HTTP.

                Args:
                    request (~.aws_service.GenerateAwsClusterAgentTokenRequest):
                        The request object.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.aws_service.GenerateAwsClusterAgentTokenResponse:

            """

            http_options = _BaseAwsClustersRestTransport._BaseGenerateAwsClusterAgentToken._get_http_options()
            request, metadata = self._interceptor.pre_generate_aws_cluster_agent_token(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAwsClustersRestTransport._BaseGenerateAwsClusterAgentToken,
                    "_BaseGenerateAwsClusterAgentToken__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.gkemulticloud_v1.AwsClustersClient.GenerateAwsClusterAgentToken",
                    extra={
                        "serviceName": "google.cloud.gkemulticloud.v1.AwsClusters",
                        "rpcName": "GenerateAwsClusterAgentToken",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                AwsClustersRestTransport._GenerateAwsClusterAgentToken._get_response(
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
            resp = aws_service.GenerateAwsClusterAgentTokenResponse()
            pb_resp = aws_service.GenerateAwsClusterAgentTokenResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_generate_aws_cluster_agent_token(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_generate_aws_cluster_agent_token_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        aws_service.GenerateAwsClusterAgentTokenResponse.to_json(
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
                    "Received response for google.cloud.gkemulticloud_v1.AwsClustersClient.generate_aws_cluster_agent_token",
                    extra={
                        "serviceName": "google.cloud.gkemulticloud.v1.AwsClusters",
                        "rpcName": "GenerateAwsClusterAgentToken",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetAwsCluster(
        _BaseAwsClustersRestTransport._BaseGetAwsCluster, AwsClustersRestStub
    ):
        def __hash__(self):
            return hash("AwsClustersRestTransport.GetAwsCluster")

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
            request: aws_service.GetAwsClusterRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> aws_resources.AwsCluster:
            r"""Call the get aws cluster method over HTTP.

            Args:
                request (~.aws_service.GetAwsClusterRequest):
                    The request object. Request message for ``AwsClusters.GetAwsCluster``
                method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.aws_resources.AwsCluster:
                    An Anthos cluster running on AWS.
            """

            http_options = (
                _BaseAwsClustersRestTransport._BaseGetAwsCluster._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_aws_cluster(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAwsClustersRestTransport._BaseGetAwsCluster,
                    "_BaseGetAwsCluster__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.gkemulticloud_v1.AwsClustersClient.GetAwsCluster",
                    extra={
                        "serviceName": "google.cloud.gkemulticloud.v1.AwsClusters",
                        "rpcName": "GetAwsCluster",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AwsClustersRestTransport._GetAwsCluster._get_response(
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
            resp = aws_resources.AwsCluster()
            pb_resp = aws_resources.AwsCluster.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_aws_cluster(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_aws_cluster_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = aws_resources.AwsCluster.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.gkemulticloud_v1.AwsClustersClient.get_aws_cluster",
                    extra={
                        "serviceName": "google.cloud.gkemulticloud.v1.AwsClusters",
                        "rpcName": "GetAwsCluster",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetAwsJsonWebKeys(
        _BaseAwsClustersRestTransport._BaseGetAwsJsonWebKeys, AwsClustersRestStub
    ):
        def __hash__(self):
            return hash("AwsClustersRestTransport.GetAwsJsonWebKeys")

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
            request: aws_service.GetAwsJsonWebKeysRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> aws_resources.AwsJsonWebKeys:
            r"""Call the get aws json web keys method over HTTP.

            Args:
                request (~.aws_service.GetAwsJsonWebKeysRequest):
                    The request object. GetAwsJsonWebKeysRequest gets the public component of
                the keys used by the cluster to sign token requests.
                This will be the jwks_uri for the discover document
                returned by getOpenIDConfig. See the OpenID Connect
                Discovery 1.0 specification for details.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.aws_resources.AwsJsonWebKeys:
                    AwsJsonWebKeys is a valid JSON Web
                Key Set as specififed in RFC 7517.

            """

            http_options = (
                _BaseAwsClustersRestTransport._BaseGetAwsJsonWebKeys._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_aws_json_web_keys(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAwsClustersRestTransport._BaseGetAwsJsonWebKeys,
                    "_BaseGetAwsJsonWebKeys__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.gkemulticloud_v1.AwsClustersClient.GetAwsJsonWebKeys",
                    extra={
                        "serviceName": "google.cloud.gkemulticloud.v1.AwsClusters",
                        "rpcName": "GetAwsJsonWebKeys",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AwsClustersRestTransport._GetAwsJsonWebKeys._get_response(
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
            resp = aws_resources.AwsJsonWebKeys()
            pb_resp = aws_resources.AwsJsonWebKeys.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_aws_json_web_keys(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_aws_json_web_keys_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = aws_resources.AwsJsonWebKeys.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.gkemulticloud_v1.AwsClustersClient.get_aws_json_web_keys",
                    extra={
                        "serviceName": "google.cloud.gkemulticloud.v1.AwsClusters",
                        "rpcName": "GetAwsJsonWebKeys",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetAwsNodePool(
        _BaseAwsClustersRestTransport._BaseGetAwsNodePool, AwsClustersRestStub
    ):
        def __hash__(self):
            return hash("AwsClustersRestTransport.GetAwsNodePool")

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
            request: aws_service.GetAwsNodePoolRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> aws_resources.AwsNodePool:
            r"""Call the get aws node pool method over HTTP.

            Args:
                request (~.aws_service.GetAwsNodePoolRequest):
                    The request object. Request message for ``AwsClusters.GetAwsNodePool``
                method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.aws_resources.AwsNodePool:
                    An Anthos node pool running on AWS.
            """

            http_options = (
                _BaseAwsClustersRestTransport._BaseGetAwsNodePool._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_aws_node_pool(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAwsClustersRestTransport._BaseGetAwsNodePool,
                    "_BaseGetAwsNodePool__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.gkemulticloud_v1.AwsClustersClient.GetAwsNodePool",
                    extra={
                        "serviceName": "google.cloud.gkemulticloud.v1.AwsClusters",
                        "rpcName": "GetAwsNodePool",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AwsClustersRestTransport._GetAwsNodePool._get_response(
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
            resp = aws_resources.AwsNodePool()
            pb_resp = aws_resources.AwsNodePool.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_aws_node_pool(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_aws_node_pool_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = aws_resources.AwsNodePool.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.gkemulticloud_v1.AwsClustersClient.get_aws_node_pool",
                    extra={
                        "serviceName": "google.cloud.gkemulticloud.v1.AwsClusters",
                        "rpcName": "GetAwsNodePool",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetAwsOpenIdConfig(
        _BaseAwsClustersRestTransport._BaseGetAwsOpenIdConfig, AwsClustersRestStub
    ):
        def __hash__(self):
            return hash("AwsClustersRestTransport.GetAwsOpenIdConfig")

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
            request: aws_service.GetAwsOpenIdConfigRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> aws_resources.AwsOpenIdConfig:
            r"""Call the get aws open id config method over HTTP.

            Args:
                request (~.aws_service.GetAwsOpenIdConfigRequest):
                    The request object. GetAwsOpenIdConfigRequest gets the
                OIDC discovery document for the cluster.
                See the OpenID Connect Discovery 1.0
                specification for details.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.aws_resources.AwsOpenIdConfig:
                    AwsOpenIdConfig is an OIDC discovery
                document for the cluster. See the OpenID
                Connect Discovery 1.0 specification for
                details.

            """

            http_options = _BaseAwsClustersRestTransport._BaseGetAwsOpenIdConfig._get_http_options()
            request, metadata = self._interceptor.pre_get_aws_open_id_config(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAwsClustersRestTransport._BaseGetAwsOpenIdConfig,
                    "_BaseGetAwsOpenIdConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.gkemulticloud_v1.AwsClustersClient.GetAwsOpenIdConfig",
                    extra={
                        "serviceName": "google.cloud.gkemulticloud.v1.AwsClusters",
                        "rpcName": "GetAwsOpenIdConfig",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AwsClustersRestTransport._GetAwsOpenIdConfig._get_response(
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
            resp = aws_resources.AwsOpenIdConfig()
            pb_resp = aws_resources.AwsOpenIdConfig.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_aws_open_id_config(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_aws_open_id_config_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = aws_resources.AwsOpenIdConfig.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.gkemulticloud_v1.AwsClustersClient.get_aws_open_id_config",
                    extra={
                        "serviceName": "google.cloud.gkemulticloud.v1.AwsClusters",
                        "rpcName": "GetAwsOpenIdConfig",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetAwsServerConfig(
        _BaseAwsClustersRestTransport._BaseGetAwsServerConfig, AwsClustersRestStub
    ):
        def __hash__(self):
            return hash("AwsClustersRestTransport.GetAwsServerConfig")

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
            request: aws_service.GetAwsServerConfigRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> aws_resources.AwsServerConfig:
            r"""Call the get aws server config method over HTTP.

            Args:
                request (~.aws_service.GetAwsServerConfigRequest):
                    The request object. GetAwsServerConfigRequest gets the
                server config of GKE cluster on AWS.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.aws_resources.AwsServerConfig:
                    AwsServerConfig is the configuration
                of GKE cluster on AWS.

            """

            http_options = _BaseAwsClustersRestTransport._BaseGetAwsServerConfig._get_http_options()
            request, metadata = self._interceptor.pre_get_aws_server_config(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAwsClustersRestTransport._BaseGetAwsServerConfig,
                    "_BaseGetAwsServerConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.gkemulticloud_v1.AwsClustersClient.GetAwsServerConfig",
                    extra={
                        "serviceName": "google.cloud.gkemulticloud.v1.AwsClusters",
                        "rpcName": "GetAwsServerConfig",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AwsClustersRestTransport._GetAwsServerConfig._get_response(
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
            resp = aws_resources.AwsServerConfig()
            pb_resp = aws_resources.AwsServerConfig.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_aws_server_config(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_aws_server_config_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = aws_resources.AwsServerConfig.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.gkemulticloud_v1.AwsClustersClient.get_aws_server_config",
                    extra={
                        "serviceName": "google.cloud.gkemulticloud.v1.AwsClusters",
                        "rpcName": "GetAwsServerConfig",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListAwsClusters(
        _BaseAwsClustersRestTransport._BaseListAwsClusters, AwsClustersRestStub
    ):
        def __hash__(self):
            return hash("AwsClustersRestTransport.ListAwsClusters")

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
            request: aws_service.ListAwsClustersRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> aws_service.ListAwsClustersResponse:
            r"""Call the list aws clusters method over HTTP.

            Args:
                request (~.aws_service.ListAwsClustersRequest):
                    The request object. Request message for ``AwsClusters.ListAwsClusters``
                method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.aws_service.ListAwsClustersResponse:
                    Response message for ``AwsClusters.ListAwsClusters``
                method.

            """

            http_options = (
                _BaseAwsClustersRestTransport._BaseListAwsClusters._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_aws_clusters(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAwsClustersRestTransport._BaseListAwsClusters,
                    "_BaseListAwsClusters__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.gkemulticloud_v1.AwsClustersClient.ListAwsClusters",
                    extra={
                        "serviceName": "google.cloud.gkemulticloud.v1.AwsClusters",
                        "rpcName": "ListAwsClusters",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AwsClustersRestTransport._ListAwsClusters._get_response(
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
            resp = aws_service.ListAwsClustersResponse()
            pb_resp = aws_service.ListAwsClustersResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_aws_clusters(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_aws_clusters_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = aws_service.ListAwsClustersResponse.to_json(
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
                    "Received response for google.cloud.gkemulticloud_v1.AwsClustersClient.list_aws_clusters",
                    extra={
                        "serviceName": "google.cloud.gkemulticloud.v1.AwsClusters",
                        "rpcName": "ListAwsClusters",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListAwsNodePools(
        _BaseAwsClustersRestTransport._BaseListAwsNodePools, AwsClustersRestStub
    ):
        def __hash__(self):
            return hash("AwsClustersRestTransport.ListAwsNodePools")

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
            request: aws_service.ListAwsNodePoolsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> aws_service.ListAwsNodePoolsResponse:
            r"""Call the list aws node pools method over HTTP.

            Args:
                request (~.aws_service.ListAwsNodePoolsRequest):
                    The request object. Request message for ``AwsClusters.ListAwsNodePools``
                method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.aws_service.ListAwsNodePoolsResponse:
                    Response message for ``AwsClusters.ListAwsNodePools``
                method.

            """

            http_options = (
                _BaseAwsClustersRestTransport._BaseListAwsNodePools._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_aws_node_pools(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAwsClustersRestTransport._BaseListAwsNodePools,
                    "_BaseListAwsNodePools__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.gkemulticloud_v1.AwsClustersClient.ListAwsNodePools",
                    extra={
                        "serviceName": "google.cloud.gkemulticloud.v1.AwsClusters",
                        "rpcName": "ListAwsNodePools",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AwsClustersRestTransport._ListAwsNodePools._get_response(
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
            resp = aws_service.ListAwsNodePoolsResponse()
            pb_resp = aws_service.ListAwsNodePoolsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_aws_node_pools(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_aws_node_pools_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = aws_service.ListAwsNodePoolsResponse.to_json(
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
                    "Received response for google.cloud.gkemulticloud_v1.AwsClustersClient.list_aws_node_pools",
                    extra={
                        "serviceName": "google.cloud.gkemulticloud.v1.AwsClusters",
                        "rpcName": "ListAwsNodePools",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _RollbackAwsNodePoolUpdate(
        _BaseAwsClustersRestTransport._BaseRollbackAwsNodePoolUpdate,
        AwsClustersRestStub,
    ):
        def __hash__(self):
            return hash("AwsClustersRestTransport.RollbackAwsNodePoolUpdate")

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
            request: aws_service.RollbackAwsNodePoolUpdateRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the rollback aws node pool
            update method over HTTP.

                Args:
                    request (~.aws_service.RollbackAwsNodePoolUpdateRequest):
                        The request object. Request message for
                    ``AwsClusters.RollbackAwsNodePoolUpdate`` method.
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

            http_options = _BaseAwsClustersRestTransport._BaseRollbackAwsNodePoolUpdate._get_http_options()
            request, metadata = self._interceptor.pre_rollback_aws_node_pool_update(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAwsClustersRestTransport._BaseRollbackAwsNodePoolUpdate,
                    "_BaseRollbackAwsNodePoolUpdate__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.gkemulticloud_v1.AwsClustersClient.RollbackAwsNodePoolUpdate",
                    extra={
                        "serviceName": "google.cloud.gkemulticloud.v1.AwsClusters",
                        "rpcName": "RollbackAwsNodePoolUpdate",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                AwsClustersRestTransport._RollbackAwsNodePoolUpdate._get_response(
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

            resp = self._interceptor.post_rollback_aws_node_pool_update(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_rollback_aws_node_pool_update_with_metadata(
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
                    "Received response for google.cloud.gkemulticloud_v1.AwsClustersClient.rollback_aws_node_pool_update",
                    extra={
                        "serviceName": "google.cloud.gkemulticloud.v1.AwsClusters",
                        "rpcName": "RollbackAwsNodePoolUpdate",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateAwsCluster(
        _BaseAwsClustersRestTransport._BaseUpdateAwsCluster, AwsClustersRestStub
    ):
        def __hash__(self):
            return hash("AwsClustersRestTransport.UpdateAwsCluster")

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
            request: aws_service.UpdateAwsClusterRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update aws cluster method over HTTP.

            Args:
                request (~.aws_service.UpdateAwsClusterRequest):
                    The request object. Request message for ``AwsClusters.UpdateAwsCluster``
                method.
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
                _BaseAwsClustersRestTransport._BaseUpdateAwsCluster._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_aws_cluster(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAwsClustersRestTransport._BaseUpdateAwsCluster,
                    "_BaseUpdateAwsCluster__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.gkemulticloud_v1.AwsClustersClient.UpdateAwsCluster",
                    extra={
                        "serviceName": "google.cloud.gkemulticloud.v1.AwsClusters",
                        "rpcName": "UpdateAwsCluster",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AwsClustersRestTransport._UpdateAwsCluster._get_response(
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

            resp = self._interceptor.post_update_aws_cluster(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_aws_cluster_with_metadata(
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
                    "Received response for google.cloud.gkemulticloud_v1.AwsClustersClient.update_aws_cluster",
                    extra={
                        "serviceName": "google.cloud.gkemulticloud.v1.AwsClusters",
                        "rpcName": "UpdateAwsCluster",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateAwsNodePool(
        _BaseAwsClustersRestTransport._BaseUpdateAwsNodePool, AwsClustersRestStub
    ):
        def __hash__(self):
            return hash("AwsClustersRestTransport.UpdateAwsNodePool")

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
            request: aws_service.UpdateAwsNodePoolRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update aws node pool method over HTTP.

            Args:
                request (~.aws_service.UpdateAwsNodePoolRequest):
                    The request object. Request message for ``AwsClusters.UpdateAwsNodePool``
                method.
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
                _BaseAwsClustersRestTransport._BaseUpdateAwsNodePool._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_aws_node_pool(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAwsClustersRestTransport._BaseUpdateAwsNodePool,
                    "_BaseUpdateAwsNodePool__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.gkemulticloud_v1.AwsClustersClient.UpdateAwsNodePool",
                    extra={
                        "serviceName": "google.cloud.gkemulticloud.v1.AwsClusters",
                        "rpcName": "UpdateAwsNodePool",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AwsClustersRestTransport._UpdateAwsNodePool._get_response(
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

            resp = self._interceptor.post_update_aws_node_pool(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_aws_node_pool_with_metadata(
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
                    "Received response for google.cloud.gkemulticloud_v1.AwsClustersClient.update_aws_node_pool",
                    extra={
                        "serviceName": "google.cloud.gkemulticloud.v1.AwsClusters",
                        "rpcName": "UpdateAwsNodePool",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def create_aws_cluster(
        self,
    ) -> Callable[[aws_service.CreateAwsClusterRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateAwsCluster(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_aws_node_pool(
        self,
    ) -> Callable[[aws_service.CreateAwsNodePoolRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateAwsNodePool(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_aws_cluster(
        self,
    ) -> Callable[[aws_service.DeleteAwsClusterRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteAwsCluster(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_aws_node_pool(
        self,
    ) -> Callable[[aws_service.DeleteAwsNodePoolRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteAwsNodePool(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def generate_aws_access_token(
        self,
    ) -> Callable[
        [aws_service.GenerateAwsAccessTokenRequest],
        aws_service.GenerateAwsAccessTokenResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GenerateAwsAccessToken(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def generate_aws_cluster_agent_token(
        self,
    ) -> Callable[
        [aws_service.GenerateAwsClusterAgentTokenRequest],
        aws_service.GenerateAwsClusterAgentTokenResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GenerateAwsClusterAgentToken(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def get_aws_cluster(
        self,
    ) -> Callable[[aws_service.GetAwsClusterRequest], aws_resources.AwsCluster]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetAwsCluster(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_aws_json_web_keys(
        self,
    ) -> Callable[[aws_service.GetAwsJsonWebKeysRequest], aws_resources.AwsJsonWebKeys]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetAwsJsonWebKeys(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_aws_node_pool(
        self,
    ) -> Callable[[aws_service.GetAwsNodePoolRequest], aws_resources.AwsNodePool]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetAwsNodePool(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_aws_open_id_config(
        self,
    ) -> Callable[
        [aws_service.GetAwsOpenIdConfigRequest], aws_resources.AwsOpenIdConfig
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetAwsOpenIdConfig(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_aws_server_config(
        self,
    ) -> Callable[
        [aws_service.GetAwsServerConfigRequest], aws_resources.AwsServerConfig
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetAwsServerConfig(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_aws_clusters(
        self,
    ) -> Callable[
        [aws_service.ListAwsClustersRequest], aws_service.ListAwsClustersResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListAwsClusters(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_aws_node_pools(
        self,
    ) -> Callable[
        [aws_service.ListAwsNodePoolsRequest], aws_service.ListAwsNodePoolsResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListAwsNodePools(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def rollback_aws_node_pool_update(
        self,
    ) -> Callable[
        [aws_service.RollbackAwsNodePoolUpdateRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._RollbackAwsNodePoolUpdate(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def update_aws_cluster(
        self,
    ) -> Callable[[aws_service.UpdateAwsClusterRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateAwsCluster(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_aws_node_pool(
        self,
    ) -> Callable[[aws_service.UpdateAwsNodePoolRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateAwsNodePool(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def cancel_operation(self):
        return self._CancelOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _CancelOperation(
        _BaseAwsClustersRestTransport._BaseCancelOperation, AwsClustersRestStub
    ):
        def __hash__(self):
            return hash("AwsClustersRestTransport.CancelOperation")

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
                _BaseAwsClustersRestTransport._BaseCancelOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_cancel_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAwsClustersRestTransport._BaseCancelOperation,
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
                    f"Sending request for google.cloud.gkemulticloud_v1.AwsClustersClient.CancelOperation",
                    extra={
                        "serviceName": "google.cloud.gkemulticloud.v1.AwsClusters",
                        "rpcName": "CancelOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AwsClustersRestTransport._CancelOperation._get_response(
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
        _BaseAwsClustersRestTransport._BaseDeleteOperation, AwsClustersRestStub
    ):
        def __hash__(self):
            return hash("AwsClustersRestTransport.DeleteOperation")

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
                _BaseAwsClustersRestTransport._BaseDeleteOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAwsClustersRestTransport._BaseDeleteOperation,
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
                    f"Sending request for google.cloud.gkemulticloud_v1.AwsClustersClient.DeleteOperation",
                    extra={
                        "serviceName": "google.cloud.gkemulticloud.v1.AwsClusters",
                        "rpcName": "DeleteOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AwsClustersRestTransport._DeleteOperation._get_response(
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
        _BaseAwsClustersRestTransport._BaseGetOperation, AwsClustersRestStub
    ):
        def __hash__(self):
            return hash("AwsClustersRestTransport.GetOperation")

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
                _BaseAwsClustersRestTransport._BaseGetOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_operation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAwsClustersRestTransport._BaseGetOperation,
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
                    f"Sending request for google.cloud.gkemulticloud_v1.AwsClustersClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.gkemulticloud.v1.AwsClusters",
                        "rpcName": "GetOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AwsClustersRestTransport._GetOperation._get_response(
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
                    "Received response for google.cloud.gkemulticloud_v1.AwsClustersAsyncClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.gkemulticloud.v1.AwsClusters",
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
        _BaseAwsClustersRestTransport._BaseListOperations, AwsClustersRestStub
    ):
        def __hash__(self):
            return hash("AwsClustersRestTransport.ListOperations")

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
                _BaseAwsClustersRestTransport._BaseListOperations._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_operations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAwsClustersRestTransport._BaseListOperations,
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
                    f"Sending request for google.cloud.gkemulticloud_v1.AwsClustersClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.gkemulticloud.v1.AwsClusters",
                        "rpcName": "ListOperations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AwsClustersRestTransport._ListOperations._get_response(
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
                    "Received response for google.cloud.gkemulticloud_v1.AwsClustersAsyncClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.gkemulticloud.v1.AwsClusters",
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


__all__ = ("AwsClustersRestTransport",)
