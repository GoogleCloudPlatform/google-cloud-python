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
from google.api_core import gapic_v1, rest_helpers, rest_streaming
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.auth.transport.requests import AuthorizedSession  # type: ignore
from google.longrunning import operations_pb2  # type: ignore
from google.protobuf import json_format
from requests import __version__ as requests_version

from google.ads.admanager_v1._compat import transcode_request
from google.ads.admanager_v1.types import live_stream_messages, live_stream_service

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseLiveStreamServiceRestTransport

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


class LiveStreamServiceRestInterceptor:
    """Interceptor for LiveStreamService.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the LiveStreamServiceRestTransport.

    .. code-block:: python
        class MyCustomLiveStreamServiceInterceptor(LiveStreamServiceRestInterceptor):
            def pre_batch_activate_live_streams(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_activate_live_streams(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_batch_archive_live_streams(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_archive_live_streams(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_batch_create_live_streams(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_create_live_streams(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_batch_pause_ads_live_streams(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_pause_ads_live_streams(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_batch_pause_live_streams(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_pause_live_streams(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_batch_refresh_master_playlists(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_refresh_master_playlists(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_batch_update_live_streams(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_update_live_streams(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_live_stream(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_live_stream(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_live_stream(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_live_stream(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_live_streams(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_live_streams(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_live_stream(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_live_stream(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = LiveStreamServiceRestTransport(interceptor=MyCustomLiveStreamServiceInterceptor())
        client = LiveStreamServiceClient(transport=transport)


    """

    def pre_batch_activate_live_streams(
        self,
        request: live_stream_service.BatchActivateLiveStreamsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        live_stream_service.BatchActivateLiveStreamsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_activate_live_streams

        Override in a subclass to manipulate the request or metadata
        before they are sent to the LiveStreamService server.
        """
        return request, metadata

    def post_batch_activate_live_streams(
        self, response: live_stream_service.BatchActivateLiveStreamsResponse
    ) -> live_stream_service.BatchActivateLiveStreamsResponse:
        """Post-rpc interceptor for batch_activate_live_streams

        DEPRECATED. Please use the `post_batch_activate_live_streams_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the LiveStreamService server but before
        it is returned to user code. This `post_batch_activate_live_streams` interceptor runs
        before the `post_batch_activate_live_streams_with_metadata` interceptor.
        """
        return response

    def post_batch_activate_live_streams_with_metadata(
        self,
        response: live_stream_service.BatchActivateLiveStreamsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        live_stream_service.BatchActivateLiveStreamsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_activate_live_streams

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the LiveStreamService server but before it is returned to user code.

        We recommend only using this `post_batch_activate_live_streams_with_metadata`
        interceptor in new development instead of the `post_batch_activate_live_streams` interceptor.
        When both interceptors are used, this `post_batch_activate_live_streams_with_metadata` interceptor runs after the
        `post_batch_activate_live_streams` interceptor. The (possibly modified) response returned by
        `post_batch_activate_live_streams` will be passed to
        `post_batch_activate_live_streams_with_metadata`.
        """
        return response, metadata

    def pre_batch_archive_live_streams(
        self,
        request: live_stream_service.BatchArchiveLiveStreamsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        live_stream_service.BatchArchiveLiveStreamsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_archive_live_streams

        Override in a subclass to manipulate the request or metadata
        before they are sent to the LiveStreamService server.
        """
        return request, metadata

    def post_batch_archive_live_streams(
        self, response: live_stream_service.BatchArchiveLiveStreamsResponse
    ) -> live_stream_service.BatchArchiveLiveStreamsResponse:
        """Post-rpc interceptor for batch_archive_live_streams

        DEPRECATED. Please use the `post_batch_archive_live_streams_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the LiveStreamService server but before
        it is returned to user code. This `post_batch_archive_live_streams` interceptor runs
        before the `post_batch_archive_live_streams_with_metadata` interceptor.
        """
        return response

    def post_batch_archive_live_streams_with_metadata(
        self,
        response: live_stream_service.BatchArchiveLiveStreamsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        live_stream_service.BatchArchiveLiveStreamsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_archive_live_streams

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the LiveStreamService server but before it is returned to user code.

        We recommend only using this `post_batch_archive_live_streams_with_metadata`
        interceptor in new development instead of the `post_batch_archive_live_streams` interceptor.
        When both interceptors are used, this `post_batch_archive_live_streams_with_metadata` interceptor runs after the
        `post_batch_archive_live_streams` interceptor. The (possibly modified) response returned by
        `post_batch_archive_live_streams` will be passed to
        `post_batch_archive_live_streams_with_metadata`.
        """
        return response, metadata

    def pre_batch_create_live_streams(
        self,
        request: live_stream_service.BatchCreateLiveStreamsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        live_stream_service.BatchCreateLiveStreamsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_create_live_streams

        Override in a subclass to manipulate the request or metadata
        before they are sent to the LiveStreamService server.
        """
        return request, metadata

    def post_batch_create_live_streams(
        self, response: live_stream_service.BatchCreateLiveStreamsResponse
    ) -> live_stream_service.BatchCreateLiveStreamsResponse:
        """Post-rpc interceptor for batch_create_live_streams

        DEPRECATED. Please use the `post_batch_create_live_streams_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the LiveStreamService server but before
        it is returned to user code. This `post_batch_create_live_streams` interceptor runs
        before the `post_batch_create_live_streams_with_metadata` interceptor.
        """
        return response

    def post_batch_create_live_streams_with_metadata(
        self,
        response: live_stream_service.BatchCreateLiveStreamsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        live_stream_service.BatchCreateLiveStreamsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_create_live_streams

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the LiveStreamService server but before it is returned to user code.

        We recommend only using this `post_batch_create_live_streams_with_metadata`
        interceptor in new development instead of the `post_batch_create_live_streams` interceptor.
        When both interceptors are used, this `post_batch_create_live_streams_with_metadata` interceptor runs after the
        `post_batch_create_live_streams` interceptor. The (possibly modified) response returned by
        `post_batch_create_live_streams` will be passed to
        `post_batch_create_live_streams_with_metadata`.
        """
        return response, metadata

    def pre_batch_pause_ads_live_streams(
        self,
        request: live_stream_service.BatchPauseAdsLiveStreamsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        live_stream_service.BatchPauseAdsLiveStreamsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_pause_ads_live_streams

        Override in a subclass to manipulate the request or metadata
        before they are sent to the LiveStreamService server.
        """
        return request, metadata

    def post_batch_pause_ads_live_streams(
        self, response: live_stream_service.BatchPauseAdsLiveStreamsResponse
    ) -> live_stream_service.BatchPauseAdsLiveStreamsResponse:
        """Post-rpc interceptor for batch_pause_ads_live_streams

        DEPRECATED. Please use the `post_batch_pause_ads_live_streams_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the LiveStreamService server but before
        it is returned to user code. This `post_batch_pause_ads_live_streams` interceptor runs
        before the `post_batch_pause_ads_live_streams_with_metadata` interceptor.
        """
        return response

    def post_batch_pause_ads_live_streams_with_metadata(
        self,
        response: live_stream_service.BatchPauseAdsLiveStreamsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        live_stream_service.BatchPauseAdsLiveStreamsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_pause_ads_live_streams

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the LiveStreamService server but before it is returned to user code.

        We recommend only using this `post_batch_pause_ads_live_streams_with_metadata`
        interceptor in new development instead of the `post_batch_pause_ads_live_streams` interceptor.
        When both interceptors are used, this `post_batch_pause_ads_live_streams_with_metadata` interceptor runs after the
        `post_batch_pause_ads_live_streams` interceptor. The (possibly modified) response returned by
        `post_batch_pause_ads_live_streams` will be passed to
        `post_batch_pause_ads_live_streams_with_metadata`.
        """
        return response, metadata

    def pre_batch_pause_live_streams(
        self,
        request: live_stream_service.BatchPauseLiveStreamsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        live_stream_service.BatchPauseLiveStreamsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_pause_live_streams

        Override in a subclass to manipulate the request or metadata
        before they are sent to the LiveStreamService server.
        """
        return request, metadata

    def post_batch_pause_live_streams(
        self, response: live_stream_service.BatchPauseLiveStreamsResponse
    ) -> live_stream_service.BatchPauseLiveStreamsResponse:
        """Post-rpc interceptor for batch_pause_live_streams

        DEPRECATED. Please use the `post_batch_pause_live_streams_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the LiveStreamService server but before
        it is returned to user code. This `post_batch_pause_live_streams` interceptor runs
        before the `post_batch_pause_live_streams_with_metadata` interceptor.
        """
        return response

    def post_batch_pause_live_streams_with_metadata(
        self,
        response: live_stream_service.BatchPauseLiveStreamsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        live_stream_service.BatchPauseLiveStreamsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_pause_live_streams

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the LiveStreamService server but before it is returned to user code.

        We recommend only using this `post_batch_pause_live_streams_with_metadata`
        interceptor in new development instead of the `post_batch_pause_live_streams` interceptor.
        When both interceptors are used, this `post_batch_pause_live_streams_with_metadata` interceptor runs after the
        `post_batch_pause_live_streams` interceptor. The (possibly modified) response returned by
        `post_batch_pause_live_streams` will be passed to
        `post_batch_pause_live_streams_with_metadata`.
        """
        return response, metadata

    def pre_batch_refresh_master_playlists(
        self,
        request: live_stream_service.BatchRefreshMasterPlaylistsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        live_stream_service.BatchRefreshMasterPlaylistsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_refresh_master_playlists

        Override in a subclass to manipulate the request or metadata
        before they are sent to the LiveStreamService server.
        """
        return request, metadata

    def post_batch_refresh_master_playlists(
        self, response: live_stream_service.BatchRefreshMasterPlaylistsResponse
    ) -> live_stream_service.BatchRefreshMasterPlaylistsResponse:
        """Post-rpc interceptor for batch_refresh_master_playlists

        DEPRECATED. Please use the `post_batch_refresh_master_playlists_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the LiveStreamService server but before
        it is returned to user code. This `post_batch_refresh_master_playlists` interceptor runs
        before the `post_batch_refresh_master_playlists_with_metadata` interceptor.
        """
        return response

    def post_batch_refresh_master_playlists_with_metadata(
        self,
        response: live_stream_service.BatchRefreshMasterPlaylistsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        live_stream_service.BatchRefreshMasterPlaylistsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_refresh_master_playlists

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the LiveStreamService server but before it is returned to user code.

        We recommend only using this `post_batch_refresh_master_playlists_with_metadata`
        interceptor in new development instead of the `post_batch_refresh_master_playlists` interceptor.
        When both interceptors are used, this `post_batch_refresh_master_playlists_with_metadata` interceptor runs after the
        `post_batch_refresh_master_playlists` interceptor. The (possibly modified) response returned by
        `post_batch_refresh_master_playlists` will be passed to
        `post_batch_refresh_master_playlists_with_metadata`.
        """
        return response, metadata

    def pre_batch_update_live_streams(
        self,
        request: live_stream_service.BatchUpdateLiveStreamsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        live_stream_service.BatchUpdateLiveStreamsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_update_live_streams

        Override in a subclass to manipulate the request or metadata
        before they are sent to the LiveStreamService server.
        """
        return request, metadata

    def post_batch_update_live_streams(
        self, response: live_stream_service.BatchUpdateLiveStreamsResponse
    ) -> live_stream_service.BatchUpdateLiveStreamsResponse:
        """Post-rpc interceptor for batch_update_live_streams

        DEPRECATED. Please use the `post_batch_update_live_streams_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the LiveStreamService server but before
        it is returned to user code. This `post_batch_update_live_streams` interceptor runs
        before the `post_batch_update_live_streams_with_metadata` interceptor.
        """
        return response

    def post_batch_update_live_streams_with_metadata(
        self,
        response: live_stream_service.BatchUpdateLiveStreamsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        live_stream_service.BatchUpdateLiveStreamsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_update_live_streams

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the LiveStreamService server but before it is returned to user code.

        We recommend only using this `post_batch_update_live_streams_with_metadata`
        interceptor in new development instead of the `post_batch_update_live_streams` interceptor.
        When both interceptors are used, this `post_batch_update_live_streams_with_metadata` interceptor runs after the
        `post_batch_update_live_streams` interceptor. The (possibly modified) response returned by
        `post_batch_update_live_streams` will be passed to
        `post_batch_update_live_streams_with_metadata`.
        """
        return response, metadata

    def pre_create_live_stream(
        self,
        request: live_stream_service.CreateLiveStreamRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        live_stream_service.CreateLiveStreamRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_live_stream

        Override in a subclass to manipulate the request or metadata
        before they are sent to the LiveStreamService server.
        """
        return request, metadata

    def post_create_live_stream(
        self, response: live_stream_messages.LiveStream
    ) -> live_stream_messages.LiveStream:
        """Post-rpc interceptor for create_live_stream

        DEPRECATED. Please use the `post_create_live_stream_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the LiveStreamService server but before
        it is returned to user code. This `post_create_live_stream` interceptor runs
        before the `post_create_live_stream_with_metadata` interceptor.
        """
        return response

    def post_create_live_stream_with_metadata(
        self,
        response: live_stream_messages.LiveStream,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        live_stream_messages.LiveStream, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for create_live_stream

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the LiveStreamService server but before it is returned to user code.

        We recommend only using this `post_create_live_stream_with_metadata`
        interceptor in new development instead of the `post_create_live_stream` interceptor.
        When both interceptors are used, this `post_create_live_stream_with_metadata` interceptor runs after the
        `post_create_live_stream` interceptor. The (possibly modified) response returned by
        `post_create_live_stream` will be passed to
        `post_create_live_stream_with_metadata`.
        """
        return response, metadata

    def pre_get_live_stream(
        self,
        request: live_stream_service.GetLiveStreamRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        live_stream_service.GetLiveStreamRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_live_stream

        Override in a subclass to manipulate the request or metadata
        before they are sent to the LiveStreamService server.
        """
        return request, metadata

    def post_get_live_stream(
        self, response: live_stream_messages.LiveStream
    ) -> live_stream_messages.LiveStream:
        """Post-rpc interceptor for get_live_stream

        DEPRECATED. Please use the `post_get_live_stream_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the LiveStreamService server but before
        it is returned to user code. This `post_get_live_stream` interceptor runs
        before the `post_get_live_stream_with_metadata` interceptor.
        """
        return response

    def post_get_live_stream_with_metadata(
        self,
        response: live_stream_messages.LiveStream,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        live_stream_messages.LiveStream, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for get_live_stream

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the LiveStreamService server but before it is returned to user code.

        We recommend only using this `post_get_live_stream_with_metadata`
        interceptor in new development instead of the `post_get_live_stream` interceptor.
        When both interceptors are used, this `post_get_live_stream_with_metadata` interceptor runs after the
        `post_get_live_stream` interceptor. The (possibly modified) response returned by
        `post_get_live_stream` will be passed to
        `post_get_live_stream_with_metadata`.
        """
        return response, metadata

    def pre_list_live_streams(
        self,
        request: live_stream_service.ListLiveStreamsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        live_stream_service.ListLiveStreamsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_live_streams

        Override in a subclass to manipulate the request or metadata
        before they are sent to the LiveStreamService server.
        """
        return request, metadata

    def post_list_live_streams(
        self, response: live_stream_service.ListLiveStreamsResponse
    ) -> live_stream_service.ListLiveStreamsResponse:
        """Post-rpc interceptor for list_live_streams

        DEPRECATED. Please use the `post_list_live_streams_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the LiveStreamService server but before
        it is returned to user code. This `post_list_live_streams` interceptor runs
        before the `post_list_live_streams_with_metadata` interceptor.
        """
        return response

    def post_list_live_streams_with_metadata(
        self,
        response: live_stream_service.ListLiveStreamsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        live_stream_service.ListLiveStreamsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_live_streams

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the LiveStreamService server but before it is returned to user code.

        We recommend only using this `post_list_live_streams_with_metadata`
        interceptor in new development instead of the `post_list_live_streams` interceptor.
        When both interceptors are used, this `post_list_live_streams_with_metadata` interceptor runs after the
        `post_list_live_streams` interceptor. The (possibly modified) response returned by
        `post_list_live_streams` will be passed to
        `post_list_live_streams_with_metadata`.
        """
        return response, metadata

    def pre_update_live_stream(
        self,
        request: live_stream_service.UpdateLiveStreamRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        live_stream_service.UpdateLiveStreamRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_live_stream

        Override in a subclass to manipulate the request or metadata
        before they are sent to the LiveStreamService server.
        """
        return request, metadata

    def post_update_live_stream(
        self, response: live_stream_messages.LiveStream
    ) -> live_stream_messages.LiveStream:
        """Post-rpc interceptor for update_live_stream

        DEPRECATED. Please use the `post_update_live_stream_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the LiveStreamService server but before
        it is returned to user code. This `post_update_live_stream` interceptor runs
        before the `post_update_live_stream_with_metadata` interceptor.
        """
        return response

    def post_update_live_stream_with_metadata(
        self,
        response: live_stream_messages.LiveStream,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        live_stream_messages.LiveStream, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for update_live_stream

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the LiveStreamService server but before it is returned to user code.

        We recommend only using this `post_update_live_stream_with_metadata`
        interceptor in new development instead of the `post_update_live_stream` interceptor.
        When both interceptors are used, this `post_update_live_stream_with_metadata` interceptor runs after the
        `post_update_live_stream` interceptor. The (possibly modified) response returned by
        `post_update_live_stream` will be passed to
        `post_update_live_stream_with_metadata`.
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
        before they are sent to the LiveStreamService server.
        """
        return request, metadata

    def post_cancel_operation(self, response: None) -> None:
        """Post-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the response
        after it is returned by the LiveStreamService server but before
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
        before they are sent to the LiveStreamService server.
        """
        return request, metadata

    def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the LiveStreamService server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class LiveStreamServiceRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: LiveStreamServiceRestInterceptor


class LiveStreamServiceRestTransport(_BaseLiveStreamServiceRestTransport):
    """REST backend synchronous transport for LiveStreamService.

    Provides methods for handling ``LiveStream`` objects.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "admanager.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[LiveStreamServiceRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'admanager.googleapis.com').
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
            interceptor (Optional[LiveStreamServiceRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or LiveStreamServiceRestInterceptor()
        self._prep_wrapped_messages(client_info)

    class _BatchActivateLiveStreams(
        _BaseLiveStreamServiceRestTransport._BaseBatchActivateLiveStreams,
        LiveStreamServiceRestStub,
    ):
        def __hash__(self):
            return hash("LiveStreamServiceRestTransport.BatchActivateLiveStreams")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: live_stream_service.BatchActivateLiveStreamsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> live_stream_service.BatchActivateLiveStreamsResponse:
            r"""Call the batch activate live
            streams method over HTTP.

                Args:
                    request (~.live_stream_service.BatchActivateLiveStreamsRequest):
                        The request object. Request object for ``BatchActivateLiveStreams`` method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.live_stream_service.BatchActivateLiveStreamsResponse:
                        Response object for ``BatchActivateLiveStreams`` method.
            """

            http_options = _BaseLiveStreamServiceRestTransport._BaseBatchActivateLiveStreams._get_http_options()
            request, metadata = self._interceptor.pre_batch_activate_live_streams(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLiveStreamServiceRestTransport._BaseBatchActivateLiveStreams,
                    "_BaseBatchActivateLiveStreams__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.ads.admanager_v1.LiveStreamServiceClient.BatchActivateLiveStreams",
                    extra={
                        "serviceName": "google.ads.admanager.v1.LiveStreamService",
                        "rpcName": "BatchActivateLiveStreams",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                LiveStreamServiceRestTransport._BatchActivateLiveStreams._get_response(
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
            resp = live_stream_service.BatchActivateLiveStreamsResponse()
            pb_resp = live_stream_service.BatchActivateLiveStreamsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_activate_live_streams(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_batch_activate_live_streams_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        live_stream_service.BatchActivateLiveStreamsResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.LiveStreamServiceClient.batch_activate_live_streams",
                    extra={
                        "serviceName": "google.ads.admanager.v1.LiveStreamService",
                        "rpcName": "BatchActivateLiveStreams",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BatchArchiveLiveStreams(
        _BaseLiveStreamServiceRestTransport._BaseBatchArchiveLiveStreams,
        LiveStreamServiceRestStub,
    ):
        def __hash__(self):
            return hash("LiveStreamServiceRestTransport.BatchArchiveLiveStreams")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: live_stream_service.BatchArchiveLiveStreamsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> live_stream_service.BatchArchiveLiveStreamsResponse:
            r"""Call the batch archive live
            streams method over HTTP.

                Args:
                    request (~.live_stream_service.BatchArchiveLiveStreamsRequest):
                        The request object. Request object for ``BatchArchiveLiveStreams`` method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.live_stream_service.BatchArchiveLiveStreamsResponse:
                        Response object for ``BatchArchiveLiveStreams`` method.
            """

            http_options = _BaseLiveStreamServiceRestTransport._BaseBatchArchiveLiveStreams._get_http_options()
            request, metadata = self._interceptor.pre_batch_archive_live_streams(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLiveStreamServiceRestTransport._BaseBatchArchiveLiveStreams,
                    "_BaseBatchArchiveLiveStreams__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.ads.admanager_v1.LiveStreamServiceClient.BatchArchiveLiveStreams",
                    extra={
                        "serviceName": "google.ads.admanager.v1.LiveStreamService",
                        "rpcName": "BatchArchiveLiveStreams",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                LiveStreamServiceRestTransport._BatchArchiveLiveStreams._get_response(
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
            resp = live_stream_service.BatchArchiveLiveStreamsResponse()
            pb_resp = live_stream_service.BatchArchiveLiveStreamsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_archive_live_streams(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_batch_archive_live_streams_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        live_stream_service.BatchArchiveLiveStreamsResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.LiveStreamServiceClient.batch_archive_live_streams",
                    extra={
                        "serviceName": "google.ads.admanager.v1.LiveStreamService",
                        "rpcName": "BatchArchiveLiveStreams",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BatchCreateLiveStreams(
        _BaseLiveStreamServiceRestTransport._BaseBatchCreateLiveStreams,
        LiveStreamServiceRestStub,
    ):
        def __hash__(self):
            return hash("LiveStreamServiceRestTransport.BatchCreateLiveStreams")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: live_stream_service.BatchCreateLiveStreamsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> live_stream_service.BatchCreateLiveStreamsResponse:
            r"""Call the batch create live streams method over HTTP.

            Args:
                request (~.live_stream_service.BatchCreateLiveStreamsRequest):
                    The request object. Request object for ``BatchCreateLiveStreams`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.live_stream_service.BatchCreateLiveStreamsResponse:
                    Response object for ``BatchCreateLiveStreams`` method.
            """

            http_options = _BaseLiveStreamServiceRestTransport._BaseBatchCreateLiveStreams._get_http_options()
            request, metadata = self._interceptor.pre_batch_create_live_streams(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLiveStreamServiceRestTransport._BaseBatchCreateLiveStreams,
                    "_BaseBatchCreateLiveStreams__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.ads.admanager_v1.LiveStreamServiceClient.BatchCreateLiveStreams",
                    extra={
                        "serviceName": "google.ads.admanager.v1.LiveStreamService",
                        "rpcName": "BatchCreateLiveStreams",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                LiveStreamServiceRestTransport._BatchCreateLiveStreams._get_response(
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
            resp = live_stream_service.BatchCreateLiveStreamsResponse()
            pb_resp = live_stream_service.BatchCreateLiveStreamsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_create_live_streams(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_batch_create_live_streams_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        live_stream_service.BatchCreateLiveStreamsResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.LiveStreamServiceClient.batch_create_live_streams",
                    extra={
                        "serviceName": "google.ads.admanager.v1.LiveStreamService",
                        "rpcName": "BatchCreateLiveStreams",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BatchPauseAdsLiveStreams(
        _BaseLiveStreamServiceRestTransport._BaseBatchPauseAdsLiveStreams,
        LiveStreamServiceRestStub,
    ):
        def __hash__(self):
            return hash("LiveStreamServiceRestTransport.BatchPauseAdsLiveStreams")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: live_stream_service.BatchPauseAdsLiveStreamsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> live_stream_service.BatchPauseAdsLiveStreamsResponse:
            r"""Call the batch pause ads live
            streams method over HTTP.

                Args:
                    request (~.live_stream_service.BatchPauseAdsLiveStreamsRequest):
                        The request object. Request object for ``BatchPauseAdsLiveStreams`` method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.live_stream_service.BatchPauseAdsLiveStreamsResponse:
                        Response object for ``BatchPauseAdsLiveStreams`` method.
            """

            http_options = _BaseLiveStreamServiceRestTransport._BaseBatchPauseAdsLiveStreams._get_http_options()
            request, metadata = self._interceptor.pre_batch_pause_ads_live_streams(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLiveStreamServiceRestTransport._BaseBatchPauseAdsLiveStreams,
                    "_BaseBatchPauseAdsLiveStreams__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.ads.admanager_v1.LiveStreamServiceClient.BatchPauseAdsLiveStreams",
                    extra={
                        "serviceName": "google.ads.admanager.v1.LiveStreamService",
                        "rpcName": "BatchPauseAdsLiveStreams",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                LiveStreamServiceRestTransport._BatchPauseAdsLiveStreams._get_response(
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
            resp = live_stream_service.BatchPauseAdsLiveStreamsResponse()
            pb_resp = live_stream_service.BatchPauseAdsLiveStreamsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_pause_ads_live_streams(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_batch_pause_ads_live_streams_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        live_stream_service.BatchPauseAdsLiveStreamsResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.LiveStreamServiceClient.batch_pause_ads_live_streams",
                    extra={
                        "serviceName": "google.ads.admanager.v1.LiveStreamService",
                        "rpcName": "BatchPauseAdsLiveStreams",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BatchPauseLiveStreams(
        _BaseLiveStreamServiceRestTransport._BaseBatchPauseLiveStreams,
        LiveStreamServiceRestStub,
    ):
        def __hash__(self):
            return hash("LiveStreamServiceRestTransport.BatchPauseLiveStreams")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: live_stream_service.BatchPauseLiveStreamsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> live_stream_service.BatchPauseLiveStreamsResponse:
            r"""Call the batch pause live streams method over HTTP.

            Args:
                request (~.live_stream_service.BatchPauseLiveStreamsRequest):
                    The request object. Request object for ``BatchPauseLiveStreams`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.live_stream_service.BatchPauseLiveStreamsResponse:
                    Response object for ``BatchPauseLiveStreams`` method.
            """

            http_options = _BaseLiveStreamServiceRestTransport._BaseBatchPauseLiveStreams._get_http_options()
            request, metadata = self._interceptor.pre_batch_pause_live_streams(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLiveStreamServiceRestTransport._BaseBatchPauseLiveStreams,
                    "_BaseBatchPauseLiveStreams__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.ads.admanager_v1.LiveStreamServiceClient.BatchPauseLiveStreams",
                    extra={
                        "serviceName": "google.ads.admanager.v1.LiveStreamService",
                        "rpcName": "BatchPauseLiveStreams",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                LiveStreamServiceRestTransport._BatchPauseLiveStreams._get_response(
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
            resp = live_stream_service.BatchPauseLiveStreamsResponse()
            pb_resp = live_stream_service.BatchPauseLiveStreamsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_pause_live_streams(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_batch_pause_live_streams_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        live_stream_service.BatchPauseLiveStreamsResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.LiveStreamServiceClient.batch_pause_live_streams",
                    extra={
                        "serviceName": "google.ads.admanager.v1.LiveStreamService",
                        "rpcName": "BatchPauseLiveStreams",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BatchRefreshMasterPlaylists(
        _BaseLiveStreamServiceRestTransport._BaseBatchRefreshMasterPlaylists,
        LiveStreamServiceRestStub,
    ):
        def __hash__(self):
            return hash("LiveStreamServiceRestTransport.BatchRefreshMasterPlaylists")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: live_stream_service.BatchRefreshMasterPlaylistsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> live_stream_service.BatchRefreshMasterPlaylistsResponse:
            r"""Call the batch refresh master
            playlists method over HTTP.

                Args:
                    request (~.live_stream_service.BatchRefreshMasterPlaylistsRequest):
                        The request object. Request object for ``BatchRefreshMasterPlaylists``
                    method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.live_stream_service.BatchRefreshMasterPlaylistsResponse:
                        Response object for ``BatchRefreshMasterPlaylists``
                    method.

            """

            http_options = _BaseLiveStreamServiceRestTransport._BaseBatchRefreshMasterPlaylists._get_http_options()
            request, metadata = self._interceptor.pre_batch_refresh_master_playlists(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLiveStreamServiceRestTransport._BaseBatchRefreshMasterPlaylists,
                    "_BaseBatchRefreshMasterPlaylists__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.ads.admanager_v1.LiveStreamServiceClient.BatchRefreshMasterPlaylists",
                    extra={
                        "serviceName": "google.ads.admanager.v1.LiveStreamService",
                        "rpcName": "BatchRefreshMasterPlaylists",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LiveStreamServiceRestTransport._BatchRefreshMasterPlaylists._get_response(
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
            resp = live_stream_service.BatchRefreshMasterPlaylistsResponse()
            pb_resp = live_stream_service.BatchRefreshMasterPlaylistsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_refresh_master_playlists(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_batch_refresh_master_playlists_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        live_stream_service.BatchRefreshMasterPlaylistsResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.LiveStreamServiceClient.batch_refresh_master_playlists",
                    extra={
                        "serviceName": "google.ads.admanager.v1.LiveStreamService",
                        "rpcName": "BatchRefreshMasterPlaylists",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BatchUpdateLiveStreams(
        _BaseLiveStreamServiceRestTransport._BaseBatchUpdateLiveStreams,
        LiveStreamServiceRestStub,
    ):
        def __hash__(self):
            return hash("LiveStreamServiceRestTransport.BatchUpdateLiveStreams")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: live_stream_service.BatchUpdateLiveStreamsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> live_stream_service.BatchUpdateLiveStreamsResponse:
            r"""Call the batch update live streams method over HTTP.

            Args:
                request (~.live_stream_service.BatchUpdateLiveStreamsRequest):
                    The request object. Request object for ``BatchUpdateLiveStreams`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.live_stream_service.BatchUpdateLiveStreamsResponse:
                    Response object for ``BatchUpdateLiveStreams`` method.
            """

            http_options = _BaseLiveStreamServiceRestTransport._BaseBatchUpdateLiveStreams._get_http_options()
            request, metadata = self._interceptor.pre_batch_update_live_streams(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLiveStreamServiceRestTransport._BaseBatchUpdateLiveStreams,
                    "_BaseBatchUpdateLiveStreams__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.ads.admanager_v1.LiveStreamServiceClient.BatchUpdateLiveStreams",
                    extra={
                        "serviceName": "google.ads.admanager.v1.LiveStreamService",
                        "rpcName": "BatchUpdateLiveStreams",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                LiveStreamServiceRestTransport._BatchUpdateLiveStreams._get_response(
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
            resp = live_stream_service.BatchUpdateLiveStreamsResponse()
            pb_resp = live_stream_service.BatchUpdateLiveStreamsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_update_live_streams(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_batch_update_live_streams_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        live_stream_service.BatchUpdateLiveStreamsResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.LiveStreamServiceClient.batch_update_live_streams",
                    extra={
                        "serviceName": "google.ads.admanager.v1.LiveStreamService",
                        "rpcName": "BatchUpdateLiveStreams",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateLiveStream(
        _BaseLiveStreamServiceRestTransport._BaseCreateLiveStream,
        LiveStreamServiceRestStub,
    ):
        def __hash__(self):
            return hash("LiveStreamServiceRestTransport.CreateLiveStream")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: live_stream_service.CreateLiveStreamRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> live_stream_messages.LiveStream:
            r"""Call the create live stream method over HTTP.

            Args:
                request (~.live_stream_service.CreateLiveStreamRequest):
                    The request object. Request object for ``CreateLiveStream`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.live_stream_messages.LiveStream:
                    A LiveStream encapsulates all the
                information necessary to enable DAI
                (Dynamic Ad Insertion) into a live video
                stream.  This includes information such
                as the start and expected end time of
                the live stream, the URL of the actual
                content for Ad Manager to pull and
                insert ads into, as well as the metadata
                necessary to generate ad requests during
                the live stream.

            """

            http_options = _BaseLiveStreamServiceRestTransport._BaseCreateLiveStream._get_http_options()
            request, metadata = self._interceptor.pre_create_live_stream(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLiveStreamServiceRestTransport._BaseCreateLiveStream,
                    "_BaseCreateLiveStream__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.ads.admanager_v1.LiveStreamServiceClient.CreateLiveStream",
                    extra={
                        "serviceName": "google.ads.admanager.v1.LiveStreamService",
                        "rpcName": "CreateLiveStream",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LiveStreamServiceRestTransport._CreateLiveStream._get_response(
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
            resp = live_stream_messages.LiveStream()
            pb_resp = live_stream_messages.LiveStream.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_live_stream(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_live_stream_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = live_stream_messages.LiveStream.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.ads.admanager_v1.LiveStreamServiceClient.create_live_stream",
                    extra={
                        "serviceName": "google.ads.admanager.v1.LiveStreamService",
                        "rpcName": "CreateLiveStream",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetLiveStream(
        _BaseLiveStreamServiceRestTransport._BaseGetLiveStream,
        LiveStreamServiceRestStub,
    ):
        def __hash__(self):
            return hash("LiveStreamServiceRestTransport.GetLiveStream")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: live_stream_service.GetLiveStreamRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> live_stream_messages.LiveStream:
            r"""Call the get live stream method over HTTP.

            Args:
                request (~.live_stream_service.GetLiveStreamRequest):
                    The request object. Request object for ``GetLiveStream`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.live_stream_messages.LiveStream:
                    A LiveStream encapsulates all the
                information necessary to enable DAI
                (Dynamic Ad Insertion) into a live video
                stream.  This includes information such
                as the start and expected end time of
                the live stream, the URL of the actual
                content for Ad Manager to pull and
                insert ads into, as well as the metadata
                necessary to generate ad requests during
                the live stream.

            """

            http_options = _BaseLiveStreamServiceRestTransport._BaseGetLiveStream._get_http_options()
            request, metadata = self._interceptor.pre_get_live_stream(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLiveStreamServiceRestTransport._BaseGetLiveStream,
                    "_BaseGetLiveStream__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.ads.admanager_v1.LiveStreamServiceClient.GetLiveStream",
                    extra={
                        "serviceName": "google.ads.admanager.v1.LiveStreamService",
                        "rpcName": "GetLiveStream",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LiveStreamServiceRestTransport._GetLiveStream._get_response(
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
            resp = live_stream_messages.LiveStream()
            pb_resp = live_stream_messages.LiveStream.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_live_stream(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_live_stream_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = live_stream_messages.LiveStream.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.ads.admanager_v1.LiveStreamServiceClient.get_live_stream",
                    extra={
                        "serviceName": "google.ads.admanager.v1.LiveStreamService",
                        "rpcName": "GetLiveStream",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListLiveStreams(
        _BaseLiveStreamServiceRestTransport._BaseListLiveStreams,
        LiveStreamServiceRestStub,
    ):
        def __hash__(self):
            return hash("LiveStreamServiceRestTransport.ListLiveStreams")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: live_stream_service.ListLiveStreamsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> live_stream_service.ListLiveStreamsResponse:
            r"""Call the list live streams method over HTTP.

            Args:
                request (~.live_stream_service.ListLiveStreamsRequest):
                    The request object. Request object for ``ListLiveStreams`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.live_stream_service.ListLiveStreamsResponse:
                    Response object for ``ListLiveStreamsRequest``
                containing matching ``LiveStream`` objects.

            """

            http_options = _BaseLiveStreamServiceRestTransport._BaseListLiveStreams._get_http_options()
            request, metadata = self._interceptor.pre_list_live_streams(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLiveStreamServiceRestTransport._BaseListLiveStreams,
                    "_BaseListLiveStreams__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.ads.admanager_v1.LiveStreamServiceClient.ListLiveStreams",
                    extra={
                        "serviceName": "google.ads.admanager.v1.LiveStreamService",
                        "rpcName": "ListLiveStreams",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LiveStreamServiceRestTransport._ListLiveStreams._get_response(
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
            resp = live_stream_service.ListLiveStreamsResponse()
            pb_resp = live_stream_service.ListLiveStreamsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_live_streams(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_live_streams_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        live_stream_service.ListLiveStreamsResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.ads.admanager_v1.LiveStreamServiceClient.list_live_streams",
                    extra={
                        "serviceName": "google.ads.admanager.v1.LiveStreamService",
                        "rpcName": "ListLiveStreams",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateLiveStream(
        _BaseLiveStreamServiceRestTransport._BaseUpdateLiveStream,
        LiveStreamServiceRestStub,
    ):
        def __hash__(self):
            return hash("LiveStreamServiceRestTransport.UpdateLiveStream")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: live_stream_service.UpdateLiveStreamRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> live_stream_messages.LiveStream:
            r"""Call the update live stream method over HTTP.

            Args:
                request (~.live_stream_service.UpdateLiveStreamRequest):
                    The request object. Request object for ``UpdateLiveStream`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.live_stream_messages.LiveStream:
                    A LiveStream encapsulates all the
                information necessary to enable DAI
                (Dynamic Ad Insertion) into a live video
                stream.  This includes information such
                as the start and expected end time of
                the live stream, the URL of the actual
                content for Ad Manager to pull and
                insert ads into, as well as the metadata
                necessary to generate ad requests during
                the live stream.

            """

            http_options = _BaseLiveStreamServiceRestTransport._BaseUpdateLiveStream._get_http_options()
            request, metadata = self._interceptor.pre_update_live_stream(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLiveStreamServiceRestTransport._BaseUpdateLiveStream,
                    "_BaseUpdateLiveStream__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.ads.admanager_v1.LiveStreamServiceClient.UpdateLiveStream",
                    extra={
                        "serviceName": "google.ads.admanager.v1.LiveStreamService",
                        "rpcName": "UpdateLiveStream",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LiveStreamServiceRestTransport._UpdateLiveStream._get_response(
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
            resp = live_stream_messages.LiveStream()
            pb_resp = live_stream_messages.LiveStream.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_live_stream(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_live_stream_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = live_stream_messages.LiveStream.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.ads.admanager_v1.LiveStreamServiceClient.update_live_stream",
                    extra={
                        "serviceName": "google.ads.admanager.v1.LiveStreamService",
                        "rpcName": "UpdateLiveStream",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def batch_activate_live_streams(
        self,
    ) -> Callable[
        [live_stream_service.BatchActivateLiveStreamsRequest],
        live_stream_service.BatchActivateLiveStreamsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchActivateLiveStreams(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def batch_archive_live_streams(
        self,
    ) -> Callable[
        [live_stream_service.BatchArchiveLiveStreamsRequest],
        live_stream_service.BatchArchiveLiveStreamsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchArchiveLiveStreams(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def batch_create_live_streams(
        self,
    ) -> Callable[
        [live_stream_service.BatchCreateLiveStreamsRequest],
        live_stream_service.BatchCreateLiveStreamsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchCreateLiveStreams(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def batch_pause_ads_live_streams(
        self,
    ) -> Callable[
        [live_stream_service.BatchPauseAdsLiveStreamsRequest],
        live_stream_service.BatchPauseAdsLiveStreamsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchPauseAdsLiveStreams(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def batch_pause_live_streams(
        self,
    ) -> Callable[
        [live_stream_service.BatchPauseLiveStreamsRequest],
        live_stream_service.BatchPauseLiveStreamsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchPauseLiveStreams(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def batch_refresh_master_playlists(
        self,
    ) -> Callable[
        [live_stream_service.BatchRefreshMasterPlaylistsRequest],
        live_stream_service.BatchRefreshMasterPlaylistsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchRefreshMasterPlaylists(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def batch_update_live_streams(
        self,
    ) -> Callable[
        [live_stream_service.BatchUpdateLiveStreamsRequest],
        live_stream_service.BatchUpdateLiveStreamsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchUpdateLiveStreams(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def create_live_stream(
        self,
    ) -> Callable[
        [live_stream_service.CreateLiveStreamRequest], live_stream_messages.LiveStream
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateLiveStream(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_live_stream(
        self,
    ) -> Callable[
        [live_stream_service.GetLiveStreamRequest], live_stream_messages.LiveStream
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetLiveStream(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_live_streams(
        self,
    ) -> Callable[
        [live_stream_service.ListLiveStreamsRequest],
        live_stream_service.ListLiveStreamsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListLiveStreams(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_live_stream(
        self,
    ) -> Callable[
        [live_stream_service.UpdateLiveStreamRequest], live_stream_messages.LiveStream
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateLiveStream(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def cancel_operation(self):
        return self._CancelOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _CancelOperation(
        _BaseLiveStreamServiceRestTransport._BaseCancelOperation,
        LiveStreamServiceRestStub,
    ):
        def __hash__(self):
            return hash("LiveStreamServiceRestTransport.CancelOperation")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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

            http_options = _BaseLiveStreamServiceRestTransport._BaseCancelOperation._get_http_options()
            request, metadata = self._interceptor.pre_cancel_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLiveStreamServiceRestTransport._BaseCancelOperation,
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
                    f"Sending request for google.ads.admanager_v1.LiveStreamServiceClient.CancelOperation",
                    extra={
                        "serviceName": "google.ads.admanager.v1.LiveStreamService",
                        "rpcName": "CancelOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LiveStreamServiceRestTransport._CancelOperation._get_response(
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
    def get_operation(self):
        return self._GetOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetOperation(
        _BaseLiveStreamServiceRestTransport._BaseGetOperation, LiveStreamServiceRestStub
    ):
        def __hash__(self):
            return hash("LiveStreamServiceRestTransport.GetOperation")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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

            http_options = _BaseLiveStreamServiceRestTransport._BaseGetOperation._get_http_options()
            request, metadata = self._interceptor.pre_get_operation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLiveStreamServiceRestTransport._BaseGetOperation,
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
                    f"Sending request for google.ads.admanager_v1.LiveStreamServiceClient.GetOperation",
                    extra={
                        "serviceName": "google.ads.admanager.v1.LiveStreamService",
                        "rpcName": "GetOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LiveStreamServiceRestTransport._GetOperation._get_response(
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
                    "Received response for google.ads.admanager_v1.LiveStreamServiceAsyncClient.GetOperation",
                    extra={
                        "serviceName": "google.ads.admanager.v1.LiveStreamService",
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


__all__ = ("LiveStreamServiceRestTransport",)
