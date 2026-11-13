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
from google.ads.admanager_v1.types import (
    audience_segment_messages,
    audience_segment_service,
)

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseAudienceSegmentServiceRestTransport

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


class AudienceSegmentServiceRestInterceptor:
    """Interceptor for AudienceSegmentService.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the AudienceSegmentServiceRestTransport.

    .. code-block:: python
        class MyCustomAudienceSegmentServiceInterceptor(AudienceSegmentServiceRestInterceptor):
            def pre_batch_activate_audience_segments(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_activate_audience_segments(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_batch_approve_audience_segments(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_approve_audience_segments(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_batch_create_audience_segments(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_create_audience_segments(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_batch_deactivate_audience_segments(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_deactivate_audience_segments(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_batch_populate_audience_segments(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_populate_audience_segments(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_batch_reject_audience_segments(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_reject_audience_segments(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_batch_update_audience_segments(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_update_audience_segments(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_audience_segment(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_audience_segment(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_audience_segment(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_audience_segment(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_audience_segments(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_audience_segments(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_audience_segment(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_audience_segment(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = AudienceSegmentServiceRestTransport(interceptor=MyCustomAudienceSegmentServiceInterceptor())
        client = AudienceSegmentServiceClient(transport=transport)


    """

    def pre_batch_activate_audience_segments(
        self,
        request: audience_segment_service.BatchActivateAudienceSegmentsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        audience_segment_service.BatchActivateAudienceSegmentsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_activate_audience_segments

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AudienceSegmentService server.
        """
        return request, metadata

    def post_batch_activate_audience_segments(
        self, response: audience_segment_service.BatchActivateAudienceSegmentsResponse
    ) -> audience_segment_service.BatchActivateAudienceSegmentsResponse:
        """Post-rpc interceptor for batch_activate_audience_segments

        DEPRECATED. Please use the `post_batch_activate_audience_segments_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AudienceSegmentService server but before
        it is returned to user code. This `post_batch_activate_audience_segments` interceptor runs
        before the `post_batch_activate_audience_segments_with_metadata` interceptor.
        """
        return response

    def post_batch_activate_audience_segments_with_metadata(
        self,
        response: audience_segment_service.BatchActivateAudienceSegmentsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        audience_segment_service.BatchActivateAudienceSegmentsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_activate_audience_segments

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AudienceSegmentService server but before it is returned to user code.

        We recommend only using this `post_batch_activate_audience_segments_with_metadata`
        interceptor in new development instead of the `post_batch_activate_audience_segments` interceptor.
        When both interceptors are used, this `post_batch_activate_audience_segments_with_metadata` interceptor runs after the
        `post_batch_activate_audience_segments` interceptor. The (possibly modified) response returned by
        `post_batch_activate_audience_segments` will be passed to
        `post_batch_activate_audience_segments_with_metadata`.
        """
        return response, metadata

    def pre_batch_approve_audience_segments(
        self,
        request: audience_segment_service.BatchApproveAudienceSegmentsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        audience_segment_service.BatchApproveAudienceSegmentsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_approve_audience_segments

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AudienceSegmentService server.
        """
        return request, metadata

    def post_batch_approve_audience_segments(
        self, response: audience_segment_service.BatchApproveAudienceSegmentsResponse
    ) -> audience_segment_service.BatchApproveAudienceSegmentsResponse:
        """Post-rpc interceptor for batch_approve_audience_segments

        DEPRECATED. Please use the `post_batch_approve_audience_segments_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AudienceSegmentService server but before
        it is returned to user code. This `post_batch_approve_audience_segments` interceptor runs
        before the `post_batch_approve_audience_segments_with_metadata` interceptor.
        """
        return response

    def post_batch_approve_audience_segments_with_metadata(
        self,
        response: audience_segment_service.BatchApproveAudienceSegmentsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        audience_segment_service.BatchApproveAudienceSegmentsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_approve_audience_segments

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AudienceSegmentService server but before it is returned to user code.

        We recommend only using this `post_batch_approve_audience_segments_with_metadata`
        interceptor in new development instead of the `post_batch_approve_audience_segments` interceptor.
        When both interceptors are used, this `post_batch_approve_audience_segments_with_metadata` interceptor runs after the
        `post_batch_approve_audience_segments` interceptor. The (possibly modified) response returned by
        `post_batch_approve_audience_segments` will be passed to
        `post_batch_approve_audience_segments_with_metadata`.
        """
        return response, metadata

    def pre_batch_create_audience_segments(
        self,
        request: audience_segment_service.BatchCreateAudienceSegmentsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        audience_segment_service.BatchCreateAudienceSegmentsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_create_audience_segments

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AudienceSegmentService server.
        """
        return request, metadata

    def post_batch_create_audience_segments(
        self, response: audience_segment_service.BatchCreateAudienceSegmentsResponse
    ) -> audience_segment_service.BatchCreateAudienceSegmentsResponse:
        """Post-rpc interceptor for batch_create_audience_segments

        DEPRECATED. Please use the `post_batch_create_audience_segments_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AudienceSegmentService server but before
        it is returned to user code. This `post_batch_create_audience_segments` interceptor runs
        before the `post_batch_create_audience_segments_with_metadata` interceptor.
        """
        return response

    def post_batch_create_audience_segments_with_metadata(
        self,
        response: audience_segment_service.BatchCreateAudienceSegmentsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        audience_segment_service.BatchCreateAudienceSegmentsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_create_audience_segments

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AudienceSegmentService server but before it is returned to user code.

        We recommend only using this `post_batch_create_audience_segments_with_metadata`
        interceptor in new development instead of the `post_batch_create_audience_segments` interceptor.
        When both interceptors are used, this `post_batch_create_audience_segments_with_metadata` interceptor runs after the
        `post_batch_create_audience_segments` interceptor. The (possibly modified) response returned by
        `post_batch_create_audience_segments` will be passed to
        `post_batch_create_audience_segments_with_metadata`.
        """
        return response, metadata

    def pre_batch_deactivate_audience_segments(
        self,
        request: audience_segment_service.BatchDeactivateAudienceSegmentsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        audience_segment_service.BatchDeactivateAudienceSegmentsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_deactivate_audience_segments

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AudienceSegmentService server.
        """
        return request, metadata

    def post_batch_deactivate_audience_segments(
        self, response: audience_segment_service.BatchDeactivateAudienceSegmentsResponse
    ) -> audience_segment_service.BatchDeactivateAudienceSegmentsResponse:
        """Post-rpc interceptor for batch_deactivate_audience_segments

        DEPRECATED. Please use the `post_batch_deactivate_audience_segments_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AudienceSegmentService server but before
        it is returned to user code. This `post_batch_deactivate_audience_segments` interceptor runs
        before the `post_batch_deactivate_audience_segments_with_metadata` interceptor.
        """
        return response

    def post_batch_deactivate_audience_segments_with_metadata(
        self,
        response: audience_segment_service.BatchDeactivateAudienceSegmentsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        audience_segment_service.BatchDeactivateAudienceSegmentsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_deactivate_audience_segments

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AudienceSegmentService server but before it is returned to user code.

        We recommend only using this `post_batch_deactivate_audience_segments_with_metadata`
        interceptor in new development instead of the `post_batch_deactivate_audience_segments` interceptor.
        When both interceptors are used, this `post_batch_deactivate_audience_segments_with_metadata` interceptor runs after the
        `post_batch_deactivate_audience_segments` interceptor. The (possibly modified) response returned by
        `post_batch_deactivate_audience_segments` will be passed to
        `post_batch_deactivate_audience_segments_with_metadata`.
        """
        return response, metadata

    def pre_batch_populate_audience_segments(
        self,
        request: audience_segment_service.BatchPopulateAudienceSegmentsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        audience_segment_service.BatchPopulateAudienceSegmentsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_populate_audience_segments

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AudienceSegmentService server.
        """
        return request, metadata

    def post_batch_populate_audience_segments(
        self, response: audience_segment_service.BatchPopulateAudienceSegmentsResponse
    ) -> audience_segment_service.BatchPopulateAudienceSegmentsResponse:
        """Post-rpc interceptor for batch_populate_audience_segments

        DEPRECATED. Please use the `post_batch_populate_audience_segments_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AudienceSegmentService server but before
        it is returned to user code. This `post_batch_populate_audience_segments` interceptor runs
        before the `post_batch_populate_audience_segments_with_metadata` interceptor.
        """
        return response

    def post_batch_populate_audience_segments_with_metadata(
        self,
        response: audience_segment_service.BatchPopulateAudienceSegmentsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        audience_segment_service.BatchPopulateAudienceSegmentsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_populate_audience_segments

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AudienceSegmentService server but before it is returned to user code.

        We recommend only using this `post_batch_populate_audience_segments_with_metadata`
        interceptor in new development instead of the `post_batch_populate_audience_segments` interceptor.
        When both interceptors are used, this `post_batch_populate_audience_segments_with_metadata` interceptor runs after the
        `post_batch_populate_audience_segments` interceptor. The (possibly modified) response returned by
        `post_batch_populate_audience_segments` will be passed to
        `post_batch_populate_audience_segments_with_metadata`.
        """
        return response, metadata

    def pre_batch_reject_audience_segments(
        self,
        request: audience_segment_service.BatchRejectAudienceSegmentsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        audience_segment_service.BatchRejectAudienceSegmentsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_reject_audience_segments

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AudienceSegmentService server.
        """
        return request, metadata

    def post_batch_reject_audience_segments(
        self, response: audience_segment_service.BatchRejectAudienceSegmentsResponse
    ) -> audience_segment_service.BatchRejectAudienceSegmentsResponse:
        """Post-rpc interceptor for batch_reject_audience_segments

        DEPRECATED. Please use the `post_batch_reject_audience_segments_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AudienceSegmentService server but before
        it is returned to user code. This `post_batch_reject_audience_segments` interceptor runs
        before the `post_batch_reject_audience_segments_with_metadata` interceptor.
        """
        return response

    def post_batch_reject_audience_segments_with_metadata(
        self,
        response: audience_segment_service.BatchRejectAudienceSegmentsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        audience_segment_service.BatchRejectAudienceSegmentsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_reject_audience_segments

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AudienceSegmentService server but before it is returned to user code.

        We recommend only using this `post_batch_reject_audience_segments_with_metadata`
        interceptor in new development instead of the `post_batch_reject_audience_segments` interceptor.
        When both interceptors are used, this `post_batch_reject_audience_segments_with_metadata` interceptor runs after the
        `post_batch_reject_audience_segments` interceptor. The (possibly modified) response returned by
        `post_batch_reject_audience_segments` will be passed to
        `post_batch_reject_audience_segments_with_metadata`.
        """
        return response, metadata

    def pre_batch_update_audience_segments(
        self,
        request: audience_segment_service.BatchUpdateAudienceSegmentsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        audience_segment_service.BatchUpdateAudienceSegmentsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_update_audience_segments

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AudienceSegmentService server.
        """
        return request, metadata

    def post_batch_update_audience_segments(
        self, response: audience_segment_service.BatchUpdateAudienceSegmentsResponse
    ) -> audience_segment_service.BatchUpdateAudienceSegmentsResponse:
        """Post-rpc interceptor for batch_update_audience_segments

        DEPRECATED. Please use the `post_batch_update_audience_segments_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AudienceSegmentService server but before
        it is returned to user code. This `post_batch_update_audience_segments` interceptor runs
        before the `post_batch_update_audience_segments_with_metadata` interceptor.
        """
        return response

    def post_batch_update_audience_segments_with_metadata(
        self,
        response: audience_segment_service.BatchUpdateAudienceSegmentsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        audience_segment_service.BatchUpdateAudienceSegmentsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_update_audience_segments

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AudienceSegmentService server but before it is returned to user code.

        We recommend only using this `post_batch_update_audience_segments_with_metadata`
        interceptor in new development instead of the `post_batch_update_audience_segments` interceptor.
        When both interceptors are used, this `post_batch_update_audience_segments_with_metadata` interceptor runs after the
        `post_batch_update_audience_segments` interceptor. The (possibly modified) response returned by
        `post_batch_update_audience_segments` will be passed to
        `post_batch_update_audience_segments_with_metadata`.
        """
        return response, metadata

    def pre_create_audience_segment(
        self,
        request: audience_segment_service.CreateAudienceSegmentRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        audience_segment_service.CreateAudienceSegmentRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_audience_segment

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AudienceSegmentService server.
        """
        return request, metadata

    def post_create_audience_segment(
        self, response: audience_segment_messages.AudienceSegment
    ) -> audience_segment_messages.AudienceSegment:
        """Post-rpc interceptor for create_audience_segment

        DEPRECATED. Please use the `post_create_audience_segment_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AudienceSegmentService server but before
        it is returned to user code. This `post_create_audience_segment` interceptor runs
        before the `post_create_audience_segment_with_metadata` interceptor.
        """
        return response

    def post_create_audience_segment_with_metadata(
        self,
        response: audience_segment_messages.AudienceSegment,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        audience_segment_messages.AudienceSegment,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for create_audience_segment

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AudienceSegmentService server but before it is returned to user code.

        We recommend only using this `post_create_audience_segment_with_metadata`
        interceptor in new development instead of the `post_create_audience_segment` interceptor.
        When both interceptors are used, this `post_create_audience_segment_with_metadata` interceptor runs after the
        `post_create_audience_segment` interceptor. The (possibly modified) response returned by
        `post_create_audience_segment` will be passed to
        `post_create_audience_segment_with_metadata`.
        """
        return response, metadata

    def pre_get_audience_segment(
        self,
        request: audience_segment_service.GetAudienceSegmentRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        audience_segment_service.GetAudienceSegmentRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_audience_segment

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AudienceSegmentService server.
        """
        return request, metadata

    def post_get_audience_segment(
        self, response: audience_segment_messages.AudienceSegment
    ) -> audience_segment_messages.AudienceSegment:
        """Post-rpc interceptor for get_audience_segment

        DEPRECATED. Please use the `post_get_audience_segment_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AudienceSegmentService server but before
        it is returned to user code. This `post_get_audience_segment` interceptor runs
        before the `post_get_audience_segment_with_metadata` interceptor.
        """
        return response

    def post_get_audience_segment_with_metadata(
        self,
        response: audience_segment_messages.AudienceSegment,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        audience_segment_messages.AudienceSegment,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for get_audience_segment

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AudienceSegmentService server but before it is returned to user code.

        We recommend only using this `post_get_audience_segment_with_metadata`
        interceptor in new development instead of the `post_get_audience_segment` interceptor.
        When both interceptors are used, this `post_get_audience_segment_with_metadata` interceptor runs after the
        `post_get_audience_segment` interceptor. The (possibly modified) response returned by
        `post_get_audience_segment` will be passed to
        `post_get_audience_segment_with_metadata`.
        """
        return response, metadata

    def pre_list_audience_segments(
        self,
        request: audience_segment_service.ListAudienceSegmentsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        audience_segment_service.ListAudienceSegmentsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_audience_segments

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AudienceSegmentService server.
        """
        return request, metadata

    def post_list_audience_segments(
        self, response: audience_segment_service.ListAudienceSegmentsResponse
    ) -> audience_segment_service.ListAudienceSegmentsResponse:
        """Post-rpc interceptor for list_audience_segments

        DEPRECATED. Please use the `post_list_audience_segments_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AudienceSegmentService server but before
        it is returned to user code. This `post_list_audience_segments` interceptor runs
        before the `post_list_audience_segments_with_metadata` interceptor.
        """
        return response

    def post_list_audience_segments_with_metadata(
        self,
        response: audience_segment_service.ListAudienceSegmentsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        audience_segment_service.ListAudienceSegmentsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_audience_segments

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AudienceSegmentService server but before it is returned to user code.

        We recommend only using this `post_list_audience_segments_with_metadata`
        interceptor in new development instead of the `post_list_audience_segments` interceptor.
        When both interceptors are used, this `post_list_audience_segments_with_metadata` interceptor runs after the
        `post_list_audience_segments` interceptor. The (possibly modified) response returned by
        `post_list_audience_segments` will be passed to
        `post_list_audience_segments_with_metadata`.
        """
        return response, metadata

    def pre_update_audience_segment(
        self,
        request: audience_segment_service.UpdateAudienceSegmentRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        audience_segment_service.UpdateAudienceSegmentRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_audience_segment

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AudienceSegmentService server.
        """
        return request, metadata

    def post_update_audience_segment(
        self, response: audience_segment_messages.AudienceSegment
    ) -> audience_segment_messages.AudienceSegment:
        """Post-rpc interceptor for update_audience_segment

        DEPRECATED. Please use the `post_update_audience_segment_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AudienceSegmentService server but before
        it is returned to user code. This `post_update_audience_segment` interceptor runs
        before the `post_update_audience_segment_with_metadata` interceptor.
        """
        return response

    def post_update_audience_segment_with_metadata(
        self,
        response: audience_segment_messages.AudienceSegment,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        audience_segment_messages.AudienceSegment,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for update_audience_segment

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AudienceSegmentService server but before it is returned to user code.

        We recommend only using this `post_update_audience_segment_with_metadata`
        interceptor in new development instead of the `post_update_audience_segment` interceptor.
        When both interceptors are used, this `post_update_audience_segment_with_metadata` interceptor runs after the
        `post_update_audience_segment` interceptor. The (possibly modified) response returned by
        `post_update_audience_segment` will be passed to
        `post_update_audience_segment_with_metadata`.
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
        before they are sent to the AudienceSegmentService server.
        """
        return request, metadata

    def post_cancel_operation(self, response: None) -> None:
        """Post-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the response
        after it is returned by the AudienceSegmentService server but before
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
        before they are sent to the AudienceSegmentService server.
        """
        return request, metadata

    def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the AudienceSegmentService server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class AudienceSegmentServiceRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: AudienceSegmentServiceRestInterceptor


class AudienceSegmentServiceRestTransport(_BaseAudienceSegmentServiceRestTransport):
    """REST backend synchronous transport for AudienceSegmentService.

    Provides methods for handling ``AudienceSegment`` objects.

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
        interceptor: Optional[AudienceSegmentServiceRestInterceptor] = None,
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
            interceptor (Optional[AudienceSegmentServiceRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or AudienceSegmentServiceRestInterceptor()
        self._prep_wrapped_messages(client_info)

    class _BatchActivateAudienceSegments(
        _BaseAudienceSegmentServiceRestTransport._BaseBatchActivateAudienceSegments,
        AudienceSegmentServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "AudienceSegmentServiceRestTransport.BatchActivateAudienceSegments"
            )

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
            request: audience_segment_service.BatchActivateAudienceSegmentsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> audience_segment_service.BatchActivateAudienceSegmentsResponse:
            r"""Call the batch activate audience
            segments method over HTTP.

                Args:
                    request (~.audience_segment_service.BatchActivateAudienceSegmentsRequest):
                        The request object. Request message for ``BatchActivateAudienceSegments``
                    method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.audience_segment_service.BatchActivateAudienceSegmentsResponse:
                        Response message for ``BatchActivateAudienceSegments``
                    method.

            """

            http_options = _BaseAudienceSegmentServiceRestTransport._BaseBatchActivateAudienceSegments._get_http_options()
            request, metadata = self._interceptor.pre_batch_activate_audience_segments(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAudienceSegmentServiceRestTransport._BaseBatchActivateAudienceSegments,
                    "_BaseBatchActivateAudienceSegments__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.AudienceSegmentServiceClient.BatchActivateAudienceSegments",
                    extra={
                        "serviceName": "google.ads.admanager.v1.AudienceSegmentService",
                        "rpcName": "BatchActivateAudienceSegments",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AudienceSegmentServiceRestTransport._BatchActivateAudienceSegments._get_response(
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
            resp = audience_segment_service.BatchActivateAudienceSegmentsResponse()
            pb_resp = audience_segment_service.BatchActivateAudienceSegmentsResponse.pb(
                resp
            )

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_activate_audience_segments(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_batch_activate_audience_segments_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = audience_segment_service.BatchActivateAudienceSegmentsResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.AudienceSegmentServiceClient.batch_activate_audience_segments",
                    extra={
                        "serviceName": "google.ads.admanager.v1.AudienceSegmentService",
                        "rpcName": "BatchActivateAudienceSegments",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BatchApproveAudienceSegments(
        _BaseAudienceSegmentServiceRestTransport._BaseBatchApproveAudienceSegments,
        AudienceSegmentServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "AudienceSegmentServiceRestTransport.BatchApproveAudienceSegments"
            )

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
            request: audience_segment_service.BatchApproveAudienceSegmentsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> audience_segment_service.BatchApproveAudienceSegmentsResponse:
            r"""Call the batch approve audience
            segments method over HTTP.

                Args:
                    request (~.audience_segment_service.BatchApproveAudienceSegmentsRequest):
                        The request object. Request message for ``BatchApproveAudienceSegments``
                    method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.audience_segment_service.BatchApproveAudienceSegmentsResponse:
                        Response message for ``BatchApproveAudienceSegments``
                    method.

            """

            http_options = _BaseAudienceSegmentServiceRestTransport._BaseBatchApproveAudienceSegments._get_http_options()
            request, metadata = self._interceptor.pre_batch_approve_audience_segments(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAudienceSegmentServiceRestTransport._BaseBatchApproveAudienceSegments,
                    "_BaseBatchApproveAudienceSegments__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.AudienceSegmentServiceClient.BatchApproveAudienceSegments",
                    extra={
                        "serviceName": "google.ads.admanager.v1.AudienceSegmentService",
                        "rpcName": "BatchApproveAudienceSegments",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AudienceSegmentServiceRestTransport._BatchApproveAudienceSegments._get_response(
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
            resp = audience_segment_service.BatchApproveAudienceSegmentsResponse()
            pb_resp = audience_segment_service.BatchApproveAudienceSegmentsResponse.pb(
                resp
            )

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_approve_audience_segments(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_batch_approve_audience_segments_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = audience_segment_service.BatchApproveAudienceSegmentsResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.AudienceSegmentServiceClient.batch_approve_audience_segments",
                    extra={
                        "serviceName": "google.ads.admanager.v1.AudienceSegmentService",
                        "rpcName": "BatchApproveAudienceSegments",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BatchCreateAudienceSegments(
        _BaseAudienceSegmentServiceRestTransport._BaseBatchCreateAudienceSegments,
        AudienceSegmentServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "AudienceSegmentServiceRestTransport.BatchCreateAudienceSegments"
            )

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
            request: audience_segment_service.BatchCreateAudienceSegmentsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> audience_segment_service.BatchCreateAudienceSegmentsResponse:
            r"""Call the batch create audience
            segments method over HTTP.

                Args:
                    request (~.audience_segment_service.BatchCreateAudienceSegmentsRequest):
                        The request object. Request object for ``BatchCreateAudienceSegments``
                    method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.audience_segment_service.BatchCreateAudienceSegmentsResponse:
                        Response object for ``BatchCreateAudienceSegments``
                    method.

            """

            http_options = _BaseAudienceSegmentServiceRestTransport._BaseBatchCreateAudienceSegments._get_http_options()
            request, metadata = self._interceptor.pre_batch_create_audience_segments(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAudienceSegmentServiceRestTransport._BaseBatchCreateAudienceSegments,
                    "_BaseBatchCreateAudienceSegments__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.AudienceSegmentServiceClient.BatchCreateAudienceSegments",
                    extra={
                        "serviceName": "google.ads.admanager.v1.AudienceSegmentService",
                        "rpcName": "BatchCreateAudienceSegments",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AudienceSegmentServiceRestTransport._BatchCreateAudienceSegments._get_response(
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
            resp = audience_segment_service.BatchCreateAudienceSegmentsResponse()
            pb_resp = audience_segment_service.BatchCreateAudienceSegmentsResponse.pb(
                resp
            )

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_create_audience_segments(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_batch_create_audience_segments_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = audience_segment_service.BatchCreateAudienceSegmentsResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.AudienceSegmentServiceClient.batch_create_audience_segments",
                    extra={
                        "serviceName": "google.ads.admanager.v1.AudienceSegmentService",
                        "rpcName": "BatchCreateAudienceSegments",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BatchDeactivateAudienceSegments(
        _BaseAudienceSegmentServiceRestTransport._BaseBatchDeactivateAudienceSegments,
        AudienceSegmentServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "AudienceSegmentServiceRestTransport.BatchDeactivateAudienceSegments"
            )

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
            request: audience_segment_service.BatchDeactivateAudienceSegmentsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> audience_segment_service.BatchDeactivateAudienceSegmentsResponse:
            r"""Call the batch deactivate audience
            segments method over HTTP.

                Args:
                    request (~.audience_segment_service.BatchDeactivateAudienceSegmentsRequest):
                        The request object. Request message for ``BatchDeactivateAudienceSegments``
                    method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.audience_segment_service.BatchDeactivateAudienceSegmentsResponse:
                        Response message for ``BatchDeactivateAudienceSegments``
                    method.

            """

            http_options = _BaseAudienceSegmentServiceRestTransport._BaseBatchDeactivateAudienceSegments._get_http_options()
            request, metadata = (
                self._interceptor.pre_batch_deactivate_audience_segments(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAudienceSegmentServiceRestTransport._BaseBatchDeactivateAudienceSegments,
                    "_BaseBatchDeactivateAudienceSegments__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.AudienceSegmentServiceClient.BatchDeactivateAudienceSegments",
                    extra={
                        "serviceName": "google.ads.admanager.v1.AudienceSegmentService",
                        "rpcName": "BatchDeactivateAudienceSegments",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AudienceSegmentServiceRestTransport._BatchDeactivateAudienceSegments._get_response(
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
            resp = audience_segment_service.BatchDeactivateAudienceSegmentsResponse()
            pb_resp = (
                audience_segment_service.BatchDeactivateAudienceSegmentsResponse.pb(
                    resp
                )
            )

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_deactivate_audience_segments(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_batch_deactivate_audience_segments_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = audience_segment_service.BatchDeactivateAudienceSegmentsResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.AudienceSegmentServiceClient.batch_deactivate_audience_segments",
                    extra={
                        "serviceName": "google.ads.admanager.v1.AudienceSegmentService",
                        "rpcName": "BatchDeactivateAudienceSegments",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BatchPopulateAudienceSegments(
        _BaseAudienceSegmentServiceRestTransport._BaseBatchPopulateAudienceSegments,
        AudienceSegmentServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "AudienceSegmentServiceRestTransport.BatchPopulateAudienceSegments"
            )

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
            request: audience_segment_service.BatchPopulateAudienceSegmentsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> audience_segment_service.BatchPopulateAudienceSegmentsResponse:
            r"""Call the batch populate audience
            segments method over HTTP.

                Args:
                    request (~.audience_segment_service.BatchPopulateAudienceSegmentsRequest):
                        The request object. Request message for ``BatchPopulateAudienceSegments``
                    method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.audience_segment_service.BatchPopulateAudienceSegmentsResponse:
                        Response message for ``BatchPopulateAudienceSegments``
                    method.

            """

            http_options = _BaseAudienceSegmentServiceRestTransport._BaseBatchPopulateAudienceSegments._get_http_options()
            request, metadata = self._interceptor.pre_batch_populate_audience_segments(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAudienceSegmentServiceRestTransport._BaseBatchPopulateAudienceSegments,
                    "_BaseBatchPopulateAudienceSegments__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.AudienceSegmentServiceClient.BatchPopulateAudienceSegments",
                    extra={
                        "serviceName": "google.ads.admanager.v1.AudienceSegmentService",
                        "rpcName": "BatchPopulateAudienceSegments",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AudienceSegmentServiceRestTransport._BatchPopulateAudienceSegments._get_response(
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
            resp = audience_segment_service.BatchPopulateAudienceSegmentsResponse()
            pb_resp = audience_segment_service.BatchPopulateAudienceSegmentsResponse.pb(
                resp
            )

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_populate_audience_segments(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_batch_populate_audience_segments_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = audience_segment_service.BatchPopulateAudienceSegmentsResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.AudienceSegmentServiceClient.batch_populate_audience_segments",
                    extra={
                        "serviceName": "google.ads.admanager.v1.AudienceSegmentService",
                        "rpcName": "BatchPopulateAudienceSegments",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BatchRejectAudienceSegments(
        _BaseAudienceSegmentServiceRestTransport._BaseBatchRejectAudienceSegments,
        AudienceSegmentServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "AudienceSegmentServiceRestTransport.BatchRejectAudienceSegments"
            )

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
            request: audience_segment_service.BatchRejectAudienceSegmentsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> audience_segment_service.BatchRejectAudienceSegmentsResponse:
            r"""Call the batch reject audience
            segments method over HTTP.

                Args:
                    request (~.audience_segment_service.BatchRejectAudienceSegmentsRequest):
                        The request object. Request message for ``BatchRejectAudienceSegments``
                    method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.audience_segment_service.BatchRejectAudienceSegmentsResponse:
                        Response message for ``BatchRejectAudienceSegments``
                    method.

            """

            http_options = _BaseAudienceSegmentServiceRestTransport._BaseBatchRejectAudienceSegments._get_http_options()
            request, metadata = self._interceptor.pre_batch_reject_audience_segments(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAudienceSegmentServiceRestTransport._BaseBatchRejectAudienceSegments,
                    "_BaseBatchRejectAudienceSegments__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.AudienceSegmentServiceClient.BatchRejectAudienceSegments",
                    extra={
                        "serviceName": "google.ads.admanager.v1.AudienceSegmentService",
                        "rpcName": "BatchRejectAudienceSegments",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AudienceSegmentServiceRestTransport._BatchRejectAudienceSegments._get_response(
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
            resp = audience_segment_service.BatchRejectAudienceSegmentsResponse()
            pb_resp = audience_segment_service.BatchRejectAudienceSegmentsResponse.pb(
                resp
            )

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_reject_audience_segments(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_batch_reject_audience_segments_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = audience_segment_service.BatchRejectAudienceSegmentsResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.AudienceSegmentServiceClient.batch_reject_audience_segments",
                    extra={
                        "serviceName": "google.ads.admanager.v1.AudienceSegmentService",
                        "rpcName": "BatchRejectAudienceSegments",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BatchUpdateAudienceSegments(
        _BaseAudienceSegmentServiceRestTransport._BaseBatchUpdateAudienceSegments,
        AudienceSegmentServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "AudienceSegmentServiceRestTransport.BatchUpdateAudienceSegments"
            )

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
            request: audience_segment_service.BatchUpdateAudienceSegmentsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> audience_segment_service.BatchUpdateAudienceSegmentsResponse:
            r"""Call the batch update audience
            segments method over HTTP.

                Args:
                    request (~.audience_segment_service.BatchUpdateAudienceSegmentsRequest):
                        The request object. Request object for ``BatchUpdateAudienceSegments``
                    method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.audience_segment_service.BatchUpdateAudienceSegmentsResponse:
                        Response object for ``BatchUpdateAudienceSegments``
                    method.

            """

            http_options = _BaseAudienceSegmentServiceRestTransport._BaseBatchUpdateAudienceSegments._get_http_options()
            request, metadata = self._interceptor.pre_batch_update_audience_segments(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAudienceSegmentServiceRestTransport._BaseBatchUpdateAudienceSegments,
                    "_BaseBatchUpdateAudienceSegments__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.AudienceSegmentServiceClient.BatchUpdateAudienceSegments",
                    extra={
                        "serviceName": "google.ads.admanager.v1.AudienceSegmentService",
                        "rpcName": "BatchUpdateAudienceSegments",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AudienceSegmentServiceRestTransport._BatchUpdateAudienceSegments._get_response(
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
            resp = audience_segment_service.BatchUpdateAudienceSegmentsResponse()
            pb_resp = audience_segment_service.BatchUpdateAudienceSegmentsResponse.pb(
                resp
            )

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_update_audience_segments(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_batch_update_audience_segments_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = audience_segment_service.BatchUpdateAudienceSegmentsResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.AudienceSegmentServiceClient.batch_update_audience_segments",
                    extra={
                        "serviceName": "google.ads.admanager.v1.AudienceSegmentService",
                        "rpcName": "BatchUpdateAudienceSegments",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateAudienceSegment(
        _BaseAudienceSegmentServiceRestTransport._BaseCreateAudienceSegment,
        AudienceSegmentServiceRestStub,
    ):
        def __hash__(self):
            return hash("AudienceSegmentServiceRestTransport.CreateAudienceSegment")

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
            request: audience_segment_service.CreateAudienceSegmentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> audience_segment_messages.AudienceSegment:
            r"""Call the create audience segment method over HTTP.

            Args:
                request (~.audience_segment_service.CreateAudienceSegmentRequest):
                    The request object. Request object for ``CreateAudienceSegment`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.audience_segment_messages.AudienceSegment:
                    The ``AudienceSegment`` resource.
            """

            http_options = _BaseAudienceSegmentServiceRestTransport._BaseCreateAudienceSegment._get_http_options()
            request, metadata = self._interceptor.pre_create_audience_segment(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAudienceSegmentServiceRestTransport._BaseCreateAudienceSegment,
                    "_BaseCreateAudienceSegment__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.AudienceSegmentServiceClient.CreateAudienceSegment",
                    extra={
                        "serviceName": "google.ads.admanager.v1.AudienceSegmentService",
                        "rpcName": "CreateAudienceSegment",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AudienceSegmentServiceRestTransport._CreateAudienceSegment._get_response(
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
            resp = audience_segment_messages.AudienceSegment()
            pb_resp = audience_segment_messages.AudienceSegment.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_audience_segment(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_audience_segment_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        audience_segment_messages.AudienceSegment.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.ads.admanager_v1.AudienceSegmentServiceClient.create_audience_segment",
                    extra={
                        "serviceName": "google.ads.admanager.v1.AudienceSegmentService",
                        "rpcName": "CreateAudienceSegment",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetAudienceSegment(
        _BaseAudienceSegmentServiceRestTransport._BaseGetAudienceSegment,
        AudienceSegmentServiceRestStub,
    ):
        def __hash__(self):
            return hash("AudienceSegmentServiceRestTransport.GetAudienceSegment")

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
            request: audience_segment_service.GetAudienceSegmentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> audience_segment_messages.AudienceSegment:
            r"""Call the get audience segment method over HTTP.

            Args:
                request (~.audience_segment_service.GetAudienceSegmentRequest):
                    The request object. Request object for ``GetAudienceSegment`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.audience_segment_messages.AudienceSegment:
                    The ``AudienceSegment`` resource.
            """

            http_options = _BaseAudienceSegmentServiceRestTransport._BaseGetAudienceSegment._get_http_options()
            request, metadata = self._interceptor.pre_get_audience_segment(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAudienceSegmentServiceRestTransport._BaseGetAudienceSegment,
                    "_BaseGetAudienceSegment__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.AudienceSegmentServiceClient.GetAudienceSegment",
                    extra={
                        "serviceName": "google.ads.admanager.v1.AudienceSegmentService",
                        "rpcName": "GetAudienceSegment",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                AudienceSegmentServiceRestTransport._GetAudienceSegment._get_response(
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
            resp = audience_segment_messages.AudienceSegment()
            pb_resp = audience_segment_messages.AudienceSegment.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_audience_segment(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_audience_segment_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        audience_segment_messages.AudienceSegment.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.ads.admanager_v1.AudienceSegmentServiceClient.get_audience_segment",
                    extra={
                        "serviceName": "google.ads.admanager.v1.AudienceSegmentService",
                        "rpcName": "GetAudienceSegment",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListAudienceSegments(
        _BaseAudienceSegmentServiceRestTransport._BaseListAudienceSegments,
        AudienceSegmentServiceRestStub,
    ):
        def __hash__(self):
            return hash("AudienceSegmentServiceRestTransport.ListAudienceSegments")

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
            request: audience_segment_service.ListAudienceSegmentsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> audience_segment_service.ListAudienceSegmentsResponse:
            r"""Call the list audience segments method over HTTP.

            Args:
                request (~.audience_segment_service.ListAudienceSegmentsRequest):
                    The request object. Request object for ``ListAudienceSegments`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.audience_segment_service.ListAudienceSegmentsResponse:
                    Response object for ``ListAudienceSegmentsRequest``
                containing matching ``AudienceSegment`` objects.

            """

            http_options = _BaseAudienceSegmentServiceRestTransport._BaseListAudienceSegments._get_http_options()
            request, metadata = self._interceptor.pre_list_audience_segments(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAudienceSegmentServiceRestTransport._BaseListAudienceSegments,
                    "_BaseListAudienceSegments__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.AudienceSegmentServiceClient.ListAudienceSegments",
                    extra={
                        "serviceName": "google.ads.admanager.v1.AudienceSegmentService",
                        "rpcName": "ListAudienceSegments",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                AudienceSegmentServiceRestTransport._ListAudienceSegments._get_response(
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
            resp = audience_segment_service.ListAudienceSegmentsResponse()
            pb_resp = audience_segment_service.ListAudienceSegmentsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_audience_segments(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_audience_segments_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        audience_segment_service.ListAudienceSegmentsResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.AudienceSegmentServiceClient.list_audience_segments",
                    extra={
                        "serviceName": "google.ads.admanager.v1.AudienceSegmentService",
                        "rpcName": "ListAudienceSegments",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateAudienceSegment(
        _BaseAudienceSegmentServiceRestTransport._BaseUpdateAudienceSegment,
        AudienceSegmentServiceRestStub,
    ):
        def __hash__(self):
            return hash("AudienceSegmentServiceRestTransport.UpdateAudienceSegment")

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
            request: audience_segment_service.UpdateAudienceSegmentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> audience_segment_messages.AudienceSegment:
            r"""Call the update audience segment method over HTTP.

            Args:
                request (~.audience_segment_service.UpdateAudienceSegmentRequest):
                    The request object. Request object for ``UpdateAudienceSegment`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.audience_segment_messages.AudienceSegment:
                    The ``AudienceSegment`` resource.
            """

            http_options = _BaseAudienceSegmentServiceRestTransport._BaseUpdateAudienceSegment._get_http_options()
            request, metadata = self._interceptor.pre_update_audience_segment(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAudienceSegmentServiceRestTransport._BaseUpdateAudienceSegment,
                    "_BaseUpdateAudienceSegment__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.AudienceSegmentServiceClient.UpdateAudienceSegment",
                    extra={
                        "serviceName": "google.ads.admanager.v1.AudienceSegmentService",
                        "rpcName": "UpdateAudienceSegment",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AudienceSegmentServiceRestTransport._UpdateAudienceSegment._get_response(
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
            resp = audience_segment_messages.AudienceSegment()
            pb_resp = audience_segment_messages.AudienceSegment.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_audience_segment(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_audience_segment_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        audience_segment_messages.AudienceSegment.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.ads.admanager_v1.AudienceSegmentServiceClient.update_audience_segment",
                    extra={
                        "serviceName": "google.ads.admanager.v1.AudienceSegmentService",
                        "rpcName": "UpdateAudienceSegment",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def batch_activate_audience_segments(
        self,
    ) -> Callable[
        [audience_segment_service.BatchActivateAudienceSegmentsRequest],
        audience_segment_service.BatchActivateAudienceSegmentsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchActivateAudienceSegments(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def batch_approve_audience_segments(
        self,
    ) -> Callable[
        [audience_segment_service.BatchApproveAudienceSegmentsRequest],
        audience_segment_service.BatchApproveAudienceSegmentsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchApproveAudienceSegments(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def batch_create_audience_segments(
        self,
    ) -> Callable[
        [audience_segment_service.BatchCreateAudienceSegmentsRequest],
        audience_segment_service.BatchCreateAudienceSegmentsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchCreateAudienceSegments(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def batch_deactivate_audience_segments(
        self,
    ) -> Callable[
        [audience_segment_service.BatchDeactivateAudienceSegmentsRequest],
        audience_segment_service.BatchDeactivateAudienceSegmentsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchDeactivateAudienceSegments(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def batch_populate_audience_segments(
        self,
    ) -> Callable[
        [audience_segment_service.BatchPopulateAudienceSegmentsRequest],
        audience_segment_service.BatchPopulateAudienceSegmentsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchPopulateAudienceSegments(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def batch_reject_audience_segments(
        self,
    ) -> Callable[
        [audience_segment_service.BatchRejectAudienceSegmentsRequest],
        audience_segment_service.BatchRejectAudienceSegmentsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchRejectAudienceSegments(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def batch_update_audience_segments(
        self,
    ) -> Callable[
        [audience_segment_service.BatchUpdateAudienceSegmentsRequest],
        audience_segment_service.BatchUpdateAudienceSegmentsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchUpdateAudienceSegments(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def create_audience_segment(
        self,
    ) -> Callable[
        [audience_segment_service.CreateAudienceSegmentRequest],
        audience_segment_messages.AudienceSegment,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateAudienceSegment(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_audience_segment(
        self,
    ) -> Callable[
        [audience_segment_service.GetAudienceSegmentRequest],
        audience_segment_messages.AudienceSegment,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetAudienceSegment(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_audience_segments(
        self,
    ) -> Callable[
        [audience_segment_service.ListAudienceSegmentsRequest],
        audience_segment_service.ListAudienceSegmentsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListAudienceSegments(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_audience_segment(
        self,
    ) -> Callable[
        [audience_segment_service.UpdateAudienceSegmentRequest],
        audience_segment_messages.AudienceSegment,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateAudienceSegment(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def cancel_operation(self):
        return self._CancelOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _CancelOperation(
        _BaseAudienceSegmentServiceRestTransport._BaseCancelOperation,
        AudienceSegmentServiceRestStub,
    ):
        def __hash__(self):
            return hash("AudienceSegmentServiceRestTransport.CancelOperation")

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

            http_options = _BaseAudienceSegmentServiceRestTransport._BaseCancelOperation._get_http_options()
            request, metadata = self._interceptor.pre_cancel_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAudienceSegmentServiceRestTransport._BaseCancelOperation,
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
                    f"Sending request for google.ads.admanager_v1.AudienceSegmentServiceClient.CancelOperation",
                    extra={
                        "serviceName": "google.ads.admanager.v1.AudienceSegmentService",
                        "rpcName": "CancelOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                AudienceSegmentServiceRestTransport._CancelOperation._get_response(
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

            return self._interceptor.post_cancel_operation(None)

    @property
    def get_operation(self):
        return self._GetOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetOperation(
        _BaseAudienceSegmentServiceRestTransport._BaseGetOperation,
        AudienceSegmentServiceRestStub,
    ):
        def __hash__(self):
            return hash("AudienceSegmentServiceRestTransport.GetOperation")

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

            http_options = _BaseAudienceSegmentServiceRestTransport._BaseGetOperation._get_http_options()
            request, metadata = self._interceptor.pre_get_operation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAudienceSegmentServiceRestTransport._BaseGetOperation,
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
                    f"Sending request for google.ads.admanager_v1.AudienceSegmentServiceClient.GetOperation",
                    extra={
                        "serviceName": "google.ads.admanager.v1.AudienceSegmentService",
                        "rpcName": "GetOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AudienceSegmentServiceRestTransport._GetOperation._get_response(
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
                    "Received response for google.ads.admanager_v1.AudienceSegmentServiceAsyncClient.GetOperation",
                    extra={
                        "serviceName": "google.ads.admanager.v1.AudienceSegmentService",
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


__all__ = ("AudienceSegmentServiceRestTransport",)
