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
from google.api_core import gapic_v1, rest_helpers, rest_streaming
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.auth.transport.requests import AuthorizedSession  # type: ignore
from google.protobuf import json_format
from requests import __version__ as requests_version

from google.maps.mapmanagement_v2beta._compat import transcode_request
from google.maps.mapmanagement_v2beta.types import map_management_service

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseMapManagementRestTransport

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


class MapManagementRestInterceptor:
    """Interceptor for MapManagement.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the MapManagementRestTransport.

    .. code-block:: python
        class MyCustomMapManagementInterceptor(MapManagementRestInterceptor):
            def pre_create_map_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_map_config(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_map_context_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_map_context_config(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_style_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_style_config(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_map_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_delete_map_context_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_delete_style_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_get_map_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_map_config(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_map_context_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_map_context_config(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_style_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_style_config(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_map_configs(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_map_configs(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_map_context_configs(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_map_context_configs(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_style_configs(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_style_configs(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_map_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_map_config(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_map_context_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_map_context_config(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_style_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_style_config(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = MapManagementRestTransport(interceptor=MyCustomMapManagementInterceptor())
        client = MapManagementClient(transport=transport)


    """

    def pre_create_map_config(
        self,
        request: map_management_service.CreateMapConfigRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        map_management_service.CreateMapConfigRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_map_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the MapManagement server.
        """
        return request, metadata

    def post_create_map_config(
        self, response: map_management_service.MapConfig
    ) -> map_management_service.MapConfig:
        """Post-rpc interceptor for create_map_config

        DEPRECATED. Please use the `post_create_map_config_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the MapManagement server but before
        it is returned to user code. This `post_create_map_config` interceptor runs
        before the `post_create_map_config_with_metadata` interceptor.
        """
        return response

    def post_create_map_config_with_metadata(
        self,
        response: map_management_service.MapConfig,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        map_management_service.MapConfig, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for create_map_config

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the MapManagement server but before it is returned to user code.

        We recommend only using this `post_create_map_config_with_metadata`
        interceptor in new development instead of the `post_create_map_config` interceptor.
        When both interceptors are used, this `post_create_map_config_with_metadata` interceptor runs after the
        `post_create_map_config` interceptor. The (possibly modified) response returned by
        `post_create_map_config` will be passed to
        `post_create_map_config_with_metadata`.
        """
        return response, metadata

    def pre_create_map_context_config(
        self,
        request: map_management_service.CreateMapContextConfigRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        map_management_service.CreateMapContextConfigRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_map_context_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the MapManagement server.
        """
        return request, metadata

    def post_create_map_context_config(
        self, response: map_management_service.MapContextConfig
    ) -> map_management_service.MapContextConfig:
        """Post-rpc interceptor for create_map_context_config

        DEPRECATED. Please use the `post_create_map_context_config_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the MapManagement server but before
        it is returned to user code. This `post_create_map_context_config` interceptor runs
        before the `post_create_map_context_config_with_metadata` interceptor.
        """
        return response

    def post_create_map_context_config_with_metadata(
        self,
        response: map_management_service.MapContextConfig,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        map_management_service.MapContextConfig, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for create_map_context_config

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the MapManagement server but before it is returned to user code.

        We recommend only using this `post_create_map_context_config_with_metadata`
        interceptor in new development instead of the `post_create_map_context_config` interceptor.
        When both interceptors are used, this `post_create_map_context_config_with_metadata` interceptor runs after the
        `post_create_map_context_config` interceptor. The (possibly modified) response returned by
        `post_create_map_context_config` will be passed to
        `post_create_map_context_config_with_metadata`.
        """
        return response, metadata

    def pre_create_style_config(
        self,
        request: map_management_service.CreateStyleConfigRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        map_management_service.CreateStyleConfigRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_style_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the MapManagement server.
        """
        return request, metadata

    def post_create_style_config(
        self, response: map_management_service.StyleConfig
    ) -> map_management_service.StyleConfig:
        """Post-rpc interceptor for create_style_config

        DEPRECATED. Please use the `post_create_style_config_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the MapManagement server but before
        it is returned to user code. This `post_create_style_config` interceptor runs
        before the `post_create_style_config_with_metadata` interceptor.
        """
        return response

    def post_create_style_config_with_metadata(
        self,
        response: map_management_service.StyleConfig,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        map_management_service.StyleConfig, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for create_style_config

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the MapManagement server but before it is returned to user code.

        We recommend only using this `post_create_style_config_with_metadata`
        interceptor in new development instead of the `post_create_style_config` interceptor.
        When both interceptors are used, this `post_create_style_config_with_metadata` interceptor runs after the
        `post_create_style_config` interceptor. The (possibly modified) response returned by
        `post_create_style_config` will be passed to
        `post_create_style_config_with_metadata`.
        """
        return response, metadata

    def pre_delete_map_config(
        self,
        request: map_management_service.DeleteMapConfigRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        map_management_service.DeleteMapConfigRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_map_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the MapManagement server.
        """
        return request, metadata

    def pre_delete_map_context_config(
        self,
        request: map_management_service.DeleteMapContextConfigRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        map_management_service.DeleteMapContextConfigRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_map_context_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the MapManagement server.
        """
        return request, metadata

    def pre_delete_style_config(
        self,
        request: map_management_service.DeleteStyleConfigRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        map_management_service.DeleteStyleConfigRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_style_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the MapManagement server.
        """
        return request, metadata

    def pre_get_map_config(
        self,
        request: map_management_service.GetMapConfigRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        map_management_service.GetMapConfigRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_map_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the MapManagement server.
        """
        return request, metadata

    def post_get_map_config(
        self, response: map_management_service.MapConfig
    ) -> map_management_service.MapConfig:
        """Post-rpc interceptor for get_map_config

        DEPRECATED. Please use the `post_get_map_config_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the MapManagement server but before
        it is returned to user code. This `post_get_map_config` interceptor runs
        before the `post_get_map_config_with_metadata` interceptor.
        """
        return response

    def post_get_map_config_with_metadata(
        self,
        response: map_management_service.MapConfig,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        map_management_service.MapConfig, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for get_map_config

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the MapManagement server but before it is returned to user code.

        We recommend only using this `post_get_map_config_with_metadata`
        interceptor in new development instead of the `post_get_map_config` interceptor.
        When both interceptors are used, this `post_get_map_config_with_metadata` interceptor runs after the
        `post_get_map_config` interceptor. The (possibly modified) response returned by
        `post_get_map_config` will be passed to
        `post_get_map_config_with_metadata`.
        """
        return response, metadata

    def pre_get_map_context_config(
        self,
        request: map_management_service.GetMapContextConfigRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        map_management_service.GetMapContextConfigRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_map_context_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the MapManagement server.
        """
        return request, metadata

    def post_get_map_context_config(
        self, response: map_management_service.MapContextConfig
    ) -> map_management_service.MapContextConfig:
        """Post-rpc interceptor for get_map_context_config

        DEPRECATED. Please use the `post_get_map_context_config_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the MapManagement server but before
        it is returned to user code. This `post_get_map_context_config` interceptor runs
        before the `post_get_map_context_config_with_metadata` interceptor.
        """
        return response

    def post_get_map_context_config_with_metadata(
        self,
        response: map_management_service.MapContextConfig,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        map_management_service.MapContextConfig, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for get_map_context_config

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the MapManagement server but before it is returned to user code.

        We recommend only using this `post_get_map_context_config_with_metadata`
        interceptor in new development instead of the `post_get_map_context_config` interceptor.
        When both interceptors are used, this `post_get_map_context_config_with_metadata` interceptor runs after the
        `post_get_map_context_config` interceptor. The (possibly modified) response returned by
        `post_get_map_context_config` will be passed to
        `post_get_map_context_config_with_metadata`.
        """
        return response, metadata

    def pre_get_style_config(
        self,
        request: map_management_service.GetStyleConfigRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        map_management_service.GetStyleConfigRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_style_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the MapManagement server.
        """
        return request, metadata

    def post_get_style_config(
        self, response: map_management_service.StyleConfig
    ) -> map_management_service.StyleConfig:
        """Post-rpc interceptor for get_style_config

        DEPRECATED. Please use the `post_get_style_config_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the MapManagement server but before
        it is returned to user code. This `post_get_style_config` interceptor runs
        before the `post_get_style_config_with_metadata` interceptor.
        """
        return response

    def post_get_style_config_with_metadata(
        self,
        response: map_management_service.StyleConfig,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        map_management_service.StyleConfig, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for get_style_config

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the MapManagement server but before it is returned to user code.

        We recommend only using this `post_get_style_config_with_metadata`
        interceptor in new development instead of the `post_get_style_config` interceptor.
        When both interceptors are used, this `post_get_style_config_with_metadata` interceptor runs after the
        `post_get_style_config` interceptor. The (possibly modified) response returned by
        `post_get_style_config` will be passed to
        `post_get_style_config_with_metadata`.
        """
        return response, metadata

    def pre_list_map_configs(
        self,
        request: map_management_service.ListMapConfigsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        map_management_service.ListMapConfigsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_map_configs

        Override in a subclass to manipulate the request or metadata
        before they are sent to the MapManagement server.
        """
        return request, metadata

    def post_list_map_configs(
        self, response: map_management_service.ListMapConfigsResponse
    ) -> map_management_service.ListMapConfigsResponse:
        """Post-rpc interceptor for list_map_configs

        DEPRECATED. Please use the `post_list_map_configs_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the MapManagement server but before
        it is returned to user code. This `post_list_map_configs` interceptor runs
        before the `post_list_map_configs_with_metadata` interceptor.
        """
        return response

    def post_list_map_configs_with_metadata(
        self,
        response: map_management_service.ListMapConfigsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        map_management_service.ListMapConfigsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_map_configs

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the MapManagement server but before it is returned to user code.

        We recommend only using this `post_list_map_configs_with_metadata`
        interceptor in new development instead of the `post_list_map_configs` interceptor.
        When both interceptors are used, this `post_list_map_configs_with_metadata` interceptor runs after the
        `post_list_map_configs` interceptor. The (possibly modified) response returned by
        `post_list_map_configs` will be passed to
        `post_list_map_configs_with_metadata`.
        """
        return response, metadata

    def pre_list_map_context_configs(
        self,
        request: map_management_service.ListMapContextConfigsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        map_management_service.ListMapContextConfigsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_map_context_configs

        Override in a subclass to manipulate the request or metadata
        before they are sent to the MapManagement server.
        """
        return request, metadata

    def post_list_map_context_configs(
        self, response: map_management_service.ListMapContextConfigsResponse
    ) -> map_management_service.ListMapContextConfigsResponse:
        """Post-rpc interceptor for list_map_context_configs

        DEPRECATED. Please use the `post_list_map_context_configs_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the MapManagement server but before
        it is returned to user code. This `post_list_map_context_configs` interceptor runs
        before the `post_list_map_context_configs_with_metadata` interceptor.
        """
        return response

    def post_list_map_context_configs_with_metadata(
        self,
        response: map_management_service.ListMapContextConfigsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        map_management_service.ListMapContextConfigsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_map_context_configs

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the MapManagement server but before it is returned to user code.

        We recommend only using this `post_list_map_context_configs_with_metadata`
        interceptor in new development instead of the `post_list_map_context_configs` interceptor.
        When both interceptors are used, this `post_list_map_context_configs_with_metadata` interceptor runs after the
        `post_list_map_context_configs` interceptor. The (possibly modified) response returned by
        `post_list_map_context_configs` will be passed to
        `post_list_map_context_configs_with_metadata`.
        """
        return response, metadata

    def pre_list_style_configs(
        self,
        request: map_management_service.ListStyleConfigsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        map_management_service.ListStyleConfigsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_style_configs

        Override in a subclass to manipulate the request or metadata
        before they are sent to the MapManagement server.
        """
        return request, metadata

    def post_list_style_configs(
        self, response: map_management_service.ListStyleConfigsResponse
    ) -> map_management_service.ListStyleConfigsResponse:
        """Post-rpc interceptor for list_style_configs

        DEPRECATED. Please use the `post_list_style_configs_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the MapManagement server but before
        it is returned to user code. This `post_list_style_configs` interceptor runs
        before the `post_list_style_configs_with_metadata` interceptor.
        """
        return response

    def post_list_style_configs_with_metadata(
        self,
        response: map_management_service.ListStyleConfigsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        map_management_service.ListStyleConfigsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_style_configs

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the MapManagement server but before it is returned to user code.

        We recommend only using this `post_list_style_configs_with_metadata`
        interceptor in new development instead of the `post_list_style_configs` interceptor.
        When both interceptors are used, this `post_list_style_configs_with_metadata` interceptor runs after the
        `post_list_style_configs` interceptor. The (possibly modified) response returned by
        `post_list_style_configs` will be passed to
        `post_list_style_configs_with_metadata`.
        """
        return response, metadata

    def pre_update_map_config(
        self,
        request: map_management_service.UpdateMapConfigRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        map_management_service.UpdateMapConfigRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_map_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the MapManagement server.
        """
        return request, metadata

    def post_update_map_config(
        self, response: map_management_service.MapConfig
    ) -> map_management_service.MapConfig:
        """Post-rpc interceptor for update_map_config

        DEPRECATED. Please use the `post_update_map_config_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the MapManagement server but before
        it is returned to user code. This `post_update_map_config` interceptor runs
        before the `post_update_map_config_with_metadata` interceptor.
        """
        return response

    def post_update_map_config_with_metadata(
        self,
        response: map_management_service.MapConfig,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        map_management_service.MapConfig, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for update_map_config

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the MapManagement server but before it is returned to user code.

        We recommend only using this `post_update_map_config_with_metadata`
        interceptor in new development instead of the `post_update_map_config` interceptor.
        When both interceptors are used, this `post_update_map_config_with_metadata` interceptor runs after the
        `post_update_map_config` interceptor. The (possibly modified) response returned by
        `post_update_map_config` will be passed to
        `post_update_map_config_with_metadata`.
        """
        return response, metadata

    def pre_update_map_context_config(
        self,
        request: map_management_service.UpdateMapContextConfigRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        map_management_service.UpdateMapContextConfigRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_map_context_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the MapManagement server.
        """
        return request, metadata

    def post_update_map_context_config(
        self, response: map_management_service.MapContextConfig
    ) -> map_management_service.MapContextConfig:
        """Post-rpc interceptor for update_map_context_config

        DEPRECATED. Please use the `post_update_map_context_config_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the MapManagement server but before
        it is returned to user code. This `post_update_map_context_config` interceptor runs
        before the `post_update_map_context_config_with_metadata` interceptor.
        """
        return response

    def post_update_map_context_config_with_metadata(
        self,
        response: map_management_service.MapContextConfig,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        map_management_service.MapContextConfig, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for update_map_context_config

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the MapManagement server but before it is returned to user code.

        We recommend only using this `post_update_map_context_config_with_metadata`
        interceptor in new development instead of the `post_update_map_context_config` interceptor.
        When both interceptors are used, this `post_update_map_context_config_with_metadata` interceptor runs after the
        `post_update_map_context_config` interceptor. The (possibly modified) response returned by
        `post_update_map_context_config` will be passed to
        `post_update_map_context_config_with_metadata`.
        """
        return response, metadata

    def pre_update_style_config(
        self,
        request: map_management_service.UpdateStyleConfigRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        map_management_service.UpdateStyleConfigRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_style_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the MapManagement server.
        """
        return request, metadata

    def post_update_style_config(
        self, response: map_management_service.StyleConfig
    ) -> map_management_service.StyleConfig:
        """Post-rpc interceptor for update_style_config

        DEPRECATED. Please use the `post_update_style_config_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the MapManagement server but before
        it is returned to user code. This `post_update_style_config` interceptor runs
        before the `post_update_style_config_with_metadata` interceptor.
        """
        return response

    def post_update_style_config_with_metadata(
        self,
        response: map_management_service.StyleConfig,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        map_management_service.StyleConfig, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for update_style_config

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the MapManagement server but before it is returned to user code.

        We recommend only using this `post_update_style_config_with_metadata`
        interceptor in new development instead of the `post_update_style_config` interceptor.
        When both interceptors are used, this `post_update_style_config_with_metadata` interceptor runs after the
        `post_update_style_config` interceptor. The (possibly modified) response returned by
        `post_update_style_config` will be passed to
        `post_update_style_config_with_metadata`.
        """
        return response, metadata


@dataclasses.dataclass
class MapManagementRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: MapManagementRestInterceptor


class MapManagementRestTransport(_BaseMapManagementRestTransport):
    """REST backend synchronous transport for MapManagement.

    The Map Management API uses your inputs to create and manage Google
    Cloud based styling resources for Google Maps.

    Using this API, you can can create and manage MapConfigs (Map IDs),
    StyleConfigs (JSON-based styling), and MapContextConfigs
    (associations between styles, datasets, and map variants).

    This API offers features through three channels:

    - ``v2alpha``: Experimental features.
    - ``v2beta``: Preview features, recommended for early adoption.
    - ``v2``: General Availability (GA) features.

    Capabilities described here are generally available across both the
    v2alpha and v2beta endpoints.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "mapmanagement.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[MapManagementRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'mapmanagement.googleapis.com').
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
            interceptor (Optional[MapManagementRestInterceptor]): Interceptor used
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
        if client_cert_source_for_mtls:
            self._session.configure_mtls_channel(client_cert_source_for_mtls)
        self._interceptor = interceptor or MapManagementRestInterceptor()
        self._prep_wrapped_messages(client_info)

    class _CreateMapConfig(
        _BaseMapManagementRestTransport._BaseCreateMapConfig, MapManagementRestStub
    ):
        def __hash__(self):
            return hash("MapManagementRestTransport.CreateMapConfig")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: map_management_service.CreateMapConfigRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> map_management_service.MapConfig:
            r"""Call the create map config method over HTTP.

            Args:
                request (~.map_management_service.CreateMapConfigRequest):
                    The request object. Request to create a MapConfig.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.map_management_service.MapConfig:
                    Represents a single map in a Maps API
                client application. The MapConfig is the
                parent resource of MapContextConfigs and
                enables custom styling in SDKs
                (Mobile/Web). A MapConfig can have
                multiple MapContextConfigs, each
                applying styling to specific map
                variants.
                Next ID = 9;

            """

            http_options = (
                _BaseMapManagementRestTransport._BaseCreateMapConfig._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_map_config(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseMapManagementRestTransport._BaseCreateMapConfig,
                    "_BaseCreateMapConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.maps.mapmanagement_v2beta.MapManagementClient.CreateMapConfig",
                    extra={
                        "serviceName": "google.maps.mapmanagement.v2beta.MapManagement",
                        "rpcName": "CreateMapConfig",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = MapManagementRestTransport._CreateMapConfig._get_response(
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
            resp = map_management_service.MapConfig()
            pb_resp = map_management_service.MapConfig.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_map_config(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_map_config_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = map_management_service.MapConfig.to_json(
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
                    "Received response for google.maps.mapmanagement_v2beta.MapManagementClient.create_map_config",
                    extra={
                        "serviceName": "google.maps.mapmanagement.v2beta.MapManagement",
                        "rpcName": "CreateMapConfig",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateMapContextConfig(
        _BaseMapManagementRestTransport._BaseCreateMapContextConfig,
        MapManagementRestStub,
    ):
        def __hash__(self):
            return hash("MapManagementRestTransport.CreateMapContextConfig")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: map_management_service.CreateMapContextConfigRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> map_management_service.MapContextConfig:
            r"""Call the create map context config method over HTTP.

            Args:
                request (~.map_management_service.CreateMapContextConfigRequest):
                    The request object. Request to create a MapContextConfig.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.map_management_service.MapContextConfig:
                    Encapsulates the styling
                configuration for a map. The
                MapContextConfig associates styling
                components, such as a StyleConfig and
                Datasets, with specific map variants of
                a MapConfig. When the MapConfig is
                loaded in an SDK, the styling and
                dataset information from the
                MapContextConfig are applied to the
                specified map variants.
                Next ID = 10;

            """

            http_options = _BaseMapManagementRestTransport._BaseCreateMapContextConfig._get_http_options()
            request, metadata = self._interceptor.pre_create_map_context_config(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseMapManagementRestTransport._BaseCreateMapContextConfig,
                    "_BaseCreateMapContextConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.maps.mapmanagement_v2beta.MapManagementClient.CreateMapContextConfig",
                    extra={
                        "serviceName": "google.maps.mapmanagement.v2beta.MapManagement",
                        "rpcName": "CreateMapContextConfig",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = MapManagementRestTransport._CreateMapContextConfig._get_response(
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
            resp = map_management_service.MapContextConfig()
            pb_resp = map_management_service.MapContextConfig.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_map_context_config(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_map_context_config_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = map_management_service.MapContextConfig.to_json(
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
                    "Received response for google.maps.mapmanagement_v2beta.MapManagementClient.create_map_context_config",
                    extra={
                        "serviceName": "google.maps.mapmanagement.v2beta.MapManagement",
                        "rpcName": "CreateMapContextConfig",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateStyleConfig(
        _BaseMapManagementRestTransport._BaseCreateStyleConfig, MapManagementRestStub
    ):
        def __hash__(self):
            return hash("MapManagementRestTransport.CreateStyleConfig")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: map_management_service.CreateStyleConfigRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> map_management_service.StyleConfig:
            r"""Call the create style config method over HTTP.

            Args:
                request (~.map_management_service.CreateStyleConfigRequest):
                    The request object. Request to create a StyleConfig.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.map_management_service.StyleConfig:
                    Represents a single style in a Maps
                API client application. The StyleConfig
                contains the style sheet that defines
                the visual appearance of the map. Next
                ID = 9;

            """

            http_options = _BaseMapManagementRestTransport._BaseCreateStyleConfig._get_http_options()
            request, metadata = self._interceptor.pre_create_style_config(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseMapManagementRestTransport._BaseCreateStyleConfig,
                    "_BaseCreateStyleConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.maps.mapmanagement_v2beta.MapManagementClient.CreateStyleConfig",
                    extra={
                        "serviceName": "google.maps.mapmanagement.v2beta.MapManagement",
                        "rpcName": "CreateStyleConfig",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = MapManagementRestTransport._CreateStyleConfig._get_response(
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
            resp = map_management_service.StyleConfig()
            pb_resp = map_management_service.StyleConfig.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_style_config(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_style_config_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = map_management_service.StyleConfig.to_json(
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
                    "Received response for google.maps.mapmanagement_v2beta.MapManagementClient.create_style_config",
                    extra={
                        "serviceName": "google.maps.mapmanagement.v2beta.MapManagement",
                        "rpcName": "CreateStyleConfig",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteMapConfig(
        _BaseMapManagementRestTransport._BaseDeleteMapConfig, MapManagementRestStub
    ):
        def __hash__(self):
            return hash("MapManagementRestTransport.DeleteMapConfig")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: map_management_service.DeleteMapConfigRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete map config method over HTTP.

            Args:
                request (~.map_management_service.DeleteMapConfigRequest):
                    The request object. Request to delete a MapConfig. If the
                MapConfig has any child
                MapContextConfigs, those will be deleted
                as well.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = (
                _BaseMapManagementRestTransport._BaseDeleteMapConfig._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_map_config(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseMapManagementRestTransport._BaseDeleteMapConfig,
                    "_BaseDeleteMapConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.maps.mapmanagement_v2beta.MapManagementClient.DeleteMapConfig",
                    extra={
                        "serviceName": "google.maps.mapmanagement.v2beta.MapManagement",
                        "rpcName": "DeleteMapConfig",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = MapManagementRestTransport._DeleteMapConfig._get_response(
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

    class _DeleteMapContextConfig(
        _BaseMapManagementRestTransport._BaseDeleteMapContextConfig,
        MapManagementRestStub,
    ):
        def __hash__(self):
            return hash("MapManagementRestTransport.DeleteMapContextConfig")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: map_management_service.DeleteMapContextConfigRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete map context config method over HTTP.

            Args:
                request (~.map_management_service.DeleteMapContextConfigRequest):
                    The request object. Request to delete a MapContextConfig.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = _BaseMapManagementRestTransport._BaseDeleteMapContextConfig._get_http_options()
            request, metadata = self._interceptor.pre_delete_map_context_config(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseMapManagementRestTransport._BaseDeleteMapContextConfig,
                    "_BaseDeleteMapContextConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.maps.mapmanagement_v2beta.MapManagementClient.DeleteMapContextConfig",
                    extra={
                        "serviceName": "google.maps.mapmanagement.v2beta.MapManagement",
                        "rpcName": "DeleteMapContextConfig",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = MapManagementRestTransport._DeleteMapContextConfig._get_response(
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

    class _DeleteStyleConfig(
        _BaseMapManagementRestTransport._BaseDeleteStyleConfig, MapManagementRestStub
    ):
        def __hash__(self):
            return hash("MapManagementRestTransport.DeleteStyleConfig")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: map_management_service.DeleteStyleConfigRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete style config method over HTTP.

            Args:
                request (~.map_management_service.DeleteStyleConfigRequest):
                    The request object. Request to delete a StyleConfig.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = _BaseMapManagementRestTransport._BaseDeleteStyleConfig._get_http_options()
            request, metadata = self._interceptor.pre_delete_style_config(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseMapManagementRestTransport._BaseDeleteStyleConfig,
                    "_BaseDeleteStyleConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.maps.mapmanagement_v2beta.MapManagementClient.DeleteStyleConfig",
                    extra={
                        "serviceName": "google.maps.mapmanagement.v2beta.MapManagement",
                        "rpcName": "DeleteStyleConfig",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = MapManagementRestTransport._DeleteStyleConfig._get_response(
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

    class _GetMapConfig(
        _BaseMapManagementRestTransport._BaseGetMapConfig, MapManagementRestStub
    ):
        def __hash__(self):
            return hash("MapManagementRestTransport.GetMapConfig")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: map_management_service.GetMapConfigRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> map_management_service.MapConfig:
            r"""Call the get map config method over HTTP.

            Args:
                request (~.map_management_service.GetMapConfigRequest):
                    The request object. Request to get a MapConfig.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.map_management_service.MapConfig:
                    Represents a single map in a Maps API
                client application. The MapConfig is the
                parent resource of MapContextConfigs and
                enables custom styling in SDKs
                (Mobile/Web). A MapConfig can have
                multiple MapContextConfigs, each
                applying styling to specific map
                variants.
                Next ID = 9;

            """

            http_options = (
                _BaseMapManagementRestTransport._BaseGetMapConfig._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_map_config(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseMapManagementRestTransport._BaseGetMapConfig,
                    "_BaseGetMapConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.maps.mapmanagement_v2beta.MapManagementClient.GetMapConfig",
                    extra={
                        "serviceName": "google.maps.mapmanagement.v2beta.MapManagement",
                        "rpcName": "GetMapConfig",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = MapManagementRestTransport._GetMapConfig._get_response(
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
            resp = map_management_service.MapConfig()
            pb_resp = map_management_service.MapConfig.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_map_config(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_map_config_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = map_management_service.MapConfig.to_json(
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
                    "Received response for google.maps.mapmanagement_v2beta.MapManagementClient.get_map_config",
                    extra={
                        "serviceName": "google.maps.mapmanagement.v2beta.MapManagement",
                        "rpcName": "GetMapConfig",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetMapContextConfig(
        _BaseMapManagementRestTransport._BaseGetMapContextConfig, MapManagementRestStub
    ):
        def __hash__(self):
            return hash("MapManagementRestTransport.GetMapContextConfig")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: map_management_service.GetMapContextConfigRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> map_management_service.MapContextConfig:
            r"""Call the get map context config method over HTTP.

            Args:
                request (~.map_management_service.GetMapContextConfigRequest):
                    The request object. Request to get a MapContextConfig.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.map_management_service.MapContextConfig:
                    Encapsulates the styling
                configuration for a map. The
                MapContextConfig associates styling
                components, such as a StyleConfig and
                Datasets, with specific map variants of
                a MapConfig. When the MapConfig is
                loaded in an SDK, the styling and
                dataset information from the
                MapContextConfig are applied to the
                specified map variants.
                Next ID = 10;

            """

            http_options = _BaseMapManagementRestTransport._BaseGetMapContextConfig._get_http_options()
            request, metadata = self._interceptor.pre_get_map_context_config(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseMapManagementRestTransport._BaseGetMapContextConfig,
                    "_BaseGetMapContextConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.maps.mapmanagement_v2beta.MapManagementClient.GetMapContextConfig",
                    extra={
                        "serviceName": "google.maps.mapmanagement.v2beta.MapManagement",
                        "rpcName": "GetMapContextConfig",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = MapManagementRestTransport._GetMapContextConfig._get_response(
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
            resp = map_management_service.MapContextConfig()
            pb_resp = map_management_service.MapContextConfig.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_map_context_config(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_map_context_config_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = map_management_service.MapContextConfig.to_json(
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
                    "Received response for google.maps.mapmanagement_v2beta.MapManagementClient.get_map_context_config",
                    extra={
                        "serviceName": "google.maps.mapmanagement.v2beta.MapManagement",
                        "rpcName": "GetMapContextConfig",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetStyleConfig(
        _BaseMapManagementRestTransport._BaseGetStyleConfig, MapManagementRestStub
    ):
        def __hash__(self):
            return hash("MapManagementRestTransport.GetStyleConfig")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: map_management_service.GetStyleConfigRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> map_management_service.StyleConfig:
            r"""Call the get style config method over HTTP.

            Args:
                request (~.map_management_service.GetStyleConfigRequest):
                    The request object. Request to get a StyleConfig.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.map_management_service.StyleConfig:
                    Represents a single style in a Maps
                API client application. The StyleConfig
                contains the style sheet that defines
                the visual appearance of the map. Next
                ID = 9;

            """

            http_options = (
                _BaseMapManagementRestTransport._BaseGetStyleConfig._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_style_config(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseMapManagementRestTransport._BaseGetStyleConfig,
                    "_BaseGetStyleConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.maps.mapmanagement_v2beta.MapManagementClient.GetStyleConfig",
                    extra={
                        "serviceName": "google.maps.mapmanagement.v2beta.MapManagement",
                        "rpcName": "GetStyleConfig",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = MapManagementRestTransport._GetStyleConfig._get_response(
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
            resp = map_management_service.StyleConfig()
            pb_resp = map_management_service.StyleConfig.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_style_config(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_style_config_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = map_management_service.StyleConfig.to_json(
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
                    "Received response for google.maps.mapmanagement_v2beta.MapManagementClient.get_style_config",
                    extra={
                        "serviceName": "google.maps.mapmanagement.v2beta.MapManagement",
                        "rpcName": "GetStyleConfig",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListMapConfigs(
        _BaseMapManagementRestTransport._BaseListMapConfigs, MapManagementRestStub
    ):
        def __hash__(self):
            return hash("MapManagementRestTransport.ListMapConfigs")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: map_management_service.ListMapConfigsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> map_management_service.ListMapConfigsResponse:
            r"""Call the list map configs method over HTTP.

            Args:
                request (~.map_management_service.ListMapConfigsRequest):
                    The request object. Request to list MapConfigs.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.map_management_service.ListMapConfigsResponse:
                    Response to list MapConfigs.
            """

            http_options = (
                _BaseMapManagementRestTransport._BaseListMapConfigs._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_map_configs(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseMapManagementRestTransport._BaseListMapConfigs,
                    "_BaseListMapConfigs__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.maps.mapmanagement_v2beta.MapManagementClient.ListMapConfigs",
                    extra={
                        "serviceName": "google.maps.mapmanagement.v2beta.MapManagement",
                        "rpcName": "ListMapConfigs",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = MapManagementRestTransport._ListMapConfigs._get_response(
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
            resp = map_management_service.ListMapConfigsResponse()
            pb_resp = map_management_service.ListMapConfigsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_map_configs(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_map_configs_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        map_management_service.ListMapConfigsResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.maps.mapmanagement_v2beta.MapManagementClient.list_map_configs",
                    extra={
                        "serviceName": "google.maps.mapmanagement.v2beta.MapManagement",
                        "rpcName": "ListMapConfigs",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListMapContextConfigs(
        _BaseMapManagementRestTransport._BaseListMapContextConfigs,
        MapManagementRestStub,
    ):
        def __hash__(self):
            return hash("MapManagementRestTransport.ListMapContextConfigs")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: map_management_service.ListMapContextConfigsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> map_management_service.ListMapContextConfigsResponse:
            r"""Call the list map context configs method over HTTP.

            Args:
                request (~.map_management_service.ListMapContextConfigsRequest):
                    The request object. Request to list MapContextConfigs.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.map_management_service.ListMapContextConfigsResponse:
                    Response to list MapContextConfigs.
            """

            http_options = _BaseMapManagementRestTransport._BaseListMapContextConfigs._get_http_options()
            request, metadata = self._interceptor.pre_list_map_context_configs(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseMapManagementRestTransport._BaseListMapContextConfigs,
                    "_BaseListMapContextConfigs__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.maps.mapmanagement_v2beta.MapManagementClient.ListMapContextConfigs",
                    extra={
                        "serviceName": "google.maps.mapmanagement.v2beta.MapManagement",
                        "rpcName": "ListMapContextConfigs",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = MapManagementRestTransport._ListMapContextConfigs._get_response(
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
            resp = map_management_service.ListMapContextConfigsResponse()
            pb_resp = map_management_service.ListMapContextConfigsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_map_context_configs(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_map_context_configs_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        map_management_service.ListMapContextConfigsResponse.to_json(
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
                    "Received response for google.maps.mapmanagement_v2beta.MapManagementClient.list_map_context_configs",
                    extra={
                        "serviceName": "google.maps.mapmanagement.v2beta.MapManagement",
                        "rpcName": "ListMapContextConfigs",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListStyleConfigs(
        _BaseMapManagementRestTransport._BaseListStyleConfigs, MapManagementRestStub
    ):
        def __hash__(self):
            return hash("MapManagementRestTransport.ListStyleConfigs")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: map_management_service.ListStyleConfigsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> map_management_service.ListStyleConfigsResponse:
            r"""Call the list style configs method over HTTP.

            Args:
                request (~.map_management_service.ListStyleConfigsRequest):
                    The request object. Request to list StyleConfigs.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.map_management_service.ListStyleConfigsResponse:
                    Response to list StyleConfigs.
            """

            http_options = _BaseMapManagementRestTransport._BaseListStyleConfigs._get_http_options()
            request, metadata = self._interceptor.pre_list_style_configs(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseMapManagementRestTransport._BaseListStyleConfigs,
                    "_BaseListStyleConfigs__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.maps.mapmanagement_v2beta.MapManagementClient.ListStyleConfigs",
                    extra={
                        "serviceName": "google.maps.mapmanagement.v2beta.MapManagement",
                        "rpcName": "ListStyleConfigs",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = MapManagementRestTransport._ListStyleConfigs._get_response(
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
            resp = map_management_service.ListStyleConfigsResponse()
            pb_resp = map_management_service.ListStyleConfigsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_style_configs(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_style_configs_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        map_management_service.ListStyleConfigsResponse.to_json(
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
                    "Received response for google.maps.mapmanagement_v2beta.MapManagementClient.list_style_configs",
                    extra={
                        "serviceName": "google.maps.mapmanagement.v2beta.MapManagement",
                        "rpcName": "ListStyleConfigs",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateMapConfig(
        _BaseMapManagementRestTransport._BaseUpdateMapConfig, MapManagementRestStub
    ):
        def __hash__(self):
            return hash("MapManagementRestTransport.UpdateMapConfig")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: map_management_service.UpdateMapConfigRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> map_management_service.MapConfig:
            r"""Call the update map config method over HTTP.

            Args:
                request (~.map_management_service.UpdateMapConfigRequest):
                    The request object. Request to update a MapConfig.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.map_management_service.MapConfig:
                    Represents a single map in a Maps API
                client application. The MapConfig is the
                parent resource of MapContextConfigs and
                enables custom styling in SDKs
                (Mobile/Web). A MapConfig can have
                multiple MapContextConfigs, each
                applying styling to specific map
                variants.
                Next ID = 9;

            """

            http_options = (
                _BaseMapManagementRestTransport._BaseUpdateMapConfig._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_map_config(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseMapManagementRestTransport._BaseUpdateMapConfig,
                    "_BaseUpdateMapConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.maps.mapmanagement_v2beta.MapManagementClient.UpdateMapConfig",
                    extra={
                        "serviceName": "google.maps.mapmanagement.v2beta.MapManagement",
                        "rpcName": "UpdateMapConfig",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = MapManagementRestTransport._UpdateMapConfig._get_response(
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
            resp = map_management_service.MapConfig()
            pb_resp = map_management_service.MapConfig.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_map_config(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_map_config_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = map_management_service.MapConfig.to_json(
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
                    "Received response for google.maps.mapmanagement_v2beta.MapManagementClient.update_map_config",
                    extra={
                        "serviceName": "google.maps.mapmanagement.v2beta.MapManagement",
                        "rpcName": "UpdateMapConfig",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateMapContextConfig(
        _BaseMapManagementRestTransport._BaseUpdateMapContextConfig,
        MapManagementRestStub,
    ):
        def __hash__(self):
            return hash("MapManagementRestTransport.UpdateMapContextConfig")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: map_management_service.UpdateMapContextConfigRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> map_management_service.MapContextConfig:
            r"""Call the update map context config method over HTTP.

            Args:
                request (~.map_management_service.UpdateMapContextConfigRequest):
                    The request object. Request to update a MapContextConfig.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.map_management_service.MapContextConfig:
                    Encapsulates the styling
                configuration for a map. The
                MapContextConfig associates styling
                components, such as a StyleConfig and
                Datasets, with specific map variants of
                a MapConfig. When the MapConfig is
                loaded in an SDK, the styling and
                dataset information from the
                MapContextConfig are applied to the
                specified map variants.
                Next ID = 10;

            """

            http_options = _BaseMapManagementRestTransport._BaseUpdateMapContextConfig._get_http_options()
            request, metadata = self._interceptor.pre_update_map_context_config(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseMapManagementRestTransport._BaseUpdateMapContextConfig,
                    "_BaseUpdateMapContextConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.maps.mapmanagement_v2beta.MapManagementClient.UpdateMapContextConfig",
                    extra={
                        "serviceName": "google.maps.mapmanagement.v2beta.MapManagement",
                        "rpcName": "UpdateMapContextConfig",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = MapManagementRestTransport._UpdateMapContextConfig._get_response(
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
            resp = map_management_service.MapContextConfig()
            pb_resp = map_management_service.MapContextConfig.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_map_context_config(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_map_context_config_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = map_management_service.MapContextConfig.to_json(
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
                    "Received response for google.maps.mapmanagement_v2beta.MapManagementClient.update_map_context_config",
                    extra={
                        "serviceName": "google.maps.mapmanagement.v2beta.MapManagement",
                        "rpcName": "UpdateMapContextConfig",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateStyleConfig(
        _BaseMapManagementRestTransport._BaseUpdateStyleConfig, MapManagementRestStub
    ):
        def __hash__(self):
            return hash("MapManagementRestTransport.UpdateStyleConfig")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: map_management_service.UpdateStyleConfigRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> map_management_service.StyleConfig:
            r"""Call the update style config method over HTTP.

            Args:
                request (~.map_management_service.UpdateStyleConfigRequest):
                    The request object. Request to update a StyleConfig.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.map_management_service.StyleConfig:
                    Represents a single style in a Maps
                API client application. The StyleConfig
                contains the style sheet that defines
                the visual appearance of the map. Next
                ID = 9;

            """

            http_options = _BaseMapManagementRestTransport._BaseUpdateStyleConfig._get_http_options()
            request, metadata = self._interceptor.pre_update_style_config(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseMapManagementRestTransport._BaseUpdateStyleConfig,
                    "_BaseUpdateStyleConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.maps.mapmanagement_v2beta.MapManagementClient.UpdateStyleConfig",
                    extra={
                        "serviceName": "google.maps.mapmanagement.v2beta.MapManagement",
                        "rpcName": "UpdateStyleConfig",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = MapManagementRestTransport._UpdateStyleConfig._get_response(
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
            resp = map_management_service.StyleConfig()
            pb_resp = map_management_service.StyleConfig.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_style_config(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_style_config_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = map_management_service.StyleConfig.to_json(
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
                    "Received response for google.maps.mapmanagement_v2beta.MapManagementClient.update_style_config",
                    extra={
                        "serviceName": "google.maps.mapmanagement.v2beta.MapManagement",
                        "rpcName": "UpdateStyleConfig",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def create_map_config(
        self,
    ) -> Callable[
        [map_management_service.CreateMapConfigRequest],
        map_management_service.MapConfig,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateMapConfig(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_map_context_config(
        self,
    ) -> Callable[
        [map_management_service.CreateMapContextConfigRequest],
        map_management_service.MapContextConfig,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateMapContextConfig(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def create_style_config(
        self,
    ) -> Callable[
        [map_management_service.CreateStyleConfigRequest],
        map_management_service.StyleConfig,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateStyleConfig(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_map_config(
        self,
    ) -> Callable[[map_management_service.DeleteMapConfigRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteMapConfig(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_map_context_config(
        self,
    ) -> Callable[
        [map_management_service.DeleteMapContextConfigRequest], empty_pb2.Empty
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteMapContextConfig(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def delete_style_config(
        self,
    ) -> Callable[[map_management_service.DeleteStyleConfigRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteStyleConfig(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_map_config(
        self,
    ) -> Callable[
        [map_management_service.GetMapConfigRequest], map_management_service.MapConfig
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetMapConfig(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_map_context_config(
        self,
    ) -> Callable[
        [map_management_service.GetMapContextConfigRequest],
        map_management_service.MapContextConfig,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetMapContextConfig(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_style_config(
        self,
    ) -> Callable[
        [map_management_service.GetStyleConfigRequest],
        map_management_service.StyleConfig,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetStyleConfig(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_map_configs(
        self,
    ) -> Callable[
        [map_management_service.ListMapConfigsRequest],
        map_management_service.ListMapConfigsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListMapConfigs(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_map_context_configs(
        self,
    ) -> Callable[
        [map_management_service.ListMapContextConfigsRequest],
        map_management_service.ListMapContextConfigsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListMapContextConfigs(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_style_configs(
        self,
    ) -> Callable[
        [map_management_service.ListStyleConfigsRequest],
        map_management_service.ListStyleConfigsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListStyleConfigs(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_map_config(
        self,
    ) -> Callable[
        [map_management_service.UpdateMapConfigRequest],
        map_management_service.MapConfig,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateMapConfig(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_map_context_config(
        self,
    ) -> Callable[
        [map_management_service.UpdateMapContextConfigRequest],
        map_management_service.MapContextConfig,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateMapContextConfig(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def update_style_config(
        self,
    ) -> Callable[
        [map_management_service.UpdateStyleConfigRequest],
        map_management_service.StyleConfig,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateStyleConfig(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def kind(self) -> str:
        return "rest"

    def close(self):
        self._session.close()


__all__ = ("MapManagementRestTransport",)
