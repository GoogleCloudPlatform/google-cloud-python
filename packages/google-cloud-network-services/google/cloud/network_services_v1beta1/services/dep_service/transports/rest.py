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

from google.cloud.network_services_v1beta1._compat import transcode_request
from google.cloud.network_services_v1beta1.types import dep

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseDepServiceRestTransport

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


class DepServiceRestInterceptor:
    """Interceptor for DepService.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the DepServiceRestTransport.

    .. code-block:: python
        class MyCustomDepServiceInterceptor(DepServiceRestInterceptor):
            def pre_create_extension_binding(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_extension_binding(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_lb_route_extension(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_lb_route_extension(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_lb_traffic_extension(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_lb_traffic_extension(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_extension_binding(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_extension_binding(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_lb_route_extension(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_lb_route_extension(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_lb_traffic_extension(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_lb_traffic_extension(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_extension_binding(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_extension_binding(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_lb_route_extension(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_lb_route_extension(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_lb_traffic_extension(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_lb_traffic_extension(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_extension_bindings(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_extension_bindings(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_lb_route_extensions(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_lb_route_extensions(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_lb_traffic_extensions(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_lb_traffic_extensions(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_extension_binding(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_extension_binding(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_lb_route_extension(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_lb_route_extension(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_lb_traffic_extension(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_lb_traffic_extension(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = DepServiceRestTransport(interceptor=MyCustomDepServiceInterceptor())
        client = DepServiceClient(transport=transport)


    """

    def pre_create_extension_binding(
        self,
        request: dep.CreateExtensionBindingRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dep.CreateExtensionBindingRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_extension_binding

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DepService server.
        """
        return request, metadata

    def post_create_extension_binding(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_extension_binding

        DEPRECATED. Please use the `post_create_extension_binding_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DepService server but before
        it is returned to user code. This `post_create_extension_binding` interceptor runs
        before the `post_create_extension_binding_with_metadata` interceptor.
        """
        return response

    def post_create_extension_binding_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_extension_binding

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DepService server but before it is returned to user code.

        We recommend only using this `post_create_extension_binding_with_metadata`
        interceptor in new development instead of the `post_create_extension_binding` interceptor.
        When both interceptors are used, this `post_create_extension_binding_with_metadata` interceptor runs after the
        `post_create_extension_binding` interceptor. The (possibly modified) response returned by
        `post_create_extension_binding` will be passed to
        `post_create_extension_binding_with_metadata`.
        """
        return response, metadata

    def pre_create_lb_route_extension(
        self,
        request: dep.CreateLbRouteExtensionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dep.CreateLbRouteExtensionRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_lb_route_extension

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DepService server.
        """
        return request, metadata

    def post_create_lb_route_extension(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_lb_route_extension

        DEPRECATED. Please use the `post_create_lb_route_extension_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DepService server but before
        it is returned to user code. This `post_create_lb_route_extension` interceptor runs
        before the `post_create_lb_route_extension_with_metadata` interceptor.
        """
        return response

    def post_create_lb_route_extension_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_lb_route_extension

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DepService server but before it is returned to user code.

        We recommend only using this `post_create_lb_route_extension_with_metadata`
        interceptor in new development instead of the `post_create_lb_route_extension` interceptor.
        When both interceptors are used, this `post_create_lb_route_extension_with_metadata` interceptor runs after the
        `post_create_lb_route_extension` interceptor. The (possibly modified) response returned by
        `post_create_lb_route_extension` will be passed to
        `post_create_lb_route_extension_with_metadata`.
        """
        return response, metadata

    def pre_create_lb_traffic_extension(
        self,
        request: dep.CreateLbTrafficExtensionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dep.CreateLbTrafficExtensionRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_lb_traffic_extension

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DepService server.
        """
        return request, metadata

    def post_create_lb_traffic_extension(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_lb_traffic_extension

        DEPRECATED. Please use the `post_create_lb_traffic_extension_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DepService server but before
        it is returned to user code. This `post_create_lb_traffic_extension` interceptor runs
        before the `post_create_lb_traffic_extension_with_metadata` interceptor.
        """
        return response

    def post_create_lb_traffic_extension_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_lb_traffic_extension

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DepService server but before it is returned to user code.

        We recommend only using this `post_create_lb_traffic_extension_with_metadata`
        interceptor in new development instead of the `post_create_lb_traffic_extension` interceptor.
        When both interceptors are used, this `post_create_lb_traffic_extension_with_metadata` interceptor runs after the
        `post_create_lb_traffic_extension` interceptor. The (possibly modified) response returned by
        `post_create_lb_traffic_extension` will be passed to
        `post_create_lb_traffic_extension_with_metadata`.
        """
        return response, metadata

    def pre_delete_extension_binding(
        self,
        request: dep.DeleteExtensionBindingRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dep.DeleteExtensionBindingRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_extension_binding

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DepService server.
        """
        return request, metadata

    def post_delete_extension_binding(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_extension_binding

        DEPRECATED. Please use the `post_delete_extension_binding_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DepService server but before
        it is returned to user code. This `post_delete_extension_binding` interceptor runs
        before the `post_delete_extension_binding_with_metadata` interceptor.
        """
        return response

    def post_delete_extension_binding_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_extension_binding

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DepService server but before it is returned to user code.

        We recommend only using this `post_delete_extension_binding_with_metadata`
        interceptor in new development instead of the `post_delete_extension_binding` interceptor.
        When both interceptors are used, this `post_delete_extension_binding_with_metadata` interceptor runs after the
        `post_delete_extension_binding` interceptor. The (possibly modified) response returned by
        `post_delete_extension_binding` will be passed to
        `post_delete_extension_binding_with_metadata`.
        """
        return response, metadata

    def pre_delete_lb_route_extension(
        self,
        request: dep.DeleteLbRouteExtensionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dep.DeleteLbRouteExtensionRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_lb_route_extension

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DepService server.
        """
        return request, metadata

    def post_delete_lb_route_extension(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_lb_route_extension

        DEPRECATED. Please use the `post_delete_lb_route_extension_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DepService server but before
        it is returned to user code. This `post_delete_lb_route_extension` interceptor runs
        before the `post_delete_lb_route_extension_with_metadata` interceptor.
        """
        return response

    def post_delete_lb_route_extension_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_lb_route_extension

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DepService server but before it is returned to user code.

        We recommend only using this `post_delete_lb_route_extension_with_metadata`
        interceptor in new development instead of the `post_delete_lb_route_extension` interceptor.
        When both interceptors are used, this `post_delete_lb_route_extension_with_metadata` interceptor runs after the
        `post_delete_lb_route_extension` interceptor. The (possibly modified) response returned by
        `post_delete_lb_route_extension` will be passed to
        `post_delete_lb_route_extension_with_metadata`.
        """
        return response, metadata

    def pre_delete_lb_traffic_extension(
        self,
        request: dep.DeleteLbTrafficExtensionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dep.DeleteLbTrafficExtensionRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_lb_traffic_extension

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DepService server.
        """
        return request, metadata

    def post_delete_lb_traffic_extension(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_lb_traffic_extension

        DEPRECATED. Please use the `post_delete_lb_traffic_extension_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DepService server but before
        it is returned to user code. This `post_delete_lb_traffic_extension` interceptor runs
        before the `post_delete_lb_traffic_extension_with_metadata` interceptor.
        """
        return response

    def post_delete_lb_traffic_extension_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_lb_traffic_extension

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DepService server but before it is returned to user code.

        We recommend only using this `post_delete_lb_traffic_extension_with_metadata`
        interceptor in new development instead of the `post_delete_lb_traffic_extension` interceptor.
        When both interceptors are used, this `post_delete_lb_traffic_extension_with_metadata` interceptor runs after the
        `post_delete_lb_traffic_extension` interceptor. The (possibly modified) response returned by
        `post_delete_lb_traffic_extension` will be passed to
        `post_delete_lb_traffic_extension_with_metadata`.
        """
        return response, metadata

    def pre_get_extension_binding(
        self,
        request: dep.GetExtensionBindingRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[dep.GetExtensionBindingRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_extension_binding

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DepService server.
        """
        return request, metadata

    def post_get_extension_binding(
        self, response: dep.ExtensionBinding
    ) -> dep.ExtensionBinding:
        """Post-rpc interceptor for get_extension_binding

        DEPRECATED. Please use the `post_get_extension_binding_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DepService server but before
        it is returned to user code. This `post_get_extension_binding` interceptor runs
        before the `post_get_extension_binding_with_metadata` interceptor.
        """
        return response

    def post_get_extension_binding_with_metadata(
        self,
        response: dep.ExtensionBinding,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[dep.ExtensionBinding, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_extension_binding

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DepService server but before it is returned to user code.

        We recommend only using this `post_get_extension_binding_with_metadata`
        interceptor in new development instead of the `post_get_extension_binding` interceptor.
        When both interceptors are used, this `post_get_extension_binding_with_metadata` interceptor runs after the
        `post_get_extension_binding` interceptor. The (possibly modified) response returned by
        `post_get_extension_binding` will be passed to
        `post_get_extension_binding_with_metadata`.
        """
        return response, metadata

    def pre_get_lb_route_extension(
        self,
        request: dep.GetLbRouteExtensionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[dep.GetLbRouteExtensionRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_lb_route_extension

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DepService server.
        """
        return request, metadata

    def post_get_lb_route_extension(
        self, response: dep.LbRouteExtension
    ) -> dep.LbRouteExtension:
        """Post-rpc interceptor for get_lb_route_extension

        DEPRECATED. Please use the `post_get_lb_route_extension_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DepService server but before
        it is returned to user code. This `post_get_lb_route_extension` interceptor runs
        before the `post_get_lb_route_extension_with_metadata` interceptor.
        """
        return response

    def post_get_lb_route_extension_with_metadata(
        self,
        response: dep.LbRouteExtension,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[dep.LbRouteExtension, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_lb_route_extension

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DepService server but before it is returned to user code.

        We recommend only using this `post_get_lb_route_extension_with_metadata`
        interceptor in new development instead of the `post_get_lb_route_extension` interceptor.
        When both interceptors are used, this `post_get_lb_route_extension_with_metadata` interceptor runs after the
        `post_get_lb_route_extension` interceptor. The (possibly modified) response returned by
        `post_get_lb_route_extension` will be passed to
        `post_get_lb_route_extension_with_metadata`.
        """
        return response, metadata

    def pre_get_lb_traffic_extension(
        self,
        request: dep.GetLbTrafficExtensionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dep.GetLbTrafficExtensionRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_lb_traffic_extension

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DepService server.
        """
        return request, metadata

    def post_get_lb_traffic_extension(
        self, response: dep.LbTrafficExtension
    ) -> dep.LbTrafficExtension:
        """Post-rpc interceptor for get_lb_traffic_extension

        DEPRECATED. Please use the `post_get_lb_traffic_extension_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DepService server but before
        it is returned to user code. This `post_get_lb_traffic_extension` interceptor runs
        before the `post_get_lb_traffic_extension_with_metadata` interceptor.
        """
        return response

    def post_get_lb_traffic_extension_with_metadata(
        self,
        response: dep.LbTrafficExtension,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[dep.LbTrafficExtension, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_lb_traffic_extension

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DepService server but before it is returned to user code.

        We recommend only using this `post_get_lb_traffic_extension_with_metadata`
        interceptor in new development instead of the `post_get_lb_traffic_extension` interceptor.
        When both interceptors are used, this `post_get_lb_traffic_extension_with_metadata` interceptor runs after the
        `post_get_lb_traffic_extension` interceptor. The (possibly modified) response returned by
        `post_get_lb_traffic_extension` will be passed to
        `post_get_lb_traffic_extension_with_metadata`.
        """
        return response, metadata

    def pre_list_extension_bindings(
        self,
        request: dep.ListExtensionBindingsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dep.ListExtensionBindingsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_extension_bindings

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DepService server.
        """
        return request, metadata

    def post_list_extension_bindings(
        self, response: dep.ListExtensionBindingsResponse
    ) -> dep.ListExtensionBindingsResponse:
        """Post-rpc interceptor for list_extension_bindings

        DEPRECATED. Please use the `post_list_extension_bindings_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DepService server but before
        it is returned to user code. This `post_list_extension_bindings` interceptor runs
        before the `post_list_extension_bindings_with_metadata` interceptor.
        """
        return response

    def post_list_extension_bindings_with_metadata(
        self,
        response: dep.ListExtensionBindingsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dep.ListExtensionBindingsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_extension_bindings

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DepService server but before it is returned to user code.

        We recommend only using this `post_list_extension_bindings_with_metadata`
        interceptor in new development instead of the `post_list_extension_bindings` interceptor.
        When both interceptors are used, this `post_list_extension_bindings_with_metadata` interceptor runs after the
        `post_list_extension_bindings` interceptor. The (possibly modified) response returned by
        `post_list_extension_bindings` will be passed to
        `post_list_extension_bindings_with_metadata`.
        """
        return response, metadata

    def pre_list_lb_route_extensions(
        self,
        request: dep.ListLbRouteExtensionsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dep.ListLbRouteExtensionsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_lb_route_extensions

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DepService server.
        """
        return request, metadata

    def post_list_lb_route_extensions(
        self, response: dep.ListLbRouteExtensionsResponse
    ) -> dep.ListLbRouteExtensionsResponse:
        """Post-rpc interceptor for list_lb_route_extensions

        DEPRECATED. Please use the `post_list_lb_route_extensions_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DepService server but before
        it is returned to user code. This `post_list_lb_route_extensions` interceptor runs
        before the `post_list_lb_route_extensions_with_metadata` interceptor.
        """
        return response

    def post_list_lb_route_extensions_with_metadata(
        self,
        response: dep.ListLbRouteExtensionsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dep.ListLbRouteExtensionsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_lb_route_extensions

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DepService server but before it is returned to user code.

        We recommend only using this `post_list_lb_route_extensions_with_metadata`
        interceptor in new development instead of the `post_list_lb_route_extensions` interceptor.
        When both interceptors are used, this `post_list_lb_route_extensions_with_metadata` interceptor runs after the
        `post_list_lb_route_extensions` interceptor. The (possibly modified) response returned by
        `post_list_lb_route_extensions` will be passed to
        `post_list_lb_route_extensions_with_metadata`.
        """
        return response, metadata

    def pre_list_lb_traffic_extensions(
        self,
        request: dep.ListLbTrafficExtensionsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dep.ListLbTrafficExtensionsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_lb_traffic_extensions

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DepService server.
        """
        return request, metadata

    def post_list_lb_traffic_extensions(
        self, response: dep.ListLbTrafficExtensionsResponse
    ) -> dep.ListLbTrafficExtensionsResponse:
        """Post-rpc interceptor for list_lb_traffic_extensions

        DEPRECATED. Please use the `post_list_lb_traffic_extensions_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DepService server but before
        it is returned to user code. This `post_list_lb_traffic_extensions` interceptor runs
        before the `post_list_lb_traffic_extensions_with_metadata` interceptor.
        """
        return response

    def post_list_lb_traffic_extensions_with_metadata(
        self,
        response: dep.ListLbTrafficExtensionsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dep.ListLbTrafficExtensionsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_lb_traffic_extensions

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DepService server but before it is returned to user code.

        We recommend only using this `post_list_lb_traffic_extensions_with_metadata`
        interceptor in new development instead of the `post_list_lb_traffic_extensions` interceptor.
        When both interceptors are used, this `post_list_lb_traffic_extensions_with_metadata` interceptor runs after the
        `post_list_lb_traffic_extensions` interceptor. The (possibly modified) response returned by
        `post_list_lb_traffic_extensions` will be passed to
        `post_list_lb_traffic_extensions_with_metadata`.
        """
        return response, metadata

    def pre_update_extension_binding(
        self,
        request: dep.UpdateExtensionBindingRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dep.UpdateExtensionBindingRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_extension_binding

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DepService server.
        """
        return request, metadata

    def post_update_extension_binding(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_extension_binding

        DEPRECATED. Please use the `post_update_extension_binding_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DepService server but before
        it is returned to user code. This `post_update_extension_binding` interceptor runs
        before the `post_update_extension_binding_with_metadata` interceptor.
        """
        return response

    def post_update_extension_binding_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_extension_binding

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DepService server but before it is returned to user code.

        We recommend only using this `post_update_extension_binding_with_metadata`
        interceptor in new development instead of the `post_update_extension_binding` interceptor.
        When both interceptors are used, this `post_update_extension_binding_with_metadata` interceptor runs after the
        `post_update_extension_binding` interceptor. The (possibly modified) response returned by
        `post_update_extension_binding` will be passed to
        `post_update_extension_binding_with_metadata`.
        """
        return response, metadata

    def pre_update_lb_route_extension(
        self,
        request: dep.UpdateLbRouteExtensionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dep.UpdateLbRouteExtensionRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_lb_route_extension

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DepService server.
        """
        return request, metadata

    def post_update_lb_route_extension(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_lb_route_extension

        DEPRECATED. Please use the `post_update_lb_route_extension_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DepService server but before
        it is returned to user code. This `post_update_lb_route_extension` interceptor runs
        before the `post_update_lb_route_extension_with_metadata` interceptor.
        """
        return response

    def post_update_lb_route_extension_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_lb_route_extension

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DepService server but before it is returned to user code.

        We recommend only using this `post_update_lb_route_extension_with_metadata`
        interceptor in new development instead of the `post_update_lb_route_extension` interceptor.
        When both interceptors are used, this `post_update_lb_route_extension_with_metadata` interceptor runs after the
        `post_update_lb_route_extension` interceptor. The (possibly modified) response returned by
        `post_update_lb_route_extension` will be passed to
        `post_update_lb_route_extension_with_metadata`.
        """
        return response, metadata

    def pre_update_lb_traffic_extension(
        self,
        request: dep.UpdateLbTrafficExtensionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dep.UpdateLbTrafficExtensionRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_lb_traffic_extension

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DepService server.
        """
        return request, metadata

    def post_update_lb_traffic_extension(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_lb_traffic_extension

        DEPRECATED. Please use the `post_update_lb_traffic_extension_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DepService server but before
        it is returned to user code. This `post_update_lb_traffic_extension` interceptor runs
        before the `post_update_lb_traffic_extension_with_metadata` interceptor.
        """
        return response

    def post_update_lb_traffic_extension_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_lb_traffic_extension

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DepService server but before it is returned to user code.

        We recommend only using this `post_update_lb_traffic_extension_with_metadata`
        interceptor in new development instead of the `post_update_lb_traffic_extension` interceptor.
        When both interceptors are used, this `post_update_lb_traffic_extension_with_metadata` interceptor runs after the
        `post_update_lb_traffic_extension` interceptor. The (possibly modified) response returned by
        `post_update_lb_traffic_extension` will be passed to
        `post_update_lb_traffic_extension_with_metadata`.
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
        before they are sent to the DepService server.
        """
        return request, metadata

    def post_get_location(
        self, response: locations_pb2.Location
    ) -> locations_pb2.Location:
        """Post-rpc interceptor for get_location

        Override in a subclass to manipulate the response
        after it is returned by the DepService server but before
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
        before they are sent to the DepService server.
        """
        return request, metadata

    def post_list_locations(
        self, response: locations_pb2.ListLocationsResponse
    ) -> locations_pb2.ListLocationsResponse:
        """Post-rpc interceptor for list_locations

        Override in a subclass to manipulate the response
        after it is returned by the DepService server but before
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
        before they are sent to the DepService server.
        """
        return request, metadata

    def post_get_iam_policy(self, response: policy_pb2.Policy) -> policy_pb2.Policy:
        """Post-rpc interceptor for get_iam_policy

        Override in a subclass to manipulate the response
        after it is returned by the DepService server but before
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
        before they are sent to the DepService server.
        """
        return request, metadata

    def post_set_iam_policy(self, response: policy_pb2.Policy) -> policy_pb2.Policy:
        """Post-rpc interceptor for set_iam_policy

        Override in a subclass to manipulate the response
        after it is returned by the DepService server but before
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
        before they are sent to the DepService server.
        """
        return request, metadata

    def post_test_iam_permissions(
        self, response: iam_policy_pb2.TestIamPermissionsResponse
    ) -> iam_policy_pb2.TestIamPermissionsResponse:
        """Post-rpc interceptor for test_iam_permissions

        Override in a subclass to manipulate the response
        after it is returned by the DepService server but before
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
        before they are sent to the DepService server.
        """
        return request, metadata

    def post_cancel_operation(self, response: None) -> None:
        """Post-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the response
        after it is returned by the DepService server but before
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
        before they are sent to the DepService server.
        """
        return request, metadata

    def post_delete_operation(self, response: None) -> None:
        """Post-rpc interceptor for delete_operation

        Override in a subclass to manipulate the response
        after it is returned by the DepService server but before
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
        before they are sent to the DepService server.
        """
        return request, metadata

    def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the DepService server but before
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
        before they are sent to the DepService server.
        """
        return request, metadata

    def post_list_operations(
        self, response: operations_pb2.ListOperationsResponse
    ) -> operations_pb2.ListOperationsResponse:
        """Post-rpc interceptor for list_operations

        Override in a subclass to manipulate the response
        after it is returned by the DepService server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class DepServiceRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: DepServiceRestInterceptor


class DepServiceRestTransport(_BaseDepServiceRestTransport):
    """REST backend synchronous transport for DepService.

    Service describing handlers for resources.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "networkservices.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[DepServiceRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'networkservices.googleapis.com').
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
            interceptor (Optional[DepServiceRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or DepServiceRestInterceptor()
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
                        "uri": "/v1beta1/{name=projects/*/locations/*/operations/*}:cancel",
                        "body": "*",
                    },
                ],
                "google.longrunning.Operations.DeleteOperation": [
                    {
                        "method": "delete",
                        "uri": "/v1beta1/{name=projects/*/locations/*/operations/*}",
                    },
                ],
                "google.longrunning.Operations.GetOperation": [
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/operations/*}",
                    },
                ],
                "google.longrunning.Operations.ListOperations": [
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*}/operations",
                    },
                ],
            }

            rest_transport = operations_v1.OperationsRestTransport(
                host=self._host,
                # use the credentials which are saved
                credentials=self._credentials,
                scopes=self._scopes,
                http_options=http_options,
                path_prefix="v1beta1",
            )

            self._operations_client = operations_v1.AbstractOperationsClient(
                transport=rest_transport
            )

        # Return the client from cache.
        return self._operations_client

    class _CreateExtensionBinding(
        _BaseDepServiceRestTransport._BaseCreateExtensionBinding, DepServiceRestStub
    ):
        def __hash__(self):
            return hash("DepServiceRestTransport.CreateExtensionBinding")

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
            request: dep.CreateExtensionBindingRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create extension binding method over HTTP.

            Args:
                request (~.dep.CreateExtensionBindingRequest):
                    The request object. Request used by the ``CreateExtensionBinding`` method.
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

            http_options = _BaseDepServiceRestTransport._BaseCreateExtensionBinding._get_http_options()
            request, metadata = self._interceptor.pre_create_extension_binding(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDepServiceRestTransport._BaseCreateExtensionBinding,
                    "_BaseCreateExtensionBinding__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networkservices_v1beta1.DepServiceClient.CreateExtensionBinding",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1beta1.DepService",
                        "rpcName": "CreateExtensionBinding",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DepServiceRestTransport._CreateExtensionBinding._get_response(
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

            resp = self._interceptor.post_create_extension_binding(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_extension_binding_with_metadata(
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
                    "Received response for google.cloud.networkservices_v1beta1.DepServiceClient.create_extension_binding",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1beta1.DepService",
                        "rpcName": "CreateExtensionBinding",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateLbRouteExtension(
        _BaseDepServiceRestTransport._BaseCreateLbRouteExtension, DepServiceRestStub
    ):
        def __hash__(self):
            return hash("DepServiceRestTransport.CreateLbRouteExtension")

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
            request: dep.CreateLbRouteExtensionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create lb route extension method over HTTP.

            Args:
                request (~.dep.CreateLbRouteExtensionRequest):
                    The request object. Message for creating a ``LbRouteExtension`` resource.
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

            http_options = _BaseDepServiceRestTransport._BaseCreateLbRouteExtension._get_http_options()
            request, metadata = self._interceptor.pre_create_lb_route_extension(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDepServiceRestTransport._BaseCreateLbRouteExtension,
                    "_BaseCreateLbRouteExtension__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networkservices_v1beta1.DepServiceClient.CreateLbRouteExtension",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1beta1.DepService",
                        "rpcName": "CreateLbRouteExtension",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DepServiceRestTransport._CreateLbRouteExtension._get_response(
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

            resp = self._interceptor.post_create_lb_route_extension(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_lb_route_extension_with_metadata(
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
                    "Received response for google.cloud.networkservices_v1beta1.DepServiceClient.create_lb_route_extension",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1beta1.DepService",
                        "rpcName": "CreateLbRouteExtension",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateLbTrafficExtension(
        _BaseDepServiceRestTransport._BaseCreateLbTrafficExtension, DepServiceRestStub
    ):
        def __hash__(self):
            return hash("DepServiceRestTransport.CreateLbTrafficExtension")

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
            request: dep.CreateLbTrafficExtensionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create lb traffic
            extension method over HTTP.

                Args:
                    request (~.dep.CreateLbTrafficExtensionRequest):
                        The request object. Message for creating a ``LbTrafficExtension`` resource.
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

            http_options = _BaseDepServiceRestTransport._BaseCreateLbTrafficExtension._get_http_options()
            request, metadata = self._interceptor.pre_create_lb_traffic_extension(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDepServiceRestTransport._BaseCreateLbTrafficExtension,
                    "_BaseCreateLbTrafficExtension__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networkservices_v1beta1.DepServiceClient.CreateLbTrafficExtension",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1beta1.DepService",
                        "rpcName": "CreateLbTrafficExtension",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DepServiceRestTransport._CreateLbTrafficExtension._get_response(
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

            resp = self._interceptor.post_create_lb_traffic_extension(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_lb_traffic_extension_with_metadata(
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
                    "Received response for google.cloud.networkservices_v1beta1.DepServiceClient.create_lb_traffic_extension",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1beta1.DepService",
                        "rpcName": "CreateLbTrafficExtension",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteExtensionBinding(
        _BaseDepServiceRestTransport._BaseDeleteExtensionBinding, DepServiceRestStub
    ):
        def __hash__(self):
            return hash("DepServiceRestTransport.DeleteExtensionBinding")

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
            request: dep.DeleteExtensionBindingRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete extension binding method over HTTP.

            Args:
                request (~.dep.DeleteExtensionBindingRequest):
                    The request object. Request used by the ``DeleteExtensionBinding`` method.
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

            http_options = _BaseDepServiceRestTransport._BaseDeleteExtensionBinding._get_http_options()
            request, metadata = self._interceptor.pre_delete_extension_binding(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDepServiceRestTransport._BaseDeleteExtensionBinding,
                    "_BaseDeleteExtensionBinding__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networkservices_v1beta1.DepServiceClient.DeleteExtensionBinding",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1beta1.DepService",
                        "rpcName": "DeleteExtensionBinding",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DepServiceRestTransport._DeleteExtensionBinding._get_response(
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

            resp = self._interceptor.post_delete_extension_binding(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_extension_binding_with_metadata(
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
                    "Received response for google.cloud.networkservices_v1beta1.DepServiceClient.delete_extension_binding",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1beta1.DepService",
                        "rpcName": "DeleteExtensionBinding",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteLbRouteExtension(
        _BaseDepServiceRestTransport._BaseDeleteLbRouteExtension, DepServiceRestStub
    ):
        def __hash__(self):
            return hash("DepServiceRestTransport.DeleteLbRouteExtension")

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
            request: dep.DeleteLbRouteExtensionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete lb route extension method over HTTP.

            Args:
                request (~.dep.DeleteLbRouteExtensionRequest):
                    The request object. Message for deleting a ``LbRouteExtension`` resource.
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

            http_options = _BaseDepServiceRestTransport._BaseDeleteLbRouteExtension._get_http_options()
            request, metadata = self._interceptor.pre_delete_lb_route_extension(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDepServiceRestTransport._BaseDeleteLbRouteExtension,
                    "_BaseDeleteLbRouteExtension__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networkservices_v1beta1.DepServiceClient.DeleteLbRouteExtension",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1beta1.DepService",
                        "rpcName": "DeleteLbRouteExtension",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DepServiceRestTransport._DeleteLbRouteExtension._get_response(
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

            resp = self._interceptor.post_delete_lb_route_extension(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_lb_route_extension_with_metadata(
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
                    "Received response for google.cloud.networkservices_v1beta1.DepServiceClient.delete_lb_route_extension",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1beta1.DepService",
                        "rpcName": "DeleteLbRouteExtension",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteLbTrafficExtension(
        _BaseDepServiceRestTransport._BaseDeleteLbTrafficExtension, DepServiceRestStub
    ):
        def __hash__(self):
            return hash("DepServiceRestTransport.DeleteLbTrafficExtension")

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
            request: dep.DeleteLbTrafficExtensionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete lb traffic
            extension method over HTTP.

                Args:
                    request (~.dep.DeleteLbTrafficExtensionRequest):
                        The request object. Message for deleting a ``LbTrafficExtension`` resource.
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

            http_options = _BaseDepServiceRestTransport._BaseDeleteLbTrafficExtension._get_http_options()
            request, metadata = self._interceptor.pre_delete_lb_traffic_extension(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDepServiceRestTransport._BaseDeleteLbTrafficExtension,
                    "_BaseDeleteLbTrafficExtension__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networkservices_v1beta1.DepServiceClient.DeleteLbTrafficExtension",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1beta1.DepService",
                        "rpcName": "DeleteLbTrafficExtension",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DepServiceRestTransport._DeleteLbTrafficExtension._get_response(
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

            resp = self._interceptor.post_delete_lb_traffic_extension(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_lb_traffic_extension_with_metadata(
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
                    "Received response for google.cloud.networkservices_v1beta1.DepServiceClient.delete_lb_traffic_extension",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1beta1.DepService",
                        "rpcName": "DeleteLbTrafficExtension",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetExtensionBinding(
        _BaseDepServiceRestTransport._BaseGetExtensionBinding, DepServiceRestStub
    ):
        def __hash__(self):
            return hash("DepServiceRestTransport.GetExtensionBinding")

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
            request: dep.GetExtensionBindingRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> dep.ExtensionBinding:
            r"""Call the get extension binding method over HTTP.

            Args:
                request (~.dep.GetExtensionBindingRequest):
                    The request object. Request used by the ``GetExtensionBinding`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.dep.ExtensionBinding:
                    ``ExtensionBinding`` is a resource representing the
                attachment of an extension to a service.

            """

            http_options = _BaseDepServiceRestTransport._BaseGetExtensionBinding._get_http_options()
            request, metadata = self._interceptor.pre_get_extension_binding(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDepServiceRestTransport._BaseGetExtensionBinding,
                    "_BaseGetExtensionBinding__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networkservices_v1beta1.DepServiceClient.GetExtensionBinding",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1beta1.DepService",
                        "rpcName": "GetExtensionBinding",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DepServiceRestTransport._GetExtensionBinding._get_response(
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
            resp = dep.ExtensionBinding()
            pb_resp = dep.ExtensionBinding.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_extension_binding(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_extension_binding_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = dep.ExtensionBinding.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.networkservices_v1beta1.DepServiceClient.get_extension_binding",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1beta1.DepService",
                        "rpcName": "GetExtensionBinding",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetLbRouteExtension(
        _BaseDepServiceRestTransport._BaseGetLbRouteExtension, DepServiceRestStub
    ):
        def __hash__(self):
            return hash("DepServiceRestTransport.GetLbRouteExtension")

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
            request: dep.GetLbRouteExtensionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> dep.LbRouteExtension:
            r"""Call the get lb route extension method over HTTP.

            Args:
                request (~.dep.GetLbRouteExtensionRequest):
                    The request object. Message for getting a ``LbRouteExtension`` resource.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.dep.LbRouteExtension:
                    ``LbRouteExtension`` is a resource that lets you control
                where traffic is routed to for a given request.

            """

            http_options = _BaseDepServiceRestTransport._BaseGetLbRouteExtension._get_http_options()
            request, metadata = self._interceptor.pre_get_lb_route_extension(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDepServiceRestTransport._BaseGetLbRouteExtension,
                    "_BaseGetLbRouteExtension__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networkservices_v1beta1.DepServiceClient.GetLbRouteExtension",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1beta1.DepService",
                        "rpcName": "GetLbRouteExtension",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DepServiceRestTransport._GetLbRouteExtension._get_response(
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
            resp = dep.LbRouteExtension()
            pb_resp = dep.LbRouteExtension.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_lb_route_extension(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_lb_route_extension_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = dep.LbRouteExtension.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.networkservices_v1beta1.DepServiceClient.get_lb_route_extension",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1beta1.DepService",
                        "rpcName": "GetLbRouteExtension",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetLbTrafficExtension(
        _BaseDepServiceRestTransport._BaseGetLbTrafficExtension, DepServiceRestStub
    ):
        def __hash__(self):
            return hash("DepServiceRestTransport.GetLbTrafficExtension")

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
            request: dep.GetLbTrafficExtensionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> dep.LbTrafficExtension:
            r"""Call the get lb traffic extension method over HTTP.

            Args:
                request (~.dep.GetLbTrafficExtensionRequest):
                    The request object. Message for getting a ``LbTrafficExtension`` resource.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.dep.LbTrafficExtension:
                    ``LbTrafficExtension`` is a resource that lets the
                extension service modify the headers and payloads of
                both requests and responses without impacting the choice
                of backend services or any other security policies
                associated with the backend service.

            """

            http_options = _BaseDepServiceRestTransport._BaseGetLbTrafficExtension._get_http_options()
            request, metadata = self._interceptor.pre_get_lb_traffic_extension(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDepServiceRestTransport._BaseGetLbTrafficExtension,
                    "_BaseGetLbTrafficExtension__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networkservices_v1beta1.DepServiceClient.GetLbTrafficExtension",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1beta1.DepService",
                        "rpcName": "GetLbTrafficExtension",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DepServiceRestTransport._GetLbTrafficExtension._get_response(
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
            resp = dep.LbTrafficExtension()
            pb_resp = dep.LbTrafficExtension.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_lb_traffic_extension(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_lb_traffic_extension_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = dep.LbTrafficExtension.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.networkservices_v1beta1.DepServiceClient.get_lb_traffic_extension",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1beta1.DepService",
                        "rpcName": "GetLbTrafficExtension",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListExtensionBindings(
        _BaseDepServiceRestTransport._BaseListExtensionBindings, DepServiceRestStub
    ):
        def __hash__(self):
            return hash("DepServiceRestTransport.ListExtensionBindings")

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
            request: dep.ListExtensionBindingsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> dep.ListExtensionBindingsResponse:
            r"""Call the list extension bindings method over HTTP.

            Args:
                request (~.dep.ListExtensionBindingsRequest):
                    The request object. Request used with the ``ListExtensionBindings`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.dep.ListExtensionBindingsResponse:
                    Response returned by the ``ListExtensionBindings``
                method.

            """

            http_options = _BaseDepServiceRestTransport._BaseListExtensionBindings._get_http_options()
            request, metadata = self._interceptor.pre_list_extension_bindings(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDepServiceRestTransport._BaseListExtensionBindings,
                    "_BaseListExtensionBindings__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networkservices_v1beta1.DepServiceClient.ListExtensionBindings",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1beta1.DepService",
                        "rpcName": "ListExtensionBindings",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DepServiceRestTransport._ListExtensionBindings._get_response(
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
            resp = dep.ListExtensionBindingsResponse()
            pb_resp = dep.ListExtensionBindingsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_extension_bindings(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_extension_bindings_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = dep.ListExtensionBindingsResponse.to_json(
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
                    "Received response for google.cloud.networkservices_v1beta1.DepServiceClient.list_extension_bindings",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1beta1.DepService",
                        "rpcName": "ListExtensionBindings",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListLbRouteExtensions(
        _BaseDepServiceRestTransport._BaseListLbRouteExtensions, DepServiceRestStub
    ):
        def __hash__(self):
            return hash("DepServiceRestTransport.ListLbRouteExtensions")

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
            request: dep.ListLbRouteExtensionsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> dep.ListLbRouteExtensionsResponse:
            r"""Call the list lb route extensions method over HTTP.

            Args:
                request (~.dep.ListLbRouteExtensionsRequest):
                    The request object. Message for requesting list of ``LbRouteExtension``
                resources.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.dep.ListLbRouteExtensionsResponse:
                    Message for response to listing ``LbRouteExtension``
                resources.

            """

            http_options = _BaseDepServiceRestTransport._BaseListLbRouteExtensions._get_http_options()
            request, metadata = self._interceptor.pre_list_lb_route_extensions(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDepServiceRestTransport._BaseListLbRouteExtensions,
                    "_BaseListLbRouteExtensions__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networkservices_v1beta1.DepServiceClient.ListLbRouteExtensions",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1beta1.DepService",
                        "rpcName": "ListLbRouteExtensions",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DepServiceRestTransport._ListLbRouteExtensions._get_response(
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
            resp = dep.ListLbRouteExtensionsResponse()
            pb_resp = dep.ListLbRouteExtensionsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_lb_route_extensions(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_lb_route_extensions_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = dep.ListLbRouteExtensionsResponse.to_json(
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
                    "Received response for google.cloud.networkservices_v1beta1.DepServiceClient.list_lb_route_extensions",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1beta1.DepService",
                        "rpcName": "ListLbRouteExtensions",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListLbTrafficExtensions(
        _BaseDepServiceRestTransport._BaseListLbTrafficExtensions, DepServiceRestStub
    ):
        def __hash__(self):
            return hash("DepServiceRestTransport.ListLbTrafficExtensions")

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
            request: dep.ListLbTrafficExtensionsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> dep.ListLbTrafficExtensionsResponse:
            r"""Call the list lb traffic
            extensions method over HTTP.

                Args:
                    request (~.dep.ListLbTrafficExtensionsRequest):
                        The request object. Message for requesting list of ``LbTrafficExtension``
                    resources.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.dep.ListLbTrafficExtensionsResponse:
                        Message for response to listing ``LbTrafficExtension``
                    resources.

            """

            http_options = _BaseDepServiceRestTransport._BaseListLbTrafficExtensions._get_http_options()
            request, metadata = self._interceptor.pre_list_lb_traffic_extensions(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDepServiceRestTransport._BaseListLbTrafficExtensions,
                    "_BaseListLbTrafficExtensions__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networkservices_v1beta1.DepServiceClient.ListLbTrafficExtensions",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1beta1.DepService",
                        "rpcName": "ListLbTrafficExtensions",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DepServiceRestTransport._ListLbTrafficExtensions._get_response(
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
            resp = dep.ListLbTrafficExtensionsResponse()
            pb_resp = dep.ListLbTrafficExtensionsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_lb_traffic_extensions(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_lb_traffic_extensions_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = dep.ListLbTrafficExtensionsResponse.to_json(
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
                    "Received response for google.cloud.networkservices_v1beta1.DepServiceClient.list_lb_traffic_extensions",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1beta1.DepService",
                        "rpcName": "ListLbTrafficExtensions",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateExtensionBinding(
        _BaseDepServiceRestTransport._BaseUpdateExtensionBinding, DepServiceRestStub
    ):
        def __hash__(self):
            return hash("DepServiceRestTransport.UpdateExtensionBinding")

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
            request: dep.UpdateExtensionBindingRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update extension binding method over HTTP.

            Args:
                request (~.dep.UpdateExtensionBindingRequest):
                    The request object. Request used by the ``UpdateExtensionBinding`` method.
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

            http_options = _BaseDepServiceRestTransport._BaseUpdateExtensionBinding._get_http_options()
            request, metadata = self._interceptor.pre_update_extension_binding(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDepServiceRestTransport._BaseUpdateExtensionBinding,
                    "_BaseUpdateExtensionBinding__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networkservices_v1beta1.DepServiceClient.UpdateExtensionBinding",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1beta1.DepService",
                        "rpcName": "UpdateExtensionBinding",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DepServiceRestTransport._UpdateExtensionBinding._get_response(
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

            resp = self._interceptor.post_update_extension_binding(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_extension_binding_with_metadata(
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
                    "Received response for google.cloud.networkservices_v1beta1.DepServiceClient.update_extension_binding",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1beta1.DepService",
                        "rpcName": "UpdateExtensionBinding",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateLbRouteExtension(
        _BaseDepServiceRestTransport._BaseUpdateLbRouteExtension, DepServiceRestStub
    ):
        def __hash__(self):
            return hash("DepServiceRestTransport.UpdateLbRouteExtension")

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
            request: dep.UpdateLbRouteExtensionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update lb route extension method over HTTP.

            Args:
                request (~.dep.UpdateLbRouteExtensionRequest):
                    The request object. Message for updating a ``LbRouteExtension`` resource.
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

            http_options = _BaseDepServiceRestTransport._BaseUpdateLbRouteExtension._get_http_options()
            request, metadata = self._interceptor.pre_update_lb_route_extension(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDepServiceRestTransport._BaseUpdateLbRouteExtension,
                    "_BaseUpdateLbRouteExtension__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networkservices_v1beta1.DepServiceClient.UpdateLbRouteExtension",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1beta1.DepService",
                        "rpcName": "UpdateLbRouteExtension",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DepServiceRestTransport._UpdateLbRouteExtension._get_response(
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

            resp = self._interceptor.post_update_lb_route_extension(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_lb_route_extension_with_metadata(
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
                    "Received response for google.cloud.networkservices_v1beta1.DepServiceClient.update_lb_route_extension",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1beta1.DepService",
                        "rpcName": "UpdateLbRouteExtension",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateLbTrafficExtension(
        _BaseDepServiceRestTransport._BaseUpdateLbTrafficExtension, DepServiceRestStub
    ):
        def __hash__(self):
            return hash("DepServiceRestTransport.UpdateLbTrafficExtension")

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
            request: dep.UpdateLbTrafficExtensionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update lb traffic
            extension method over HTTP.

                Args:
                    request (~.dep.UpdateLbTrafficExtensionRequest):
                        The request object. Message for updating a ``LbTrafficExtension`` resource.
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

            http_options = _BaseDepServiceRestTransport._BaseUpdateLbTrafficExtension._get_http_options()
            request, metadata = self._interceptor.pre_update_lb_traffic_extension(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDepServiceRestTransport._BaseUpdateLbTrafficExtension,
                    "_BaseUpdateLbTrafficExtension__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networkservices_v1beta1.DepServiceClient.UpdateLbTrafficExtension",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1beta1.DepService",
                        "rpcName": "UpdateLbTrafficExtension",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DepServiceRestTransport._UpdateLbTrafficExtension._get_response(
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

            resp = self._interceptor.post_update_lb_traffic_extension(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_lb_traffic_extension_with_metadata(
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
                    "Received response for google.cloud.networkservices_v1beta1.DepServiceClient.update_lb_traffic_extension",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1beta1.DepService",
                        "rpcName": "UpdateLbTrafficExtension",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def create_extension_binding(
        self,
    ) -> Callable[[dep.CreateExtensionBindingRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateExtensionBinding(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def create_lb_route_extension(
        self,
    ) -> Callable[[dep.CreateLbRouteExtensionRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateLbRouteExtension(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def create_lb_traffic_extension(
        self,
    ) -> Callable[[dep.CreateLbTrafficExtensionRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateLbTrafficExtension(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def delete_extension_binding(
        self,
    ) -> Callable[[dep.DeleteExtensionBindingRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteExtensionBinding(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def delete_lb_route_extension(
        self,
    ) -> Callable[[dep.DeleteLbRouteExtensionRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteLbRouteExtension(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def delete_lb_traffic_extension(
        self,
    ) -> Callable[[dep.DeleteLbTrafficExtensionRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteLbTrafficExtension(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def get_extension_binding(
        self,
    ) -> Callable[[dep.GetExtensionBindingRequest], dep.ExtensionBinding]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetExtensionBinding(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_lb_route_extension(
        self,
    ) -> Callable[[dep.GetLbRouteExtensionRequest], dep.LbRouteExtension]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetLbRouteExtension(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_lb_traffic_extension(
        self,
    ) -> Callable[[dep.GetLbTrafficExtensionRequest], dep.LbTrafficExtension]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetLbTrafficExtension(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_extension_bindings(
        self,
    ) -> Callable[
        [dep.ListExtensionBindingsRequest], dep.ListExtensionBindingsResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListExtensionBindings(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_lb_route_extensions(
        self,
    ) -> Callable[
        [dep.ListLbRouteExtensionsRequest], dep.ListLbRouteExtensionsResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListLbRouteExtensions(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_lb_traffic_extensions(
        self,
    ) -> Callable[
        [dep.ListLbTrafficExtensionsRequest], dep.ListLbTrafficExtensionsResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListLbTrafficExtensions(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def update_extension_binding(
        self,
    ) -> Callable[[dep.UpdateExtensionBindingRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateExtensionBinding(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def update_lb_route_extension(
        self,
    ) -> Callable[[dep.UpdateLbRouteExtensionRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateLbRouteExtension(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def update_lb_traffic_extension(
        self,
    ) -> Callable[[dep.UpdateLbTrafficExtensionRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateLbTrafficExtension(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def get_location(self):
        return self._GetLocation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetLocation(
        _BaseDepServiceRestTransport._BaseGetLocation, DepServiceRestStub
    ):
        def __hash__(self):
            return hash("DepServiceRestTransport.GetLocation")

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
                _BaseDepServiceRestTransport._BaseGetLocation._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_location(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDepServiceRestTransport._BaseGetLocation,
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
                    f"Sending request for google.cloud.networkservices_v1beta1.DepServiceClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1beta1.DepService",
                        "rpcName": "GetLocation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DepServiceRestTransport._GetLocation._get_response(
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
                    "Received response for google.cloud.networkservices_v1beta1.DepServiceAsyncClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1beta1.DepService",
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
        _BaseDepServiceRestTransport._BaseListLocations, DepServiceRestStub
    ):
        def __hash__(self):
            return hash("DepServiceRestTransport.ListLocations")

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
                _BaseDepServiceRestTransport._BaseListLocations._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_locations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDepServiceRestTransport._BaseListLocations,
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
                    f"Sending request for google.cloud.networkservices_v1beta1.DepServiceClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1beta1.DepService",
                        "rpcName": "ListLocations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DepServiceRestTransport._ListLocations._get_response(
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
                    "Received response for google.cloud.networkservices_v1beta1.DepServiceAsyncClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1beta1.DepService",
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
        _BaseDepServiceRestTransport._BaseGetIamPolicy, DepServiceRestStub
    ):
        def __hash__(self):
            return hash("DepServiceRestTransport.GetIamPolicy")

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
                _BaseDepServiceRestTransport._BaseGetIamPolicy._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_iam_policy(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDepServiceRestTransport._BaseGetIamPolicy,
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
                    f"Sending request for google.cloud.networkservices_v1beta1.DepServiceClient.GetIamPolicy",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1beta1.DepService",
                        "rpcName": "GetIamPolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DepServiceRestTransport._GetIamPolicy._get_response(
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
                    "Received response for google.cloud.networkservices_v1beta1.DepServiceAsyncClient.GetIamPolicy",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1beta1.DepService",
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
        _BaseDepServiceRestTransport._BaseSetIamPolicy, DepServiceRestStub
    ):
        def __hash__(self):
            return hash("DepServiceRestTransport.SetIamPolicy")

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
                _BaseDepServiceRestTransport._BaseSetIamPolicy._get_http_options()
            )
            request, metadata = self._interceptor.pre_set_iam_policy(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDepServiceRestTransport._BaseSetIamPolicy,
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
                    f"Sending request for google.cloud.networkservices_v1beta1.DepServiceClient.SetIamPolicy",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1beta1.DepService",
                        "rpcName": "SetIamPolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DepServiceRestTransport._SetIamPolicy._get_response(
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
                    "Received response for google.cloud.networkservices_v1beta1.DepServiceAsyncClient.SetIamPolicy",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1beta1.DepService",
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
        _BaseDepServiceRestTransport._BaseTestIamPermissions, DepServiceRestStub
    ):
        def __hash__(self):
            return hash("DepServiceRestTransport.TestIamPermissions")

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

            http_options = (
                _BaseDepServiceRestTransport._BaseTestIamPermissions._get_http_options()
            )
            request, metadata = self._interceptor.pre_test_iam_permissions(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDepServiceRestTransport._BaseTestIamPermissions,
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
                    f"Sending request for google.cloud.networkservices_v1beta1.DepServiceClient.TestIamPermissions",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1beta1.DepService",
                        "rpcName": "TestIamPermissions",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DepServiceRestTransport._TestIamPermissions._get_response(
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
                    "Received response for google.cloud.networkservices_v1beta1.DepServiceAsyncClient.TestIamPermissions",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1beta1.DepService",
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
        _BaseDepServiceRestTransport._BaseCancelOperation, DepServiceRestStub
    ):
        def __hash__(self):
            return hash("DepServiceRestTransport.CancelOperation")

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
                _BaseDepServiceRestTransport._BaseCancelOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_cancel_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDepServiceRestTransport._BaseCancelOperation,
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
                    f"Sending request for google.cloud.networkservices_v1beta1.DepServiceClient.CancelOperation",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1beta1.DepService",
                        "rpcName": "CancelOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DepServiceRestTransport._CancelOperation._get_response(
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
        _BaseDepServiceRestTransport._BaseDeleteOperation, DepServiceRestStub
    ):
        def __hash__(self):
            return hash("DepServiceRestTransport.DeleteOperation")

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
                _BaseDepServiceRestTransport._BaseDeleteOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDepServiceRestTransport._BaseDeleteOperation,
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
                    f"Sending request for google.cloud.networkservices_v1beta1.DepServiceClient.DeleteOperation",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1beta1.DepService",
                        "rpcName": "DeleteOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DepServiceRestTransport._DeleteOperation._get_response(
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
        _BaseDepServiceRestTransport._BaseGetOperation, DepServiceRestStub
    ):
        def __hash__(self):
            return hash("DepServiceRestTransport.GetOperation")

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
                _BaseDepServiceRestTransport._BaseGetOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_operation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDepServiceRestTransport._BaseGetOperation,
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
                    f"Sending request for google.cloud.networkservices_v1beta1.DepServiceClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1beta1.DepService",
                        "rpcName": "GetOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DepServiceRestTransport._GetOperation._get_response(
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
                    "Received response for google.cloud.networkservices_v1beta1.DepServiceAsyncClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1beta1.DepService",
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
        _BaseDepServiceRestTransport._BaseListOperations, DepServiceRestStub
    ):
        def __hash__(self):
            return hash("DepServiceRestTransport.ListOperations")

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
                _BaseDepServiceRestTransport._BaseListOperations._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_operations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDepServiceRestTransport._BaseListOperations,
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
                    f"Sending request for google.cloud.networkservices_v1beta1.DepServiceClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1beta1.DepService",
                        "rpcName": "ListOperations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DepServiceRestTransport._ListOperations._get_response(
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
                    "Received response for google.cloud.networkservices_v1beta1.DepServiceAsyncClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1beta1.DepService",
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


__all__ = ("DepServiceRestTransport",)
