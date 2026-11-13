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
from google.longrunning import operations_pb2  # type: ignore
from google.protobuf import json_format
from requests import __version__ as requests_version

from google.cloud.tpu_v2._compat import transcode_request
from google.cloud.tpu_v2.types import cloud_tpu

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseTpuRestTransport

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


class TpuRestInterceptor:
    """Interceptor for Tpu.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the TpuRestTransport.

    .. code-block:: python
        class MyCustomTpuInterceptor(TpuRestInterceptor):
            def pre_create_node(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_node(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_queued_resource(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_queued_resource(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_node(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_node(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_queued_resource(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_queued_resource(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_generate_service_identity(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_generate_service_identity(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_accelerator_type(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_accelerator_type(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_guest_attributes(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_guest_attributes(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_node(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_node(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_queued_resource(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_queued_resource(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_runtime_version(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_runtime_version(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_accelerator_types(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_accelerator_types(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_nodes(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_nodes(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_queued_resources(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_queued_resources(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_runtime_versions(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_runtime_versions(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_reset_queued_resource(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_reset_queued_resource(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_start_node(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_start_node(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_stop_node(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_stop_node(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_node(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_node(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = TpuRestTransport(interceptor=MyCustomTpuInterceptor())
        client = TpuClient(transport=transport)


    """

    def pre_create_node(
        self,
        request: cloud_tpu.CreateNodeRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[cloud_tpu.CreateNodeRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for create_node

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Tpu server.
        """
        return request, metadata

    def post_create_node(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_node

        DEPRECATED. Please use the `post_create_node_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Tpu server but before
        it is returned to user code. This `post_create_node` interceptor runs
        before the `post_create_node_with_metadata` interceptor.
        """
        return response

    def post_create_node_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_node

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Tpu server but before it is returned to user code.

        We recommend only using this `post_create_node_with_metadata`
        interceptor in new development instead of the `post_create_node` interceptor.
        When both interceptors are used, this `post_create_node_with_metadata` interceptor runs after the
        `post_create_node` interceptor. The (possibly modified) response returned by
        `post_create_node` will be passed to
        `post_create_node_with_metadata`.
        """
        return response, metadata

    def pre_create_queued_resource(
        self,
        request: cloud_tpu.CreateQueuedResourceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_tpu.CreateQueuedResourceRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_queued_resource

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Tpu server.
        """
        return request, metadata

    def post_create_queued_resource(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_queued_resource

        DEPRECATED. Please use the `post_create_queued_resource_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Tpu server but before
        it is returned to user code. This `post_create_queued_resource` interceptor runs
        before the `post_create_queued_resource_with_metadata` interceptor.
        """
        return response

    def post_create_queued_resource_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_queued_resource

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Tpu server but before it is returned to user code.

        We recommend only using this `post_create_queued_resource_with_metadata`
        interceptor in new development instead of the `post_create_queued_resource` interceptor.
        When both interceptors are used, this `post_create_queued_resource_with_metadata` interceptor runs after the
        `post_create_queued_resource` interceptor. The (possibly modified) response returned by
        `post_create_queued_resource` will be passed to
        `post_create_queued_resource_with_metadata`.
        """
        return response, metadata

    def pre_delete_node(
        self,
        request: cloud_tpu.DeleteNodeRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[cloud_tpu.DeleteNodeRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for delete_node

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Tpu server.
        """
        return request, metadata

    def post_delete_node(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_node

        DEPRECATED. Please use the `post_delete_node_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Tpu server but before
        it is returned to user code. This `post_delete_node` interceptor runs
        before the `post_delete_node_with_metadata` interceptor.
        """
        return response

    def post_delete_node_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_node

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Tpu server but before it is returned to user code.

        We recommend only using this `post_delete_node_with_metadata`
        interceptor in new development instead of the `post_delete_node` interceptor.
        When both interceptors are used, this `post_delete_node_with_metadata` interceptor runs after the
        `post_delete_node` interceptor. The (possibly modified) response returned by
        `post_delete_node` will be passed to
        `post_delete_node_with_metadata`.
        """
        return response, metadata

    def pre_delete_queued_resource(
        self,
        request: cloud_tpu.DeleteQueuedResourceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_tpu.DeleteQueuedResourceRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_queued_resource

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Tpu server.
        """
        return request, metadata

    def post_delete_queued_resource(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_queued_resource

        DEPRECATED. Please use the `post_delete_queued_resource_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Tpu server but before
        it is returned to user code. This `post_delete_queued_resource` interceptor runs
        before the `post_delete_queued_resource_with_metadata` interceptor.
        """
        return response

    def post_delete_queued_resource_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_queued_resource

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Tpu server but before it is returned to user code.

        We recommend only using this `post_delete_queued_resource_with_metadata`
        interceptor in new development instead of the `post_delete_queued_resource` interceptor.
        When both interceptors are used, this `post_delete_queued_resource_with_metadata` interceptor runs after the
        `post_delete_queued_resource` interceptor. The (possibly modified) response returned by
        `post_delete_queued_resource` will be passed to
        `post_delete_queued_resource_with_metadata`.
        """
        return response, metadata

    def pre_generate_service_identity(
        self,
        request: cloud_tpu.GenerateServiceIdentityRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_tpu.GenerateServiceIdentityRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for generate_service_identity

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Tpu server.
        """
        return request, metadata

    def post_generate_service_identity(
        self, response: cloud_tpu.GenerateServiceIdentityResponse
    ) -> cloud_tpu.GenerateServiceIdentityResponse:
        """Post-rpc interceptor for generate_service_identity

        DEPRECATED. Please use the `post_generate_service_identity_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Tpu server but before
        it is returned to user code. This `post_generate_service_identity` interceptor runs
        before the `post_generate_service_identity_with_metadata` interceptor.
        """
        return response

    def post_generate_service_identity_with_metadata(
        self,
        response: cloud_tpu.GenerateServiceIdentityResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_tpu.GenerateServiceIdentityResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for generate_service_identity

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Tpu server but before it is returned to user code.

        We recommend only using this `post_generate_service_identity_with_metadata`
        interceptor in new development instead of the `post_generate_service_identity` interceptor.
        When both interceptors are used, this `post_generate_service_identity_with_metadata` interceptor runs after the
        `post_generate_service_identity` interceptor. The (possibly modified) response returned by
        `post_generate_service_identity` will be passed to
        `post_generate_service_identity_with_metadata`.
        """
        return response, metadata

    def pre_get_accelerator_type(
        self,
        request: cloud_tpu.GetAcceleratorTypeRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_tpu.GetAcceleratorTypeRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_accelerator_type

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Tpu server.
        """
        return request, metadata

    def post_get_accelerator_type(
        self, response: cloud_tpu.AcceleratorType
    ) -> cloud_tpu.AcceleratorType:
        """Post-rpc interceptor for get_accelerator_type

        DEPRECATED. Please use the `post_get_accelerator_type_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Tpu server but before
        it is returned to user code. This `post_get_accelerator_type` interceptor runs
        before the `post_get_accelerator_type_with_metadata` interceptor.
        """
        return response

    def post_get_accelerator_type_with_metadata(
        self,
        response: cloud_tpu.AcceleratorType,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[cloud_tpu.AcceleratorType, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_accelerator_type

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Tpu server but before it is returned to user code.

        We recommend only using this `post_get_accelerator_type_with_metadata`
        interceptor in new development instead of the `post_get_accelerator_type` interceptor.
        When both interceptors are used, this `post_get_accelerator_type_with_metadata` interceptor runs after the
        `post_get_accelerator_type` interceptor. The (possibly modified) response returned by
        `post_get_accelerator_type` will be passed to
        `post_get_accelerator_type_with_metadata`.
        """
        return response, metadata

    def pre_get_guest_attributes(
        self,
        request: cloud_tpu.GetGuestAttributesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_tpu.GetGuestAttributesRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_guest_attributes

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Tpu server.
        """
        return request, metadata

    def post_get_guest_attributes(
        self, response: cloud_tpu.GetGuestAttributesResponse
    ) -> cloud_tpu.GetGuestAttributesResponse:
        """Post-rpc interceptor for get_guest_attributes

        DEPRECATED. Please use the `post_get_guest_attributes_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Tpu server but before
        it is returned to user code. This `post_get_guest_attributes` interceptor runs
        before the `post_get_guest_attributes_with_metadata` interceptor.
        """
        return response

    def post_get_guest_attributes_with_metadata(
        self,
        response: cloud_tpu.GetGuestAttributesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_tpu.GetGuestAttributesResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for get_guest_attributes

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Tpu server but before it is returned to user code.

        We recommend only using this `post_get_guest_attributes_with_metadata`
        interceptor in new development instead of the `post_get_guest_attributes` interceptor.
        When both interceptors are used, this `post_get_guest_attributes_with_metadata` interceptor runs after the
        `post_get_guest_attributes` interceptor. The (possibly modified) response returned by
        `post_get_guest_attributes` will be passed to
        `post_get_guest_attributes_with_metadata`.
        """
        return response, metadata

    def pre_get_node(
        self,
        request: cloud_tpu.GetNodeRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[cloud_tpu.GetNodeRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_node

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Tpu server.
        """
        return request, metadata

    def post_get_node(self, response: cloud_tpu.Node) -> cloud_tpu.Node:
        """Post-rpc interceptor for get_node

        DEPRECATED. Please use the `post_get_node_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Tpu server but before
        it is returned to user code. This `post_get_node` interceptor runs
        before the `post_get_node_with_metadata` interceptor.
        """
        return response

    def post_get_node_with_metadata(
        self,
        response: cloud_tpu.Node,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[cloud_tpu.Node, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_node

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Tpu server but before it is returned to user code.

        We recommend only using this `post_get_node_with_metadata`
        interceptor in new development instead of the `post_get_node` interceptor.
        When both interceptors are used, this `post_get_node_with_metadata` interceptor runs after the
        `post_get_node` interceptor. The (possibly modified) response returned by
        `post_get_node` will be passed to
        `post_get_node_with_metadata`.
        """
        return response, metadata

    def pre_get_queued_resource(
        self,
        request: cloud_tpu.GetQueuedResourceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_tpu.GetQueuedResourceRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_queued_resource

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Tpu server.
        """
        return request, metadata

    def post_get_queued_resource(
        self, response: cloud_tpu.QueuedResource
    ) -> cloud_tpu.QueuedResource:
        """Post-rpc interceptor for get_queued_resource

        DEPRECATED. Please use the `post_get_queued_resource_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Tpu server but before
        it is returned to user code. This `post_get_queued_resource` interceptor runs
        before the `post_get_queued_resource_with_metadata` interceptor.
        """
        return response

    def post_get_queued_resource_with_metadata(
        self,
        response: cloud_tpu.QueuedResource,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[cloud_tpu.QueuedResource, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_queued_resource

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Tpu server but before it is returned to user code.

        We recommend only using this `post_get_queued_resource_with_metadata`
        interceptor in new development instead of the `post_get_queued_resource` interceptor.
        When both interceptors are used, this `post_get_queued_resource_with_metadata` interceptor runs after the
        `post_get_queued_resource` interceptor. The (possibly modified) response returned by
        `post_get_queued_resource` will be passed to
        `post_get_queued_resource_with_metadata`.
        """
        return response, metadata

    def pre_get_runtime_version(
        self,
        request: cloud_tpu.GetRuntimeVersionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_tpu.GetRuntimeVersionRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_runtime_version

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Tpu server.
        """
        return request, metadata

    def post_get_runtime_version(
        self, response: cloud_tpu.RuntimeVersion
    ) -> cloud_tpu.RuntimeVersion:
        """Post-rpc interceptor for get_runtime_version

        DEPRECATED. Please use the `post_get_runtime_version_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Tpu server but before
        it is returned to user code. This `post_get_runtime_version` interceptor runs
        before the `post_get_runtime_version_with_metadata` interceptor.
        """
        return response

    def post_get_runtime_version_with_metadata(
        self,
        response: cloud_tpu.RuntimeVersion,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[cloud_tpu.RuntimeVersion, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_runtime_version

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Tpu server but before it is returned to user code.

        We recommend only using this `post_get_runtime_version_with_metadata`
        interceptor in new development instead of the `post_get_runtime_version` interceptor.
        When both interceptors are used, this `post_get_runtime_version_with_metadata` interceptor runs after the
        `post_get_runtime_version` interceptor. The (possibly modified) response returned by
        `post_get_runtime_version` will be passed to
        `post_get_runtime_version_with_metadata`.
        """
        return response, metadata

    def pre_list_accelerator_types(
        self,
        request: cloud_tpu.ListAcceleratorTypesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_tpu.ListAcceleratorTypesRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_accelerator_types

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Tpu server.
        """
        return request, metadata

    def post_list_accelerator_types(
        self, response: cloud_tpu.ListAcceleratorTypesResponse
    ) -> cloud_tpu.ListAcceleratorTypesResponse:
        """Post-rpc interceptor for list_accelerator_types

        DEPRECATED. Please use the `post_list_accelerator_types_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Tpu server but before
        it is returned to user code. This `post_list_accelerator_types` interceptor runs
        before the `post_list_accelerator_types_with_metadata` interceptor.
        """
        return response

    def post_list_accelerator_types_with_metadata(
        self,
        response: cloud_tpu.ListAcceleratorTypesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_tpu.ListAcceleratorTypesResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_accelerator_types

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Tpu server but before it is returned to user code.

        We recommend only using this `post_list_accelerator_types_with_metadata`
        interceptor in new development instead of the `post_list_accelerator_types` interceptor.
        When both interceptors are used, this `post_list_accelerator_types_with_metadata` interceptor runs after the
        `post_list_accelerator_types` interceptor. The (possibly modified) response returned by
        `post_list_accelerator_types` will be passed to
        `post_list_accelerator_types_with_metadata`.
        """
        return response, metadata

    def pre_list_nodes(
        self,
        request: cloud_tpu.ListNodesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[cloud_tpu.ListNodesRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for list_nodes

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Tpu server.
        """
        return request, metadata

    def post_list_nodes(
        self, response: cloud_tpu.ListNodesResponse
    ) -> cloud_tpu.ListNodesResponse:
        """Post-rpc interceptor for list_nodes

        DEPRECATED. Please use the `post_list_nodes_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Tpu server but before
        it is returned to user code. This `post_list_nodes` interceptor runs
        before the `post_list_nodes_with_metadata` interceptor.
        """
        return response

    def post_list_nodes_with_metadata(
        self,
        response: cloud_tpu.ListNodesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[cloud_tpu.ListNodesResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for list_nodes

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Tpu server but before it is returned to user code.

        We recommend only using this `post_list_nodes_with_metadata`
        interceptor in new development instead of the `post_list_nodes` interceptor.
        When both interceptors are used, this `post_list_nodes_with_metadata` interceptor runs after the
        `post_list_nodes` interceptor. The (possibly modified) response returned by
        `post_list_nodes` will be passed to
        `post_list_nodes_with_metadata`.
        """
        return response, metadata

    def pre_list_queued_resources(
        self,
        request: cloud_tpu.ListQueuedResourcesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_tpu.ListQueuedResourcesRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_queued_resources

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Tpu server.
        """
        return request, metadata

    def post_list_queued_resources(
        self, response: cloud_tpu.ListQueuedResourcesResponse
    ) -> cloud_tpu.ListQueuedResourcesResponse:
        """Post-rpc interceptor for list_queued_resources

        DEPRECATED. Please use the `post_list_queued_resources_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Tpu server but before
        it is returned to user code. This `post_list_queued_resources` interceptor runs
        before the `post_list_queued_resources_with_metadata` interceptor.
        """
        return response

    def post_list_queued_resources_with_metadata(
        self,
        response: cloud_tpu.ListQueuedResourcesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_tpu.ListQueuedResourcesResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_queued_resources

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Tpu server but before it is returned to user code.

        We recommend only using this `post_list_queued_resources_with_metadata`
        interceptor in new development instead of the `post_list_queued_resources` interceptor.
        When both interceptors are used, this `post_list_queued_resources_with_metadata` interceptor runs after the
        `post_list_queued_resources` interceptor. The (possibly modified) response returned by
        `post_list_queued_resources` will be passed to
        `post_list_queued_resources_with_metadata`.
        """
        return response, metadata

    def pre_list_runtime_versions(
        self,
        request: cloud_tpu.ListRuntimeVersionsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_tpu.ListRuntimeVersionsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_runtime_versions

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Tpu server.
        """
        return request, metadata

    def post_list_runtime_versions(
        self, response: cloud_tpu.ListRuntimeVersionsResponse
    ) -> cloud_tpu.ListRuntimeVersionsResponse:
        """Post-rpc interceptor for list_runtime_versions

        DEPRECATED. Please use the `post_list_runtime_versions_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Tpu server but before
        it is returned to user code. This `post_list_runtime_versions` interceptor runs
        before the `post_list_runtime_versions_with_metadata` interceptor.
        """
        return response

    def post_list_runtime_versions_with_metadata(
        self,
        response: cloud_tpu.ListRuntimeVersionsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_tpu.ListRuntimeVersionsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_runtime_versions

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Tpu server but before it is returned to user code.

        We recommend only using this `post_list_runtime_versions_with_metadata`
        interceptor in new development instead of the `post_list_runtime_versions` interceptor.
        When both interceptors are used, this `post_list_runtime_versions_with_metadata` interceptor runs after the
        `post_list_runtime_versions` interceptor. The (possibly modified) response returned by
        `post_list_runtime_versions` will be passed to
        `post_list_runtime_versions_with_metadata`.
        """
        return response, metadata

    def pre_reset_queued_resource(
        self,
        request: cloud_tpu.ResetQueuedResourceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_tpu.ResetQueuedResourceRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for reset_queued_resource

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Tpu server.
        """
        return request, metadata

    def post_reset_queued_resource(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for reset_queued_resource

        DEPRECATED. Please use the `post_reset_queued_resource_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Tpu server but before
        it is returned to user code. This `post_reset_queued_resource` interceptor runs
        before the `post_reset_queued_resource_with_metadata` interceptor.
        """
        return response

    def post_reset_queued_resource_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for reset_queued_resource

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Tpu server but before it is returned to user code.

        We recommend only using this `post_reset_queued_resource_with_metadata`
        interceptor in new development instead of the `post_reset_queued_resource` interceptor.
        When both interceptors are used, this `post_reset_queued_resource_with_metadata` interceptor runs after the
        `post_reset_queued_resource` interceptor. The (possibly modified) response returned by
        `post_reset_queued_resource` will be passed to
        `post_reset_queued_resource_with_metadata`.
        """
        return response, metadata

    def pre_start_node(
        self,
        request: cloud_tpu.StartNodeRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[cloud_tpu.StartNodeRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for start_node

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Tpu server.
        """
        return request, metadata

    def post_start_node(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for start_node

        DEPRECATED. Please use the `post_start_node_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Tpu server but before
        it is returned to user code. This `post_start_node` interceptor runs
        before the `post_start_node_with_metadata` interceptor.
        """
        return response

    def post_start_node_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for start_node

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Tpu server but before it is returned to user code.

        We recommend only using this `post_start_node_with_metadata`
        interceptor in new development instead of the `post_start_node` interceptor.
        When both interceptors are used, this `post_start_node_with_metadata` interceptor runs after the
        `post_start_node` interceptor. The (possibly modified) response returned by
        `post_start_node` will be passed to
        `post_start_node_with_metadata`.
        """
        return response, metadata

    def pre_stop_node(
        self,
        request: cloud_tpu.StopNodeRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[cloud_tpu.StopNodeRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for stop_node

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Tpu server.
        """
        return request, metadata

    def post_stop_node(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for stop_node

        DEPRECATED. Please use the `post_stop_node_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Tpu server but before
        it is returned to user code. This `post_stop_node` interceptor runs
        before the `post_stop_node_with_metadata` interceptor.
        """
        return response

    def post_stop_node_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for stop_node

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Tpu server but before it is returned to user code.

        We recommend only using this `post_stop_node_with_metadata`
        interceptor in new development instead of the `post_stop_node` interceptor.
        When both interceptors are used, this `post_stop_node_with_metadata` interceptor runs after the
        `post_stop_node` interceptor. The (possibly modified) response returned by
        `post_stop_node` will be passed to
        `post_stop_node_with_metadata`.
        """
        return response, metadata

    def pre_update_node(
        self,
        request: cloud_tpu.UpdateNodeRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[cloud_tpu.UpdateNodeRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for update_node

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Tpu server.
        """
        return request, metadata

    def post_update_node(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_node

        DEPRECATED. Please use the `post_update_node_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Tpu server but before
        it is returned to user code. This `post_update_node` interceptor runs
        before the `post_update_node_with_metadata` interceptor.
        """
        return response

    def post_update_node_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_node

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Tpu server but before it is returned to user code.

        We recommend only using this `post_update_node_with_metadata`
        interceptor in new development instead of the `post_update_node` interceptor.
        When both interceptors are used, this `post_update_node_with_metadata` interceptor runs after the
        `post_update_node` interceptor. The (possibly modified) response returned by
        `post_update_node` will be passed to
        `post_update_node_with_metadata`.
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
        before they are sent to the Tpu server.
        """
        return request, metadata

    def post_get_location(
        self, response: locations_pb2.Location
    ) -> locations_pb2.Location:
        """Post-rpc interceptor for get_location

        Override in a subclass to manipulate the response
        after it is returned by the Tpu server but before
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
        before they are sent to the Tpu server.
        """
        return request, metadata

    def post_list_locations(
        self, response: locations_pb2.ListLocationsResponse
    ) -> locations_pb2.ListLocationsResponse:
        """Post-rpc interceptor for list_locations

        Override in a subclass to manipulate the response
        after it is returned by the Tpu server but before
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
        before they are sent to the Tpu server.
        """
        return request, metadata

    def post_cancel_operation(self, response: None) -> None:
        """Post-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the response
        after it is returned by the Tpu server but before
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
        before they are sent to the Tpu server.
        """
        return request, metadata

    def post_delete_operation(self, response: None) -> None:
        """Post-rpc interceptor for delete_operation

        Override in a subclass to manipulate the response
        after it is returned by the Tpu server but before
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
        before they are sent to the Tpu server.
        """
        return request, metadata

    def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the Tpu server but before
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
        before they are sent to the Tpu server.
        """
        return request, metadata

    def post_list_operations(
        self, response: operations_pb2.ListOperationsResponse
    ) -> operations_pb2.ListOperationsResponse:
        """Post-rpc interceptor for list_operations

        Override in a subclass to manipulate the response
        after it is returned by the Tpu server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class TpuRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: TpuRestInterceptor


class TpuRestTransport(_BaseTpuRestTransport):
    """REST backend synchronous transport for Tpu.

    Manages TPU nodes and other resources

    TPU API v2

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "tpu.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[TpuRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'tpu.googleapis.com').
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
            interceptor (Optional[TpuRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or TpuRestInterceptor()
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
                        "uri": "/v2/{name=projects/*/locations/*/operations/*}:cancel",
                    },
                ],
                "google.longrunning.Operations.DeleteOperation": [
                    {
                        "method": "delete",
                        "uri": "/v2/{name=projects/*/locations/*/operations/*}",
                    },
                ],
                "google.longrunning.Operations.GetOperation": [
                    {
                        "method": "get",
                        "uri": "/v2/{name=projects/*/locations/*/operations/*}",
                    },
                ],
                "google.longrunning.Operations.ListOperations": [
                    {
                        "method": "get",
                        "uri": "/v2/{name=projects/*/locations/*}/operations",
                    },
                ],
            }

            rest_transport = operations_v1.OperationsRestTransport(
                host=self._host,
                # use the credentials which are saved
                credentials=self._credentials,
                scopes=self._scopes,
                http_options=http_options,
                path_prefix="v2",
            )

            self._operations_client = operations_v1.AbstractOperationsClient(
                transport=rest_transport
            )

        # Return the client from cache.
        return self._operations_client

    class _CreateNode(_BaseTpuRestTransport._BaseCreateNode, TpuRestStub):
        def __hash__(self):
            return hash("TpuRestTransport.CreateNode")

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
            request: cloud_tpu.CreateNodeRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create node method over HTTP.

            Args:
                request (~.cloud_tpu.CreateNodeRequest):
                    The request object. Request for
                [CreateNode][google.cloud.tpu.v2.Tpu.CreateNode].
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

            http_options = _BaseTpuRestTransport._BaseCreateNode._get_http_options()
            request, metadata = self._interceptor.pre_create_node(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseTpuRestTransport._BaseCreateNode,
                    "_BaseCreateNode__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.tpu_v2.TpuClient.CreateNode",
                    extra={
                        "serviceName": "google.cloud.tpu.v2.Tpu",
                        "rpcName": "CreateNode",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = TpuRestTransport._CreateNode._get_response(
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

            resp = self._interceptor.post_create_node(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_node_with_metadata(
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
                    "Received response for google.cloud.tpu_v2.TpuClient.create_node",
                    extra={
                        "serviceName": "google.cloud.tpu.v2.Tpu",
                        "rpcName": "CreateNode",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateQueuedResource(
        _BaseTpuRestTransport._BaseCreateQueuedResource, TpuRestStub
    ):
        def __hash__(self):
            return hash("TpuRestTransport.CreateQueuedResource")

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
            request: cloud_tpu.CreateQueuedResourceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create queued resource method over HTTP.

            Args:
                request (~.cloud_tpu.CreateQueuedResourceRequest):
                    The request object. Request for
                [CreateQueuedResource][google.cloud.tpu.v2.Tpu.CreateQueuedResource].
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
                _BaseTpuRestTransport._BaseCreateQueuedResource._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_queued_resource(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseTpuRestTransport._BaseCreateQueuedResource,
                    "_BaseCreateQueuedResource__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.tpu_v2.TpuClient.CreateQueuedResource",
                    extra={
                        "serviceName": "google.cloud.tpu.v2.Tpu",
                        "rpcName": "CreateQueuedResource",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = TpuRestTransport._CreateQueuedResource._get_response(
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

            resp = self._interceptor.post_create_queued_resource(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_queued_resource_with_metadata(
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
                    "Received response for google.cloud.tpu_v2.TpuClient.create_queued_resource",
                    extra={
                        "serviceName": "google.cloud.tpu.v2.Tpu",
                        "rpcName": "CreateQueuedResource",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteNode(_BaseTpuRestTransport._BaseDeleteNode, TpuRestStub):
        def __hash__(self):
            return hash("TpuRestTransport.DeleteNode")

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
            request: cloud_tpu.DeleteNodeRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete node method over HTTP.

            Args:
                request (~.cloud_tpu.DeleteNodeRequest):
                    The request object. Request for
                [DeleteNode][google.cloud.tpu.v2.Tpu.DeleteNode].
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

            http_options = _BaseTpuRestTransport._BaseDeleteNode._get_http_options()
            request, metadata = self._interceptor.pre_delete_node(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseTpuRestTransport._BaseDeleteNode,
                    "_BaseDeleteNode__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.tpu_v2.TpuClient.DeleteNode",
                    extra={
                        "serviceName": "google.cloud.tpu.v2.Tpu",
                        "rpcName": "DeleteNode",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = TpuRestTransport._DeleteNode._get_response(
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

            resp = self._interceptor.post_delete_node(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_node_with_metadata(
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
                    "Received response for google.cloud.tpu_v2.TpuClient.delete_node",
                    extra={
                        "serviceName": "google.cloud.tpu.v2.Tpu",
                        "rpcName": "DeleteNode",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteQueuedResource(
        _BaseTpuRestTransport._BaseDeleteQueuedResource, TpuRestStub
    ):
        def __hash__(self):
            return hash("TpuRestTransport.DeleteQueuedResource")

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
            request: cloud_tpu.DeleteQueuedResourceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete queued resource method over HTTP.

            Args:
                request (~.cloud_tpu.DeleteQueuedResourceRequest):
                    The request object. Request for
                [DeleteQueuedResource][google.cloud.tpu.v2.Tpu.DeleteQueuedResource].
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
                _BaseTpuRestTransport._BaseDeleteQueuedResource._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_queued_resource(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseTpuRestTransport._BaseDeleteQueuedResource,
                    "_BaseDeleteQueuedResource__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.tpu_v2.TpuClient.DeleteQueuedResource",
                    extra={
                        "serviceName": "google.cloud.tpu.v2.Tpu",
                        "rpcName": "DeleteQueuedResource",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = TpuRestTransport._DeleteQueuedResource._get_response(
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

            resp = self._interceptor.post_delete_queued_resource(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_queued_resource_with_metadata(
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
                    "Received response for google.cloud.tpu_v2.TpuClient.delete_queued_resource",
                    extra={
                        "serviceName": "google.cloud.tpu.v2.Tpu",
                        "rpcName": "DeleteQueuedResource",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GenerateServiceIdentity(
        _BaseTpuRestTransport._BaseGenerateServiceIdentity, TpuRestStub
    ):
        def __hash__(self):
            return hash("TpuRestTransport.GenerateServiceIdentity")

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
            request: cloud_tpu.GenerateServiceIdentityRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cloud_tpu.GenerateServiceIdentityResponse:
            r"""Call the generate service identity method over HTTP.

            Args:
                request (~.cloud_tpu.GenerateServiceIdentityRequest):
                    The request object. Request for
                [GenerateServiceIdentity][google.cloud.tpu.v2.Tpu.GenerateServiceIdentity].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cloud_tpu.GenerateServiceIdentityResponse:
                    Response for
                [GenerateServiceIdentity][google.cloud.tpu.v2.Tpu.GenerateServiceIdentity].

            """

            http_options = (
                _BaseTpuRestTransport._BaseGenerateServiceIdentity._get_http_options()
            )
            request, metadata = self._interceptor.pre_generate_service_identity(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseTpuRestTransport._BaseGenerateServiceIdentity,
                    "_BaseGenerateServiceIdentity__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.tpu_v2.TpuClient.GenerateServiceIdentity",
                    extra={
                        "serviceName": "google.cloud.tpu.v2.Tpu",
                        "rpcName": "GenerateServiceIdentity",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = TpuRestTransport._GenerateServiceIdentity._get_response(
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
            resp = cloud_tpu.GenerateServiceIdentityResponse()
            pb_resp = cloud_tpu.GenerateServiceIdentityResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_generate_service_identity(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_generate_service_identity_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        cloud_tpu.GenerateServiceIdentityResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.tpu_v2.TpuClient.generate_service_identity",
                    extra={
                        "serviceName": "google.cloud.tpu.v2.Tpu",
                        "rpcName": "GenerateServiceIdentity",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetAcceleratorType(
        _BaseTpuRestTransport._BaseGetAcceleratorType, TpuRestStub
    ):
        def __hash__(self):
            return hash("TpuRestTransport.GetAcceleratorType")

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
            request: cloud_tpu.GetAcceleratorTypeRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cloud_tpu.AcceleratorType:
            r"""Call the get accelerator type method over HTTP.

            Args:
                request (~.cloud_tpu.GetAcceleratorTypeRequest):
                    The request object. Request for
                [GetAcceleratorType][google.cloud.tpu.v2.Tpu.GetAcceleratorType].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cloud_tpu.AcceleratorType:
                    A accelerator type that a Node can be
                configured with.

            """

            http_options = (
                _BaseTpuRestTransport._BaseGetAcceleratorType._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_accelerator_type(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseTpuRestTransport._BaseGetAcceleratorType,
                    "_BaseGetAcceleratorType__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.tpu_v2.TpuClient.GetAcceleratorType",
                    extra={
                        "serviceName": "google.cloud.tpu.v2.Tpu",
                        "rpcName": "GetAcceleratorType",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = TpuRestTransport._GetAcceleratorType._get_response(
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
            resp = cloud_tpu.AcceleratorType()
            pb_resp = cloud_tpu.AcceleratorType.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_accelerator_type(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_accelerator_type_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = cloud_tpu.AcceleratorType.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.tpu_v2.TpuClient.get_accelerator_type",
                    extra={
                        "serviceName": "google.cloud.tpu.v2.Tpu",
                        "rpcName": "GetAcceleratorType",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetGuestAttributes(
        _BaseTpuRestTransport._BaseGetGuestAttributes, TpuRestStub
    ):
        def __hash__(self):
            return hash("TpuRestTransport.GetGuestAttributes")

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
            request: cloud_tpu.GetGuestAttributesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cloud_tpu.GetGuestAttributesResponse:
            r"""Call the get guest attributes method over HTTP.

            Args:
                request (~.cloud_tpu.GetGuestAttributesRequest):
                    The request object. Request for
                [GetGuestAttributes][google.cloud.tpu.v2.Tpu.GetGuestAttributes].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cloud_tpu.GetGuestAttributesResponse:
                    Response for
                [GetGuestAttributes][google.cloud.tpu.v2.Tpu.GetGuestAttributes].

            """

            http_options = (
                _BaseTpuRestTransport._BaseGetGuestAttributes._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_guest_attributes(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseTpuRestTransport._BaseGetGuestAttributes,
                    "_BaseGetGuestAttributes__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.tpu_v2.TpuClient.GetGuestAttributes",
                    extra={
                        "serviceName": "google.cloud.tpu.v2.Tpu",
                        "rpcName": "GetGuestAttributes",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = TpuRestTransport._GetGuestAttributes._get_response(
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
            resp = cloud_tpu.GetGuestAttributesResponse()
            pb_resp = cloud_tpu.GetGuestAttributesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_guest_attributes(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_guest_attributes_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = cloud_tpu.GetGuestAttributesResponse.to_json(
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
                    "Received response for google.cloud.tpu_v2.TpuClient.get_guest_attributes",
                    extra={
                        "serviceName": "google.cloud.tpu.v2.Tpu",
                        "rpcName": "GetGuestAttributes",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetNode(_BaseTpuRestTransport._BaseGetNode, TpuRestStub):
        def __hash__(self):
            return hash("TpuRestTransport.GetNode")

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
            request: cloud_tpu.GetNodeRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cloud_tpu.Node:
            r"""Call the get node method over HTTP.

            Args:
                request (~.cloud_tpu.GetNodeRequest):
                    The request object. Request for [GetNode][google.cloud.tpu.v2.Tpu.GetNode].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cloud_tpu.Node:
                    A TPU instance.
            """

            http_options = _BaseTpuRestTransport._BaseGetNode._get_http_options()
            request, metadata = self._interceptor.pre_get_node(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseTpuRestTransport._BaseGetNode,
                    "_BaseGetNode__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.tpu_v2.TpuClient.GetNode",
                    extra={
                        "serviceName": "google.cloud.tpu.v2.Tpu",
                        "rpcName": "GetNode",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = TpuRestTransport._GetNode._get_response(
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
            resp = cloud_tpu.Node()
            pb_resp = cloud_tpu.Node.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_node(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_node_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = cloud_tpu.Node.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.tpu_v2.TpuClient.get_node",
                    extra={
                        "serviceName": "google.cloud.tpu.v2.Tpu",
                        "rpcName": "GetNode",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetQueuedResource(_BaseTpuRestTransport._BaseGetQueuedResource, TpuRestStub):
        def __hash__(self):
            return hash("TpuRestTransport.GetQueuedResource")

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
            request: cloud_tpu.GetQueuedResourceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cloud_tpu.QueuedResource:
            r"""Call the get queued resource method over HTTP.

            Args:
                request (~.cloud_tpu.GetQueuedResourceRequest):
                    The request object. Request for
                [GetQueuedResource][google.cloud.tpu.v2.Tpu.GetQueuedResource]
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cloud_tpu.QueuedResource:
                    A QueuedResource represents a request
                for resources that will be placed in a
                queue and fulfilled when the necessary
                resources are available.

            """

            http_options = (
                _BaseTpuRestTransport._BaseGetQueuedResource._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_queued_resource(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseTpuRestTransport._BaseGetQueuedResource,
                    "_BaseGetQueuedResource__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.tpu_v2.TpuClient.GetQueuedResource",
                    extra={
                        "serviceName": "google.cloud.tpu.v2.Tpu",
                        "rpcName": "GetQueuedResource",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = TpuRestTransport._GetQueuedResource._get_response(
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
            resp = cloud_tpu.QueuedResource()
            pb_resp = cloud_tpu.QueuedResource.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_queued_resource(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_queued_resource_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = cloud_tpu.QueuedResource.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.tpu_v2.TpuClient.get_queued_resource",
                    extra={
                        "serviceName": "google.cloud.tpu.v2.Tpu",
                        "rpcName": "GetQueuedResource",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetRuntimeVersion(_BaseTpuRestTransport._BaseGetRuntimeVersion, TpuRestStub):
        def __hash__(self):
            return hash("TpuRestTransport.GetRuntimeVersion")

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
            request: cloud_tpu.GetRuntimeVersionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cloud_tpu.RuntimeVersion:
            r"""Call the get runtime version method over HTTP.

            Args:
                request (~.cloud_tpu.GetRuntimeVersionRequest):
                    The request object. Request for
                [GetRuntimeVersion][google.cloud.tpu.v2.Tpu.GetRuntimeVersion].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cloud_tpu.RuntimeVersion:
                    A runtime version that a Node can be
                configured with.

            """

            http_options = (
                _BaseTpuRestTransport._BaseGetRuntimeVersion._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_runtime_version(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseTpuRestTransport._BaseGetRuntimeVersion,
                    "_BaseGetRuntimeVersion__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.tpu_v2.TpuClient.GetRuntimeVersion",
                    extra={
                        "serviceName": "google.cloud.tpu.v2.Tpu",
                        "rpcName": "GetRuntimeVersion",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = TpuRestTransport._GetRuntimeVersion._get_response(
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
            resp = cloud_tpu.RuntimeVersion()
            pb_resp = cloud_tpu.RuntimeVersion.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_runtime_version(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_runtime_version_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = cloud_tpu.RuntimeVersion.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.tpu_v2.TpuClient.get_runtime_version",
                    extra={
                        "serviceName": "google.cloud.tpu.v2.Tpu",
                        "rpcName": "GetRuntimeVersion",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListAcceleratorTypes(
        _BaseTpuRestTransport._BaseListAcceleratorTypes, TpuRestStub
    ):
        def __hash__(self):
            return hash("TpuRestTransport.ListAcceleratorTypes")

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
            request: cloud_tpu.ListAcceleratorTypesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cloud_tpu.ListAcceleratorTypesResponse:
            r"""Call the list accelerator types method over HTTP.

            Args:
                request (~.cloud_tpu.ListAcceleratorTypesRequest):
                    The request object. Request for
                [ListAcceleratorTypes][google.cloud.tpu.v2.Tpu.ListAcceleratorTypes].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cloud_tpu.ListAcceleratorTypesResponse:
                    Response for
                [ListAcceleratorTypes][google.cloud.tpu.v2.Tpu.ListAcceleratorTypes].

            """

            http_options = (
                _BaseTpuRestTransport._BaseListAcceleratorTypes._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_accelerator_types(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseTpuRestTransport._BaseListAcceleratorTypes,
                    "_BaseListAcceleratorTypes__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.tpu_v2.TpuClient.ListAcceleratorTypes",
                    extra={
                        "serviceName": "google.cloud.tpu.v2.Tpu",
                        "rpcName": "ListAcceleratorTypes",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = TpuRestTransport._ListAcceleratorTypes._get_response(
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
            resp = cloud_tpu.ListAcceleratorTypesResponse()
            pb_resp = cloud_tpu.ListAcceleratorTypesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_accelerator_types(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_accelerator_types_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = cloud_tpu.ListAcceleratorTypesResponse.to_json(
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
                    "Received response for google.cloud.tpu_v2.TpuClient.list_accelerator_types",
                    extra={
                        "serviceName": "google.cloud.tpu.v2.Tpu",
                        "rpcName": "ListAcceleratorTypes",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListNodes(_BaseTpuRestTransport._BaseListNodes, TpuRestStub):
        def __hash__(self):
            return hash("TpuRestTransport.ListNodes")

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
            request: cloud_tpu.ListNodesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cloud_tpu.ListNodesResponse:
            r"""Call the list nodes method over HTTP.

            Args:
                request (~.cloud_tpu.ListNodesRequest):
                    The request object. Request for
                [ListNodes][google.cloud.tpu.v2.Tpu.ListNodes].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cloud_tpu.ListNodesResponse:
                    Response for
                [ListNodes][google.cloud.tpu.v2.Tpu.ListNodes].

            """

            http_options = _BaseTpuRestTransport._BaseListNodes._get_http_options()
            request, metadata = self._interceptor.pre_list_nodes(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseTpuRestTransport._BaseListNodes,
                    "_BaseListNodes__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.tpu_v2.TpuClient.ListNodes",
                    extra={
                        "serviceName": "google.cloud.tpu.v2.Tpu",
                        "rpcName": "ListNodes",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = TpuRestTransport._ListNodes._get_response(
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
            resp = cloud_tpu.ListNodesResponse()
            pb_resp = cloud_tpu.ListNodesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_nodes(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_nodes_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = cloud_tpu.ListNodesResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.tpu_v2.TpuClient.list_nodes",
                    extra={
                        "serviceName": "google.cloud.tpu.v2.Tpu",
                        "rpcName": "ListNodes",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListQueuedResources(
        _BaseTpuRestTransport._BaseListQueuedResources, TpuRestStub
    ):
        def __hash__(self):
            return hash("TpuRestTransport.ListQueuedResources")

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
            request: cloud_tpu.ListQueuedResourcesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cloud_tpu.ListQueuedResourcesResponse:
            r"""Call the list queued resources method over HTTP.

            Args:
                request (~.cloud_tpu.ListQueuedResourcesRequest):
                    The request object. Request for
                [ListQueuedResources][google.cloud.tpu.v2.Tpu.ListQueuedResources].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cloud_tpu.ListQueuedResourcesResponse:
                    Response for
                [ListQueuedResources][google.cloud.tpu.v2.Tpu.ListQueuedResources].

            """

            http_options = (
                _BaseTpuRestTransport._BaseListQueuedResources._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_queued_resources(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseTpuRestTransport._BaseListQueuedResources,
                    "_BaseListQueuedResources__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.tpu_v2.TpuClient.ListQueuedResources",
                    extra={
                        "serviceName": "google.cloud.tpu.v2.Tpu",
                        "rpcName": "ListQueuedResources",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = TpuRestTransport._ListQueuedResources._get_response(
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
            resp = cloud_tpu.ListQueuedResourcesResponse()
            pb_resp = cloud_tpu.ListQueuedResourcesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_queued_resources(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_queued_resources_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = cloud_tpu.ListQueuedResourcesResponse.to_json(
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
                    "Received response for google.cloud.tpu_v2.TpuClient.list_queued_resources",
                    extra={
                        "serviceName": "google.cloud.tpu.v2.Tpu",
                        "rpcName": "ListQueuedResources",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListRuntimeVersions(
        _BaseTpuRestTransport._BaseListRuntimeVersions, TpuRestStub
    ):
        def __hash__(self):
            return hash("TpuRestTransport.ListRuntimeVersions")

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
            request: cloud_tpu.ListRuntimeVersionsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cloud_tpu.ListRuntimeVersionsResponse:
            r"""Call the list runtime versions method over HTTP.

            Args:
                request (~.cloud_tpu.ListRuntimeVersionsRequest):
                    The request object. Request for
                [ListRuntimeVersions][google.cloud.tpu.v2.Tpu.ListRuntimeVersions].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cloud_tpu.ListRuntimeVersionsResponse:
                    Response for
                [ListRuntimeVersions][google.cloud.tpu.v2.Tpu.ListRuntimeVersions].

            """

            http_options = (
                _BaseTpuRestTransport._BaseListRuntimeVersions._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_runtime_versions(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseTpuRestTransport._BaseListRuntimeVersions,
                    "_BaseListRuntimeVersions__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.tpu_v2.TpuClient.ListRuntimeVersions",
                    extra={
                        "serviceName": "google.cloud.tpu.v2.Tpu",
                        "rpcName": "ListRuntimeVersions",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = TpuRestTransport._ListRuntimeVersions._get_response(
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
            resp = cloud_tpu.ListRuntimeVersionsResponse()
            pb_resp = cloud_tpu.ListRuntimeVersionsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_runtime_versions(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_runtime_versions_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = cloud_tpu.ListRuntimeVersionsResponse.to_json(
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
                    "Received response for google.cloud.tpu_v2.TpuClient.list_runtime_versions",
                    extra={
                        "serviceName": "google.cloud.tpu.v2.Tpu",
                        "rpcName": "ListRuntimeVersions",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ResetQueuedResource(
        _BaseTpuRestTransport._BaseResetQueuedResource, TpuRestStub
    ):
        def __hash__(self):
            return hash("TpuRestTransport.ResetQueuedResource")

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
            request: cloud_tpu.ResetQueuedResourceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the reset queued resource method over HTTP.

            Args:
                request (~.cloud_tpu.ResetQueuedResourceRequest):
                    The request object. Request for
                [ResetQueuedResource][google.cloud.tpu.v2.Tpu.ResetQueuedResource].
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
                _BaseTpuRestTransport._BaseResetQueuedResource._get_http_options()
            )
            request, metadata = self._interceptor.pre_reset_queued_resource(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseTpuRestTransport._BaseResetQueuedResource,
                    "_BaseResetQueuedResource__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.tpu_v2.TpuClient.ResetQueuedResource",
                    extra={
                        "serviceName": "google.cloud.tpu.v2.Tpu",
                        "rpcName": "ResetQueuedResource",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = TpuRestTransport._ResetQueuedResource._get_response(
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

            resp = self._interceptor.post_reset_queued_resource(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_reset_queued_resource_with_metadata(
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
                    "Received response for google.cloud.tpu_v2.TpuClient.reset_queued_resource",
                    extra={
                        "serviceName": "google.cloud.tpu.v2.Tpu",
                        "rpcName": "ResetQueuedResource",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _StartNode(_BaseTpuRestTransport._BaseStartNode, TpuRestStub):
        def __hash__(self):
            return hash("TpuRestTransport.StartNode")

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
            request: cloud_tpu.StartNodeRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the start node method over HTTP.

            Args:
                request (~.cloud_tpu.StartNodeRequest):
                    The request object. Request for
                [StartNode][google.cloud.tpu.v2.Tpu.StartNode].
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

            http_options = _BaseTpuRestTransport._BaseStartNode._get_http_options()
            request, metadata = self._interceptor.pre_start_node(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseTpuRestTransport._BaseStartNode,
                    "_BaseStartNode__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.tpu_v2.TpuClient.StartNode",
                    extra={
                        "serviceName": "google.cloud.tpu.v2.Tpu",
                        "rpcName": "StartNode",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = TpuRestTransport._StartNode._get_response(
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

            resp = self._interceptor.post_start_node(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_start_node_with_metadata(
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
                    "Received response for google.cloud.tpu_v2.TpuClient.start_node",
                    extra={
                        "serviceName": "google.cloud.tpu.v2.Tpu",
                        "rpcName": "StartNode",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _StopNode(_BaseTpuRestTransport._BaseStopNode, TpuRestStub):
        def __hash__(self):
            return hash("TpuRestTransport.StopNode")

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
            request: cloud_tpu.StopNodeRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the stop node method over HTTP.

            Args:
                request (~.cloud_tpu.StopNodeRequest):
                    The request object. Request for
                [StopNode][google.cloud.tpu.v2.Tpu.StopNode].
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

            http_options = _BaseTpuRestTransport._BaseStopNode._get_http_options()
            request, metadata = self._interceptor.pre_stop_node(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseTpuRestTransport._BaseStopNode,
                    "_BaseStopNode__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.tpu_v2.TpuClient.StopNode",
                    extra={
                        "serviceName": "google.cloud.tpu.v2.Tpu",
                        "rpcName": "StopNode",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = TpuRestTransport._StopNode._get_response(
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

            resp = self._interceptor.post_stop_node(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_stop_node_with_metadata(
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
                    "Received response for google.cloud.tpu_v2.TpuClient.stop_node",
                    extra={
                        "serviceName": "google.cloud.tpu.v2.Tpu",
                        "rpcName": "StopNode",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateNode(_BaseTpuRestTransport._BaseUpdateNode, TpuRestStub):
        def __hash__(self):
            return hash("TpuRestTransport.UpdateNode")

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
            request: cloud_tpu.UpdateNodeRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update node method over HTTP.

            Args:
                request (~.cloud_tpu.UpdateNodeRequest):
                    The request object. Request for
                [UpdateNode][google.cloud.tpu.v2.Tpu.UpdateNode].
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

            http_options = _BaseTpuRestTransport._BaseUpdateNode._get_http_options()
            request, metadata = self._interceptor.pre_update_node(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseTpuRestTransport._BaseUpdateNode,
                    "_BaseUpdateNode__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.tpu_v2.TpuClient.UpdateNode",
                    extra={
                        "serviceName": "google.cloud.tpu.v2.Tpu",
                        "rpcName": "UpdateNode",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = TpuRestTransport._UpdateNode._get_response(
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

            resp = self._interceptor.post_update_node(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_node_with_metadata(
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
                    "Received response for google.cloud.tpu_v2.TpuClient.update_node",
                    extra={
                        "serviceName": "google.cloud.tpu.v2.Tpu",
                        "rpcName": "UpdateNode",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def create_node(
        self,
    ) -> Callable[[cloud_tpu.CreateNodeRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateNode(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_queued_resource(
        self,
    ) -> Callable[[cloud_tpu.CreateQueuedResourceRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateQueuedResource(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_node(
        self,
    ) -> Callable[[cloud_tpu.DeleteNodeRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteNode(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_queued_resource(
        self,
    ) -> Callable[[cloud_tpu.DeleteQueuedResourceRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteQueuedResource(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def generate_service_identity(
        self,
    ) -> Callable[
        [cloud_tpu.GenerateServiceIdentityRequest],
        cloud_tpu.GenerateServiceIdentityResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GenerateServiceIdentity(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def get_accelerator_type(
        self,
    ) -> Callable[[cloud_tpu.GetAcceleratorTypeRequest], cloud_tpu.AcceleratorType]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetAcceleratorType(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_guest_attributes(
        self,
    ) -> Callable[
        [cloud_tpu.GetGuestAttributesRequest], cloud_tpu.GetGuestAttributesResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetGuestAttributes(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_node(self) -> Callable[[cloud_tpu.GetNodeRequest], cloud_tpu.Node]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetNode(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_queued_resource(
        self,
    ) -> Callable[[cloud_tpu.GetQueuedResourceRequest], cloud_tpu.QueuedResource]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetQueuedResource(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_runtime_version(
        self,
    ) -> Callable[[cloud_tpu.GetRuntimeVersionRequest], cloud_tpu.RuntimeVersion]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetRuntimeVersion(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_accelerator_types(
        self,
    ) -> Callable[
        [cloud_tpu.ListAcceleratorTypesRequest], cloud_tpu.ListAcceleratorTypesResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListAcceleratorTypes(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_nodes(
        self,
    ) -> Callable[[cloud_tpu.ListNodesRequest], cloud_tpu.ListNodesResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListNodes(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_queued_resources(
        self,
    ) -> Callable[
        [cloud_tpu.ListQueuedResourcesRequest], cloud_tpu.ListQueuedResourcesResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListQueuedResources(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_runtime_versions(
        self,
    ) -> Callable[
        [cloud_tpu.ListRuntimeVersionsRequest], cloud_tpu.ListRuntimeVersionsResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListRuntimeVersions(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def reset_queued_resource(
        self,
    ) -> Callable[[cloud_tpu.ResetQueuedResourceRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ResetQueuedResource(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def start_node(
        self,
    ) -> Callable[[cloud_tpu.StartNodeRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._StartNode(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def stop_node(
        self,
    ) -> Callable[[cloud_tpu.StopNodeRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._StopNode(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_node(
        self,
    ) -> Callable[[cloud_tpu.UpdateNodeRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateNode(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_location(self):
        return self._GetLocation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetLocation(_BaseTpuRestTransport._BaseGetLocation, TpuRestStub):
        def __hash__(self):
            return hash("TpuRestTransport.GetLocation")

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

            http_options = _BaseTpuRestTransport._BaseGetLocation._get_http_options()
            request, metadata = self._interceptor.pre_get_location(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseTpuRestTransport._BaseGetLocation,
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
                    f"Sending request for google.cloud.tpu_v2.TpuClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.tpu.v2.Tpu",
                        "rpcName": "GetLocation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = TpuRestTransport._GetLocation._get_response(
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
                    "Received response for google.cloud.tpu_v2.TpuAsyncClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.tpu.v2.Tpu",
                        "rpcName": "GetLocation",
                        "httpResponse": http_response,
                        "metadata": http_response["headers"],
                    },
                )
            return resp

    @property
    def list_locations(self):
        return self._ListLocations(self._session, self._host, self._interceptor)  # type: ignore

    class _ListLocations(_BaseTpuRestTransport._BaseListLocations, TpuRestStub):
        def __hash__(self):
            return hash("TpuRestTransport.ListLocations")

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

            http_options = _BaseTpuRestTransport._BaseListLocations._get_http_options()
            request, metadata = self._interceptor.pre_list_locations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseTpuRestTransport._BaseListLocations,
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
                    f"Sending request for google.cloud.tpu_v2.TpuClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.tpu.v2.Tpu",
                        "rpcName": "ListLocations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = TpuRestTransport._ListLocations._get_response(
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
                    "Received response for google.cloud.tpu_v2.TpuAsyncClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.tpu.v2.Tpu",
                        "rpcName": "ListLocations",
                        "httpResponse": http_response,
                        "metadata": http_response["headers"],
                    },
                )
            return resp

    @property
    def cancel_operation(self):
        return self._CancelOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _CancelOperation(_BaseTpuRestTransport._BaseCancelOperation, TpuRestStub):
        def __hash__(self):
            return hash("TpuRestTransport.CancelOperation")

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
                _BaseTpuRestTransport._BaseCancelOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_cancel_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseTpuRestTransport._BaseCancelOperation,
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
                    f"Sending request for google.cloud.tpu_v2.TpuClient.CancelOperation",
                    extra={
                        "serviceName": "google.cloud.tpu.v2.Tpu",
                        "rpcName": "CancelOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = TpuRestTransport._CancelOperation._get_response(
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

            return self._interceptor.post_cancel_operation(None)

    @property
    def delete_operation(self):
        return self._DeleteOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _DeleteOperation(_BaseTpuRestTransport._BaseDeleteOperation, TpuRestStub):
        def __hash__(self):
            return hash("TpuRestTransport.DeleteOperation")

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
                _BaseTpuRestTransport._BaseDeleteOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseTpuRestTransport._BaseDeleteOperation,
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
                    f"Sending request for google.cloud.tpu_v2.TpuClient.DeleteOperation",
                    extra={
                        "serviceName": "google.cloud.tpu.v2.Tpu",
                        "rpcName": "DeleteOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = TpuRestTransport._DeleteOperation._get_response(
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

    class _GetOperation(_BaseTpuRestTransport._BaseGetOperation, TpuRestStub):
        def __hash__(self):
            return hash("TpuRestTransport.GetOperation")

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

            http_options = _BaseTpuRestTransport._BaseGetOperation._get_http_options()
            request, metadata = self._interceptor.pre_get_operation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseTpuRestTransport._BaseGetOperation,
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
                    f"Sending request for google.cloud.tpu_v2.TpuClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.tpu.v2.Tpu",
                        "rpcName": "GetOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = TpuRestTransport._GetOperation._get_response(
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
                    "Received response for google.cloud.tpu_v2.TpuAsyncClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.tpu.v2.Tpu",
                        "rpcName": "GetOperation",
                        "httpResponse": http_response,
                        "metadata": http_response["headers"],
                    },
                )
            return resp

    @property
    def list_operations(self):
        return self._ListOperations(self._session, self._host, self._interceptor)  # type: ignore

    class _ListOperations(_BaseTpuRestTransport._BaseListOperations, TpuRestStub):
        def __hash__(self):
            return hash("TpuRestTransport.ListOperations")

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

            http_options = _BaseTpuRestTransport._BaseListOperations._get_http_options()
            request, metadata = self._interceptor.pre_list_operations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseTpuRestTransport._BaseListOperations,
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
                    f"Sending request for google.cloud.tpu_v2.TpuClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.tpu.v2.Tpu",
                        "rpcName": "ListOperations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = TpuRestTransport._ListOperations._get_response(
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
                    "Received response for google.cloud.tpu_v2.TpuAsyncClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.tpu.v2.Tpu",
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


__all__ = ("TpuRestTransport",)
