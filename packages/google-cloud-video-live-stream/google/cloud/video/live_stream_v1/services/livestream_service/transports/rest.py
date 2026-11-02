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
from google.cloud.location import locations_pb2  # type: ignore
from google.longrunning import operations_pb2  # type: ignore
from google.protobuf import json_format
from requests import __version__ as requests_version

from google.cloud.video.live_stream_v1._compat import transcode_request
from google.cloud.video.live_stream_v1.types import resources, service

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseLivestreamServiceRestTransport

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


class LivestreamServiceRestInterceptor:
    """Interceptor for LivestreamService.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the LivestreamServiceRestTransport.

    .. code-block:: python
        class MyCustomLivestreamServiceInterceptor(LivestreamServiceRestInterceptor):
            def pre_create_asset(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_asset(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_channel(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_channel(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_clip(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_clip(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_dvr_session(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_dvr_session(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_event(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_event(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_input(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_input(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_asset(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_asset(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_channel(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_channel(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_clip(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_clip(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_dvr_session(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_dvr_session(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_event(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_delete_input(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_input(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_asset(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_asset(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_channel(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_channel(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_clip(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_clip(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_dvr_session(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_dvr_session(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_event(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_event(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_input(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_input(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_pool(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_pool(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_assets(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_assets(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_channels(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_channels(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_clips(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_clips(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_dvr_sessions(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_dvr_sessions(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_events(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_events(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_inputs(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_inputs(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_preview_input(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_preview_input(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_start_channel(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_start_channel(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_start_distribution(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_start_distribution(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_stop_channel(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_stop_channel(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_stop_distribution(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_stop_distribution(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_channel(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_channel(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_dvr_session(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_dvr_session(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_input(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_input(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_pool(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_pool(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = LivestreamServiceRestTransport(interceptor=MyCustomLivestreamServiceInterceptor())
        client = LivestreamServiceClient(transport=transport)


    """

    def pre_create_asset(
        self,
        request: service.CreateAssetRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.CreateAssetRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for create_asset

        Override in a subclass to manipulate the request or metadata
        before they are sent to the LivestreamService server.
        """
        return request, metadata

    def post_create_asset(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_asset

        DEPRECATED. Please use the `post_create_asset_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the LivestreamService server but before
        it is returned to user code. This `post_create_asset` interceptor runs
        before the `post_create_asset_with_metadata` interceptor.
        """
        return response

    def post_create_asset_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_asset

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the LivestreamService server but before it is returned to user code.

        We recommend only using this `post_create_asset_with_metadata`
        interceptor in new development instead of the `post_create_asset` interceptor.
        When both interceptors are used, this `post_create_asset_with_metadata` interceptor runs after the
        `post_create_asset` interceptor. The (possibly modified) response returned by
        `post_create_asset` will be passed to
        `post_create_asset_with_metadata`.
        """
        return response, metadata

    def pre_create_channel(
        self,
        request: service.CreateChannelRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.CreateChannelRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for create_channel

        Override in a subclass to manipulate the request or metadata
        before they are sent to the LivestreamService server.
        """
        return request, metadata

    def post_create_channel(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_channel

        DEPRECATED. Please use the `post_create_channel_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the LivestreamService server but before
        it is returned to user code. This `post_create_channel` interceptor runs
        before the `post_create_channel_with_metadata` interceptor.
        """
        return response

    def post_create_channel_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_channel

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the LivestreamService server but before it is returned to user code.

        We recommend only using this `post_create_channel_with_metadata`
        interceptor in new development instead of the `post_create_channel` interceptor.
        When both interceptors are used, this `post_create_channel_with_metadata` interceptor runs after the
        `post_create_channel` interceptor. The (possibly modified) response returned by
        `post_create_channel` will be passed to
        `post_create_channel_with_metadata`.
        """
        return response, metadata

    def pre_create_clip(
        self,
        request: service.CreateClipRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.CreateClipRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for create_clip

        Override in a subclass to manipulate the request or metadata
        before they are sent to the LivestreamService server.
        """
        return request, metadata

    def post_create_clip(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_clip

        DEPRECATED. Please use the `post_create_clip_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the LivestreamService server but before
        it is returned to user code. This `post_create_clip` interceptor runs
        before the `post_create_clip_with_metadata` interceptor.
        """
        return response

    def post_create_clip_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_clip

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the LivestreamService server but before it is returned to user code.

        We recommend only using this `post_create_clip_with_metadata`
        interceptor in new development instead of the `post_create_clip` interceptor.
        When both interceptors are used, this `post_create_clip_with_metadata` interceptor runs after the
        `post_create_clip` interceptor. The (possibly modified) response returned by
        `post_create_clip` will be passed to
        `post_create_clip_with_metadata`.
        """
        return response, metadata

    def pre_create_dvr_session(
        self,
        request: service.CreateDvrSessionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.CreateDvrSessionRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_dvr_session

        Override in a subclass to manipulate the request or metadata
        before they are sent to the LivestreamService server.
        """
        return request, metadata

    def post_create_dvr_session(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_dvr_session

        DEPRECATED. Please use the `post_create_dvr_session_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the LivestreamService server but before
        it is returned to user code. This `post_create_dvr_session` interceptor runs
        before the `post_create_dvr_session_with_metadata` interceptor.
        """
        return response

    def post_create_dvr_session_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_dvr_session

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the LivestreamService server but before it is returned to user code.

        We recommend only using this `post_create_dvr_session_with_metadata`
        interceptor in new development instead of the `post_create_dvr_session` interceptor.
        When both interceptors are used, this `post_create_dvr_session_with_metadata` interceptor runs after the
        `post_create_dvr_session` interceptor. The (possibly modified) response returned by
        `post_create_dvr_session` will be passed to
        `post_create_dvr_session_with_metadata`.
        """
        return response, metadata

    def pre_create_event(
        self,
        request: service.CreateEventRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.CreateEventRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for create_event

        Override in a subclass to manipulate the request or metadata
        before they are sent to the LivestreamService server.
        """
        return request, metadata

    def post_create_event(self, response: resources.Event) -> resources.Event:
        """Post-rpc interceptor for create_event

        DEPRECATED. Please use the `post_create_event_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the LivestreamService server but before
        it is returned to user code. This `post_create_event` interceptor runs
        before the `post_create_event_with_metadata` interceptor.
        """
        return response

    def post_create_event_with_metadata(
        self,
        response: resources.Event,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[resources.Event, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_event

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the LivestreamService server but before it is returned to user code.

        We recommend only using this `post_create_event_with_metadata`
        interceptor in new development instead of the `post_create_event` interceptor.
        When both interceptors are used, this `post_create_event_with_metadata` interceptor runs after the
        `post_create_event` interceptor. The (possibly modified) response returned by
        `post_create_event` will be passed to
        `post_create_event_with_metadata`.
        """
        return response, metadata

    def pre_create_input(
        self,
        request: service.CreateInputRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.CreateInputRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for create_input

        Override in a subclass to manipulate the request or metadata
        before they are sent to the LivestreamService server.
        """
        return request, metadata

    def post_create_input(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_input

        DEPRECATED. Please use the `post_create_input_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the LivestreamService server but before
        it is returned to user code. This `post_create_input` interceptor runs
        before the `post_create_input_with_metadata` interceptor.
        """
        return response

    def post_create_input_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_input

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the LivestreamService server but before it is returned to user code.

        We recommend only using this `post_create_input_with_metadata`
        interceptor in new development instead of the `post_create_input` interceptor.
        When both interceptors are used, this `post_create_input_with_metadata` interceptor runs after the
        `post_create_input` interceptor. The (possibly modified) response returned by
        `post_create_input` will be passed to
        `post_create_input_with_metadata`.
        """
        return response, metadata

    def pre_delete_asset(
        self,
        request: service.DeleteAssetRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.DeleteAssetRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for delete_asset

        Override in a subclass to manipulate the request or metadata
        before they are sent to the LivestreamService server.
        """
        return request, metadata

    def post_delete_asset(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_asset

        DEPRECATED. Please use the `post_delete_asset_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the LivestreamService server but before
        it is returned to user code. This `post_delete_asset` interceptor runs
        before the `post_delete_asset_with_metadata` interceptor.
        """
        return response

    def post_delete_asset_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_asset

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the LivestreamService server but before it is returned to user code.

        We recommend only using this `post_delete_asset_with_metadata`
        interceptor in new development instead of the `post_delete_asset` interceptor.
        When both interceptors are used, this `post_delete_asset_with_metadata` interceptor runs after the
        `post_delete_asset` interceptor. The (possibly modified) response returned by
        `post_delete_asset` will be passed to
        `post_delete_asset_with_metadata`.
        """
        return response, metadata

    def pre_delete_channel(
        self,
        request: service.DeleteChannelRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.DeleteChannelRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for delete_channel

        Override in a subclass to manipulate the request or metadata
        before they are sent to the LivestreamService server.
        """
        return request, metadata

    def post_delete_channel(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_channel

        DEPRECATED. Please use the `post_delete_channel_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the LivestreamService server but before
        it is returned to user code. This `post_delete_channel` interceptor runs
        before the `post_delete_channel_with_metadata` interceptor.
        """
        return response

    def post_delete_channel_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_channel

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the LivestreamService server but before it is returned to user code.

        We recommend only using this `post_delete_channel_with_metadata`
        interceptor in new development instead of the `post_delete_channel` interceptor.
        When both interceptors are used, this `post_delete_channel_with_metadata` interceptor runs after the
        `post_delete_channel` interceptor. The (possibly modified) response returned by
        `post_delete_channel` will be passed to
        `post_delete_channel_with_metadata`.
        """
        return response, metadata

    def pre_delete_clip(
        self,
        request: service.DeleteClipRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.DeleteClipRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for delete_clip

        Override in a subclass to manipulate the request or metadata
        before they are sent to the LivestreamService server.
        """
        return request, metadata

    def post_delete_clip(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_clip

        DEPRECATED. Please use the `post_delete_clip_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the LivestreamService server but before
        it is returned to user code. This `post_delete_clip` interceptor runs
        before the `post_delete_clip_with_metadata` interceptor.
        """
        return response

    def post_delete_clip_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_clip

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the LivestreamService server but before it is returned to user code.

        We recommend only using this `post_delete_clip_with_metadata`
        interceptor in new development instead of the `post_delete_clip` interceptor.
        When both interceptors are used, this `post_delete_clip_with_metadata` interceptor runs after the
        `post_delete_clip` interceptor. The (possibly modified) response returned by
        `post_delete_clip` will be passed to
        `post_delete_clip_with_metadata`.
        """
        return response, metadata

    def pre_delete_dvr_session(
        self,
        request: service.DeleteDvrSessionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.DeleteDvrSessionRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_dvr_session

        Override in a subclass to manipulate the request or metadata
        before they are sent to the LivestreamService server.
        """
        return request, metadata

    def post_delete_dvr_session(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_dvr_session

        DEPRECATED. Please use the `post_delete_dvr_session_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the LivestreamService server but before
        it is returned to user code. This `post_delete_dvr_session` interceptor runs
        before the `post_delete_dvr_session_with_metadata` interceptor.
        """
        return response

    def post_delete_dvr_session_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_dvr_session

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the LivestreamService server but before it is returned to user code.

        We recommend only using this `post_delete_dvr_session_with_metadata`
        interceptor in new development instead of the `post_delete_dvr_session` interceptor.
        When both interceptors are used, this `post_delete_dvr_session_with_metadata` interceptor runs after the
        `post_delete_dvr_session` interceptor. The (possibly modified) response returned by
        `post_delete_dvr_session` will be passed to
        `post_delete_dvr_session_with_metadata`.
        """
        return response, metadata

    def pre_delete_event(
        self,
        request: service.DeleteEventRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.DeleteEventRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for delete_event

        Override in a subclass to manipulate the request or metadata
        before they are sent to the LivestreamService server.
        """
        return request, metadata

    def pre_delete_input(
        self,
        request: service.DeleteInputRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.DeleteInputRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for delete_input

        Override in a subclass to manipulate the request or metadata
        before they are sent to the LivestreamService server.
        """
        return request, metadata

    def post_delete_input(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_input

        DEPRECATED. Please use the `post_delete_input_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the LivestreamService server but before
        it is returned to user code. This `post_delete_input` interceptor runs
        before the `post_delete_input_with_metadata` interceptor.
        """
        return response

    def post_delete_input_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_input

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the LivestreamService server but before it is returned to user code.

        We recommend only using this `post_delete_input_with_metadata`
        interceptor in new development instead of the `post_delete_input` interceptor.
        When both interceptors are used, this `post_delete_input_with_metadata` interceptor runs after the
        `post_delete_input` interceptor. The (possibly modified) response returned by
        `post_delete_input` will be passed to
        `post_delete_input_with_metadata`.
        """
        return response, metadata

    def pre_get_asset(
        self,
        request: service.GetAssetRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.GetAssetRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_asset

        Override in a subclass to manipulate the request or metadata
        before they are sent to the LivestreamService server.
        """
        return request, metadata

    def post_get_asset(self, response: resources.Asset) -> resources.Asset:
        """Post-rpc interceptor for get_asset

        DEPRECATED. Please use the `post_get_asset_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the LivestreamService server but before
        it is returned to user code. This `post_get_asset` interceptor runs
        before the `post_get_asset_with_metadata` interceptor.
        """
        return response

    def post_get_asset_with_metadata(
        self,
        response: resources.Asset,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[resources.Asset, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_asset

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the LivestreamService server but before it is returned to user code.

        We recommend only using this `post_get_asset_with_metadata`
        interceptor in new development instead of the `post_get_asset` interceptor.
        When both interceptors are used, this `post_get_asset_with_metadata` interceptor runs after the
        `post_get_asset` interceptor. The (possibly modified) response returned by
        `post_get_asset` will be passed to
        `post_get_asset_with_metadata`.
        """
        return response, metadata

    def pre_get_channel(
        self,
        request: service.GetChannelRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.GetChannelRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_channel

        Override in a subclass to manipulate the request or metadata
        before they are sent to the LivestreamService server.
        """
        return request, metadata

    def post_get_channel(self, response: resources.Channel) -> resources.Channel:
        """Post-rpc interceptor for get_channel

        DEPRECATED. Please use the `post_get_channel_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the LivestreamService server but before
        it is returned to user code. This `post_get_channel` interceptor runs
        before the `post_get_channel_with_metadata` interceptor.
        """
        return response

    def post_get_channel_with_metadata(
        self,
        response: resources.Channel,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[resources.Channel, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_channel

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the LivestreamService server but before it is returned to user code.

        We recommend only using this `post_get_channel_with_metadata`
        interceptor in new development instead of the `post_get_channel` interceptor.
        When both interceptors are used, this `post_get_channel_with_metadata` interceptor runs after the
        `post_get_channel` interceptor. The (possibly modified) response returned by
        `post_get_channel` will be passed to
        `post_get_channel_with_metadata`.
        """
        return response, metadata

    def pre_get_clip(
        self,
        request: service.GetClipRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.GetClipRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_clip

        Override in a subclass to manipulate the request or metadata
        before they are sent to the LivestreamService server.
        """
        return request, metadata

    def post_get_clip(self, response: resources.Clip) -> resources.Clip:
        """Post-rpc interceptor for get_clip

        DEPRECATED. Please use the `post_get_clip_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the LivestreamService server but before
        it is returned to user code. This `post_get_clip` interceptor runs
        before the `post_get_clip_with_metadata` interceptor.
        """
        return response

    def post_get_clip_with_metadata(
        self,
        response: resources.Clip,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[resources.Clip, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_clip

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the LivestreamService server but before it is returned to user code.

        We recommend only using this `post_get_clip_with_metadata`
        interceptor in new development instead of the `post_get_clip` interceptor.
        When both interceptors are used, this `post_get_clip_with_metadata` interceptor runs after the
        `post_get_clip` interceptor. The (possibly modified) response returned by
        `post_get_clip` will be passed to
        `post_get_clip_with_metadata`.
        """
        return response, metadata

    def pre_get_dvr_session(
        self,
        request: service.GetDvrSessionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.GetDvrSessionRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_dvr_session

        Override in a subclass to manipulate the request or metadata
        before they are sent to the LivestreamService server.
        """
        return request, metadata

    def post_get_dvr_session(
        self, response: resources.DvrSession
    ) -> resources.DvrSession:
        """Post-rpc interceptor for get_dvr_session

        DEPRECATED. Please use the `post_get_dvr_session_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the LivestreamService server but before
        it is returned to user code. This `post_get_dvr_session` interceptor runs
        before the `post_get_dvr_session_with_metadata` interceptor.
        """
        return response

    def post_get_dvr_session_with_metadata(
        self,
        response: resources.DvrSession,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[resources.DvrSession, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_dvr_session

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the LivestreamService server but before it is returned to user code.

        We recommend only using this `post_get_dvr_session_with_metadata`
        interceptor in new development instead of the `post_get_dvr_session` interceptor.
        When both interceptors are used, this `post_get_dvr_session_with_metadata` interceptor runs after the
        `post_get_dvr_session` interceptor. The (possibly modified) response returned by
        `post_get_dvr_session` will be passed to
        `post_get_dvr_session_with_metadata`.
        """
        return response, metadata

    def pre_get_event(
        self,
        request: service.GetEventRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.GetEventRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_event

        Override in a subclass to manipulate the request or metadata
        before they are sent to the LivestreamService server.
        """
        return request, metadata

    def post_get_event(self, response: resources.Event) -> resources.Event:
        """Post-rpc interceptor for get_event

        DEPRECATED. Please use the `post_get_event_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the LivestreamService server but before
        it is returned to user code. This `post_get_event` interceptor runs
        before the `post_get_event_with_metadata` interceptor.
        """
        return response

    def post_get_event_with_metadata(
        self,
        response: resources.Event,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[resources.Event, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_event

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the LivestreamService server but before it is returned to user code.

        We recommend only using this `post_get_event_with_metadata`
        interceptor in new development instead of the `post_get_event` interceptor.
        When both interceptors are used, this `post_get_event_with_metadata` interceptor runs after the
        `post_get_event` interceptor. The (possibly modified) response returned by
        `post_get_event` will be passed to
        `post_get_event_with_metadata`.
        """
        return response, metadata

    def pre_get_input(
        self,
        request: service.GetInputRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.GetInputRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_input

        Override in a subclass to manipulate the request or metadata
        before they are sent to the LivestreamService server.
        """
        return request, metadata

    def post_get_input(self, response: resources.Input) -> resources.Input:
        """Post-rpc interceptor for get_input

        DEPRECATED. Please use the `post_get_input_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the LivestreamService server but before
        it is returned to user code. This `post_get_input` interceptor runs
        before the `post_get_input_with_metadata` interceptor.
        """
        return response

    def post_get_input_with_metadata(
        self,
        response: resources.Input,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[resources.Input, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_input

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the LivestreamService server but before it is returned to user code.

        We recommend only using this `post_get_input_with_metadata`
        interceptor in new development instead of the `post_get_input` interceptor.
        When both interceptors are used, this `post_get_input_with_metadata` interceptor runs after the
        `post_get_input` interceptor. The (possibly modified) response returned by
        `post_get_input` will be passed to
        `post_get_input_with_metadata`.
        """
        return response, metadata

    def pre_get_pool(
        self,
        request: service.GetPoolRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.GetPoolRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_pool

        Override in a subclass to manipulate the request or metadata
        before they are sent to the LivestreamService server.
        """
        return request, metadata

    def post_get_pool(self, response: resources.Pool) -> resources.Pool:
        """Post-rpc interceptor for get_pool

        DEPRECATED. Please use the `post_get_pool_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the LivestreamService server but before
        it is returned to user code. This `post_get_pool` interceptor runs
        before the `post_get_pool_with_metadata` interceptor.
        """
        return response

    def post_get_pool_with_metadata(
        self,
        response: resources.Pool,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[resources.Pool, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_pool

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the LivestreamService server but before it is returned to user code.

        We recommend only using this `post_get_pool_with_metadata`
        interceptor in new development instead of the `post_get_pool` interceptor.
        When both interceptors are used, this `post_get_pool_with_metadata` interceptor runs after the
        `post_get_pool` interceptor. The (possibly modified) response returned by
        `post_get_pool` will be passed to
        `post_get_pool_with_metadata`.
        """
        return response, metadata

    def pre_list_assets(
        self,
        request: service.ListAssetsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.ListAssetsRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for list_assets

        Override in a subclass to manipulate the request or metadata
        before they are sent to the LivestreamService server.
        """
        return request, metadata

    def post_list_assets(
        self, response: service.ListAssetsResponse
    ) -> service.ListAssetsResponse:
        """Post-rpc interceptor for list_assets

        DEPRECATED. Please use the `post_list_assets_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the LivestreamService server but before
        it is returned to user code. This `post_list_assets` interceptor runs
        before the `post_list_assets_with_metadata` interceptor.
        """
        return response

    def post_list_assets_with_metadata(
        self,
        response: service.ListAssetsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.ListAssetsResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for list_assets

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the LivestreamService server but before it is returned to user code.

        We recommend only using this `post_list_assets_with_metadata`
        interceptor in new development instead of the `post_list_assets` interceptor.
        When both interceptors are used, this `post_list_assets_with_metadata` interceptor runs after the
        `post_list_assets` interceptor. The (possibly modified) response returned by
        `post_list_assets` will be passed to
        `post_list_assets_with_metadata`.
        """
        return response, metadata

    def pre_list_channels(
        self,
        request: service.ListChannelsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.ListChannelsRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for list_channels

        Override in a subclass to manipulate the request or metadata
        before they are sent to the LivestreamService server.
        """
        return request, metadata

    def post_list_channels(
        self, response: service.ListChannelsResponse
    ) -> service.ListChannelsResponse:
        """Post-rpc interceptor for list_channels

        DEPRECATED. Please use the `post_list_channels_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the LivestreamService server but before
        it is returned to user code. This `post_list_channels` interceptor runs
        before the `post_list_channels_with_metadata` interceptor.
        """
        return response

    def post_list_channels_with_metadata(
        self,
        response: service.ListChannelsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.ListChannelsResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for list_channels

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the LivestreamService server but before it is returned to user code.

        We recommend only using this `post_list_channels_with_metadata`
        interceptor in new development instead of the `post_list_channels` interceptor.
        When both interceptors are used, this `post_list_channels_with_metadata` interceptor runs after the
        `post_list_channels` interceptor. The (possibly modified) response returned by
        `post_list_channels` will be passed to
        `post_list_channels_with_metadata`.
        """
        return response, metadata

    def pre_list_clips(
        self,
        request: service.ListClipsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.ListClipsRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for list_clips

        Override in a subclass to manipulate the request or metadata
        before they are sent to the LivestreamService server.
        """
        return request, metadata

    def post_list_clips(
        self, response: service.ListClipsResponse
    ) -> service.ListClipsResponse:
        """Post-rpc interceptor for list_clips

        DEPRECATED. Please use the `post_list_clips_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the LivestreamService server but before
        it is returned to user code. This `post_list_clips` interceptor runs
        before the `post_list_clips_with_metadata` interceptor.
        """
        return response

    def post_list_clips_with_metadata(
        self,
        response: service.ListClipsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.ListClipsResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for list_clips

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the LivestreamService server but before it is returned to user code.

        We recommend only using this `post_list_clips_with_metadata`
        interceptor in new development instead of the `post_list_clips` interceptor.
        When both interceptors are used, this `post_list_clips_with_metadata` interceptor runs after the
        `post_list_clips` interceptor. The (possibly modified) response returned by
        `post_list_clips` will be passed to
        `post_list_clips_with_metadata`.
        """
        return response, metadata

    def pre_list_dvr_sessions(
        self,
        request: service.ListDvrSessionsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.ListDvrSessionsRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for list_dvr_sessions

        Override in a subclass to manipulate the request or metadata
        before they are sent to the LivestreamService server.
        """
        return request, metadata

    def post_list_dvr_sessions(
        self, response: service.ListDvrSessionsResponse
    ) -> service.ListDvrSessionsResponse:
        """Post-rpc interceptor for list_dvr_sessions

        DEPRECATED. Please use the `post_list_dvr_sessions_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the LivestreamService server but before
        it is returned to user code. This `post_list_dvr_sessions` interceptor runs
        before the `post_list_dvr_sessions_with_metadata` interceptor.
        """
        return response

    def post_list_dvr_sessions_with_metadata(
        self,
        response: service.ListDvrSessionsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.ListDvrSessionsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_dvr_sessions

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the LivestreamService server but before it is returned to user code.

        We recommend only using this `post_list_dvr_sessions_with_metadata`
        interceptor in new development instead of the `post_list_dvr_sessions` interceptor.
        When both interceptors are used, this `post_list_dvr_sessions_with_metadata` interceptor runs after the
        `post_list_dvr_sessions` interceptor. The (possibly modified) response returned by
        `post_list_dvr_sessions` will be passed to
        `post_list_dvr_sessions_with_metadata`.
        """
        return response, metadata

    def pre_list_events(
        self,
        request: service.ListEventsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.ListEventsRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for list_events

        Override in a subclass to manipulate the request or metadata
        before they are sent to the LivestreamService server.
        """
        return request, metadata

    def post_list_events(
        self, response: service.ListEventsResponse
    ) -> service.ListEventsResponse:
        """Post-rpc interceptor for list_events

        DEPRECATED. Please use the `post_list_events_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the LivestreamService server but before
        it is returned to user code. This `post_list_events` interceptor runs
        before the `post_list_events_with_metadata` interceptor.
        """
        return response

    def post_list_events_with_metadata(
        self,
        response: service.ListEventsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.ListEventsResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for list_events

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the LivestreamService server but before it is returned to user code.

        We recommend only using this `post_list_events_with_metadata`
        interceptor in new development instead of the `post_list_events` interceptor.
        When both interceptors are used, this `post_list_events_with_metadata` interceptor runs after the
        `post_list_events` interceptor. The (possibly modified) response returned by
        `post_list_events` will be passed to
        `post_list_events_with_metadata`.
        """
        return response, metadata

    def pre_list_inputs(
        self,
        request: service.ListInputsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.ListInputsRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for list_inputs

        Override in a subclass to manipulate the request or metadata
        before they are sent to the LivestreamService server.
        """
        return request, metadata

    def post_list_inputs(
        self, response: service.ListInputsResponse
    ) -> service.ListInputsResponse:
        """Post-rpc interceptor for list_inputs

        DEPRECATED. Please use the `post_list_inputs_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the LivestreamService server but before
        it is returned to user code. This `post_list_inputs` interceptor runs
        before the `post_list_inputs_with_metadata` interceptor.
        """
        return response

    def post_list_inputs_with_metadata(
        self,
        response: service.ListInputsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.ListInputsResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for list_inputs

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the LivestreamService server but before it is returned to user code.

        We recommend only using this `post_list_inputs_with_metadata`
        interceptor in new development instead of the `post_list_inputs` interceptor.
        When both interceptors are used, this `post_list_inputs_with_metadata` interceptor runs after the
        `post_list_inputs` interceptor. The (possibly modified) response returned by
        `post_list_inputs` will be passed to
        `post_list_inputs_with_metadata`.
        """
        return response, metadata

    def pre_preview_input(
        self,
        request: service.PreviewInputRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.PreviewInputRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for preview_input

        Override in a subclass to manipulate the request or metadata
        before they are sent to the LivestreamService server.
        """
        return request, metadata

    def post_preview_input(
        self, response: service.PreviewInputResponse
    ) -> service.PreviewInputResponse:
        """Post-rpc interceptor for preview_input

        DEPRECATED. Please use the `post_preview_input_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the LivestreamService server but before
        it is returned to user code. This `post_preview_input` interceptor runs
        before the `post_preview_input_with_metadata` interceptor.
        """
        return response

    def post_preview_input_with_metadata(
        self,
        response: service.PreviewInputResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.PreviewInputResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for preview_input

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the LivestreamService server but before it is returned to user code.

        We recommend only using this `post_preview_input_with_metadata`
        interceptor in new development instead of the `post_preview_input` interceptor.
        When both interceptors are used, this `post_preview_input_with_metadata` interceptor runs after the
        `post_preview_input` interceptor. The (possibly modified) response returned by
        `post_preview_input` will be passed to
        `post_preview_input_with_metadata`.
        """
        return response, metadata

    def pre_start_channel(
        self,
        request: service.StartChannelRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.StartChannelRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for start_channel

        Override in a subclass to manipulate the request or metadata
        before they are sent to the LivestreamService server.
        """
        return request, metadata

    def post_start_channel(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for start_channel

        DEPRECATED. Please use the `post_start_channel_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the LivestreamService server but before
        it is returned to user code. This `post_start_channel` interceptor runs
        before the `post_start_channel_with_metadata` interceptor.
        """
        return response

    def post_start_channel_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for start_channel

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the LivestreamService server but before it is returned to user code.

        We recommend only using this `post_start_channel_with_metadata`
        interceptor in new development instead of the `post_start_channel` interceptor.
        When both interceptors are used, this `post_start_channel_with_metadata` interceptor runs after the
        `post_start_channel` interceptor. The (possibly modified) response returned by
        `post_start_channel` will be passed to
        `post_start_channel_with_metadata`.
        """
        return response, metadata

    def pre_start_distribution(
        self,
        request: service.StartDistributionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.StartDistributionRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for start_distribution

        Override in a subclass to manipulate the request or metadata
        before they are sent to the LivestreamService server.
        """
        return request, metadata

    def post_start_distribution(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for start_distribution

        DEPRECATED. Please use the `post_start_distribution_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the LivestreamService server but before
        it is returned to user code. This `post_start_distribution` interceptor runs
        before the `post_start_distribution_with_metadata` interceptor.
        """
        return response

    def post_start_distribution_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for start_distribution

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the LivestreamService server but before it is returned to user code.

        We recommend only using this `post_start_distribution_with_metadata`
        interceptor in new development instead of the `post_start_distribution` interceptor.
        When both interceptors are used, this `post_start_distribution_with_metadata` interceptor runs after the
        `post_start_distribution` interceptor. The (possibly modified) response returned by
        `post_start_distribution` will be passed to
        `post_start_distribution_with_metadata`.
        """
        return response, metadata

    def pre_stop_channel(
        self,
        request: service.StopChannelRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.StopChannelRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for stop_channel

        Override in a subclass to manipulate the request or metadata
        before they are sent to the LivestreamService server.
        """
        return request, metadata

    def post_stop_channel(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for stop_channel

        DEPRECATED. Please use the `post_stop_channel_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the LivestreamService server but before
        it is returned to user code. This `post_stop_channel` interceptor runs
        before the `post_stop_channel_with_metadata` interceptor.
        """
        return response

    def post_stop_channel_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for stop_channel

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the LivestreamService server but before it is returned to user code.

        We recommend only using this `post_stop_channel_with_metadata`
        interceptor in new development instead of the `post_stop_channel` interceptor.
        When both interceptors are used, this `post_stop_channel_with_metadata` interceptor runs after the
        `post_stop_channel` interceptor. The (possibly modified) response returned by
        `post_stop_channel` will be passed to
        `post_stop_channel_with_metadata`.
        """
        return response, metadata

    def pre_stop_distribution(
        self,
        request: service.StopDistributionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.StopDistributionRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for stop_distribution

        Override in a subclass to manipulate the request or metadata
        before they are sent to the LivestreamService server.
        """
        return request, metadata

    def post_stop_distribution(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for stop_distribution

        DEPRECATED. Please use the `post_stop_distribution_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the LivestreamService server but before
        it is returned to user code. This `post_stop_distribution` interceptor runs
        before the `post_stop_distribution_with_metadata` interceptor.
        """
        return response

    def post_stop_distribution_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for stop_distribution

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the LivestreamService server but before it is returned to user code.

        We recommend only using this `post_stop_distribution_with_metadata`
        interceptor in new development instead of the `post_stop_distribution` interceptor.
        When both interceptors are used, this `post_stop_distribution_with_metadata` interceptor runs after the
        `post_stop_distribution` interceptor. The (possibly modified) response returned by
        `post_stop_distribution` will be passed to
        `post_stop_distribution_with_metadata`.
        """
        return response, metadata

    def pre_update_channel(
        self,
        request: service.UpdateChannelRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.UpdateChannelRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for update_channel

        Override in a subclass to manipulate the request or metadata
        before they are sent to the LivestreamService server.
        """
        return request, metadata

    def post_update_channel(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_channel

        DEPRECATED. Please use the `post_update_channel_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the LivestreamService server but before
        it is returned to user code. This `post_update_channel` interceptor runs
        before the `post_update_channel_with_metadata` interceptor.
        """
        return response

    def post_update_channel_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_channel

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the LivestreamService server but before it is returned to user code.

        We recommend only using this `post_update_channel_with_metadata`
        interceptor in new development instead of the `post_update_channel` interceptor.
        When both interceptors are used, this `post_update_channel_with_metadata` interceptor runs after the
        `post_update_channel` interceptor. The (possibly modified) response returned by
        `post_update_channel` will be passed to
        `post_update_channel_with_metadata`.
        """
        return response, metadata

    def pre_update_dvr_session(
        self,
        request: service.UpdateDvrSessionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.UpdateDvrSessionRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_dvr_session

        Override in a subclass to manipulate the request or metadata
        before they are sent to the LivestreamService server.
        """
        return request, metadata

    def post_update_dvr_session(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_dvr_session

        DEPRECATED. Please use the `post_update_dvr_session_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the LivestreamService server but before
        it is returned to user code. This `post_update_dvr_session` interceptor runs
        before the `post_update_dvr_session_with_metadata` interceptor.
        """
        return response

    def post_update_dvr_session_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_dvr_session

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the LivestreamService server but before it is returned to user code.

        We recommend only using this `post_update_dvr_session_with_metadata`
        interceptor in new development instead of the `post_update_dvr_session` interceptor.
        When both interceptors are used, this `post_update_dvr_session_with_metadata` interceptor runs after the
        `post_update_dvr_session` interceptor. The (possibly modified) response returned by
        `post_update_dvr_session` will be passed to
        `post_update_dvr_session_with_metadata`.
        """
        return response, metadata

    def pre_update_input(
        self,
        request: service.UpdateInputRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.UpdateInputRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for update_input

        Override in a subclass to manipulate the request or metadata
        before they are sent to the LivestreamService server.
        """
        return request, metadata

    def post_update_input(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_input

        DEPRECATED. Please use the `post_update_input_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the LivestreamService server but before
        it is returned to user code. This `post_update_input` interceptor runs
        before the `post_update_input_with_metadata` interceptor.
        """
        return response

    def post_update_input_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_input

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the LivestreamService server but before it is returned to user code.

        We recommend only using this `post_update_input_with_metadata`
        interceptor in new development instead of the `post_update_input` interceptor.
        When both interceptors are used, this `post_update_input_with_metadata` interceptor runs after the
        `post_update_input` interceptor. The (possibly modified) response returned by
        `post_update_input` will be passed to
        `post_update_input_with_metadata`.
        """
        return response, metadata

    def pre_update_pool(
        self,
        request: service.UpdatePoolRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.UpdatePoolRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for update_pool

        Override in a subclass to manipulate the request or metadata
        before they are sent to the LivestreamService server.
        """
        return request, metadata

    def post_update_pool(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_pool

        DEPRECATED. Please use the `post_update_pool_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the LivestreamService server but before
        it is returned to user code. This `post_update_pool` interceptor runs
        before the `post_update_pool_with_metadata` interceptor.
        """
        return response

    def post_update_pool_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_pool

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the LivestreamService server but before it is returned to user code.

        We recommend only using this `post_update_pool_with_metadata`
        interceptor in new development instead of the `post_update_pool` interceptor.
        When both interceptors are used, this `post_update_pool_with_metadata` interceptor runs after the
        `post_update_pool` interceptor. The (possibly modified) response returned by
        `post_update_pool` will be passed to
        `post_update_pool_with_metadata`.
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
        before they are sent to the LivestreamService server.
        """
        return request, metadata

    def post_get_location(
        self, response: locations_pb2.Location
    ) -> locations_pb2.Location:
        """Post-rpc interceptor for get_location

        Override in a subclass to manipulate the response
        after it is returned by the LivestreamService server but before
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
        before they are sent to the LivestreamService server.
        """
        return request, metadata

    def post_list_locations(
        self, response: locations_pb2.ListLocationsResponse
    ) -> locations_pb2.ListLocationsResponse:
        """Post-rpc interceptor for list_locations

        Override in a subclass to manipulate the response
        after it is returned by the LivestreamService server but before
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
        before they are sent to the LivestreamService server.
        """
        return request, metadata

    def post_cancel_operation(self, response: None) -> None:
        """Post-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the response
        after it is returned by the LivestreamService server but before
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
        before they are sent to the LivestreamService server.
        """
        return request, metadata

    def post_delete_operation(self, response: None) -> None:
        """Post-rpc interceptor for delete_operation

        Override in a subclass to manipulate the response
        after it is returned by the LivestreamService server but before
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
        before they are sent to the LivestreamService server.
        """
        return request, metadata

    def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the LivestreamService server but before
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
        before they are sent to the LivestreamService server.
        """
        return request, metadata

    def post_list_operations(
        self, response: operations_pb2.ListOperationsResponse
    ) -> operations_pb2.ListOperationsResponse:
        """Post-rpc interceptor for list_operations

        Override in a subclass to manipulate the response
        after it is returned by the LivestreamService server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class LivestreamServiceRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: LivestreamServiceRestInterceptor


class LivestreamServiceRestTransport(_BaseLivestreamServiceRestTransport):
    """REST backend synchronous transport for LivestreamService.

    Using Live Stream API, you can generate live streams in the
    various renditions and streaming formats. The streaming format
    include HTTP Live Streaming (HLS) and Dynamic Adaptive Streaming
    over HTTP (DASH). You can send a source stream in the various
    ways, including Real-Time Messaging Protocol (RTMP) and Secure
    Reliable Transport (SRT).

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "livestream.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[LivestreamServiceRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'livestream.googleapis.com').
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
            interceptor (Optional[LivestreamServiceRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or LivestreamServiceRestInterceptor()
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

    class _CreateAsset(
        _BaseLivestreamServiceRestTransport._BaseCreateAsset, LivestreamServiceRestStub
    ):
        def __hash__(self):
            return hash("LivestreamServiceRestTransport.CreateAsset")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: service.CreateAssetRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create asset method over HTTP.

            Args:
                request (~.service.CreateAssetRequest):
                    The request object. Request message for
                "LivestreamService.CreateAsset".
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
                _BaseLivestreamServiceRestTransport._BaseCreateAsset._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_asset(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLivestreamServiceRestTransport._BaseCreateAsset,
                    "_BaseCreateAsset__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.video.livestream_v1.LivestreamServiceClient.CreateAsset",
                    extra={
                        "serviceName": "google.cloud.video.livestream.v1.LivestreamService",
                        "rpcName": "CreateAsset",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LivestreamServiceRestTransport._CreateAsset._get_response(
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

            resp = self._interceptor.post_create_asset(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_asset_with_metadata(
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
                    "Received response for google.cloud.video.livestream_v1.LivestreamServiceClient.create_asset",
                    extra={
                        "serviceName": "google.cloud.video.livestream.v1.LivestreamService",
                        "rpcName": "CreateAsset",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateChannel(
        _BaseLivestreamServiceRestTransport._BaseCreateChannel,
        LivestreamServiceRestStub,
    ):
        def __hash__(self):
            return hash("LivestreamServiceRestTransport.CreateChannel")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: service.CreateChannelRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create channel method over HTTP.

            Args:
                request (~.service.CreateChannelRequest):
                    The request object. Request message for
                "LivestreamService.CreateChannel".
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

            http_options = _BaseLivestreamServiceRestTransport._BaseCreateChannel._get_http_options()
            request, metadata = self._interceptor.pre_create_channel(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLivestreamServiceRestTransport._BaseCreateChannel,
                    "_BaseCreateChannel__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.video.livestream_v1.LivestreamServiceClient.CreateChannel",
                    extra={
                        "serviceName": "google.cloud.video.livestream.v1.LivestreamService",
                        "rpcName": "CreateChannel",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LivestreamServiceRestTransport._CreateChannel._get_response(
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

            resp = self._interceptor.post_create_channel(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_channel_with_metadata(
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
                    "Received response for google.cloud.video.livestream_v1.LivestreamServiceClient.create_channel_",
                    extra={
                        "serviceName": "google.cloud.video.livestream.v1.LivestreamService",
                        "rpcName": "CreateChannel",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateClip(
        _BaseLivestreamServiceRestTransport._BaseCreateClip, LivestreamServiceRestStub
    ):
        def __hash__(self):
            return hash("LivestreamServiceRestTransport.CreateClip")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: service.CreateClipRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create clip method over HTTP.

            Args:
                request (~.service.CreateClipRequest):
                    The request object. Request message for
                "LivestreamService.CreateClip".
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
                _BaseLivestreamServiceRestTransport._BaseCreateClip._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_clip(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLivestreamServiceRestTransport._BaseCreateClip,
                    "_BaseCreateClip__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.video.livestream_v1.LivestreamServiceClient.CreateClip",
                    extra={
                        "serviceName": "google.cloud.video.livestream.v1.LivestreamService",
                        "rpcName": "CreateClip",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LivestreamServiceRestTransport._CreateClip._get_response(
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

            resp = self._interceptor.post_create_clip(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_clip_with_metadata(
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
                    "Received response for google.cloud.video.livestream_v1.LivestreamServiceClient.create_clip",
                    extra={
                        "serviceName": "google.cloud.video.livestream.v1.LivestreamService",
                        "rpcName": "CreateClip",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateDvrSession(
        _BaseLivestreamServiceRestTransport._BaseCreateDvrSession,
        LivestreamServiceRestStub,
    ):
        def __hash__(self):
            return hash("LivestreamServiceRestTransport.CreateDvrSession")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: service.CreateDvrSessionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create dvr session method over HTTP.

            Args:
                request (~.service.CreateDvrSessionRequest):
                    The request object. Request message for
                "LivestreamService.CreateDvrSession".
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

            http_options = _BaseLivestreamServiceRestTransport._BaseCreateDvrSession._get_http_options()
            request, metadata = self._interceptor.pre_create_dvr_session(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLivestreamServiceRestTransport._BaseCreateDvrSession,
                    "_BaseCreateDvrSession__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.video.livestream_v1.LivestreamServiceClient.CreateDvrSession",
                    extra={
                        "serviceName": "google.cloud.video.livestream.v1.LivestreamService",
                        "rpcName": "CreateDvrSession",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LivestreamServiceRestTransport._CreateDvrSession._get_response(
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

            resp = self._interceptor.post_create_dvr_session(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_dvr_session_with_metadata(
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
                    "Received response for google.cloud.video.livestream_v1.LivestreamServiceClient.create_dvr_session",
                    extra={
                        "serviceName": "google.cloud.video.livestream.v1.LivestreamService",
                        "rpcName": "CreateDvrSession",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateEvent(
        _BaseLivestreamServiceRestTransport._BaseCreateEvent, LivestreamServiceRestStub
    ):
        def __hash__(self):
            return hash("LivestreamServiceRestTransport.CreateEvent")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: service.CreateEventRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> resources.Event:
            r"""Call the create event method over HTTP.

            Args:
                request (~.service.CreateEventRequest):
                    The request object. Request message for
                "LivestreamService.CreateEvent".
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.resources.Event:
                    Event is a sub-resource of a channel,
                which can be scheduled by the user to
                execute operations on a channel resource
                without having to stop the channel.

            """

            http_options = (
                _BaseLivestreamServiceRestTransport._BaseCreateEvent._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_event(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLivestreamServiceRestTransport._BaseCreateEvent,
                    "_BaseCreateEvent__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.video.livestream_v1.LivestreamServiceClient.CreateEvent",
                    extra={
                        "serviceName": "google.cloud.video.livestream.v1.LivestreamService",
                        "rpcName": "CreateEvent",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LivestreamServiceRestTransport._CreateEvent._get_response(
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
            resp = resources.Event()
            pb_resp = resources.Event.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_event(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_event_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = resources.Event.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.video.livestream_v1.LivestreamServiceClient.create_event",
                    extra={
                        "serviceName": "google.cloud.video.livestream.v1.LivestreamService",
                        "rpcName": "CreateEvent",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateInput(
        _BaseLivestreamServiceRestTransport._BaseCreateInput, LivestreamServiceRestStub
    ):
        def __hash__(self):
            return hash("LivestreamServiceRestTransport.CreateInput")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: service.CreateInputRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create input method over HTTP.

            Args:
                request (~.service.CreateInputRequest):
                    The request object. Request message for
                "LivestreamService.CreateInput".
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
                _BaseLivestreamServiceRestTransport._BaseCreateInput._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_input(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLivestreamServiceRestTransport._BaseCreateInput,
                    "_BaseCreateInput__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.video.livestream_v1.LivestreamServiceClient.CreateInput",
                    extra={
                        "serviceName": "google.cloud.video.livestream.v1.LivestreamService",
                        "rpcName": "CreateInput",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LivestreamServiceRestTransport._CreateInput._get_response(
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

            resp = self._interceptor.post_create_input(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_input_with_metadata(
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
                    "Received response for google.cloud.video.livestream_v1.LivestreamServiceClient.create_input",
                    extra={
                        "serviceName": "google.cloud.video.livestream.v1.LivestreamService",
                        "rpcName": "CreateInput",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteAsset(
        _BaseLivestreamServiceRestTransport._BaseDeleteAsset, LivestreamServiceRestStub
    ):
        def __hash__(self):
            return hash("LivestreamServiceRestTransport.DeleteAsset")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: service.DeleteAssetRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete asset method over HTTP.

            Args:
                request (~.service.DeleteAssetRequest):
                    The request object. Request message for
                "LivestreamService.DeleteAsset".
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
                _BaseLivestreamServiceRestTransport._BaseDeleteAsset._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_asset(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLivestreamServiceRestTransport._BaseDeleteAsset,
                    "_BaseDeleteAsset__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.video.livestream_v1.LivestreamServiceClient.DeleteAsset",
                    extra={
                        "serviceName": "google.cloud.video.livestream.v1.LivestreamService",
                        "rpcName": "DeleteAsset",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LivestreamServiceRestTransport._DeleteAsset._get_response(
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

            resp = self._interceptor.post_delete_asset(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_asset_with_metadata(
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
                    "Received response for google.cloud.video.livestream_v1.LivestreamServiceClient.delete_asset",
                    extra={
                        "serviceName": "google.cloud.video.livestream.v1.LivestreamService",
                        "rpcName": "DeleteAsset",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteChannel(
        _BaseLivestreamServiceRestTransport._BaseDeleteChannel,
        LivestreamServiceRestStub,
    ):
        def __hash__(self):
            return hash("LivestreamServiceRestTransport.DeleteChannel")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: service.DeleteChannelRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete channel method over HTTP.

            Args:
                request (~.service.DeleteChannelRequest):
                    The request object. Request message for
                "LivestreamService.DeleteChannel".
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

            http_options = _BaseLivestreamServiceRestTransport._BaseDeleteChannel._get_http_options()
            request, metadata = self._interceptor.pre_delete_channel(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLivestreamServiceRestTransport._BaseDeleteChannel,
                    "_BaseDeleteChannel__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.video.livestream_v1.LivestreamServiceClient.DeleteChannel",
                    extra={
                        "serviceName": "google.cloud.video.livestream.v1.LivestreamService",
                        "rpcName": "DeleteChannel",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LivestreamServiceRestTransport._DeleteChannel._get_response(
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

            resp = self._interceptor.post_delete_channel(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_channel_with_metadata(
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
                    "Received response for google.cloud.video.livestream_v1.LivestreamServiceClient.delete_channel",
                    extra={
                        "serviceName": "google.cloud.video.livestream.v1.LivestreamService",
                        "rpcName": "DeleteChannel",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteClip(
        _BaseLivestreamServiceRestTransport._BaseDeleteClip, LivestreamServiceRestStub
    ):
        def __hash__(self):
            return hash("LivestreamServiceRestTransport.DeleteClip")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: service.DeleteClipRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete clip method over HTTP.

            Args:
                request (~.service.DeleteClipRequest):
                    The request object. Request message for
                "LivestreamService.DeleteClip".
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
                _BaseLivestreamServiceRestTransport._BaseDeleteClip._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_clip(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLivestreamServiceRestTransport._BaseDeleteClip,
                    "_BaseDeleteClip__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.video.livestream_v1.LivestreamServiceClient.DeleteClip",
                    extra={
                        "serviceName": "google.cloud.video.livestream.v1.LivestreamService",
                        "rpcName": "DeleteClip",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LivestreamServiceRestTransport._DeleteClip._get_response(
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

            resp = self._interceptor.post_delete_clip(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_clip_with_metadata(
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
                    "Received response for google.cloud.video.livestream_v1.LivestreamServiceClient.delete_clip",
                    extra={
                        "serviceName": "google.cloud.video.livestream.v1.LivestreamService",
                        "rpcName": "DeleteClip",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteDvrSession(
        _BaseLivestreamServiceRestTransport._BaseDeleteDvrSession,
        LivestreamServiceRestStub,
    ):
        def __hash__(self):
            return hash("LivestreamServiceRestTransport.DeleteDvrSession")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: service.DeleteDvrSessionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete dvr session method over HTTP.

            Args:
                request (~.service.DeleteDvrSessionRequest):
                    The request object. Request message for
                "LivestreamService.DeleteDvrSession".
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

            http_options = _BaseLivestreamServiceRestTransport._BaseDeleteDvrSession._get_http_options()
            request, metadata = self._interceptor.pre_delete_dvr_session(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLivestreamServiceRestTransport._BaseDeleteDvrSession,
                    "_BaseDeleteDvrSession__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.video.livestream_v1.LivestreamServiceClient.DeleteDvrSession",
                    extra={
                        "serviceName": "google.cloud.video.livestream.v1.LivestreamService",
                        "rpcName": "DeleteDvrSession",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LivestreamServiceRestTransport._DeleteDvrSession._get_response(
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

            resp = self._interceptor.post_delete_dvr_session(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_dvr_session_with_metadata(
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
                    "Received response for google.cloud.video.livestream_v1.LivestreamServiceClient.delete_dvr_session",
                    extra={
                        "serviceName": "google.cloud.video.livestream.v1.LivestreamService",
                        "rpcName": "DeleteDvrSession",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteEvent(
        _BaseLivestreamServiceRestTransport._BaseDeleteEvent, LivestreamServiceRestStub
    ):
        def __hash__(self):
            return hash("LivestreamServiceRestTransport.DeleteEvent")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: service.DeleteEventRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete event method over HTTP.

            Args:
                request (~.service.DeleteEventRequest):
                    The request object. Request message for
                "LivestreamService.DeleteEvent".
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = (
                _BaseLivestreamServiceRestTransport._BaseDeleteEvent._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_event(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLivestreamServiceRestTransport._BaseDeleteEvent,
                    "_BaseDeleteEvent__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.video.livestream_v1.LivestreamServiceClient.DeleteEvent",
                    extra={
                        "serviceName": "google.cloud.video.livestream.v1.LivestreamService",
                        "rpcName": "DeleteEvent",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LivestreamServiceRestTransport._DeleteEvent._get_response(
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

    class _DeleteInput(
        _BaseLivestreamServiceRestTransport._BaseDeleteInput, LivestreamServiceRestStub
    ):
        def __hash__(self):
            return hash("LivestreamServiceRestTransport.DeleteInput")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: service.DeleteInputRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete input method over HTTP.

            Args:
                request (~.service.DeleteInputRequest):
                    The request object. Request message for
                "LivestreamService.DeleteInput".
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
                _BaseLivestreamServiceRestTransport._BaseDeleteInput._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_input(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLivestreamServiceRestTransport._BaseDeleteInput,
                    "_BaseDeleteInput__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.video.livestream_v1.LivestreamServiceClient.DeleteInput",
                    extra={
                        "serviceName": "google.cloud.video.livestream.v1.LivestreamService",
                        "rpcName": "DeleteInput",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LivestreamServiceRestTransport._DeleteInput._get_response(
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

            resp = self._interceptor.post_delete_input(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_input_with_metadata(
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
                    "Received response for google.cloud.video.livestream_v1.LivestreamServiceClient.delete_input",
                    extra={
                        "serviceName": "google.cloud.video.livestream.v1.LivestreamService",
                        "rpcName": "DeleteInput",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetAsset(
        _BaseLivestreamServiceRestTransport._BaseGetAsset, LivestreamServiceRestStub
    ):
        def __hash__(self):
            return hash("LivestreamServiceRestTransport.GetAsset")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: service.GetAssetRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> resources.Asset:
            r"""Call the get asset method over HTTP.

            Args:
                request (~.service.GetAssetRequest):
                    The request object. Request message for
                "LivestreamService.GetAsset".
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.resources.Asset:
                    An asset represents a video or an
                image.

            """

            http_options = (
                _BaseLivestreamServiceRestTransport._BaseGetAsset._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_asset(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLivestreamServiceRestTransport._BaseGetAsset,
                    "_BaseGetAsset__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.video.livestream_v1.LivestreamServiceClient.GetAsset",
                    extra={
                        "serviceName": "google.cloud.video.livestream.v1.LivestreamService",
                        "rpcName": "GetAsset",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LivestreamServiceRestTransport._GetAsset._get_response(
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
            resp = resources.Asset()
            pb_resp = resources.Asset.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_asset(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_asset_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = resources.Asset.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.video.livestream_v1.LivestreamServiceClient.get_asset",
                    extra={
                        "serviceName": "google.cloud.video.livestream.v1.LivestreamService",
                        "rpcName": "GetAsset",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetChannel(
        _BaseLivestreamServiceRestTransport._BaseGetChannel, LivestreamServiceRestStub
    ):
        def __hash__(self):
            return hash("LivestreamServiceRestTransport.GetChannel")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: service.GetChannelRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> resources.Channel:
            r"""Call the get channel method over HTTP.

            Args:
                request (~.service.GetChannelRequest):
                    The request object. Request message for
                "LivestreamService.GetChannel".
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.resources.Channel:
                    Channel resource represents the
                processor that does a user-defined
                "streaming" operation, which includes
                getting an input stream through an
                input, transcoding it to multiple
                renditions, and publishing output live
                streams in certain formats (for example,
                HLS or DASH) to the specified location.

            """

            http_options = (
                _BaseLivestreamServiceRestTransport._BaseGetChannel._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_channel(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLivestreamServiceRestTransport._BaseGetChannel,
                    "_BaseGetChannel__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.video.livestream_v1.LivestreamServiceClient.GetChannel",
                    extra={
                        "serviceName": "google.cloud.video.livestream.v1.LivestreamService",
                        "rpcName": "GetChannel",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LivestreamServiceRestTransport._GetChannel._get_response(
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
            resp = resources.Channel()
            pb_resp = resources.Channel.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_channel(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_channel_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = resources.Channel.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.video.livestream_v1.LivestreamServiceClient.get_channel",
                    extra={
                        "serviceName": "google.cloud.video.livestream.v1.LivestreamService",
                        "rpcName": "GetChannel",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetClip(
        _BaseLivestreamServiceRestTransport._BaseGetClip, LivestreamServiceRestStub
    ):
        def __hash__(self):
            return hash("LivestreamServiceRestTransport.GetClip")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: service.GetClipRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> resources.Clip:
            r"""Call the get clip method over HTTP.

            Args:
                request (~.service.GetClipRequest):
                    The request object. Request message for
                "LivestreamService.GetClip".
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.resources.Clip:
                    Clip is a sub-resource under channel.
                Each clip represents a clipping
                operation that generates a VOD playlist
                from its channel given a set of
                timestamp ranges.

            """

            http_options = (
                _BaseLivestreamServiceRestTransport._BaseGetClip._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_clip(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLivestreamServiceRestTransport._BaseGetClip,
                    "_BaseGetClip__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.video.livestream_v1.LivestreamServiceClient.GetClip",
                    extra={
                        "serviceName": "google.cloud.video.livestream.v1.LivestreamService",
                        "rpcName": "GetClip",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LivestreamServiceRestTransport._GetClip._get_response(
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
            resp = resources.Clip()
            pb_resp = resources.Clip.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_clip(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_clip_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = resources.Clip.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.video.livestream_v1.LivestreamServiceClient.get_clip",
                    extra={
                        "serviceName": "google.cloud.video.livestream.v1.LivestreamService",
                        "rpcName": "GetClip",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetDvrSession(
        _BaseLivestreamServiceRestTransport._BaseGetDvrSession,
        LivestreamServiceRestStub,
    ):
        def __hash__(self):
            return hash("LivestreamServiceRestTransport.GetDvrSession")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: service.GetDvrSessionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> resources.DvrSession:
            r"""Call the get dvr session method over HTTP.

            Args:
                request (~.service.GetDvrSessionRequest):
                    The request object. Request message for
                "LivestreamService.GetDvrSession".
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.resources.DvrSession:
                    DvrSession is a sub-resource under
                channel. Each DvrSession represents a
                DVR recording of the live stream for a
                specific time range.

            """

            http_options = _BaseLivestreamServiceRestTransport._BaseGetDvrSession._get_http_options()
            request, metadata = self._interceptor.pre_get_dvr_session(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLivestreamServiceRestTransport._BaseGetDvrSession,
                    "_BaseGetDvrSession__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.video.livestream_v1.LivestreamServiceClient.GetDvrSession",
                    extra={
                        "serviceName": "google.cloud.video.livestream.v1.LivestreamService",
                        "rpcName": "GetDvrSession",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LivestreamServiceRestTransport._GetDvrSession._get_response(
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
            resp = resources.DvrSession()
            pb_resp = resources.DvrSession.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_dvr_session(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_dvr_session_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = resources.DvrSession.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.video.livestream_v1.LivestreamServiceClient.get_dvr_session",
                    extra={
                        "serviceName": "google.cloud.video.livestream.v1.LivestreamService",
                        "rpcName": "GetDvrSession",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetEvent(
        _BaseLivestreamServiceRestTransport._BaseGetEvent, LivestreamServiceRestStub
    ):
        def __hash__(self):
            return hash("LivestreamServiceRestTransport.GetEvent")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: service.GetEventRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> resources.Event:
            r"""Call the get event method over HTTP.

            Args:
                request (~.service.GetEventRequest):
                    The request object. Request message for
                "LivestreamService.GetEvent".
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.resources.Event:
                    Event is a sub-resource of a channel,
                which can be scheduled by the user to
                execute operations on a channel resource
                without having to stop the channel.

            """

            http_options = (
                _BaseLivestreamServiceRestTransport._BaseGetEvent._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_event(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLivestreamServiceRestTransport._BaseGetEvent,
                    "_BaseGetEvent__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.video.livestream_v1.LivestreamServiceClient.GetEvent",
                    extra={
                        "serviceName": "google.cloud.video.livestream.v1.LivestreamService",
                        "rpcName": "GetEvent",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LivestreamServiceRestTransport._GetEvent._get_response(
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
            resp = resources.Event()
            pb_resp = resources.Event.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_event(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_event_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = resources.Event.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.video.livestream_v1.LivestreamServiceClient.get_event",
                    extra={
                        "serviceName": "google.cloud.video.livestream.v1.LivestreamService",
                        "rpcName": "GetEvent",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetInput(
        _BaseLivestreamServiceRestTransport._BaseGetInput, LivestreamServiceRestStub
    ):
        def __hash__(self):
            return hash("LivestreamServiceRestTransport.GetInput")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: service.GetInputRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> resources.Input:
            r"""Call the get input method over HTTP.

            Args:
                request (~.service.GetInputRequest):
                    The request object. Request message for
                "LivestreamService.GetInput".
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.resources.Input:
                    Input resource represents the
                endpoint from which the channel ingests
                the input stream.

            """

            http_options = (
                _BaseLivestreamServiceRestTransport._BaseGetInput._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_input(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLivestreamServiceRestTransport._BaseGetInput,
                    "_BaseGetInput__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.video.livestream_v1.LivestreamServiceClient.GetInput",
                    extra={
                        "serviceName": "google.cloud.video.livestream.v1.LivestreamService",
                        "rpcName": "GetInput",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LivestreamServiceRestTransport._GetInput._get_response(
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
            resp = resources.Input()
            pb_resp = resources.Input.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_input(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_input_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = resources.Input.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.video.livestream_v1.LivestreamServiceClient.get_input",
                    extra={
                        "serviceName": "google.cloud.video.livestream.v1.LivestreamService",
                        "rpcName": "GetInput",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetPool(
        _BaseLivestreamServiceRestTransport._BaseGetPool, LivestreamServiceRestStub
    ):
        def __hash__(self):
            return hash("LivestreamServiceRestTransport.GetPool")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: service.GetPoolRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> resources.Pool:
            r"""Call the get pool method over HTTP.

            Args:
                request (~.service.GetPoolRequest):
                    The request object. Request message for
                "LivestreamService.GetPool".
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.resources.Pool:
                    Pool resource defines the
                configuration of Live Stream pools for a
                specific location. Currently we support
                only one pool resource per project per
                location. After the creation of the
                first input, a default pool is created
                automatically at
                "projects/{project}/locations/{location}/pools/default".

            """

            http_options = (
                _BaseLivestreamServiceRestTransport._BaseGetPool._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_pool(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLivestreamServiceRestTransport._BaseGetPool,
                    "_BaseGetPool__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.video.livestream_v1.LivestreamServiceClient.GetPool",
                    extra={
                        "serviceName": "google.cloud.video.livestream.v1.LivestreamService",
                        "rpcName": "GetPool",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LivestreamServiceRestTransport._GetPool._get_response(
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
            resp = resources.Pool()
            pb_resp = resources.Pool.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_pool(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_pool_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = resources.Pool.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.video.livestream_v1.LivestreamServiceClient.get_pool",
                    extra={
                        "serviceName": "google.cloud.video.livestream.v1.LivestreamService",
                        "rpcName": "GetPool",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListAssets(
        _BaseLivestreamServiceRestTransport._BaseListAssets, LivestreamServiceRestStub
    ):
        def __hash__(self):
            return hash("LivestreamServiceRestTransport.ListAssets")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: service.ListAssetsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> service.ListAssetsResponse:
            r"""Call the list assets method over HTTP.

            Args:
                request (~.service.ListAssetsRequest):
                    The request object. Request message for
                "LivestreamService.ListAssets".
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.service.ListAssetsResponse:
                    Response message for
                "LivestreamService.ListAssets".

            """

            http_options = (
                _BaseLivestreamServiceRestTransport._BaseListAssets._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_assets(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLivestreamServiceRestTransport._BaseListAssets,
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
                    f"Sending request for google.cloud.video.livestream_v1.LivestreamServiceClient.ListAssets",
                    extra={
                        "serviceName": "google.cloud.video.livestream.v1.LivestreamService",
                        "rpcName": "ListAssets",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LivestreamServiceRestTransport._ListAssets._get_response(
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
            resp = service.ListAssetsResponse()
            pb_resp = service.ListAssetsResponse.pb(resp)

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
                    response_payload = service.ListAssetsResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.video.livestream_v1.LivestreamServiceClient.list_assets",
                    extra={
                        "serviceName": "google.cloud.video.livestream.v1.LivestreamService",
                        "rpcName": "ListAssets",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListChannels(
        _BaseLivestreamServiceRestTransport._BaseListChannels, LivestreamServiceRestStub
    ):
        def __hash__(self):
            return hash("LivestreamServiceRestTransport.ListChannels")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: service.ListChannelsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> service.ListChannelsResponse:
            r"""Call the list channels method over HTTP.

            Args:
                request (~.service.ListChannelsRequest):
                    The request object. Request message for
                "LivestreamService.ListChannels".
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.service.ListChannelsResponse:
                    Response message for
                "LivestreamService.ListChannels".

            """

            http_options = _BaseLivestreamServiceRestTransport._BaseListChannels._get_http_options()
            request, metadata = self._interceptor.pre_list_channels(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLivestreamServiceRestTransport._BaseListChannels,
                    "_BaseListChannels__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.video.livestream_v1.LivestreamServiceClient.ListChannels",
                    extra={
                        "serviceName": "google.cloud.video.livestream.v1.LivestreamService",
                        "rpcName": "ListChannels",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LivestreamServiceRestTransport._ListChannels._get_response(
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
            resp = service.ListChannelsResponse()
            pb_resp = service.ListChannelsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_channels(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_channels_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = service.ListChannelsResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.video.livestream_v1.LivestreamServiceClient.list_channels",
                    extra={
                        "serviceName": "google.cloud.video.livestream.v1.LivestreamService",
                        "rpcName": "ListChannels",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListClips(
        _BaseLivestreamServiceRestTransport._BaseListClips, LivestreamServiceRestStub
    ):
        def __hash__(self):
            return hash("LivestreamServiceRestTransport.ListClips")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: service.ListClipsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> service.ListClipsResponse:
            r"""Call the list clips method over HTTP.

            Args:
                request (~.service.ListClipsRequest):
                    The request object. Request message for
                "LivestreamService.ListClips".
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.service.ListClipsResponse:
                    Response message for
                "LivestreamService.ListClips".

            """

            http_options = (
                _BaseLivestreamServiceRestTransport._BaseListClips._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_clips(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLivestreamServiceRestTransport._BaseListClips,
                    "_BaseListClips__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.video.livestream_v1.LivestreamServiceClient.ListClips",
                    extra={
                        "serviceName": "google.cloud.video.livestream.v1.LivestreamService",
                        "rpcName": "ListClips",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LivestreamServiceRestTransport._ListClips._get_response(
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
            resp = service.ListClipsResponse()
            pb_resp = service.ListClipsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_clips(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_clips_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = service.ListClipsResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.video.livestream_v1.LivestreamServiceClient.list_clips",
                    extra={
                        "serviceName": "google.cloud.video.livestream.v1.LivestreamService",
                        "rpcName": "ListClips",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListDvrSessions(
        _BaseLivestreamServiceRestTransport._BaseListDvrSessions,
        LivestreamServiceRestStub,
    ):
        def __hash__(self):
            return hash("LivestreamServiceRestTransport.ListDvrSessions")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: service.ListDvrSessionsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> service.ListDvrSessionsResponse:
            r"""Call the list dvr sessions method over HTTP.

            Args:
                request (~.service.ListDvrSessionsRequest):
                    The request object. Request message for
                "LivestreamService.ListDvrSessions".
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.service.ListDvrSessionsResponse:
                    Response message for
                "LivestreamService.ListDvrSessions".

            """

            http_options = _BaseLivestreamServiceRestTransport._BaseListDvrSessions._get_http_options()
            request, metadata = self._interceptor.pre_list_dvr_sessions(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLivestreamServiceRestTransport._BaseListDvrSessions,
                    "_BaseListDvrSessions__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.video.livestream_v1.LivestreamServiceClient.ListDvrSessions",
                    extra={
                        "serviceName": "google.cloud.video.livestream.v1.LivestreamService",
                        "rpcName": "ListDvrSessions",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LivestreamServiceRestTransport._ListDvrSessions._get_response(
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
            resp = service.ListDvrSessionsResponse()
            pb_resp = service.ListDvrSessionsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_dvr_sessions(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_dvr_sessions_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = service.ListDvrSessionsResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.video.livestream_v1.LivestreamServiceClient.list_dvr_sessions",
                    extra={
                        "serviceName": "google.cloud.video.livestream.v1.LivestreamService",
                        "rpcName": "ListDvrSessions",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListEvents(
        _BaseLivestreamServiceRestTransport._BaseListEvents, LivestreamServiceRestStub
    ):
        def __hash__(self):
            return hash("LivestreamServiceRestTransport.ListEvents")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: service.ListEventsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> service.ListEventsResponse:
            r"""Call the list events method over HTTP.

            Args:
                request (~.service.ListEventsRequest):
                    The request object. Request message for
                "LivestreamService.ListEvents".
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.service.ListEventsResponse:
                    Response message for
                "LivestreamService.ListEvents".

            """

            http_options = (
                _BaseLivestreamServiceRestTransport._BaseListEvents._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_events(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLivestreamServiceRestTransport._BaseListEvents,
                    "_BaseListEvents__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.video.livestream_v1.LivestreamServiceClient.ListEvents",
                    extra={
                        "serviceName": "google.cloud.video.livestream.v1.LivestreamService",
                        "rpcName": "ListEvents",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LivestreamServiceRestTransport._ListEvents._get_response(
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
            resp = service.ListEventsResponse()
            pb_resp = service.ListEventsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_events(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_events_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = service.ListEventsResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.video.livestream_v1.LivestreamServiceClient.list_events",
                    extra={
                        "serviceName": "google.cloud.video.livestream.v1.LivestreamService",
                        "rpcName": "ListEvents",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListInputs(
        _BaseLivestreamServiceRestTransport._BaseListInputs, LivestreamServiceRestStub
    ):
        def __hash__(self):
            return hash("LivestreamServiceRestTransport.ListInputs")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: service.ListInputsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> service.ListInputsResponse:
            r"""Call the list inputs method over HTTP.

            Args:
                request (~.service.ListInputsRequest):
                    The request object. Request message for
                "LivestreamService.ListInputs".
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.service.ListInputsResponse:
                    Response message for
                "LivestreamService.ListInputs".

            """

            http_options = (
                _BaseLivestreamServiceRestTransport._BaseListInputs._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_inputs(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLivestreamServiceRestTransport._BaseListInputs,
                    "_BaseListInputs__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.video.livestream_v1.LivestreamServiceClient.ListInputs",
                    extra={
                        "serviceName": "google.cloud.video.livestream.v1.LivestreamService",
                        "rpcName": "ListInputs",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LivestreamServiceRestTransport._ListInputs._get_response(
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
            resp = service.ListInputsResponse()
            pb_resp = service.ListInputsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_inputs(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_inputs_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = service.ListInputsResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.video.livestream_v1.LivestreamServiceClient.list_inputs",
                    extra={
                        "serviceName": "google.cloud.video.livestream.v1.LivestreamService",
                        "rpcName": "ListInputs",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _PreviewInput(
        _BaseLivestreamServiceRestTransport._BasePreviewInput, LivestreamServiceRestStub
    ):
        def __hash__(self):
            return hash("LivestreamServiceRestTransport.PreviewInput")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: service.PreviewInputRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> service.PreviewInputResponse:
            r"""Call the preview input method over HTTP.

            Args:
                request (~.service.PreviewInputRequest):
                    The request object. Request message for
                "LivestreamService.PreviewInput".
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.service.PreviewInputResponse:
                    Response message for
                "LivestreamService.PreviewInput"

            """

            http_options = _BaseLivestreamServiceRestTransport._BasePreviewInput._get_http_options()
            request, metadata = self._interceptor.pre_preview_input(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLivestreamServiceRestTransport._BasePreviewInput,
                    "_BasePreviewInput__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.video.livestream_v1.LivestreamServiceClient.PreviewInput",
                    extra={
                        "serviceName": "google.cloud.video.livestream.v1.LivestreamService",
                        "rpcName": "PreviewInput",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LivestreamServiceRestTransport._PreviewInput._get_response(
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
            resp = service.PreviewInputResponse()
            pb_resp = service.PreviewInputResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_preview_input(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_preview_input_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = service.PreviewInputResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.video.livestream_v1.LivestreamServiceClient.preview_input",
                    extra={
                        "serviceName": "google.cloud.video.livestream.v1.LivestreamService",
                        "rpcName": "PreviewInput",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _StartChannel(
        _BaseLivestreamServiceRestTransport._BaseStartChannel, LivestreamServiceRestStub
    ):
        def __hash__(self):
            return hash("LivestreamServiceRestTransport.StartChannel")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: service.StartChannelRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the start channel method over HTTP.

            Args:
                request (~.service.StartChannelRequest):
                    The request object. Request message for
                "LivestreamService.StartChannel".
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

            http_options = _BaseLivestreamServiceRestTransport._BaseStartChannel._get_http_options()
            request, metadata = self._interceptor.pre_start_channel(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLivestreamServiceRestTransport._BaseStartChannel,
                    "_BaseStartChannel__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.video.livestream_v1.LivestreamServiceClient.StartChannel",
                    extra={
                        "serviceName": "google.cloud.video.livestream.v1.LivestreamService",
                        "rpcName": "StartChannel",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LivestreamServiceRestTransport._StartChannel._get_response(
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

            resp = self._interceptor.post_start_channel(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_start_channel_with_metadata(
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
                    "Received response for google.cloud.video.livestream_v1.LivestreamServiceClient.start_channel",
                    extra={
                        "serviceName": "google.cloud.video.livestream.v1.LivestreamService",
                        "rpcName": "StartChannel",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _StartDistribution(
        _BaseLivestreamServiceRestTransport._BaseStartDistribution,
        LivestreamServiceRestStub,
    ):
        def __hash__(self):
            return hash("LivestreamServiceRestTransport.StartDistribution")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: service.StartDistributionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the start distribution method over HTTP.

            Args:
                request (~.service.StartDistributionRequest):
                    The request object. Request message for
                "LivestreamService.StartDistribution".
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

            http_options = _BaseLivestreamServiceRestTransport._BaseStartDistribution._get_http_options()
            request, metadata = self._interceptor.pre_start_distribution(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLivestreamServiceRestTransport._BaseStartDistribution,
                    "_BaseStartDistribution__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.video.livestream_v1.LivestreamServiceClient.StartDistribution",
                    extra={
                        "serviceName": "google.cloud.video.livestream.v1.LivestreamService",
                        "rpcName": "StartDistribution",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LivestreamServiceRestTransport._StartDistribution._get_response(
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

            resp = self._interceptor.post_start_distribution(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_start_distribution_with_metadata(
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
                    "Received response for google.cloud.video.livestream_v1.LivestreamServiceClient.start_distribution",
                    extra={
                        "serviceName": "google.cloud.video.livestream.v1.LivestreamService",
                        "rpcName": "StartDistribution",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _StopChannel(
        _BaseLivestreamServiceRestTransport._BaseStopChannel, LivestreamServiceRestStub
    ):
        def __hash__(self):
            return hash("LivestreamServiceRestTransport.StopChannel")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: service.StopChannelRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the stop channel method over HTTP.

            Args:
                request (~.service.StopChannelRequest):
                    The request object. Request message for
                "LivestreamService.StopChannel".
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
                _BaseLivestreamServiceRestTransport._BaseStopChannel._get_http_options()
            )
            request, metadata = self._interceptor.pre_stop_channel(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLivestreamServiceRestTransport._BaseStopChannel,
                    "_BaseStopChannel__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.video.livestream_v1.LivestreamServiceClient.StopChannel",
                    extra={
                        "serviceName": "google.cloud.video.livestream.v1.LivestreamService",
                        "rpcName": "StopChannel",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LivestreamServiceRestTransport._StopChannel._get_response(
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

            resp = self._interceptor.post_stop_channel(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_stop_channel_with_metadata(
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
                    "Received response for google.cloud.video.livestream_v1.LivestreamServiceClient.stop_channel",
                    extra={
                        "serviceName": "google.cloud.video.livestream.v1.LivestreamService",
                        "rpcName": "StopChannel",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _StopDistribution(
        _BaseLivestreamServiceRestTransport._BaseStopDistribution,
        LivestreamServiceRestStub,
    ):
        def __hash__(self):
            return hash("LivestreamServiceRestTransport.StopDistribution")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: service.StopDistributionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the stop distribution method over HTTP.

            Args:
                request (~.service.StopDistributionRequest):
                    The request object. Request message for
                "LivestreamService.StopDistribution".
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

            http_options = _BaseLivestreamServiceRestTransport._BaseStopDistribution._get_http_options()
            request, metadata = self._interceptor.pre_stop_distribution(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLivestreamServiceRestTransport._BaseStopDistribution,
                    "_BaseStopDistribution__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.video.livestream_v1.LivestreamServiceClient.StopDistribution",
                    extra={
                        "serviceName": "google.cloud.video.livestream.v1.LivestreamService",
                        "rpcName": "StopDistribution",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LivestreamServiceRestTransport._StopDistribution._get_response(
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

            resp = self._interceptor.post_stop_distribution(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_stop_distribution_with_metadata(
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
                    "Received response for google.cloud.video.livestream_v1.LivestreamServiceClient.stop_distribution",
                    extra={
                        "serviceName": "google.cloud.video.livestream.v1.LivestreamService",
                        "rpcName": "StopDistribution",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateChannel(
        _BaseLivestreamServiceRestTransport._BaseUpdateChannel,
        LivestreamServiceRestStub,
    ):
        def __hash__(self):
            return hash("LivestreamServiceRestTransport.UpdateChannel")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: service.UpdateChannelRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update channel method over HTTP.

            Args:
                request (~.service.UpdateChannelRequest):
                    The request object. Request message for
                "LivestreamService.UpdateChannel".
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

            http_options = _BaseLivestreamServiceRestTransport._BaseUpdateChannel._get_http_options()
            request, metadata = self._interceptor.pre_update_channel(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLivestreamServiceRestTransport._BaseUpdateChannel,
                    "_BaseUpdateChannel__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.video.livestream_v1.LivestreamServiceClient.UpdateChannel",
                    extra={
                        "serviceName": "google.cloud.video.livestream.v1.LivestreamService",
                        "rpcName": "UpdateChannel",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LivestreamServiceRestTransport._UpdateChannel._get_response(
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

            resp = self._interceptor.post_update_channel(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_channel_with_metadata(
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
                    "Received response for google.cloud.video.livestream_v1.LivestreamServiceClient.update_channel",
                    extra={
                        "serviceName": "google.cloud.video.livestream.v1.LivestreamService",
                        "rpcName": "UpdateChannel",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateDvrSession(
        _BaseLivestreamServiceRestTransport._BaseUpdateDvrSession,
        LivestreamServiceRestStub,
    ):
        def __hash__(self):
            return hash("LivestreamServiceRestTransport.UpdateDvrSession")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: service.UpdateDvrSessionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update dvr session method over HTTP.

            Args:
                request (~.service.UpdateDvrSessionRequest):
                    The request object. Request message for
                "LivestreamService.UpdateDvrSession".
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

            http_options = _BaseLivestreamServiceRestTransport._BaseUpdateDvrSession._get_http_options()
            request, metadata = self._interceptor.pre_update_dvr_session(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLivestreamServiceRestTransport._BaseUpdateDvrSession,
                    "_BaseUpdateDvrSession__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.video.livestream_v1.LivestreamServiceClient.UpdateDvrSession",
                    extra={
                        "serviceName": "google.cloud.video.livestream.v1.LivestreamService",
                        "rpcName": "UpdateDvrSession",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LivestreamServiceRestTransport._UpdateDvrSession._get_response(
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

            resp = self._interceptor.post_update_dvr_session(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_dvr_session_with_metadata(
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
                    "Received response for google.cloud.video.livestream_v1.LivestreamServiceClient.update_dvr_session",
                    extra={
                        "serviceName": "google.cloud.video.livestream.v1.LivestreamService",
                        "rpcName": "UpdateDvrSession",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateInput(
        _BaseLivestreamServiceRestTransport._BaseUpdateInput, LivestreamServiceRestStub
    ):
        def __hash__(self):
            return hash("LivestreamServiceRestTransport.UpdateInput")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: service.UpdateInputRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update input method over HTTP.

            Args:
                request (~.service.UpdateInputRequest):
                    The request object. Request message for
                "LivestreamService.UpdateInput".
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
                _BaseLivestreamServiceRestTransport._BaseUpdateInput._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_input(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLivestreamServiceRestTransport._BaseUpdateInput,
                    "_BaseUpdateInput__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.video.livestream_v1.LivestreamServiceClient.UpdateInput",
                    extra={
                        "serviceName": "google.cloud.video.livestream.v1.LivestreamService",
                        "rpcName": "UpdateInput",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LivestreamServiceRestTransport._UpdateInput._get_response(
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

            resp = self._interceptor.post_update_input(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_input_with_metadata(
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
                    "Received response for google.cloud.video.livestream_v1.LivestreamServiceClient.update_input",
                    extra={
                        "serviceName": "google.cloud.video.livestream.v1.LivestreamService",
                        "rpcName": "UpdateInput",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdatePool(
        _BaseLivestreamServiceRestTransport._BaseUpdatePool, LivestreamServiceRestStub
    ):
        def __hash__(self):
            return hash("LivestreamServiceRestTransport.UpdatePool")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: service.UpdatePoolRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update pool method over HTTP.

            Args:
                request (~.service.UpdatePoolRequest):
                    The request object. Request message for
                "LivestreamService.UpdatePool".
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
                _BaseLivestreamServiceRestTransport._BaseUpdatePool._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_pool(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLivestreamServiceRestTransport._BaseUpdatePool,
                    "_BaseUpdatePool__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.video.livestream_v1.LivestreamServiceClient.UpdatePool",
                    extra={
                        "serviceName": "google.cloud.video.livestream.v1.LivestreamService",
                        "rpcName": "UpdatePool",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LivestreamServiceRestTransport._UpdatePool._get_response(
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

            resp = self._interceptor.post_update_pool(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_pool_with_metadata(
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
                    "Received response for google.cloud.video.livestream_v1.LivestreamServiceClient.update_pool",
                    extra={
                        "serviceName": "google.cloud.video.livestream.v1.LivestreamService",
                        "rpcName": "UpdatePool",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def create_asset(
        self,
    ) -> Callable[[service.CreateAssetRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateAsset(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_channel_(
        self,
    ) -> Callable[[service.CreateChannelRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateChannel(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_clip(
        self,
    ) -> Callable[[service.CreateClipRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateClip(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_dvr_session(
        self,
    ) -> Callable[[service.CreateDvrSessionRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateDvrSession(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_event(self) -> Callable[[service.CreateEventRequest], resources.Event]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateEvent(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_input(
        self,
    ) -> Callable[[service.CreateInputRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateInput(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_asset(
        self,
    ) -> Callable[[service.DeleteAssetRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteAsset(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_channel(
        self,
    ) -> Callable[[service.DeleteChannelRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteChannel(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_clip(
        self,
    ) -> Callable[[service.DeleteClipRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteClip(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_dvr_session(
        self,
    ) -> Callable[[service.DeleteDvrSessionRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteDvrSession(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_event(self) -> Callable[[service.DeleteEventRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteEvent(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_input(
        self,
    ) -> Callable[[service.DeleteInputRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteInput(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_asset(self) -> Callable[[service.GetAssetRequest], resources.Asset]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetAsset(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_channel(self) -> Callable[[service.GetChannelRequest], resources.Channel]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetChannel(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_clip(self) -> Callable[[service.GetClipRequest], resources.Clip]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetClip(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_dvr_session(
        self,
    ) -> Callable[[service.GetDvrSessionRequest], resources.DvrSession]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetDvrSession(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_event(self) -> Callable[[service.GetEventRequest], resources.Event]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetEvent(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_input(self) -> Callable[[service.GetInputRequest], resources.Input]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetInput(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_pool(self) -> Callable[[service.GetPoolRequest], resources.Pool]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetPool(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_assets(
        self,
    ) -> Callable[[service.ListAssetsRequest], service.ListAssetsResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListAssets(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_channels(
        self,
    ) -> Callable[[service.ListChannelsRequest], service.ListChannelsResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListChannels(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_clips(
        self,
    ) -> Callable[[service.ListClipsRequest], service.ListClipsResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListClips(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_dvr_sessions(
        self,
    ) -> Callable[[service.ListDvrSessionsRequest], service.ListDvrSessionsResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListDvrSessions(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_events(
        self,
    ) -> Callable[[service.ListEventsRequest], service.ListEventsResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListEvents(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_inputs(
        self,
    ) -> Callable[[service.ListInputsRequest], service.ListInputsResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListInputs(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def preview_input(
        self,
    ) -> Callable[[service.PreviewInputRequest], service.PreviewInputResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._PreviewInput(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def start_channel(
        self,
    ) -> Callable[[service.StartChannelRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._StartChannel(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def start_distribution(
        self,
    ) -> Callable[[service.StartDistributionRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._StartDistribution(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def stop_channel(
        self,
    ) -> Callable[[service.StopChannelRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._StopChannel(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def stop_distribution(
        self,
    ) -> Callable[[service.StopDistributionRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._StopDistribution(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_channel(
        self,
    ) -> Callable[[service.UpdateChannelRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateChannel(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_dvr_session(
        self,
    ) -> Callable[[service.UpdateDvrSessionRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateDvrSession(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_input(
        self,
    ) -> Callable[[service.UpdateInputRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateInput(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_pool(
        self,
    ) -> Callable[[service.UpdatePoolRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdatePool(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_location(self):
        return self._GetLocation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetLocation(
        _BaseLivestreamServiceRestTransport._BaseGetLocation, LivestreamServiceRestStub
    ):
        def __hash__(self):
            return hash("LivestreamServiceRestTransport.GetLocation")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
                _BaseLivestreamServiceRestTransport._BaseGetLocation._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_location(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLivestreamServiceRestTransport._BaseGetLocation,
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
                    f"Sending request for google.cloud.video.livestream_v1.LivestreamServiceClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.video.livestream.v1.LivestreamService",
                        "rpcName": "GetLocation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LivestreamServiceRestTransport._GetLocation._get_response(
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
                    "Received response for google.cloud.video.livestream_v1.LivestreamServiceAsyncClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.video.livestream.v1.LivestreamService",
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
        _BaseLivestreamServiceRestTransport._BaseListLocations,
        LivestreamServiceRestStub,
    ):
        def __hash__(self):
            return hash("LivestreamServiceRestTransport.ListLocations")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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

            http_options = _BaseLivestreamServiceRestTransport._BaseListLocations._get_http_options()
            request, metadata = self._interceptor.pre_list_locations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLivestreamServiceRestTransport._BaseListLocations,
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
                    f"Sending request for google.cloud.video.livestream_v1.LivestreamServiceClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.video.livestream.v1.LivestreamService",
                        "rpcName": "ListLocations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LivestreamServiceRestTransport._ListLocations._get_response(
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
                    "Received response for google.cloud.video.livestream_v1.LivestreamServiceAsyncClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.video.livestream.v1.LivestreamService",
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
        _BaseLivestreamServiceRestTransport._BaseCancelOperation,
        LivestreamServiceRestStub,
    ):
        def __hash__(self):
            return hash("LivestreamServiceRestTransport.CancelOperation")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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

            http_options = _BaseLivestreamServiceRestTransport._BaseCancelOperation._get_http_options()
            request, metadata = self._interceptor.pre_cancel_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLivestreamServiceRestTransport._BaseCancelOperation,
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
                    f"Sending request for google.cloud.video.livestream_v1.LivestreamServiceClient.CancelOperation",
                    extra={
                        "serviceName": "google.cloud.video.livestream.v1.LivestreamService",
                        "rpcName": "CancelOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LivestreamServiceRestTransport._CancelOperation._get_response(
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
        _BaseLivestreamServiceRestTransport._BaseDeleteOperation,
        LivestreamServiceRestStub,
    ):
        def __hash__(self):
            return hash("LivestreamServiceRestTransport.DeleteOperation")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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

            http_options = _BaseLivestreamServiceRestTransport._BaseDeleteOperation._get_http_options()
            request, metadata = self._interceptor.pre_delete_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLivestreamServiceRestTransport._BaseDeleteOperation,
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
                    f"Sending request for google.cloud.video.livestream_v1.LivestreamServiceClient.DeleteOperation",
                    extra={
                        "serviceName": "google.cloud.video.livestream.v1.LivestreamService",
                        "rpcName": "DeleteOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LivestreamServiceRestTransport._DeleteOperation._get_response(
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
        _BaseLivestreamServiceRestTransport._BaseGetOperation, LivestreamServiceRestStub
    ):
        def __hash__(self):
            return hash("LivestreamServiceRestTransport.GetOperation")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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

            http_options = _BaseLivestreamServiceRestTransport._BaseGetOperation._get_http_options()
            request, metadata = self._interceptor.pre_get_operation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLivestreamServiceRestTransport._BaseGetOperation,
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
                    f"Sending request for google.cloud.video.livestream_v1.LivestreamServiceClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.video.livestream.v1.LivestreamService",
                        "rpcName": "GetOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LivestreamServiceRestTransport._GetOperation._get_response(
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
                    "Received response for google.cloud.video.livestream_v1.LivestreamServiceAsyncClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.video.livestream.v1.LivestreamService",
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
        _BaseLivestreamServiceRestTransport._BaseListOperations,
        LivestreamServiceRestStub,
    ):
        def __hash__(self):
            return hash("LivestreamServiceRestTransport.ListOperations")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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

            http_options = _BaseLivestreamServiceRestTransport._BaseListOperations._get_http_options()
            request, metadata = self._interceptor.pre_list_operations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLivestreamServiceRestTransport._BaseListOperations,
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
                    f"Sending request for google.cloud.video.livestream_v1.LivestreamServiceClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.video.livestream.v1.LivestreamService",
                        "rpcName": "ListOperations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LivestreamServiceRestTransport._ListOperations._get_response(
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
                    "Received response for google.cloud.video.livestream_v1.LivestreamServiceAsyncClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.video.livestream.v1.LivestreamService",
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


__all__ = ("LivestreamServiceRestTransport",)
