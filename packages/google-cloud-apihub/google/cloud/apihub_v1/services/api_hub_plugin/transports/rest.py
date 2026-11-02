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

from google.cloud.apihub_v1._compat import transcode_request
from google.cloud.apihub_v1.types import plugin_service

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseApiHubPluginRestTransport

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


class ApiHubPluginRestInterceptor:
    """Interceptor for ApiHubPlugin.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the ApiHubPluginRestTransport.

    .. code-block:: python
        class MyCustomApiHubPluginInterceptor(ApiHubPluginRestInterceptor):
            def pre_create_plugin(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_plugin(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_plugin_instance(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_plugin_instance(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_plugin(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_plugin(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_plugin_instance(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_plugin_instance(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_disable_plugin(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_disable_plugin(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_disable_plugin_instance_action(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_disable_plugin_instance_action(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_enable_plugin(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_enable_plugin(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_enable_plugin_instance_action(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_enable_plugin_instance_action(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_execute_plugin_instance_action(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_execute_plugin_instance_action(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_plugin(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_plugin(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_plugin_instance(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_plugin_instance(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_plugin_instances(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_plugin_instances(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_plugins(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_plugins(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_plugin_instance(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_plugin_instance(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = ApiHubPluginRestTransport(interceptor=MyCustomApiHubPluginInterceptor())
        client = ApiHubPluginClient(transport=transport)


    """

    def pre_create_plugin(
        self,
        request: plugin_service.CreatePluginRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        plugin_service.CreatePluginRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_plugin

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ApiHubPlugin server.
        """
        return request, metadata

    def post_create_plugin(
        self, response: plugin_service.Plugin
    ) -> plugin_service.Plugin:
        """Post-rpc interceptor for create_plugin

        DEPRECATED. Please use the `post_create_plugin_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ApiHubPlugin server but before
        it is returned to user code. This `post_create_plugin` interceptor runs
        before the `post_create_plugin_with_metadata` interceptor.
        """
        return response

    def post_create_plugin_with_metadata(
        self,
        response: plugin_service.Plugin,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[plugin_service.Plugin, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_plugin

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ApiHubPlugin server but before it is returned to user code.

        We recommend only using this `post_create_plugin_with_metadata`
        interceptor in new development instead of the `post_create_plugin` interceptor.
        When both interceptors are used, this `post_create_plugin_with_metadata` interceptor runs after the
        `post_create_plugin` interceptor. The (possibly modified) response returned by
        `post_create_plugin` will be passed to
        `post_create_plugin_with_metadata`.
        """
        return response, metadata

    def pre_create_plugin_instance(
        self,
        request: plugin_service.CreatePluginInstanceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        plugin_service.CreatePluginInstanceRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_plugin_instance

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ApiHubPlugin server.
        """
        return request, metadata

    def post_create_plugin_instance(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_plugin_instance

        DEPRECATED. Please use the `post_create_plugin_instance_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ApiHubPlugin server but before
        it is returned to user code. This `post_create_plugin_instance` interceptor runs
        before the `post_create_plugin_instance_with_metadata` interceptor.
        """
        return response

    def post_create_plugin_instance_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_plugin_instance

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ApiHubPlugin server but before it is returned to user code.

        We recommend only using this `post_create_plugin_instance_with_metadata`
        interceptor in new development instead of the `post_create_plugin_instance` interceptor.
        When both interceptors are used, this `post_create_plugin_instance_with_metadata` interceptor runs after the
        `post_create_plugin_instance` interceptor. The (possibly modified) response returned by
        `post_create_plugin_instance` will be passed to
        `post_create_plugin_instance_with_metadata`.
        """
        return response, metadata

    def pre_delete_plugin(
        self,
        request: plugin_service.DeletePluginRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        plugin_service.DeletePluginRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_plugin

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ApiHubPlugin server.
        """
        return request, metadata

    def post_delete_plugin(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_plugin

        DEPRECATED. Please use the `post_delete_plugin_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ApiHubPlugin server but before
        it is returned to user code. This `post_delete_plugin` interceptor runs
        before the `post_delete_plugin_with_metadata` interceptor.
        """
        return response

    def post_delete_plugin_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_plugin

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ApiHubPlugin server but before it is returned to user code.

        We recommend only using this `post_delete_plugin_with_metadata`
        interceptor in new development instead of the `post_delete_plugin` interceptor.
        When both interceptors are used, this `post_delete_plugin_with_metadata` interceptor runs after the
        `post_delete_plugin` interceptor. The (possibly modified) response returned by
        `post_delete_plugin` will be passed to
        `post_delete_plugin_with_metadata`.
        """
        return response, metadata

    def pre_delete_plugin_instance(
        self,
        request: plugin_service.DeletePluginInstanceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        plugin_service.DeletePluginInstanceRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_plugin_instance

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ApiHubPlugin server.
        """
        return request, metadata

    def post_delete_plugin_instance(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_plugin_instance

        DEPRECATED. Please use the `post_delete_plugin_instance_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ApiHubPlugin server but before
        it is returned to user code. This `post_delete_plugin_instance` interceptor runs
        before the `post_delete_plugin_instance_with_metadata` interceptor.
        """
        return response

    def post_delete_plugin_instance_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_plugin_instance

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ApiHubPlugin server but before it is returned to user code.

        We recommend only using this `post_delete_plugin_instance_with_metadata`
        interceptor in new development instead of the `post_delete_plugin_instance` interceptor.
        When both interceptors are used, this `post_delete_plugin_instance_with_metadata` interceptor runs after the
        `post_delete_plugin_instance` interceptor. The (possibly modified) response returned by
        `post_delete_plugin_instance` will be passed to
        `post_delete_plugin_instance_with_metadata`.
        """
        return response, metadata

    def pre_disable_plugin(
        self,
        request: plugin_service.DisablePluginRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        plugin_service.DisablePluginRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for disable_plugin

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ApiHubPlugin server.
        """
        return request, metadata

    def post_disable_plugin(
        self, response: plugin_service.Plugin
    ) -> plugin_service.Plugin:
        """Post-rpc interceptor for disable_plugin

        DEPRECATED. Please use the `post_disable_plugin_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ApiHubPlugin server but before
        it is returned to user code. This `post_disable_plugin` interceptor runs
        before the `post_disable_plugin_with_metadata` interceptor.
        """
        return response

    def post_disable_plugin_with_metadata(
        self,
        response: plugin_service.Plugin,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[plugin_service.Plugin, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for disable_plugin

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ApiHubPlugin server but before it is returned to user code.

        We recommend only using this `post_disable_plugin_with_metadata`
        interceptor in new development instead of the `post_disable_plugin` interceptor.
        When both interceptors are used, this `post_disable_plugin_with_metadata` interceptor runs after the
        `post_disable_plugin` interceptor. The (possibly modified) response returned by
        `post_disable_plugin` will be passed to
        `post_disable_plugin_with_metadata`.
        """
        return response, metadata

    def pre_disable_plugin_instance_action(
        self,
        request: plugin_service.DisablePluginInstanceActionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        plugin_service.DisablePluginInstanceActionRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for disable_plugin_instance_action

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ApiHubPlugin server.
        """
        return request, metadata

    def post_disable_plugin_instance_action(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for disable_plugin_instance_action

        DEPRECATED. Please use the `post_disable_plugin_instance_action_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ApiHubPlugin server but before
        it is returned to user code. This `post_disable_plugin_instance_action` interceptor runs
        before the `post_disable_plugin_instance_action_with_metadata` interceptor.
        """
        return response

    def post_disable_plugin_instance_action_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for disable_plugin_instance_action

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ApiHubPlugin server but before it is returned to user code.

        We recommend only using this `post_disable_plugin_instance_action_with_metadata`
        interceptor in new development instead of the `post_disable_plugin_instance_action` interceptor.
        When both interceptors are used, this `post_disable_plugin_instance_action_with_metadata` interceptor runs after the
        `post_disable_plugin_instance_action` interceptor. The (possibly modified) response returned by
        `post_disable_plugin_instance_action` will be passed to
        `post_disable_plugin_instance_action_with_metadata`.
        """
        return response, metadata

    def pre_enable_plugin(
        self,
        request: plugin_service.EnablePluginRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        plugin_service.EnablePluginRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for enable_plugin

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ApiHubPlugin server.
        """
        return request, metadata

    def post_enable_plugin(
        self, response: plugin_service.Plugin
    ) -> plugin_service.Plugin:
        """Post-rpc interceptor for enable_plugin

        DEPRECATED. Please use the `post_enable_plugin_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ApiHubPlugin server but before
        it is returned to user code. This `post_enable_plugin` interceptor runs
        before the `post_enable_plugin_with_metadata` interceptor.
        """
        return response

    def post_enable_plugin_with_metadata(
        self,
        response: plugin_service.Plugin,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[plugin_service.Plugin, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for enable_plugin

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ApiHubPlugin server but before it is returned to user code.

        We recommend only using this `post_enable_plugin_with_metadata`
        interceptor in new development instead of the `post_enable_plugin` interceptor.
        When both interceptors are used, this `post_enable_plugin_with_metadata` interceptor runs after the
        `post_enable_plugin` interceptor. The (possibly modified) response returned by
        `post_enable_plugin` will be passed to
        `post_enable_plugin_with_metadata`.
        """
        return response, metadata

    def pre_enable_plugin_instance_action(
        self,
        request: plugin_service.EnablePluginInstanceActionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        plugin_service.EnablePluginInstanceActionRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for enable_plugin_instance_action

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ApiHubPlugin server.
        """
        return request, metadata

    def post_enable_plugin_instance_action(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for enable_plugin_instance_action

        DEPRECATED. Please use the `post_enable_plugin_instance_action_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ApiHubPlugin server but before
        it is returned to user code. This `post_enable_plugin_instance_action` interceptor runs
        before the `post_enable_plugin_instance_action_with_metadata` interceptor.
        """
        return response

    def post_enable_plugin_instance_action_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for enable_plugin_instance_action

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ApiHubPlugin server but before it is returned to user code.

        We recommend only using this `post_enable_plugin_instance_action_with_metadata`
        interceptor in new development instead of the `post_enable_plugin_instance_action` interceptor.
        When both interceptors are used, this `post_enable_plugin_instance_action_with_metadata` interceptor runs after the
        `post_enable_plugin_instance_action` interceptor. The (possibly modified) response returned by
        `post_enable_plugin_instance_action` will be passed to
        `post_enable_plugin_instance_action_with_metadata`.
        """
        return response, metadata

    def pre_execute_plugin_instance_action(
        self,
        request: plugin_service.ExecutePluginInstanceActionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        plugin_service.ExecutePluginInstanceActionRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for execute_plugin_instance_action

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ApiHubPlugin server.
        """
        return request, metadata

    def post_execute_plugin_instance_action(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for execute_plugin_instance_action

        DEPRECATED. Please use the `post_execute_plugin_instance_action_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ApiHubPlugin server but before
        it is returned to user code. This `post_execute_plugin_instance_action` interceptor runs
        before the `post_execute_plugin_instance_action_with_metadata` interceptor.
        """
        return response

    def post_execute_plugin_instance_action_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for execute_plugin_instance_action

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ApiHubPlugin server but before it is returned to user code.

        We recommend only using this `post_execute_plugin_instance_action_with_metadata`
        interceptor in new development instead of the `post_execute_plugin_instance_action` interceptor.
        When both interceptors are used, this `post_execute_plugin_instance_action_with_metadata` interceptor runs after the
        `post_execute_plugin_instance_action` interceptor. The (possibly modified) response returned by
        `post_execute_plugin_instance_action` will be passed to
        `post_execute_plugin_instance_action_with_metadata`.
        """
        return response, metadata

    def pre_get_plugin(
        self,
        request: plugin_service.GetPluginRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        plugin_service.GetPluginRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_plugin

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ApiHubPlugin server.
        """
        return request, metadata

    def post_get_plugin(self, response: plugin_service.Plugin) -> plugin_service.Plugin:
        """Post-rpc interceptor for get_plugin

        DEPRECATED. Please use the `post_get_plugin_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ApiHubPlugin server but before
        it is returned to user code. This `post_get_plugin` interceptor runs
        before the `post_get_plugin_with_metadata` interceptor.
        """
        return response

    def post_get_plugin_with_metadata(
        self,
        response: plugin_service.Plugin,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[plugin_service.Plugin, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_plugin

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ApiHubPlugin server but before it is returned to user code.

        We recommend only using this `post_get_plugin_with_metadata`
        interceptor in new development instead of the `post_get_plugin` interceptor.
        When both interceptors are used, this `post_get_plugin_with_metadata` interceptor runs after the
        `post_get_plugin` interceptor. The (possibly modified) response returned by
        `post_get_plugin` will be passed to
        `post_get_plugin_with_metadata`.
        """
        return response, metadata

    def pre_get_plugin_instance(
        self,
        request: plugin_service.GetPluginInstanceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        plugin_service.GetPluginInstanceRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_plugin_instance

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ApiHubPlugin server.
        """
        return request, metadata

    def post_get_plugin_instance(
        self, response: plugin_service.PluginInstance
    ) -> plugin_service.PluginInstance:
        """Post-rpc interceptor for get_plugin_instance

        DEPRECATED. Please use the `post_get_plugin_instance_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ApiHubPlugin server but before
        it is returned to user code. This `post_get_plugin_instance` interceptor runs
        before the `post_get_plugin_instance_with_metadata` interceptor.
        """
        return response

    def post_get_plugin_instance_with_metadata(
        self,
        response: plugin_service.PluginInstance,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[plugin_service.PluginInstance, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_plugin_instance

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ApiHubPlugin server but before it is returned to user code.

        We recommend only using this `post_get_plugin_instance_with_metadata`
        interceptor in new development instead of the `post_get_plugin_instance` interceptor.
        When both interceptors are used, this `post_get_plugin_instance_with_metadata` interceptor runs after the
        `post_get_plugin_instance` interceptor. The (possibly modified) response returned by
        `post_get_plugin_instance` will be passed to
        `post_get_plugin_instance_with_metadata`.
        """
        return response, metadata

    def pre_list_plugin_instances(
        self,
        request: plugin_service.ListPluginInstancesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        plugin_service.ListPluginInstancesRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_plugin_instances

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ApiHubPlugin server.
        """
        return request, metadata

    def post_list_plugin_instances(
        self, response: plugin_service.ListPluginInstancesResponse
    ) -> plugin_service.ListPluginInstancesResponse:
        """Post-rpc interceptor for list_plugin_instances

        DEPRECATED. Please use the `post_list_plugin_instances_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ApiHubPlugin server but before
        it is returned to user code. This `post_list_plugin_instances` interceptor runs
        before the `post_list_plugin_instances_with_metadata` interceptor.
        """
        return response

    def post_list_plugin_instances_with_metadata(
        self,
        response: plugin_service.ListPluginInstancesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        plugin_service.ListPluginInstancesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_plugin_instances

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ApiHubPlugin server but before it is returned to user code.

        We recommend only using this `post_list_plugin_instances_with_metadata`
        interceptor in new development instead of the `post_list_plugin_instances` interceptor.
        When both interceptors are used, this `post_list_plugin_instances_with_metadata` interceptor runs after the
        `post_list_plugin_instances` interceptor. The (possibly modified) response returned by
        `post_list_plugin_instances` will be passed to
        `post_list_plugin_instances_with_metadata`.
        """
        return response, metadata

    def pre_list_plugins(
        self,
        request: plugin_service.ListPluginsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        plugin_service.ListPluginsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_plugins

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ApiHubPlugin server.
        """
        return request, metadata

    def post_list_plugins(
        self, response: plugin_service.ListPluginsResponse
    ) -> plugin_service.ListPluginsResponse:
        """Post-rpc interceptor for list_plugins

        DEPRECATED. Please use the `post_list_plugins_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ApiHubPlugin server but before
        it is returned to user code. This `post_list_plugins` interceptor runs
        before the `post_list_plugins_with_metadata` interceptor.
        """
        return response

    def post_list_plugins_with_metadata(
        self,
        response: plugin_service.ListPluginsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        plugin_service.ListPluginsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_plugins

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ApiHubPlugin server but before it is returned to user code.

        We recommend only using this `post_list_plugins_with_metadata`
        interceptor in new development instead of the `post_list_plugins` interceptor.
        When both interceptors are used, this `post_list_plugins_with_metadata` interceptor runs after the
        `post_list_plugins` interceptor. The (possibly modified) response returned by
        `post_list_plugins` will be passed to
        `post_list_plugins_with_metadata`.
        """
        return response, metadata

    def pre_update_plugin_instance(
        self,
        request: plugin_service.UpdatePluginInstanceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        plugin_service.UpdatePluginInstanceRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_plugin_instance

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ApiHubPlugin server.
        """
        return request, metadata

    def post_update_plugin_instance(
        self, response: plugin_service.PluginInstance
    ) -> plugin_service.PluginInstance:
        """Post-rpc interceptor for update_plugin_instance

        DEPRECATED. Please use the `post_update_plugin_instance_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ApiHubPlugin server but before
        it is returned to user code. This `post_update_plugin_instance` interceptor runs
        before the `post_update_plugin_instance_with_metadata` interceptor.
        """
        return response

    def post_update_plugin_instance_with_metadata(
        self,
        response: plugin_service.PluginInstance,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[plugin_service.PluginInstance, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_plugin_instance

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ApiHubPlugin server but before it is returned to user code.

        We recommend only using this `post_update_plugin_instance_with_metadata`
        interceptor in new development instead of the `post_update_plugin_instance` interceptor.
        When both interceptors are used, this `post_update_plugin_instance_with_metadata` interceptor runs after the
        `post_update_plugin_instance` interceptor. The (possibly modified) response returned by
        `post_update_plugin_instance` will be passed to
        `post_update_plugin_instance_with_metadata`.
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
        before they are sent to the ApiHubPlugin server.
        """
        return request, metadata

    def post_get_location(
        self, response: locations_pb2.Location
    ) -> locations_pb2.Location:
        """Post-rpc interceptor for get_location

        Override in a subclass to manipulate the response
        after it is returned by the ApiHubPlugin server but before
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
        before they are sent to the ApiHubPlugin server.
        """
        return request, metadata

    def post_list_locations(
        self, response: locations_pb2.ListLocationsResponse
    ) -> locations_pb2.ListLocationsResponse:
        """Post-rpc interceptor for list_locations

        Override in a subclass to manipulate the response
        after it is returned by the ApiHubPlugin server but before
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
        before they are sent to the ApiHubPlugin server.
        """
        return request, metadata

    def post_cancel_operation(self, response: None) -> None:
        """Post-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the response
        after it is returned by the ApiHubPlugin server but before
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
        before they are sent to the ApiHubPlugin server.
        """
        return request, metadata

    def post_delete_operation(self, response: None) -> None:
        """Post-rpc interceptor for delete_operation

        Override in a subclass to manipulate the response
        after it is returned by the ApiHubPlugin server but before
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
        before they are sent to the ApiHubPlugin server.
        """
        return request, metadata

    def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the ApiHubPlugin server but before
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
        before they are sent to the ApiHubPlugin server.
        """
        return request, metadata

    def post_list_operations(
        self, response: operations_pb2.ListOperationsResponse
    ) -> operations_pb2.ListOperationsResponse:
        """Post-rpc interceptor for list_operations

        Override in a subclass to manipulate the response
        after it is returned by the ApiHubPlugin server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class ApiHubPluginRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: ApiHubPluginRestInterceptor


class ApiHubPluginRestTransport(_BaseApiHubPluginRestTransport):
    """REST backend synchronous transport for ApiHubPlugin.

    This service is used for managing plugins inside the API Hub.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "apihub.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[ApiHubPluginRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'apihub.googleapis.com').
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
            interceptor (Optional[ApiHubPluginRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or ApiHubPluginRestInterceptor()
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

    class _CreatePlugin(
        _BaseApiHubPluginRestTransport._BaseCreatePlugin, ApiHubPluginRestStub
    ):
        def __hash__(self):
            return hash("ApiHubPluginRestTransport.CreatePlugin")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: plugin_service.CreatePluginRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> plugin_service.Plugin:
            r"""Call the create plugin method over HTTP.

            Args:
                request (~.plugin_service.CreatePluginRequest):
                    The request object. The
                [CreatePlugin][google.cloud.apihub.v1.ApiHubPlugin.CreatePlugin]
                method's request.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.plugin_service.Plugin:
                    A plugin resource in the API Hub.
            """

            http_options = (
                _BaseApiHubPluginRestTransport._BaseCreatePlugin._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_plugin(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseApiHubPluginRestTransport._BaseCreatePlugin,
                    "_BaseCreatePlugin__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.apihub_v1.ApiHubPluginClient.CreatePlugin",
                    extra={
                        "serviceName": "google.cloud.apihub.v1.ApiHubPlugin",
                        "rpcName": "CreatePlugin",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ApiHubPluginRestTransport._CreatePlugin._get_response(
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
            resp = plugin_service.Plugin()
            pb_resp = plugin_service.Plugin.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_plugin(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_plugin_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = plugin_service.Plugin.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.apihub_v1.ApiHubPluginClient.create_plugin",
                    extra={
                        "serviceName": "google.cloud.apihub.v1.ApiHubPlugin",
                        "rpcName": "CreatePlugin",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreatePluginInstance(
        _BaseApiHubPluginRestTransport._BaseCreatePluginInstance, ApiHubPluginRestStub
    ):
        def __hash__(self):
            return hash("ApiHubPluginRestTransport.CreatePluginInstance")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: plugin_service.CreatePluginInstanceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create plugin instance method over HTTP.

            Args:
                request (~.plugin_service.CreatePluginInstanceRequest):
                    The request object. The
                [CreatePluginInstance][google.cloud.apihub.v1.ApiHubPlugin.CreatePluginInstance]
                method's request.
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

            http_options = _BaseApiHubPluginRestTransport._BaseCreatePluginInstance._get_http_options()
            request, metadata = self._interceptor.pre_create_plugin_instance(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseApiHubPluginRestTransport._BaseCreatePluginInstance,
                    "_BaseCreatePluginInstance__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.apihub_v1.ApiHubPluginClient.CreatePluginInstance",
                    extra={
                        "serviceName": "google.cloud.apihub.v1.ApiHubPlugin",
                        "rpcName": "CreatePluginInstance",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ApiHubPluginRestTransport._CreatePluginInstance._get_response(
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

            resp = self._interceptor.post_create_plugin_instance(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_plugin_instance_with_metadata(
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
                    "Received response for google.cloud.apihub_v1.ApiHubPluginClient.create_plugin_instance",
                    extra={
                        "serviceName": "google.cloud.apihub.v1.ApiHubPlugin",
                        "rpcName": "CreatePluginInstance",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeletePlugin(
        _BaseApiHubPluginRestTransport._BaseDeletePlugin, ApiHubPluginRestStub
    ):
        def __hash__(self):
            return hash("ApiHubPluginRestTransport.DeletePlugin")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: plugin_service.DeletePluginRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete plugin method over HTTP.

            Args:
                request (~.plugin_service.DeletePluginRequest):
                    The request object. The [DeletePlugin][ApiHub.DeletePlugin] method's
                request.
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
                _BaseApiHubPluginRestTransport._BaseDeletePlugin._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_plugin(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseApiHubPluginRestTransport._BaseDeletePlugin,
                    "_BaseDeletePlugin__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.apihub_v1.ApiHubPluginClient.DeletePlugin",
                    extra={
                        "serviceName": "google.cloud.apihub.v1.ApiHubPlugin",
                        "rpcName": "DeletePlugin",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ApiHubPluginRestTransport._DeletePlugin._get_response(
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

            resp = self._interceptor.post_delete_plugin(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_plugin_with_metadata(
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
                    "Received response for google.cloud.apihub_v1.ApiHubPluginClient.delete_plugin",
                    extra={
                        "serviceName": "google.cloud.apihub.v1.ApiHubPlugin",
                        "rpcName": "DeletePlugin",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeletePluginInstance(
        _BaseApiHubPluginRestTransport._BaseDeletePluginInstance, ApiHubPluginRestStub
    ):
        def __hash__(self):
            return hash("ApiHubPluginRestTransport.DeletePluginInstance")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: plugin_service.DeletePluginInstanceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete plugin instance method over HTTP.

            Args:
                request (~.plugin_service.DeletePluginInstanceRequest):
                    The request object. The
                [DeletePluginInstance][google.cloud.apihub.v1.ApiHubPlugin.DeletePluginInstance]
                method's request.
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

            http_options = _BaseApiHubPluginRestTransport._BaseDeletePluginInstance._get_http_options()
            request, metadata = self._interceptor.pre_delete_plugin_instance(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseApiHubPluginRestTransport._BaseDeletePluginInstance,
                    "_BaseDeletePluginInstance__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.apihub_v1.ApiHubPluginClient.DeletePluginInstance",
                    extra={
                        "serviceName": "google.cloud.apihub.v1.ApiHubPlugin",
                        "rpcName": "DeletePluginInstance",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ApiHubPluginRestTransport._DeletePluginInstance._get_response(
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

            resp = self._interceptor.post_delete_plugin_instance(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_plugin_instance_with_metadata(
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
                    "Received response for google.cloud.apihub_v1.ApiHubPluginClient.delete_plugin_instance",
                    extra={
                        "serviceName": "google.cloud.apihub.v1.ApiHubPlugin",
                        "rpcName": "DeletePluginInstance",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DisablePlugin(
        _BaseApiHubPluginRestTransport._BaseDisablePlugin, ApiHubPluginRestStub
    ):
        def __hash__(self):
            return hash("ApiHubPluginRestTransport.DisablePlugin")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: plugin_service.DisablePluginRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> plugin_service.Plugin:
            r"""Call the disable plugin method over HTTP.

            Args:
                request (~.plugin_service.DisablePluginRequest):
                    The request object. The
                [DisablePlugin][google.cloud.apihub.v1.ApiHubPlugin.DisablePlugin]
                method's request.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.plugin_service.Plugin:
                    A plugin resource in the API Hub.
            """

            http_options = (
                _BaseApiHubPluginRestTransport._BaseDisablePlugin._get_http_options()
            )
            request, metadata = self._interceptor.pre_disable_plugin(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseApiHubPluginRestTransport._BaseDisablePlugin,
                    "_BaseDisablePlugin__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.apihub_v1.ApiHubPluginClient.DisablePlugin",
                    extra={
                        "serviceName": "google.cloud.apihub.v1.ApiHubPlugin",
                        "rpcName": "DisablePlugin",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ApiHubPluginRestTransport._DisablePlugin._get_response(
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
            resp = plugin_service.Plugin()
            pb_resp = plugin_service.Plugin.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_disable_plugin(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_disable_plugin_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = plugin_service.Plugin.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.apihub_v1.ApiHubPluginClient.disable_plugin",
                    extra={
                        "serviceName": "google.cloud.apihub.v1.ApiHubPlugin",
                        "rpcName": "DisablePlugin",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DisablePluginInstanceAction(
        _BaseApiHubPluginRestTransport._BaseDisablePluginInstanceAction,
        ApiHubPluginRestStub,
    ):
        def __hash__(self):
            return hash("ApiHubPluginRestTransport.DisablePluginInstanceAction")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: plugin_service.DisablePluginInstanceActionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the disable plugin instance
            action method over HTTP.

                Args:
                    request (~.plugin_service.DisablePluginInstanceActionRequest):
                        The request object. The
                    [DisablePluginInstanceAction][google.cloud.apihub.v1.ApiHubPlugin.DisablePluginInstanceAction]
                    method's request.
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

            http_options = _BaseApiHubPluginRestTransport._BaseDisablePluginInstanceAction._get_http_options()
            request, metadata = self._interceptor.pre_disable_plugin_instance_action(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseApiHubPluginRestTransport._BaseDisablePluginInstanceAction,
                    "_BaseDisablePluginInstanceAction__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.apihub_v1.ApiHubPluginClient.DisablePluginInstanceAction",
                    extra={
                        "serviceName": "google.cloud.apihub.v1.ApiHubPlugin",
                        "rpcName": "DisablePluginInstanceAction",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ApiHubPluginRestTransport._DisablePluginInstanceAction._get_response(
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

            resp = self._interceptor.post_disable_plugin_instance_action(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_disable_plugin_instance_action_with_metadata(
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
                    "Received response for google.cloud.apihub_v1.ApiHubPluginClient.disable_plugin_instance_action",
                    extra={
                        "serviceName": "google.cloud.apihub.v1.ApiHubPlugin",
                        "rpcName": "DisablePluginInstanceAction",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _EnablePlugin(
        _BaseApiHubPluginRestTransport._BaseEnablePlugin, ApiHubPluginRestStub
    ):
        def __hash__(self):
            return hash("ApiHubPluginRestTransport.EnablePlugin")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: plugin_service.EnablePluginRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> plugin_service.Plugin:
            r"""Call the enable plugin method over HTTP.

            Args:
                request (~.plugin_service.EnablePluginRequest):
                    The request object. The
                [EnablePlugin][google.cloud.apihub.v1.ApiHubPlugin.EnablePlugin]
                method's request.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.plugin_service.Plugin:
                    A plugin resource in the API Hub.
            """

            http_options = (
                _BaseApiHubPluginRestTransport._BaseEnablePlugin._get_http_options()
            )
            request, metadata = self._interceptor.pre_enable_plugin(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseApiHubPluginRestTransport._BaseEnablePlugin,
                    "_BaseEnablePlugin__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.apihub_v1.ApiHubPluginClient.EnablePlugin",
                    extra={
                        "serviceName": "google.cloud.apihub.v1.ApiHubPlugin",
                        "rpcName": "EnablePlugin",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ApiHubPluginRestTransport._EnablePlugin._get_response(
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
            resp = plugin_service.Plugin()
            pb_resp = plugin_service.Plugin.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_enable_plugin(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_enable_plugin_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = plugin_service.Plugin.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.apihub_v1.ApiHubPluginClient.enable_plugin",
                    extra={
                        "serviceName": "google.cloud.apihub.v1.ApiHubPlugin",
                        "rpcName": "EnablePlugin",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _EnablePluginInstanceAction(
        _BaseApiHubPluginRestTransport._BaseEnablePluginInstanceAction,
        ApiHubPluginRestStub,
    ):
        def __hash__(self):
            return hash("ApiHubPluginRestTransport.EnablePluginInstanceAction")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: plugin_service.EnablePluginInstanceActionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the enable plugin instance
            action method over HTTP.

                Args:
                    request (~.plugin_service.EnablePluginInstanceActionRequest):
                        The request object. The
                    [EnablePluginInstanceAction][google.cloud.apihub.v1.ApiHubPlugin.EnablePluginInstanceAction]
                    method's request.
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

            http_options = _BaseApiHubPluginRestTransport._BaseEnablePluginInstanceAction._get_http_options()
            request, metadata = self._interceptor.pre_enable_plugin_instance_action(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseApiHubPluginRestTransport._BaseEnablePluginInstanceAction,
                    "_BaseEnablePluginInstanceAction__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.apihub_v1.ApiHubPluginClient.EnablePluginInstanceAction",
                    extra={
                        "serviceName": "google.cloud.apihub.v1.ApiHubPlugin",
                        "rpcName": "EnablePluginInstanceAction",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ApiHubPluginRestTransport._EnablePluginInstanceAction._get_response(
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

            resp = self._interceptor.post_enable_plugin_instance_action(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_enable_plugin_instance_action_with_metadata(
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
                    "Received response for google.cloud.apihub_v1.ApiHubPluginClient.enable_plugin_instance_action",
                    extra={
                        "serviceName": "google.cloud.apihub.v1.ApiHubPlugin",
                        "rpcName": "EnablePluginInstanceAction",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ExecutePluginInstanceAction(
        _BaseApiHubPluginRestTransport._BaseExecutePluginInstanceAction,
        ApiHubPluginRestStub,
    ):
        def __hash__(self):
            return hash("ApiHubPluginRestTransport.ExecutePluginInstanceAction")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: plugin_service.ExecutePluginInstanceActionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the execute plugin instance
            action method over HTTP.

                Args:
                    request (~.plugin_service.ExecutePluginInstanceActionRequest):
                        The request object. The
                    [ExecutePluginInstanceAction][google.cloud.apihub.v1.ApiHubPlugin.ExecutePluginInstanceAction]
                    method's request.
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

            http_options = _BaseApiHubPluginRestTransport._BaseExecutePluginInstanceAction._get_http_options()
            request, metadata = self._interceptor.pre_execute_plugin_instance_action(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseApiHubPluginRestTransport._BaseExecutePluginInstanceAction,
                    "_BaseExecutePluginInstanceAction__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.apihub_v1.ApiHubPluginClient.ExecutePluginInstanceAction",
                    extra={
                        "serviceName": "google.cloud.apihub.v1.ApiHubPlugin",
                        "rpcName": "ExecutePluginInstanceAction",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ApiHubPluginRestTransport._ExecutePluginInstanceAction._get_response(
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

            resp = self._interceptor.post_execute_plugin_instance_action(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_execute_plugin_instance_action_with_metadata(
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
                    "Received response for google.cloud.apihub_v1.ApiHubPluginClient.execute_plugin_instance_action",
                    extra={
                        "serviceName": "google.cloud.apihub.v1.ApiHubPlugin",
                        "rpcName": "ExecutePluginInstanceAction",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetPlugin(
        _BaseApiHubPluginRestTransport._BaseGetPlugin, ApiHubPluginRestStub
    ):
        def __hash__(self):
            return hash("ApiHubPluginRestTransport.GetPlugin")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: plugin_service.GetPluginRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> plugin_service.Plugin:
            r"""Call the get plugin method over HTTP.

            Args:
                request (~.plugin_service.GetPluginRequest):
                    The request object. The
                [GetPlugin][google.cloud.apihub.v1.ApiHubPlugin.GetPlugin]
                method's request.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.plugin_service.Plugin:
                    A plugin resource in the API Hub.
            """

            http_options = (
                _BaseApiHubPluginRestTransport._BaseGetPlugin._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_plugin(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseApiHubPluginRestTransport._BaseGetPlugin,
                    "_BaseGetPlugin__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.apihub_v1.ApiHubPluginClient.GetPlugin",
                    extra={
                        "serviceName": "google.cloud.apihub.v1.ApiHubPlugin",
                        "rpcName": "GetPlugin",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ApiHubPluginRestTransport._GetPlugin._get_response(
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
            resp = plugin_service.Plugin()
            pb_resp = plugin_service.Plugin.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_plugin(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_plugin_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = plugin_service.Plugin.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.apihub_v1.ApiHubPluginClient.get_plugin",
                    extra={
                        "serviceName": "google.cloud.apihub.v1.ApiHubPlugin",
                        "rpcName": "GetPlugin",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetPluginInstance(
        _BaseApiHubPluginRestTransport._BaseGetPluginInstance, ApiHubPluginRestStub
    ):
        def __hash__(self):
            return hash("ApiHubPluginRestTransport.GetPluginInstance")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: plugin_service.GetPluginInstanceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> plugin_service.PluginInstance:
            r"""Call the get plugin instance method over HTTP.

            Args:
                request (~.plugin_service.GetPluginInstanceRequest):
                    The request object. The
                [GetPluginInstance][google.cloud.apihub.v1.ApiHubPlugin.GetPluginInstance]
                method's request.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.plugin_service.PluginInstance:
                    Represents a plugin instance resource
                in the API Hub. A PluginInstance is a
                specific instance of a hub plugin with
                its own configuration, state, and
                execution details.

            """

            http_options = _BaseApiHubPluginRestTransport._BaseGetPluginInstance._get_http_options()
            request, metadata = self._interceptor.pre_get_plugin_instance(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseApiHubPluginRestTransport._BaseGetPluginInstance,
                    "_BaseGetPluginInstance__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.apihub_v1.ApiHubPluginClient.GetPluginInstance",
                    extra={
                        "serviceName": "google.cloud.apihub.v1.ApiHubPlugin",
                        "rpcName": "GetPluginInstance",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ApiHubPluginRestTransport._GetPluginInstance._get_response(
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
            resp = plugin_service.PluginInstance()
            pb_resp = plugin_service.PluginInstance.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_plugin_instance(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_plugin_instance_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = plugin_service.PluginInstance.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.apihub_v1.ApiHubPluginClient.get_plugin_instance",
                    extra={
                        "serviceName": "google.cloud.apihub.v1.ApiHubPlugin",
                        "rpcName": "GetPluginInstance",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListPluginInstances(
        _BaseApiHubPluginRestTransport._BaseListPluginInstances, ApiHubPluginRestStub
    ):
        def __hash__(self):
            return hash("ApiHubPluginRestTransport.ListPluginInstances")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: plugin_service.ListPluginInstancesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> plugin_service.ListPluginInstancesResponse:
            r"""Call the list plugin instances method over HTTP.

            Args:
                request (~.plugin_service.ListPluginInstancesRequest):
                    The request object. The
                [ListPluginInstances][google.cloud.apihub.v1.ApiHubPlugin.ListPluginInstances]
                method's request.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.plugin_service.ListPluginInstancesResponse:
                    The
                [ListPluginInstances][google.cloud.apihub.v1.ApiHubPlugin.ListPluginInstances]
                method's response.

            """

            http_options = _BaseApiHubPluginRestTransport._BaseListPluginInstances._get_http_options()
            request, metadata = self._interceptor.pre_list_plugin_instances(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseApiHubPluginRestTransport._BaseListPluginInstances,
                    "_BaseListPluginInstances__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.apihub_v1.ApiHubPluginClient.ListPluginInstances",
                    extra={
                        "serviceName": "google.cloud.apihub.v1.ApiHubPlugin",
                        "rpcName": "ListPluginInstances",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ApiHubPluginRestTransport._ListPluginInstances._get_response(
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
            resp = plugin_service.ListPluginInstancesResponse()
            pb_resp = plugin_service.ListPluginInstancesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_plugin_instances(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_plugin_instances_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        plugin_service.ListPluginInstancesResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.apihub_v1.ApiHubPluginClient.list_plugin_instances",
                    extra={
                        "serviceName": "google.cloud.apihub.v1.ApiHubPlugin",
                        "rpcName": "ListPluginInstances",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListPlugins(
        _BaseApiHubPluginRestTransport._BaseListPlugins, ApiHubPluginRestStub
    ):
        def __hash__(self):
            return hash("ApiHubPluginRestTransport.ListPlugins")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: plugin_service.ListPluginsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> plugin_service.ListPluginsResponse:
            r"""Call the list plugins method over HTTP.

            Args:
                request (~.plugin_service.ListPluginsRequest):
                    The request object. The
                [ListPlugins][google.cloud.apihub.v1.ApiHubPlugin.ListPlugins]
                method's request.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.plugin_service.ListPluginsResponse:
                    The
                [ListPlugins][google.cloud.apihub.v1.ApiHubPlugin.ListPlugins]
                method's response.

            """

            http_options = (
                _BaseApiHubPluginRestTransport._BaseListPlugins._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_plugins(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseApiHubPluginRestTransport._BaseListPlugins,
                    "_BaseListPlugins__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.apihub_v1.ApiHubPluginClient.ListPlugins",
                    extra={
                        "serviceName": "google.cloud.apihub.v1.ApiHubPlugin",
                        "rpcName": "ListPlugins",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ApiHubPluginRestTransport._ListPlugins._get_response(
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
            resp = plugin_service.ListPluginsResponse()
            pb_resp = plugin_service.ListPluginsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_plugins(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_plugins_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = plugin_service.ListPluginsResponse.to_json(
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
                    "Received response for google.cloud.apihub_v1.ApiHubPluginClient.list_plugins",
                    extra={
                        "serviceName": "google.cloud.apihub.v1.ApiHubPlugin",
                        "rpcName": "ListPlugins",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdatePluginInstance(
        _BaseApiHubPluginRestTransport._BaseUpdatePluginInstance, ApiHubPluginRestStub
    ):
        def __hash__(self):
            return hash("ApiHubPluginRestTransport.UpdatePluginInstance")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: plugin_service.UpdatePluginInstanceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> plugin_service.PluginInstance:
            r"""Call the update plugin instance method over HTTP.

            Args:
                request (~.plugin_service.UpdatePluginInstanceRequest):
                    The request object. The
                [UpdatePluginInstance][google.cloud.apihub.v1.ApiHubPlugin.UpdatePluginInstance]
                method's request.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.plugin_service.PluginInstance:
                    Represents a plugin instance resource
                in the API Hub. A PluginInstance is a
                specific instance of a hub plugin with
                its own configuration, state, and
                execution details.

            """

            http_options = _BaseApiHubPluginRestTransport._BaseUpdatePluginInstance._get_http_options()
            request, metadata = self._interceptor.pre_update_plugin_instance(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseApiHubPluginRestTransport._BaseUpdatePluginInstance,
                    "_BaseUpdatePluginInstance__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.apihub_v1.ApiHubPluginClient.UpdatePluginInstance",
                    extra={
                        "serviceName": "google.cloud.apihub.v1.ApiHubPlugin",
                        "rpcName": "UpdatePluginInstance",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ApiHubPluginRestTransport._UpdatePluginInstance._get_response(
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
            resp = plugin_service.PluginInstance()
            pb_resp = plugin_service.PluginInstance.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_plugin_instance(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_plugin_instance_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = plugin_service.PluginInstance.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.apihub_v1.ApiHubPluginClient.update_plugin_instance",
                    extra={
                        "serviceName": "google.cloud.apihub.v1.ApiHubPlugin",
                        "rpcName": "UpdatePluginInstance",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def create_plugin(
        self,
    ) -> Callable[[plugin_service.CreatePluginRequest], plugin_service.Plugin]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreatePlugin(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_plugin_instance(
        self,
    ) -> Callable[
        [plugin_service.CreatePluginInstanceRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreatePluginInstance(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_plugin(
        self,
    ) -> Callable[[plugin_service.DeletePluginRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeletePlugin(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_plugin_instance(
        self,
    ) -> Callable[
        [plugin_service.DeletePluginInstanceRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeletePluginInstance(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def disable_plugin(
        self,
    ) -> Callable[[plugin_service.DisablePluginRequest], plugin_service.Plugin]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DisablePlugin(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def disable_plugin_instance_action(
        self,
    ) -> Callable[
        [plugin_service.DisablePluginInstanceActionRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DisablePluginInstanceAction(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def enable_plugin(
        self,
    ) -> Callable[[plugin_service.EnablePluginRequest], plugin_service.Plugin]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._EnablePlugin(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def enable_plugin_instance_action(
        self,
    ) -> Callable[
        [plugin_service.EnablePluginInstanceActionRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._EnablePluginInstanceAction(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def execute_plugin_instance_action(
        self,
    ) -> Callable[
        [plugin_service.ExecutePluginInstanceActionRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ExecutePluginInstanceAction(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def get_plugin(
        self,
    ) -> Callable[[plugin_service.GetPluginRequest], plugin_service.Plugin]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetPlugin(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_plugin_instance(
        self,
    ) -> Callable[
        [plugin_service.GetPluginInstanceRequest], plugin_service.PluginInstance
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetPluginInstance(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_plugin_instances(
        self,
    ) -> Callable[
        [plugin_service.ListPluginInstancesRequest],
        plugin_service.ListPluginInstancesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListPluginInstances(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_plugins(
        self,
    ) -> Callable[
        [plugin_service.ListPluginsRequest], plugin_service.ListPluginsResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListPlugins(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_plugin_instance(
        self,
    ) -> Callable[
        [plugin_service.UpdatePluginInstanceRequest], plugin_service.PluginInstance
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdatePluginInstance(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_location(self):
        return self._GetLocation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetLocation(
        _BaseApiHubPluginRestTransport._BaseGetLocation, ApiHubPluginRestStub
    ):
        def __hash__(self):
            return hash("ApiHubPluginRestTransport.GetLocation")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
                _BaseApiHubPluginRestTransport._BaseGetLocation._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_location(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseApiHubPluginRestTransport._BaseGetLocation,
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
                    f"Sending request for google.cloud.apihub_v1.ApiHubPluginClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.apihub.v1.ApiHubPlugin",
                        "rpcName": "GetLocation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ApiHubPluginRestTransport._GetLocation._get_response(
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
                    "Received response for google.cloud.apihub_v1.ApiHubPluginAsyncClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.apihub.v1.ApiHubPlugin",
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
        _BaseApiHubPluginRestTransport._BaseListLocations, ApiHubPluginRestStub
    ):
        def __hash__(self):
            return hash("ApiHubPluginRestTransport.ListLocations")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
                _BaseApiHubPluginRestTransport._BaseListLocations._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_locations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseApiHubPluginRestTransport._BaseListLocations,
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
                    f"Sending request for google.cloud.apihub_v1.ApiHubPluginClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.apihub.v1.ApiHubPlugin",
                        "rpcName": "ListLocations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ApiHubPluginRestTransport._ListLocations._get_response(
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
                    "Received response for google.cloud.apihub_v1.ApiHubPluginAsyncClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.apihub.v1.ApiHubPlugin",
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
        _BaseApiHubPluginRestTransport._BaseCancelOperation, ApiHubPluginRestStub
    ):
        def __hash__(self):
            return hash("ApiHubPluginRestTransport.CancelOperation")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
                _BaseApiHubPluginRestTransport._BaseCancelOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_cancel_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseApiHubPluginRestTransport._BaseCancelOperation,
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
                    f"Sending request for google.cloud.apihub_v1.ApiHubPluginClient.CancelOperation",
                    extra={
                        "serviceName": "google.cloud.apihub.v1.ApiHubPlugin",
                        "rpcName": "CancelOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ApiHubPluginRestTransport._CancelOperation._get_response(
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
        _BaseApiHubPluginRestTransport._BaseDeleteOperation, ApiHubPluginRestStub
    ):
        def __hash__(self):
            return hash("ApiHubPluginRestTransport.DeleteOperation")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
                _BaseApiHubPluginRestTransport._BaseDeleteOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseApiHubPluginRestTransport._BaseDeleteOperation,
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
                    f"Sending request for google.cloud.apihub_v1.ApiHubPluginClient.DeleteOperation",
                    extra={
                        "serviceName": "google.cloud.apihub.v1.ApiHubPlugin",
                        "rpcName": "DeleteOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ApiHubPluginRestTransport._DeleteOperation._get_response(
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
        _BaseApiHubPluginRestTransport._BaseGetOperation, ApiHubPluginRestStub
    ):
        def __hash__(self):
            return hash("ApiHubPluginRestTransport.GetOperation")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
                _BaseApiHubPluginRestTransport._BaseGetOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_operation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseApiHubPluginRestTransport._BaseGetOperation,
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
                    f"Sending request for google.cloud.apihub_v1.ApiHubPluginClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.apihub.v1.ApiHubPlugin",
                        "rpcName": "GetOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ApiHubPluginRestTransport._GetOperation._get_response(
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
                    "Received response for google.cloud.apihub_v1.ApiHubPluginAsyncClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.apihub.v1.ApiHubPlugin",
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
        _BaseApiHubPluginRestTransport._BaseListOperations, ApiHubPluginRestStub
    ):
        def __hash__(self):
            return hash("ApiHubPluginRestTransport.ListOperations")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
                _BaseApiHubPluginRestTransport._BaseListOperations._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_operations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseApiHubPluginRestTransport._BaseListOperations,
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
                    f"Sending request for google.cloud.apihub_v1.ApiHubPluginClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.apihub.v1.ApiHubPlugin",
                        "rpcName": "ListOperations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ApiHubPluginRestTransport._ListOperations._get_response(
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
                    "Received response for google.cloud.apihub_v1.ApiHubPluginAsyncClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.apihub.v1.ApiHubPlugin",
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


__all__ = ("ApiHubPluginRestTransport",)
