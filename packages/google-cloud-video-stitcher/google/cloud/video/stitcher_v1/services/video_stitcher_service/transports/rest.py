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

from google.cloud.video.stitcher_v1._compat import transcode_request
from google.cloud.video.stitcher_v1.types import (
    ad_tag_details,
    cdn_keys,
    live_configs,
    sessions,
    slates,
    stitch_details,
    video_stitcher_service,
    vod_configs,
)

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseVideoStitcherServiceRestTransport

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


class VideoStitcherServiceRestInterceptor:
    """Interceptor for VideoStitcherService.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the VideoStitcherServiceRestTransport.

    .. code-block:: python
        class MyCustomVideoStitcherServiceInterceptor(VideoStitcherServiceRestInterceptor):
            def pre_create_cdn_key(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_cdn_key(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_live_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_live_config(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_live_session(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_live_session(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_slate(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_slate(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_vod_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_vod_config(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_vod_session(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_vod_session(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_cdn_key(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_cdn_key(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_live_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_live_config(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_slate(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_slate(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_vod_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_vod_config(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_cdn_key(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_cdn_key(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_live_ad_tag_detail(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_live_ad_tag_detail(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_live_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_live_config(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_live_session(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_live_session(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_slate(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_slate(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_vod_ad_tag_detail(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_vod_ad_tag_detail(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_vod_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_vod_config(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_vod_session(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_vod_session(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_vod_stitch_detail(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_vod_stitch_detail(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_cdn_keys(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_cdn_keys(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_live_ad_tag_details(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_live_ad_tag_details(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_live_configs(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_live_configs(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_slates(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_slates(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_vod_ad_tag_details(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_vod_ad_tag_details(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_vod_configs(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_vod_configs(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_vod_stitch_details(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_vod_stitch_details(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_cdn_key(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_cdn_key(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_live_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_live_config(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_slate(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_slate(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_vod_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_vod_config(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = VideoStitcherServiceRestTransport(interceptor=MyCustomVideoStitcherServiceInterceptor())
        client = VideoStitcherServiceClient(transport=transport)


    """

    def pre_create_cdn_key(
        self,
        request: video_stitcher_service.CreateCdnKeyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        video_stitcher_service.CreateCdnKeyRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_cdn_key

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VideoStitcherService server.
        """
        return request, metadata

    def post_create_cdn_key(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_cdn_key

        DEPRECATED. Please use the `post_create_cdn_key_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VideoStitcherService server but before
        it is returned to user code. This `post_create_cdn_key` interceptor runs
        before the `post_create_cdn_key_with_metadata` interceptor.
        """
        return response

    def post_create_cdn_key_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_cdn_key

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VideoStitcherService server but before it is returned to user code.

        We recommend only using this `post_create_cdn_key_with_metadata`
        interceptor in new development instead of the `post_create_cdn_key` interceptor.
        When both interceptors are used, this `post_create_cdn_key_with_metadata` interceptor runs after the
        `post_create_cdn_key` interceptor. The (possibly modified) response returned by
        `post_create_cdn_key` will be passed to
        `post_create_cdn_key_with_metadata`.
        """
        return response, metadata

    def pre_create_live_config(
        self,
        request: video_stitcher_service.CreateLiveConfigRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        video_stitcher_service.CreateLiveConfigRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_live_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VideoStitcherService server.
        """
        return request, metadata

    def post_create_live_config(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_live_config

        DEPRECATED. Please use the `post_create_live_config_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VideoStitcherService server but before
        it is returned to user code. This `post_create_live_config` interceptor runs
        before the `post_create_live_config_with_metadata` interceptor.
        """
        return response

    def post_create_live_config_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_live_config

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VideoStitcherService server but before it is returned to user code.

        We recommend only using this `post_create_live_config_with_metadata`
        interceptor in new development instead of the `post_create_live_config` interceptor.
        When both interceptors are used, this `post_create_live_config_with_metadata` interceptor runs after the
        `post_create_live_config` interceptor. The (possibly modified) response returned by
        `post_create_live_config` will be passed to
        `post_create_live_config_with_metadata`.
        """
        return response, metadata

    def pre_create_live_session(
        self,
        request: video_stitcher_service.CreateLiveSessionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        video_stitcher_service.CreateLiveSessionRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_live_session

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VideoStitcherService server.
        """
        return request, metadata

    def post_create_live_session(
        self, response: sessions.LiveSession
    ) -> sessions.LiveSession:
        """Post-rpc interceptor for create_live_session

        DEPRECATED. Please use the `post_create_live_session_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VideoStitcherService server but before
        it is returned to user code. This `post_create_live_session` interceptor runs
        before the `post_create_live_session_with_metadata` interceptor.
        """
        return response

    def post_create_live_session_with_metadata(
        self,
        response: sessions.LiveSession,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[sessions.LiveSession, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_live_session

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VideoStitcherService server but before it is returned to user code.

        We recommend only using this `post_create_live_session_with_metadata`
        interceptor in new development instead of the `post_create_live_session` interceptor.
        When both interceptors are used, this `post_create_live_session_with_metadata` interceptor runs after the
        `post_create_live_session` interceptor. The (possibly modified) response returned by
        `post_create_live_session` will be passed to
        `post_create_live_session_with_metadata`.
        """
        return response, metadata

    def pre_create_slate(
        self,
        request: video_stitcher_service.CreateSlateRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        video_stitcher_service.CreateSlateRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_slate

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VideoStitcherService server.
        """
        return request, metadata

    def post_create_slate(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_slate

        DEPRECATED. Please use the `post_create_slate_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VideoStitcherService server but before
        it is returned to user code. This `post_create_slate` interceptor runs
        before the `post_create_slate_with_metadata` interceptor.
        """
        return response

    def post_create_slate_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_slate

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VideoStitcherService server but before it is returned to user code.

        We recommend only using this `post_create_slate_with_metadata`
        interceptor in new development instead of the `post_create_slate` interceptor.
        When both interceptors are used, this `post_create_slate_with_metadata` interceptor runs after the
        `post_create_slate` interceptor. The (possibly modified) response returned by
        `post_create_slate` will be passed to
        `post_create_slate_with_metadata`.
        """
        return response, metadata

    def pre_create_vod_config(
        self,
        request: video_stitcher_service.CreateVodConfigRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        video_stitcher_service.CreateVodConfigRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_vod_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VideoStitcherService server.
        """
        return request, metadata

    def post_create_vod_config(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_vod_config

        DEPRECATED. Please use the `post_create_vod_config_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VideoStitcherService server but before
        it is returned to user code. This `post_create_vod_config` interceptor runs
        before the `post_create_vod_config_with_metadata` interceptor.
        """
        return response

    def post_create_vod_config_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_vod_config

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VideoStitcherService server but before it is returned to user code.

        We recommend only using this `post_create_vod_config_with_metadata`
        interceptor in new development instead of the `post_create_vod_config` interceptor.
        When both interceptors are used, this `post_create_vod_config_with_metadata` interceptor runs after the
        `post_create_vod_config` interceptor. The (possibly modified) response returned by
        `post_create_vod_config` will be passed to
        `post_create_vod_config_with_metadata`.
        """
        return response, metadata

    def pre_create_vod_session(
        self,
        request: video_stitcher_service.CreateVodSessionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        video_stitcher_service.CreateVodSessionRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_vod_session

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VideoStitcherService server.
        """
        return request, metadata

    def post_create_vod_session(
        self, response: sessions.VodSession
    ) -> sessions.VodSession:
        """Post-rpc interceptor for create_vod_session

        DEPRECATED. Please use the `post_create_vod_session_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VideoStitcherService server but before
        it is returned to user code. This `post_create_vod_session` interceptor runs
        before the `post_create_vod_session_with_metadata` interceptor.
        """
        return response

    def post_create_vod_session_with_metadata(
        self,
        response: sessions.VodSession,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[sessions.VodSession, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_vod_session

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VideoStitcherService server but before it is returned to user code.

        We recommend only using this `post_create_vod_session_with_metadata`
        interceptor in new development instead of the `post_create_vod_session` interceptor.
        When both interceptors are used, this `post_create_vod_session_with_metadata` interceptor runs after the
        `post_create_vod_session` interceptor. The (possibly modified) response returned by
        `post_create_vod_session` will be passed to
        `post_create_vod_session_with_metadata`.
        """
        return response, metadata

    def pre_delete_cdn_key(
        self,
        request: video_stitcher_service.DeleteCdnKeyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        video_stitcher_service.DeleteCdnKeyRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_cdn_key

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VideoStitcherService server.
        """
        return request, metadata

    def post_delete_cdn_key(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_cdn_key

        DEPRECATED. Please use the `post_delete_cdn_key_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VideoStitcherService server but before
        it is returned to user code. This `post_delete_cdn_key` interceptor runs
        before the `post_delete_cdn_key_with_metadata` interceptor.
        """
        return response

    def post_delete_cdn_key_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_cdn_key

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VideoStitcherService server but before it is returned to user code.

        We recommend only using this `post_delete_cdn_key_with_metadata`
        interceptor in new development instead of the `post_delete_cdn_key` interceptor.
        When both interceptors are used, this `post_delete_cdn_key_with_metadata` interceptor runs after the
        `post_delete_cdn_key` interceptor. The (possibly modified) response returned by
        `post_delete_cdn_key` will be passed to
        `post_delete_cdn_key_with_metadata`.
        """
        return response, metadata

    def pre_delete_live_config(
        self,
        request: video_stitcher_service.DeleteLiveConfigRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        video_stitcher_service.DeleteLiveConfigRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_live_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VideoStitcherService server.
        """
        return request, metadata

    def post_delete_live_config(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_live_config

        DEPRECATED. Please use the `post_delete_live_config_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VideoStitcherService server but before
        it is returned to user code. This `post_delete_live_config` interceptor runs
        before the `post_delete_live_config_with_metadata` interceptor.
        """
        return response

    def post_delete_live_config_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_live_config

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VideoStitcherService server but before it is returned to user code.

        We recommend only using this `post_delete_live_config_with_metadata`
        interceptor in new development instead of the `post_delete_live_config` interceptor.
        When both interceptors are used, this `post_delete_live_config_with_metadata` interceptor runs after the
        `post_delete_live_config` interceptor. The (possibly modified) response returned by
        `post_delete_live_config` will be passed to
        `post_delete_live_config_with_metadata`.
        """
        return response, metadata

    def pre_delete_slate(
        self,
        request: video_stitcher_service.DeleteSlateRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        video_stitcher_service.DeleteSlateRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_slate

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VideoStitcherService server.
        """
        return request, metadata

    def post_delete_slate(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_slate

        DEPRECATED. Please use the `post_delete_slate_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VideoStitcherService server but before
        it is returned to user code. This `post_delete_slate` interceptor runs
        before the `post_delete_slate_with_metadata` interceptor.
        """
        return response

    def post_delete_slate_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_slate

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VideoStitcherService server but before it is returned to user code.

        We recommend only using this `post_delete_slate_with_metadata`
        interceptor in new development instead of the `post_delete_slate` interceptor.
        When both interceptors are used, this `post_delete_slate_with_metadata` interceptor runs after the
        `post_delete_slate` interceptor. The (possibly modified) response returned by
        `post_delete_slate` will be passed to
        `post_delete_slate_with_metadata`.
        """
        return response, metadata

    def pre_delete_vod_config(
        self,
        request: video_stitcher_service.DeleteVodConfigRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        video_stitcher_service.DeleteVodConfigRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_vod_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VideoStitcherService server.
        """
        return request, metadata

    def post_delete_vod_config(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_vod_config

        DEPRECATED. Please use the `post_delete_vod_config_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VideoStitcherService server but before
        it is returned to user code. This `post_delete_vod_config` interceptor runs
        before the `post_delete_vod_config_with_metadata` interceptor.
        """
        return response

    def post_delete_vod_config_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_vod_config

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VideoStitcherService server but before it is returned to user code.

        We recommend only using this `post_delete_vod_config_with_metadata`
        interceptor in new development instead of the `post_delete_vod_config` interceptor.
        When both interceptors are used, this `post_delete_vod_config_with_metadata` interceptor runs after the
        `post_delete_vod_config` interceptor. The (possibly modified) response returned by
        `post_delete_vod_config` will be passed to
        `post_delete_vod_config_with_metadata`.
        """
        return response, metadata

    def pre_get_cdn_key(
        self,
        request: video_stitcher_service.GetCdnKeyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        video_stitcher_service.GetCdnKeyRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_cdn_key

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VideoStitcherService server.
        """
        return request, metadata

    def post_get_cdn_key(self, response: cdn_keys.CdnKey) -> cdn_keys.CdnKey:
        """Post-rpc interceptor for get_cdn_key

        DEPRECATED. Please use the `post_get_cdn_key_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VideoStitcherService server but before
        it is returned to user code. This `post_get_cdn_key` interceptor runs
        before the `post_get_cdn_key_with_metadata` interceptor.
        """
        return response

    def post_get_cdn_key_with_metadata(
        self,
        response: cdn_keys.CdnKey,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[cdn_keys.CdnKey, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_cdn_key

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VideoStitcherService server but before it is returned to user code.

        We recommend only using this `post_get_cdn_key_with_metadata`
        interceptor in new development instead of the `post_get_cdn_key` interceptor.
        When both interceptors are used, this `post_get_cdn_key_with_metadata` interceptor runs after the
        `post_get_cdn_key` interceptor. The (possibly modified) response returned by
        `post_get_cdn_key` will be passed to
        `post_get_cdn_key_with_metadata`.
        """
        return response, metadata

    def pre_get_live_ad_tag_detail(
        self,
        request: video_stitcher_service.GetLiveAdTagDetailRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        video_stitcher_service.GetLiveAdTagDetailRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_live_ad_tag_detail

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VideoStitcherService server.
        """
        return request, metadata

    def post_get_live_ad_tag_detail(
        self, response: ad_tag_details.LiveAdTagDetail
    ) -> ad_tag_details.LiveAdTagDetail:
        """Post-rpc interceptor for get_live_ad_tag_detail

        DEPRECATED. Please use the `post_get_live_ad_tag_detail_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VideoStitcherService server but before
        it is returned to user code. This `post_get_live_ad_tag_detail` interceptor runs
        before the `post_get_live_ad_tag_detail_with_metadata` interceptor.
        """
        return response

    def post_get_live_ad_tag_detail_with_metadata(
        self,
        response: ad_tag_details.LiveAdTagDetail,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[ad_tag_details.LiveAdTagDetail, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_live_ad_tag_detail

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VideoStitcherService server but before it is returned to user code.

        We recommend only using this `post_get_live_ad_tag_detail_with_metadata`
        interceptor in new development instead of the `post_get_live_ad_tag_detail` interceptor.
        When both interceptors are used, this `post_get_live_ad_tag_detail_with_metadata` interceptor runs after the
        `post_get_live_ad_tag_detail` interceptor. The (possibly modified) response returned by
        `post_get_live_ad_tag_detail` will be passed to
        `post_get_live_ad_tag_detail_with_metadata`.
        """
        return response, metadata

    def pre_get_live_config(
        self,
        request: video_stitcher_service.GetLiveConfigRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        video_stitcher_service.GetLiveConfigRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_live_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VideoStitcherService server.
        """
        return request, metadata

    def post_get_live_config(
        self, response: live_configs.LiveConfig
    ) -> live_configs.LiveConfig:
        """Post-rpc interceptor for get_live_config

        DEPRECATED. Please use the `post_get_live_config_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VideoStitcherService server but before
        it is returned to user code. This `post_get_live_config` interceptor runs
        before the `post_get_live_config_with_metadata` interceptor.
        """
        return response

    def post_get_live_config_with_metadata(
        self,
        response: live_configs.LiveConfig,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[live_configs.LiveConfig, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_live_config

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VideoStitcherService server but before it is returned to user code.

        We recommend only using this `post_get_live_config_with_metadata`
        interceptor in new development instead of the `post_get_live_config` interceptor.
        When both interceptors are used, this `post_get_live_config_with_metadata` interceptor runs after the
        `post_get_live_config` interceptor. The (possibly modified) response returned by
        `post_get_live_config` will be passed to
        `post_get_live_config_with_metadata`.
        """
        return response, metadata

    def pre_get_live_session(
        self,
        request: video_stitcher_service.GetLiveSessionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        video_stitcher_service.GetLiveSessionRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_live_session

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VideoStitcherService server.
        """
        return request, metadata

    def post_get_live_session(
        self, response: sessions.LiveSession
    ) -> sessions.LiveSession:
        """Post-rpc interceptor for get_live_session

        DEPRECATED. Please use the `post_get_live_session_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VideoStitcherService server but before
        it is returned to user code. This `post_get_live_session` interceptor runs
        before the `post_get_live_session_with_metadata` interceptor.
        """
        return response

    def post_get_live_session_with_metadata(
        self,
        response: sessions.LiveSession,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[sessions.LiveSession, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_live_session

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VideoStitcherService server but before it is returned to user code.

        We recommend only using this `post_get_live_session_with_metadata`
        interceptor in new development instead of the `post_get_live_session` interceptor.
        When both interceptors are used, this `post_get_live_session_with_metadata` interceptor runs after the
        `post_get_live_session` interceptor. The (possibly modified) response returned by
        `post_get_live_session` will be passed to
        `post_get_live_session_with_metadata`.
        """
        return response, metadata

    def pre_get_slate(
        self,
        request: video_stitcher_service.GetSlateRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        video_stitcher_service.GetSlateRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_slate

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VideoStitcherService server.
        """
        return request, metadata

    def post_get_slate(self, response: slates.Slate) -> slates.Slate:
        """Post-rpc interceptor for get_slate

        DEPRECATED. Please use the `post_get_slate_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VideoStitcherService server but before
        it is returned to user code. This `post_get_slate` interceptor runs
        before the `post_get_slate_with_metadata` interceptor.
        """
        return response

    def post_get_slate_with_metadata(
        self, response: slates.Slate, metadata: Sequence[Tuple[str, Union[str, bytes]]]
    ) -> Tuple[slates.Slate, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_slate

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VideoStitcherService server but before it is returned to user code.

        We recommend only using this `post_get_slate_with_metadata`
        interceptor in new development instead of the `post_get_slate` interceptor.
        When both interceptors are used, this `post_get_slate_with_metadata` interceptor runs after the
        `post_get_slate` interceptor. The (possibly modified) response returned by
        `post_get_slate` will be passed to
        `post_get_slate_with_metadata`.
        """
        return response, metadata

    def pre_get_vod_ad_tag_detail(
        self,
        request: video_stitcher_service.GetVodAdTagDetailRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        video_stitcher_service.GetVodAdTagDetailRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_vod_ad_tag_detail

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VideoStitcherService server.
        """
        return request, metadata

    def post_get_vod_ad_tag_detail(
        self, response: ad_tag_details.VodAdTagDetail
    ) -> ad_tag_details.VodAdTagDetail:
        """Post-rpc interceptor for get_vod_ad_tag_detail

        DEPRECATED. Please use the `post_get_vod_ad_tag_detail_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VideoStitcherService server but before
        it is returned to user code. This `post_get_vod_ad_tag_detail` interceptor runs
        before the `post_get_vod_ad_tag_detail_with_metadata` interceptor.
        """
        return response

    def post_get_vod_ad_tag_detail_with_metadata(
        self,
        response: ad_tag_details.VodAdTagDetail,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[ad_tag_details.VodAdTagDetail, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_vod_ad_tag_detail

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VideoStitcherService server but before it is returned to user code.

        We recommend only using this `post_get_vod_ad_tag_detail_with_metadata`
        interceptor in new development instead of the `post_get_vod_ad_tag_detail` interceptor.
        When both interceptors are used, this `post_get_vod_ad_tag_detail_with_metadata` interceptor runs after the
        `post_get_vod_ad_tag_detail` interceptor. The (possibly modified) response returned by
        `post_get_vod_ad_tag_detail` will be passed to
        `post_get_vod_ad_tag_detail_with_metadata`.
        """
        return response, metadata

    def pre_get_vod_config(
        self,
        request: video_stitcher_service.GetVodConfigRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        video_stitcher_service.GetVodConfigRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_vod_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VideoStitcherService server.
        """
        return request, metadata

    def post_get_vod_config(
        self, response: vod_configs.VodConfig
    ) -> vod_configs.VodConfig:
        """Post-rpc interceptor for get_vod_config

        DEPRECATED. Please use the `post_get_vod_config_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VideoStitcherService server but before
        it is returned to user code. This `post_get_vod_config` interceptor runs
        before the `post_get_vod_config_with_metadata` interceptor.
        """
        return response

    def post_get_vod_config_with_metadata(
        self,
        response: vod_configs.VodConfig,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[vod_configs.VodConfig, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_vod_config

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VideoStitcherService server but before it is returned to user code.

        We recommend only using this `post_get_vod_config_with_metadata`
        interceptor in new development instead of the `post_get_vod_config` interceptor.
        When both interceptors are used, this `post_get_vod_config_with_metadata` interceptor runs after the
        `post_get_vod_config` interceptor. The (possibly modified) response returned by
        `post_get_vod_config` will be passed to
        `post_get_vod_config_with_metadata`.
        """
        return response, metadata

    def pre_get_vod_session(
        self,
        request: video_stitcher_service.GetVodSessionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        video_stitcher_service.GetVodSessionRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_vod_session

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VideoStitcherService server.
        """
        return request, metadata

    def post_get_vod_session(
        self, response: sessions.VodSession
    ) -> sessions.VodSession:
        """Post-rpc interceptor for get_vod_session

        DEPRECATED. Please use the `post_get_vod_session_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VideoStitcherService server but before
        it is returned to user code. This `post_get_vod_session` interceptor runs
        before the `post_get_vod_session_with_metadata` interceptor.
        """
        return response

    def post_get_vod_session_with_metadata(
        self,
        response: sessions.VodSession,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[sessions.VodSession, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_vod_session

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VideoStitcherService server but before it is returned to user code.

        We recommend only using this `post_get_vod_session_with_metadata`
        interceptor in new development instead of the `post_get_vod_session` interceptor.
        When both interceptors are used, this `post_get_vod_session_with_metadata` interceptor runs after the
        `post_get_vod_session` interceptor. The (possibly modified) response returned by
        `post_get_vod_session` will be passed to
        `post_get_vod_session_with_metadata`.
        """
        return response, metadata

    def pre_get_vod_stitch_detail(
        self,
        request: video_stitcher_service.GetVodStitchDetailRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        video_stitcher_service.GetVodStitchDetailRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_vod_stitch_detail

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VideoStitcherService server.
        """
        return request, metadata

    def post_get_vod_stitch_detail(
        self, response: stitch_details.VodStitchDetail
    ) -> stitch_details.VodStitchDetail:
        """Post-rpc interceptor for get_vod_stitch_detail

        DEPRECATED. Please use the `post_get_vod_stitch_detail_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VideoStitcherService server but before
        it is returned to user code. This `post_get_vod_stitch_detail` interceptor runs
        before the `post_get_vod_stitch_detail_with_metadata` interceptor.
        """
        return response

    def post_get_vod_stitch_detail_with_metadata(
        self,
        response: stitch_details.VodStitchDetail,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[stitch_details.VodStitchDetail, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_vod_stitch_detail

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VideoStitcherService server but before it is returned to user code.

        We recommend only using this `post_get_vod_stitch_detail_with_metadata`
        interceptor in new development instead of the `post_get_vod_stitch_detail` interceptor.
        When both interceptors are used, this `post_get_vod_stitch_detail_with_metadata` interceptor runs after the
        `post_get_vod_stitch_detail` interceptor. The (possibly modified) response returned by
        `post_get_vod_stitch_detail` will be passed to
        `post_get_vod_stitch_detail_with_metadata`.
        """
        return response, metadata

    def pre_list_cdn_keys(
        self,
        request: video_stitcher_service.ListCdnKeysRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        video_stitcher_service.ListCdnKeysRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_cdn_keys

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VideoStitcherService server.
        """
        return request, metadata

    def post_list_cdn_keys(
        self, response: video_stitcher_service.ListCdnKeysResponse
    ) -> video_stitcher_service.ListCdnKeysResponse:
        """Post-rpc interceptor for list_cdn_keys

        DEPRECATED. Please use the `post_list_cdn_keys_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VideoStitcherService server but before
        it is returned to user code. This `post_list_cdn_keys` interceptor runs
        before the `post_list_cdn_keys_with_metadata` interceptor.
        """
        return response

    def post_list_cdn_keys_with_metadata(
        self,
        response: video_stitcher_service.ListCdnKeysResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        video_stitcher_service.ListCdnKeysResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_cdn_keys

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VideoStitcherService server but before it is returned to user code.

        We recommend only using this `post_list_cdn_keys_with_metadata`
        interceptor in new development instead of the `post_list_cdn_keys` interceptor.
        When both interceptors are used, this `post_list_cdn_keys_with_metadata` interceptor runs after the
        `post_list_cdn_keys` interceptor. The (possibly modified) response returned by
        `post_list_cdn_keys` will be passed to
        `post_list_cdn_keys_with_metadata`.
        """
        return response, metadata

    def pre_list_live_ad_tag_details(
        self,
        request: video_stitcher_service.ListLiveAdTagDetailsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        video_stitcher_service.ListLiveAdTagDetailsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_live_ad_tag_details

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VideoStitcherService server.
        """
        return request, metadata

    def post_list_live_ad_tag_details(
        self, response: video_stitcher_service.ListLiveAdTagDetailsResponse
    ) -> video_stitcher_service.ListLiveAdTagDetailsResponse:
        """Post-rpc interceptor for list_live_ad_tag_details

        DEPRECATED. Please use the `post_list_live_ad_tag_details_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VideoStitcherService server but before
        it is returned to user code. This `post_list_live_ad_tag_details` interceptor runs
        before the `post_list_live_ad_tag_details_with_metadata` interceptor.
        """
        return response

    def post_list_live_ad_tag_details_with_metadata(
        self,
        response: video_stitcher_service.ListLiveAdTagDetailsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        video_stitcher_service.ListLiveAdTagDetailsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_live_ad_tag_details

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VideoStitcherService server but before it is returned to user code.

        We recommend only using this `post_list_live_ad_tag_details_with_metadata`
        interceptor in new development instead of the `post_list_live_ad_tag_details` interceptor.
        When both interceptors are used, this `post_list_live_ad_tag_details_with_metadata` interceptor runs after the
        `post_list_live_ad_tag_details` interceptor. The (possibly modified) response returned by
        `post_list_live_ad_tag_details` will be passed to
        `post_list_live_ad_tag_details_with_metadata`.
        """
        return response, metadata

    def pre_list_live_configs(
        self,
        request: video_stitcher_service.ListLiveConfigsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        video_stitcher_service.ListLiveConfigsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_live_configs

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VideoStitcherService server.
        """
        return request, metadata

    def post_list_live_configs(
        self, response: video_stitcher_service.ListLiveConfigsResponse
    ) -> video_stitcher_service.ListLiveConfigsResponse:
        """Post-rpc interceptor for list_live_configs

        DEPRECATED. Please use the `post_list_live_configs_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VideoStitcherService server but before
        it is returned to user code. This `post_list_live_configs` interceptor runs
        before the `post_list_live_configs_with_metadata` interceptor.
        """
        return response

    def post_list_live_configs_with_metadata(
        self,
        response: video_stitcher_service.ListLiveConfigsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        video_stitcher_service.ListLiveConfigsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_live_configs

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VideoStitcherService server but before it is returned to user code.

        We recommend only using this `post_list_live_configs_with_metadata`
        interceptor in new development instead of the `post_list_live_configs` interceptor.
        When both interceptors are used, this `post_list_live_configs_with_metadata` interceptor runs after the
        `post_list_live_configs` interceptor. The (possibly modified) response returned by
        `post_list_live_configs` will be passed to
        `post_list_live_configs_with_metadata`.
        """
        return response, metadata

    def pre_list_slates(
        self,
        request: video_stitcher_service.ListSlatesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        video_stitcher_service.ListSlatesRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_slates

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VideoStitcherService server.
        """
        return request, metadata

    def post_list_slates(
        self, response: video_stitcher_service.ListSlatesResponse
    ) -> video_stitcher_service.ListSlatesResponse:
        """Post-rpc interceptor for list_slates

        DEPRECATED. Please use the `post_list_slates_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VideoStitcherService server but before
        it is returned to user code. This `post_list_slates` interceptor runs
        before the `post_list_slates_with_metadata` interceptor.
        """
        return response

    def post_list_slates_with_metadata(
        self,
        response: video_stitcher_service.ListSlatesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        video_stitcher_service.ListSlatesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_slates

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VideoStitcherService server but before it is returned to user code.

        We recommend only using this `post_list_slates_with_metadata`
        interceptor in new development instead of the `post_list_slates` interceptor.
        When both interceptors are used, this `post_list_slates_with_metadata` interceptor runs after the
        `post_list_slates` interceptor. The (possibly modified) response returned by
        `post_list_slates` will be passed to
        `post_list_slates_with_metadata`.
        """
        return response, metadata

    def pre_list_vod_ad_tag_details(
        self,
        request: video_stitcher_service.ListVodAdTagDetailsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        video_stitcher_service.ListVodAdTagDetailsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_vod_ad_tag_details

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VideoStitcherService server.
        """
        return request, metadata

    def post_list_vod_ad_tag_details(
        self, response: video_stitcher_service.ListVodAdTagDetailsResponse
    ) -> video_stitcher_service.ListVodAdTagDetailsResponse:
        """Post-rpc interceptor for list_vod_ad_tag_details

        DEPRECATED. Please use the `post_list_vod_ad_tag_details_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VideoStitcherService server but before
        it is returned to user code. This `post_list_vod_ad_tag_details` interceptor runs
        before the `post_list_vod_ad_tag_details_with_metadata` interceptor.
        """
        return response

    def post_list_vod_ad_tag_details_with_metadata(
        self,
        response: video_stitcher_service.ListVodAdTagDetailsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        video_stitcher_service.ListVodAdTagDetailsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_vod_ad_tag_details

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VideoStitcherService server but before it is returned to user code.

        We recommend only using this `post_list_vod_ad_tag_details_with_metadata`
        interceptor in new development instead of the `post_list_vod_ad_tag_details` interceptor.
        When both interceptors are used, this `post_list_vod_ad_tag_details_with_metadata` interceptor runs after the
        `post_list_vod_ad_tag_details` interceptor. The (possibly modified) response returned by
        `post_list_vod_ad_tag_details` will be passed to
        `post_list_vod_ad_tag_details_with_metadata`.
        """
        return response, metadata

    def pre_list_vod_configs(
        self,
        request: video_stitcher_service.ListVodConfigsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        video_stitcher_service.ListVodConfigsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_vod_configs

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VideoStitcherService server.
        """
        return request, metadata

    def post_list_vod_configs(
        self, response: video_stitcher_service.ListVodConfigsResponse
    ) -> video_stitcher_service.ListVodConfigsResponse:
        """Post-rpc interceptor for list_vod_configs

        DEPRECATED. Please use the `post_list_vod_configs_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VideoStitcherService server but before
        it is returned to user code. This `post_list_vod_configs` interceptor runs
        before the `post_list_vod_configs_with_metadata` interceptor.
        """
        return response

    def post_list_vod_configs_with_metadata(
        self,
        response: video_stitcher_service.ListVodConfigsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        video_stitcher_service.ListVodConfigsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_vod_configs

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VideoStitcherService server but before it is returned to user code.

        We recommend only using this `post_list_vod_configs_with_metadata`
        interceptor in new development instead of the `post_list_vod_configs` interceptor.
        When both interceptors are used, this `post_list_vod_configs_with_metadata` interceptor runs after the
        `post_list_vod_configs` interceptor. The (possibly modified) response returned by
        `post_list_vod_configs` will be passed to
        `post_list_vod_configs_with_metadata`.
        """
        return response, metadata

    def pre_list_vod_stitch_details(
        self,
        request: video_stitcher_service.ListVodStitchDetailsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        video_stitcher_service.ListVodStitchDetailsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_vod_stitch_details

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VideoStitcherService server.
        """
        return request, metadata

    def post_list_vod_stitch_details(
        self, response: video_stitcher_service.ListVodStitchDetailsResponse
    ) -> video_stitcher_service.ListVodStitchDetailsResponse:
        """Post-rpc interceptor for list_vod_stitch_details

        DEPRECATED. Please use the `post_list_vod_stitch_details_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VideoStitcherService server but before
        it is returned to user code. This `post_list_vod_stitch_details` interceptor runs
        before the `post_list_vod_stitch_details_with_metadata` interceptor.
        """
        return response

    def post_list_vod_stitch_details_with_metadata(
        self,
        response: video_stitcher_service.ListVodStitchDetailsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        video_stitcher_service.ListVodStitchDetailsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_vod_stitch_details

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VideoStitcherService server but before it is returned to user code.

        We recommend only using this `post_list_vod_stitch_details_with_metadata`
        interceptor in new development instead of the `post_list_vod_stitch_details` interceptor.
        When both interceptors are used, this `post_list_vod_stitch_details_with_metadata` interceptor runs after the
        `post_list_vod_stitch_details` interceptor. The (possibly modified) response returned by
        `post_list_vod_stitch_details` will be passed to
        `post_list_vod_stitch_details_with_metadata`.
        """
        return response, metadata

    def pre_update_cdn_key(
        self,
        request: video_stitcher_service.UpdateCdnKeyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        video_stitcher_service.UpdateCdnKeyRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_cdn_key

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VideoStitcherService server.
        """
        return request, metadata

    def post_update_cdn_key(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_cdn_key

        DEPRECATED. Please use the `post_update_cdn_key_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VideoStitcherService server but before
        it is returned to user code. This `post_update_cdn_key` interceptor runs
        before the `post_update_cdn_key_with_metadata` interceptor.
        """
        return response

    def post_update_cdn_key_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_cdn_key

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VideoStitcherService server but before it is returned to user code.

        We recommend only using this `post_update_cdn_key_with_metadata`
        interceptor in new development instead of the `post_update_cdn_key` interceptor.
        When both interceptors are used, this `post_update_cdn_key_with_metadata` interceptor runs after the
        `post_update_cdn_key` interceptor. The (possibly modified) response returned by
        `post_update_cdn_key` will be passed to
        `post_update_cdn_key_with_metadata`.
        """
        return response, metadata

    def pre_update_live_config(
        self,
        request: video_stitcher_service.UpdateLiveConfigRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        video_stitcher_service.UpdateLiveConfigRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_live_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VideoStitcherService server.
        """
        return request, metadata

    def post_update_live_config(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_live_config

        DEPRECATED. Please use the `post_update_live_config_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VideoStitcherService server but before
        it is returned to user code. This `post_update_live_config` interceptor runs
        before the `post_update_live_config_with_metadata` interceptor.
        """
        return response

    def post_update_live_config_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_live_config

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VideoStitcherService server but before it is returned to user code.

        We recommend only using this `post_update_live_config_with_metadata`
        interceptor in new development instead of the `post_update_live_config` interceptor.
        When both interceptors are used, this `post_update_live_config_with_metadata` interceptor runs after the
        `post_update_live_config` interceptor. The (possibly modified) response returned by
        `post_update_live_config` will be passed to
        `post_update_live_config_with_metadata`.
        """
        return response, metadata

    def pre_update_slate(
        self,
        request: video_stitcher_service.UpdateSlateRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        video_stitcher_service.UpdateSlateRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_slate

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VideoStitcherService server.
        """
        return request, metadata

    def post_update_slate(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_slate

        DEPRECATED. Please use the `post_update_slate_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VideoStitcherService server but before
        it is returned to user code. This `post_update_slate` interceptor runs
        before the `post_update_slate_with_metadata` interceptor.
        """
        return response

    def post_update_slate_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_slate

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VideoStitcherService server but before it is returned to user code.

        We recommend only using this `post_update_slate_with_metadata`
        interceptor in new development instead of the `post_update_slate` interceptor.
        When both interceptors are used, this `post_update_slate_with_metadata` interceptor runs after the
        `post_update_slate` interceptor. The (possibly modified) response returned by
        `post_update_slate` will be passed to
        `post_update_slate_with_metadata`.
        """
        return response, metadata

    def pre_update_vod_config(
        self,
        request: video_stitcher_service.UpdateVodConfigRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        video_stitcher_service.UpdateVodConfigRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_vod_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VideoStitcherService server.
        """
        return request, metadata

    def post_update_vod_config(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_vod_config

        DEPRECATED. Please use the `post_update_vod_config_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VideoStitcherService server but before
        it is returned to user code. This `post_update_vod_config` interceptor runs
        before the `post_update_vod_config_with_metadata` interceptor.
        """
        return response

    def post_update_vod_config_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_vod_config

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VideoStitcherService server but before it is returned to user code.

        We recommend only using this `post_update_vod_config_with_metadata`
        interceptor in new development instead of the `post_update_vod_config` interceptor.
        When both interceptors are used, this `post_update_vod_config_with_metadata` interceptor runs after the
        `post_update_vod_config` interceptor. The (possibly modified) response returned by
        `post_update_vod_config` will be passed to
        `post_update_vod_config_with_metadata`.
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
        before they are sent to the VideoStitcherService server.
        """
        return request, metadata

    def post_cancel_operation(self, response: None) -> None:
        """Post-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the response
        after it is returned by the VideoStitcherService server but before
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
        before they are sent to the VideoStitcherService server.
        """
        return request, metadata

    def post_delete_operation(self, response: None) -> None:
        """Post-rpc interceptor for delete_operation

        Override in a subclass to manipulate the response
        after it is returned by the VideoStitcherService server but before
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
        before they are sent to the VideoStitcherService server.
        """
        return request, metadata

    def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the VideoStitcherService server but before
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
        before they are sent to the VideoStitcherService server.
        """
        return request, metadata

    def post_list_operations(
        self, response: operations_pb2.ListOperationsResponse
    ) -> operations_pb2.ListOperationsResponse:
        """Post-rpc interceptor for list_operations

        Override in a subclass to manipulate the response
        after it is returned by the VideoStitcherService server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class VideoStitcherServiceRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: VideoStitcherServiceRestInterceptor


class VideoStitcherServiceRestTransport(_BaseVideoStitcherServiceRestTransport):
    """REST backend synchronous transport for VideoStitcherService.

    Video-On-Demand content stitching API allows you to insert
    ads into (VoD) video on demand files. You will be able to render
    custom scrubber bars with highlighted ads, enforce ad policies,
    allow seamless playback and tracking on native players and
    monetize content with any standard VMAP compliant ad server.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "videostitcher.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[VideoStitcherServiceRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'videostitcher.googleapis.com').
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
            interceptor (Optional[VideoStitcherServiceRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or VideoStitcherServiceRestInterceptor()
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

    class _CreateCdnKey(
        _BaseVideoStitcherServiceRestTransport._BaseCreateCdnKey,
        VideoStitcherServiceRestStub,
    ):
        def __hash__(self):
            return hash("VideoStitcherServiceRestTransport.CreateCdnKey")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: video_stitcher_service.CreateCdnKeyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create cdn key method over HTTP.

            Args:
                request (~.video_stitcher_service.CreateCdnKeyRequest):
                    The request object. Request message for
                VideoStitcherService.createCdnKey.
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

            http_options = _BaseVideoStitcherServiceRestTransport._BaseCreateCdnKey._get_http_options()
            request, metadata = self._interceptor.pre_create_cdn_key(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVideoStitcherServiceRestTransport._BaseCreateCdnKey,
                    "_BaseCreateCdnKey__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.video.stitcher_v1.VideoStitcherServiceClient.CreateCdnKey",
                    extra={
                        "serviceName": "google.cloud.video.stitcher.v1.VideoStitcherService",
                        "rpcName": "CreateCdnKey",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VideoStitcherServiceRestTransport._CreateCdnKey._get_response(
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

            resp = self._interceptor.post_create_cdn_key(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_cdn_key_with_metadata(
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
                    "Received response for google.cloud.video.stitcher_v1.VideoStitcherServiceClient.create_cdn_key",
                    extra={
                        "serviceName": "google.cloud.video.stitcher.v1.VideoStitcherService",
                        "rpcName": "CreateCdnKey",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateLiveConfig(
        _BaseVideoStitcherServiceRestTransport._BaseCreateLiveConfig,
        VideoStitcherServiceRestStub,
    ):
        def __hash__(self):
            return hash("VideoStitcherServiceRestTransport.CreateLiveConfig")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: video_stitcher_service.CreateLiveConfigRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create live config method over HTTP.

            Args:
                request (~.video_stitcher_service.CreateLiveConfigRequest):
                    The request object. Request message for
                VideoStitcherService.createLiveConfig
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

            http_options = _BaseVideoStitcherServiceRestTransport._BaseCreateLiveConfig._get_http_options()
            request, metadata = self._interceptor.pre_create_live_config(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVideoStitcherServiceRestTransport._BaseCreateLiveConfig,
                    "_BaseCreateLiveConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.video.stitcher_v1.VideoStitcherServiceClient.CreateLiveConfig",
                    extra={
                        "serviceName": "google.cloud.video.stitcher.v1.VideoStitcherService",
                        "rpcName": "CreateLiveConfig",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                VideoStitcherServiceRestTransport._CreateLiveConfig._get_response(
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

            resp = self._interceptor.post_create_live_config(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_live_config_with_metadata(
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
                    "Received response for google.cloud.video.stitcher_v1.VideoStitcherServiceClient.create_live_config",
                    extra={
                        "serviceName": "google.cloud.video.stitcher.v1.VideoStitcherService",
                        "rpcName": "CreateLiveConfig",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateLiveSession(
        _BaseVideoStitcherServiceRestTransport._BaseCreateLiveSession,
        VideoStitcherServiceRestStub,
    ):
        def __hash__(self):
            return hash("VideoStitcherServiceRestTransport.CreateLiveSession")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: video_stitcher_service.CreateLiveSessionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> sessions.LiveSession:
            r"""Call the create live session method over HTTP.

            Args:
                request (~.video_stitcher_service.CreateLiveSessionRequest):
                    The request object. Request message for
                VideoStitcherService.createLiveSession.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.sessions.LiveSession:
                    Metadata for a live session. The
                session expires 5 minutes after the
                client stops fetching the session's
                playlists.

            """

            http_options = _BaseVideoStitcherServiceRestTransport._BaseCreateLiveSession._get_http_options()
            request, metadata = self._interceptor.pre_create_live_session(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVideoStitcherServiceRestTransport._BaseCreateLiveSession,
                    "_BaseCreateLiveSession__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.video.stitcher_v1.VideoStitcherServiceClient.CreateLiveSession",
                    extra={
                        "serviceName": "google.cloud.video.stitcher.v1.VideoStitcherService",
                        "rpcName": "CreateLiveSession",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                VideoStitcherServiceRestTransport._CreateLiveSession._get_response(
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
            resp = sessions.LiveSession()
            pb_resp = sessions.LiveSession.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_live_session(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_live_session_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = sessions.LiveSession.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.video.stitcher_v1.VideoStitcherServiceClient.create_live_session",
                    extra={
                        "serviceName": "google.cloud.video.stitcher.v1.VideoStitcherService",
                        "rpcName": "CreateLiveSession",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateSlate(
        _BaseVideoStitcherServiceRestTransport._BaseCreateSlate,
        VideoStitcherServiceRestStub,
    ):
        def __hash__(self):
            return hash("VideoStitcherServiceRestTransport.CreateSlate")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: video_stitcher_service.CreateSlateRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create slate method over HTTP.

            Args:
                request (~.video_stitcher_service.CreateSlateRequest):
                    The request object. Request message for
                VideoStitcherService.createSlate.
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

            http_options = _BaseVideoStitcherServiceRestTransport._BaseCreateSlate._get_http_options()
            request, metadata = self._interceptor.pre_create_slate(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVideoStitcherServiceRestTransport._BaseCreateSlate,
                    "_BaseCreateSlate__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.video.stitcher_v1.VideoStitcherServiceClient.CreateSlate",
                    extra={
                        "serviceName": "google.cloud.video.stitcher.v1.VideoStitcherService",
                        "rpcName": "CreateSlate",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VideoStitcherServiceRestTransport._CreateSlate._get_response(
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

            resp = self._interceptor.post_create_slate(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_slate_with_metadata(
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
                    "Received response for google.cloud.video.stitcher_v1.VideoStitcherServiceClient.create_slate",
                    extra={
                        "serviceName": "google.cloud.video.stitcher.v1.VideoStitcherService",
                        "rpcName": "CreateSlate",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateVodConfig(
        _BaseVideoStitcherServiceRestTransport._BaseCreateVodConfig,
        VideoStitcherServiceRestStub,
    ):
        def __hash__(self):
            return hash("VideoStitcherServiceRestTransport.CreateVodConfig")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: video_stitcher_service.CreateVodConfigRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create vod config method over HTTP.

            Args:
                request (~.video_stitcher_service.CreateVodConfigRequest):
                    The request object. Request message for
                VideoStitcherService.createVodConfig
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

            http_options = _BaseVideoStitcherServiceRestTransport._BaseCreateVodConfig._get_http_options()
            request, metadata = self._interceptor.pre_create_vod_config(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVideoStitcherServiceRestTransport._BaseCreateVodConfig,
                    "_BaseCreateVodConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.video.stitcher_v1.VideoStitcherServiceClient.CreateVodConfig",
                    extra={
                        "serviceName": "google.cloud.video.stitcher.v1.VideoStitcherService",
                        "rpcName": "CreateVodConfig",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VideoStitcherServiceRestTransport._CreateVodConfig._get_response(
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

            resp = self._interceptor.post_create_vod_config(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_vod_config_with_metadata(
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
                    "Received response for google.cloud.video.stitcher_v1.VideoStitcherServiceClient.create_vod_config",
                    extra={
                        "serviceName": "google.cloud.video.stitcher.v1.VideoStitcherService",
                        "rpcName": "CreateVodConfig",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateVodSession(
        _BaseVideoStitcherServiceRestTransport._BaseCreateVodSession,
        VideoStitcherServiceRestStub,
    ):
        def __hash__(self):
            return hash("VideoStitcherServiceRestTransport.CreateVodSession")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: video_stitcher_service.CreateVodSessionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> sessions.VodSession:
            r"""Call the create vod session method over HTTP.

            Args:
                request (~.video_stitcher_service.CreateVodSessionRequest):
                    The request object. Request message for
                VideoStitcherService.createVodSession
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.sessions.VodSession:
                    Metadata for a VOD session. The
                session expires 4 hours after its
                creation.

            """

            http_options = _BaseVideoStitcherServiceRestTransport._BaseCreateVodSession._get_http_options()
            request, metadata = self._interceptor.pre_create_vod_session(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVideoStitcherServiceRestTransport._BaseCreateVodSession,
                    "_BaseCreateVodSession__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.video.stitcher_v1.VideoStitcherServiceClient.CreateVodSession",
                    extra={
                        "serviceName": "google.cloud.video.stitcher.v1.VideoStitcherService",
                        "rpcName": "CreateVodSession",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                VideoStitcherServiceRestTransport._CreateVodSession._get_response(
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
            resp = sessions.VodSession()
            pb_resp = sessions.VodSession.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_vod_session(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_vod_session_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = sessions.VodSession.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.video.stitcher_v1.VideoStitcherServiceClient.create_vod_session",
                    extra={
                        "serviceName": "google.cloud.video.stitcher.v1.VideoStitcherService",
                        "rpcName": "CreateVodSession",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteCdnKey(
        _BaseVideoStitcherServiceRestTransport._BaseDeleteCdnKey,
        VideoStitcherServiceRestStub,
    ):
        def __hash__(self):
            return hash("VideoStitcherServiceRestTransport.DeleteCdnKey")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: video_stitcher_service.DeleteCdnKeyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete cdn key method over HTTP.

            Args:
                request (~.video_stitcher_service.DeleteCdnKeyRequest):
                    The request object. Request message for
                VideoStitcherService.deleteCdnKey.
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

            http_options = _BaseVideoStitcherServiceRestTransport._BaseDeleteCdnKey._get_http_options()
            request, metadata = self._interceptor.pre_delete_cdn_key(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVideoStitcherServiceRestTransport._BaseDeleteCdnKey,
                    "_BaseDeleteCdnKey__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.video.stitcher_v1.VideoStitcherServiceClient.DeleteCdnKey",
                    extra={
                        "serviceName": "google.cloud.video.stitcher.v1.VideoStitcherService",
                        "rpcName": "DeleteCdnKey",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VideoStitcherServiceRestTransport._DeleteCdnKey._get_response(
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

            resp = self._interceptor.post_delete_cdn_key(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_cdn_key_with_metadata(
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
                    "Received response for google.cloud.video.stitcher_v1.VideoStitcherServiceClient.delete_cdn_key",
                    extra={
                        "serviceName": "google.cloud.video.stitcher.v1.VideoStitcherService",
                        "rpcName": "DeleteCdnKey",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteLiveConfig(
        _BaseVideoStitcherServiceRestTransport._BaseDeleteLiveConfig,
        VideoStitcherServiceRestStub,
    ):
        def __hash__(self):
            return hash("VideoStitcherServiceRestTransport.DeleteLiveConfig")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: video_stitcher_service.DeleteLiveConfigRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete live config method over HTTP.

            Args:
                request (~.video_stitcher_service.DeleteLiveConfigRequest):
                    The request object. Request message for
                VideoStitcherService.deleteLiveConfig.
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

            http_options = _BaseVideoStitcherServiceRestTransport._BaseDeleteLiveConfig._get_http_options()
            request, metadata = self._interceptor.pre_delete_live_config(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVideoStitcherServiceRestTransport._BaseDeleteLiveConfig,
                    "_BaseDeleteLiveConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.video.stitcher_v1.VideoStitcherServiceClient.DeleteLiveConfig",
                    extra={
                        "serviceName": "google.cloud.video.stitcher.v1.VideoStitcherService",
                        "rpcName": "DeleteLiveConfig",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                VideoStitcherServiceRestTransport._DeleteLiveConfig._get_response(
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

            resp = self._interceptor.post_delete_live_config(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_live_config_with_metadata(
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
                    "Received response for google.cloud.video.stitcher_v1.VideoStitcherServiceClient.delete_live_config",
                    extra={
                        "serviceName": "google.cloud.video.stitcher.v1.VideoStitcherService",
                        "rpcName": "DeleteLiveConfig",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteSlate(
        _BaseVideoStitcherServiceRestTransport._BaseDeleteSlate,
        VideoStitcherServiceRestStub,
    ):
        def __hash__(self):
            return hash("VideoStitcherServiceRestTransport.DeleteSlate")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: video_stitcher_service.DeleteSlateRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete slate method over HTTP.

            Args:
                request (~.video_stitcher_service.DeleteSlateRequest):
                    The request object. Request message for
                VideoStitcherService.deleteSlate.
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

            http_options = _BaseVideoStitcherServiceRestTransport._BaseDeleteSlate._get_http_options()
            request, metadata = self._interceptor.pre_delete_slate(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVideoStitcherServiceRestTransport._BaseDeleteSlate,
                    "_BaseDeleteSlate__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.video.stitcher_v1.VideoStitcherServiceClient.DeleteSlate",
                    extra={
                        "serviceName": "google.cloud.video.stitcher.v1.VideoStitcherService",
                        "rpcName": "DeleteSlate",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VideoStitcherServiceRestTransport._DeleteSlate._get_response(
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

            resp = self._interceptor.post_delete_slate(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_slate_with_metadata(
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
                    "Received response for google.cloud.video.stitcher_v1.VideoStitcherServiceClient.delete_slate",
                    extra={
                        "serviceName": "google.cloud.video.stitcher.v1.VideoStitcherService",
                        "rpcName": "DeleteSlate",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteVodConfig(
        _BaseVideoStitcherServiceRestTransport._BaseDeleteVodConfig,
        VideoStitcherServiceRestStub,
    ):
        def __hash__(self):
            return hash("VideoStitcherServiceRestTransport.DeleteVodConfig")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: video_stitcher_service.DeleteVodConfigRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete vod config method over HTTP.

            Args:
                request (~.video_stitcher_service.DeleteVodConfigRequest):
                    The request object. Request message for
                VideoStitcherService.deleteVodConfig.
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

            http_options = _BaseVideoStitcherServiceRestTransport._BaseDeleteVodConfig._get_http_options()
            request, metadata = self._interceptor.pre_delete_vod_config(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVideoStitcherServiceRestTransport._BaseDeleteVodConfig,
                    "_BaseDeleteVodConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.video.stitcher_v1.VideoStitcherServiceClient.DeleteVodConfig",
                    extra={
                        "serviceName": "google.cloud.video.stitcher.v1.VideoStitcherService",
                        "rpcName": "DeleteVodConfig",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VideoStitcherServiceRestTransport._DeleteVodConfig._get_response(
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

            resp = self._interceptor.post_delete_vod_config(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_vod_config_with_metadata(
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
                    "Received response for google.cloud.video.stitcher_v1.VideoStitcherServiceClient.delete_vod_config",
                    extra={
                        "serviceName": "google.cloud.video.stitcher.v1.VideoStitcherService",
                        "rpcName": "DeleteVodConfig",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetCdnKey(
        _BaseVideoStitcherServiceRestTransport._BaseGetCdnKey,
        VideoStitcherServiceRestStub,
    ):
        def __hash__(self):
            return hash("VideoStitcherServiceRestTransport.GetCdnKey")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: video_stitcher_service.GetCdnKeyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cdn_keys.CdnKey:
            r"""Call the get cdn key method over HTTP.

            Args:
                request (~.video_stitcher_service.GetCdnKeyRequest):
                    The request object. Request message for
                VideoStitcherService.getCdnKey.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cdn_keys.CdnKey:
                    Configuration for a CDN key. Used by
                the Video Stitcher to sign URIs for
                fetching video manifests and signing
                media segments for playback.

            """

            http_options = _BaseVideoStitcherServiceRestTransport._BaseGetCdnKey._get_http_options()
            request, metadata = self._interceptor.pre_get_cdn_key(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVideoStitcherServiceRestTransport._BaseGetCdnKey,
                    "_BaseGetCdnKey__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.video.stitcher_v1.VideoStitcherServiceClient.GetCdnKey",
                    extra={
                        "serviceName": "google.cloud.video.stitcher.v1.VideoStitcherService",
                        "rpcName": "GetCdnKey",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VideoStitcherServiceRestTransport._GetCdnKey._get_response(
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
            resp = cdn_keys.CdnKey()
            pb_resp = cdn_keys.CdnKey.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_cdn_key(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_cdn_key_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = cdn_keys.CdnKey.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.video.stitcher_v1.VideoStitcherServiceClient.get_cdn_key",
                    extra={
                        "serviceName": "google.cloud.video.stitcher.v1.VideoStitcherService",
                        "rpcName": "GetCdnKey",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetLiveAdTagDetail(
        _BaseVideoStitcherServiceRestTransport._BaseGetLiveAdTagDetail,
        VideoStitcherServiceRestStub,
    ):
        def __hash__(self):
            return hash("VideoStitcherServiceRestTransport.GetLiveAdTagDetail")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: video_stitcher_service.GetLiveAdTagDetailRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> ad_tag_details.LiveAdTagDetail:
            r"""Call the get live ad tag detail method over HTTP.

            Args:
                request (~.video_stitcher_service.GetLiveAdTagDetailRequest):
                    The request object. Request message for
                VideoStitcherService.getLiveAdTagDetail
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.ad_tag_details.LiveAdTagDetail:
                    Information related to the details
                for one ad tag. This resource is only
                available for live sessions that do not
                implement Google Ad Manager ad
                insertion.

            """

            http_options = _BaseVideoStitcherServiceRestTransport._BaseGetLiveAdTagDetail._get_http_options()
            request, metadata = self._interceptor.pre_get_live_ad_tag_detail(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVideoStitcherServiceRestTransport._BaseGetLiveAdTagDetail,
                    "_BaseGetLiveAdTagDetail__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.video.stitcher_v1.VideoStitcherServiceClient.GetLiveAdTagDetail",
                    extra={
                        "serviceName": "google.cloud.video.stitcher.v1.VideoStitcherService",
                        "rpcName": "GetLiveAdTagDetail",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                VideoStitcherServiceRestTransport._GetLiveAdTagDetail._get_response(
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
            resp = ad_tag_details.LiveAdTagDetail()
            pb_resp = ad_tag_details.LiveAdTagDetail.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_live_ad_tag_detail(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_live_ad_tag_detail_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = ad_tag_details.LiveAdTagDetail.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.video.stitcher_v1.VideoStitcherServiceClient.get_live_ad_tag_detail",
                    extra={
                        "serviceName": "google.cloud.video.stitcher.v1.VideoStitcherService",
                        "rpcName": "GetLiveAdTagDetail",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetLiveConfig(
        _BaseVideoStitcherServiceRestTransport._BaseGetLiveConfig,
        VideoStitcherServiceRestStub,
    ):
        def __hash__(self):
            return hash("VideoStitcherServiceRestTransport.GetLiveConfig")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: video_stitcher_service.GetLiveConfigRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> live_configs.LiveConfig:
            r"""Call the get live config method over HTTP.

            Args:
                request (~.video_stitcher_service.GetLiveConfigRequest):
                    The request object. Request message for
                VideoStitcherService.getLiveConfig.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.live_configs.LiveConfig:
                    Metadata for used to register live
                configs.

            """

            http_options = _BaseVideoStitcherServiceRestTransport._BaseGetLiveConfig._get_http_options()
            request, metadata = self._interceptor.pre_get_live_config(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVideoStitcherServiceRestTransport._BaseGetLiveConfig,
                    "_BaseGetLiveConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.video.stitcher_v1.VideoStitcherServiceClient.GetLiveConfig",
                    extra={
                        "serviceName": "google.cloud.video.stitcher.v1.VideoStitcherService",
                        "rpcName": "GetLiveConfig",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VideoStitcherServiceRestTransport._GetLiveConfig._get_response(
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
            resp = live_configs.LiveConfig()
            pb_resp = live_configs.LiveConfig.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_live_config(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_live_config_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = live_configs.LiveConfig.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.video.stitcher_v1.VideoStitcherServiceClient.get_live_config",
                    extra={
                        "serviceName": "google.cloud.video.stitcher.v1.VideoStitcherService",
                        "rpcName": "GetLiveConfig",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetLiveSession(
        _BaseVideoStitcherServiceRestTransport._BaseGetLiveSession,
        VideoStitcherServiceRestStub,
    ):
        def __hash__(self):
            return hash("VideoStitcherServiceRestTransport.GetLiveSession")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: video_stitcher_service.GetLiveSessionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> sessions.LiveSession:
            r"""Call the get live session method over HTTP.

            Args:
                request (~.video_stitcher_service.GetLiveSessionRequest):
                    The request object. Request message for
                VideoStitcherService.getSession.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.sessions.LiveSession:
                    Metadata for a live session. The
                session expires 5 minutes after the
                client stops fetching the session's
                playlists.

            """

            http_options = _BaseVideoStitcherServiceRestTransport._BaseGetLiveSession._get_http_options()
            request, metadata = self._interceptor.pre_get_live_session(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVideoStitcherServiceRestTransport._BaseGetLiveSession,
                    "_BaseGetLiveSession__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.video.stitcher_v1.VideoStitcherServiceClient.GetLiveSession",
                    extra={
                        "serviceName": "google.cloud.video.stitcher.v1.VideoStitcherService",
                        "rpcName": "GetLiveSession",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VideoStitcherServiceRestTransport._GetLiveSession._get_response(
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
            resp = sessions.LiveSession()
            pb_resp = sessions.LiveSession.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_live_session(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_live_session_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = sessions.LiveSession.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.video.stitcher_v1.VideoStitcherServiceClient.get_live_session",
                    extra={
                        "serviceName": "google.cloud.video.stitcher.v1.VideoStitcherService",
                        "rpcName": "GetLiveSession",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetSlate(
        _BaseVideoStitcherServiceRestTransport._BaseGetSlate,
        VideoStitcherServiceRestStub,
    ):
        def __hash__(self):
            return hash("VideoStitcherServiceRestTransport.GetSlate")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: video_stitcher_service.GetSlateRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> slates.Slate:
            r"""Call the get slate method over HTTP.

            Args:
                request (~.video_stitcher_service.GetSlateRequest):
                    The request object. Request message for
                VideoStitcherService.getSlate.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.slates.Slate:
                    Slate object
            """

            http_options = (
                _BaseVideoStitcherServiceRestTransport._BaseGetSlate._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_slate(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVideoStitcherServiceRestTransport._BaseGetSlate,
                    "_BaseGetSlate__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.video.stitcher_v1.VideoStitcherServiceClient.GetSlate",
                    extra={
                        "serviceName": "google.cloud.video.stitcher.v1.VideoStitcherService",
                        "rpcName": "GetSlate",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VideoStitcherServiceRestTransport._GetSlate._get_response(
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
            resp = slates.Slate()
            pb_resp = slates.Slate.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_slate(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_slate_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = slates.Slate.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.video.stitcher_v1.VideoStitcherServiceClient.get_slate",
                    extra={
                        "serviceName": "google.cloud.video.stitcher.v1.VideoStitcherService",
                        "rpcName": "GetSlate",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetVodAdTagDetail(
        _BaseVideoStitcherServiceRestTransport._BaseGetVodAdTagDetail,
        VideoStitcherServiceRestStub,
    ):
        def __hash__(self):
            return hash("VideoStitcherServiceRestTransport.GetVodAdTagDetail")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: video_stitcher_service.GetVodAdTagDetailRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> ad_tag_details.VodAdTagDetail:
            r"""Call the get vod ad tag detail method over HTTP.

            Args:
                request (~.video_stitcher_service.GetVodAdTagDetailRequest):
                    The request object. Request message for
                VideoStitcherService.getVodAdTagDetail
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.ad_tag_details.VodAdTagDetail:
                    Information related to the details
                for one ad tag. This resource is only
                available for VOD sessions that do not
                implement Google Ad Manager ad
                insertion.

            """

            http_options = _BaseVideoStitcherServiceRestTransport._BaseGetVodAdTagDetail._get_http_options()
            request, metadata = self._interceptor.pre_get_vod_ad_tag_detail(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVideoStitcherServiceRestTransport._BaseGetVodAdTagDetail,
                    "_BaseGetVodAdTagDetail__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.video.stitcher_v1.VideoStitcherServiceClient.GetVodAdTagDetail",
                    extra={
                        "serviceName": "google.cloud.video.stitcher.v1.VideoStitcherService",
                        "rpcName": "GetVodAdTagDetail",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                VideoStitcherServiceRestTransport._GetVodAdTagDetail._get_response(
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
            resp = ad_tag_details.VodAdTagDetail()
            pb_resp = ad_tag_details.VodAdTagDetail.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_vod_ad_tag_detail(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_vod_ad_tag_detail_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = ad_tag_details.VodAdTagDetail.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.video.stitcher_v1.VideoStitcherServiceClient.get_vod_ad_tag_detail",
                    extra={
                        "serviceName": "google.cloud.video.stitcher.v1.VideoStitcherService",
                        "rpcName": "GetVodAdTagDetail",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetVodConfig(
        _BaseVideoStitcherServiceRestTransport._BaseGetVodConfig,
        VideoStitcherServiceRestStub,
    ):
        def __hash__(self):
            return hash("VideoStitcherServiceRestTransport.GetVodConfig")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: video_stitcher_service.GetVodConfigRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> vod_configs.VodConfig:
            r"""Call the get vod config method over HTTP.

            Args:
                request (~.video_stitcher_service.GetVodConfigRequest):
                    The request object. Request message for
                VideoStitcherService.getVodConfig.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.vod_configs.VodConfig:
                    Metadata used to register VOD
                configs.

            """

            http_options = _BaseVideoStitcherServiceRestTransport._BaseGetVodConfig._get_http_options()
            request, metadata = self._interceptor.pre_get_vod_config(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVideoStitcherServiceRestTransport._BaseGetVodConfig,
                    "_BaseGetVodConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.video.stitcher_v1.VideoStitcherServiceClient.GetVodConfig",
                    extra={
                        "serviceName": "google.cloud.video.stitcher.v1.VideoStitcherService",
                        "rpcName": "GetVodConfig",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VideoStitcherServiceRestTransport._GetVodConfig._get_response(
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
            resp = vod_configs.VodConfig()
            pb_resp = vod_configs.VodConfig.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_vod_config(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_vod_config_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = vod_configs.VodConfig.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.video.stitcher_v1.VideoStitcherServiceClient.get_vod_config",
                    extra={
                        "serviceName": "google.cloud.video.stitcher.v1.VideoStitcherService",
                        "rpcName": "GetVodConfig",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetVodSession(
        _BaseVideoStitcherServiceRestTransport._BaseGetVodSession,
        VideoStitcherServiceRestStub,
    ):
        def __hash__(self):
            return hash("VideoStitcherServiceRestTransport.GetVodSession")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: video_stitcher_service.GetVodSessionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> sessions.VodSession:
            r"""Call the get vod session method over HTTP.

            Args:
                request (~.video_stitcher_service.GetVodSessionRequest):
                    The request object. Request message for
                VideoStitcherService.getVodSession
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.sessions.VodSession:
                    Metadata for a VOD session. The
                session expires 4 hours after its
                creation.

            """

            http_options = _BaseVideoStitcherServiceRestTransport._BaseGetVodSession._get_http_options()
            request, metadata = self._interceptor.pre_get_vod_session(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVideoStitcherServiceRestTransport._BaseGetVodSession,
                    "_BaseGetVodSession__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.video.stitcher_v1.VideoStitcherServiceClient.GetVodSession",
                    extra={
                        "serviceName": "google.cloud.video.stitcher.v1.VideoStitcherService",
                        "rpcName": "GetVodSession",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VideoStitcherServiceRestTransport._GetVodSession._get_response(
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
            resp = sessions.VodSession()
            pb_resp = sessions.VodSession.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_vod_session(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_vod_session_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = sessions.VodSession.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.video.stitcher_v1.VideoStitcherServiceClient.get_vod_session",
                    extra={
                        "serviceName": "google.cloud.video.stitcher.v1.VideoStitcherService",
                        "rpcName": "GetVodSession",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetVodStitchDetail(
        _BaseVideoStitcherServiceRestTransport._BaseGetVodStitchDetail,
        VideoStitcherServiceRestStub,
    ):
        def __hash__(self):
            return hash("VideoStitcherServiceRestTransport.GetVodStitchDetail")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: video_stitcher_service.GetVodStitchDetailRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> stitch_details.VodStitchDetail:
            r"""Call the get vod stitch detail method over HTTP.

            Args:
                request (~.video_stitcher_service.GetVodStitchDetailRequest):
                    The request object. Request message for
                VideoStitcherService.getVodStitchDetail.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.stitch_details.VodStitchDetail:
                    Information related to the
                interstitial of a VOD session. This
                resource is only available for VOD
                sessions that do not implement Google Ad
                Manager ad insertion.

            """

            http_options = _BaseVideoStitcherServiceRestTransport._BaseGetVodStitchDetail._get_http_options()
            request, metadata = self._interceptor.pre_get_vod_stitch_detail(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVideoStitcherServiceRestTransport._BaseGetVodStitchDetail,
                    "_BaseGetVodStitchDetail__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.video.stitcher_v1.VideoStitcherServiceClient.GetVodStitchDetail",
                    extra={
                        "serviceName": "google.cloud.video.stitcher.v1.VideoStitcherService",
                        "rpcName": "GetVodStitchDetail",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                VideoStitcherServiceRestTransport._GetVodStitchDetail._get_response(
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
            resp = stitch_details.VodStitchDetail()
            pb_resp = stitch_details.VodStitchDetail.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_vod_stitch_detail(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_vod_stitch_detail_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = stitch_details.VodStitchDetail.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.video.stitcher_v1.VideoStitcherServiceClient.get_vod_stitch_detail",
                    extra={
                        "serviceName": "google.cloud.video.stitcher.v1.VideoStitcherService",
                        "rpcName": "GetVodStitchDetail",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListCdnKeys(
        _BaseVideoStitcherServiceRestTransport._BaseListCdnKeys,
        VideoStitcherServiceRestStub,
    ):
        def __hash__(self):
            return hash("VideoStitcherServiceRestTransport.ListCdnKeys")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: video_stitcher_service.ListCdnKeysRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> video_stitcher_service.ListCdnKeysResponse:
            r"""Call the list cdn keys method over HTTP.

            Args:
                request (~.video_stitcher_service.ListCdnKeysRequest):
                    The request object. Request message for
                VideoStitcherService.listCdnKeys.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.video_stitcher_service.ListCdnKeysResponse:
                    Response message for
                VideoStitcher.ListCdnKeys.

            """

            http_options = _BaseVideoStitcherServiceRestTransport._BaseListCdnKeys._get_http_options()
            request, metadata = self._interceptor.pre_list_cdn_keys(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVideoStitcherServiceRestTransport._BaseListCdnKeys,
                    "_BaseListCdnKeys__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.video.stitcher_v1.VideoStitcherServiceClient.ListCdnKeys",
                    extra={
                        "serviceName": "google.cloud.video.stitcher.v1.VideoStitcherService",
                        "rpcName": "ListCdnKeys",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VideoStitcherServiceRestTransport._ListCdnKeys._get_response(
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
            resp = video_stitcher_service.ListCdnKeysResponse()
            pb_resp = video_stitcher_service.ListCdnKeysResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_cdn_keys(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_cdn_keys_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        video_stitcher_service.ListCdnKeysResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.video.stitcher_v1.VideoStitcherServiceClient.list_cdn_keys",
                    extra={
                        "serviceName": "google.cloud.video.stitcher.v1.VideoStitcherService",
                        "rpcName": "ListCdnKeys",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListLiveAdTagDetails(
        _BaseVideoStitcherServiceRestTransport._BaseListLiveAdTagDetails,
        VideoStitcherServiceRestStub,
    ):
        def __hash__(self):
            return hash("VideoStitcherServiceRestTransport.ListLiveAdTagDetails")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: video_stitcher_service.ListLiveAdTagDetailsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> video_stitcher_service.ListLiveAdTagDetailsResponse:
            r"""Call the list live ad tag details method over HTTP.

            Args:
                request (~.video_stitcher_service.ListLiveAdTagDetailsRequest):
                    The request object. Request message for
                VideoStitcherService.listLiveAdTagDetails.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.video_stitcher_service.ListLiveAdTagDetailsResponse:
                    Response message for
                VideoStitcherService.listLiveAdTagDetails.

            """

            http_options = _BaseVideoStitcherServiceRestTransport._BaseListLiveAdTagDetails._get_http_options()
            request, metadata = self._interceptor.pre_list_live_ad_tag_details(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVideoStitcherServiceRestTransport._BaseListLiveAdTagDetails,
                    "_BaseListLiveAdTagDetails__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.video.stitcher_v1.VideoStitcherServiceClient.ListLiveAdTagDetails",
                    extra={
                        "serviceName": "google.cloud.video.stitcher.v1.VideoStitcherService",
                        "rpcName": "ListLiveAdTagDetails",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                VideoStitcherServiceRestTransport._ListLiveAdTagDetails._get_response(
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
            resp = video_stitcher_service.ListLiveAdTagDetailsResponse()
            pb_resp = video_stitcher_service.ListLiveAdTagDetailsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_live_ad_tag_details(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_live_ad_tag_details_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        video_stitcher_service.ListLiveAdTagDetailsResponse.to_json(
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
                    "Received response for google.cloud.video.stitcher_v1.VideoStitcherServiceClient.list_live_ad_tag_details",
                    extra={
                        "serviceName": "google.cloud.video.stitcher.v1.VideoStitcherService",
                        "rpcName": "ListLiveAdTagDetails",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListLiveConfigs(
        _BaseVideoStitcherServiceRestTransport._BaseListLiveConfigs,
        VideoStitcherServiceRestStub,
    ):
        def __hash__(self):
            return hash("VideoStitcherServiceRestTransport.ListLiveConfigs")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: video_stitcher_service.ListLiveConfigsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> video_stitcher_service.ListLiveConfigsResponse:
            r"""Call the list live configs method over HTTP.

            Args:
                request (~.video_stitcher_service.ListLiveConfigsRequest):
                    The request object. Request message for
                VideoStitcherService.listLiveConfig.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.video_stitcher_service.ListLiveConfigsResponse:
                    Response message for
                VideoStitcher.ListLiveConfig.

            """

            http_options = _BaseVideoStitcherServiceRestTransport._BaseListLiveConfigs._get_http_options()
            request, metadata = self._interceptor.pre_list_live_configs(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVideoStitcherServiceRestTransport._BaseListLiveConfigs,
                    "_BaseListLiveConfigs__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.video.stitcher_v1.VideoStitcherServiceClient.ListLiveConfigs",
                    extra={
                        "serviceName": "google.cloud.video.stitcher.v1.VideoStitcherService",
                        "rpcName": "ListLiveConfigs",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VideoStitcherServiceRestTransport._ListLiveConfigs._get_response(
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
            resp = video_stitcher_service.ListLiveConfigsResponse()
            pb_resp = video_stitcher_service.ListLiveConfigsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_live_configs(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_live_configs_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        video_stitcher_service.ListLiveConfigsResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.video.stitcher_v1.VideoStitcherServiceClient.list_live_configs",
                    extra={
                        "serviceName": "google.cloud.video.stitcher.v1.VideoStitcherService",
                        "rpcName": "ListLiveConfigs",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListSlates(
        _BaseVideoStitcherServiceRestTransport._BaseListSlates,
        VideoStitcherServiceRestStub,
    ):
        def __hash__(self):
            return hash("VideoStitcherServiceRestTransport.ListSlates")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: video_stitcher_service.ListSlatesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> video_stitcher_service.ListSlatesResponse:
            r"""Call the list slates method over HTTP.

            Args:
                request (~.video_stitcher_service.ListSlatesRequest):
                    The request object. Request message for
                VideoStitcherService.listSlates.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.video_stitcher_service.ListSlatesResponse:
                    Response message for
                VideoStitcherService.listSlates.

            """

            http_options = _BaseVideoStitcherServiceRestTransport._BaseListSlates._get_http_options()
            request, metadata = self._interceptor.pre_list_slates(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVideoStitcherServiceRestTransport._BaseListSlates,
                    "_BaseListSlates__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.video.stitcher_v1.VideoStitcherServiceClient.ListSlates",
                    extra={
                        "serviceName": "google.cloud.video.stitcher.v1.VideoStitcherService",
                        "rpcName": "ListSlates",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VideoStitcherServiceRestTransport._ListSlates._get_response(
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
            resp = video_stitcher_service.ListSlatesResponse()
            pb_resp = video_stitcher_service.ListSlatesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_slates(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_slates_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        video_stitcher_service.ListSlatesResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.video.stitcher_v1.VideoStitcherServiceClient.list_slates",
                    extra={
                        "serviceName": "google.cloud.video.stitcher.v1.VideoStitcherService",
                        "rpcName": "ListSlates",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListVodAdTagDetails(
        _BaseVideoStitcherServiceRestTransport._BaseListVodAdTagDetails,
        VideoStitcherServiceRestStub,
    ):
        def __hash__(self):
            return hash("VideoStitcherServiceRestTransport.ListVodAdTagDetails")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: video_stitcher_service.ListVodAdTagDetailsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> video_stitcher_service.ListVodAdTagDetailsResponse:
            r"""Call the list vod ad tag details method over HTTP.

            Args:
                request (~.video_stitcher_service.ListVodAdTagDetailsRequest):
                    The request object. Request message for
                VideoStitcherService.listVodAdTagDetails.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.video_stitcher_service.ListVodAdTagDetailsResponse:
                    Response message for
                VideoStitcherService.listVodAdTagDetails.

            """

            http_options = _BaseVideoStitcherServiceRestTransport._BaseListVodAdTagDetails._get_http_options()
            request, metadata = self._interceptor.pre_list_vod_ad_tag_details(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVideoStitcherServiceRestTransport._BaseListVodAdTagDetails,
                    "_BaseListVodAdTagDetails__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.video.stitcher_v1.VideoStitcherServiceClient.ListVodAdTagDetails",
                    extra={
                        "serviceName": "google.cloud.video.stitcher.v1.VideoStitcherService",
                        "rpcName": "ListVodAdTagDetails",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                VideoStitcherServiceRestTransport._ListVodAdTagDetails._get_response(
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
            resp = video_stitcher_service.ListVodAdTagDetailsResponse()
            pb_resp = video_stitcher_service.ListVodAdTagDetailsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_vod_ad_tag_details(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_vod_ad_tag_details_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        video_stitcher_service.ListVodAdTagDetailsResponse.to_json(
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
                    "Received response for google.cloud.video.stitcher_v1.VideoStitcherServiceClient.list_vod_ad_tag_details",
                    extra={
                        "serviceName": "google.cloud.video.stitcher.v1.VideoStitcherService",
                        "rpcName": "ListVodAdTagDetails",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListVodConfigs(
        _BaseVideoStitcherServiceRestTransport._BaseListVodConfigs,
        VideoStitcherServiceRestStub,
    ):
        def __hash__(self):
            return hash("VideoStitcherServiceRestTransport.ListVodConfigs")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: video_stitcher_service.ListVodConfigsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> video_stitcher_service.ListVodConfigsResponse:
            r"""Call the list vod configs method over HTTP.

            Args:
                request (~.video_stitcher_service.ListVodConfigsRequest):
                    The request object. Request message for
                VideoStitcherService.listVodConfig.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.video_stitcher_service.ListVodConfigsResponse:
                    Response message for
                VideoStitcher.ListVodConfig.

            """

            http_options = _BaseVideoStitcherServiceRestTransport._BaseListVodConfigs._get_http_options()
            request, metadata = self._interceptor.pre_list_vod_configs(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVideoStitcherServiceRestTransport._BaseListVodConfigs,
                    "_BaseListVodConfigs__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.video.stitcher_v1.VideoStitcherServiceClient.ListVodConfigs",
                    extra={
                        "serviceName": "google.cloud.video.stitcher.v1.VideoStitcherService",
                        "rpcName": "ListVodConfigs",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VideoStitcherServiceRestTransport._ListVodConfigs._get_response(
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
            resp = video_stitcher_service.ListVodConfigsResponse()
            pb_resp = video_stitcher_service.ListVodConfigsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_vod_configs(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_vod_configs_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        video_stitcher_service.ListVodConfigsResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.video.stitcher_v1.VideoStitcherServiceClient.list_vod_configs",
                    extra={
                        "serviceName": "google.cloud.video.stitcher.v1.VideoStitcherService",
                        "rpcName": "ListVodConfigs",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListVodStitchDetails(
        _BaseVideoStitcherServiceRestTransport._BaseListVodStitchDetails,
        VideoStitcherServiceRestStub,
    ):
        def __hash__(self):
            return hash("VideoStitcherServiceRestTransport.ListVodStitchDetails")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: video_stitcher_service.ListVodStitchDetailsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> video_stitcher_service.ListVodStitchDetailsResponse:
            r"""Call the list vod stitch details method over HTTP.

            Args:
                request (~.video_stitcher_service.ListVodStitchDetailsRequest):
                    The request object. Request message for
                VideoStitcherService.listVodStitchDetails.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.video_stitcher_service.ListVodStitchDetailsResponse:
                    Response message for
                VideoStitcherService.listVodStitchDetails.

            """

            http_options = _BaseVideoStitcherServiceRestTransport._BaseListVodStitchDetails._get_http_options()
            request, metadata = self._interceptor.pre_list_vod_stitch_details(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVideoStitcherServiceRestTransport._BaseListVodStitchDetails,
                    "_BaseListVodStitchDetails__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.video.stitcher_v1.VideoStitcherServiceClient.ListVodStitchDetails",
                    extra={
                        "serviceName": "google.cloud.video.stitcher.v1.VideoStitcherService",
                        "rpcName": "ListVodStitchDetails",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                VideoStitcherServiceRestTransport._ListVodStitchDetails._get_response(
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
            resp = video_stitcher_service.ListVodStitchDetailsResponse()
            pb_resp = video_stitcher_service.ListVodStitchDetailsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_vod_stitch_details(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_vod_stitch_details_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        video_stitcher_service.ListVodStitchDetailsResponse.to_json(
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
                    "Received response for google.cloud.video.stitcher_v1.VideoStitcherServiceClient.list_vod_stitch_details",
                    extra={
                        "serviceName": "google.cloud.video.stitcher.v1.VideoStitcherService",
                        "rpcName": "ListVodStitchDetails",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateCdnKey(
        _BaseVideoStitcherServiceRestTransport._BaseUpdateCdnKey,
        VideoStitcherServiceRestStub,
    ):
        def __hash__(self):
            return hash("VideoStitcherServiceRestTransport.UpdateCdnKey")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: video_stitcher_service.UpdateCdnKeyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update cdn key method over HTTP.

            Args:
                request (~.video_stitcher_service.UpdateCdnKeyRequest):
                    The request object. Request message for
                VideoStitcherService.updateCdnKey.
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

            http_options = _BaseVideoStitcherServiceRestTransport._BaseUpdateCdnKey._get_http_options()
            request, metadata = self._interceptor.pre_update_cdn_key(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVideoStitcherServiceRestTransport._BaseUpdateCdnKey,
                    "_BaseUpdateCdnKey__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.video.stitcher_v1.VideoStitcherServiceClient.UpdateCdnKey",
                    extra={
                        "serviceName": "google.cloud.video.stitcher.v1.VideoStitcherService",
                        "rpcName": "UpdateCdnKey",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VideoStitcherServiceRestTransport._UpdateCdnKey._get_response(
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

            resp = self._interceptor.post_update_cdn_key(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_cdn_key_with_metadata(
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
                    "Received response for google.cloud.video.stitcher_v1.VideoStitcherServiceClient.update_cdn_key",
                    extra={
                        "serviceName": "google.cloud.video.stitcher.v1.VideoStitcherService",
                        "rpcName": "UpdateCdnKey",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateLiveConfig(
        _BaseVideoStitcherServiceRestTransport._BaseUpdateLiveConfig,
        VideoStitcherServiceRestStub,
    ):
        def __hash__(self):
            return hash("VideoStitcherServiceRestTransport.UpdateLiveConfig")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: video_stitcher_service.UpdateLiveConfigRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update live config method over HTTP.

            Args:
                request (~.video_stitcher_service.UpdateLiveConfigRequest):
                    The request object. Request message for
                VideoStitcherService.updateLiveConfig.
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

            http_options = _BaseVideoStitcherServiceRestTransport._BaseUpdateLiveConfig._get_http_options()
            request, metadata = self._interceptor.pre_update_live_config(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVideoStitcherServiceRestTransport._BaseUpdateLiveConfig,
                    "_BaseUpdateLiveConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.video.stitcher_v1.VideoStitcherServiceClient.UpdateLiveConfig",
                    extra={
                        "serviceName": "google.cloud.video.stitcher.v1.VideoStitcherService",
                        "rpcName": "UpdateLiveConfig",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                VideoStitcherServiceRestTransport._UpdateLiveConfig._get_response(
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

            resp = self._interceptor.post_update_live_config(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_live_config_with_metadata(
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
                    "Received response for google.cloud.video.stitcher_v1.VideoStitcherServiceClient.update_live_config",
                    extra={
                        "serviceName": "google.cloud.video.stitcher.v1.VideoStitcherService",
                        "rpcName": "UpdateLiveConfig",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateSlate(
        _BaseVideoStitcherServiceRestTransport._BaseUpdateSlate,
        VideoStitcherServiceRestStub,
    ):
        def __hash__(self):
            return hash("VideoStitcherServiceRestTransport.UpdateSlate")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: video_stitcher_service.UpdateSlateRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update slate method over HTTP.

            Args:
                request (~.video_stitcher_service.UpdateSlateRequest):
                    The request object. Request message for
                VideoStitcherService.updateSlate.
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

            http_options = _BaseVideoStitcherServiceRestTransport._BaseUpdateSlate._get_http_options()
            request, metadata = self._interceptor.pre_update_slate(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVideoStitcherServiceRestTransport._BaseUpdateSlate,
                    "_BaseUpdateSlate__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.video.stitcher_v1.VideoStitcherServiceClient.UpdateSlate",
                    extra={
                        "serviceName": "google.cloud.video.stitcher.v1.VideoStitcherService",
                        "rpcName": "UpdateSlate",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VideoStitcherServiceRestTransport._UpdateSlate._get_response(
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

            resp = self._interceptor.post_update_slate(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_slate_with_metadata(
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
                    "Received response for google.cloud.video.stitcher_v1.VideoStitcherServiceClient.update_slate",
                    extra={
                        "serviceName": "google.cloud.video.stitcher.v1.VideoStitcherService",
                        "rpcName": "UpdateSlate",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateVodConfig(
        _BaseVideoStitcherServiceRestTransport._BaseUpdateVodConfig,
        VideoStitcherServiceRestStub,
    ):
        def __hash__(self):
            return hash("VideoStitcherServiceRestTransport.UpdateVodConfig")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: video_stitcher_service.UpdateVodConfigRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update vod config method over HTTP.

            Args:
                request (~.video_stitcher_service.UpdateVodConfigRequest):
                    The request object. Request message for
                VideoStitcherService.updateVodConfig.
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

            http_options = _BaseVideoStitcherServiceRestTransport._BaseUpdateVodConfig._get_http_options()
            request, metadata = self._interceptor.pre_update_vod_config(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVideoStitcherServiceRestTransport._BaseUpdateVodConfig,
                    "_BaseUpdateVodConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.video.stitcher_v1.VideoStitcherServiceClient.UpdateVodConfig",
                    extra={
                        "serviceName": "google.cloud.video.stitcher.v1.VideoStitcherService",
                        "rpcName": "UpdateVodConfig",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VideoStitcherServiceRestTransport._UpdateVodConfig._get_response(
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

            resp = self._interceptor.post_update_vod_config(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_vod_config_with_metadata(
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
                    "Received response for google.cloud.video.stitcher_v1.VideoStitcherServiceClient.update_vod_config",
                    extra={
                        "serviceName": "google.cloud.video.stitcher.v1.VideoStitcherService",
                        "rpcName": "UpdateVodConfig",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def create_cdn_key(
        self,
    ) -> Callable[
        [video_stitcher_service.CreateCdnKeyRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateCdnKey(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_live_config(
        self,
    ) -> Callable[
        [video_stitcher_service.CreateLiveConfigRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateLiveConfig(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_live_session(
        self,
    ) -> Callable[
        [video_stitcher_service.CreateLiveSessionRequest], sessions.LiveSession
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateLiveSession(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_slate(
        self,
    ) -> Callable[
        [video_stitcher_service.CreateSlateRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateSlate(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_vod_config(
        self,
    ) -> Callable[
        [video_stitcher_service.CreateVodConfigRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateVodConfig(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_vod_session(
        self,
    ) -> Callable[
        [video_stitcher_service.CreateVodSessionRequest], sessions.VodSession
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateVodSession(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_cdn_key(
        self,
    ) -> Callable[
        [video_stitcher_service.DeleteCdnKeyRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteCdnKey(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_live_config(
        self,
    ) -> Callable[
        [video_stitcher_service.DeleteLiveConfigRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteLiveConfig(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_slate(
        self,
    ) -> Callable[
        [video_stitcher_service.DeleteSlateRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteSlate(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_vod_config(
        self,
    ) -> Callable[
        [video_stitcher_service.DeleteVodConfigRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteVodConfig(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_cdn_key(
        self,
    ) -> Callable[[video_stitcher_service.GetCdnKeyRequest], cdn_keys.CdnKey]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetCdnKey(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_live_ad_tag_detail(
        self,
    ) -> Callable[
        [video_stitcher_service.GetLiveAdTagDetailRequest],
        ad_tag_details.LiveAdTagDetail,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetLiveAdTagDetail(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_live_config(
        self,
    ) -> Callable[
        [video_stitcher_service.GetLiveConfigRequest], live_configs.LiveConfig
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetLiveConfig(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_live_session(
        self,
    ) -> Callable[[video_stitcher_service.GetLiveSessionRequest], sessions.LiveSession]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetLiveSession(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_slate(
        self,
    ) -> Callable[[video_stitcher_service.GetSlateRequest], slates.Slate]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetSlate(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_vod_ad_tag_detail(
        self,
    ) -> Callable[
        [video_stitcher_service.GetVodAdTagDetailRequest], ad_tag_details.VodAdTagDetail
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetVodAdTagDetail(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_vod_config(
        self,
    ) -> Callable[[video_stitcher_service.GetVodConfigRequest], vod_configs.VodConfig]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetVodConfig(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_vod_session(
        self,
    ) -> Callable[[video_stitcher_service.GetVodSessionRequest], sessions.VodSession]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetVodSession(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_vod_stitch_detail(
        self,
    ) -> Callable[
        [video_stitcher_service.GetVodStitchDetailRequest],
        stitch_details.VodStitchDetail,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetVodStitchDetail(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_cdn_keys(
        self,
    ) -> Callable[
        [video_stitcher_service.ListCdnKeysRequest],
        video_stitcher_service.ListCdnKeysResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListCdnKeys(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_live_ad_tag_details(
        self,
    ) -> Callable[
        [video_stitcher_service.ListLiveAdTagDetailsRequest],
        video_stitcher_service.ListLiveAdTagDetailsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListLiveAdTagDetails(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_live_configs(
        self,
    ) -> Callable[
        [video_stitcher_service.ListLiveConfigsRequest],
        video_stitcher_service.ListLiveConfigsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListLiveConfigs(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_slates(
        self,
    ) -> Callable[
        [video_stitcher_service.ListSlatesRequest],
        video_stitcher_service.ListSlatesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListSlates(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_vod_ad_tag_details(
        self,
    ) -> Callable[
        [video_stitcher_service.ListVodAdTagDetailsRequest],
        video_stitcher_service.ListVodAdTagDetailsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListVodAdTagDetails(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_vod_configs(
        self,
    ) -> Callable[
        [video_stitcher_service.ListVodConfigsRequest],
        video_stitcher_service.ListVodConfigsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListVodConfigs(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_vod_stitch_details(
        self,
    ) -> Callable[
        [video_stitcher_service.ListVodStitchDetailsRequest],
        video_stitcher_service.ListVodStitchDetailsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListVodStitchDetails(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_cdn_key(
        self,
    ) -> Callable[
        [video_stitcher_service.UpdateCdnKeyRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateCdnKey(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_live_config(
        self,
    ) -> Callable[
        [video_stitcher_service.UpdateLiveConfigRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateLiveConfig(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_slate(
        self,
    ) -> Callable[
        [video_stitcher_service.UpdateSlateRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateSlate(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_vod_config(
        self,
    ) -> Callable[
        [video_stitcher_service.UpdateVodConfigRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateVodConfig(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def cancel_operation(self):
        return self._CancelOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _CancelOperation(
        _BaseVideoStitcherServiceRestTransport._BaseCancelOperation,
        VideoStitcherServiceRestStub,
    ):
        def __hash__(self):
            return hash("VideoStitcherServiceRestTransport.CancelOperation")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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

            http_options = _BaseVideoStitcherServiceRestTransport._BaseCancelOperation._get_http_options()
            request, metadata = self._interceptor.pre_cancel_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVideoStitcherServiceRestTransport._BaseCancelOperation,
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
                    f"Sending request for google.cloud.video.stitcher_v1.VideoStitcherServiceClient.CancelOperation",
                    extra={
                        "serviceName": "google.cloud.video.stitcher.v1.VideoStitcherService",
                        "rpcName": "CancelOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VideoStitcherServiceRestTransport._CancelOperation._get_response(
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
        _BaseVideoStitcherServiceRestTransport._BaseDeleteOperation,
        VideoStitcherServiceRestStub,
    ):
        def __hash__(self):
            return hash("VideoStitcherServiceRestTransport.DeleteOperation")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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

            http_options = _BaseVideoStitcherServiceRestTransport._BaseDeleteOperation._get_http_options()
            request, metadata = self._interceptor.pre_delete_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVideoStitcherServiceRestTransport._BaseDeleteOperation,
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
                    f"Sending request for google.cloud.video.stitcher_v1.VideoStitcherServiceClient.DeleteOperation",
                    extra={
                        "serviceName": "google.cloud.video.stitcher.v1.VideoStitcherService",
                        "rpcName": "DeleteOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VideoStitcherServiceRestTransport._DeleteOperation._get_response(
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
        _BaseVideoStitcherServiceRestTransport._BaseGetOperation,
        VideoStitcherServiceRestStub,
    ):
        def __hash__(self):
            return hash("VideoStitcherServiceRestTransport.GetOperation")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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

            http_options = _BaseVideoStitcherServiceRestTransport._BaseGetOperation._get_http_options()
            request, metadata = self._interceptor.pre_get_operation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVideoStitcherServiceRestTransport._BaseGetOperation,
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
                    f"Sending request for google.cloud.video.stitcher_v1.VideoStitcherServiceClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.video.stitcher.v1.VideoStitcherService",
                        "rpcName": "GetOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VideoStitcherServiceRestTransport._GetOperation._get_response(
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
                    "Received response for google.cloud.video.stitcher_v1.VideoStitcherServiceAsyncClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.video.stitcher.v1.VideoStitcherService",
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
        _BaseVideoStitcherServiceRestTransport._BaseListOperations,
        VideoStitcherServiceRestStub,
    ):
        def __hash__(self):
            return hash("VideoStitcherServiceRestTransport.ListOperations")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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

            http_options = _BaseVideoStitcherServiceRestTransport._BaseListOperations._get_http_options()
            request, metadata = self._interceptor.pre_list_operations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVideoStitcherServiceRestTransport._BaseListOperations,
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
                    f"Sending request for google.cloud.video.stitcher_v1.VideoStitcherServiceClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.video.stitcher.v1.VideoStitcherService",
                        "rpcName": "ListOperations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VideoStitcherServiceRestTransport._ListOperations._get_response(
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
                    "Received response for google.cloud.video.stitcher_v1.VideoStitcherServiceAsyncClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.video.stitcher.v1.VideoStitcherService",
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


__all__ = ("VideoStitcherServiceRestTransport",)
