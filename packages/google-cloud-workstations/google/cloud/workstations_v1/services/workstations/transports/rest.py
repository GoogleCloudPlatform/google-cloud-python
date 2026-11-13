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
from google.cloud.location import locations_pb2  # type: ignore
from google.iam.v1 import (
    iam_policy_pb2,  # type: ignore
    policy_pb2,  # type: ignore
)
from google.longrunning import operations_pb2  # type: ignore
from google.protobuf import json_format
from requests import __version__ as requests_version

from google.cloud.workstations_v1._compat import transcode_request
from google.cloud.workstations_v1.types import workstations

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseWorkstationsRestTransport

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


class WorkstationsRestInterceptor:
    """Interceptor for Workstations.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the WorkstationsRestTransport.

    .. code-block:: python
        class MyCustomWorkstationsInterceptor(WorkstationsRestInterceptor):
            def pre_create_workstation(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_workstation(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_workstation_cluster(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_workstation_cluster(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_workstation_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_workstation_config(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_workstation(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_workstation(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_workstation_cluster(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_workstation_cluster(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_workstation_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_workstation_config(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_generate_access_token(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_generate_access_token(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_workstation(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_workstation(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_workstation_cluster(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_workstation_cluster(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_workstation_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_workstation_config(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_usable_workstation_configs(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_usable_workstation_configs(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_usable_workstations(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_usable_workstations(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_workstation_clusters(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_workstation_clusters(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_workstation_configs(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_workstation_configs(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_workstations(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_workstations(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_start_workstation(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_start_workstation(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_stop_workstation(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_stop_workstation(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_workstation(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_workstation(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_workstation_cluster(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_workstation_cluster(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_workstation_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_workstation_config(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = WorkstationsRestTransport(interceptor=MyCustomWorkstationsInterceptor())
        client = WorkstationsClient(transport=transport)


    """

    def pre_create_workstation(
        self,
        request: workstations.CreateWorkstationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        workstations.CreateWorkstationRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_workstation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Workstations server.
        """
        return request, metadata

    def post_create_workstation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_workstation

        DEPRECATED. Please use the `post_create_workstation_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Workstations server but before
        it is returned to user code. This `post_create_workstation` interceptor runs
        before the `post_create_workstation_with_metadata` interceptor.
        """
        return response

    def post_create_workstation_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_workstation

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Workstations server but before it is returned to user code.

        We recommend only using this `post_create_workstation_with_metadata`
        interceptor in new development instead of the `post_create_workstation` interceptor.
        When both interceptors are used, this `post_create_workstation_with_metadata` interceptor runs after the
        `post_create_workstation` interceptor. The (possibly modified) response returned by
        `post_create_workstation` will be passed to
        `post_create_workstation_with_metadata`.
        """
        return response, metadata

    def pre_create_workstation_cluster(
        self,
        request: workstations.CreateWorkstationClusterRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        workstations.CreateWorkstationClusterRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_workstation_cluster

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Workstations server.
        """
        return request, metadata

    def post_create_workstation_cluster(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_workstation_cluster

        DEPRECATED. Please use the `post_create_workstation_cluster_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Workstations server but before
        it is returned to user code. This `post_create_workstation_cluster` interceptor runs
        before the `post_create_workstation_cluster_with_metadata` interceptor.
        """
        return response

    def post_create_workstation_cluster_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_workstation_cluster

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Workstations server but before it is returned to user code.

        We recommend only using this `post_create_workstation_cluster_with_metadata`
        interceptor in new development instead of the `post_create_workstation_cluster` interceptor.
        When both interceptors are used, this `post_create_workstation_cluster_with_metadata` interceptor runs after the
        `post_create_workstation_cluster` interceptor. The (possibly modified) response returned by
        `post_create_workstation_cluster` will be passed to
        `post_create_workstation_cluster_with_metadata`.
        """
        return response, metadata

    def pre_create_workstation_config(
        self,
        request: workstations.CreateWorkstationConfigRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        workstations.CreateWorkstationConfigRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_workstation_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Workstations server.
        """
        return request, metadata

    def post_create_workstation_config(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_workstation_config

        DEPRECATED. Please use the `post_create_workstation_config_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Workstations server but before
        it is returned to user code. This `post_create_workstation_config` interceptor runs
        before the `post_create_workstation_config_with_metadata` interceptor.
        """
        return response

    def post_create_workstation_config_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_workstation_config

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Workstations server but before it is returned to user code.

        We recommend only using this `post_create_workstation_config_with_metadata`
        interceptor in new development instead of the `post_create_workstation_config` interceptor.
        When both interceptors are used, this `post_create_workstation_config_with_metadata` interceptor runs after the
        `post_create_workstation_config` interceptor. The (possibly modified) response returned by
        `post_create_workstation_config` will be passed to
        `post_create_workstation_config_with_metadata`.
        """
        return response, metadata

    def pre_delete_workstation(
        self,
        request: workstations.DeleteWorkstationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        workstations.DeleteWorkstationRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_workstation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Workstations server.
        """
        return request, metadata

    def post_delete_workstation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_workstation

        DEPRECATED. Please use the `post_delete_workstation_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Workstations server but before
        it is returned to user code. This `post_delete_workstation` interceptor runs
        before the `post_delete_workstation_with_metadata` interceptor.
        """
        return response

    def post_delete_workstation_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_workstation

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Workstations server but before it is returned to user code.

        We recommend only using this `post_delete_workstation_with_metadata`
        interceptor in new development instead of the `post_delete_workstation` interceptor.
        When both interceptors are used, this `post_delete_workstation_with_metadata` interceptor runs after the
        `post_delete_workstation` interceptor. The (possibly modified) response returned by
        `post_delete_workstation` will be passed to
        `post_delete_workstation_with_metadata`.
        """
        return response, metadata

    def pre_delete_workstation_cluster(
        self,
        request: workstations.DeleteWorkstationClusterRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        workstations.DeleteWorkstationClusterRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_workstation_cluster

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Workstations server.
        """
        return request, metadata

    def post_delete_workstation_cluster(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_workstation_cluster

        DEPRECATED. Please use the `post_delete_workstation_cluster_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Workstations server but before
        it is returned to user code. This `post_delete_workstation_cluster` interceptor runs
        before the `post_delete_workstation_cluster_with_metadata` interceptor.
        """
        return response

    def post_delete_workstation_cluster_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_workstation_cluster

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Workstations server but before it is returned to user code.

        We recommend only using this `post_delete_workstation_cluster_with_metadata`
        interceptor in new development instead of the `post_delete_workstation_cluster` interceptor.
        When both interceptors are used, this `post_delete_workstation_cluster_with_metadata` interceptor runs after the
        `post_delete_workstation_cluster` interceptor. The (possibly modified) response returned by
        `post_delete_workstation_cluster` will be passed to
        `post_delete_workstation_cluster_with_metadata`.
        """
        return response, metadata

    def pre_delete_workstation_config(
        self,
        request: workstations.DeleteWorkstationConfigRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        workstations.DeleteWorkstationConfigRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_workstation_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Workstations server.
        """
        return request, metadata

    def post_delete_workstation_config(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_workstation_config

        DEPRECATED. Please use the `post_delete_workstation_config_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Workstations server but before
        it is returned to user code. This `post_delete_workstation_config` interceptor runs
        before the `post_delete_workstation_config_with_metadata` interceptor.
        """
        return response

    def post_delete_workstation_config_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_workstation_config

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Workstations server but before it is returned to user code.

        We recommend only using this `post_delete_workstation_config_with_metadata`
        interceptor in new development instead of the `post_delete_workstation_config` interceptor.
        When both interceptors are used, this `post_delete_workstation_config_with_metadata` interceptor runs after the
        `post_delete_workstation_config` interceptor. The (possibly modified) response returned by
        `post_delete_workstation_config` will be passed to
        `post_delete_workstation_config_with_metadata`.
        """
        return response, metadata

    def pre_generate_access_token(
        self,
        request: workstations.GenerateAccessTokenRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        workstations.GenerateAccessTokenRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for generate_access_token

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Workstations server.
        """
        return request, metadata

    def post_generate_access_token(
        self, response: workstations.GenerateAccessTokenResponse
    ) -> workstations.GenerateAccessTokenResponse:
        """Post-rpc interceptor for generate_access_token

        DEPRECATED. Please use the `post_generate_access_token_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Workstations server but before
        it is returned to user code. This `post_generate_access_token` interceptor runs
        before the `post_generate_access_token_with_metadata` interceptor.
        """
        return response

    def post_generate_access_token_with_metadata(
        self,
        response: workstations.GenerateAccessTokenResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        workstations.GenerateAccessTokenResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for generate_access_token

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Workstations server but before it is returned to user code.

        We recommend only using this `post_generate_access_token_with_metadata`
        interceptor in new development instead of the `post_generate_access_token` interceptor.
        When both interceptors are used, this `post_generate_access_token_with_metadata` interceptor runs after the
        `post_generate_access_token` interceptor. The (possibly modified) response returned by
        `post_generate_access_token` will be passed to
        `post_generate_access_token_with_metadata`.
        """
        return response, metadata

    def pre_get_workstation(
        self,
        request: workstations.GetWorkstationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        workstations.GetWorkstationRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_workstation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Workstations server.
        """
        return request, metadata

    def post_get_workstation(
        self, response: workstations.Workstation
    ) -> workstations.Workstation:
        """Post-rpc interceptor for get_workstation

        DEPRECATED. Please use the `post_get_workstation_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Workstations server but before
        it is returned to user code. This `post_get_workstation` interceptor runs
        before the `post_get_workstation_with_metadata` interceptor.
        """
        return response

    def post_get_workstation_with_metadata(
        self,
        response: workstations.Workstation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[workstations.Workstation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_workstation

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Workstations server but before it is returned to user code.

        We recommend only using this `post_get_workstation_with_metadata`
        interceptor in new development instead of the `post_get_workstation` interceptor.
        When both interceptors are used, this `post_get_workstation_with_metadata` interceptor runs after the
        `post_get_workstation` interceptor. The (possibly modified) response returned by
        `post_get_workstation` will be passed to
        `post_get_workstation_with_metadata`.
        """
        return response, metadata

    def pre_get_workstation_cluster(
        self,
        request: workstations.GetWorkstationClusterRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        workstations.GetWorkstationClusterRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_workstation_cluster

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Workstations server.
        """
        return request, metadata

    def post_get_workstation_cluster(
        self, response: workstations.WorkstationCluster
    ) -> workstations.WorkstationCluster:
        """Post-rpc interceptor for get_workstation_cluster

        DEPRECATED. Please use the `post_get_workstation_cluster_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Workstations server but before
        it is returned to user code. This `post_get_workstation_cluster` interceptor runs
        before the `post_get_workstation_cluster_with_metadata` interceptor.
        """
        return response

    def post_get_workstation_cluster_with_metadata(
        self,
        response: workstations.WorkstationCluster,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        workstations.WorkstationCluster, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for get_workstation_cluster

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Workstations server but before it is returned to user code.

        We recommend only using this `post_get_workstation_cluster_with_metadata`
        interceptor in new development instead of the `post_get_workstation_cluster` interceptor.
        When both interceptors are used, this `post_get_workstation_cluster_with_metadata` interceptor runs after the
        `post_get_workstation_cluster` interceptor. The (possibly modified) response returned by
        `post_get_workstation_cluster` will be passed to
        `post_get_workstation_cluster_with_metadata`.
        """
        return response, metadata

    def pre_get_workstation_config(
        self,
        request: workstations.GetWorkstationConfigRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        workstations.GetWorkstationConfigRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_workstation_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Workstations server.
        """
        return request, metadata

    def post_get_workstation_config(
        self, response: workstations.WorkstationConfig
    ) -> workstations.WorkstationConfig:
        """Post-rpc interceptor for get_workstation_config

        DEPRECATED. Please use the `post_get_workstation_config_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Workstations server but before
        it is returned to user code. This `post_get_workstation_config` interceptor runs
        before the `post_get_workstation_config_with_metadata` interceptor.
        """
        return response

    def post_get_workstation_config_with_metadata(
        self,
        response: workstations.WorkstationConfig,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[workstations.WorkstationConfig, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_workstation_config

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Workstations server but before it is returned to user code.

        We recommend only using this `post_get_workstation_config_with_metadata`
        interceptor in new development instead of the `post_get_workstation_config` interceptor.
        When both interceptors are used, this `post_get_workstation_config_with_metadata` interceptor runs after the
        `post_get_workstation_config` interceptor. The (possibly modified) response returned by
        `post_get_workstation_config` will be passed to
        `post_get_workstation_config_with_metadata`.
        """
        return response, metadata

    def pre_list_usable_workstation_configs(
        self,
        request: workstations.ListUsableWorkstationConfigsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        workstations.ListUsableWorkstationConfigsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_usable_workstation_configs

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Workstations server.
        """
        return request, metadata

    def post_list_usable_workstation_configs(
        self, response: workstations.ListUsableWorkstationConfigsResponse
    ) -> workstations.ListUsableWorkstationConfigsResponse:
        """Post-rpc interceptor for list_usable_workstation_configs

        DEPRECATED. Please use the `post_list_usable_workstation_configs_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Workstations server but before
        it is returned to user code. This `post_list_usable_workstation_configs` interceptor runs
        before the `post_list_usable_workstation_configs_with_metadata` interceptor.
        """
        return response

    def post_list_usable_workstation_configs_with_metadata(
        self,
        response: workstations.ListUsableWorkstationConfigsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        workstations.ListUsableWorkstationConfigsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_usable_workstation_configs

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Workstations server but before it is returned to user code.

        We recommend only using this `post_list_usable_workstation_configs_with_metadata`
        interceptor in new development instead of the `post_list_usable_workstation_configs` interceptor.
        When both interceptors are used, this `post_list_usable_workstation_configs_with_metadata` interceptor runs after the
        `post_list_usable_workstation_configs` interceptor. The (possibly modified) response returned by
        `post_list_usable_workstation_configs` will be passed to
        `post_list_usable_workstation_configs_with_metadata`.
        """
        return response, metadata

    def pre_list_usable_workstations(
        self,
        request: workstations.ListUsableWorkstationsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        workstations.ListUsableWorkstationsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_usable_workstations

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Workstations server.
        """
        return request, metadata

    def post_list_usable_workstations(
        self, response: workstations.ListUsableWorkstationsResponse
    ) -> workstations.ListUsableWorkstationsResponse:
        """Post-rpc interceptor for list_usable_workstations

        DEPRECATED. Please use the `post_list_usable_workstations_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Workstations server but before
        it is returned to user code. This `post_list_usable_workstations` interceptor runs
        before the `post_list_usable_workstations_with_metadata` interceptor.
        """
        return response

    def post_list_usable_workstations_with_metadata(
        self,
        response: workstations.ListUsableWorkstationsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        workstations.ListUsableWorkstationsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_usable_workstations

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Workstations server but before it is returned to user code.

        We recommend only using this `post_list_usable_workstations_with_metadata`
        interceptor in new development instead of the `post_list_usable_workstations` interceptor.
        When both interceptors are used, this `post_list_usable_workstations_with_metadata` interceptor runs after the
        `post_list_usable_workstations` interceptor. The (possibly modified) response returned by
        `post_list_usable_workstations` will be passed to
        `post_list_usable_workstations_with_metadata`.
        """
        return response, metadata

    def pre_list_workstation_clusters(
        self,
        request: workstations.ListWorkstationClustersRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        workstations.ListWorkstationClustersRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_workstation_clusters

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Workstations server.
        """
        return request, metadata

    def post_list_workstation_clusters(
        self, response: workstations.ListWorkstationClustersResponse
    ) -> workstations.ListWorkstationClustersResponse:
        """Post-rpc interceptor for list_workstation_clusters

        DEPRECATED. Please use the `post_list_workstation_clusters_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Workstations server but before
        it is returned to user code. This `post_list_workstation_clusters` interceptor runs
        before the `post_list_workstation_clusters_with_metadata` interceptor.
        """
        return response

    def post_list_workstation_clusters_with_metadata(
        self,
        response: workstations.ListWorkstationClustersResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        workstations.ListWorkstationClustersResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_workstation_clusters

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Workstations server but before it is returned to user code.

        We recommend only using this `post_list_workstation_clusters_with_metadata`
        interceptor in new development instead of the `post_list_workstation_clusters` interceptor.
        When both interceptors are used, this `post_list_workstation_clusters_with_metadata` interceptor runs after the
        `post_list_workstation_clusters` interceptor. The (possibly modified) response returned by
        `post_list_workstation_clusters` will be passed to
        `post_list_workstation_clusters_with_metadata`.
        """
        return response, metadata

    def pre_list_workstation_configs(
        self,
        request: workstations.ListWorkstationConfigsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        workstations.ListWorkstationConfigsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_workstation_configs

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Workstations server.
        """
        return request, metadata

    def post_list_workstation_configs(
        self, response: workstations.ListWorkstationConfigsResponse
    ) -> workstations.ListWorkstationConfigsResponse:
        """Post-rpc interceptor for list_workstation_configs

        DEPRECATED. Please use the `post_list_workstation_configs_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Workstations server but before
        it is returned to user code. This `post_list_workstation_configs` interceptor runs
        before the `post_list_workstation_configs_with_metadata` interceptor.
        """
        return response

    def post_list_workstation_configs_with_metadata(
        self,
        response: workstations.ListWorkstationConfigsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        workstations.ListWorkstationConfigsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_workstation_configs

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Workstations server but before it is returned to user code.

        We recommend only using this `post_list_workstation_configs_with_metadata`
        interceptor in new development instead of the `post_list_workstation_configs` interceptor.
        When both interceptors are used, this `post_list_workstation_configs_with_metadata` interceptor runs after the
        `post_list_workstation_configs` interceptor. The (possibly modified) response returned by
        `post_list_workstation_configs` will be passed to
        `post_list_workstation_configs_with_metadata`.
        """
        return response, metadata

    def pre_list_workstations(
        self,
        request: workstations.ListWorkstationsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        workstations.ListWorkstationsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_workstations

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Workstations server.
        """
        return request, metadata

    def post_list_workstations(
        self, response: workstations.ListWorkstationsResponse
    ) -> workstations.ListWorkstationsResponse:
        """Post-rpc interceptor for list_workstations

        DEPRECATED. Please use the `post_list_workstations_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Workstations server but before
        it is returned to user code. This `post_list_workstations` interceptor runs
        before the `post_list_workstations_with_metadata` interceptor.
        """
        return response

    def post_list_workstations_with_metadata(
        self,
        response: workstations.ListWorkstationsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        workstations.ListWorkstationsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_workstations

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Workstations server but before it is returned to user code.

        We recommend only using this `post_list_workstations_with_metadata`
        interceptor in new development instead of the `post_list_workstations` interceptor.
        When both interceptors are used, this `post_list_workstations_with_metadata` interceptor runs after the
        `post_list_workstations` interceptor. The (possibly modified) response returned by
        `post_list_workstations` will be passed to
        `post_list_workstations_with_metadata`.
        """
        return response, metadata

    def pre_start_workstation(
        self,
        request: workstations.StartWorkstationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        workstations.StartWorkstationRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for start_workstation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Workstations server.
        """
        return request, metadata

    def post_start_workstation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for start_workstation

        DEPRECATED. Please use the `post_start_workstation_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Workstations server but before
        it is returned to user code. This `post_start_workstation` interceptor runs
        before the `post_start_workstation_with_metadata` interceptor.
        """
        return response

    def post_start_workstation_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for start_workstation

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Workstations server but before it is returned to user code.

        We recommend only using this `post_start_workstation_with_metadata`
        interceptor in new development instead of the `post_start_workstation` interceptor.
        When both interceptors are used, this `post_start_workstation_with_metadata` interceptor runs after the
        `post_start_workstation` interceptor. The (possibly modified) response returned by
        `post_start_workstation` will be passed to
        `post_start_workstation_with_metadata`.
        """
        return response, metadata

    def pre_stop_workstation(
        self,
        request: workstations.StopWorkstationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        workstations.StopWorkstationRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for stop_workstation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Workstations server.
        """
        return request, metadata

    def post_stop_workstation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for stop_workstation

        DEPRECATED. Please use the `post_stop_workstation_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Workstations server but before
        it is returned to user code. This `post_stop_workstation` interceptor runs
        before the `post_stop_workstation_with_metadata` interceptor.
        """
        return response

    def post_stop_workstation_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for stop_workstation

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Workstations server but before it is returned to user code.

        We recommend only using this `post_stop_workstation_with_metadata`
        interceptor in new development instead of the `post_stop_workstation` interceptor.
        When both interceptors are used, this `post_stop_workstation_with_metadata` interceptor runs after the
        `post_stop_workstation` interceptor. The (possibly modified) response returned by
        `post_stop_workstation` will be passed to
        `post_stop_workstation_with_metadata`.
        """
        return response, metadata

    def pre_update_workstation(
        self,
        request: workstations.UpdateWorkstationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        workstations.UpdateWorkstationRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_workstation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Workstations server.
        """
        return request, metadata

    def post_update_workstation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_workstation

        DEPRECATED. Please use the `post_update_workstation_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Workstations server but before
        it is returned to user code. This `post_update_workstation` interceptor runs
        before the `post_update_workstation_with_metadata` interceptor.
        """
        return response

    def post_update_workstation_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_workstation

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Workstations server but before it is returned to user code.

        We recommend only using this `post_update_workstation_with_metadata`
        interceptor in new development instead of the `post_update_workstation` interceptor.
        When both interceptors are used, this `post_update_workstation_with_metadata` interceptor runs after the
        `post_update_workstation` interceptor. The (possibly modified) response returned by
        `post_update_workstation` will be passed to
        `post_update_workstation_with_metadata`.
        """
        return response, metadata

    def pre_update_workstation_cluster(
        self,
        request: workstations.UpdateWorkstationClusterRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        workstations.UpdateWorkstationClusterRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_workstation_cluster

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Workstations server.
        """
        return request, metadata

    def post_update_workstation_cluster(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_workstation_cluster

        DEPRECATED. Please use the `post_update_workstation_cluster_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Workstations server but before
        it is returned to user code. This `post_update_workstation_cluster` interceptor runs
        before the `post_update_workstation_cluster_with_metadata` interceptor.
        """
        return response

    def post_update_workstation_cluster_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_workstation_cluster

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Workstations server but before it is returned to user code.

        We recommend only using this `post_update_workstation_cluster_with_metadata`
        interceptor in new development instead of the `post_update_workstation_cluster` interceptor.
        When both interceptors are used, this `post_update_workstation_cluster_with_metadata` interceptor runs after the
        `post_update_workstation_cluster` interceptor. The (possibly modified) response returned by
        `post_update_workstation_cluster` will be passed to
        `post_update_workstation_cluster_with_metadata`.
        """
        return response, metadata

    def pre_update_workstation_config(
        self,
        request: workstations.UpdateWorkstationConfigRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        workstations.UpdateWorkstationConfigRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_workstation_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Workstations server.
        """
        return request, metadata

    def post_update_workstation_config(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_workstation_config

        DEPRECATED. Please use the `post_update_workstation_config_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Workstations server but before
        it is returned to user code. This `post_update_workstation_config` interceptor runs
        before the `post_update_workstation_config_with_metadata` interceptor.
        """
        return response

    def post_update_workstation_config_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_workstation_config

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Workstations server but before it is returned to user code.

        We recommend only using this `post_update_workstation_config_with_metadata`
        interceptor in new development instead of the `post_update_workstation_config` interceptor.
        When both interceptors are used, this `post_update_workstation_config_with_metadata` interceptor runs after the
        `post_update_workstation_config` interceptor. The (possibly modified) response returned by
        `post_update_workstation_config` will be passed to
        `post_update_workstation_config_with_metadata`.
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
        before they are sent to the Workstations server.
        """
        return request, metadata

    def post_get_iam_policy(self, response: policy_pb2.Policy) -> policy_pb2.Policy:
        """Post-rpc interceptor for get_iam_policy

        Override in a subclass to manipulate the response
        after it is returned by the Workstations server but before
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
        before they are sent to the Workstations server.
        """
        return request, metadata

    def post_set_iam_policy(self, response: policy_pb2.Policy) -> policy_pb2.Policy:
        """Post-rpc interceptor for set_iam_policy

        Override in a subclass to manipulate the response
        after it is returned by the Workstations server but before
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
        before they are sent to the Workstations server.
        """
        return request, metadata

    def post_test_iam_permissions(
        self, response: iam_policy_pb2.TestIamPermissionsResponse
    ) -> iam_policy_pb2.TestIamPermissionsResponse:
        """Post-rpc interceptor for test_iam_permissions

        Override in a subclass to manipulate the response
        after it is returned by the Workstations server but before
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
        before they are sent to the Workstations server.
        """
        return request, metadata

    def post_cancel_operation(self, response: None) -> None:
        """Post-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the response
        after it is returned by the Workstations server but before
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
        before they are sent to the Workstations server.
        """
        return request, metadata

    def post_delete_operation(self, response: None) -> None:
        """Post-rpc interceptor for delete_operation

        Override in a subclass to manipulate the response
        after it is returned by the Workstations server but before
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
        before they are sent to the Workstations server.
        """
        return request, metadata

    def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the Workstations server but before
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
        before they are sent to the Workstations server.
        """
        return request, metadata

    def post_list_operations(
        self, response: operations_pb2.ListOperationsResponse
    ) -> operations_pb2.ListOperationsResponse:
        """Post-rpc interceptor for list_operations

        Override in a subclass to manipulate the response
        after it is returned by the Workstations server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class WorkstationsRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: WorkstationsRestInterceptor


class WorkstationsRestTransport(_BaseWorkstationsRestTransport):
    """REST backend synchronous transport for Workstations.

    Service for interacting with Cloud Workstations.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "workstations.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[WorkstationsRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'workstations.googleapis.com').
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
            interceptor (Optional[WorkstationsRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or WorkstationsRestInterceptor()
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

    class _CreateWorkstation(
        _BaseWorkstationsRestTransport._BaseCreateWorkstation, WorkstationsRestStub
    ):
        def __hash__(self):
            return hash("WorkstationsRestTransport.CreateWorkstation")

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
            request: workstations.CreateWorkstationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create workstation method over HTTP.

            Args:
                request (~.workstations.CreateWorkstationRequest):
                    The request object. Message for creating a
                CreateWorkstation.
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

            http_options = _BaseWorkstationsRestTransport._BaseCreateWorkstation._get_http_options()
            request, metadata = self._interceptor.pre_create_workstation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseWorkstationsRestTransport._BaseCreateWorkstation,
                    "_BaseCreateWorkstation__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.workstations_v1.WorkstationsClient.CreateWorkstation",
                    extra={
                        "serviceName": "google.cloud.workstations.v1.Workstations",
                        "rpcName": "CreateWorkstation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = WorkstationsRestTransport._CreateWorkstation._get_response(
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

            resp = self._interceptor.post_create_workstation(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_workstation_with_metadata(
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
                    "Received response for google.cloud.workstations_v1.WorkstationsClient.create_workstation",
                    extra={
                        "serviceName": "google.cloud.workstations.v1.Workstations",
                        "rpcName": "CreateWorkstation",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateWorkstationCluster(
        _BaseWorkstationsRestTransport._BaseCreateWorkstationCluster,
        WorkstationsRestStub,
    ):
        def __hash__(self):
            return hash("WorkstationsRestTransport.CreateWorkstationCluster")

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
            request: workstations.CreateWorkstationClusterRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create workstation
            cluster method over HTTP.

                Args:
                    request (~.workstations.CreateWorkstationClusterRequest):
                        The request object. Message for creating a
                    CreateWorkstationCluster.
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

            http_options = _BaseWorkstationsRestTransport._BaseCreateWorkstationCluster._get_http_options()
            request, metadata = self._interceptor.pre_create_workstation_cluster(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseWorkstationsRestTransport._BaseCreateWorkstationCluster,
                    "_BaseCreateWorkstationCluster__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.workstations_v1.WorkstationsClient.CreateWorkstationCluster",
                    extra={
                        "serviceName": "google.cloud.workstations.v1.Workstations",
                        "rpcName": "CreateWorkstationCluster",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                WorkstationsRestTransport._CreateWorkstationCluster._get_response(
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

            resp = self._interceptor.post_create_workstation_cluster(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_workstation_cluster_with_metadata(
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
                    "Received response for google.cloud.workstations_v1.WorkstationsClient.create_workstation_cluster",
                    extra={
                        "serviceName": "google.cloud.workstations.v1.Workstations",
                        "rpcName": "CreateWorkstationCluster",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateWorkstationConfig(
        _BaseWorkstationsRestTransport._BaseCreateWorkstationConfig,
        WorkstationsRestStub,
    ):
        def __hash__(self):
            return hash("WorkstationsRestTransport.CreateWorkstationConfig")

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
            request: workstations.CreateWorkstationConfigRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create workstation config method over HTTP.

            Args:
                request (~.workstations.CreateWorkstationConfigRequest):
                    The request object. Message for creating a
                CreateWorkstationConfig.
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

            http_options = _BaseWorkstationsRestTransport._BaseCreateWorkstationConfig._get_http_options()
            request, metadata = self._interceptor.pre_create_workstation_config(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseWorkstationsRestTransport._BaseCreateWorkstationConfig,
                    "_BaseCreateWorkstationConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.workstations_v1.WorkstationsClient.CreateWorkstationConfig",
                    extra={
                        "serviceName": "google.cloud.workstations.v1.Workstations",
                        "rpcName": "CreateWorkstationConfig",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = WorkstationsRestTransport._CreateWorkstationConfig._get_response(
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

            resp = self._interceptor.post_create_workstation_config(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_workstation_config_with_metadata(
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
                    "Received response for google.cloud.workstations_v1.WorkstationsClient.create_workstation_config",
                    extra={
                        "serviceName": "google.cloud.workstations.v1.Workstations",
                        "rpcName": "CreateWorkstationConfig",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteWorkstation(
        _BaseWorkstationsRestTransport._BaseDeleteWorkstation, WorkstationsRestStub
    ):
        def __hash__(self):
            return hash("WorkstationsRestTransport.DeleteWorkstation")

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
            request: workstations.DeleteWorkstationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete workstation method over HTTP.

            Args:
                request (~.workstations.DeleteWorkstationRequest):
                    The request object. Request message for
                DeleteWorkstation.
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

            http_options = _BaseWorkstationsRestTransport._BaseDeleteWorkstation._get_http_options()
            request, metadata = self._interceptor.pre_delete_workstation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseWorkstationsRestTransport._BaseDeleteWorkstation,
                    "_BaseDeleteWorkstation__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.workstations_v1.WorkstationsClient.DeleteWorkstation",
                    extra={
                        "serviceName": "google.cloud.workstations.v1.Workstations",
                        "rpcName": "DeleteWorkstation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = WorkstationsRestTransport._DeleteWorkstation._get_response(
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

            resp = self._interceptor.post_delete_workstation(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_workstation_with_metadata(
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
                    "Received response for google.cloud.workstations_v1.WorkstationsClient.delete_workstation",
                    extra={
                        "serviceName": "google.cloud.workstations.v1.Workstations",
                        "rpcName": "DeleteWorkstation",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteWorkstationCluster(
        _BaseWorkstationsRestTransport._BaseDeleteWorkstationCluster,
        WorkstationsRestStub,
    ):
        def __hash__(self):
            return hash("WorkstationsRestTransport.DeleteWorkstationCluster")

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
            request: workstations.DeleteWorkstationClusterRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete workstation
            cluster method over HTTP.

                Args:
                    request (~.workstations.DeleteWorkstationClusterRequest):
                        The request object. Message for deleting a workstation
                    cluster.
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

            http_options = _BaseWorkstationsRestTransport._BaseDeleteWorkstationCluster._get_http_options()
            request, metadata = self._interceptor.pre_delete_workstation_cluster(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseWorkstationsRestTransport._BaseDeleteWorkstationCluster,
                    "_BaseDeleteWorkstationCluster__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.workstations_v1.WorkstationsClient.DeleteWorkstationCluster",
                    extra={
                        "serviceName": "google.cloud.workstations.v1.Workstations",
                        "rpcName": "DeleteWorkstationCluster",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                WorkstationsRestTransport._DeleteWorkstationCluster._get_response(
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

            resp = self._interceptor.post_delete_workstation_cluster(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_workstation_cluster_with_metadata(
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
                    "Received response for google.cloud.workstations_v1.WorkstationsClient.delete_workstation_cluster",
                    extra={
                        "serviceName": "google.cloud.workstations.v1.Workstations",
                        "rpcName": "DeleteWorkstationCluster",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteWorkstationConfig(
        _BaseWorkstationsRestTransport._BaseDeleteWorkstationConfig,
        WorkstationsRestStub,
    ):
        def __hash__(self):
            return hash("WorkstationsRestTransport.DeleteWorkstationConfig")

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
            request: workstations.DeleteWorkstationConfigRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete workstation config method over HTTP.

            Args:
                request (~.workstations.DeleteWorkstationConfigRequest):
                    The request object. Message for deleting a workstation
                configuration.
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

            http_options = _BaseWorkstationsRestTransport._BaseDeleteWorkstationConfig._get_http_options()
            request, metadata = self._interceptor.pre_delete_workstation_config(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseWorkstationsRestTransport._BaseDeleteWorkstationConfig,
                    "_BaseDeleteWorkstationConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.workstations_v1.WorkstationsClient.DeleteWorkstationConfig",
                    extra={
                        "serviceName": "google.cloud.workstations.v1.Workstations",
                        "rpcName": "DeleteWorkstationConfig",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = WorkstationsRestTransport._DeleteWorkstationConfig._get_response(
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

            resp = self._interceptor.post_delete_workstation_config(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_workstation_config_with_metadata(
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
                    "Received response for google.cloud.workstations_v1.WorkstationsClient.delete_workstation_config",
                    extra={
                        "serviceName": "google.cloud.workstations.v1.Workstations",
                        "rpcName": "DeleteWorkstationConfig",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GenerateAccessToken(
        _BaseWorkstationsRestTransport._BaseGenerateAccessToken, WorkstationsRestStub
    ):
        def __hash__(self):
            return hash("WorkstationsRestTransport.GenerateAccessToken")

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
            request: workstations.GenerateAccessTokenRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> workstations.GenerateAccessTokenResponse:
            r"""Call the generate access token method over HTTP.

            Args:
                request (~.workstations.GenerateAccessTokenRequest):
                    The request object. Request message for
                GenerateAccessToken.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.workstations.GenerateAccessTokenResponse:
                    Response message for
                GenerateAccessToken.

            """

            http_options = _BaseWorkstationsRestTransport._BaseGenerateAccessToken._get_http_options()
            request, metadata = self._interceptor.pre_generate_access_token(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseWorkstationsRestTransport._BaseGenerateAccessToken,
                    "_BaseGenerateAccessToken__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.workstations_v1.WorkstationsClient.GenerateAccessToken",
                    extra={
                        "serviceName": "google.cloud.workstations.v1.Workstations",
                        "rpcName": "GenerateAccessToken",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = WorkstationsRestTransport._GenerateAccessToken._get_response(
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
            resp = workstations.GenerateAccessTokenResponse()
            pb_resp = workstations.GenerateAccessTokenResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_generate_access_token(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_generate_access_token_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = workstations.GenerateAccessTokenResponse.to_json(
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
                    "Received response for google.cloud.workstations_v1.WorkstationsClient.generate_access_token",
                    extra={
                        "serviceName": "google.cloud.workstations.v1.Workstations",
                        "rpcName": "GenerateAccessToken",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetWorkstation(
        _BaseWorkstationsRestTransport._BaseGetWorkstation, WorkstationsRestStub
    ):
        def __hash__(self):
            return hash("WorkstationsRestTransport.GetWorkstation")

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
            request: workstations.GetWorkstationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> workstations.Workstation:
            r"""Call the get workstation method over HTTP.

            Args:
                request (~.workstations.GetWorkstationRequest):
                    The request object. Request message for GetWorkstation.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.workstations.Workstation:
                    A single instance of a developer
                workstation with its own persistent
                storage.

            """

            http_options = (
                _BaseWorkstationsRestTransport._BaseGetWorkstation._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_workstation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseWorkstationsRestTransport._BaseGetWorkstation,
                    "_BaseGetWorkstation__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.workstations_v1.WorkstationsClient.GetWorkstation",
                    extra={
                        "serviceName": "google.cloud.workstations.v1.Workstations",
                        "rpcName": "GetWorkstation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = WorkstationsRestTransport._GetWorkstation._get_response(
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
            resp = workstations.Workstation()
            pb_resp = workstations.Workstation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_workstation(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_workstation_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = workstations.Workstation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.workstations_v1.WorkstationsClient.get_workstation",
                    extra={
                        "serviceName": "google.cloud.workstations.v1.Workstations",
                        "rpcName": "GetWorkstation",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetWorkstationCluster(
        _BaseWorkstationsRestTransport._BaseGetWorkstationCluster, WorkstationsRestStub
    ):
        def __hash__(self):
            return hash("WorkstationsRestTransport.GetWorkstationCluster")

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
            request: workstations.GetWorkstationClusterRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> workstations.WorkstationCluster:
            r"""Call the get workstation cluster method over HTTP.

            Args:
                request (~.workstations.GetWorkstationClusterRequest):
                    The request object. Request message for
                GetWorkstationCluster.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.workstations.WorkstationCluster:
                    A workstation cluster resource in the
                Cloud Workstations API.
                Defines a group of workstations in a
                particular region and the VPC network
                they're attached to.

            """

            http_options = _BaseWorkstationsRestTransport._BaseGetWorkstationCluster._get_http_options()
            request, metadata = self._interceptor.pre_get_workstation_cluster(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseWorkstationsRestTransport._BaseGetWorkstationCluster,
                    "_BaseGetWorkstationCluster__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.workstations_v1.WorkstationsClient.GetWorkstationCluster",
                    extra={
                        "serviceName": "google.cloud.workstations.v1.Workstations",
                        "rpcName": "GetWorkstationCluster",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = WorkstationsRestTransport._GetWorkstationCluster._get_response(
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
            resp = workstations.WorkstationCluster()
            pb_resp = workstations.WorkstationCluster.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_workstation_cluster(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_workstation_cluster_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = workstations.WorkstationCluster.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.workstations_v1.WorkstationsClient.get_workstation_cluster",
                    extra={
                        "serviceName": "google.cloud.workstations.v1.Workstations",
                        "rpcName": "GetWorkstationCluster",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetWorkstationConfig(
        _BaseWorkstationsRestTransport._BaseGetWorkstationConfig, WorkstationsRestStub
    ):
        def __hash__(self):
            return hash("WorkstationsRestTransport.GetWorkstationConfig")

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
            request: workstations.GetWorkstationConfigRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> workstations.WorkstationConfig:
            r"""Call the get workstation config method over HTTP.

            Args:
                request (~.workstations.GetWorkstationConfigRequest):
                    The request object. Request message for
                GetWorkstationConfig.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.workstations.WorkstationConfig:
                    A workstation configuration resource in the Cloud
                Workstations API.

                Workstation configurations act as templates for
                workstations. The workstation configuration defines
                details such as the workstation virtual machine (VM)
                instance type, persistent storage, container image
                defining environment, which IDE or Code Editor to use,
                and more. Administrators and platform teams can also use
                `Identity and Access Management
                (IAM) <https://cloud.google.com/iam/docs/overview>`__
                rules to grant access to teams or to individual
                developers.

            """

            http_options = _BaseWorkstationsRestTransport._BaseGetWorkstationConfig._get_http_options()
            request, metadata = self._interceptor.pre_get_workstation_config(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseWorkstationsRestTransport._BaseGetWorkstationConfig,
                    "_BaseGetWorkstationConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.workstations_v1.WorkstationsClient.GetWorkstationConfig",
                    extra={
                        "serviceName": "google.cloud.workstations.v1.Workstations",
                        "rpcName": "GetWorkstationConfig",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = WorkstationsRestTransport._GetWorkstationConfig._get_response(
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
            resp = workstations.WorkstationConfig()
            pb_resp = workstations.WorkstationConfig.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_workstation_config(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_workstation_config_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = workstations.WorkstationConfig.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.workstations_v1.WorkstationsClient.get_workstation_config",
                    extra={
                        "serviceName": "google.cloud.workstations.v1.Workstations",
                        "rpcName": "GetWorkstationConfig",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListUsableWorkstationConfigs(
        _BaseWorkstationsRestTransport._BaseListUsableWorkstationConfigs,
        WorkstationsRestStub,
    ):
        def __hash__(self):
            return hash("WorkstationsRestTransport.ListUsableWorkstationConfigs")

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
            request: workstations.ListUsableWorkstationConfigsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> workstations.ListUsableWorkstationConfigsResponse:
            r"""Call the list usable workstation
            configs method over HTTP.

                Args:
                    request (~.workstations.ListUsableWorkstationConfigsRequest):
                        The request object. Request message for
                    ListUsableWorkstationConfigs.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.workstations.ListUsableWorkstationConfigsResponse:
                        Response message for
                    ListUsableWorkstationConfigs.

            """

            http_options = _BaseWorkstationsRestTransport._BaseListUsableWorkstationConfigs._get_http_options()
            request, metadata = self._interceptor.pre_list_usable_workstation_configs(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseWorkstationsRestTransport._BaseListUsableWorkstationConfigs,
                    "_BaseListUsableWorkstationConfigs__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.workstations_v1.WorkstationsClient.ListUsableWorkstationConfigs",
                    extra={
                        "serviceName": "google.cloud.workstations.v1.Workstations",
                        "rpcName": "ListUsableWorkstationConfigs",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                WorkstationsRestTransport._ListUsableWorkstationConfigs._get_response(
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
            resp = workstations.ListUsableWorkstationConfigsResponse()
            pb_resp = workstations.ListUsableWorkstationConfigsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_usable_workstation_configs(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_list_usable_workstation_configs_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        workstations.ListUsableWorkstationConfigsResponse.to_json(
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
                    "Received response for google.cloud.workstations_v1.WorkstationsClient.list_usable_workstation_configs",
                    extra={
                        "serviceName": "google.cloud.workstations.v1.Workstations",
                        "rpcName": "ListUsableWorkstationConfigs",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListUsableWorkstations(
        _BaseWorkstationsRestTransport._BaseListUsableWorkstations, WorkstationsRestStub
    ):
        def __hash__(self):
            return hash("WorkstationsRestTransport.ListUsableWorkstations")

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
            request: workstations.ListUsableWorkstationsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> workstations.ListUsableWorkstationsResponse:
            r"""Call the list usable workstations method over HTTP.

            Args:
                request (~.workstations.ListUsableWorkstationsRequest):
                    The request object. Request message for
                ListUsableWorkstations.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.workstations.ListUsableWorkstationsResponse:
                    Response message for
                ListUsableWorkstations.

            """

            http_options = _BaseWorkstationsRestTransport._BaseListUsableWorkstations._get_http_options()
            request, metadata = self._interceptor.pre_list_usable_workstations(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseWorkstationsRestTransport._BaseListUsableWorkstations,
                    "_BaseListUsableWorkstations__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.workstations_v1.WorkstationsClient.ListUsableWorkstations",
                    extra={
                        "serviceName": "google.cloud.workstations.v1.Workstations",
                        "rpcName": "ListUsableWorkstations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = WorkstationsRestTransport._ListUsableWorkstations._get_response(
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
            resp = workstations.ListUsableWorkstationsResponse()
            pb_resp = workstations.ListUsableWorkstationsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_usable_workstations(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_usable_workstations_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        workstations.ListUsableWorkstationsResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.workstations_v1.WorkstationsClient.list_usable_workstations",
                    extra={
                        "serviceName": "google.cloud.workstations.v1.Workstations",
                        "rpcName": "ListUsableWorkstations",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListWorkstationClusters(
        _BaseWorkstationsRestTransport._BaseListWorkstationClusters,
        WorkstationsRestStub,
    ):
        def __hash__(self):
            return hash("WorkstationsRestTransport.ListWorkstationClusters")

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
            request: workstations.ListWorkstationClustersRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> workstations.ListWorkstationClustersResponse:
            r"""Call the list workstation clusters method over HTTP.

            Args:
                request (~.workstations.ListWorkstationClustersRequest):
                    The request object. Request message for
                ListWorkstationClusters.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.workstations.ListWorkstationClustersResponse:
                    Response message for
                ListWorkstationClusters.

            """

            http_options = _BaseWorkstationsRestTransport._BaseListWorkstationClusters._get_http_options()
            request, metadata = self._interceptor.pre_list_workstation_clusters(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseWorkstationsRestTransport._BaseListWorkstationClusters,
                    "_BaseListWorkstationClusters__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.workstations_v1.WorkstationsClient.ListWorkstationClusters",
                    extra={
                        "serviceName": "google.cloud.workstations.v1.Workstations",
                        "rpcName": "ListWorkstationClusters",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = WorkstationsRestTransport._ListWorkstationClusters._get_response(
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
            resp = workstations.ListWorkstationClustersResponse()
            pb_resp = workstations.ListWorkstationClustersResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_workstation_clusters(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_workstation_clusters_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        workstations.ListWorkstationClustersResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.workstations_v1.WorkstationsClient.list_workstation_clusters",
                    extra={
                        "serviceName": "google.cloud.workstations.v1.Workstations",
                        "rpcName": "ListWorkstationClusters",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListWorkstationConfigs(
        _BaseWorkstationsRestTransport._BaseListWorkstationConfigs, WorkstationsRestStub
    ):
        def __hash__(self):
            return hash("WorkstationsRestTransport.ListWorkstationConfigs")

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
            request: workstations.ListWorkstationConfigsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> workstations.ListWorkstationConfigsResponse:
            r"""Call the list workstation configs method over HTTP.

            Args:
                request (~.workstations.ListWorkstationConfigsRequest):
                    The request object. Request message for
                ListWorkstationConfigs.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.workstations.ListWorkstationConfigsResponse:
                    Response message for
                ListWorkstationConfigs.

            """

            http_options = _BaseWorkstationsRestTransport._BaseListWorkstationConfigs._get_http_options()
            request, metadata = self._interceptor.pre_list_workstation_configs(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseWorkstationsRestTransport._BaseListWorkstationConfigs,
                    "_BaseListWorkstationConfigs__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.workstations_v1.WorkstationsClient.ListWorkstationConfigs",
                    extra={
                        "serviceName": "google.cloud.workstations.v1.Workstations",
                        "rpcName": "ListWorkstationConfigs",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = WorkstationsRestTransport._ListWorkstationConfigs._get_response(
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
            resp = workstations.ListWorkstationConfigsResponse()
            pb_resp = workstations.ListWorkstationConfigsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_workstation_configs(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_workstation_configs_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        workstations.ListWorkstationConfigsResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.workstations_v1.WorkstationsClient.list_workstation_configs",
                    extra={
                        "serviceName": "google.cloud.workstations.v1.Workstations",
                        "rpcName": "ListWorkstationConfigs",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListWorkstations(
        _BaseWorkstationsRestTransport._BaseListWorkstations, WorkstationsRestStub
    ):
        def __hash__(self):
            return hash("WorkstationsRestTransport.ListWorkstations")

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
            request: workstations.ListWorkstationsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> workstations.ListWorkstationsResponse:
            r"""Call the list workstations method over HTTP.

            Args:
                request (~.workstations.ListWorkstationsRequest):
                    The request object. Request message for ListWorkstations.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.workstations.ListWorkstationsResponse:
                    Response message for
                ListWorkstations.

            """

            http_options = (
                _BaseWorkstationsRestTransport._BaseListWorkstations._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_workstations(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseWorkstationsRestTransport._BaseListWorkstations,
                    "_BaseListWorkstations__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.workstations_v1.WorkstationsClient.ListWorkstations",
                    extra={
                        "serviceName": "google.cloud.workstations.v1.Workstations",
                        "rpcName": "ListWorkstations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = WorkstationsRestTransport._ListWorkstations._get_response(
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
            resp = workstations.ListWorkstationsResponse()
            pb_resp = workstations.ListWorkstationsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_workstations(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_workstations_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = workstations.ListWorkstationsResponse.to_json(
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
                    "Received response for google.cloud.workstations_v1.WorkstationsClient.list_workstations",
                    extra={
                        "serviceName": "google.cloud.workstations.v1.Workstations",
                        "rpcName": "ListWorkstations",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _StartWorkstation(
        _BaseWorkstationsRestTransport._BaseStartWorkstation, WorkstationsRestStub
    ):
        def __hash__(self):
            return hash("WorkstationsRestTransport.StartWorkstation")

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
            request: workstations.StartWorkstationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the start workstation method over HTTP.

            Args:
                request (~.workstations.StartWorkstationRequest):
                    The request object. Request message for StartWorkstation.
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
                _BaseWorkstationsRestTransport._BaseStartWorkstation._get_http_options()
            )
            request, metadata = self._interceptor.pre_start_workstation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseWorkstationsRestTransport._BaseStartWorkstation,
                    "_BaseStartWorkstation__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.workstations_v1.WorkstationsClient.StartWorkstation",
                    extra={
                        "serviceName": "google.cloud.workstations.v1.Workstations",
                        "rpcName": "StartWorkstation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = WorkstationsRestTransport._StartWorkstation._get_response(
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

            resp = self._interceptor.post_start_workstation(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_start_workstation_with_metadata(
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
                    "Received response for google.cloud.workstations_v1.WorkstationsClient.start_workstation",
                    extra={
                        "serviceName": "google.cloud.workstations.v1.Workstations",
                        "rpcName": "StartWorkstation",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _StopWorkstation(
        _BaseWorkstationsRestTransport._BaseStopWorkstation, WorkstationsRestStub
    ):
        def __hash__(self):
            return hash("WorkstationsRestTransport.StopWorkstation")

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
            request: workstations.StopWorkstationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the stop workstation method over HTTP.

            Args:
                request (~.workstations.StopWorkstationRequest):
                    The request object. Request message for StopWorkstation.
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
                _BaseWorkstationsRestTransport._BaseStopWorkstation._get_http_options()
            )
            request, metadata = self._interceptor.pre_stop_workstation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseWorkstationsRestTransport._BaseStopWorkstation,
                    "_BaseStopWorkstation__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.workstations_v1.WorkstationsClient.StopWorkstation",
                    extra={
                        "serviceName": "google.cloud.workstations.v1.Workstations",
                        "rpcName": "StopWorkstation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = WorkstationsRestTransport._StopWorkstation._get_response(
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

            resp = self._interceptor.post_stop_workstation(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_stop_workstation_with_metadata(
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
                    "Received response for google.cloud.workstations_v1.WorkstationsClient.stop_workstation",
                    extra={
                        "serviceName": "google.cloud.workstations.v1.Workstations",
                        "rpcName": "StopWorkstation",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateWorkstation(
        _BaseWorkstationsRestTransport._BaseUpdateWorkstation, WorkstationsRestStub
    ):
        def __hash__(self):
            return hash("WorkstationsRestTransport.UpdateWorkstation")

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
            request: workstations.UpdateWorkstationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update workstation method over HTTP.

            Args:
                request (~.workstations.UpdateWorkstationRequest):
                    The request object. Request message for
                UpdateWorkstation.
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

            http_options = _BaseWorkstationsRestTransport._BaseUpdateWorkstation._get_http_options()
            request, metadata = self._interceptor.pre_update_workstation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseWorkstationsRestTransport._BaseUpdateWorkstation,
                    "_BaseUpdateWorkstation__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.workstations_v1.WorkstationsClient.UpdateWorkstation",
                    extra={
                        "serviceName": "google.cloud.workstations.v1.Workstations",
                        "rpcName": "UpdateWorkstation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = WorkstationsRestTransport._UpdateWorkstation._get_response(
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

            resp = self._interceptor.post_update_workstation(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_workstation_with_metadata(
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
                    "Received response for google.cloud.workstations_v1.WorkstationsClient.update_workstation",
                    extra={
                        "serviceName": "google.cloud.workstations.v1.Workstations",
                        "rpcName": "UpdateWorkstation",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateWorkstationCluster(
        _BaseWorkstationsRestTransport._BaseUpdateWorkstationCluster,
        WorkstationsRestStub,
    ):
        def __hash__(self):
            return hash("WorkstationsRestTransport.UpdateWorkstationCluster")

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
            request: workstations.UpdateWorkstationClusterRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update workstation
            cluster method over HTTP.

                Args:
                    request (~.workstations.UpdateWorkstationClusterRequest):
                        The request object. Request message for
                    UpdateWorkstationCluster.
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

            http_options = _BaseWorkstationsRestTransport._BaseUpdateWorkstationCluster._get_http_options()
            request, metadata = self._interceptor.pre_update_workstation_cluster(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseWorkstationsRestTransport._BaseUpdateWorkstationCluster,
                    "_BaseUpdateWorkstationCluster__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.workstations_v1.WorkstationsClient.UpdateWorkstationCluster",
                    extra={
                        "serviceName": "google.cloud.workstations.v1.Workstations",
                        "rpcName": "UpdateWorkstationCluster",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                WorkstationsRestTransport._UpdateWorkstationCluster._get_response(
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

            resp = self._interceptor.post_update_workstation_cluster(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_workstation_cluster_with_metadata(
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
                    "Received response for google.cloud.workstations_v1.WorkstationsClient.update_workstation_cluster",
                    extra={
                        "serviceName": "google.cloud.workstations.v1.Workstations",
                        "rpcName": "UpdateWorkstationCluster",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateWorkstationConfig(
        _BaseWorkstationsRestTransport._BaseUpdateWorkstationConfig,
        WorkstationsRestStub,
    ):
        def __hash__(self):
            return hash("WorkstationsRestTransport.UpdateWorkstationConfig")

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
            request: workstations.UpdateWorkstationConfigRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update workstation config method over HTTP.

            Args:
                request (~.workstations.UpdateWorkstationConfigRequest):
                    The request object. Request message for
                UpdateWorkstationConfig.
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

            http_options = _BaseWorkstationsRestTransport._BaseUpdateWorkstationConfig._get_http_options()
            request, metadata = self._interceptor.pre_update_workstation_config(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseWorkstationsRestTransport._BaseUpdateWorkstationConfig,
                    "_BaseUpdateWorkstationConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.workstations_v1.WorkstationsClient.UpdateWorkstationConfig",
                    extra={
                        "serviceName": "google.cloud.workstations.v1.Workstations",
                        "rpcName": "UpdateWorkstationConfig",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = WorkstationsRestTransport._UpdateWorkstationConfig._get_response(
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

            resp = self._interceptor.post_update_workstation_config(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_workstation_config_with_metadata(
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
                    "Received response for google.cloud.workstations_v1.WorkstationsClient.update_workstation_config",
                    extra={
                        "serviceName": "google.cloud.workstations.v1.Workstations",
                        "rpcName": "UpdateWorkstationConfig",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def create_workstation(
        self,
    ) -> Callable[[workstations.CreateWorkstationRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateWorkstation(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_workstation_cluster(
        self,
    ) -> Callable[
        [workstations.CreateWorkstationClusterRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateWorkstationCluster(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def create_workstation_config(
        self,
    ) -> Callable[
        [workstations.CreateWorkstationConfigRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateWorkstationConfig(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def delete_workstation(
        self,
    ) -> Callable[[workstations.DeleteWorkstationRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteWorkstation(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_workstation_cluster(
        self,
    ) -> Callable[
        [workstations.DeleteWorkstationClusterRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteWorkstationCluster(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def delete_workstation_config(
        self,
    ) -> Callable[
        [workstations.DeleteWorkstationConfigRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteWorkstationConfig(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def generate_access_token(
        self,
    ) -> Callable[
        [workstations.GenerateAccessTokenRequest],
        workstations.GenerateAccessTokenResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GenerateAccessToken(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_workstation(
        self,
    ) -> Callable[[workstations.GetWorkstationRequest], workstations.Workstation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetWorkstation(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_workstation_cluster(
        self,
    ) -> Callable[
        [workstations.GetWorkstationClusterRequest], workstations.WorkstationCluster
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetWorkstationCluster(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_workstation_config(
        self,
    ) -> Callable[
        [workstations.GetWorkstationConfigRequest], workstations.WorkstationConfig
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetWorkstationConfig(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_usable_workstation_configs(
        self,
    ) -> Callable[
        [workstations.ListUsableWorkstationConfigsRequest],
        workstations.ListUsableWorkstationConfigsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListUsableWorkstationConfigs(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def list_usable_workstations(
        self,
    ) -> Callable[
        [workstations.ListUsableWorkstationsRequest],
        workstations.ListUsableWorkstationsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListUsableWorkstations(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def list_workstation_clusters(
        self,
    ) -> Callable[
        [workstations.ListWorkstationClustersRequest],
        workstations.ListWorkstationClustersResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListWorkstationClusters(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def list_workstation_configs(
        self,
    ) -> Callable[
        [workstations.ListWorkstationConfigsRequest],
        workstations.ListWorkstationConfigsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListWorkstationConfigs(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def list_workstations(
        self,
    ) -> Callable[
        [workstations.ListWorkstationsRequest], workstations.ListWorkstationsResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListWorkstations(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def start_workstation(
        self,
    ) -> Callable[[workstations.StartWorkstationRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._StartWorkstation(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def stop_workstation(
        self,
    ) -> Callable[[workstations.StopWorkstationRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._StopWorkstation(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_workstation(
        self,
    ) -> Callable[[workstations.UpdateWorkstationRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateWorkstation(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_workstation_cluster(
        self,
    ) -> Callable[
        [workstations.UpdateWorkstationClusterRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateWorkstationCluster(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def update_workstation_config(
        self,
    ) -> Callable[
        [workstations.UpdateWorkstationConfigRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateWorkstationConfig(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def get_iam_policy(self):
        return self._GetIamPolicy(self._session, self._host, self._interceptor)  # type: ignore

    class _GetIamPolicy(
        _BaseWorkstationsRestTransport._BaseGetIamPolicy, WorkstationsRestStub
    ):
        def __hash__(self):
            return hash("WorkstationsRestTransport.GetIamPolicy")

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

            http_options = (
                _BaseWorkstationsRestTransport._BaseGetIamPolicy._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_iam_policy(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseWorkstationsRestTransport._BaseGetIamPolicy,
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
                    f"Sending request for google.cloud.workstations_v1.WorkstationsClient.GetIamPolicy",
                    extra={
                        "serviceName": "google.cloud.workstations.v1.Workstations",
                        "rpcName": "GetIamPolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = WorkstationsRestTransport._GetIamPolicy._get_response(
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
                    "Received response for google.cloud.workstations_v1.WorkstationsAsyncClient.GetIamPolicy",
                    extra={
                        "serviceName": "google.cloud.workstations.v1.Workstations",
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
        _BaseWorkstationsRestTransport._BaseSetIamPolicy, WorkstationsRestStub
    ):
        def __hash__(self):
            return hash("WorkstationsRestTransport.SetIamPolicy")

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

            http_options = (
                _BaseWorkstationsRestTransport._BaseSetIamPolicy._get_http_options()
            )
            request, metadata = self._interceptor.pre_set_iam_policy(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseWorkstationsRestTransport._BaseSetIamPolicy,
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
                    f"Sending request for google.cloud.workstations_v1.WorkstationsClient.SetIamPolicy",
                    extra={
                        "serviceName": "google.cloud.workstations.v1.Workstations",
                        "rpcName": "SetIamPolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = WorkstationsRestTransport._SetIamPolicy._get_response(
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
                    "Received response for google.cloud.workstations_v1.WorkstationsAsyncClient.SetIamPolicy",
                    extra={
                        "serviceName": "google.cloud.workstations.v1.Workstations",
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
        _BaseWorkstationsRestTransport._BaseTestIamPermissions, WorkstationsRestStub
    ):
        def __hash__(self):
            return hash("WorkstationsRestTransport.TestIamPermissions")

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

            http_options = _BaseWorkstationsRestTransport._BaseTestIamPermissions._get_http_options()
            request, metadata = self._interceptor.pre_test_iam_permissions(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseWorkstationsRestTransport._BaseTestIamPermissions,
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
                    f"Sending request for google.cloud.workstations_v1.WorkstationsClient.TestIamPermissions",
                    extra={
                        "serviceName": "google.cloud.workstations.v1.Workstations",
                        "rpcName": "TestIamPermissions",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = WorkstationsRestTransport._TestIamPermissions._get_response(
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
                    "Received response for google.cloud.workstations_v1.WorkstationsAsyncClient.TestIamPermissions",
                    extra={
                        "serviceName": "google.cloud.workstations.v1.Workstations",
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
        _BaseWorkstationsRestTransport._BaseCancelOperation, WorkstationsRestStub
    ):
        def __hash__(self):
            return hash("WorkstationsRestTransport.CancelOperation")

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
                _BaseWorkstationsRestTransport._BaseCancelOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_cancel_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseWorkstationsRestTransport._BaseCancelOperation,
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
                    f"Sending request for google.cloud.workstations_v1.WorkstationsClient.CancelOperation",
                    extra={
                        "serviceName": "google.cloud.workstations.v1.Workstations",
                        "rpcName": "CancelOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = WorkstationsRestTransport._CancelOperation._get_response(
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
        _BaseWorkstationsRestTransport._BaseDeleteOperation, WorkstationsRestStub
    ):
        def __hash__(self):
            return hash("WorkstationsRestTransport.DeleteOperation")

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
                _BaseWorkstationsRestTransport._BaseDeleteOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseWorkstationsRestTransport._BaseDeleteOperation,
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
                    f"Sending request for google.cloud.workstations_v1.WorkstationsClient.DeleteOperation",
                    extra={
                        "serviceName": "google.cloud.workstations.v1.Workstations",
                        "rpcName": "DeleteOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = WorkstationsRestTransport._DeleteOperation._get_response(
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
        _BaseWorkstationsRestTransport._BaseGetOperation, WorkstationsRestStub
    ):
        def __hash__(self):
            return hash("WorkstationsRestTransport.GetOperation")

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
                _BaseWorkstationsRestTransport._BaseGetOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_operation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseWorkstationsRestTransport._BaseGetOperation,
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
                    f"Sending request for google.cloud.workstations_v1.WorkstationsClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.workstations.v1.Workstations",
                        "rpcName": "GetOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = WorkstationsRestTransport._GetOperation._get_response(
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
                    "Received response for google.cloud.workstations_v1.WorkstationsAsyncClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.workstations.v1.Workstations",
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
        _BaseWorkstationsRestTransport._BaseListOperations, WorkstationsRestStub
    ):
        def __hash__(self):
            return hash("WorkstationsRestTransport.ListOperations")

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
                _BaseWorkstationsRestTransport._BaseListOperations._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_operations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseWorkstationsRestTransport._BaseListOperations,
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
                    f"Sending request for google.cloud.workstations_v1.WorkstationsClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.workstations.v1.Workstations",
                        "rpcName": "ListOperations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = WorkstationsRestTransport._ListOperations._get_response(
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
                    "Received response for google.cloud.workstations_v1.WorkstationsAsyncClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.workstations.v1.Workstations",
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


__all__ = ("WorkstationsRestTransport",)
