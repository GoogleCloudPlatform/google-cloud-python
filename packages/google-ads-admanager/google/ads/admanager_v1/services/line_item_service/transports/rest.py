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
from google.longrunning import operations_pb2  # type: ignore
from google.protobuf import json_format
from requests import __version__ as requests_version

from google.ads.admanager_v1._compat import transcode_request
from google.ads.admanager_v1.types import line_item_messages, line_item_service

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseLineItemServiceRestTransport

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


class LineItemServiceRestInterceptor:
    """Interceptor for LineItemService.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the LineItemServiceRestTransport.

    .. code-block:: python
        class MyCustomLineItemServiceInterceptor(LineItemServiceRestInterceptor):
            def pre_batch_activate_line_items(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_activate_line_items(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_batch_archive_line_items(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_archive_line_items(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_batch_create_line_items(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_create_line_items(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_batch_delete_line_items(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_batch_pause_line_items(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_pause_line_items(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_batch_release_line_items(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_release_line_items(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_batch_reserve_and_overbook_line_items(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_reserve_and_overbook_line_items(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_batch_reserve_line_items(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_reserve_line_items(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_batch_resume_and_overbook_line_items(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_resume_and_overbook_line_items(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_batch_resume_line_items(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_resume_line_items(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_batch_unarchive_line_items(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_unarchive_line_items(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_batch_update_line_items(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_update_line_items(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_line_item(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_line_item(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_line_item(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_line_item(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_line_items(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_line_items(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_line_item(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_line_item(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = LineItemServiceRestTransport(interceptor=MyCustomLineItemServiceInterceptor())
        client = LineItemServiceClient(transport=transport)


    """

    def pre_batch_activate_line_items(
        self,
        request: line_item_service.BatchActivateLineItemsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        line_item_service.BatchActivateLineItemsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_activate_line_items

        Override in a subclass to manipulate the request or metadata
        before they are sent to the LineItemService server.
        """
        return request, metadata

    def post_batch_activate_line_items(
        self, response: line_item_service.BatchActivateLineItemsResponse
    ) -> line_item_service.BatchActivateLineItemsResponse:
        """Post-rpc interceptor for batch_activate_line_items

        DEPRECATED. Please use the `post_batch_activate_line_items_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the LineItemService server but before
        it is returned to user code. This `post_batch_activate_line_items` interceptor runs
        before the `post_batch_activate_line_items_with_metadata` interceptor.
        """
        return response

    def post_batch_activate_line_items_with_metadata(
        self,
        response: line_item_service.BatchActivateLineItemsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        line_item_service.BatchActivateLineItemsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_activate_line_items

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the LineItemService server but before it is returned to user code.

        We recommend only using this `post_batch_activate_line_items_with_metadata`
        interceptor in new development instead of the `post_batch_activate_line_items` interceptor.
        When both interceptors are used, this `post_batch_activate_line_items_with_metadata` interceptor runs after the
        `post_batch_activate_line_items` interceptor. The (possibly modified) response returned by
        `post_batch_activate_line_items` will be passed to
        `post_batch_activate_line_items_with_metadata`.
        """
        return response, metadata

    def pre_batch_archive_line_items(
        self,
        request: line_item_service.BatchArchiveLineItemsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        line_item_service.BatchArchiveLineItemsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_archive_line_items

        Override in a subclass to manipulate the request or metadata
        before they are sent to the LineItemService server.
        """
        return request, metadata

    def post_batch_archive_line_items(
        self, response: line_item_service.BatchArchiveLineItemsResponse
    ) -> line_item_service.BatchArchiveLineItemsResponse:
        """Post-rpc interceptor for batch_archive_line_items

        DEPRECATED. Please use the `post_batch_archive_line_items_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the LineItemService server but before
        it is returned to user code. This `post_batch_archive_line_items` interceptor runs
        before the `post_batch_archive_line_items_with_metadata` interceptor.
        """
        return response

    def post_batch_archive_line_items_with_metadata(
        self,
        response: line_item_service.BatchArchiveLineItemsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        line_item_service.BatchArchiveLineItemsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_archive_line_items

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the LineItemService server but before it is returned to user code.

        We recommend only using this `post_batch_archive_line_items_with_metadata`
        interceptor in new development instead of the `post_batch_archive_line_items` interceptor.
        When both interceptors are used, this `post_batch_archive_line_items_with_metadata` interceptor runs after the
        `post_batch_archive_line_items` interceptor. The (possibly modified) response returned by
        `post_batch_archive_line_items` will be passed to
        `post_batch_archive_line_items_with_metadata`.
        """
        return response, metadata

    def pre_batch_create_line_items(
        self,
        request: line_item_service.BatchCreateLineItemsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        line_item_service.BatchCreateLineItemsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_create_line_items

        Override in a subclass to manipulate the request or metadata
        before they are sent to the LineItemService server.
        """
        return request, metadata

    def post_batch_create_line_items(
        self, response: line_item_service.BatchCreateLineItemsResponse
    ) -> line_item_service.BatchCreateLineItemsResponse:
        """Post-rpc interceptor for batch_create_line_items

        DEPRECATED. Please use the `post_batch_create_line_items_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the LineItemService server but before
        it is returned to user code. This `post_batch_create_line_items` interceptor runs
        before the `post_batch_create_line_items_with_metadata` interceptor.
        """
        return response

    def post_batch_create_line_items_with_metadata(
        self,
        response: line_item_service.BatchCreateLineItemsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        line_item_service.BatchCreateLineItemsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_create_line_items

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the LineItemService server but before it is returned to user code.

        We recommend only using this `post_batch_create_line_items_with_metadata`
        interceptor in new development instead of the `post_batch_create_line_items` interceptor.
        When both interceptors are used, this `post_batch_create_line_items_with_metadata` interceptor runs after the
        `post_batch_create_line_items` interceptor. The (possibly modified) response returned by
        `post_batch_create_line_items` will be passed to
        `post_batch_create_line_items_with_metadata`.
        """
        return response, metadata

    def pre_batch_delete_line_items(
        self,
        request: line_item_service.BatchDeleteLineItemsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        line_item_service.BatchDeleteLineItemsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_delete_line_items

        Override in a subclass to manipulate the request or metadata
        before they are sent to the LineItemService server.
        """
        return request, metadata

    def pre_batch_pause_line_items(
        self,
        request: line_item_service.BatchPauseLineItemsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        line_item_service.BatchPauseLineItemsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_pause_line_items

        Override in a subclass to manipulate the request or metadata
        before they are sent to the LineItemService server.
        """
        return request, metadata

    def post_batch_pause_line_items(
        self, response: line_item_service.BatchPauseLineItemsResponse
    ) -> line_item_service.BatchPauseLineItemsResponse:
        """Post-rpc interceptor for batch_pause_line_items

        DEPRECATED. Please use the `post_batch_pause_line_items_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the LineItemService server but before
        it is returned to user code. This `post_batch_pause_line_items` interceptor runs
        before the `post_batch_pause_line_items_with_metadata` interceptor.
        """
        return response

    def post_batch_pause_line_items_with_metadata(
        self,
        response: line_item_service.BatchPauseLineItemsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        line_item_service.BatchPauseLineItemsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_pause_line_items

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the LineItemService server but before it is returned to user code.

        We recommend only using this `post_batch_pause_line_items_with_metadata`
        interceptor in new development instead of the `post_batch_pause_line_items` interceptor.
        When both interceptors are used, this `post_batch_pause_line_items_with_metadata` interceptor runs after the
        `post_batch_pause_line_items` interceptor. The (possibly modified) response returned by
        `post_batch_pause_line_items` will be passed to
        `post_batch_pause_line_items_with_metadata`.
        """
        return response, metadata

    def pre_batch_release_line_items(
        self,
        request: line_item_service.BatchReleaseLineItemsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        line_item_service.BatchReleaseLineItemsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_release_line_items

        Override in a subclass to manipulate the request or metadata
        before they are sent to the LineItemService server.
        """
        return request, metadata

    def post_batch_release_line_items(
        self, response: line_item_service.BatchReleaseLineItemsResponse
    ) -> line_item_service.BatchReleaseLineItemsResponse:
        """Post-rpc interceptor for batch_release_line_items

        DEPRECATED. Please use the `post_batch_release_line_items_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the LineItemService server but before
        it is returned to user code. This `post_batch_release_line_items` interceptor runs
        before the `post_batch_release_line_items_with_metadata` interceptor.
        """
        return response

    def post_batch_release_line_items_with_metadata(
        self,
        response: line_item_service.BatchReleaseLineItemsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        line_item_service.BatchReleaseLineItemsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_release_line_items

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the LineItemService server but before it is returned to user code.

        We recommend only using this `post_batch_release_line_items_with_metadata`
        interceptor in new development instead of the `post_batch_release_line_items` interceptor.
        When both interceptors are used, this `post_batch_release_line_items_with_metadata` interceptor runs after the
        `post_batch_release_line_items` interceptor. The (possibly modified) response returned by
        `post_batch_release_line_items` will be passed to
        `post_batch_release_line_items_with_metadata`.
        """
        return response, metadata

    def pre_batch_reserve_and_overbook_line_items(
        self,
        request: line_item_service.BatchReserveAndOverbookLineItemsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        line_item_service.BatchReserveAndOverbookLineItemsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_reserve_and_overbook_line_items

        Override in a subclass to manipulate the request or metadata
        before they are sent to the LineItemService server.
        """
        return request, metadata

    def post_batch_reserve_and_overbook_line_items(
        self, response: line_item_service.BatchReserveAndOverbookLineItemsResponse
    ) -> line_item_service.BatchReserveAndOverbookLineItemsResponse:
        """Post-rpc interceptor for batch_reserve_and_overbook_line_items

        DEPRECATED. Please use the `post_batch_reserve_and_overbook_line_items_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the LineItemService server but before
        it is returned to user code. This `post_batch_reserve_and_overbook_line_items` interceptor runs
        before the `post_batch_reserve_and_overbook_line_items_with_metadata` interceptor.
        """
        return response

    def post_batch_reserve_and_overbook_line_items_with_metadata(
        self,
        response: line_item_service.BatchReserveAndOverbookLineItemsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        line_item_service.BatchReserveAndOverbookLineItemsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_reserve_and_overbook_line_items

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the LineItemService server but before it is returned to user code.

        We recommend only using this `post_batch_reserve_and_overbook_line_items_with_metadata`
        interceptor in new development instead of the `post_batch_reserve_and_overbook_line_items` interceptor.
        When both interceptors are used, this `post_batch_reserve_and_overbook_line_items_with_metadata` interceptor runs after the
        `post_batch_reserve_and_overbook_line_items` interceptor. The (possibly modified) response returned by
        `post_batch_reserve_and_overbook_line_items` will be passed to
        `post_batch_reserve_and_overbook_line_items_with_metadata`.
        """
        return response, metadata

    def pre_batch_reserve_line_items(
        self,
        request: line_item_service.BatchReserveLineItemsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        line_item_service.BatchReserveLineItemsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_reserve_line_items

        Override in a subclass to manipulate the request or metadata
        before they are sent to the LineItemService server.
        """
        return request, metadata

    def post_batch_reserve_line_items(
        self, response: line_item_service.BatchReserveLineItemsResponse
    ) -> line_item_service.BatchReserveLineItemsResponse:
        """Post-rpc interceptor for batch_reserve_line_items

        DEPRECATED. Please use the `post_batch_reserve_line_items_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the LineItemService server but before
        it is returned to user code. This `post_batch_reserve_line_items` interceptor runs
        before the `post_batch_reserve_line_items_with_metadata` interceptor.
        """
        return response

    def post_batch_reserve_line_items_with_metadata(
        self,
        response: line_item_service.BatchReserveLineItemsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        line_item_service.BatchReserveLineItemsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_reserve_line_items

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the LineItemService server but before it is returned to user code.

        We recommend only using this `post_batch_reserve_line_items_with_metadata`
        interceptor in new development instead of the `post_batch_reserve_line_items` interceptor.
        When both interceptors are used, this `post_batch_reserve_line_items_with_metadata` interceptor runs after the
        `post_batch_reserve_line_items` interceptor. The (possibly modified) response returned by
        `post_batch_reserve_line_items` will be passed to
        `post_batch_reserve_line_items_with_metadata`.
        """
        return response, metadata

    def pre_batch_resume_and_overbook_line_items(
        self,
        request: line_item_service.BatchResumeAndOverbookLineItemsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        line_item_service.BatchResumeAndOverbookLineItemsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_resume_and_overbook_line_items

        Override in a subclass to manipulate the request or metadata
        before they are sent to the LineItemService server.
        """
        return request, metadata

    def post_batch_resume_and_overbook_line_items(
        self, response: line_item_service.BatchResumeAndOverbookLineItemsResponse
    ) -> line_item_service.BatchResumeAndOverbookLineItemsResponse:
        """Post-rpc interceptor for batch_resume_and_overbook_line_items

        DEPRECATED. Please use the `post_batch_resume_and_overbook_line_items_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the LineItemService server but before
        it is returned to user code. This `post_batch_resume_and_overbook_line_items` interceptor runs
        before the `post_batch_resume_and_overbook_line_items_with_metadata` interceptor.
        """
        return response

    def post_batch_resume_and_overbook_line_items_with_metadata(
        self,
        response: line_item_service.BatchResumeAndOverbookLineItemsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        line_item_service.BatchResumeAndOverbookLineItemsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_resume_and_overbook_line_items

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the LineItemService server but before it is returned to user code.

        We recommend only using this `post_batch_resume_and_overbook_line_items_with_metadata`
        interceptor in new development instead of the `post_batch_resume_and_overbook_line_items` interceptor.
        When both interceptors are used, this `post_batch_resume_and_overbook_line_items_with_metadata` interceptor runs after the
        `post_batch_resume_and_overbook_line_items` interceptor. The (possibly modified) response returned by
        `post_batch_resume_and_overbook_line_items` will be passed to
        `post_batch_resume_and_overbook_line_items_with_metadata`.
        """
        return response, metadata

    def pre_batch_resume_line_items(
        self,
        request: line_item_service.BatchResumeLineItemsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        line_item_service.BatchResumeLineItemsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_resume_line_items

        Override in a subclass to manipulate the request or metadata
        before they are sent to the LineItemService server.
        """
        return request, metadata

    def post_batch_resume_line_items(
        self, response: line_item_service.BatchResumeLineItemsResponse
    ) -> line_item_service.BatchResumeLineItemsResponse:
        """Post-rpc interceptor for batch_resume_line_items

        DEPRECATED. Please use the `post_batch_resume_line_items_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the LineItemService server but before
        it is returned to user code. This `post_batch_resume_line_items` interceptor runs
        before the `post_batch_resume_line_items_with_metadata` interceptor.
        """
        return response

    def post_batch_resume_line_items_with_metadata(
        self,
        response: line_item_service.BatchResumeLineItemsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        line_item_service.BatchResumeLineItemsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_resume_line_items

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the LineItemService server but before it is returned to user code.

        We recommend only using this `post_batch_resume_line_items_with_metadata`
        interceptor in new development instead of the `post_batch_resume_line_items` interceptor.
        When both interceptors are used, this `post_batch_resume_line_items_with_metadata` interceptor runs after the
        `post_batch_resume_line_items` interceptor. The (possibly modified) response returned by
        `post_batch_resume_line_items` will be passed to
        `post_batch_resume_line_items_with_metadata`.
        """
        return response, metadata

    def pre_batch_unarchive_line_items(
        self,
        request: line_item_service.BatchUnarchiveLineItemsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        line_item_service.BatchUnarchiveLineItemsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_unarchive_line_items

        Override in a subclass to manipulate the request or metadata
        before they are sent to the LineItemService server.
        """
        return request, metadata

    def post_batch_unarchive_line_items(
        self, response: line_item_service.BatchUnarchiveLineItemsResponse
    ) -> line_item_service.BatchUnarchiveLineItemsResponse:
        """Post-rpc interceptor for batch_unarchive_line_items

        DEPRECATED. Please use the `post_batch_unarchive_line_items_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the LineItemService server but before
        it is returned to user code. This `post_batch_unarchive_line_items` interceptor runs
        before the `post_batch_unarchive_line_items_with_metadata` interceptor.
        """
        return response

    def post_batch_unarchive_line_items_with_metadata(
        self,
        response: line_item_service.BatchUnarchiveLineItemsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        line_item_service.BatchUnarchiveLineItemsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_unarchive_line_items

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the LineItemService server but before it is returned to user code.

        We recommend only using this `post_batch_unarchive_line_items_with_metadata`
        interceptor in new development instead of the `post_batch_unarchive_line_items` interceptor.
        When both interceptors are used, this `post_batch_unarchive_line_items_with_metadata` interceptor runs after the
        `post_batch_unarchive_line_items` interceptor. The (possibly modified) response returned by
        `post_batch_unarchive_line_items` will be passed to
        `post_batch_unarchive_line_items_with_metadata`.
        """
        return response, metadata

    def pre_batch_update_line_items(
        self,
        request: line_item_service.BatchUpdateLineItemsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        line_item_service.BatchUpdateLineItemsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_update_line_items

        Override in a subclass to manipulate the request or metadata
        before they are sent to the LineItemService server.
        """
        return request, metadata

    def post_batch_update_line_items(
        self, response: line_item_service.BatchUpdateLineItemsResponse
    ) -> line_item_service.BatchUpdateLineItemsResponse:
        """Post-rpc interceptor for batch_update_line_items

        DEPRECATED. Please use the `post_batch_update_line_items_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the LineItemService server but before
        it is returned to user code. This `post_batch_update_line_items` interceptor runs
        before the `post_batch_update_line_items_with_metadata` interceptor.
        """
        return response

    def post_batch_update_line_items_with_metadata(
        self,
        response: line_item_service.BatchUpdateLineItemsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        line_item_service.BatchUpdateLineItemsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_update_line_items

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the LineItemService server but before it is returned to user code.

        We recommend only using this `post_batch_update_line_items_with_metadata`
        interceptor in new development instead of the `post_batch_update_line_items` interceptor.
        When both interceptors are used, this `post_batch_update_line_items_with_metadata` interceptor runs after the
        `post_batch_update_line_items` interceptor. The (possibly modified) response returned by
        `post_batch_update_line_items` will be passed to
        `post_batch_update_line_items_with_metadata`.
        """
        return response, metadata

    def pre_create_line_item(
        self,
        request: line_item_service.CreateLineItemRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        line_item_service.CreateLineItemRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_line_item

        Override in a subclass to manipulate the request or metadata
        before they are sent to the LineItemService server.
        """
        return request, metadata

    def post_create_line_item(
        self, response: line_item_messages.LineItem
    ) -> line_item_messages.LineItem:
        """Post-rpc interceptor for create_line_item

        DEPRECATED. Please use the `post_create_line_item_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the LineItemService server but before
        it is returned to user code. This `post_create_line_item` interceptor runs
        before the `post_create_line_item_with_metadata` interceptor.
        """
        return response

    def post_create_line_item_with_metadata(
        self,
        response: line_item_messages.LineItem,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[line_item_messages.LineItem, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_line_item

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the LineItemService server but before it is returned to user code.

        We recommend only using this `post_create_line_item_with_metadata`
        interceptor in new development instead of the `post_create_line_item` interceptor.
        When both interceptors are used, this `post_create_line_item_with_metadata` interceptor runs after the
        `post_create_line_item` interceptor. The (possibly modified) response returned by
        `post_create_line_item` will be passed to
        `post_create_line_item_with_metadata`.
        """
        return response, metadata

    def pre_get_line_item(
        self,
        request: line_item_service.GetLineItemRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        line_item_service.GetLineItemRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_line_item

        Override in a subclass to manipulate the request or metadata
        before they are sent to the LineItemService server.
        """
        return request, metadata

    def post_get_line_item(
        self, response: line_item_messages.LineItem
    ) -> line_item_messages.LineItem:
        """Post-rpc interceptor for get_line_item

        DEPRECATED. Please use the `post_get_line_item_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the LineItemService server but before
        it is returned to user code. This `post_get_line_item` interceptor runs
        before the `post_get_line_item_with_metadata` interceptor.
        """
        return response

    def post_get_line_item_with_metadata(
        self,
        response: line_item_messages.LineItem,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[line_item_messages.LineItem, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_line_item

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the LineItemService server but before it is returned to user code.

        We recommend only using this `post_get_line_item_with_metadata`
        interceptor in new development instead of the `post_get_line_item` interceptor.
        When both interceptors are used, this `post_get_line_item_with_metadata` interceptor runs after the
        `post_get_line_item` interceptor. The (possibly modified) response returned by
        `post_get_line_item` will be passed to
        `post_get_line_item_with_metadata`.
        """
        return response, metadata

    def pre_list_line_items(
        self,
        request: line_item_service.ListLineItemsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        line_item_service.ListLineItemsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_line_items

        Override in a subclass to manipulate the request or metadata
        before they are sent to the LineItemService server.
        """
        return request, metadata

    def post_list_line_items(
        self, response: line_item_service.ListLineItemsResponse
    ) -> line_item_service.ListLineItemsResponse:
        """Post-rpc interceptor for list_line_items

        DEPRECATED. Please use the `post_list_line_items_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the LineItemService server but before
        it is returned to user code. This `post_list_line_items` interceptor runs
        before the `post_list_line_items_with_metadata` interceptor.
        """
        return response

    def post_list_line_items_with_metadata(
        self,
        response: line_item_service.ListLineItemsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        line_item_service.ListLineItemsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_line_items

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the LineItemService server but before it is returned to user code.

        We recommend only using this `post_list_line_items_with_metadata`
        interceptor in new development instead of the `post_list_line_items` interceptor.
        When both interceptors are used, this `post_list_line_items_with_metadata` interceptor runs after the
        `post_list_line_items` interceptor. The (possibly modified) response returned by
        `post_list_line_items` will be passed to
        `post_list_line_items_with_metadata`.
        """
        return response, metadata

    def pre_update_line_item(
        self,
        request: line_item_service.UpdateLineItemRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        line_item_service.UpdateLineItemRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_line_item

        Override in a subclass to manipulate the request or metadata
        before they are sent to the LineItemService server.
        """
        return request, metadata

    def post_update_line_item(
        self, response: line_item_messages.LineItem
    ) -> line_item_messages.LineItem:
        """Post-rpc interceptor for update_line_item

        DEPRECATED. Please use the `post_update_line_item_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the LineItemService server but before
        it is returned to user code. This `post_update_line_item` interceptor runs
        before the `post_update_line_item_with_metadata` interceptor.
        """
        return response

    def post_update_line_item_with_metadata(
        self,
        response: line_item_messages.LineItem,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[line_item_messages.LineItem, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_line_item

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the LineItemService server but before it is returned to user code.

        We recommend only using this `post_update_line_item_with_metadata`
        interceptor in new development instead of the `post_update_line_item` interceptor.
        When both interceptors are used, this `post_update_line_item_with_metadata` interceptor runs after the
        `post_update_line_item` interceptor. The (possibly modified) response returned by
        `post_update_line_item` will be passed to
        `post_update_line_item_with_metadata`.
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
        before they are sent to the LineItemService server.
        """
        return request, metadata

    def post_cancel_operation(self, response: None) -> None:
        """Post-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the response
        after it is returned by the LineItemService server but before
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
        before they are sent to the LineItemService server.
        """
        return request, metadata

    def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the LineItemService server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class LineItemServiceRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: LineItemServiceRestInterceptor


class LineItemServiceRestTransport(_BaseLineItemServiceRestTransport):
    """REST backend synchronous transport for LineItemService.

    Provides methods for handling ``LineItem`` objects.

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
        interceptor: Optional[LineItemServiceRestInterceptor] = None,
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
            interceptor (Optional[LineItemServiceRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or LineItemServiceRestInterceptor()
        self._prep_wrapped_messages(client_info)

    class _BatchActivateLineItems(
        _BaseLineItemServiceRestTransport._BaseBatchActivateLineItems,
        LineItemServiceRestStub,
    ):
        def __hash__(self):
            return hash("LineItemServiceRestTransport.BatchActivateLineItems")

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
            request: line_item_service.BatchActivateLineItemsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> line_item_service.BatchActivateLineItemsResponse:
            r"""Call the batch activate line items method over HTTP.

            Args:
                request (~.line_item_service.BatchActivateLineItemsRequest):
                    The request object. Request object for ``BatchActivateLineItems`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.line_item_service.BatchActivateLineItemsResponse:
                    Response object for ``BatchActivateLineItems`` method.
            """

            http_options = _BaseLineItemServiceRestTransport._BaseBatchActivateLineItems._get_http_options()
            request, metadata = self._interceptor.pre_batch_activate_line_items(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLineItemServiceRestTransport._BaseBatchActivateLineItems,
                    "_BaseBatchActivateLineItems__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.LineItemServiceClient.BatchActivateLineItems",
                    extra={
                        "serviceName": "google.ads.admanager.v1.LineItemService",
                        "rpcName": "BatchActivateLineItems",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                LineItemServiceRestTransport._BatchActivateLineItems._get_response(
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
            resp = line_item_service.BatchActivateLineItemsResponse()
            pb_resp = line_item_service.BatchActivateLineItemsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_activate_line_items(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_batch_activate_line_items_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        line_item_service.BatchActivateLineItemsResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.LineItemServiceClient.batch_activate_line_items",
                    extra={
                        "serviceName": "google.ads.admanager.v1.LineItemService",
                        "rpcName": "BatchActivateLineItems",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BatchArchiveLineItems(
        _BaseLineItemServiceRestTransport._BaseBatchArchiveLineItems,
        LineItemServiceRestStub,
    ):
        def __hash__(self):
            return hash("LineItemServiceRestTransport.BatchArchiveLineItems")

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
            request: line_item_service.BatchArchiveLineItemsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> line_item_service.BatchArchiveLineItemsResponse:
            r"""Call the batch archive line items method over HTTP.

            Args:
                request (~.line_item_service.BatchArchiveLineItemsRequest):
                    The request object. Request object for ``BatchArchiveLineItems`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.line_item_service.BatchArchiveLineItemsResponse:
                    Response object for ``BatchArchiveLineItems`` method.
            """

            http_options = _BaseLineItemServiceRestTransport._BaseBatchArchiveLineItems._get_http_options()
            request, metadata = self._interceptor.pre_batch_archive_line_items(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLineItemServiceRestTransport._BaseBatchArchiveLineItems,
                    "_BaseBatchArchiveLineItems__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.LineItemServiceClient.BatchArchiveLineItems",
                    extra={
                        "serviceName": "google.ads.admanager.v1.LineItemService",
                        "rpcName": "BatchArchiveLineItems",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                LineItemServiceRestTransport._BatchArchiveLineItems._get_response(
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
            resp = line_item_service.BatchArchiveLineItemsResponse()
            pb_resp = line_item_service.BatchArchiveLineItemsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_archive_line_items(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_batch_archive_line_items_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        line_item_service.BatchArchiveLineItemsResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.LineItemServiceClient.batch_archive_line_items",
                    extra={
                        "serviceName": "google.ads.admanager.v1.LineItemService",
                        "rpcName": "BatchArchiveLineItems",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BatchCreateLineItems(
        _BaseLineItemServiceRestTransport._BaseBatchCreateLineItems,
        LineItemServiceRestStub,
    ):
        def __hash__(self):
            return hash("LineItemServiceRestTransport.BatchCreateLineItems")

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
            request: line_item_service.BatchCreateLineItemsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> line_item_service.BatchCreateLineItemsResponse:
            r"""Call the batch create line items method over HTTP.

            Args:
                request (~.line_item_service.BatchCreateLineItemsRequest):
                    The request object. Request object for ``BatchCreateLineItems`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.line_item_service.BatchCreateLineItemsResponse:
                    Response object for ``BatchCreateLineItems`` method.
            """

            http_options = _BaseLineItemServiceRestTransport._BaseBatchCreateLineItems._get_http_options()
            request, metadata = self._interceptor.pre_batch_create_line_items(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLineItemServiceRestTransport._BaseBatchCreateLineItems,
                    "_BaseBatchCreateLineItems__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.LineItemServiceClient.BatchCreateLineItems",
                    extra={
                        "serviceName": "google.ads.admanager.v1.LineItemService",
                        "rpcName": "BatchCreateLineItems",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LineItemServiceRestTransport._BatchCreateLineItems._get_response(
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
            resp = line_item_service.BatchCreateLineItemsResponse()
            pb_resp = line_item_service.BatchCreateLineItemsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_create_line_items(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_batch_create_line_items_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        line_item_service.BatchCreateLineItemsResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.ads.admanager_v1.LineItemServiceClient.batch_create_line_items",
                    extra={
                        "serviceName": "google.ads.admanager.v1.LineItemService",
                        "rpcName": "BatchCreateLineItems",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BatchDeleteLineItems(
        _BaseLineItemServiceRestTransport._BaseBatchDeleteLineItems,
        LineItemServiceRestStub,
    ):
        def __hash__(self):
            return hash("LineItemServiceRestTransport.BatchDeleteLineItems")

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
            request: line_item_service.BatchDeleteLineItemsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the batch delete line items method over HTTP.

            Args:
                request (~.line_item_service.BatchDeleteLineItemsRequest):
                    The request object. Request object for ``BatchDeleteLineItems`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = _BaseLineItemServiceRestTransport._BaseBatchDeleteLineItems._get_http_options()
            request, metadata = self._interceptor.pre_batch_delete_line_items(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLineItemServiceRestTransport._BaseBatchDeleteLineItems,
                    "_BaseBatchDeleteLineItems__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.LineItemServiceClient.BatchDeleteLineItems",
                    extra={
                        "serviceName": "google.ads.admanager.v1.LineItemService",
                        "rpcName": "BatchDeleteLineItems",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LineItemServiceRestTransport._BatchDeleteLineItems._get_response(
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

    class _BatchPauseLineItems(
        _BaseLineItemServiceRestTransport._BaseBatchPauseLineItems,
        LineItemServiceRestStub,
    ):
        def __hash__(self):
            return hash("LineItemServiceRestTransport.BatchPauseLineItems")

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
            request: line_item_service.BatchPauseLineItemsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> line_item_service.BatchPauseLineItemsResponse:
            r"""Call the batch pause line items method over HTTP.

            Args:
                request (~.line_item_service.BatchPauseLineItemsRequest):
                    The request object. Request object for ``BatchPauseLineItems`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.line_item_service.BatchPauseLineItemsResponse:
                    Response object for ``BatchPauseLineItems`` method.
            """

            http_options = _BaseLineItemServiceRestTransport._BaseBatchPauseLineItems._get_http_options()
            request, metadata = self._interceptor.pre_batch_pause_line_items(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLineItemServiceRestTransport._BaseBatchPauseLineItems,
                    "_BaseBatchPauseLineItems__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.LineItemServiceClient.BatchPauseLineItems",
                    extra={
                        "serviceName": "google.ads.admanager.v1.LineItemService",
                        "rpcName": "BatchPauseLineItems",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LineItemServiceRestTransport._BatchPauseLineItems._get_response(
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
            resp = line_item_service.BatchPauseLineItemsResponse()
            pb_resp = line_item_service.BatchPauseLineItemsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_pause_line_items(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_batch_pause_line_items_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        line_item_service.BatchPauseLineItemsResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.ads.admanager_v1.LineItemServiceClient.batch_pause_line_items",
                    extra={
                        "serviceName": "google.ads.admanager.v1.LineItemService",
                        "rpcName": "BatchPauseLineItems",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BatchReleaseLineItems(
        _BaseLineItemServiceRestTransport._BaseBatchReleaseLineItems,
        LineItemServiceRestStub,
    ):
        def __hash__(self):
            return hash("LineItemServiceRestTransport.BatchReleaseLineItems")

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
            request: line_item_service.BatchReleaseLineItemsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> line_item_service.BatchReleaseLineItemsResponse:
            r"""Call the batch release line items method over HTTP.

            Args:
                request (~.line_item_service.BatchReleaseLineItemsRequest):
                    The request object. Request object for ``BatchReleaseLineItems`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.line_item_service.BatchReleaseLineItemsResponse:
                    Response object for ``BatchReleaseLineItems`` method.
            """

            http_options = _BaseLineItemServiceRestTransport._BaseBatchReleaseLineItems._get_http_options()
            request, metadata = self._interceptor.pre_batch_release_line_items(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLineItemServiceRestTransport._BaseBatchReleaseLineItems,
                    "_BaseBatchReleaseLineItems__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.LineItemServiceClient.BatchReleaseLineItems",
                    extra={
                        "serviceName": "google.ads.admanager.v1.LineItemService",
                        "rpcName": "BatchReleaseLineItems",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                LineItemServiceRestTransport._BatchReleaseLineItems._get_response(
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
            resp = line_item_service.BatchReleaseLineItemsResponse()
            pb_resp = line_item_service.BatchReleaseLineItemsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_release_line_items(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_batch_release_line_items_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        line_item_service.BatchReleaseLineItemsResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.LineItemServiceClient.batch_release_line_items",
                    extra={
                        "serviceName": "google.ads.admanager.v1.LineItemService",
                        "rpcName": "BatchReleaseLineItems",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BatchReserveAndOverbookLineItems(
        _BaseLineItemServiceRestTransport._BaseBatchReserveAndOverbookLineItems,
        LineItemServiceRestStub,
    ):
        def __hash__(self):
            return hash("LineItemServiceRestTransport.BatchReserveAndOverbookLineItems")

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
            request: line_item_service.BatchReserveAndOverbookLineItemsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> line_item_service.BatchReserveAndOverbookLineItemsResponse:
            r"""Call the batch reserve and
            overbook line items method over HTTP.

                Args:
                    request (~.line_item_service.BatchReserveAndOverbookLineItemsRequest):
                        The request object. Request object for ``BatchReserveAndOverbookLineItems``
                    method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.line_item_service.BatchReserveAndOverbookLineItemsResponse:
                        Response object for ``BatchReserveAndOverbookLineItems``
                    method.

            """

            http_options = _BaseLineItemServiceRestTransport._BaseBatchReserveAndOverbookLineItems._get_http_options()
            request, metadata = (
                self._interceptor.pre_batch_reserve_and_overbook_line_items(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLineItemServiceRestTransport._BaseBatchReserveAndOverbookLineItems,
                    "_BaseBatchReserveAndOverbookLineItems__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.LineItemServiceClient.BatchReserveAndOverbookLineItems",
                    extra={
                        "serviceName": "google.ads.admanager.v1.LineItemService",
                        "rpcName": "BatchReserveAndOverbookLineItems",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LineItemServiceRestTransport._BatchReserveAndOverbookLineItems._get_response(
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
            resp = line_item_service.BatchReserveAndOverbookLineItemsResponse()
            pb_resp = line_item_service.BatchReserveAndOverbookLineItemsResponse.pb(
                resp
            )

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_reserve_and_overbook_line_items(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_batch_reserve_and_overbook_line_items_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = line_item_service.BatchReserveAndOverbookLineItemsResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.LineItemServiceClient.batch_reserve_and_overbook_line_items",
                    extra={
                        "serviceName": "google.ads.admanager.v1.LineItemService",
                        "rpcName": "BatchReserveAndOverbookLineItems",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BatchReserveLineItems(
        _BaseLineItemServiceRestTransport._BaseBatchReserveLineItems,
        LineItemServiceRestStub,
    ):
        def __hash__(self):
            return hash("LineItemServiceRestTransport.BatchReserveLineItems")

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
            request: line_item_service.BatchReserveLineItemsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> line_item_service.BatchReserveLineItemsResponse:
            r"""Call the batch reserve line items method over HTTP.

            Args:
                request (~.line_item_service.BatchReserveLineItemsRequest):
                    The request object. Request object for ``BatchReserveLineItems`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.line_item_service.BatchReserveLineItemsResponse:
                    Response object for ``BatchReserveLineItems`` method.
            """

            http_options = _BaseLineItemServiceRestTransport._BaseBatchReserveLineItems._get_http_options()
            request, metadata = self._interceptor.pre_batch_reserve_line_items(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLineItemServiceRestTransport._BaseBatchReserveLineItems,
                    "_BaseBatchReserveLineItems__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.LineItemServiceClient.BatchReserveLineItems",
                    extra={
                        "serviceName": "google.ads.admanager.v1.LineItemService",
                        "rpcName": "BatchReserveLineItems",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                LineItemServiceRestTransport._BatchReserveLineItems._get_response(
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
            resp = line_item_service.BatchReserveLineItemsResponse()
            pb_resp = line_item_service.BatchReserveLineItemsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_reserve_line_items(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_batch_reserve_line_items_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        line_item_service.BatchReserveLineItemsResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.LineItemServiceClient.batch_reserve_line_items",
                    extra={
                        "serviceName": "google.ads.admanager.v1.LineItemService",
                        "rpcName": "BatchReserveLineItems",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BatchResumeAndOverbookLineItems(
        _BaseLineItemServiceRestTransport._BaseBatchResumeAndOverbookLineItems,
        LineItemServiceRestStub,
    ):
        def __hash__(self):
            return hash("LineItemServiceRestTransport.BatchResumeAndOverbookLineItems")

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
            request: line_item_service.BatchResumeAndOverbookLineItemsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> line_item_service.BatchResumeAndOverbookLineItemsResponse:
            r"""Call the batch resume and overbook
            line items method over HTTP.

                Args:
                    request (~.line_item_service.BatchResumeAndOverbookLineItemsRequest):
                        The request object. Request object for ``BatchResumeAndOverbookLineItems``
                    method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.line_item_service.BatchResumeAndOverbookLineItemsResponse:
                        Response object for ``BatchResumeAndOverbookLineItems``
                    method.

            """

            http_options = _BaseLineItemServiceRestTransport._BaseBatchResumeAndOverbookLineItems._get_http_options()
            request, metadata = (
                self._interceptor.pre_batch_resume_and_overbook_line_items(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLineItemServiceRestTransport._BaseBatchResumeAndOverbookLineItems,
                    "_BaseBatchResumeAndOverbookLineItems__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.LineItemServiceClient.BatchResumeAndOverbookLineItems",
                    extra={
                        "serviceName": "google.ads.admanager.v1.LineItemService",
                        "rpcName": "BatchResumeAndOverbookLineItems",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LineItemServiceRestTransport._BatchResumeAndOverbookLineItems._get_response(
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
            resp = line_item_service.BatchResumeAndOverbookLineItemsResponse()
            pb_resp = line_item_service.BatchResumeAndOverbookLineItemsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_resume_and_overbook_line_items(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_batch_resume_and_overbook_line_items_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = line_item_service.BatchResumeAndOverbookLineItemsResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.LineItemServiceClient.batch_resume_and_overbook_line_items",
                    extra={
                        "serviceName": "google.ads.admanager.v1.LineItemService",
                        "rpcName": "BatchResumeAndOverbookLineItems",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BatchResumeLineItems(
        _BaseLineItemServiceRestTransport._BaseBatchResumeLineItems,
        LineItemServiceRestStub,
    ):
        def __hash__(self):
            return hash("LineItemServiceRestTransport.BatchResumeLineItems")

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
            request: line_item_service.BatchResumeLineItemsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> line_item_service.BatchResumeLineItemsResponse:
            r"""Call the batch resume line items method over HTTP.

            Args:
                request (~.line_item_service.BatchResumeLineItemsRequest):
                    The request object. Request object for ``BatchResumeLineItems`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.line_item_service.BatchResumeLineItemsResponse:
                    Response object for ``BatchResumeLineItems`` method.
            """

            http_options = _BaseLineItemServiceRestTransport._BaseBatchResumeLineItems._get_http_options()
            request, metadata = self._interceptor.pre_batch_resume_line_items(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLineItemServiceRestTransport._BaseBatchResumeLineItems,
                    "_BaseBatchResumeLineItems__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.LineItemServiceClient.BatchResumeLineItems",
                    extra={
                        "serviceName": "google.ads.admanager.v1.LineItemService",
                        "rpcName": "BatchResumeLineItems",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LineItemServiceRestTransport._BatchResumeLineItems._get_response(
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
            resp = line_item_service.BatchResumeLineItemsResponse()
            pb_resp = line_item_service.BatchResumeLineItemsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_resume_line_items(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_batch_resume_line_items_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        line_item_service.BatchResumeLineItemsResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.ads.admanager_v1.LineItemServiceClient.batch_resume_line_items",
                    extra={
                        "serviceName": "google.ads.admanager.v1.LineItemService",
                        "rpcName": "BatchResumeLineItems",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BatchUnarchiveLineItems(
        _BaseLineItemServiceRestTransport._BaseBatchUnarchiveLineItems,
        LineItemServiceRestStub,
    ):
        def __hash__(self):
            return hash("LineItemServiceRestTransport.BatchUnarchiveLineItems")

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
            request: line_item_service.BatchUnarchiveLineItemsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> line_item_service.BatchUnarchiveLineItemsResponse:
            r"""Call the batch unarchive line
            items method over HTTP.

                Args:
                    request (~.line_item_service.BatchUnarchiveLineItemsRequest):
                        The request object. Request object for ``BatchUnarchiveLineItems`` method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.line_item_service.BatchUnarchiveLineItemsResponse:
                        Response object for ``BatchUnarchiveLineItems`` method.
            """

            http_options = _BaseLineItemServiceRestTransport._BaseBatchUnarchiveLineItems._get_http_options()
            request, metadata = self._interceptor.pre_batch_unarchive_line_items(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLineItemServiceRestTransport._BaseBatchUnarchiveLineItems,
                    "_BaseBatchUnarchiveLineItems__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.LineItemServiceClient.BatchUnarchiveLineItems",
                    extra={
                        "serviceName": "google.ads.admanager.v1.LineItemService",
                        "rpcName": "BatchUnarchiveLineItems",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                LineItemServiceRestTransport._BatchUnarchiveLineItems._get_response(
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
            resp = line_item_service.BatchUnarchiveLineItemsResponse()
            pb_resp = line_item_service.BatchUnarchiveLineItemsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_unarchive_line_items(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_batch_unarchive_line_items_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        line_item_service.BatchUnarchiveLineItemsResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.LineItemServiceClient.batch_unarchive_line_items",
                    extra={
                        "serviceName": "google.ads.admanager.v1.LineItemService",
                        "rpcName": "BatchUnarchiveLineItems",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BatchUpdateLineItems(
        _BaseLineItemServiceRestTransport._BaseBatchUpdateLineItems,
        LineItemServiceRestStub,
    ):
        def __hash__(self):
            return hash("LineItemServiceRestTransport.BatchUpdateLineItems")

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
            request: line_item_service.BatchUpdateLineItemsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> line_item_service.BatchUpdateLineItemsResponse:
            r"""Call the batch update line items method over HTTP.

            Args:
                request (~.line_item_service.BatchUpdateLineItemsRequest):
                    The request object. Request object for ``BatchUpdateLineItems`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.line_item_service.BatchUpdateLineItemsResponse:
                    Response object for ``BatchUpdateLineItems`` method.
            """

            http_options = _BaseLineItemServiceRestTransport._BaseBatchUpdateLineItems._get_http_options()
            request, metadata = self._interceptor.pre_batch_update_line_items(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLineItemServiceRestTransport._BaseBatchUpdateLineItems,
                    "_BaseBatchUpdateLineItems__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.LineItemServiceClient.BatchUpdateLineItems",
                    extra={
                        "serviceName": "google.ads.admanager.v1.LineItemService",
                        "rpcName": "BatchUpdateLineItems",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LineItemServiceRestTransport._BatchUpdateLineItems._get_response(
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
            resp = line_item_service.BatchUpdateLineItemsResponse()
            pb_resp = line_item_service.BatchUpdateLineItemsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_update_line_items(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_batch_update_line_items_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        line_item_service.BatchUpdateLineItemsResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.ads.admanager_v1.LineItemServiceClient.batch_update_line_items",
                    extra={
                        "serviceName": "google.ads.admanager.v1.LineItemService",
                        "rpcName": "BatchUpdateLineItems",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateLineItem(
        _BaseLineItemServiceRestTransport._BaseCreateLineItem, LineItemServiceRestStub
    ):
        def __hash__(self):
            return hash("LineItemServiceRestTransport.CreateLineItem")

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
            request: line_item_service.CreateLineItemRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> line_item_messages.LineItem:
            r"""Call the create line item method over HTTP.

            Args:
                request (~.line_item_service.CreateLineItemRequest):
                    The request object. Request object for ``CreateLineItem`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.line_item_messages.LineItem:
                    A LineItem contains information about
                how specific ad creatives are intended
                to serve to your website or app along
                with pricing and other delivery details.

            """

            http_options = _BaseLineItemServiceRestTransport._BaseCreateLineItem._get_http_options()
            request, metadata = self._interceptor.pre_create_line_item(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLineItemServiceRestTransport._BaseCreateLineItem,
                    "_BaseCreateLineItem__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.LineItemServiceClient.CreateLineItem",
                    extra={
                        "serviceName": "google.ads.admanager.v1.LineItemService",
                        "rpcName": "CreateLineItem",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LineItemServiceRestTransport._CreateLineItem._get_response(
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
            resp = line_item_messages.LineItem()
            pb_resp = line_item_messages.LineItem.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_line_item(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_line_item_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = line_item_messages.LineItem.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.ads.admanager_v1.LineItemServiceClient.create_line_item",
                    extra={
                        "serviceName": "google.ads.admanager.v1.LineItemService",
                        "rpcName": "CreateLineItem",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetLineItem(
        _BaseLineItemServiceRestTransport._BaseGetLineItem, LineItemServiceRestStub
    ):
        def __hash__(self):
            return hash("LineItemServiceRestTransport.GetLineItem")

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
            request: line_item_service.GetLineItemRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> line_item_messages.LineItem:
            r"""Call the get line item method over HTTP.

            Args:
                request (~.line_item_service.GetLineItemRequest):
                    The request object. Request object for ``GetLineItem`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.line_item_messages.LineItem:
                    A LineItem contains information about
                how specific ad creatives are intended
                to serve to your website or app along
                with pricing and other delivery details.

            """

            http_options = (
                _BaseLineItemServiceRestTransport._BaseGetLineItem._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_line_item(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLineItemServiceRestTransport._BaseGetLineItem,
                    "_BaseGetLineItem__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.LineItemServiceClient.GetLineItem",
                    extra={
                        "serviceName": "google.ads.admanager.v1.LineItemService",
                        "rpcName": "GetLineItem",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LineItemServiceRestTransport._GetLineItem._get_response(
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
            resp = line_item_messages.LineItem()
            pb_resp = line_item_messages.LineItem.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_line_item(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_line_item_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = line_item_messages.LineItem.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.ads.admanager_v1.LineItemServiceClient.get_line_item",
                    extra={
                        "serviceName": "google.ads.admanager.v1.LineItemService",
                        "rpcName": "GetLineItem",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListLineItems(
        _BaseLineItemServiceRestTransport._BaseListLineItems, LineItemServiceRestStub
    ):
        def __hash__(self):
            return hash("LineItemServiceRestTransport.ListLineItems")

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
            request: line_item_service.ListLineItemsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> line_item_service.ListLineItemsResponse:
            r"""Call the list line items method over HTTP.

            Args:
                request (~.line_item_service.ListLineItemsRequest):
                    The request object. Request object for ``ListLineItems`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.line_item_service.ListLineItemsResponse:
                    Response object for ``ListLineItemsRequest`` containing
                matching ``LineItem`` objects.

            """

            http_options = (
                _BaseLineItemServiceRestTransport._BaseListLineItems._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_line_items(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLineItemServiceRestTransport._BaseListLineItems,
                    "_BaseListLineItems__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.LineItemServiceClient.ListLineItems",
                    extra={
                        "serviceName": "google.ads.admanager.v1.LineItemService",
                        "rpcName": "ListLineItems",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LineItemServiceRestTransport._ListLineItems._get_response(
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
            resp = line_item_service.ListLineItemsResponse()
            pb_resp = line_item_service.ListLineItemsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_line_items(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_line_items_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = line_item_service.ListLineItemsResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.LineItemServiceClient.list_line_items",
                    extra={
                        "serviceName": "google.ads.admanager.v1.LineItemService",
                        "rpcName": "ListLineItems",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateLineItem(
        _BaseLineItemServiceRestTransport._BaseUpdateLineItem, LineItemServiceRestStub
    ):
        def __hash__(self):
            return hash("LineItemServiceRestTransport.UpdateLineItem")

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
            request: line_item_service.UpdateLineItemRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> line_item_messages.LineItem:
            r"""Call the update line item method over HTTP.

            Args:
                request (~.line_item_service.UpdateLineItemRequest):
                    The request object. Request object for ``UpdateLineItem`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.line_item_messages.LineItem:
                    A LineItem contains information about
                how specific ad creatives are intended
                to serve to your website or app along
                with pricing and other delivery details.

            """

            http_options = _BaseLineItemServiceRestTransport._BaseUpdateLineItem._get_http_options()
            request, metadata = self._interceptor.pre_update_line_item(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLineItemServiceRestTransport._BaseUpdateLineItem,
                    "_BaseUpdateLineItem__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.LineItemServiceClient.UpdateLineItem",
                    extra={
                        "serviceName": "google.ads.admanager.v1.LineItemService",
                        "rpcName": "UpdateLineItem",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LineItemServiceRestTransport._UpdateLineItem._get_response(
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
            resp = line_item_messages.LineItem()
            pb_resp = line_item_messages.LineItem.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_line_item(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_line_item_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = line_item_messages.LineItem.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.ads.admanager_v1.LineItemServiceClient.update_line_item",
                    extra={
                        "serviceName": "google.ads.admanager.v1.LineItemService",
                        "rpcName": "UpdateLineItem",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def batch_activate_line_items(
        self,
    ) -> Callable[
        [line_item_service.BatchActivateLineItemsRequest],
        line_item_service.BatchActivateLineItemsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchActivateLineItems(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def batch_archive_line_items(
        self,
    ) -> Callable[
        [line_item_service.BatchArchiveLineItemsRequest],
        line_item_service.BatchArchiveLineItemsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchArchiveLineItems(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def batch_create_line_items(
        self,
    ) -> Callable[
        [line_item_service.BatchCreateLineItemsRequest],
        line_item_service.BatchCreateLineItemsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchCreateLineItems(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def batch_delete_line_items(
        self,
    ) -> Callable[[line_item_service.BatchDeleteLineItemsRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchDeleteLineItems(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def batch_pause_line_items(
        self,
    ) -> Callable[
        [line_item_service.BatchPauseLineItemsRequest],
        line_item_service.BatchPauseLineItemsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchPauseLineItems(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def batch_release_line_items(
        self,
    ) -> Callable[
        [line_item_service.BatchReleaseLineItemsRequest],
        line_item_service.BatchReleaseLineItemsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchReleaseLineItems(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def batch_reserve_and_overbook_line_items(
        self,
    ) -> Callable[
        [line_item_service.BatchReserveAndOverbookLineItemsRequest],
        line_item_service.BatchReserveAndOverbookLineItemsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchReserveAndOverbookLineItems(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def batch_reserve_line_items(
        self,
    ) -> Callable[
        [line_item_service.BatchReserveLineItemsRequest],
        line_item_service.BatchReserveLineItemsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchReserveLineItems(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def batch_resume_and_overbook_line_items(
        self,
    ) -> Callable[
        [line_item_service.BatchResumeAndOverbookLineItemsRequest],
        line_item_service.BatchResumeAndOverbookLineItemsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchResumeAndOverbookLineItems(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def batch_resume_line_items(
        self,
    ) -> Callable[
        [line_item_service.BatchResumeLineItemsRequest],
        line_item_service.BatchResumeLineItemsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchResumeLineItems(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def batch_unarchive_line_items(
        self,
    ) -> Callable[
        [line_item_service.BatchUnarchiveLineItemsRequest],
        line_item_service.BatchUnarchiveLineItemsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchUnarchiveLineItems(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def batch_update_line_items(
        self,
    ) -> Callable[
        [line_item_service.BatchUpdateLineItemsRequest],
        line_item_service.BatchUpdateLineItemsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchUpdateLineItems(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_line_item(
        self,
    ) -> Callable[
        [line_item_service.CreateLineItemRequest], line_item_messages.LineItem
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateLineItem(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_line_item(
        self,
    ) -> Callable[[line_item_service.GetLineItemRequest], line_item_messages.LineItem]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetLineItem(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_line_items(
        self,
    ) -> Callable[
        [line_item_service.ListLineItemsRequest],
        line_item_service.ListLineItemsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListLineItems(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_line_item(
        self,
    ) -> Callable[
        [line_item_service.UpdateLineItemRequest], line_item_messages.LineItem
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateLineItem(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def cancel_operation(self):
        return self._CancelOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _CancelOperation(
        _BaseLineItemServiceRestTransport._BaseCancelOperation, LineItemServiceRestStub
    ):
        def __hash__(self):
            return hash("LineItemServiceRestTransport.CancelOperation")

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

            http_options = _BaseLineItemServiceRestTransport._BaseCancelOperation._get_http_options()
            request, metadata = self._interceptor.pre_cancel_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLineItemServiceRestTransport._BaseCancelOperation,
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
                    f"Sending request for google.ads.admanager_v1.LineItemServiceClient.CancelOperation",
                    extra={
                        "serviceName": "google.ads.admanager.v1.LineItemService",
                        "rpcName": "CancelOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LineItemServiceRestTransport._CancelOperation._get_response(
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
        _BaseLineItemServiceRestTransport._BaseGetOperation, LineItemServiceRestStub
    ):
        def __hash__(self):
            return hash("LineItemServiceRestTransport.GetOperation")

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
                _BaseLineItemServiceRestTransport._BaseGetOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_operation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLineItemServiceRestTransport._BaseGetOperation,
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
                    f"Sending request for google.ads.admanager_v1.LineItemServiceClient.GetOperation",
                    extra={
                        "serviceName": "google.ads.admanager.v1.LineItemService",
                        "rpcName": "GetOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LineItemServiceRestTransport._GetOperation._get_response(
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
                    "Received response for google.ads.admanager_v1.LineItemServiceAsyncClient.GetOperation",
                    extra={
                        "serviceName": "google.ads.admanager.v1.LineItemService",
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


__all__ = ("LineItemServiceRestTransport",)
