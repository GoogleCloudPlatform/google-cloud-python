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
from google.ads.admanager_v1.types import ad_unit_messages, ad_unit_service

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseAdUnitServiceRestTransport

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


class AdUnitServiceRestInterceptor:
    """Interceptor for AdUnitService.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the AdUnitServiceRestTransport.

    .. code-block:: python
        class MyCustomAdUnitServiceInterceptor(AdUnitServiceRestInterceptor):
            def pre_batch_activate_ad_units(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_activate_ad_units(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_batch_archive_ad_units(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_archive_ad_units(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_batch_create_ad_units(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_create_ad_units(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_batch_deactivate_ad_units(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_deactivate_ad_units(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_batch_update_ad_units(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_update_ad_units(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_ad_unit(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_ad_unit(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_ad_unit(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_ad_unit(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_ad_units(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_ad_units(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_ad_unit_sizes(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_ad_unit_sizes(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_ad_unit(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_ad_unit(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = AdUnitServiceRestTransport(interceptor=MyCustomAdUnitServiceInterceptor())
        client = AdUnitServiceClient(transport=transport)


    """

    def pre_batch_activate_ad_units(
        self,
        request: ad_unit_service.BatchActivateAdUnitsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        ad_unit_service.BatchActivateAdUnitsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_activate_ad_units

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AdUnitService server.
        """
        return request, metadata

    def post_batch_activate_ad_units(
        self, response: ad_unit_service.BatchActivateAdUnitsResponse
    ) -> ad_unit_service.BatchActivateAdUnitsResponse:
        """Post-rpc interceptor for batch_activate_ad_units

        DEPRECATED. Please use the `post_batch_activate_ad_units_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AdUnitService server but before
        it is returned to user code. This `post_batch_activate_ad_units` interceptor runs
        before the `post_batch_activate_ad_units_with_metadata` interceptor.
        """
        return response

    def post_batch_activate_ad_units_with_metadata(
        self,
        response: ad_unit_service.BatchActivateAdUnitsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        ad_unit_service.BatchActivateAdUnitsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_activate_ad_units

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AdUnitService server but before it is returned to user code.

        We recommend only using this `post_batch_activate_ad_units_with_metadata`
        interceptor in new development instead of the `post_batch_activate_ad_units` interceptor.
        When both interceptors are used, this `post_batch_activate_ad_units_with_metadata` interceptor runs after the
        `post_batch_activate_ad_units` interceptor. The (possibly modified) response returned by
        `post_batch_activate_ad_units` will be passed to
        `post_batch_activate_ad_units_with_metadata`.
        """
        return response, metadata

    def pre_batch_archive_ad_units(
        self,
        request: ad_unit_service.BatchArchiveAdUnitsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        ad_unit_service.BatchArchiveAdUnitsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_archive_ad_units

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AdUnitService server.
        """
        return request, metadata

    def post_batch_archive_ad_units(
        self, response: ad_unit_service.BatchArchiveAdUnitsResponse
    ) -> ad_unit_service.BatchArchiveAdUnitsResponse:
        """Post-rpc interceptor for batch_archive_ad_units

        DEPRECATED. Please use the `post_batch_archive_ad_units_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AdUnitService server but before
        it is returned to user code. This `post_batch_archive_ad_units` interceptor runs
        before the `post_batch_archive_ad_units_with_metadata` interceptor.
        """
        return response

    def post_batch_archive_ad_units_with_metadata(
        self,
        response: ad_unit_service.BatchArchiveAdUnitsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        ad_unit_service.BatchArchiveAdUnitsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_archive_ad_units

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AdUnitService server but before it is returned to user code.

        We recommend only using this `post_batch_archive_ad_units_with_metadata`
        interceptor in new development instead of the `post_batch_archive_ad_units` interceptor.
        When both interceptors are used, this `post_batch_archive_ad_units_with_metadata` interceptor runs after the
        `post_batch_archive_ad_units` interceptor. The (possibly modified) response returned by
        `post_batch_archive_ad_units` will be passed to
        `post_batch_archive_ad_units_with_metadata`.
        """
        return response, metadata

    def pre_batch_create_ad_units(
        self,
        request: ad_unit_service.BatchCreateAdUnitsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        ad_unit_service.BatchCreateAdUnitsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_create_ad_units

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AdUnitService server.
        """
        return request, metadata

    def post_batch_create_ad_units(
        self, response: ad_unit_service.BatchCreateAdUnitsResponse
    ) -> ad_unit_service.BatchCreateAdUnitsResponse:
        """Post-rpc interceptor for batch_create_ad_units

        DEPRECATED. Please use the `post_batch_create_ad_units_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AdUnitService server but before
        it is returned to user code. This `post_batch_create_ad_units` interceptor runs
        before the `post_batch_create_ad_units_with_metadata` interceptor.
        """
        return response

    def post_batch_create_ad_units_with_metadata(
        self,
        response: ad_unit_service.BatchCreateAdUnitsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        ad_unit_service.BatchCreateAdUnitsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_create_ad_units

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AdUnitService server but before it is returned to user code.

        We recommend only using this `post_batch_create_ad_units_with_metadata`
        interceptor in new development instead of the `post_batch_create_ad_units` interceptor.
        When both interceptors are used, this `post_batch_create_ad_units_with_metadata` interceptor runs after the
        `post_batch_create_ad_units` interceptor. The (possibly modified) response returned by
        `post_batch_create_ad_units` will be passed to
        `post_batch_create_ad_units_with_metadata`.
        """
        return response, metadata

    def pre_batch_deactivate_ad_units(
        self,
        request: ad_unit_service.BatchDeactivateAdUnitsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        ad_unit_service.BatchDeactivateAdUnitsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_deactivate_ad_units

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AdUnitService server.
        """
        return request, metadata

    def post_batch_deactivate_ad_units(
        self, response: ad_unit_service.BatchDeactivateAdUnitsResponse
    ) -> ad_unit_service.BatchDeactivateAdUnitsResponse:
        """Post-rpc interceptor for batch_deactivate_ad_units

        DEPRECATED. Please use the `post_batch_deactivate_ad_units_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AdUnitService server but before
        it is returned to user code. This `post_batch_deactivate_ad_units` interceptor runs
        before the `post_batch_deactivate_ad_units_with_metadata` interceptor.
        """
        return response

    def post_batch_deactivate_ad_units_with_metadata(
        self,
        response: ad_unit_service.BatchDeactivateAdUnitsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        ad_unit_service.BatchDeactivateAdUnitsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_deactivate_ad_units

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AdUnitService server but before it is returned to user code.

        We recommend only using this `post_batch_deactivate_ad_units_with_metadata`
        interceptor in new development instead of the `post_batch_deactivate_ad_units` interceptor.
        When both interceptors are used, this `post_batch_deactivate_ad_units_with_metadata` interceptor runs after the
        `post_batch_deactivate_ad_units` interceptor. The (possibly modified) response returned by
        `post_batch_deactivate_ad_units` will be passed to
        `post_batch_deactivate_ad_units_with_metadata`.
        """
        return response, metadata

    def pre_batch_update_ad_units(
        self,
        request: ad_unit_service.BatchUpdateAdUnitsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        ad_unit_service.BatchUpdateAdUnitsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_update_ad_units

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AdUnitService server.
        """
        return request, metadata

    def post_batch_update_ad_units(
        self, response: ad_unit_service.BatchUpdateAdUnitsResponse
    ) -> ad_unit_service.BatchUpdateAdUnitsResponse:
        """Post-rpc interceptor for batch_update_ad_units

        DEPRECATED. Please use the `post_batch_update_ad_units_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AdUnitService server but before
        it is returned to user code. This `post_batch_update_ad_units` interceptor runs
        before the `post_batch_update_ad_units_with_metadata` interceptor.
        """
        return response

    def post_batch_update_ad_units_with_metadata(
        self,
        response: ad_unit_service.BatchUpdateAdUnitsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        ad_unit_service.BatchUpdateAdUnitsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_update_ad_units

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AdUnitService server but before it is returned to user code.

        We recommend only using this `post_batch_update_ad_units_with_metadata`
        interceptor in new development instead of the `post_batch_update_ad_units` interceptor.
        When both interceptors are used, this `post_batch_update_ad_units_with_metadata` interceptor runs after the
        `post_batch_update_ad_units` interceptor. The (possibly modified) response returned by
        `post_batch_update_ad_units` will be passed to
        `post_batch_update_ad_units_with_metadata`.
        """
        return response, metadata

    def pre_create_ad_unit(
        self,
        request: ad_unit_service.CreateAdUnitRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        ad_unit_service.CreateAdUnitRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_ad_unit

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AdUnitService server.
        """
        return request, metadata

    def post_create_ad_unit(
        self, response: ad_unit_messages.AdUnit
    ) -> ad_unit_messages.AdUnit:
        """Post-rpc interceptor for create_ad_unit

        DEPRECATED. Please use the `post_create_ad_unit_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AdUnitService server but before
        it is returned to user code. This `post_create_ad_unit` interceptor runs
        before the `post_create_ad_unit_with_metadata` interceptor.
        """
        return response

    def post_create_ad_unit_with_metadata(
        self,
        response: ad_unit_messages.AdUnit,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[ad_unit_messages.AdUnit, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_ad_unit

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AdUnitService server but before it is returned to user code.

        We recommend only using this `post_create_ad_unit_with_metadata`
        interceptor in new development instead of the `post_create_ad_unit` interceptor.
        When both interceptors are used, this `post_create_ad_unit_with_metadata` interceptor runs after the
        `post_create_ad_unit` interceptor. The (possibly modified) response returned by
        `post_create_ad_unit` will be passed to
        `post_create_ad_unit_with_metadata`.
        """
        return response, metadata

    def pre_get_ad_unit(
        self,
        request: ad_unit_service.GetAdUnitRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        ad_unit_service.GetAdUnitRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_ad_unit

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AdUnitService server.
        """
        return request, metadata

    def post_get_ad_unit(
        self, response: ad_unit_messages.AdUnit
    ) -> ad_unit_messages.AdUnit:
        """Post-rpc interceptor for get_ad_unit

        DEPRECATED. Please use the `post_get_ad_unit_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AdUnitService server but before
        it is returned to user code. This `post_get_ad_unit` interceptor runs
        before the `post_get_ad_unit_with_metadata` interceptor.
        """
        return response

    def post_get_ad_unit_with_metadata(
        self,
        response: ad_unit_messages.AdUnit,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[ad_unit_messages.AdUnit, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_ad_unit

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AdUnitService server but before it is returned to user code.

        We recommend only using this `post_get_ad_unit_with_metadata`
        interceptor in new development instead of the `post_get_ad_unit` interceptor.
        When both interceptors are used, this `post_get_ad_unit_with_metadata` interceptor runs after the
        `post_get_ad_unit` interceptor. The (possibly modified) response returned by
        `post_get_ad_unit` will be passed to
        `post_get_ad_unit_with_metadata`.
        """
        return response, metadata

    def pre_list_ad_units(
        self,
        request: ad_unit_service.ListAdUnitsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        ad_unit_service.ListAdUnitsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_ad_units

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AdUnitService server.
        """
        return request, metadata

    def post_list_ad_units(
        self, response: ad_unit_service.ListAdUnitsResponse
    ) -> ad_unit_service.ListAdUnitsResponse:
        """Post-rpc interceptor for list_ad_units

        DEPRECATED. Please use the `post_list_ad_units_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AdUnitService server but before
        it is returned to user code. This `post_list_ad_units` interceptor runs
        before the `post_list_ad_units_with_metadata` interceptor.
        """
        return response

    def post_list_ad_units_with_metadata(
        self,
        response: ad_unit_service.ListAdUnitsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        ad_unit_service.ListAdUnitsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_ad_units

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AdUnitService server but before it is returned to user code.

        We recommend only using this `post_list_ad_units_with_metadata`
        interceptor in new development instead of the `post_list_ad_units` interceptor.
        When both interceptors are used, this `post_list_ad_units_with_metadata` interceptor runs after the
        `post_list_ad_units` interceptor. The (possibly modified) response returned by
        `post_list_ad_units` will be passed to
        `post_list_ad_units_with_metadata`.
        """
        return response, metadata

    def pre_list_ad_unit_sizes(
        self,
        request: ad_unit_service.ListAdUnitSizesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        ad_unit_service.ListAdUnitSizesRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_ad_unit_sizes

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AdUnitService server.
        """
        return request, metadata

    def post_list_ad_unit_sizes(
        self, response: ad_unit_service.ListAdUnitSizesResponse
    ) -> ad_unit_service.ListAdUnitSizesResponse:
        """Post-rpc interceptor for list_ad_unit_sizes

        DEPRECATED. Please use the `post_list_ad_unit_sizes_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AdUnitService server but before
        it is returned to user code. This `post_list_ad_unit_sizes` interceptor runs
        before the `post_list_ad_unit_sizes_with_metadata` interceptor.
        """
        return response

    def post_list_ad_unit_sizes_with_metadata(
        self,
        response: ad_unit_service.ListAdUnitSizesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        ad_unit_service.ListAdUnitSizesResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_ad_unit_sizes

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AdUnitService server but before it is returned to user code.

        We recommend only using this `post_list_ad_unit_sizes_with_metadata`
        interceptor in new development instead of the `post_list_ad_unit_sizes` interceptor.
        When both interceptors are used, this `post_list_ad_unit_sizes_with_metadata` interceptor runs after the
        `post_list_ad_unit_sizes` interceptor. The (possibly modified) response returned by
        `post_list_ad_unit_sizes` will be passed to
        `post_list_ad_unit_sizes_with_metadata`.
        """
        return response, metadata

    def pre_update_ad_unit(
        self,
        request: ad_unit_service.UpdateAdUnitRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        ad_unit_service.UpdateAdUnitRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_ad_unit

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AdUnitService server.
        """
        return request, metadata

    def post_update_ad_unit(
        self, response: ad_unit_messages.AdUnit
    ) -> ad_unit_messages.AdUnit:
        """Post-rpc interceptor for update_ad_unit

        DEPRECATED. Please use the `post_update_ad_unit_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AdUnitService server but before
        it is returned to user code. This `post_update_ad_unit` interceptor runs
        before the `post_update_ad_unit_with_metadata` interceptor.
        """
        return response

    def post_update_ad_unit_with_metadata(
        self,
        response: ad_unit_messages.AdUnit,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[ad_unit_messages.AdUnit, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_ad_unit

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AdUnitService server but before it is returned to user code.

        We recommend only using this `post_update_ad_unit_with_metadata`
        interceptor in new development instead of the `post_update_ad_unit` interceptor.
        When both interceptors are used, this `post_update_ad_unit_with_metadata` interceptor runs after the
        `post_update_ad_unit` interceptor. The (possibly modified) response returned by
        `post_update_ad_unit` will be passed to
        `post_update_ad_unit_with_metadata`.
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
        before they are sent to the AdUnitService server.
        """
        return request, metadata

    def post_cancel_operation(self, response: None) -> None:
        """Post-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the response
        after it is returned by the AdUnitService server but before
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
        before they are sent to the AdUnitService server.
        """
        return request, metadata

    def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the AdUnitService server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class AdUnitServiceRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: AdUnitServiceRestInterceptor


class AdUnitServiceRestTransport(_BaseAdUnitServiceRestTransport):
    """REST backend synchronous transport for AdUnitService.

    Provides methods for handling AdUnit objects.

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
        interceptor: Optional[AdUnitServiceRestInterceptor] = None,
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
            interceptor (Optional[AdUnitServiceRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or AdUnitServiceRestInterceptor()
        self._prep_wrapped_messages(client_info)

    class _BatchActivateAdUnits(
        _BaseAdUnitServiceRestTransport._BaseBatchActivateAdUnits, AdUnitServiceRestStub
    ):
        def __hash__(self):
            return hash("AdUnitServiceRestTransport.BatchActivateAdUnits")

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
            request: ad_unit_service.BatchActivateAdUnitsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> ad_unit_service.BatchActivateAdUnitsResponse:
            r"""Call the batch activate ad units method over HTTP.

            Args:
                request (~.ad_unit_service.BatchActivateAdUnitsRequest):
                    The request object. Request object for ``BatchActivateAdUnits`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.ad_unit_service.BatchActivateAdUnitsResponse:
                    Response object for ``BatchActivateAdUnits`` method.
            """

            http_options = _BaseAdUnitServiceRestTransport._BaseBatchActivateAdUnits._get_http_options()
            request, metadata = self._interceptor.pre_batch_activate_ad_units(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAdUnitServiceRestTransport._BaseBatchActivateAdUnits,
                    "_BaseBatchActivateAdUnits__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.AdUnitServiceClient.BatchActivateAdUnits",
                    extra={
                        "serviceName": "google.ads.admanager.v1.AdUnitService",
                        "rpcName": "BatchActivateAdUnits",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AdUnitServiceRestTransport._BatchActivateAdUnits._get_response(
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
            resp = ad_unit_service.BatchActivateAdUnitsResponse()
            pb_resp = ad_unit_service.BatchActivateAdUnitsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_activate_ad_units(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_batch_activate_ad_units_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        ad_unit_service.BatchActivateAdUnitsResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.ads.admanager_v1.AdUnitServiceClient.batch_activate_ad_units",
                    extra={
                        "serviceName": "google.ads.admanager.v1.AdUnitService",
                        "rpcName": "BatchActivateAdUnits",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BatchArchiveAdUnits(
        _BaseAdUnitServiceRestTransport._BaseBatchArchiveAdUnits, AdUnitServiceRestStub
    ):
        def __hash__(self):
            return hash("AdUnitServiceRestTransport.BatchArchiveAdUnits")

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
            request: ad_unit_service.BatchArchiveAdUnitsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> ad_unit_service.BatchArchiveAdUnitsResponse:
            r"""Call the batch archive ad units method over HTTP.

            Args:
                request (~.ad_unit_service.BatchArchiveAdUnitsRequest):
                    The request object. Request object for ``BatchArchiveAdUnits`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.ad_unit_service.BatchArchiveAdUnitsResponse:
                    Response object for ``BatchArchiveAdUnits`` method.
            """

            http_options = _BaseAdUnitServiceRestTransport._BaseBatchArchiveAdUnits._get_http_options()
            request, metadata = self._interceptor.pre_batch_archive_ad_units(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAdUnitServiceRestTransport._BaseBatchArchiveAdUnits,
                    "_BaseBatchArchiveAdUnits__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.AdUnitServiceClient.BatchArchiveAdUnits",
                    extra={
                        "serviceName": "google.ads.admanager.v1.AdUnitService",
                        "rpcName": "BatchArchiveAdUnits",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AdUnitServiceRestTransport._BatchArchiveAdUnits._get_response(
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
            resp = ad_unit_service.BatchArchiveAdUnitsResponse()
            pb_resp = ad_unit_service.BatchArchiveAdUnitsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_archive_ad_units(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_batch_archive_ad_units_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        ad_unit_service.BatchArchiveAdUnitsResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.ads.admanager_v1.AdUnitServiceClient.batch_archive_ad_units",
                    extra={
                        "serviceName": "google.ads.admanager.v1.AdUnitService",
                        "rpcName": "BatchArchiveAdUnits",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BatchCreateAdUnits(
        _BaseAdUnitServiceRestTransport._BaseBatchCreateAdUnits, AdUnitServiceRestStub
    ):
        def __hash__(self):
            return hash("AdUnitServiceRestTransport.BatchCreateAdUnits")

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
            request: ad_unit_service.BatchCreateAdUnitsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> ad_unit_service.BatchCreateAdUnitsResponse:
            r"""Call the batch create ad units method over HTTP.

            Args:
                request (~.ad_unit_service.BatchCreateAdUnitsRequest):
                    The request object. Request object for ``BatchCreateAdUnits`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.ad_unit_service.BatchCreateAdUnitsResponse:
                    Response object for ``BatchCreateAdUnits`` method.
            """

            http_options = _BaseAdUnitServiceRestTransport._BaseBatchCreateAdUnits._get_http_options()
            request, metadata = self._interceptor.pre_batch_create_ad_units(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAdUnitServiceRestTransport._BaseBatchCreateAdUnits,
                    "_BaseBatchCreateAdUnits__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.AdUnitServiceClient.BatchCreateAdUnits",
                    extra={
                        "serviceName": "google.ads.admanager.v1.AdUnitService",
                        "rpcName": "BatchCreateAdUnits",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AdUnitServiceRestTransport._BatchCreateAdUnits._get_response(
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
            resp = ad_unit_service.BatchCreateAdUnitsResponse()
            pb_resp = ad_unit_service.BatchCreateAdUnitsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_create_ad_units(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_batch_create_ad_units_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        ad_unit_service.BatchCreateAdUnitsResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.ads.admanager_v1.AdUnitServiceClient.batch_create_ad_units",
                    extra={
                        "serviceName": "google.ads.admanager.v1.AdUnitService",
                        "rpcName": "BatchCreateAdUnits",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BatchDeactivateAdUnits(
        _BaseAdUnitServiceRestTransport._BaseBatchDeactivateAdUnits,
        AdUnitServiceRestStub,
    ):
        def __hash__(self):
            return hash("AdUnitServiceRestTransport.BatchDeactivateAdUnits")

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
            request: ad_unit_service.BatchDeactivateAdUnitsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> ad_unit_service.BatchDeactivateAdUnitsResponse:
            r"""Call the batch deactivate ad units method over HTTP.

            Args:
                request (~.ad_unit_service.BatchDeactivateAdUnitsRequest):
                    The request object. Request object for ``BatchDeactivateAdUnits`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.ad_unit_service.BatchDeactivateAdUnitsResponse:
                    Response object for ``BatchDeactivateAdUnits`` method.
            """

            http_options = _BaseAdUnitServiceRestTransport._BaseBatchDeactivateAdUnits._get_http_options()
            request, metadata = self._interceptor.pre_batch_deactivate_ad_units(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAdUnitServiceRestTransport._BaseBatchDeactivateAdUnits,
                    "_BaseBatchDeactivateAdUnits__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.AdUnitServiceClient.BatchDeactivateAdUnits",
                    extra={
                        "serviceName": "google.ads.admanager.v1.AdUnitService",
                        "rpcName": "BatchDeactivateAdUnits",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AdUnitServiceRestTransport._BatchDeactivateAdUnits._get_response(
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
            resp = ad_unit_service.BatchDeactivateAdUnitsResponse()
            pb_resp = ad_unit_service.BatchDeactivateAdUnitsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_deactivate_ad_units(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_batch_deactivate_ad_units_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        ad_unit_service.BatchDeactivateAdUnitsResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.ads.admanager_v1.AdUnitServiceClient.batch_deactivate_ad_units",
                    extra={
                        "serviceName": "google.ads.admanager.v1.AdUnitService",
                        "rpcName": "BatchDeactivateAdUnits",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BatchUpdateAdUnits(
        _BaseAdUnitServiceRestTransport._BaseBatchUpdateAdUnits, AdUnitServiceRestStub
    ):
        def __hash__(self):
            return hash("AdUnitServiceRestTransport.BatchUpdateAdUnits")

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
            request: ad_unit_service.BatchUpdateAdUnitsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> ad_unit_service.BatchUpdateAdUnitsResponse:
            r"""Call the batch update ad units method over HTTP.

            Args:
                request (~.ad_unit_service.BatchUpdateAdUnitsRequest):
                    The request object. Request object for ``BatchUpdateAdUnits`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.ad_unit_service.BatchUpdateAdUnitsResponse:
                    Response object for ``BatchUpdateAdUnits`` method.
            """

            http_options = _BaseAdUnitServiceRestTransport._BaseBatchUpdateAdUnits._get_http_options()
            request, metadata = self._interceptor.pre_batch_update_ad_units(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAdUnitServiceRestTransport._BaseBatchUpdateAdUnits,
                    "_BaseBatchUpdateAdUnits__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.AdUnitServiceClient.BatchUpdateAdUnits",
                    extra={
                        "serviceName": "google.ads.admanager.v1.AdUnitService",
                        "rpcName": "BatchUpdateAdUnits",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AdUnitServiceRestTransport._BatchUpdateAdUnits._get_response(
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
            resp = ad_unit_service.BatchUpdateAdUnitsResponse()
            pb_resp = ad_unit_service.BatchUpdateAdUnitsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_update_ad_units(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_batch_update_ad_units_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        ad_unit_service.BatchUpdateAdUnitsResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.ads.admanager_v1.AdUnitServiceClient.batch_update_ad_units",
                    extra={
                        "serviceName": "google.ads.admanager.v1.AdUnitService",
                        "rpcName": "BatchUpdateAdUnits",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateAdUnit(
        _BaseAdUnitServiceRestTransport._BaseCreateAdUnit, AdUnitServiceRestStub
    ):
        def __hash__(self):
            return hash("AdUnitServiceRestTransport.CreateAdUnit")

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
            request: ad_unit_service.CreateAdUnitRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> ad_unit_messages.AdUnit:
            r"""Call the create ad unit method over HTTP.

            Args:
                request (~.ad_unit_service.CreateAdUnitRequest):
                    The request object. Request object for ``CreateAdUnit`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.ad_unit_messages.AdUnit:
                    The AdUnit resource.
            """

            http_options = (
                _BaseAdUnitServiceRestTransport._BaseCreateAdUnit._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_ad_unit(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAdUnitServiceRestTransport._BaseCreateAdUnit,
                    "_BaseCreateAdUnit__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.AdUnitServiceClient.CreateAdUnit",
                    extra={
                        "serviceName": "google.ads.admanager.v1.AdUnitService",
                        "rpcName": "CreateAdUnit",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AdUnitServiceRestTransport._CreateAdUnit._get_response(
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
            resp = ad_unit_messages.AdUnit()
            pb_resp = ad_unit_messages.AdUnit.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_ad_unit(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_ad_unit_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = ad_unit_messages.AdUnit.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.ads.admanager_v1.AdUnitServiceClient.create_ad_unit",
                    extra={
                        "serviceName": "google.ads.admanager.v1.AdUnitService",
                        "rpcName": "CreateAdUnit",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetAdUnit(
        _BaseAdUnitServiceRestTransport._BaseGetAdUnit, AdUnitServiceRestStub
    ):
        def __hash__(self):
            return hash("AdUnitServiceRestTransport.GetAdUnit")

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
            request: ad_unit_service.GetAdUnitRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> ad_unit_messages.AdUnit:
            r"""Call the get ad unit method over HTTP.

            Args:
                request (~.ad_unit_service.GetAdUnitRequest):
                    The request object. Request object for GetAdUnit method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.ad_unit_messages.AdUnit:
                    The AdUnit resource.
            """

            http_options = (
                _BaseAdUnitServiceRestTransport._BaseGetAdUnit._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_ad_unit(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAdUnitServiceRestTransport._BaseGetAdUnit,
                    "_BaseGetAdUnit__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.AdUnitServiceClient.GetAdUnit",
                    extra={
                        "serviceName": "google.ads.admanager.v1.AdUnitService",
                        "rpcName": "GetAdUnit",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AdUnitServiceRestTransport._GetAdUnit._get_response(
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
            resp = ad_unit_messages.AdUnit()
            pb_resp = ad_unit_messages.AdUnit.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_ad_unit(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_ad_unit_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = ad_unit_messages.AdUnit.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.ads.admanager_v1.AdUnitServiceClient.get_ad_unit",
                    extra={
                        "serviceName": "google.ads.admanager.v1.AdUnitService",
                        "rpcName": "GetAdUnit",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListAdUnits(
        _BaseAdUnitServiceRestTransport._BaseListAdUnits, AdUnitServiceRestStub
    ):
        def __hash__(self):
            return hash("AdUnitServiceRestTransport.ListAdUnits")

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
            request: ad_unit_service.ListAdUnitsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> ad_unit_service.ListAdUnitsResponse:
            r"""Call the list ad units method over HTTP.

            Args:
                request (~.ad_unit_service.ListAdUnitsRequest):
                    The request object. Request object for ListAdUnits
                method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.ad_unit_service.ListAdUnitsResponse:
                    Response object for
                ListAdUnitsRequest containing matching
                AdUnit resources.

            """

            http_options = (
                _BaseAdUnitServiceRestTransport._BaseListAdUnits._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_ad_units(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAdUnitServiceRestTransport._BaseListAdUnits,
                    "_BaseListAdUnits__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.AdUnitServiceClient.ListAdUnits",
                    extra={
                        "serviceName": "google.ads.admanager.v1.AdUnitService",
                        "rpcName": "ListAdUnits",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AdUnitServiceRestTransport._ListAdUnits._get_response(
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
            resp = ad_unit_service.ListAdUnitsResponse()
            pb_resp = ad_unit_service.ListAdUnitsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_ad_units(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_ad_units_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = ad_unit_service.ListAdUnitsResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.AdUnitServiceClient.list_ad_units",
                    extra={
                        "serviceName": "google.ads.admanager.v1.AdUnitService",
                        "rpcName": "ListAdUnits",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListAdUnitSizes(
        _BaseAdUnitServiceRestTransport._BaseListAdUnitSizes, AdUnitServiceRestStub
    ):
        def __hash__(self):
            return hash("AdUnitServiceRestTransport.ListAdUnitSizes")

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
            request: ad_unit_service.ListAdUnitSizesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> ad_unit_service.ListAdUnitSizesResponse:
            r"""Call the list ad unit sizes method over HTTP.

            Args:
                request (~.ad_unit_service.ListAdUnitSizesRequest):
                    The request object. Request object for ListAdUnitSizes
                method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.ad_unit_service.ListAdUnitSizesResponse:
                    Response object for
                ListAdUnitSizesRequest containing
                matching AdUnitSizes.

            """

            http_options = (
                _BaseAdUnitServiceRestTransport._BaseListAdUnitSizes._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_ad_unit_sizes(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAdUnitServiceRestTransport._BaseListAdUnitSizes,
                    "_BaseListAdUnitSizes__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.AdUnitServiceClient.ListAdUnitSizes",
                    extra={
                        "serviceName": "google.ads.admanager.v1.AdUnitService",
                        "rpcName": "ListAdUnitSizes",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AdUnitServiceRestTransport._ListAdUnitSizes._get_response(
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
            resp = ad_unit_service.ListAdUnitSizesResponse()
            pb_resp = ad_unit_service.ListAdUnitSizesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_ad_unit_sizes(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_ad_unit_sizes_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = ad_unit_service.ListAdUnitSizesResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.AdUnitServiceClient.list_ad_unit_sizes",
                    extra={
                        "serviceName": "google.ads.admanager.v1.AdUnitService",
                        "rpcName": "ListAdUnitSizes",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateAdUnit(
        _BaseAdUnitServiceRestTransport._BaseUpdateAdUnit, AdUnitServiceRestStub
    ):
        def __hash__(self):
            return hash("AdUnitServiceRestTransport.UpdateAdUnit")

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
            request: ad_unit_service.UpdateAdUnitRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> ad_unit_messages.AdUnit:
            r"""Call the update ad unit method over HTTP.

            Args:
                request (~.ad_unit_service.UpdateAdUnitRequest):
                    The request object. Request object for ``UpdateAdUnit`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.ad_unit_messages.AdUnit:
                    The AdUnit resource.
            """

            http_options = (
                _BaseAdUnitServiceRestTransport._BaseUpdateAdUnit._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_ad_unit(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAdUnitServiceRestTransport._BaseUpdateAdUnit,
                    "_BaseUpdateAdUnit__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.AdUnitServiceClient.UpdateAdUnit",
                    extra={
                        "serviceName": "google.ads.admanager.v1.AdUnitService",
                        "rpcName": "UpdateAdUnit",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AdUnitServiceRestTransport._UpdateAdUnit._get_response(
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
            resp = ad_unit_messages.AdUnit()
            pb_resp = ad_unit_messages.AdUnit.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_ad_unit(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_ad_unit_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = ad_unit_messages.AdUnit.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.ads.admanager_v1.AdUnitServiceClient.update_ad_unit",
                    extra={
                        "serviceName": "google.ads.admanager.v1.AdUnitService",
                        "rpcName": "UpdateAdUnit",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def batch_activate_ad_units(
        self,
    ) -> Callable[
        [ad_unit_service.BatchActivateAdUnitsRequest],
        ad_unit_service.BatchActivateAdUnitsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchActivateAdUnits(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def batch_archive_ad_units(
        self,
    ) -> Callable[
        [ad_unit_service.BatchArchiveAdUnitsRequest],
        ad_unit_service.BatchArchiveAdUnitsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchArchiveAdUnits(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def batch_create_ad_units(
        self,
    ) -> Callable[
        [ad_unit_service.BatchCreateAdUnitsRequest],
        ad_unit_service.BatchCreateAdUnitsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchCreateAdUnits(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def batch_deactivate_ad_units(
        self,
    ) -> Callable[
        [ad_unit_service.BatchDeactivateAdUnitsRequest],
        ad_unit_service.BatchDeactivateAdUnitsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchDeactivateAdUnits(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def batch_update_ad_units(
        self,
    ) -> Callable[
        [ad_unit_service.BatchUpdateAdUnitsRequest],
        ad_unit_service.BatchUpdateAdUnitsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchUpdateAdUnits(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_ad_unit(
        self,
    ) -> Callable[[ad_unit_service.CreateAdUnitRequest], ad_unit_messages.AdUnit]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateAdUnit(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_ad_unit(
        self,
    ) -> Callable[[ad_unit_service.GetAdUnitRequest], ad_unit_messages.AdUnit]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetAdUnit(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_ad_units(
        self,
    ) -> Callable[
        [ad_unit_service.ListAdUnitsRequest], ad_unit_service.ListAdUnitsResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListAdUnits(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_ad_unit_sizes(
        self,
    ) -> Callable[
        [ad_unit_service.ListAdUnitSizesRequest],
        ad_unit_service.ListAdUnitSizesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListAdUnitSizes(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_ad_unit(
        self,
    ) -> Callable[[ad_unit_service.UpdateAdUnitRequest], ad_unit_messages.AdUnit]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateAdUnit(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def cancel_operation(self):
        return self._CancelOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _CancelOperation(
        _BaseAdUnitServiceRestTransport._BaseCancelOperation, AdUnitServiceRestStub
    ):
        def __hash__(self):
            return hash("AdUnitServiceRestTransport.CancelOperation")

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
                _BaseAdUnitServiceRestTransport._BaseCancelOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_cancel_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAdUnitServiceRestTransport._BaseCancelOperation,
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
                    f"Sending request for google.ads.admanager_v1.AdUnitServiceClient.CancelOperation",
                    extra={
                        "serviceName": "google.ads.admanager.v1.AdUnitService",
                        "rpcName": "CancelOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AdUnitServiceRestTransport._CancelOperation._get_response(
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
        _BaseAdUnitServiceRestTransport._BaseGetOperation, AdUnitServiceRestStub
    ):
        def __hash__(self):
            return hash("AdUnitServiceRestTransport.GetOperation")

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
                _BaseAdUnitServiceRestTransport._BaseGetOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_operation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAdUnitServiceRestTransport._BaseGetOperation,
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
                    f"Sending request for google.ads.admanager_v1.AdUnitServiceClient.GetOperation",
                    extra={
                        "serviceName": "google.ads.admanager.v1.AdUnitService",
                        "rpcName": "GetOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AdUnitServiceRestTransport._GetOperation._get_response(
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
                    "Received response for google.ads.admanager_v1.AdUnitServiceAsyncClient.GetOperation",
                    extra={
                        "serviceName": "google.ads.admanager.v1.AdUnitService",
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


__all__ = ("AdUnitServiceRestTransport",)
