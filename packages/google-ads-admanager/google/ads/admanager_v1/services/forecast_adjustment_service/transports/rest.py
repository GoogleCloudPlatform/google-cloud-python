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
    forecast_adjustment_messages,
    forecast_adjustment_service,
)

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseForecastAdjustmentServiceRestTransport

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


class ForecastAdjustmentServiceRestInterceptor:
    """Interceptor for ForecastAdjustmentService.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the ForecastAdjustmentServiceRestTransport.

    .. code-block:: python
        class MyCustomForecastAdjustmentServiceInterceptor(ForecastAdjustmentServiceRestInterceptor):
            def pre_batch_activate_forecast_adjustments(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_activate_forecast_adjustments(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_batch_create_forecast_adjustments(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_create_forecast_adjustments(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_batch_deactivate_forecast_adjustments(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_deactivate_forecast_adjustments(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_batch_update_forecast_adjustments(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_update_forecast_adjustments(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_calculate_daily_ad_opportunity_counts(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_calculate_daily_ad_opportunity_counts(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_forecast_adjustment(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_forecast_adjustment(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_forecast_adjustment(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_forecast_adjustment(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_forecast_adjustments(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_forecast_adjustments(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_forecast_adjustment(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_forecast_adjustment(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = ForecastAdjustmentServiceRestTransport(interceptor=MyCustomForecastAdjustmentServiceInterceptor())
        client = ForecastAdjustmentServiceClient(transport=transport)


    """

    def pre_batch_activate_forecast_adjustments(
        self,
        request: forecast_adjustment_service.BatchActivateForecastAdjustmentsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        forecast_adjustment_service.BatchActivateForecastAdjustmentsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_activate_forecast_adjustments

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ForecastAdjustmentService server.
        """
        return request, metadata

    def post_batch_activate_forecast_adjustments(
        self,
        response: forecast_adjustment_service.BatchActivateForecastAdjustmentsResponse,
    ) -> forecast_adjustment_service.BatchActivateForecastAdjustmentsResponse:
        """Post-rpc interceptor for batch_activate_forecast_adjustments

        DEPRECATED. Please use the `post_batch_activate_forecast_adjustments_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ForecastAdjustmentService server but before
        it is returned to user code. This `post_batch_activate_forecast_adjustments` interceptor runs
        before the `post_batch_activate_forecast_adjustments_with_metadata` interceptor.
        """
        return response

    def post_batch_activate_forecast_adjustments_with_metadata(
        self,
        response: forecast_adjustment_service.BatchActivateForecastAdjustmentsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        forecast_adjustment_service.BatchActivateForecastAdjustmentsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_activate_forecast_adjustments

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ForecastAdjustmentService server but before it is returned to user code.

        We recommend only using this `post_batch_activate_forecast_adjustments_with_metadata`
        interceptor in new development instead of the `post_batch_activate_forecast_adjustments` interceptor.
        When both interceptors are used, this `post_batch_activate_forecast_adjustments_with_metadata` interceptor runs after the
        `post_batch_activate_forecast_adjustments` interceptor. The (possibly modified) response returned by
        `post_batch_activate_forecast_adjustments` will be passed to
        `post_batch_activate_forecast_adjustments_with_metadata`.
        """
        return response, metadata

    def pre_batch_create_forecast_adjustments(
        self,
        request: forecast_adjustment_service.BatchCreateForecastAdjustmentsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        forecast_adjustment_service.BatchCreateForecastAdjustmentsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_create_forecast_adjustments

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ForecastAdjustmentService server.
        """
        return request, metadata

    def post_batch_create_forecast_adjustments(
        self,
        response: forecast_adjustment_service.BatchCreateForecastAdjustmentsResponse,
    ) -> forecast_adjustment_service.BatchCreateForecastAdjustmentsResponse:
        """Post-rpc interceptor for batch_create_forecast_adjustments

        DEPRECATED. Please use the `post_batch_create_forecast_adjustments_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ForecastAdjustmentService server but before
        it is returned to user code. This `post_batch_create_forecast_adjustments` interceptor runs
        before the `post_batch_create_forecast_adjustments_with_metadata` interceptor.
        """
        return response

    def post_batch_create_forecast_adjustments_with_metadata(
        self,
        response: forecast_adjustment_service.BatchCreateForecastAdjustmentsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        forecast_adjustment_service.BatchCreateForecastAdjustmentsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_create_forecast_adjustments

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ForecastAdjustmentService server but before it is returned to user code.

        We recommend only using this `post_batch_create_forecast_adjustments_with_metadata`
        interceptor in new development instead of the `post_batch_create_forecast_adjustments` interceptor.
        When both interceptors are used, this `post_batch_create_forecast_adjustments_with_metadata` interceptor runs after the
        `post_batch_create_forecast_adjustments` interceptor. The (possibly modified) response returned by
        `post_batch_create_forecast_adjustments` will be passed to
        `post_batch_create_forecast_adjustments_with_metadata`.
        """
        return response, metadata

    def pre_batch_deactivate_forecast_adjustments(
        self,
        request: forecast_adjustment_service.BatchDeactivateForecastAdjustmentsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        forecast_adjustment_service.BatchDeactivateForecastAdjustmentsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_deactivate_forecast_adjustments

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ForecastAdjustmentService server.
        """
        return request, metadata

    def post_batch_deactivate_forecast_adjustments(
        self,
        response: forecast_adjustment_service.BatchDeactivateForecastAdjustmentsResponse,
    ) -> forecast_adjustment_service.BatchDeactivateForecastAdjustmentsResponse:
        """Post-rpc interceptor for batch_deactivate_forecast_adjustments

        DEPRECATED. Please use the `post_batch_deactivate_forecast_adjustments_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ForecastAdjustmentService server but before
        it is returned to user code. This `post_batch_deactivate_forecast_adjustments` interceptor runs
        before the `post_batch_deactivate_forecast_adjustments_with_metadata` interceptor.
        """
        return response

    def post_batch_deactivate_forecast_adjustments_with_metadata(
        self,
        response: forecast_adjustment_service.BatchDeactivateForecastAdjustmentsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        forecast_adjustment_service.BatchDeactivateForecastAdjustmentsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_deactivate_forecast_adjustments

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ForecastAdjustmentService server but before it is returned to user code.

        We recommend only using this `post_batch_deactivate_forecast_adjustments_with_metadata`
        interceptor in new development instead of the `post_batch_deactivate_forecast_adjustments` interceptor.
        When both interceptors are used, this `post_batch_deactivate_forecast_adjustments_with_metadata` interceptor runs after the
        `post_batch_deactivate_forecast_adjustments` interceptor. The (possibly modified) response returned by
        `post_batch_deactivate_forecast_adjustments` will be passed to
        `post_batch_deactivate_forecast_adjustments_with_metadata`.
        """
        return response, metadata

    def pre_batch_update_forecast_adjustments(
        self,
        request: forecast_adjustment_service.BatchUpdateForecastAdjustmentsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        forecast_adjustment_service.BatchUpdateForecastAdjustmentsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_update_forecast_adjustments

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ForecastAdjustmentService server.
        """
        return request, metadata

    def post_batch_update_forecast_adjustments(
        self,
        response: forecast_adjustment_service.BatchUpdateForecastAdjustmentsResponse,
    ) -> forecast_adjustment_service.BatchUpdateForecastAdjustmentsResponse:
        """Post-rpc interceptor for batch_update_forecast_adjustments

        DEPRECATED. Please use the `post_batch_update_forecast_adjustments_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ForecastAdjustmentService server but before
        it is returned to user code. This `post_batch_update_forecast_adjustments` interceptor runs
        before the `post_batch_update_forecast_adjustments_with_metadata` interceptor.
        """
        return response

    def post_batch_update_forecast_adjustments_with_metadata(
        self,
        response: forecast_adjustment_service.BatchUpdateForecastAdjustmentsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        forecast_adjustment_service.BatchUpdateForecastAdjustmentsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_update_forecast_adjustments

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ForecastAdjustmentService server but before it is returned to user code.

        We recommend only using this `post_batch_update_forecast_adjustments_with_metadata`
        interceptor in new development instead of the `post_batch_update_forecast_adjustments` interceptor.
        When both interceptors are used, this `post_batch_update_forecast_adjustments_with_metadata` interceptor runs after the
        `post_batch_update_forecast_adjustments` interceptor. The (possibly modified) response returned by
        `post_batch_update_forecast_adjustments` will be passed to
        `post_batch_update_forecast_adjustments_with_metadata`.
        """
        return response, metadata

    def pre_calculate_daily_ad_opportunity_counts(
        self,
        request: forecast_adjustment_service.CalculateDailyAdOpportunityCountsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        forecast_adjustment_service.CalculateDailyAdOpportunityCountsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for calculate_daily_ad_opportunity_counts

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ForecastAdjustmentService server.
        """
        return request, metadata

    def post_calculate_daily_ad_opportunity_counts(
        self,
        response: forecast_adjustment_service.CalculateDailyAdOpportunityCountsResponse,
    ) -> forecast_adjustment_service.CalculateDailyAdOpportunityCountsResponse:
        """Post-rpc interceptor for calculate_daily_ad_opportunity_counts

        DEPRECATED. Please use the `post_calculate_daily_ad_opportunity_counts_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ForecastAdjustmentService server but before
        it is returned to user code. This `post_calculate_daily_ad_opportunity_counts` interceptor runs
        before the `post_calculate_daily_ad_opportunity_counts_with_metadata` interceptor.
        """
        return response

    def post_calculate_daily_ad_opportunity_counts_with_metadata(
        self,
        response: forecast_adjustment_service.CalculateDailyAdOpportunityCountsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        forecast_adjustment_service.CalculateDailyAdOpportunityCountsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for calculate_daily_ad_opportunity_counts

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ForecastAdjustmentService server but before it is returned to user code.

        We recommend only using this `post_calculate_daily_ad_opportunity_counts_with_metadata`
        interceptor in new development instead of the `post_calculate_daily_ad_opportunity_counts` interceptor.
        When both interceptors are used, this `post_calculate_daily_ad_opportunity_counts_with_metadata` interceptor runs after the
        `post_calculate_daily_ad_opportunity_counts` interceptor. The (possibly modified) response returned by
        `post_calculate_daily_ad_opportunity_counts` will be passed to
        `post_calculate_daily_ad_opportunity_counts_with_metadata`.
        """
        return response, metadata

    def pre_create_forecast_adjustment(
        self,
        request: forecast_adjustment_service.CreateForecastAdjustmentRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        forecast_adjustment_service.CreateForecastAdjustmentRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_forecast_adjustment

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ForecastAdjustmentService server.
        """
        return request, metadata

    def post_create_forecast_adjustment(
        self, response: forecast_adjustment_messages.ForecastAdjustment
    ) -> forecast_adjustment_messages.ForecastAdjustment:
        """Post-rpc interceptor for create_forecast_adjustment

        DEPRECATED. Please use the `post_create_forecast_adjustment_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ForecastAdjustmentService server but before
        it is returned to user code. This `post_create_forecast_adjustment` interceptor runs
        before the `post_create_forecast_adjustment_with_metadata` interceptor.
        """
        return response

    def post_create_forecast_adjustment_with_metadata(
        self,
        response: forecast_adjustment_messages.ForecastAdjustment,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        forecast_adjustment_messages.ForecastAdjustment,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for create_forecast_adjustment

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ForecastAdjustmentService server but before it is returned to user code.

        We recommend only using this `post_create_forecast_adjustment_with_metadata`
        interceptor in new development instead of the `post_create_forecast_adjustment` interceptor.
        When both interceptors are used, this `post_create_forecast_adjustment_with_metadata` interceptor runs after the
        `post_create_forecast_adjustment` interceptor. The (possibly modified) response returned by
        `post_create_forecast_adjustment` will be passed to
        `post_create_forecast_adjustment_with_metadata`.
        """
        return response, metadata

    def pre_get_forecast_adjustment(
        self,
        request: forecast_adjustment_service.GetForecastAdjustmentRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        forecast_adjustment_service.GetForecastAdjustmentRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_forecast_adjustment

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ForecastAdjustmentService server.
        """
        return request, metadata

    def post_get_forecast_adjustment(
        self, response: forecast_adjustment_messages.ForecastAdjustment
    ) -> forecast_adjustment_messages.ForecastAdjustment:
        """Post-rpc interceptor for get_forecast_adjustment

        DEPRECATED. Please use the `post_get_forecast_adjustment_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ForecastAdjustmentService server but before
        it is returned to user code. This `post_get_forecast_adjustment` interceptor runs
        before the `post_get_forecast_adjustment_with_metadata` interceptor.
        """
        return response

    def post_get_forecast_adjustment_with_metadata(
        self,
        response: forecast_adjustment_messages.ForecastAdjustment,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        forecast_adjustment_messages.ForecastAdjustment,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for get_forecast_adjustment

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ForecastAdjustmentService server but before it is returned to user code.

        We recommend only using this `post_get_forecast_adjustment_with_metadata`
        interceptor in new development instead of the `post_get_forecast_adjustment` interceptor.
        When both interceptors are used, this `post_get_forecast_adjustment_with_metadata` interceptor runs after the
        `post_get_forecast_adjustment` interceptor. The (possibly modified) response returned by
        `post_get_forecast_adjustment` will be passed to
        `post_get_forecast_adjustment_with_metadata`.
        """
        return response, metadata

    def pre_list_forecast_adjustments(
        self,
        request: forecast_adjustment_service.ListForecastAdjustmentsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        forecast_adjustment_service.ListForecastAdjustmentsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_forecast_adjustments

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ForecastAdjustmentService server.
        """
        return request, metadata

    def post_list_forecast_adjustments(
        self, response: forecast_adjustment_service.ListForecastAdjustmentsResponse
    ) -> forecast_adjustment_service.ListForecastAdjustmentsResponse:
        """Post-rpc interceptor for list_forecast_adjustments

        DEPRECATED. Please use the `post_list_forecast_adjustments_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ForecastAdjustmentService server but before
        it is returned to user code. This `post_list_forecast_adjustments` interceptor runs
        before the `post_list_forecast_adjustments_with_metadata` interceptor.
        """
        return response

    def post_list_forecast_adjustments_with_metadata(
        self,
        response: forecast_adjustment_service.ListForecastAdjustmentsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        forecast_adjustment_service.ListForecastAdjustmentsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_forecast_adjustments

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ForecastAdjustmentService server but before it is returned to user code.

        We recommend only using this `post_list_forecast_adjustments_with_metadata`
        interceptor in new development instead of the `post_list_forecast_adjustments` interceptor.
        When both interceptors are used, this `post_list_forecast_adjustments_with_metadata` interceptor runs after the
        `post_list_forecast_adjustments` interceptor. The (possibly modified) response returned by
        `post_list_forecast_adjustments` will be passed to
        `post_list_forecast_adjustments_with_metadata`.
        """
        return response, metadata

    def pre_update_forecast_adjustment(
        self,
        request: forecast_adjustment_service.UpdateForecastAdjustmentRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        forecast_adjustment_service.UpdateForecastAdjustmentRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_forecast_adjustment

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ForecastAdjustmentService server.
        """
        return request, metadata

    def post_update_forecast_adjustment(
        self, response: forecast_adjustment_messages.ForecastAdjustment
    ) -> forecast_adjustment_messages.ForecastAdjustment:
        """Post-rpc interceptor for update_forecast_adjustment

        DEPRECATED. Please use the `post_update_forecast_adjustment_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ForecastAdjustmentService server but before
        it is returned to user code. This `post_update_forecast_adjustment` interceptor runs
        before the `post_update_forecast_adjustment_with_metadata` interceptor.
        """
        return response

    def post_update_forecast_adjustment_with_metadata(
        self,
        response: forecast_adjustment_messages.ForecastAdjustment,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        forecast_adjustment_messages.ForecastAdjustment,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for update_forecast_adjustment

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ForecastAdjustmentService server but before it is returned to user code.

        We recommend only using this `post_update_forecast_adjustment_with_metadata`
        interceptor in new development instead of the `post_update_forecast_adjustment` interceptor.
        When both interceptors are used, this `post_update_forecast_adjustment_with_metadata` interceptor runs after the
        `post_update_forecast_adjustment` interceptor. The (possibly modified) response returned by
        `post_update_forecast_adjustment` will be passed to
        `post_update_forecast_adjustment_with_metadata`.
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
        before they are sent to the ForecastAdjustmentService server.
        """
        return request, metadata

    def post_cancel_operation(self, response: None) -> None:
        """Post-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the response
        after it is returned by the ForecastAdjustmentService server but before
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
        before they are sent to the ForecastAdjustmentService server.
        """
        return request, metadata

    def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the ForecastAdjustmentService server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class ForecastAdjustmentServiceRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: ForecastAdjustmentServiceRestInterceptor


class ForecastAdjustmentServiceRestTransport(
    _BaseForecastAdjustmentServiceRestTransport
):
    """REST backend synchronous transport for ForecastAdjustmentService.

    Provides methods for handling ``ForecastAdjustment`` objects.

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
        interceptor: Optional[ForecastAdjustmentServiceRestInterceptor] = None,
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
            interceptor (Optional[ForecastAdjustmentServiceRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or ForecastAdjustmentServiceRestInterceptor()
        self._prep_wrapped_messages(client_info)

    class _BatchActivateForecastAdjustments(
        _BaseForecastAdjustmentServiceRestTransport._BaseBatchActivateForecastAdjustments,
        ForecastAdjustmentServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "ForecastAdjustmentServiceRestTransport.BatchActivateForecastAdjustments"
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
            request: forecast_adjustment_service.BatchActivateForecastAdjustmentsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> forecast_adjustment_service.BatchActivateForecastAdjustmentsResponse:
            r"""Call the batch activate forecast
            adjustments method over HTTP.

                Args:
                    request (~.forecast_adjustment_service.BatchActivateForecastAdjustmentsRequest):
                        The request object. Request message for ``BatchActivateForecastAdjustments``
                    method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.forecast_adjustment_service.BatchActivateForecastAdjustmentsResponse:
                        Response object for ``BatchActivateForecastAdjustments``
                    method.

            """

            http_options = _BaseForecastAdjustmentServiceRestTransport._BaseBatchActivateForecastAdjustments._get_http_options()
            request, metadata = (
                self._interceptor.pre_batch_activate_forecast_adjustments(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseForecastAdjustmentServiceRestTransport._BaseBatchActivateForecastAdjustments,
                    "_BaseBatchActivateForecastAdjustments__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.ForecastAdjustmentServiceClient.BatchActivateForecastAdjustments",
                    extra={
                        "serviceName": "google.ads.admanager.v1.ForecastAdjustmentService",
                        "rpcName": "BatchActivateForecastAdjustments",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ForecastAdjustmentServiceRestTransport._BatchActivateForecastAdjustments._get_response(
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
                forecast_adjustment_service.BatchActivateForecastAdjustmentsResponse()
            )
            pb_resp = (
                forecast_adjustment_service.BatchActivateForecastAdjustmentsResponse.pb(
                    resp
                )
            )

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_activate_forecast_adjustments(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_batch_activate_forecast_adjustments_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = forecast_adjustment_service.BatchActivateForecastAdjustmentsResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.ForecastAdjustmentServiceClient.batch_activate_forecast_adjustments",
                    extra={
                        "serviceName": "google.ads.admanager.v1.ForecastAdjustmentService",
                        "rpcName": "BatchActivateForecastAdjustments",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BatchCreateForecastAdjustments(
        _BaseForecastAdjustmentServiceRestTransport._BaseBatchCreateForecastAdjustments,
        ForecastAdjustmentServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "ForecastAdjustmentServiceRestTransport.BatchCreateForecastAdjustments"
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
            request: forecast_adjustment_service.BatchCreateForecastAdjustmentsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> forecast_adjustment_service.BatchCreateForecastAdjustmentsResponse:
            r"""Call the batch create forecast
            adjustments method over HTTP.

                Args:
                    request (~.forecast_adjustment_service.BatchCreateForecastAdjustmentsRequest):
                        The request object. Request object for ``BatchCreateForecastAdjustments``
                    method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.forecast_adjustment_service.BatchCreateForecastAdjustmentsResponse:
                        Response object for ``BatchCreateForecastAdjustments``
                    method.

            """

            http_options = _BaseForecastAdjustmentServiceRestTransport._BaseBatchCreateForecastAdjustments._get_http_options()
            request, metadata = self._interceptor.pre_batch_create_forecast_adjustments(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseForecastAdjustmentServiceRestTransport._BaseBatchCreateForecastAdjustments,
                    "_BaseBatchCreateForecastAdjustments__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.ForecastAdjustmentServiceClient.BatchCreateForecastAdjustments",
                    extra={
                        "serviceName": "google.ads.admanager.v1.ForecastAdjustmentService",
                        "rpcName": "BatchCreateForecastAdjustments",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ForecastAdjustmentServiceRestTransport._BatchCreateForecastAdjustments._get_response(
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
            resp = forecast_adjustment_service.BatchCreateForecastAdjustmentsResponse()
            pb_resp = (
                forecast_adjustment_service.BatchCreateForecastAdjustmentsResponse.pb(
                    resp
                )
            )

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_create_forecast_adjustments(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_batch_create_forecast_adjustments_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = forecast_adjustment_service.BatchCreateForecastAdjustmentsResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.ForecastAdjustmentServiceClient.batch_create_forecast_adjustments",
                    extra={
                        "serviceName": "google.ads.admanager.v1.ForecastAdjustmentService",
                        "rpcName": "BatchCreateForecastAdjustments",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BatchDeactivateForecastAdjustments(
        _BaseForecastAdjustmentServiceRestTransport._BaseBatchDeactivateForecastAdjustments,
        ForecastAdjustmentServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "ForecastAdjustmentServiceRestTransport.BatchDeactivateForecastAdjustments"
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
            request: forecast_adjustment_service.BatchDeactivateForecastAdjustmentsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> forecast_adjustment_service.BatchDeactivateForecastAdjustmentsResponse:
            r"""Call the batch deactivate forecast
            adjustments method over HTTP.

                Args:
                    request (~.forecast_adjustment_service.BatchDeactivateForecastAdjustmentsRequest):
                        The request object. Request message for
                    ``BatchDeactivateForecastAdjustments`` method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.forecast_adjustment_service.BatchDeactivateForecastAdjustmentsResponse:
                        Response object for
                    ``BatchDeactivateForecastAdjustments`` method.

            """

            http_options = _BaseForecastAdjustmentServiceRestTransport._BaseBatchDeactivateForecastAdjustments._get_http_options()
            request, metadata = (
                self._interceptor.pre_batch_deactivate_forecast_adjustments(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseForecastAdjustmentServiceRestTransport._BaseBatchDeactivateForecastAdjustments,
                    "_BaseBatchDeactivateForecastAdjustments__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.ForecastAdjustmentServiceClient.BatchDeactivateForecastAdjustments",
                    extra={
                        "serviceName": "google.ads.admanager.v1.ForecastAdjustmentService",
                        "rpcName": "BatchDeactivateForecastAdjustments",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ForecastAdjustmentServiceRestTransport._BatchDeactivateForecastAdjustments._get_response(
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
                forecast_adjustment_service.BatchDeactivateForecastAdjustmentsResponse()
            )
            pb_resp = forecast_adjustment_service.BatchDeactivateForecastAdjustmentsResponse.pb(
                resp
            )

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_deactivate_forecast_adjustments(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_batch_deactivate_forecast_adjustments_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = forecast_adjustment_service.BatchDeactivateForecastAdjustmentsResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.ForecastAdjustmentServiceClient.batch_deactivate_forecast_adjustments",
                    extra={
                        "serviceName": "google.ads.admanager.v1.ForecastAdjustmentService",
                        "rpcName": "BatchDeactivateForecastAdjustments",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BatchUpdateForecastAdjustments(
        _BaseForecastAdjustmentServiceRestTransport._BaseBatchUpdateForecastAdjustments,
        ForecastAdjustmentServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "ForecastAdjustmentServiceRestTransport.BatchUpdateForecastAdjustments"
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
            request: forecast_adjustment_service.BatchUpdateForecastAdjustmentsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> forecast_adjustment_service.BatchUpdateForecastAdjustmentsResponse:
            r"""Call the batch update forecast
            adjustments method over HTTP.

                Args:
                    request (~.forecast_adjustment_service.BatchUpdateForecastAdjustmentsRequest):
                        The request object. Request object for ``BatchUpdateForecastAdjustments``
                    method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.forecast_adjustment_service.BatchUpdateForecastAdjustmentsResponse:
                        Response object for ``BatchUpdateForecastAdjustments``
                    method.

            """

            http_options = _BaseForecastAdjustmentServiceRestTransport._BaseBatchUpdateForecastAdjustments._get_http_options()
            request, metadata = self._interceptor.pre_batch_update_forecast_adjustments(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseForecastAdjustmentServiceRestTransport._BaseBatchUpdateForecastAdjustments,
                    "_BaseBatchUpdateForecastAdjustments__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.ForecastAdjustmentServiceClient.BatchUpdateForecastAdjustments",
                    extra={
                        "serviceName": "google.ads.admanager.v1.ForecastAdjustmentService",
                        "rpcName": "BatchUpdateForecastAdjustments",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ForecastAdjustmentServiceRestTransport._BatchUpdateForecastAdjustments._get_response(
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
            resp = forecast_adjustment_service.BatchUpdateForecastAdjustmentsResponse()
            pb_resp = (
                forecast_adjustment_service.BatchUpdateForecastAdjustmentsResponse.pb(
                    resp
                )
            )

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_update_forecast_adjustments(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_batch_update_forecast_adjustments_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = forecast_adjustment_service.BatchUpdateForecastAdjustmentsResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.ForecastAdjustmentServiceClient.batch_update_forecast_adjustments",
                    extra={
                        "serviceName": "google.ads.admanager.v1.ForecastAdjustmentService",
                        "rpcName": "BatchUpdateForecastAdjustments",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CalculateDailyAdOpportunityCounts(
        _BaseForecastAdjustmentServiceRestTransport._BaseCalculateDailyAdOpportunityCounts,
        ForecastAdjustmentServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "ForecastAdjustmentServiceRestTransport.CalculateDailyAdOpportunityCounts"
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
            request: forecast_adjustment_service.CalculateDailyAdOpportunityCountsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> forecast_adjustment_service.CalculateDailyAdOpportunityCountsResponse:
            r"""Call the calculate daily ad
            opportunity counts method over HTTP.

                Args:
                    request (~.forecast_adjustment_service.CalculateDailyAdOpportunityCountsRequest):
                        The request object. Request message for
                    ``CalculateDailyAdOpportunityCounts`` method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.forecast_adjustment_service.CalculateDailyAdOpportunityCountsResponse:
                        Response message for
                    ``CalculateDailyAdOpportunityCounts`` method.

            """

            http_options = _BaseForecastAdjustmentServiceRestTransport._BaseCalculateDailyAdOpportunityCounts._get_http_options()
            request, metadata = (
                self._interceptor.pre_calculate_daily_ad_opportunity_counts(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseForecastAdjustmentServiceRestTransport._BaseCalculateDailyAdOpportunityCounts,
                    "_BaseCalculateDailyAdOpportunityCounts__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.ForecastAdjustmentServiceClient.CalculateDailyAdOpportunityCounts",
                    extra={
                        "serviceName": "google.ads.admanager.v1.ForecastAdjustmentService",
                        "rpcName": "CalculateDailyAdOpportunityCounts",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ForecastAdjustmentServiceRestTransport._CalculateDailyAdOpportunityCounts._get_response(
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
                forecast_adjustment_service.CalculateDailyAdOpportunityCountsResponse()
            )
            pb_resp = forecast_adjustment_service.CalculateDailyAdOpportunityCountsResponse.pb(
                resp
            )

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_calculate_daily_ad_opportunity_counts(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_calculate_daily_ad_opportunity_counts_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = forecast_adjustment_service.CalculateDailyAdOpportunityCountsResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.ForecastAdjustmentServiceClient.calculate_daily_ad_opportunity_counts",
                    extra={
                        "serviceName": "google.ads.admanager.v1.ForecastAdjustmentService",
                        "rpcName": "CalculateDailyAdOpportunityCounts",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateForecastAdjustment(
        _BaseForecastAdjustmentServiceRestTransport._BaseCreateForecastAdjustment,
        ForecastAdjustmentServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "ForecastAdjustmentServiceRestTransport.CreateForecastAdjustment"
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
            request: forecast_adjustment_service.CreateForecastAdjustmentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> forecast_adjustment_messages.ForecastAdjustment:
            r"""Call the create forecast
            adjustment method over HTTP.

                Args:
                    request (~.forecast_adjustment_service.CreateForecastAdjustmentRequest):
                        The request object. Request object for ``CreateForecastAdjustment`` method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.forecast_adjustment_messages.ForecastAdjustment:
                        Provides information about the
                    expected volume and composition of
                    traffic over a date range for a traffic
                    forecast segment.

            """

            http_options = _BaseForecastAdjustmentServiceRestTransport._BaseCreateForecastAdjustment._get_http_options()
            request, metadata = self._interceptor.pre_create_forecast_adjustment(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseForecastAdjustmentServiceRestTransport._BaseCreateForecastAdjustment,
                    "_BaseCreateForecastAdjustment__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.ForecastAdjustmentServiceClient.CreateForecastAdjustment",
                    extra={
                        "serviceName": "google.ads.admanager.v1.ForecastAdjustmentService",
                        "rpcName": "CreateForecastAdjustment",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ForecastAdjustmentServiceRestTransport._CreateForecastAdjustment._get_response(
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
            resp = forecast_adjustment_messages.ForecastAdjustment()
            pb_resp = forecast_adjustment_messages.ForecastAdjustment.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_forecast_adjustment(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_forecast_adjustment_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        forecast_adjustment_messages.ForecastAdjustment.to_json(
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
                    "Received response for google.ads.admanager_v1.ForecastAdjustmentServiceClient.create_forecast_adjustment",
                    extra={
                        "serviceName": "google.ads.admanager.v1.ForecastAdjustmentService",
                        "rpcName": "CreateForecastAdjustment",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetForecastAdjustment(
        _BaseForecastAdjustmentServiceRestTransport._BaseGetForecastAdjustment,
        ForecastAdjustmentServiceRestStub,
    ):
        def __hash__(self):
            return hash("ForecastAdjustmentServiceRestTransport.GetForecastAdjustment")

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
            request: forecast_adjustment_service.GetForecastAdjustmentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> forecast_adjustment_messages.ForecastAdjustment:
            r"""Call the get forecast adjustment method over HTTP.

            Args:
                request (~.forecast_adjustment_service.GetForecastAdjustmentRequest):
                    The request object. Request object for ``GetForecastAdjustment`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.forecast_adjustment_messages.ForecastAdjustment:
                    Provides information about the
                expected volume and composition of
                traffic over a date range for a traffic
                forecast segment.

            """

            http_options = _BaseForecastAdjustmentServiceRestTransport._BaseGetForecastAdjustment._get_http_options()
            request, metadata = self._interceptor.pre_get_forecast_adjustment(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseForecastAdjustmentServiceRestTransport._BaseGetForecastAdjustment,
                    "_BaseGetForecastAdjustment__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.ForecastAdjustmentServiceClient.GetForecastAdjustment",
                    extra={
                        "serviceName": "google.ads.admanager.v1.ForecastAdjustmentService",
                        "rpcName": "GetForecastAdjustment",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ForecastAdjustmentServiceRestTransport._GetForecastAdjustment._get_response(
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
            resp = forecast_adjustment_messages.ForecastAdjustment()
            pb_resp = forecast_adjustment_messages.ForecastAdjustment.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_forecast_adjustment(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_forecast_adjustment_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        forecast_adjustment_messages.ForecastAdjustment.to_json(
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
                    "Received response for google.ads.admanager_v1.ForecastAdjustmentServiceClient.get_forecast_adjustment",
                    extra={
                        "serviceName": "google.ads.admanager.v1.ForecastAdjustmentService",
                        "rpcName": "GetForecastAdjustment",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListForecastAdjustments(
        _BaseForecastAdjustmentServiceRestTransport._BaseListForecastAdjustments,
        ForecastAdjustmentServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "ForecastAdjustmentServiceRestTransport.ListForecastAdjustments"
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
            )
            return response

        def __call__(
            self,
            request: forecast_adjustment_service.ListForecastAdjustmentsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> forecast_adjustment_service.ListForecastAdjustmentsResponse:
            r"""Call the list forecast adjustments method over HTTP.

            Args:
                request (~.forecast_adjustment_service.ListForecastAdjustmentsRequest):
                    The request object. Request object for ``ListForecastAdjustments`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.forecast_adjustment_service.ListForecastAdjustmentsResponse:
                    Response object for ``ListForecastAdjustmentsRequest``
                containing matching ``ForecastAdjustment`` objects.

            """

            http_options = _BaseForecastAdjustmentServiceRestTransport._BaseListForecastAdjustments._get_http_options()
            request, metadata = self._interceptor.pre_list_forecast_adjustments(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseForecastAdjustmentServiceRestTransport._BaseListForecastAdjustments,
                    "_BaseListForecastAdjustments__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.ForecastAdjustmentServiceClient.ListForecastAdjustments",
                    extra={
                        "serviceName": "google.ads.admanager.v1.ForecastAdjustmentService",
                        "rpcName": "ListForecastAdjustments",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ForecastAdjustmentServiceRestTransport._ListForecastAdjustments._get_response(
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
            resp = forecast_adjustment_service.ListForecastAdjustmentsResponse()
            pb_resp = forecast_adjustment_service.ListForecastAdjustmentsResponse.pb(
                resp
            )

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_forecast_adjustments(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_forecast_adjustments_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = forecast_adjustment_service.ListForecastAdjustmentsResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.ForecastAdjustmentServiceClient.list_forecast_adjustments",
                    extra={
                        "serviceName": "google.ads.admanager.v1.ForecastAdjustmentService",
                        "rpcName": "ListForecastAdjustments",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateForecastAdjustment(
        _BaseForecastAdjustmentServiceRestTransport._BaseUpdateForecastAdjustment,
        ForecastAdjustmentServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "ForecastAdjustmentServiceRestTransport.UpdateForecastAdjustment"
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
            request: forecast_adjustment_service.UpdateForecastAdjustmentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> forecast_adjustment_messages.ForecastAdjustment:
            r"""Call the update forecast
            adjustment method over HTTP.

                Args:
                    request (~.forecast_adjustment_service.UpdateForecastAdjustmentRequest):
                        The request object. Request object for ``UpdateForecastAdjustment`` method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.forecast_adjustment_messages.ForecastAdjustment:
                        Provides information about the
                    expected volume and composition of
                    traffic over a date range for a traffic
                    forecast segment.

            """

            http_options = _BaseForecastAdjustmentServiceRestTransport._BaseUpdateForecastAdjustment._get_http_options()
            request, metadata = self._interceptor.pre_update_forecast_adjustment(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseForecastAdjustmentServiceRestTransport._BaseUpdateForecastAdjustment,
                    "_BaseUpdateForecastAdjustment__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.ForecastAdjustmentServiceClient.UpdateForecastAdjustment",
                    extra={
                        "serviceName": "google.ads.admanager.v1.ForecastAdjustmentService",
                        "rpcName": "UpdateForecastAdjustment",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ForecastAdjustmentServiceRestTransport._UpdateForecastAdjustment._get_response(
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
            resp = forecast_adjustment_messages.ForecastAdjustment()
            pb_resp = forecast_adjustment_messages.ForecastAdjustment.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_forecast_adjustment(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_forecast_adjustment_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        forecast_adjustment_messages.ForecastAdjustment.to_json(
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
                    "Received response for google.ads.admanager_v1.ForecastAdjustmentServiceClient.update_forecast_adjustment",
                    extra={
                        "serviceName": "google.ads.admanager.v1.ForecastAdjustmentService",
                        "rpcName": "UpdateForecastAdjustment",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def batch_activate_forecast_adjustments(
        self,
    ) -> Callable[
        [forecast_adjustment_service.BatchActivateForecastAdjustmentsRequest],
        forecast_adjustment_service.BatchActivateForecastAdjustmentsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchActivateForecastAdjustments(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def batch_create_forecast_adjustments(
        self,
    ) -> Callable[
        [forecast_adjustment_service.BatchCreateForecastAdjustmentsRequest],
        forecast_adjustment_service.BatchCreateForecastAdjustmentsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchCreateForecastAdjustments(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def batch_deactivate_forecast_adjustments(
        self,
    ) -> Callable[
        [forecast_adjustment_service.BatchDeactivateForecastAdjustmentsRequest],
        forecast_adjustment_service.BatchDeactivateForecastAdjustmentsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchDeactivateForecastAdjustments(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def batch_update_forecast_adjustments(
        self,
    ) -> Callable[
        [forecast_adjustment_service.BatchUpdateForecastAdjustmentsRequest],
        forecast_adjustment_service.BatchUpdateForecastAdjustmentsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchUpdateForecastAdjustments(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def calculate_daily_ad_opportunity_counts(
        self,
    ) -> Callable[
        [forecast_adjustment_service.CalculateDailyAdOpportunityCountsRequest],
        forecast_adjustment_service.CalculateDailyAdOpportunityCountsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CalculateDailyAdOpportunityCounts(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def create_forecast_adjustment(
        self,
    ) -> Callable[
        [forecast_adjustment_service.CreateForecastAdjustmentRequest],
        forecast_adjustment_messages.ForecastAdjustment,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateForecastAdjustment(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def get_forecast_adjustment(
        self,
    ) -> Callable[
        [forecast_adjustment_service.GetForecastAdjustmentRequest],
        forecast_adjustment_messages.ForecastAdjustment,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetForecastAdjustment(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_forecast_adjustments(
        self,
    ) -> Callable[
        [forecast_adjustment_service.ListForecastAdjustmentsRequest],
        forecast_adjustment_service.ListForecastAdjustmentsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListForecastAdjustments(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def update_forecast_adjustment(
        self,
    ) -> Callable[
        [forecast_adjustment_service.UpdateForecastAdjustmentRequest],
        forecast_adjustment_messages.ForecastAdjustment,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateForecastAdjustment(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def cancel_operation(self):
        return self._CancelOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _CancelOperation(
        _BaseForecastAdjustmentServiceRestTransport._BaseCancelOperation,
        ForecastAdjustmentServiceRestStub,
    ):
        def __hash__(self):
            return hash("ForecastAdjustmentServiceRestTransport.CancelOperation")

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

            http_options = _BaseForecastAdjustmentServiceRestTransport._BaseCancelOperation._get_http_options()
            request, metadata = self._interceptor.pre_cancel_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseForecastAdjustmentServiceRestTransport._BaseCancelOperation,
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
                    f"Sending request for google.ads.admanager_v1.ForecastAdjustmentServiceClient.CancelOperation",
                    extra={
                        "serviceName": "google.ads.admanager.v1.ForecastAdjustmentService",
                        "rpcName": "CancelOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ForecastAdjustmentServiceRestTransport._CancelOperation._get_response(
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
        _BaseForecastAdjustmentServiceRestTransport._BaseGetOperation,
        ForecastAdjustmentServiceRestStub,
    ):
        def __hash__(self):
            return hash("ForecastAdjustmentServiceRestTransport.GetOperation")

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

            http_options = _BaseForecastAdjustmentServiceRestTransport._BaseGetOperation._get_http_options()
            request, metadata = self._interceptor.pre_get_operation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseForecastAdjustmentServiceRestTransport._BaseGetOperation,
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
                    f"Sending request for google.ads.admanager_v1.ForecastAdjustmentServiceClient.GetOperation",
                    extra={
                        "serviceName": "google.ads.admanager.v1.ForecastAdjustmentService",
                        "rpcName": "GetOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ForecastAdjustmentServiceRestTransport._GetOperation._get_response(
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
                    "Received response for google.ads.admanager_v1.ForecastAdjustmentServiceAsyncClient.GetOperation",
                    extra={
                        "serviceName": "google.ads.admanager.v1.ForecastAdjustmentService",
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


__all__ = ("ForecastAdjustmentServiceRestTransport",)
