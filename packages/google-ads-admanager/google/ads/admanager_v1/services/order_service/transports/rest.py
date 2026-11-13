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
from google.ads.admanager_v1.types import order_messages, order_service

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseOrderServiceRestTransport

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


class OrderServiceRestInterceptor:
    """Interceptor for OrderService.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the OrderServiceRestTransport.

    .. code-block:: python
        class MyCustomOrderServiceInterceptor(OrderServiceRestInterceptor):
            def pre_batch_approve_and_overbook_orders(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_approve_and_overbook_orders(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_batch_approve_orders(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_approve_orders(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_batch_approve_orders_without_reservation(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_approve_orders_without_reservation(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_batch_archive_orders(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_archive_orders(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_batch_create_orders(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_create_orders(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_batch_delete_orders(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_delete_orders(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_batch_disapprove_orders(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_disapprove_orders(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_batch_disapprove_orders_without_reservation_changes(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_disapprove_orders_without_reservation_changes(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_batch_pause_orders(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_pause_orders(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_batch_resume_and_overbook_orders(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_resume_and_overbook_orders(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_batch_resume_orders(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_resume_orders(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_batch_retract_orders(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_retract_orders(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_batch_retract_orders_without_reservation_changes(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_retract_orders_without_reservation_changes(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_batch_submit_orders_for_approval(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_submit_orders_for_approval(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_batch_submit_orders_for_approval_and_overbook(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_submit_orders_for_approval_and_overbook(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_batch_submit_orders_for_approval_without_reservation_changes(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_submit_orders_for_approval_without_reservation_changes(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_batch_unarchive_orders(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_unarchive_orders(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_batch_update_orders(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_update_orders(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_order(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_order(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_orders(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_orders(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = OrderServiceRestTransport(interceptor=MyCustomOrderServiceInterceptor())
        client = OrderServiceClient(transport=transport)


    """

    def pre_batch_approve_and_overbook_orders(
        self,
        request: order_service.BatchApproveAndOverbookOrdersRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        order_service.BatchApproveAndOverbookOrdersRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_approve_and_overbook_orders

        Override in a subclass to manipulate the request or metadata
        before they are sent to the OrderService server.
        """
        return request, metadata

    def post_batch_approve_and_overbook_orders(
        self, response: order_service.BatchApproveAndOverbookOrdersResponse
    ) -> order_service.BatchApproveAndOverbookOrdersResponse:
        """Post-rpc interceptor for batch_approve_and_overbook_orders

        DEPRECATED. Please use the `post_batch_approve_and_overbook_orders_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the OrderService server but before
        it is returned to user code. This `post_batch_approve_and_overbook_orders` interceptor runs
        before the `post_batch_approve_and_overbook_orders_with_metadata` interceptor.
        """
        return response

    def post_batch_approve_and_overbook_orders_with_metadata(
        self,
        response: order_service.BatchApproveAndOverbookOrdersResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        order_service.BatchApproveAndOverbookOrdersResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_approve_and_overbook_orders

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the OrderService server but before it is returned to user code.

        We recommend only using this `post_batch_approve_and_overbook_orders_with_metadata`
        interceptor in new development instead of the `post_batch_approve_and_overbook_orders` interceptor.
        When both interceptors are used, this `post_batch_approve_and_overbook_orders_with_metadata` interceptor runs after the
        `post_batch_approve_and_overbook_orders` interceptor. The (possibly modified) response returned by
        `post_batch_approve_and_overbook_orders` will be passed to
        `post_batch_approve_and_overbook_orders_with_metadata`.
        """
        return response, metadata

    def pre_batch_approve_orders(
        self,
        request: order_service.BatchApproveOrdersRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        order_service.BatchApproveOrdersRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for batch_approve_orders

        Override in a subclass to manipulate the request or metadata
        before they are sent to the OrderService server.
        """
        return request, metadata

    def post_batch_approve_orders(
        self, response: order_service.BatchApproveOrdersResponse
    ) -> order_service.BatchApproveOrdersResponse:
        """Post-rpc interceptor for batch_approve_orders

        DEPRECATED. Please use the `post_batch_approve_orders_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the OrderService server but before
        it is returned to user code. This `post_batch_approve_orders` interceptor runs
        before the `post_batch_approve_orders_with_metadata` interceptor.
        """
        return response

    def post_batch_approve_orders_with_metadata(
        self,
        response: order_service.BatchApproveOrdersResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        order_service.BatchApproveOrdersResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_approve_orders

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the OrderService server but before it is returned to user code.

        We recommend only using this `post_batch_approve_orders_with_metadata`
        interceptor in new development instead of the `post_batch_approve_orders` interceptor.
        When both interceptors are used, this `post_batch_approve_orders_with_metadata` interceptor runs after the
        `post_batch_approve_orders` interceptor. The (possibly modified) response returned by
        `post_batch_approve_orders` will be passed to
        `post_batch_approve_orders_with_metadata`.
        """
        return response, metadata

    def pre_batch_approve_orders_without_reservation(
        self,
        request: order_service.BatchApproveOrdersWithoutReservationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        order_service.BatchApproveOrdersWithoutReservationRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_approve_orders_without_reservation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the OrderService server.
        """
        return request, metadata

    def post_batch_approve_orders_without_reservation(
        self, response: order_service.BatchApproveOrdersWithoutReservationResponse
    ) -> order_service.BatchApproveOrdersWithoutReservationResponse:
        """Post-rpc interceptor for batch_approve_orders_without_reservation

        DEPRECATED. Please use the `post_batch_approve_orders_without_reservation_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the OrderService server but before
        it is returned to user code. This `post_batch_approve_orders_without_reservation` interceptor runs
        before the `post_batch_approve_orders_without_reservation_with_metadata` interceptor.
        """
        return response

    def post_batch_approve_orders_without_reservation_with_metadata(
        self,
        response: order_service.BatchApproveOrdersWithoutReservationResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        order_service.BatchApproveOrdersWithoutReservationResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_approve_orders_without_reservation

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the OrderService server but before it is returned to user code.

        We recommend only using this `post_batch_approve_orders_without_reservation_with_metadata`
        interceptor in new development instead of the `post_batch_approve_orders_without_reservation` interceptor.
        When both interceptors are used, this `post_batch_approve_orders_without_reservation_with_metadata` interceptor runs after the
        `post_batch_approve_orders_without_reservation` interceptor. The (possibly modified) response returned by
        `post_batch_approve_orders_without_reservation` will be passed to
        `post_batch_approve_orders_without_reservation_with_metadata`.
        """
        return response, metadata

    def pre_batch_archive_orders(
        self,
        request: order_service.BatchArchiveOrdersRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        order_service.BatchArchiveOrdersRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for batch_archive_orders

        Override in a subclass to manipulate the request or metadata
        before they are sent to the OrderService server.
        """
        return request, metadata

    def post_batch_archive_orders(
        self, response: order_service.BatchArchiveOrdersResponse
    ) -> order_service.BatchArchiveOrdersResponse:
        """Post-rpc interceptor for batch_archive_orders

        DEPRECATED. Please use the `post_batch_archive_orders_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the OrderService server but before
        it is returned to user code. This `post_batch_archive_orders` interceptor runs
        before the `post_batch_archive_orders_with_metadata` interceptor.
        """
        return response

    def post_batch_archive_orders_with_metadata(
        self,
        response: order_service.BatchArchiveOrdersResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        order_service.BatchArchiveOrdersResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_archive_orders

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the OrderService server but before it is returned to user code.

        We recommend only using this `post_batch_archive_orders_with_metadata`
        interceptor in new development instead of the `post_batch_archive_orders` interceptor.
        When both interceptors are used, this `post_batch_archive_orders_with_metadata` interceptor runs after the
        `post_batch_archive_orders` interceptor. The (possibly modified) response returned by
        `post_batch_archive_orders` will be passed to
        `post_batch_archive_orders_with_metadata`.
        """
        return response, metadata

    def pre_batch_create_orders(
        self,
        request: order_service.BatchCreateOrdersRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        order_service.BatchCreateOrdersRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for batch_create_orders

        Override in a subclass to manipulate the request or metadata
        before they are sent to the OrderService server.
        """
        return request, metadata

    def post_batch_create_orders(
        self, response: order_service.BatchCreateOrdersResponse
    ) -> order_service.BatchCreateOrdersResponse:
        """Post-rpc interceptor for batch_create_orders

        DEPRECATED. Please use the `post_batch_create_orders_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the OrderService server but before
        it is returned to user code. This `post_batch_create_orders` interceptor runs
        before the `post_batch_create_orders_with_metadata` interceptor.
        """
        return response

    def post_batch_create_orders_with_metadata(
        self,
        response: order_service.BatchCreateOrdersResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        order_service.BatchCreateOrdersResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for batch_create_orders

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the OrderService server but before it is returned to user code.

        We recommend only using this `post_batch_create_orders_with_metadata`
        interceptor in new development instead of the `post_batch_create_orders` interceptor.
        When both interceptors are used, this `post_batch_create_orders_with_metadata` interceptor runs after the
        `post_batch_create_orders` interceptor. The (possibly modified) response returned by
        `post_batch_create_orders` will be passed to
        `post_batch_create_orders_with_metadata`.
        """
        return response, metadata

    def pre_batch_delete_orders(
        self,
        request: order_service.BatchDeleteOrdersRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        order_service.BatchDeleteOrdersRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for batch_delete_orders

        Override in a subclass to manipulate the request or metadata
        before they are sent to the OrderService server.
        """
        return request, metadata

    def post_batch_delete_orders(
        self, response: order_service.BatchDeleteOrdersResponse
    ) -> order_service.BatchDeleteOrdersResponse:
        """Post-rpc interceptor for batch_delete_orders

        DEPRECATED. Please use the `post_batch_delete_orders_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the OrderService server but before
        it is returned to user code. This `post_batch_delete_orders` interceptor runs
        before the `post_batch_delete_orders_with_metadata` interceptor.
        """
        return response

    def post_batch_delete_orders_with_metadata(
        self,
        response: order_service.BatchDeleteOrdersResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        order_service.BatchDeleteOrdersResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for batch_delete_orders

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the OrderService server but before it is returned to user code.

        We recommend only using this `post_batch_delete_orders_with_metadata`
        interceptor in new development instead of the `post_batch_delete_orders` interceptor.
        When both interceptors are used, this `post_batch_delete_orders_with_metadata` interceptor runs after the
        `post_batch_delete_orders` interceptor. The (possibly modified) response returned by
        `post_batch_delete_orders` will be passed to
        `post_batch_delete_orders_with_metadata`.
        """
        return response, metadata

    def pre_batch_disapprove_orders(
        self,
        request: order_service.BatchDisapproveOrdersRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        order_service.BatchDisapproveOrdersRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_disapprove_orders

        Override in a subclass to manipulate the request or metadata
        before they are sent to the OrderService server.
        """
        return request, metadata

    def post_batch_disapprove_orders(
        self, response: order_service.BatchDisapproveOrdersResponse
    ) -> order_service.BatchDisapproveOrdersResponse:
        """Post-rpc interceptor for batch_disapprove_orders

        DEPRECATED. Please use the `post_batch_disapprove_orders_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the OrderService server but before
        it is returned to user code. This `post_batch_disapprove_orders` interceptor runs
        before the `post_batch_disapprove_orders_with_metadata` interceptor.
        """
        return response

    def post_batch_disapprove_orders_with_metadata(
        self,
        response: order_service.BatchDisapproveOrdersResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        order_service.BatchDisapproveOrdersResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_disapprove_orders

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the OrderService server but before it is returned to user code.

        We recommend only using this `post_batch_disapprove_orders_with_metadata`
        interceptor in new development instead of the `post_batch_disapprove_orders` interceptor.
        When both interceptors are used, this `post_batch_disapprove_orders_with_metadata` interceptor runs after the
        `post_batch_disapprove_orders` interceptor. The (possibly modified) response returned by
        `post_batch_disapprove_orders` will be passed to
        `post_batch_disapprove_orders_with_metadata`.
        """
        return response, metadata

    def pre_batch_disapprove_orders_without_reservation_changes(
        self,
        request: order_service.BatchDisapproveOrdersWithoutReservationChangesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        order_service.BatchDisapproveOrdersWithoutReservationChangesRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_disapprove_orders_without_reservation_changes

        Override in a subclass to manipulate the request or metadata
        before they are sent to the OrderService server.
        """
        return request, metadata

    def post_batch_disapprove_orders_without_reservation_changes(
        self,
        response: order_service.BatchDisapproveOrdersWithoutReservationChangesResponse,
    ) -> order_service.BatchDisapproveOrdersWithoutReservationChangesResponse:
        """Post-rpc interceptor for batch_disapprove_orders_without_reservation_changes

        DEPRECATED. Please use the `post_batch_disapprove_orders_without_reservation_changes_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the OrderService server but before
        it is returned to user code. This `post_batch_disapprove_orders_without_reservation_changes` interceptor runs
        before the `post_batch_disapprove_orders_without_reservation_changes_with_metadata` interceptor.
        """
        return response

    def post_batch_disapprove_orders_without_reservation_changes_with_metadata(
        self,
        response: order_service.BatchDisapproveOrdersWithoutReservationChangesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        order_service.BatchDisapproveOrdersWithoutReservationChangesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_disapprove_orders_without_reservation_changes

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the OrderService server but before it is returned to user code.

        We recommend only using this `post_batch_disapprove_orders_without_reservation_changes_with_metadata`
        interceptor in new development instead of the `post_batch_disapprove_orders_without_reservation_changes` interceptor.
        When both interceptors are used, this `post_batch_disapprove_orders_without_reservation_changes_with_metadata` interceptor runs after the
        `post_batch_disapprove_orders_without_reservation_changes` interceptor. The (possibly modified) response returned by
        `post_batch_disapprove_orders_without_reservation_changes` will be passed to
        `post_batch_disapprove_orders_without_reservation_changes_with_metadata`.
        """
        return response, metadata

    def pre_batch_pause_orders(
        self,
        request: order_service.BatchPauseOrdersRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        order_service.BatchPauseOrdersRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for batch_pause_orders

        Override in a subclass to manipulate the request or metadata
        before they are sent to the OrderService server.
        """
        return request, metadata

    def post_batch_pause_orders(
        self, response: order_service.BatchPauseOrdersResponse
    ) -> order_service.BatchPauseOrdersResponse:
        """Post-rpc interceptor for batch_pause_orders

        DEPRECATED. Please use the `post_batch_pause_orders_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the OrderService server but before
        it is returned to user code. This `post_batch_pause_orders` interceptor runs
        before the `post_batch_pause_orders_with_metadata` interceptor.
        """
        return response

    def post_batch_pause_orders_with_metadata(
        self,
        response: order_service.BatchPauseOrdersResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        order_service.BatchPauseOrdersResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for batch_pause_orders

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the OrderService server but before it is returned to user code.

        We recommend only using this `post_batch_pause_orders_with_metadata`
        interceptor in new development instead of the `post_batch_pause_orders` interceptor.
        When both interceptors are used, this `post_batch_pause_orders_with_metadata` interceptor runs after the
        `post_batch_pause_orders` interceptor. The (possibly modified) response returned by
        `post_batch_pause_orders` will be passed to
        `post_batch_pause_orders_with_metadata`.
        """
        return response, metadata

    def pre_batch_resume_and_overbook_orders(
        self,
        request: order_service.BatchResumeAndOverbookOrdersRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        order_service.BatchResumeAndOverbookOrdersRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_resume_and_overbook_orders

        Override in a subclass to manipulate the request or metadata
        before they are sent to the OrderService server.
        """
        return request, metadata

    def post_batch_resume_and_overbook_orders(
        self, response: order_service.BatchResumeAndOverbookOrdersResponse
    ) -> order_service.BatchResumeAndOverbookOrdersResponse:
        """Post-rpc interceptor for batch_resume_and_overbook_orders

        DEPRECATED. Please use the `post_batch_resume_and_overbook_orders_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the OrderService server but before
        it is returned to user code. This `post_batch_resume_and_overbook_orders` interceptor runs
        before the `post_batch_resume_and_overbook_orders_with_metadata` interceptor.
        """
        return response

    def post_batch_resume_and_overbook_orders_with_metadata(
        self,
        response: order_service.BatchResumeAndOverbookOrdersResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        order_service.BatchResumeAndOverbookOrdersResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_resume_and_overbook_orders

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the OrderService server but before it is returned to user code.

        We recommend only using this `post_batch_resume_and_overbook_orders_with_metadata`
        interceptor in new development instead of the `post_batch_resume_and_overbook_orders` interceptor.
        When both interceptors are used, this `post_batch_resume_and_overbook_orders_with_metadata` interceptor runs after the
        `post_batch_resume_and_overbook_orders` interceptor. The (possibly modified) response returned by
        `post_batch_resume_and_overbook_orders` will be passed to
        `post_batch_resume_and_overbook_orders_with_metadata`.
        """
        return response, metadata

    def pre_batch_resume_orders(
        self,
        request: order_service.BatchResumeOrdersRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        order_service.BatchResumeOrdersRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for batch_resume_orders

        Override in a subclass to manipulate the request or metadata
        before they are sent to the OrderService server.
        """
        return request, metadata

    def post_batch_resume_orders(
        self, response: order_service.BatchResumeOrdersResponse
    ) -> order_service.BatchResumeOrdersResponse:
        """Post-rpc interceptor for batch_resume_orders

        DEPRECATED. Please use the `post_batch_resume_orders_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the OrderService server but before
        it is returned to user code. This `post_batch_resume_orders` interceptor runs
        before the `post_batch_resume_orders_with_metadata` interceptor.
        """
        return response

    def post_batch_resume_orders_with_metadata(
        self,
        response: order_service.BatchResumeOrdersResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        order_service.BatchResumeOrdersResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for batch_resume_orders

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the OrderService server but before it is returned to user code.

        We recommend only using this `post_batch_resume_orders_with_metadata`
        interceptor in new development instead of the `post_batch_resume_orders` interceptor.
        When both interceptors are used, this `post_batch_resume_orders_with_metadata` interceptor runs after the
        `post_batch_resume_orders` interceptor. The (possibly modified) response returned by
        `post_batch_resume_orders` will be passed to
        `post_batch_resume_orders_with_metadata`.
        """
        return response, metadata

    def pre_batch_retract_orders(
        self,
        request: order_service.BatchRetractOrdersRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        order_service.BatchRetractOrdersRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for batch_retract_orders

        Override in a subclass to manipulate the request or metadata
        before they are sent to the OrderService server.
        """
        return request, metadata

    def post_batch_retract_orders(
        self, response: order_service.BatchRetractOrdersResponse
    ) -> order_service.BatchRetractOrdersResponse:
        """Post-rpc interceptor for batch_retract_orders

        DEPRECATED. Please use the `post_batch_retract_orders_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the OrderService server but before
        it is returned to user code. This `post_batch_retract_orders` interceptor runs
        before the `post_batch_retract_orders_with_metadata` interceptor.
        """
        return response

    def post_batch_retract_orders_with_metadata(
        self,
        response: order_service.BatchRetractOrdersResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        order_service.BatchRetractOrdersResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_retract_orders

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the OrderService server but before it is returned to user code.

        We recommend only using this `post_batch_retract_orders_with_metadata`
        interceptor in new development instead of the `post_batch_retract_orders` interceptor.
        When both interceptors are used, this `post_batch_retract_orders_with_metadata` interceptor runs after the
        `post_batch_retract_orders` interceptor. The (possibly modified) response returned by
        `post_batch_retract_orders` will be passed to
        `post_batch_retract_orders_with_metadata`.
        """
        return response, metadata

    def pre_batch_retract_orders_without_reservation_changes(
        self,
        request: order_service.BatchRetractOrdersWithoutReservationChangesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        order_service.BatchRetractOrdersWithoutReservationChangesRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_retract_orders_without_reservation_changes

        Override in a subclass to manipulate the request or metadata
        before they are sent to the OrderService server.
        """
        return request, metadata

    def post_batch_retract_orders_without_reservation_changes(
        self,
        response: order_service.BatchRetractOrdersWithoutReservationChangesResponse,
    ) -> order_service.BatchRetractOrdersWithoutReservationChangesResponse:
        """Post-rpc interceptor for batch_retract_orders_without_reservation_changes

        DEPRECATED. Please use the `post_batch_retract_orders_without_reservation_changes_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the OrderService server but before
        it is returned to user code. This `post_batch_retract_orders_without_reservation_changes` interceptor runs
        before the `post_batch_retract_orders_without_reservation_changes_with_metadata` interceptor.
        """
        return response

    def post_batch_retract_orders_without_reservation_changes_with_metadata(
        self,
        response: order_service.BatchRetractOrdersWithoutReservationChangesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        order_service.BatchRetractOrdersWithoutReservationChangesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_retract_orders_without_reservation_changes

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the OrderService server but before it is returned to user code.

        We recommend only using this `post_batch_retract_orders_without_reservation_changes_with_metadata`
        interceptor in new development instead of the `post_batch_retract_orders_without_reservation_changes` interceptor.
        When both interceptors are used, this `post_batch_retract_orders_without_reservation_changes_with_metadata` interceptor runs after the
        `post_batch_retract_orders_without_reservation_changes` interceptor. The (possibly modified) response returned by
        `post_batch_retract_orders_without_reservation_changes` will be passed to
        `post_batch_retract_orders_without_reservation_changes_with_metadata`.
        """
        return response, metadata

    def pre_batch_submit_orders_for_approval(
        self,
        request: order_service.BatchSubmitOrdersForApprovalRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        order_service.BatchSubmitOrdersForApprovalRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_submit_orders_for_approval

        Override in a subclass to manipulate the request or metadata
        before they are sent to the OrderService server.
        """
        return request, metadata

    def post_batch_submit_orders_for_approval(
        self, response: order_service.BatchSubmitOrdersForApprovalResponse
    ) -> order_service.BatchSubmitOrdersForApprovalResponse:
        """Post-rpc interceptor for batch_submit_orders_for_approval

        DEPRECATED. Please use the `post_batch_submit_orders_for_approval_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the OrderService server but before
        it is returned to user code. This `post_batch_submit_orders_for_approval` interceptor runs
        before the `post_batch_submit_orders_for_approval_with_metadata` interceptor.
        """
        return response

    def post_batch_submit_orders_for_approval_with_metadata(
        self,
        response: order_service.BatchSubmitOrdersForApprovalResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        order_service.BatchSubmitOrdersForApprovalResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_submit_orders_for_approval

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the OrderService server but before it is returned to user code.

        We recommend only using this `post_batch_submit_orders_for_approval_with_metadata`
        interceptor in new development instead of the `post_batch_submit_orders_for_approval` interceptor.
        When both interceptors are used, this `post_batch_submit_orders_for_approval_with_metadata` interceptor runs after the
        `post_batch_submit_orders_for_approval` interceptor. The (possibly modified) response returned by
        `post_batch_submit_orders_for_approval` will be passed to
        `post_batch_submit_orders_for_approval_with_metadata`.
        """
        return response, metadata

    def pre_batch_submit_orders_for_approval_and_overbook(
        self,
        request: order_service.BatchSubmitOrdersForApprovalAndOverbookRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        order_service.BatchSubmitOrdersForApprovalAndOverbookRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_submit_orders_for_approval_and_overbook

        Override in a subclass to manipulate the request or metadata
        before they are sent to the OrderService server.
        """
        return request, metadata

    def post_batch_submit_orders_for_approval_and_overbook(
        self, response: order_service.BatchSubmitOrdersForApprovalAndOverbookResponse
    ) -> order_service.BatchSubmitOrdersForApprovalAndOverbookResponse:
        """Post-rpc interceptor for batch_submit_orders_for_approval_and_overbook

        DEPRECATED. Please use the `post_batch_submit_orders_for_approval_and_overbook_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the OrderService server but before
        it is returned to user code. This `post_batch_submit_orders_for_approval_and_overbook` interceptor runs
        before the `post_batch_submit_orders_for_approval_and_overbook_with_metadata` interceptor.
        """
        return response

    def post_batch_submit_orders_for_approval_and_overbook_with_metadata(
        self,
        response: order_service.BatchSubmitOrdersForApprovalAndOverbookResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        order_service.BatchSubmitOrdersForApprovalAndOverbookResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_submit_orders_for_approval_and_overbook

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the OrderService server but before it is returned to user code.

        We recommend only using this `post_batch_submit_orders_for_approval_and_overbook_with_metadata`
        interceptor in new development instead of the `post_batch_submit_orders_for_approval_and_overbook` interceptor.
        When both interceptors are used, this `post_batch_submit_orders_for_approval_and_overbook_with_metadata` interceptor runs after the
        `post_batch_submit_orders_for_approval_and_overbook` interceptor. The (possibly modified) response returned by
        `post_batch_submit_orders_for_approval_and_overbook` will be passed to
        `post_batch_submit_orders_for_approval_and_overbook_with_metadata`.
        """
        return response, metadata

    def pre_batch_submit_orders_for_approval_without_reservation_changes(
        self,
        request: order_service.BatchSubmitOrdersForApprovalWithoutReservationChangesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        order_service.BatchSubmitOrdersForApprovalWithoutReservationChangesRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_submit_orders_for_approval_without_reservation_changes

        Override in a subclass to manipulate the request or metadata
        before they are sent to the OrderService server.
        """
        return request, metadata

    def post_batch_submit_orders_for_approval_without_reservation_changes(
        self,
        response: order_service.BatchSubmitOrdersForApprovalWithoutReservationChangesResponse,
    ) -> order_service.BatchSubmitOrdersForApprovalWithoutReservationChangesResponse:
        """Post-rpc interceptor for batch_submit_orders_for_approval_without_reservation_changes

        DEPRECATED. Please use the `post_batch_submit_orders_for_approval_without_reservation_changes_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the OrderService server but before
        it is returned to user code. This `post_batch_submit_orders_for_approval_without_reservation_changes` interceptor runs
        before the `post_batch_submit_orders_for_approval_without_reservation_changes_with_metadata` interceptor.
        """
        return response

    def post_batch_submit_orders_for_approval_without_reservation_changes_with_metadata(
        self,
        response: order_service.BatchSubmitOrdersForApprovalWithoutReservationChangesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        order_service.BatchSubmitOrdersForApprovalWithoutReservationChangesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_submit_orders_for_approval_without_reservation_changes

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the OrderService server but before it is returned to user code.

        We recommend only using this `post_batch_submit_orders_for_approval_without_reservation_changes_with_metadata`
        interceptor in new development instead of the `post_batch_submit_orders_for_approval_without_reservation_changes` interceptor.
        When both interceptors are used, this `post_batch_submit_orders_for_approval_without_reservation_changes_with_metadata` interceptor runs after the
        `post_batch_submit_orders_for_approval_without_reservation_changes` interceptor. The (possibly modified) response returned by
        `post_batch_submit_orders_for_approval_without_reservation_changes` will be passed to
        `post_batch_submit_orders_for_approval_without_reservation_changes_with_metadata`.
        """
        return response, metadata

    def pre_batch_unarchive_orders(
        self,
        request: order_service.BatchUnarchiveOrdersRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        order_service.BatchUnarchiveOrdersRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_unarchive_orders

        Override in a subclass to manipulate the request or metadata
        before they are sent to the OrderService server.
        """
        return request, metadata

    def post_batch_unarchive_orders(
        self, response: order_service.BatchUnarchiveOrdersResponse
    ) -> order_service.BatchUnarchiveOrdersResponse:
        """Post-rpc interceptor for batch_unarchive_orders

        DEPRECATED. Please use the `post_batch_unarchive_orders_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the OrderService server but before
        it is returned to user code. This `post_batch_unarchive_orders` interceptor runs
        before the `post_batch_unarchive_orders_with_metadata` interceptor.
        """
        return response

    def post_batch_unarchive_orders_with_metadata(
        self,
        response: order_service.BatchUnarchiveOrdersResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        order_service.BatchUnarchiveOrdersResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_unarchive_orders

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the OrderService server but before it is returned to user code.

        We recommend only using this `post_batch_unarchive_orders_with_metadata`
        interceptor in new development instead of the `post_batch_unarchive_orders` interceptor.
        When both interceptors are used, this `post_batch_unarchive_orders_with_metadata` interceptor runs after the
        `post_batch_unarchive_orders` interceptor. The (possibly modified) response returned by
        `post_batch_unarchive_orders` will be passed to
        `post_batch_unarchive_orders_with_metadata`.
        """
        return response, metadata

    def pre_batch_update_orders(
        self,
        request: order_service.BatchUpdateOrdersRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        order_service.BatchUpdateOrdersRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for batch_update_orders

        Override in a subclass to manipulate the request or metadata
        before they are sent to the OrderService server.
        """
        return request, metadata

    def post_batch_update_orders(
        self, response: order_service.BatchUpdateOrdersResponse
    ) -> order_service.BatchUpdateOrdersResponse:
        """Post-rpc interceptor for batch_update_orders

        DEPRECATED. Please use the `post_batch_update_orders_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the OrderService server but before
        it is returned to user code. This `post_batch_update_orders` interceptor runs
        before the `post_batch_update_orders_with_metadata` interceptor.
        """
        return response

    def post_batch_update_orders_with_metadata(
        self,
        response: order_service.BatchUpdateOrdersResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        order_service.BatchUpdateOrdersResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for batch_update_orders

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the OrderService server but before it is returned to user code.

        We recommend only using this `post_batch_update_orders_with_metadata`
        interceptor in new development instead of the `post_batch_update_orders` interceptor.
        When both interceptors are used, this `post_batch_update_orders_with_metadata` interceptor runs after the
        `post_batch_update_orders` interceptor. The (possibly modified) response returned by
        `post_batch_update_orders` will be passed to
        `post_batch_update_orders_with_metadata`.
        """
        return response, metadata

    def pre_get_order(
        self,
        request: order_service.GetOrderRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[order_service.GetOrderRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_order

        Override in a subclass to manipulate the request or metadata
        before they are sent to the OrderService server.
        """
        return request, metadata

    def post_get_order(self, response: order_messages.Order) -> order_messages.Order:
        """Post-rpc interceptor for get_order

        DEPRECATED. Please use the `post_get_order_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the OrderService server but before
        it is returned to user code. This `post_get_order` interceptor runs
        before the `post_get_order_with_metadata` interceptor.
        """
        return response

    def post_get_order_with_metadata(
        self,
        response: order_messages.Order,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[order_messages.Order, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_order

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the OrderService server but before it is returned to user code.

        We recommend only using this `post_get_order_with_metadata`
        interceptor in new development instead of the `post_get_order` interceptor.
        When both interceptors are used, this `post_get_order_with_metadata` interceptor runs after the
        `post_get_order` interceptor. The (possibly modified) response returned by
        `post_get_order` will be passed to
        `post_get_order_with_metadata`.
        """
        return response, metadata

    def pre_list_orders(
        self,
        request: order_service.ListOrdersRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        order_service.ListOrdersRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_orders

        Override in a subclass to manipulate the request or metadata
        before they are sent to the OrderService server.
        """
        return request, metadata

    def post_list_orders(
        self, response: order_service.ListOrdersResponse
    ) -> order_service.ListOrdersResponse:
        """Post-rpc interceptor for list_orders

        DEPRECATED. Please use the `post_list_orders_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the OrderService server but before
        it is returned to user code. This `post_list_orders` interceptor runs
        before the `post_list_orders_with_metadata` interceptor.
        """
        return response

    def post_list_orders_with_metadata(
        self,
        response: order_service.ListOrdersResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        order_service.ListOrdersResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_orders

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the OrderService server but before it is returned to user code.

        We recommend only using this `post_list_orders_with_metadata`
        interceptor in new development instead of the `post_list_orders` interceptor.
        When both interceptors are used, this `post_list_orders_with_metadata` interceptor runs after the
        `post_list_orders` interceptor. The (possibly modified) response returned by
        `post_list_orders` will be passed to
        `post_list_orders_with_metadata`.
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
        before they are sent to the OrderService server.
        """
        return request, metadata

    def post_cancel_operation(self, response: None) -> None:
        """Post-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the response
        after it is returned by the OrderService server but before
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
        before they are sent to the OrderService server.
        """
        return request, metadata

    def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the OrderService server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class OrderServiceRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: OrderServiceRestInterceptor


class OrderServiceRestTransport(_BaseOrderServiceRestTransport):
    """REST backend synchronous transport for OrderService.

    Provides methods for handling ``Order`` objects.

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
        interceptor: Optional[OrderServiceRestInterceptor] = None,
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
            interceptor (Optional[OrderServiceRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or OrderServiceRestInterceptor()
        self._prep_wrapped_messages(client_info)

    class _BatchApproveAndOverbookOrders(
        _BaseOrderServiceRestTransport._BaseBatchApproveAndOverbookOrders,
        OrderServiceRestStub,
    ):
        def __hash__(self):
            return hash("OrderServiceRestTransport.BatchApproveAndOverbookOrders")

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
            request: order_service.BatchApproveAndOverbookOrdersRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> order_service.BatchApproveAndOverbookOrdersResponse:
            r"""Call the batch approve and
            overbook orders method over HTTP.

                Args:
                    request (~.order_service.BatchApproveAndOverbookOrdersRequest):
                        The request object. Request message for ``BatchApproveAndOverbookOrders``
                    method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.order_service.BatchApproveAndOverbookOrdersResponse:
                        Response object for ``BatchApproveAndOverbookOrders``
                    method.

            """

            http_options = _BaseOrderServiceRestTransport._BaseBatchApproveAndOverbookOrders._get_http_options()
            request, metadata = self._interceptor.pre_batch_approve_and_overbook_orders(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseOrderServiceRestTransport._BaseBatchApproveAndOverbookOrders,
                    "_BaseBatchApproveAndOverbookOrders__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.OrderServiceClient.BatchApproveAndOverbookOrders",
                    extra={
                        "serviceName": "google.ads.admanager.v1.OrderService",
                        "rpcName": "BatchApproveAndOverbookOrders",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                OrderServiceRestTransport._BatchApproveAndOverbookOrders._get_response(
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
            resp = order_service.BatchApproveAndOverbookOrdersResponse()
            pb_resp = order_service.BatchApproveAndOverbookOrdersResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_approve_and_overbook_orders(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_batch_approve_and_overbook_orders_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        order_service.BatchApproveAndOverbookOrdersResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.OrderServiceClient.batch_approve_and_overbook_orders",
                    extra={
                        "serviceName": "google.ads.admanager.v1.OrderService",
                        "rpcName": "BatchApproveAndOverbookOrders",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BatchApproveOrders(
        _BaseOrderServiceRestTransport._BaseBatchApproveOrders, OrderServiceRestStub
    ):
        def __hash__(self):
            return hash("OrderServiceRestTransport.BatchApproveOrders")

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
            request: order_service.BatchApproveOrdersRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> order_service.BatchApproveOrdersResponse:
            r"""Call the batch approve orders method over HTTP.

            Args:
                request (~.order_service.BatchApproveOrdersRequest):
                    The request object. Request message for ``BatchApproveOrders`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.order_service.BatchApproveOrdersResponse:
                    Response object for ``BatchApproveOrders`` method.
            """

            http_options = _BaseOrderServiceRestTransport._BaseBatchApproveOrders._get_http_options()
            request, metadata = self._interceptor.pre_batch_approve_orders(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseOrderServiceRestTransport._BaseBatchApproveOrders,
                    "_BaseBatchApproveOrders__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.OrderServiceClient.BatchApproveOrders",
                    extra={
                        "serviceName": "google.ads.admanager.v1.OrderService",
                        "rpcName": "BatchApproveOrders",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = OrderServiceRestTransport._BatchApproveOrders._get_response(
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
            resp = order_service.BatchApproveOrdersResponse()
            pb_resp = order_service.BatchApproveOrdersResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_approve_orders(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_batch_approve_orders_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = order_service.BatchApproveOrdersResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.OrderServiceClient.batch_approve_orders",
                    extra={
                        "serviceName": "google.ads.admanager.v1.OrderService",
                        "rpcName": "BatchApproveOrders",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BatchApproveOrdersWithoutReservation(
        _BaseOrderServiceRestTransport._BaseBatchApproveOrdersWithoutReservation,
        OrderServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "OrderServiceRestTransport.BatchApproveOrdersWithoutReservation"
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
            request: order_service.BatchApproveOrdersWithoutReservationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> order_service.BatchApproveOrdersWithoutReservationResponse:
            r"""Call the batch approve orders
            without reservation method over HTTP.

                Args:
                    request (~.order_service.BatchApproveOrdersWithoutReservationRequest):
                        The request object. Request message for
                    ``BatchApproveOrdersWithoutReservation`` method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.order_service.BatchApproveOrdersWithoutReservationResponse:
                        Response object for
                    ``BatchApproveOrdersWithoutReservation`` method.

            """

            http_options = _BaseOrderServiceRestTransport._BaseBatchApproveOrdersWithoutReservation._get_http_options()
            request, metadata = (
                self._interceptor.pre_batch_approve_orders_without_reservation(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseOrderServiceRestTransport._BaseBatchApproveOrdersWithoutReservation,
                    "_BaseBatchApproveOrdersWithoutReservation__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.OrderServiceClient.BatchApproveOrdersWithoutReservation",
                    extra={
                        "serviceName": "google.ads.admanager.v1.OrderService",
                        "rpcName": "BatchApproveOrdersWithoutReservation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = OrderServiceRestTransport._BatchApproveOrdersWithoutReservation._get_response(
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
            resp = order_service.BatchApproveOrdersWithoutReservationResponse()
            pb_resp = order_service.BatchApproveOrdersWithoutReservationResponse.pb(
                resp
            )

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_approve_orders_without_reservation(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_batch_approve_orders_without_reservation_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = order_service.BatchApproveOrdersWithoutReservationResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.OrderServiceClient.batch_approve_orders_without_reservation",
                    extra={
                        "serviceName": "google.ads.admanager.v1.OrderService",
                        "rpcName": "BatchApproveOrdersWithoutReservation",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BatchArchiveOrders(
        _BaseOrderServiceRestTransport._BaseBatchArchiveOrders, OrderServiceRestStub
    ):
        def __hash__(self):
            return hash("OrderServiceRestTransport.BatchArchiveOrders")

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
            request: order_service.BatchArchiveOrdersRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> order_service.BatchArchiveOrdersResponse:
            r"""Call the batch archive orders method over HTTP.

            Args:
                request (~.order_service.BatchArchiveOrdersRequest):
                    The request object. Request message for ``BatchArchiveOrders`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.order_service.BatchArchiveOrdersResponse:
                    Response object for ``BatchArchiveOrders`` method.
            """

            http_options = _BaseOrderServiceRestTransport._BaseBatchArchiveOrders._get_http_options()
            request, metadata = self._interceptor.pre_batch_archive_orders(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseOrderServiceRestTransport._BaseBatchArchiveOrders,
                    "_BaseBatchArchiveOrders__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.OrderServiceClient.BatchArchiveOrders",
                    extra={
                        "serviceName": "google.ads.admanager.v1.OrderService",
                        "rpcName": "BatchArchiveOrders",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = OrderServiceRestTransport._BatchArchiveOrders._get_response(
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
            resp = order_service.BatchArchiveOrdersResponse()
            pb_resp = order_service.BatchArchiveOrdersResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_archive_orders(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_batch_archive_orders_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = order_service.BatchArchiveOrdersResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.OrderServiceClient.batch_archive_orders",
                    extra={
                        "serviceName": "google.ads.admanager.v1.OrderService",
                        "rpcName": "BatchArchiveOrders",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BatchCreateOrders(
        _BaseOrderServiceRestTransport._BaseBatchCreateOrders, OrderServiceRestStub
    ):
        def __hash__(self):
            return hash("OrderServiceRestTransport.BatchCreateOrders")

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
            request: order_service.BatchCreateOrdersRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> order_service.BatchCreateOrdersResponse:
            r"""Call the batch create orders method over HTTP.

            Args:
                request (~.order_service.BatchCreateOrdersRequest):
                    The request object. Request object for ``BatchCreateOrders`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.order_service.BatchCreateOrdersResponse:
                    Response object for ``BatchCreateOrders`` method.
            """

            http_options = _BaseOrderServiceRestTransport._BaseBatchCreateOrders._get_http_options()
            request, metadata = self._interceptor.pre_batch_create_orders(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseOrderServiceRestTransport._BaseBatchCreateOrders,
                    "_BaseBatchCreateOrders__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.OrderServiceClient.BatchCreateOrders",
                    extra={
                        "serviceName": "google.ads.admanager.v1.OrderService",
                        "rpcName": "BatchCreateOrders",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = OrderServiceRestTransport._BatchCreateOrders._get_response(
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
            resp = order_service.BatchCreateOrdersResponse()
            pb_resp = order_service.BatchCreateOrdersResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_create_orders(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_batch_create_orders_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = order_service.BatchCreateOrdersResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.OrderServiceClient.batch_create_orders",
                    extra={
                        "serviceName": "google.ads.admanager.v1.OrderService",
                        "rpcName": "BatchCreateOrders",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BatchDeleteOrders(
        _BaseOrderServiceRestTransport._BaseBatchDeleteOrders, OrderServiceRestStub
    ):
        def __hash__(self):
            return hash("OrderServiceRestTransport.BatchDeleteOrders")

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
            request: order_service.BatchDeleteOrdersRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> order_service.BatchDeleteOrdersResponse:
            r"""Call the batch delete orders method over HTTP.

            Args:
                request (~.order_service.BatchDeleteOrdersRequest):
                    The request object. Request message for ``BatchDeleteOrders`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.order_service.BatchDeleteOrdersResponse:
                    Response object for ``BatchDeleteOrders`` method.
            """

            http_options = _BaseOrderServiceRestTransport._BaseBatchDeleteOrders._get_http_options()
            request, metadata = self._interceptor.pre_batch_delete_orders(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseOrderServiceRestTransport._BaseBatchDeleteOrders,
                    "_BaseBatchDeleteOrders__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.OrderServiceClient.BatchDeleteOrders",
                    extra={
                        "serviceName": "google.ads.admanager.v1.OrderService",
                        "rpcName": "BatchDeleteOrders",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = OrderServiceRestTransport._BatchDeleteOrders._get_response(
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
            resp = order_service.BatchDeleteOrdersResponse()
            pb_resp = order_service.BatchDeleteOrdersResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_delete_orders(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_batch_delete_orders_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = order_service.BatchDeleteOrdersResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.OrderServiceClient.batch_delete_orders",
                    extra={
                        "serviceName": "google.ads.admanager.v1.OrderService",
                        "rpcName": "BatchDeleteOrders",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BatchDisapproveOrders(
        _BaseOrderServiceRestTransport._BaseBatchDisapproveOrders, OrderServiceRestStub
    ):
        def __hash__(self):
            return hash("OrderServiceRestTransport.BatchDisapproveOrders")

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
            request: order_service.BatchDisapproveOrdersRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> order_service.BatchDisapproveOrdersResponse:
            r"""Call the batch disapprove orders method over HTTP.

            Args:
                request (~.order_service.BatchDisapproveOrdersRequest):
                    The request object. Request message for ``BatchDisapproveOrders`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.order_service.BatchDisapproveOrdersResponse:
                    Response object for ``BatchDisapproveOrders`` method.
            """

            http_options = _BaseOrderServiceRestTransport._BaseBatchDisapproveOrders._get_http_options()
            request, metadata = self._interceptor.pre_batch_disapprove_orders(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseOrderServiceRestTransport._BaseBatchDisapproveOrders,
                    "_BaseBatchDisapproveOrders__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.OrderServiceClient.BatchDisapproveOrders",
                    extra={
                        "serviceName": "google.ads.admanager.v1.OrderService",
                        "rpcName": "BatchDisapproveOrders",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = OrderServiceRestTransport._BatchDisapproveOrders._get_response(
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
            resp = order_service.BatchDisapproveOrdersResponse()
            pb_resp = order_service.BatchDisapproveOrdersResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_disapprove_orders(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_batch_disapprove_orders_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        order_service.BatchDisapproveOrdersResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.ads.admanager_v1.OrderServiceClient.batch_disapprove_orders",
                    extra={
                        "serviceName": "google.ads.admanager.v1.OrderService",
                        "rpcName": "BatchDisapproveOrders",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BatchDisapproveOrdersWithoutReservationChanges(
        _BaseOrderServiceRestTransport._BaseBatchDisapproveOrdersWithoutReservationChanges,
        OrderServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "OrderServiceRestTransport.BatchDisapproveOrdersWithoutReservationChanges"
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
            request: order_service.BatchDisapproveOrdersWithoutReservationChangesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> order_service.BatchDisapproveOrdersWithoutReservationChangesResponse:
            r"""Call the batch disapprove orders
            without reservation changes method over HTTP.

                Args:
                    request (~.order_service.BatchDisapproveOrdersWithoutReservationChangesRequest):
                        The request object. Request message for
                    ``BatchDisapproveOrdersWithoutReservationChanges``
                    method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.order_service.BatchDisapproveOrdersWithoutReservationChangesResponse:
                        Response object for
                    ``BatchDisapproveOrdersWithoutReservationChanges``
                    method.

            """

            http_options = _BaseOrderServiceRestTransport._BaseBatchDisapproveOrdersWithoutReservationChanges._get_http_options()
            request, metadata = (
                self._interceptor.pre_batch_disapprove_orders_without_reservation_changes(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseOrderServiceRestTransport._BaseBatchDisapproveOrdersWithoutReservationChanges,
                    "_BaseBatchDisapproveOrdersWithoutReservationChanges__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.OrderServiceClient.BatchDisapproveOrdersWithoutReservationChanges",
                    extra={
                        "serviceName": "google.ads.admanager.v1.OrderService",
                        "rpcName": "BatchDisapproveOrdersWithoutReservationChanges",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = OrderServiceRestTransport._BatchDisapproveOrdersWithoutReservationChanges._get_response(
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
            resp = (
                order_service.BatchDisapproveOrdersWithoutReservationChangesResponse()
            )
            pb_resp = (
                order_service.BatchDisapproveOrdersWithoutReservationChangesResponse.pb(
                    resp
                )
            )

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_disapprove_orders_without_reservation_changes(
                resp
            )
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_batch_disapprove_orders_without_reservation_changes_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = order_service.BatchDisapproveOrdersWithoutReservationChangesResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.OrderServiceClient.batch_disapprove_orders_without_reservation_changes",
                    extra={
                        "serviceName": "google.ads.admanager.v1.OrderService",
                        "rpcName": "BatchDisapproveOrdersWithoutReservationChanges",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BatchPauseOrders(
        _BaseOrderServiceRestTransport._BaseBatchPauseOrders, OrderServiceRestStub
    ):
        def __hash__(self):
            return hash("OrderServiceRestTransport.BatchPauseOrders")

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
            request: order_service.BatchPauseOrdersRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> order_service.BatchPauseOrdersResponse:
            r"""Call the batch pause orders method over HTTP.

            Args:
                request (~.order_service.BatchPauseOrdersRequest):
                    The request object. Request message for ``BatchPauseOrders`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.order_service.BatchPauseOrdersResponse:
                    Response object for ``BatchPauseOrders`` method.
            """

            http_options = (
                _BaseOrderServiceRestTransport._BaseBatchPauseOrders._get_http_options()
            )
            request, metadata = self._interceptor.pre_batch_pause_orders(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseOrderServiceRestTransport._BaseBatchPauseOrders,
                    "_BaseBatchPauseOrders__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.OrderServiceClient.BatchPauseOrders",
                    extra={
                        "serviceName": "google.ads.admanager.v1.OrderService",
                        "rpcName": "BatchPauseOrders",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = OrderServiceRestTransport._BatchPauseOrders._get_response(
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
            resp = order_service.BatchPauseOrdersResponse()
            pb_resp = order_service.BatchPauseOrdersResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_pause_orders(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_batch_pause_orders_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = order_service.BatchPauseOrdersResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.OrderServiceClient.batch_pause_orders",
                    extra={
                        "serviceName": "google.ads.admanager.v1.OrderService",
                        "rpcName": "BatchPauseOrders",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BatchResumeAndOverbookOrders(
        _BaseOrderServiceRestTransport._BaseBatchResumeAndOverbookOrders,
        OrderServiceRestStub,
    ):
        def __hash__(self):
            return hash("OrderServiceRestTransport.BatchResumeAndOverbookOrders")

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
            request: order_service.BatchResumeAndOverbookOrdersRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> order_service.BatchResumeAndOverbookOrdersResponse:
            r"""Call the batch resume and overbook
            orders method over HTTP.

                Args:
                    request (~.order_service.BatchResumeAndOverbookOrdersRequest):
                        The request object. Request message for ``BatchResumeAndOverbookOrders``
                    method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.order_service.BatchResumeAndOverbookOrdersResponse:
                        Response object for ``BatchResumeAndOverbookOrders``
                    method.

            """

            http_options = _BaseOrderServiceRestTransport._BaseBatchResumeAndOverbookOrders._get_http_options()
            request, metadata = self._interceptor.pre_batch_resume_and_overbook_orders(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseOrderServiceRestTransport._BaseBatchResumeAndOverbookOrders,
                    "_BaseBatchResumeAndOverbookOrders__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.OrderServiceClient.BatchResumeAndOverbookOrders",
                    extra={
                        "serviceName": "google.ads.admanager.v1.OrderService",
                        "rpcName": "BatchResumeAndOverbookOrders",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                OrderServiceRestTransport._BatchResumeAndOverbookOrders._get_response(
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
            resp = order_service.BatchResumeAndOverbookOrdersResponse()
            pb_resp = order_service.BatchResumeAndOverbookOrdersResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_resume_and_overbook_orders(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_batch_resume_and_overbook_orders_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        order_service.BatchResumeAndOverbookOrdersResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.OrderServiceClient.batch_resume_and_overbook_orders",
                    extra={
                        "serviceName": "google.ads.admanager.v1.OrderService",
                        "rpcName": "BatchResumeAndOverbookOrders",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BatchResumeOrders(
        _BaseOrderServiceRestTransport._BaseBatchResumeOrders, OrderServiceRestStub
    ):
        def __hash__(self):
            return hash("OrderServiceRestTransport.BatchResumeOrders")

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
            request: order_service.BatchResumeOrdersRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> order_service.BatchResumeOrdersResponse:
            r"""Call the batch resume orders method over HTTP.

            Args:
                request (~.order_service.BatchResumeOrdersRequest):
                    The request object. Request message for ``BatchResumeOrders`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.order_service.BatchResumeOrdersResponse:
                    Response object for ``BatchResumeOrders`` method.
            """

            http_options = _BaseOrderServiceRestTransport._BaseBatchResumeOrders._get_http_options()
            request, metadata = self._interceptor.pre_batch_resume_orders(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseOrderServiceRestTransport._BaseBatchResumeOrders,
                    "_BaseBatchResumeOrders__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.OrderServiceClient.BatchResumeOrders",
                    extra={
                        "serviceName": "google.ads.admanager.v1.OrderService",
                        "rpcName": "BatchResumeOrders",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = OrderServiceRestTransport._BatchResumeOrders._get_response(
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
            resp = order_service.BatchResumeOrdersResponse()
            pb_resp = order_service.BatchResumeOrdersResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_resume_orders(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_batch_resume_orders_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = order_service.BatchResumeOrdersResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.OrderServiceClient.batch_resume_orders",
                    extra={
                        "serviceName": "google.ads.admanager.v1.OrderService",
                        "rpcName": "BatchResumeOrders",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BatchRetractOrders(
        _BaseOrderServiceRestTransport._BaseBatchRetractOrders, OrderServiceRestStub
    ):
        def __hash__(self):
            return hash("OrderServiceRestTransport.BatchRetractOrders")

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
            request: order_service.BatchRetractOrdersRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> order_service.BatchRetractOrdersResponse:
            r"""Call the batch retract orders method over HTTP.

            Args:
                request (~.order_service.BatchRetractOrdersRequest):
                    The request object. Request message for ``BatchRetractOrders`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.order_service.BatchRetractOrdersResponse:
                    Response object for ``BatchRetractOrders`` method.
            """

            http_options = _BaseOrderServiceRestTransport._BaseBatchRetractOrders._get_http_options()
            request, metadata = self._interceptor.pre_batch_retract_orders(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseOrderServiceRestTransport._BaseBatchRetractOrders,
                    "_BaseBatchRetractOrders__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.OrderServiceClient.BatchRetractOrders",
                    extra={
                        "serviceName": "google.ads.admanager.v1.OrderService",
                        "rpcName": "BatchRetractOrders",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = OrderServiceRestTransport._BatchRetractOrders._get_response(
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
            resp = order_service.BatchRetractOrdersResponse()
            pb_resp = order_service.BatchRetractOrdersResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_retract_orders(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_batch_retract_orders_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = order_service.BatchRetractOrdersResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.OrderServiceClient.batch_retract_orders",
                    extra={
                        "serviceName": "google.ads.admanager.v1.OrderService",
                        "rpcName": "BatchRetractOrders",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BatchRetractOrdersWithoutReservationChanges(
        _BaseOrderServiceRestTransport._BaseBatchRetractOrdersWithoutReservationChanges,
        OrderServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "OrderServiceRestTransport.BatchRetractOrdersWithoutReservationChanges"
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
            request: order_service.BatchRetractOrdersWithoutReservationChangesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> order_service.BatchRetractOrdersWithoutReservationChangesResponse:
            r"""Call the batch retract orders
            without reservation changes method over HTTP.

                Args:
                    request (~.order_service.BatchRetractOrdersWithoutReservationChangesRequest):
                        The request object. Request message for
                    ``BatchRetractOrdersWithoutReservationChanges`` method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.order_service.BatchRetractOrdersWithoutReservationChangesResponse:
                        Response object for
                    ``BatchRetractOrdersWithoutReservationChanges`` method.

            """

            http_options = _BaseOrderServiceRestTransport._BaseBatchRetractOrdersWithoutReservationChanges._get_http_options()
            request, metadata = (
                self._interceptor.pre_batch_retract_orders_without_reservation_changes(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseOrderServiceRestTransport._BaseBatchRetractOrdersWithoutReservationChanges,
                    "_BaseBatchRetractOrdersWithoutReservationChanges__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.OrderServiceClient.BatchRetractOrdersWithoutReservationChanges",
                    extra={
                        "serviceName": "google.ads.admanager.v1.OrderService",
                        "rpcName": "BatchRetractOrdersWithoutReservationChanges",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = OrderServiceRestTransport._BatchRetractOrdersWithoutReservationChanges._get_response(
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
            resp = order_service.BatchRetractOrdersWithoutReservationChangesResponse()
            pb_resp = (
                order_service.BatchRetractOrdersWithoutReservationChangesResponse.pb(
                    resp
                )
            )

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = (
                self._interceptor.post_batch_retract_orders_without_reservation_changes(
                    resp
                )
            )
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_batch_retract_orders_without_reservation_changes_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = order_service.BatchRetractOrdersWithoutReservationChangesResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.OrderServiceClient.batch_retract_orders_without_reservation_changes",
                    extra={
                        "serviceName": "google.ads.admanager.v1.OrderService",
                        "rpcName": "BatchRetractOrdersWithoutReservationChanges",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BatchSubmitOrdersForApproval(
        _BaseOrderServiceRestTransport._BaseBatchSubmitOrdersForApproval,
        OrderServiceRestStub,
    ):
        def __hash__(self):
            return hash("OrderServiceRestTransport.BatchSubmitOrdersForApproval")

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
            request: order_service.BatchSubmitOrdersForApprovalRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> order_service.BatchSubmitOrdersForApprovalResponse:
            r"""Call the batch submit orders for
            approval method over HTTP.

                Args:
                    request (~.order_service.BatchSubmitOrdersForApprovalRequest):
                        The request object. Request message for ``BatchSubmitOrdersForApproval``
                    method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.order_service.BatchSubmitOrdersForApprovalResponse:
                        Response object for ``BatchSubmitOrdersForApproval``
                    method.

            """

            http_options = _BaseOrderServiceRestTransport._BaseBatchSubmitOrdersForApproval._get_http_options()
            request, metadata = self._interceptor.pre_batch_submit_orders_for_approval(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseOrderServiceRestTransport._BaseBatchSubmitOrdersForApproval,
                    "_BaseBatchSubmitOrdersForApproval__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.OrderServiceClient.BatchSubmitOrdersForApproval",
                    extra={
                        "serviceName": "google.ads.admanager.v1.OrderService",
                        "rpcName": "BatchSubmitOrdersForApproval",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                OrderServiceRestTransport._BatchSubmitOrdersForApproval._get_response(
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
            resp = order_service.BatchSubmitOrdersForApprovalResponse()
            pb_resp = order_service.BatchSubmitOrdersForApprovalResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_submit_orders_for_approval(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_batch_submit_orders_for_approval_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        order_service.BatchSubmitOrdersForApprovalResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.OrderServiceClient.batch_submit_orders_for_approval",
                    extra={
                        "serviceName": "google.ads.admanager.v1.OrderService",
                        "rpcName": "BatchSubmitOrdersForApproval",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BatchSubmitOrdersForApprovalAndOverbook(
        _BaseOrderServiceRestTransport._BaseBatchSubmitOrdersForApprovalAndOverbook,
        OrderServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "OrderServiceRestTransport.BatchSubmitOrdersForApprovalAndOverbook"
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
            request: order_service.BatchSubmitOrdersForApprovalAndOverbookRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> order_service.BatchSubmitOrdersForApprovalAndOverbookResponse:
            r"""Call the batch submit orders for
            approval and overbook method over HTTP.

                Args:
                    request (~.order_service.BatchSubmitOrdersForApprovalAndOverbookRequest):
                        The request object. Request message for
                    ``BatchSubmitOrdersForApprovalAndOverbook`` method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.order_service.BatchSubmitOrdersForApprovalAndOverbookResponse:
                        Response object for
                    ``BatchSubmitOrdersForApprovalAndOverbook`` method.

            """

            http_options = _BaseOrderServiceRestTransport._BaseBatchSubmitOrdersForApprovalAndOverbook._get_http_options()
            request, metadata = (
                self._interceptor.pre_batch_submit_orders_for_approval_and_overbook(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseOrderServiceRestTransport._BaseBatchSubmitOrdersForApprovalAndOverbook,
                    "_BaseBatchSubmitOrdersForApprovalAndOverbook__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.OrderServiceClient.BatchSubmitOrdersForApprovalAndOverbook",
                    extra={
                        "serviceName": "google.ads.admanager.v1.OrderService",
                        "rpcName": "BatchSubmitOrdersForApprovalAndOverbook",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = OrderServiceRestTransport._BatchSubmitOrdersForApprovalAndOverbook._get_response(
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
            resp = order_service.BatchSubmitOrdersForApprovalAndOverbookResponse()
            pb_resp = order_service.BatchSubmitOrdersForApprovalAndOverbookResponse.pb(
                resp
            )

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_submit_orders_for_approval_and_overbook(
                resp
            )
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_batch_submit_orders_for_approval_and_overbook_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = order_service.BatchSubmitOrdersForApprovalAndOverbookResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.OrderServiceClient.batch_submit_orders_for_approval_and_overbook",
                    extra={
                        "serviceName": "google.ads.admanager.v1.OrderService",
                        "rpcName": "BatchSubmitOrdersForApprovalAndOverbook",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BatchSubmitOrdersForApprovalWithoutReservationChanges(
        _BaseOrderServiceRestTransport._BaseBatchSubmitOrdersForApprovalWithoutReservationChanges,
        OrderServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "OrderServiceRestTransport.BatchSubmitOrdersForApprovalWithoutReservationChanges"
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
            request: order_service.BatchSubmitOrdersForApprovalWithoutReservationChangesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> (
            order_service.BatchSubmitOrdersForApprovalWithoutReservationChangesResponse
        ):
            r"""Call the batch submit orders for
            approval without reservation changes method over HTTP.

                Args:
                    request (~.order_service.BatchSubmitOrdersForApprovalWithoutReservationChangesRequest):
                        The request object. Request message for
                    ``BatchSubmitOrdersForApprovalWithoutReservationChanges``
                    method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.order_service.BatchSubmitOrdersForApprovalWithoutReservationChangesResponse:
                        Response object for
                    ``BatchSubmitOrdersForApprovalWithoutReservationChanges``
                    method.

            """

            http_options = _BaseOrderServiceRestTransport._BaseBatchSubmitOrdersForApprovalWithoutReservationChanges._get_http_options()
            request, metadata = (
                self._interceptor.pre_batch_submit_orders_for_approval_without_reservation_changes(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseOrderServiceRestTransport._BaseBatchSubmitOrdersForApprovalWithoutReservationChanges,
                    "_BaseBatchSubmitOrdersForApprovalWithoutReservationChanges__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.OrderServiceClient.BatchSubmitOrdersForApprovalWithoutReservationChanges",
                    extra={
                        "serviceName": "google.ads.admanager.v1.OrderService",
                        "rpcName": "BatchSubmitOrdersForApprovalWithoutReservationChanges",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = OrderServiceRestTransport._BatchSubmitOrdersForApprovalWithoutReservationChanges._get_response(
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
            resp = order_service.BatchSubmitOrdersForApprovalWithoutReservationChangesResponse()
            pb_resp = order_service.BatchSubmitOrdersForApprovalWithoutReservationChangesResponse.pb(
                resp
            )

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_submit_orders_for_approval_without_reservation_changes(
                resp
            )
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_batch_submit_orders_for_approval_without_reservation_changes_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = order_service.BatchSubmitOrdersForApprovalWithoutReservationChangesResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.OrderServiceClient.batch_submit_orders_for_approval_without_reservation_changes",
                    extra={
                        "serviceName": "google.ads.admanager.v1.OrderService",
                        "rpcName": "BatchSubmitOrdersForApprovalWithoutReservationChanges",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BatchUnarchiveOrders(
        _BaseOrderServiceRestTransport._BaseBatchUnarchiveOrders, OrderServiceRestStub
    ):
        def __hash__(self):
            return hash("OrderServiceRestTransport.BatchUnarchiveOrders")

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
            request: order_service.BatchUnarchiveOrdersRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> order_service.BatchUnarchiveOrdersResponse:
            r"""Call the batch unarchive orders method over HTTP.

            Args:
                request (~.order_service.BatchUnarchiveOrdersRequest):
                    The request object. Request message for ``BatchUnarchiveOrders`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.order_service.BatchUnarchiveOrdersResponse:
                    Response object for ``BatchUnarchiveOrders`` method.
            """

            http_options = _BaseOrderServiceRestTransport._BaseBatchUnarchiveOrders._get_http_options()
            request, metadata = self._interceptor.pre_batch_unarchive_orders(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseOrderServiceRestTransport._BaseBatchUnarchiveOrders,
                    "_BaseBatchUnarchiveOrders__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.OrderServiceClient.BatchUnarchiveOrders",
                    extra={
                        "serviceName": "google.ads.admanager.v1.OrderService",
                        "rpcName": "BatchUnarchiveOrders",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = OrderServiceRestTransport._BatchUnarchiveOrders._get_response(
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
            resp = order_service.BatchUnarchiveOrdersResponse()
            pb_resp = order_service.BatchUnarchiveOrdersResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_unarchive_orders(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_batch_unarchive_orders_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        order_service.BatchUnarchiveOrdersResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.ads.admanager_v1.OrderServiceClient.batch_unarchive_orders",
                    extra={
                        "serviceName": "google.ads.admanager.v1.OrderService",
                        "rpcName": "BatchUnarchiveOrders",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BatchUpdateOrders(
        _BaseOrderServiceRestTransport._BaseBatchUpdateOrders, OrderServiceRestStub
    ):
        def __hash__(self):
            return hash("OrderServiceRestTransport.BatchUpdateOrders")

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
            request: order_service.BatchUpdateOrdersRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> order_service.BatchUpdateOrdersResponse:
            r"""Call the batch update orders method over HTTP.

            Args:
                request (~.order_service.BatchUpdateOrdersRequest):
                    The request object. Request object for ``BatchUpdateOrders`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.order_service.BatchUpdateOrdersResponse:
                    Response object for ``BatchUpdateOrders`` method.
            """

            http_options = _BaseOrderServiceRestTransport._BaseBatchUpdateOrders._get_http_options()
            request, metadata = self._interceptor.pre_batch_update_orders(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseOrderServiceRestTransport._BaseBatchUpdateOrders,
                    "_BaseBatchUpdateOrders__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.OrderServiceClient.BatchUpdateOrders",
                    extra={
                        "serviceName": "google.ads.admanager.v1.OrderService",
                        "rpcName": "BatchUpdateOrders",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = OrderServiceRestTransport._BatchUpdateOrders._get_response(
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
            resp = order_service.BatchUpdateOrdersResponse()
            pb_resp = order_service.BatchUpdateOrdersResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_update_orders(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_batch_update_orders_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = order_service.BatchUpdateOrdersResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.OrderServiceClient.batch_update_orders",
                    extra={
                        "serviceName": "google.ads.admanager.v1.OrderService",
                        "rpcName": "BatchUpdateOrders",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetOrder(_BaseOrderServiceRestTransport._BaseGetOrder, OrderServiceRestStub):
        def __hash__(self):
            return hash("OrderServiceRestTransport.GetOrder")

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
            request: order_service.GetOrderRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> order_messages.Order:
            r"""Call the get order method over HTTP.

            Args:
                request (~.order_service.GetOrderRequest):
                    The request object. Request object for ``GetOrder`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.order_messages.Order:
                    The ``Order`` resource.
            """

            http_options = (
                _BaseOrderServiceRestTransport._BaseGetOrder._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_order(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseOrderServiceRestTransport._BaseGetOrder,
                    "_BaseGetOrder__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.OrderServiceClient.GetOrder",
                    extra={
                        "serviceName": "google.ads.admanager.v1.OrderService",
                        "rpcName": "GetOrder",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = OrderServiceRestTransport._GetOrder._get_response(
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
            resp = order_messages.Order()
            pb_resp = order_messages.Order.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_order(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_order_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = order_messages.Order.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.ads.admanager_v1.OrderServiceClient.get_order",
                    extra={
                        "serviceName": "google.ads.admanager.v1.OrderService",
                        "rpcName": "GetOrder",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListOrders(
        _BaseOrderServiceRestTransport._BaseListOrders, OrderServiceRestStub
    ):
        def __hash__(self):
            return hash("OrderServiceRestTransport.ListOrders")

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
            request: order_service.ListOrdersRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> order_service.ListOrdersResponse:
            r"""Call the list orders method over HTTP.

            Args:
                request (~.order_service.ListOrdersRequest):
                    The request object. Request object for ``ListOrders`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.order_service.ListOrdersResponse:
                    Response object for ``ListOrdersRequest`` containing
                matching ``Order`` resources.

            """

            http_options = (
                _BaseOrderServiceRestTransport._BaseListOrders._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_orders(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseOrderServiceRestTransport._BaseListOrders,
                    "_BaseListOrders__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.OrderServiceClient.ListOrders",
                    extra={
                        "serviceName": "google.ads.admanager.v1.OrderService",
                        "rpcName": "ListOrders",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = OrderServiceRestTransport._ListOrders._get_response(
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
            resp = order_service.ListOrdersResponse()
            pb_resp = order_service.ListOrdersResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_orders(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_orders_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = order_service.ListOrdersResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.OrderServiceClient.list_orders",
                    extra={
                        "serviceName": "google.ads.admanager.v1.OrderService",
                        "rpcName": "ListOrders",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def batch_approve_and_overbook_orders(
        self,
    ) -> Callable[
        [order_service.BatchApproveAndOverbookOrdersRequest],
        order_service.BatchApproveAndOverbookOrdersResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchApproveAndOverbookOrders(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def batch_approve_orders(
        self,
    ) -> Callable[
        [order_service.BatchApproveOrdersRequest],
        order_service.BatchApproveOrdersResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchApproveOrders(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def batch_approve_orders_without_reservation(
        self,
    ) -> Callable[
        [order_service.BatchApproveOrdersWithoutReservationRequest],
        order_service.BatchApproveOrdersWithoutReservationResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchApproveOrdersWithoutReservation(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def batch_archive_orders(
        self,
    ) -> Callable[
        [order_service.BatchArchiveOrdersRequest],
        order_service.BatchArchiveOrdersResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchArchiveOrders(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def batch_create_orders(
        self,
    ) -> Callable[
        [order_service.BatchCreateOrdersRequest],
        order_service.BatchCreateOrdersResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchCreateOrders(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def batch_delete_orders(
        self,
    ) -> Callable[
        [order_service.BatchDeleteOrdersRequest],
        order_service.BatchDeleteOrdersResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchDeleteOrders(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def batch_disapprove_orders(
        self,
    ) -> Callable[
        [order_service.BatchDisapproveOrdersRequest],
        order_service.BatchDisapproveOrdersResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchDisapproveOrders(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def batch_disapprove_orders_without_reservation_changes(
        self,
    ) -> Callable[
        [order_service.BatchDisapproveOrdersWithoutReservationChangesRequest],
        order_service.BatchDisapproveOrdersWithoutReservationChangesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchDisapproveOrdersWithoutReservationChanges(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def batch_pause_orders(
        self,
    ) -> Callable[
        [order_service.BatchPauseOrdersRequest], order_service.BatchPauseOrdersResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchPauseOrders(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def batch_resume_and_overbook_orders(
        self,
    ) -> Callable[
        [order_service.BatchResumeAndOverbookOrdersRequest],
        order_service.BatchResumeAndOverbookOrdersResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchResumeAndOverbookOrders(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def batch_resume_orders(
        self,
    ) -> Callable[
        [order_service.BatchResumeOrdersRequest],
        order_service.BatchResumeOrdersResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchResumeOrders(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def batch_retract_orders(
        self,
    ) -> Callable[
        [order_service.BatchRetractOrdersRequest],
        order_service.BatchRetractOrdersResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchRetractOrders(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def batch_retract_orders_without_reservation_changes(
        self,
    ) -> Callable[
        [order_service.BatchRetractOrdersWithoutReservationChangesRequest],
        order_service.BatchRetractOrdersWithoutReservationChangesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchRetractOrdersWithoutReservationChanges(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def batch_submit_orders_for_approval(
        self,
    ) -> Callable[
        [order_service.BatchSubmitOrdersForApprovalRequest],
        order_service.BatchSubmitOrdersForApprovalResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchSubmitOrdersForApproval(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def batch_submit_orders_for_approval_and_overbook(
        self,
    ) -> Callable[
        [order_service.BatchSubmitOrdersForApprovalAndOverbookRequest],
        order_service.BatchSubmitOrdersForApprovalAndOverbookResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchSubmitOrdersForApprovalAndOverbook(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def batch_submit_orders_for_approval_without_reservation_changes(
        self,
    ) -> Callable[
        [order_service.BatchSubmitOrdersForApprovalWithoutReservationChangesRequest],
        order_service.BatchSubmitOrdersForApprovalWithoutReservationChangesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchSubmitOrdersForApprovalWithoutReservationChanges(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def batch_unarchive_orders(
        self,
    ) -> Callable[
        [order_service.BatchUnarchiveOrdersRequest],
        order_service.BatchUnarchiveOrdersResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchUnarchiveOrders(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def batch_update_orders(
        self,
    ) -> Callable[
        [order_service.BatchUpdateOrdersRequest],
        order_service.BatchUpdateOrdersResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchUpdateOrders(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_order(
        self,
    ) -> Callable[[order_service.GetOrderRequest], order_messages.Order]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetOrder(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_orders(
        self,
    ) -> Callable[[order_service.ListOrdersRequest], order_service.ListOrdersResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListOrders(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def cancel_operation(self):
        return self._CancelOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _CancelOperation(
        _BaseOrderServiceRestTransport._BaseCancelOperation, OrderServiceRestStub
    ):
        def __hash__(self):
            return hash("OrderServiceRestTransport.CancelOperation")

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
                _BaseOrderServiceRestTransport._BaseCancelOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_cancel_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseOrderServiceRestTransport._BaseCancelOperation,
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
                    f"Sending request for google.ads.admanager_v1.OrderServiceClient.CancelOperation",
                    extra={
                        "serviceName": "google.ads.admanager.v1.OrderService",
                        "rpcName": "CancelOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = OrderServiceRestTransport._CancelOperation._get_response(
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
        _BaseOrderServiceRestTransport._BaseGetOperation, OrderServiceRestStub
    ):
        def __hash__(self):
            return hash("OrderServiceRestTransport.GetOperation")

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
                _BaseOrderServiceRestTransport._BaseGetOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_operation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseOrderServiceRestTransport._BaseGetOperation,
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
                    f"Sending request for google.ads.admanager_v1.OrderServiceClient.GetOperation",
                    extra={
                        "serviceName": "google.ads.admanager.v1.OrderService",
                        "rpcName": "GetOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = OrderServiceRestTransport._GetOperation._get_response(
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
                    "Received response for google.ads.admanager_v1.OrderServiceAsyncClient.GetOperation",
                    extra={
                        "serviceName": "google.ads.admanager.v1.OrderService",
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


__all__ = ("OrderServiceRestTransport",)
