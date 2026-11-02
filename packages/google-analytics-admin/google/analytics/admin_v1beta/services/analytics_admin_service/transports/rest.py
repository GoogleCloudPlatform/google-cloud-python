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

from google.analytics.admin_v1beta._compat import transcode_request
from google.analytics.admin_v1beta.types import analytics_admin, resources

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseAnalyticsAdminServiceRestTransport

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


class AnalyticsAdminServiceRestInterceptor:
    """Interceptor for AnalyticsAdminService.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the AnalyticsAdminServiceRestTransport.

    .. code-block:: python
        class MyCustomAnalyticsAdminServiceInterceptor(AnalyticsAdminServiceRestInterceptor):
            def pre_acknowledge_user_data_collection(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_acknowledge_user_data_collection(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_archive_custom_dimension(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_archive_custom_metric(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_create_conversion_event(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_conversion_event(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_custom_dimension(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_custom_dimension(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_custom_metric(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_custom_metric(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_data_stream(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_data_stream(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_firebase_link(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_firebase_link(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_google_ads_link(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_google_ads_link(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_key_event(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_key_event(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_measurement_protocol_secret(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_measurement_protocol_secret(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_property(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_property(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_account(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_delete_conversion_event(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_delete_data_stream(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_delete_firebase_link(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_delete_google_ads_link(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_delete_key_event(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_delete_measurement_protocol_secret(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_delete_property(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_property(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_account(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_account(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_conversion_event(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_conversion_event(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_custom_dimension(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_custom_dimension(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_custom_metric(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_custom_metric(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_data_retention_settings(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_data_retention_settings(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_data_sharing_settings(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_data_sharing_settings(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_data_stream(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_data_stream(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_key_event(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_key_event(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_measurement_protocol_secret(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_measurement_protocol_secret(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_property(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_property(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_accounts(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_accounts(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_account_summaries(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_account_summaries(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_conversion_events(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_conversion_events(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_custom_dimensions(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_custom_dimensions(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_custom_metrics(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_custom_metrics(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_data_streams(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_data_streams(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_firebase_links(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_firebase_links(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_google_ads_links(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_google_ads_links(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_key_events(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_key_events(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_measurement_protocol_secrets(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_measurement_protocol_secrets(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_properties(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_properties(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_provision_account_ticket(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_provision_account_ticket(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_run_access_report(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_run_access_report(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_search_change_history_events(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_search_change_history_events(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_account(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_account(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_conversion_event(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_conversion_event(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_custom_dimension(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_custom_dimension(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_custom_metric(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_custom_metric(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_data_retention_settings(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_data_retention_settings(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_data_stream(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_data_stream(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_google_ads_link(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_google_ads_link(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_key_event(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_key_event(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_measurement_protocol_secret(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_measurement_protocol_secret(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_property(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_property(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = AnalyticsAdminServiceRestTransport(interceptor=MyCustomAnalyticsAdminServiceInterceptor())
        client = AnalyticsAdminServiceClient(transport=transport)


    """

    def pre_acknowledge_user_data_collection(
        self,
        request: analytics_admin.AcknowledgeUserDataCollectionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        analytics_admin.AcknowledgeUserDataCollectionRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for acknowledge_user_data_collection

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AnalyticsAdminService server.
        """
        return request, metadata

    def post_acknowledge_user_data_collection(
        self, response: analytics_admin.AcknowledgeUserDataCollectionResponse
    ) -> analytics_admin.AcknowledgeUserDataCollectionResponse:
        """Post-rpc interceptor for acknowledge_user_data_collection

        DEPRECATED. Please use the `post_acknowledge_user_data_collection_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AnalyticsAdminService server but before
        it is returned to user code. This `post_acknowledge_user_data_collection` interceptor runs
        before the `post_acknowledge_user_data_collection_with_metadata` interceptor.
        """
        return response

    def post_acknowledge_user_data_collection_with_metadata(
        self,
        response: analytics_admin.AcknowledgeUserDataCollectionResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        analytics_admin.AcknowledgeUserDataCollectionResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for acknowledge_user_data_collection

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AnalyticsAdminService server but before it is returned to user code.

        We recommend only using this `post_acknowledge_user_data_collection_with_metadata`
        interceptor in new development instead of the `post_acknowledge_user_data_collection` interceptor.
        When both interceptors are used, this `post_acknowledge_user_data_collection_with_metadata` interceptor runs after the
        `post_acknowledge_user_data_collection` interceptor. The (possibly modified) response returned by
        `post_acknowledge_user_data_collection` will be passed to
        `post_acknowledge_user_data_collection_with_metadata`.
        """
        return response, metadata

    def pre_archive_custom_dimension(
        self,
        request: analytics_admin.ArchiveCustomDimensionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        analytics_admin.ArchiveCustomDimensionRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for archive_custom_dimension

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AnalyticsAdminService server.
        """
        return request, metadata

    def pre_archive_custom_metric(
        self,
        request: analytics_admin.ArchiveCustomMetricRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        analytics_admin.ArchiveCustomMetricRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for archive_custom_metric

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AnalyticsAdminService server.
        """
        return request, metadata

    def pre_create_conversion_event(
        self,
        request: analytics_admin.CreateConversionEventRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        analytics_admin.CreateConversionEventRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_conversion_event

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AnalyticsAdminService server.
        """
        return request, metadata

    def post_create_conversion_event(
        self, response: resources.ConversionEvent
    ) -> resources.ConversionEvent:
        """Post-rpc interceptor for create_conversion_event

        DEPRECATED. Please use the `post_create_conversion_event_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AnalyticsAdminService server but before
        it is returned to user code. This `post_create_conversion_event` interceptor runs
        before the `post_create_conversion_event_with_metadata` interceptor.
        """
        return response

    def post_create_conversion_event_with_metadata(
        self,
        response: resources.ConversionEvent,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[resources.ConversionEvent, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_conversion_event

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AnalyticsAdminService server but before it is returned to user code.

        We recommend only using this `post_create_conversion_event_with_metadata`
        interceptor in new development instead of the `post_create_conversion_event` interceptor.
        When both interceptors are used, this `post_create_conversion_event_with_metadata` interceptor runs after the
        `post_create_conversion_event` interceptor. The (possibly modified) response returned by
        `post_create_conversion_event` will be passed to
        `post_create_conversion_event_with_metadata`.
        """
        return response, metadata

    def pre_create_custom_dimension(
        self,
        request: analytics_admin.CreateCustomDimensionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        analytics_admin.CreateCustomDimensionRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_custom_dimension

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AnalyticsAdminService server.
        """
        return request, metadata

    def post_create_custom_dimension(
        self, response: resources.CustomDimension
    ) -> resources.CustomDimension:
        """Post-rpc interceptor for create_custom_dimension

        DEPRECATED. Please use the `post_create_custom_dimension_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AnalyticsAdminService server but before
        it is returned to user code. This `post_create_custom_dimension` interceptor runs
        before the `post_create_custom_dimension_with_metadata` interceptor.
        """
        return response

    def post_create_custom_dimension_with_metadata(
        self,
        response: resources.CustomDimension,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[resources.CustomDimension, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_custom_dimension

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AnalyticsAdminService server but before it is returned to user code.

        We recommend only using this `post_create_custom_dimension_with_metadata`
        interceptor in new development instead of the `post_create_custom_dimension` interceptor.
        When both interceptors are used, this `post_create_custom_dimension_with_metadata` interceptor runs after the
        `post_create_custom_dimension` interceptor. The (possibly modified) response returned by
        `post_create_custom_dimension` will be passed to
        `post_create_custom_dimension_with_metadata`.
        """
        return response, metadata

    def pre_create_custom_metric(
        self,
        request: analytics_admin.CreateCustomMetricRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        analytics_admin.CreateCustomMetricRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_custom_metric

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AnalyticsAdminService server.
        """
        return request, metadata

    def post_create_custom_metric(
        self, response: resources.CustomMetric
    ) -> resources.CustomMetric:
        """Post-rpc interceptor for create_custom_metric

        DEPRECATED. Please use the `post_create_custom_metric_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AnalyticsAdminService server but before
        it is returned to user code. This `post_create_custom_metric` interceptor runs
        before the `post_create_custom_metric_with_metadata` interceptor.
        """
        return response

    def post_create_custom_metric_with_metadata(
        self,
        response: resources.CustomMetric,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[resources.CustomMetric, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_custom_metric

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AnalyticsAdminService server but before it is returned to user code.

        We recommend only using this `post_create_custom_metric_with_metadata`
        interceptor in new development instead of the `post_create_custom_metric` interceptor.
        When both interceptors are used, this `post_create_custom_metric_with_metadata` interceptor runs after the
        `post_create_custom_metric` interceptor. The (possibly modified) response returned by
        `post_create_custom_metric` will be passed to
        `post_create_custom_metric_with_metadata`.
        """
        return response, metadata

    def pre_create_data_stream(
        self,
        request: analytics_admin.CreateDataStreamRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        analytics_admin.CreateDataStreamRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_data_stream

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AnalyticsAdminService server.
        """
        return request, metadata

    def post_create_data_stream(
        self, response: resources.DataStream
    ) -> resources.DataStream:
        """Post-rpc interceptor for create_data_stream

        DEPRECATED. Please use the `post_create_data_stream_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AnalyticsAdminService server but before
        it is returned to user code. This `post_create_data_stream` interceptor runs
        before the `post_create_data_stream_with_metadata` interceptor.
        """
        return response

    def post_create_data_stream_with_metadata(
        self,
        response: resources.DataStream,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[resources.DataStream, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_data_stream

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AnalyticsAdminService server but before it is returned to user code.

        We recommend only using this `post_create_data_stream_with_metadata`
        interceptor in new development instead of the `post_create_data_stream` interceptor.
        When both interceptors are used, this `post_create_data_stream_with_metadata` interceptor runs after the
        `post_create_data_stream` interceptor. The (possibly modified) response returned by
        `post_create_data_stream` will be passed to
        `post_create_data_stream_with_metadata`.
        """
        return response, metadata

    def pre_create_firebase_link(
        self,
        request: analytics_admin.CreateFirebaseLinkRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        analytics_admin.CreateFirebaseLinkRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_firebase_link

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AnalyticsAdminService server.
        """
        return request, metadata

    def post_create_firebase_link(
        self, response: resources.FirebaseLink
    ) -> resources.FirebaseLink:
        """Post-rpc interceptor for create_firebase_link

        DEPRECATED. Please use the `post_create_firebase_link_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AnalyticsAdminService server but before
        it is returned to user code. This `post_create_firebase_link` interceptor runs
        before the `post_create_firebase_link_with_metadata` interceptor.
        """
        return response

    def post_create_firebase_link_with_metadata(
        self,
        response: resources.FirebaseLink,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[resources.FirebaseLink, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_firebase_link

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AnalyticsAdminService server but before it is returned to user code.

        We recommend only using this `post_create_firebase_link_with_metadata`
        interceptor in new development instead of the `post_create_firebase_link` interceptor.
        When both interceptors are used, this `post_create_firebase_link_with_metadata` interceptor runs after the
        `post_create_firebase_link` interceptor. The (possibly modified) response returned by
        `post_create_firebase_link` will be passed to
        `post_create_firebase_link_with_metadata`.
        """
        return response, metadata

    def pre_create_google_ads_link(
        self,
        request: analytics_admin.CreateGoogleAdsLinkRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        analytics_admin.CreateGoogleAdsLinkRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_google_ads_link

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AnalyticsAdminService server.
        """
        return request, metadata

    def post_create_google_ads_link(
        self, response: resources.GoogleAdsLink
    ) -> resources.GoogleAdsLink:
        """Post-rpc interceptor for create_google_ads_link

        DEPRECATED. Please use the `post_create_google_ads_link_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AnalyticsAdminService server but before
        it is returned to user code. This `post_create_google_ads_link` interceptor runs
        before the `post_create_google_ads_link_with_metadata` interceptor.
        """
        return response

    def post_create_google_ads_link_with_metadata(
        self,
        response: resources.GoogleAdsLink,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[resources.GoogleAdsLink, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_google_ads_link

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AnalyticsAdminService server but before it is returned to user code.

        We recommend only using this `post_create_google_ads_link_with_metadata`
        interceptor in new development instead of the `post_create_google_ads_link` interceptor.
        When both interceptors are used, this `post_create_google_ads_link_with_metadata` interceptor runs after the
        `post_create_google_ads_link` interceptor. The (possibly modified) response returned by
        `post_create_google_ads_link` will be passed to
        `post_create_google_ads_link_with_metadata`.
        """
        return response, metadata

    def pre_create_key_event(
        self,
        request: analytics_admin.CreateKeyEventRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        analytics_admin.CreateKeyEventRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_key_event

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AnalyticsAdminService server.
        """
        return request, metadata

    def post_create_key_event(self, response: resources.KeyEvent) -> resources.KeyEvent:
        """Post-rpc interceptor for create_key_event

        DEPRECATED. Please use the `post_create_key_event_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AnalyticsAdminService server but before
        it is returned to user code. This `post_create_key_event` interceptor runs
        before the `post_create_key_event_with_metadata` interceptor.
        """
        return response

    def post_create_key_event_with_metadata(
        self,
        response: resources.KeyEvent,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[resources.KeyEvent, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_key_event

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AnalyticsAdminService server but before it is returned to user code.

        We recommend only using this `post_create_key_event_with_metadata`
        interceptor in new development instead of the `post_create_key_event` interceptor.
        When both interceptors are used, this `post_create_key_event_with_metadata` interceptor runs after the
        `post_create_key_event` interceptor. The (possibly modified) response returned by
        `post_create_key_event` will be passed to
        `post_create_key_event_with_metadata`.
        """
        return response, metadata

    def pre_create_measurement_protocol_secret(
        self,
        request: analytics_admin.CreateMeasurementProtocolSecretRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        analytics_admin.CreateMeasurementProtocolSecretRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_measurement_protocol_secret

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AnalyticsAdminService server.
        """
        return request, metadata

    def post_create_measurement_protocol_secret(
        self, response: resources.MeasurementProtocolSecret
    ) -> resources.MeasurementProtocolSecret:
        """Post-rpc interceptor for create_measurement_protocol_secret

        DEPRECATED. Please use the `post_create_measurement_protocol_secret_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AnalyticsAdminService server but before
        it is returned to user code. This `post_create_measurement_protocol_secret` interceptor runs
        before the `post_create_measurement_protocol_secret_with_metadata` interceptor.
        """
        return response

    def post_create_measurement_protocol_secret_with_metadata(
        self,
        response: resources.MeasurementProtocolSecret,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        resources.MeasurementProtocolSecret, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for create_measurement_protocol_secret

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AnalyticsAdminService server but before it is returned to user code.

        We recommend only using this `post_create_measurement_protocol_secret_with_metadata`
        interceptor in new development instead of the `post_create_measurement_protocol_secret` interceptor.
        When both interceptors are used, this `post_create_measurement_protocol_secret_with_metadata` interceptor runs after the
        `post_create_measurement_protocol_secret` interceptor. The (possibly modified) response returned by
        `post_create_measurement_protocol_secret` will be passed to
        `post_create_measurement_protocol_secret_with_metadata`.
        """
        return response, metadata

    def pre_create_property(
        self,
        request: analytics_admin.CreatePropertyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        analytics_admin.CreatePropertyRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_property

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AnalyticsAdminService server.
        """
        return request, metadata

    def post_create_property(self, response: resources.Property) -> resources.Property:
        """Post-rpc interceptor for create_property

        DEPRECATED. Please use the `post_create_property_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AnalyticsAdminService server but before
        it is returned to user code. This `post_create_property` interceptor runs
        before the `post_create_property_with_metadata` interceptor.
        """
        return response

    def post_create_property_with_metadata(
        self,
        response: resources.Property,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[resources.Property, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_property

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AnalyticsAdminService server but before it is returned to user code.

        We recommend only using this `post_create_property_with_metadata`
        interceptor in new development instead of the `post_create_property` interceptor.
        When both interceptors are used, this `post_create_property_with_metadata` interceptor runs after the
        `post_create_property` interceptor. The (possibly modified) response returned by
        `post_create_property` will be passed to
        `post_create_property_with_metadata`.
        """
        return response, metadata

    def pre_delete_account(
        self,
        request: analytics_admin.DeleteAccountRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        analytics_admin.DeleteAccountRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_account

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AnalyticsAdminService server.
        """
        return request, metadata

    def pre_delete_conversion_event(
        self,
        request: analytics_admin.DeleteConversionEventRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        analytics_admin.DeleteConversionEventRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_conversion_event

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AnalyticsAdminService server.
        """
        return request, metadata

    def pre_delete_data_stream(
        self,
        request: analytics_admin.DeleteDataStreamRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        analytics_admin.DeleteDataStreamRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_data_stream

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AnalyticsAdminService server.
        """
        return request, metadata

    def pre_delete_firebase_link(
        self,
        request: analytics_admin.DeleteFirebaseLinkRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        analytics_admin.DeleteFirebaseLinkRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_firebase_link

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AnalyticsAdminService server.
        """
        return request, metadata

    def pre_delete_google_ads_link(
        self,
        request: analytics_admin.DeleteGoogleAdsLinkRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        analytics_admin.DeleteGoogleAdsLinkRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_google_ads_link

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AnalyticsAdminService server.
        """
        return request, metadata

    def pre_delete_key_event(
        self,
        request: analytics_admin.DeleteKeyEventRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        analytics_admin.DeleteKeyEventRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_key_event

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AnalyticsAdminService server.
        """
        return request, metadata

    def pre_delete_measurement_protocol_secret(
        self,
        request: analytics_admin.DeleteMeasurementProtocolSecretRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        analytics_admin.DeleteMeasurementProtocolSecretRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_measurement_protocol_secret

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AnalyticsAdminService server.
        """
        return request, metadata

    def pre_delete_property(
        self,
        request: analytics_admin.DeletePropertyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        analytics_admin.DeletePropertyRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_property

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AnalyticsAdminService server.
        """
        return request, metadata

    def post_delete_property(self, response: resources.Property) -> resources.Property:
        """Post-rpc interceptor for delete_property

        DEPRECATED. Please use the `post_delete_property_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AnalyticsAdminService server but before
        it is returned to user code. This `post_delete_property` interceptor runs
        before the `post_delete_property_with_metadata` interceptor.
        """
        return response

    def post_delete_property_with_metadata(
        self,
        response: resources.Property,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[resources.Property, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_property

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AnalyticsAdminService server but before it is returned to user code.

        We recommend only using this `post_delete_property_with_metadata`
        interceptor in new development instead of the `post_delete_property` interceptor.
        When both interceptors are used, this `post_delete_property_with_metadata` interceptor runs after the
        `post_delete_property` interceptor. The (possibly modified) response returned by
        `post_delete_property` will be passed to
        `post_delete_property_with_metadata`.
        """
        return response, metadata

    def pre_get_account(
        self,
        request: analytics_admin.GetAccountRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        analytics_admin.GetAccountRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_account

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AnalyticsAdminService server.
        """
        return request, metadata

    def post_get_account(self, response: resources.Account) -> resources.Account:
        """Post-rpc interceptor for get_account

        DEPRECATED. Please use the `post_get_account_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AnalyticsAdminService server but before
        it is returned to user code. This `post_get_account` interceptor runs
        before the `post_get_account_with_metadata` interceptor.
        """
        return response

    def post_get_account_with_metadata(
        self,
        response: resources.Account,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[resources.Account, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_account

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AnalyticsAdminService server but before it is returned to user code.

        We recommend only using this `post_get_account_with_metadata`
        interceptor in new development instead of the `post_get_account` interceptor.
        When both interceptors are used, this `post_get_account_with_metadata` interceptor runs after the
        `post_get_account` interceptor. The (possibly modified) response returned by
        `post_get_account` will be passed to
        `post_get_account_with_metadata`.
        """
        return response, metadata

    def pre_get_conversion_event(
        self,
        request: analytics_admin.GetConversionEventRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        analytics_admin.GetConversionEventRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_conversion_event

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AnalyticsAdminService server.
        """
        return request, metadata

    def post_get_conversion_event(
        self, response: resources.ConversionEvent
    ) -> resources.ConversionEvent:
        """Post-rpc interceptor for get_conversion_event

        DEPRECATED. Please use the `post_get_conversion_event_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AnalyticsAdminService server but before
        it is returned to user code. This `post_get_conversion_event` interceptor runs
        before the `post_get_conversion_event_with_metadata` interceptor.
        """
        return response

    def post_get_conversion_event_with_metadata(
        self,
        response: resources.ConversionEvent,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[resources.ConversionEvent, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_conversion_event

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AnalyticsAdminService server but before it is returned to user code.

        We recommend only using this `post_get_conversion_event_with_metadata`
        interceptor in new development instead of the `post_get_conversion_event` interceptor.
        When both interceptors are used, this `post_get_conversion_event_with_metadata` interceptor runs after the
        `post_get_conversion_event` interceptor. The (possibly modified) response returned by
        `post_get_conversion_event` will be passed to
        `post_get_conversion_event_with_metadata`.
        """
        return response, metadata

    def pre_get_custom_dimension(
        self,
        request: analytics_admin.GetCustomDimensionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        analytics_admin.GetCustomDimensionRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_custom_dimension

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AnalyticsAdminService server.
        """
        return request, metadata

    def post_get_custom_dimension(
        self, response: resources.CustomDimension
    ) -> resources.CustomDimension:
        """Post-rpc interceptor for get_custom_dimension

        DEPRECATED. Please use the `post_get_custom_dimension_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AnalyticsAdminService server but before
        it is returned to user code. This `post_get_custom_dimension` interceptor runs
        before the `post_get_custom_dimension_with_metadata` interceptor.
        """
        return response

    def post_get_custom_dimension_with_metadata(
        self,
        response: resources.CustomDimension,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[resources.CustomDimension, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_custom_dimension

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AnalyticsAdminService server but before it is returned to user code.

        We recommend only using this `post_get_custom_dimension_with_metadata`
        interceptor in new development instead of the `post_get_custom_dimension` interceptor.
        When both interceptors are used, this `post_get_custom_dimension_with_metadata` interceptor runs after the
        `post_get_custom_dimension` interceptor. The (possibly modified) response returned by
        `post_get_custom_dimension` will be passed to
        `post_get_custom_dimension_with_metadata`.
        """
        return response, metadata

    def pre_get_custom_metric(
        self,
        request: analytics_admin.GetCustomMetricRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        analytics_admin.GetCustomMetricRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_custom_metric

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AnalyticsAdminService server.
        """
        return request, metadata

    def post_get_custom_metric(
        self, response: resources.CustomMetric
    ) -> resources.CustomMetric:
        """Post-rpc interceptor for get_custom_metric

        DEPRECATED. Please use the `post_get_custom_metric_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AnalyticsAdminService server but before
        it is returned to user code. This `post_get_custom_metric` interceptor runs
        before the `post_get_custom_metric_with_metadata` interceptor.
        """
        return response

    def post_get_custom_metric_with_metadata(
        self,
        response: resources.CustomMetric,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[resources.CustomMetric, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_custom_metric

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AnalyticsAdminService server but before it is returned to user code.

        We recommend only using this `post_get_custom_metric_with_metadata`
        interceptor in new development instead of the `post_get_custom_metric` interceptor.
        When both interceptors are used, this `post_get_custom_metric_with_metadata` interceptor runs after the
        `post_get_custom_metric` interceptor. The (possibly modified) response returned by
        `post_get_custom_metric` will be passed to
        `post_get_custom_metric_with_metadata`.
        """
        return response, metadata

    def pre_get_data_retention_settings(
        self,
        request: analytics_admin.GetDataRetentionSettingsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        analytics_admin.GetDataRetentionSettingsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_data_retention_settings

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AnalyticsAdminService server.
        """
        return request, metadata

    def post_get_data_retention_settings(
        self, response: resources.DataRetentionSettings
    ) -> resources.DataRetentionSettings:
        """Post-rpc interceptor for get_data_retention_settings

        DEPRECATED. Please use the `post_get_data_retention_settings_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AnalyticsAdminService server but before
        it is returned to user code. This `post_get_data_retention_settings` interceptor runs
        before the `post_get_data_retention_settings_with_metadata` interceptor.
        """
        return response

    def post_get_data_retention_settings_with_metadata(
        self,
        response: resources.DataRetentionSettings,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        resources.DataRetentionSettings, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for get_data_retention_settings

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AnalyticsAdminService server but before it is returned to user code.

        We recommend only using this `post_get_data_retention_settings_with_metadata`
        interceptor in new development instead of the `post_get_data_retention_settings` interceptor.
        When both interceptors are used, this `post_get_data_retention_settings_with_metadata` interceptor runs after the
        `post_get_data_retention_settings` interceptor. The (possibly modified) response returned by
        `post_get_data_retention_settings` will be passed to
        `post_get_data_retention_settings_with_metadata`.
        """
        return response, metadata

    def pre_get_data_sharing_settings(
        self,
        request: analytics_admin.GetDataSharingSettingsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        analytics_admin.GetDataSharingSettingsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_data_sharing_settings

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AnalyticsAdminService server.
        """
        return request, metadata

    def post_get_data_sharing_settings(
        self, response: resources.DataSharingSettings
    ) -> resources.DataSharingSettings:
        """Post-rpc interceptor for get_data_sharing_settings

        DEPRECATED. Please use the `post_get_data_sharing_settings_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AnalyticsAdminService server but before
        it is returned to user code. This `post_get_data_sharing_settings` interceptor runs
        before the `post_get_data_sharing_settings_with_metadata` interceptor.
        """
        return response

    def post_get_data_sharing_settings_with_metadata(
        self,
        response: resources.DataSharingSettings,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[resources.DataSharingSettings, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_data_sharing_settings

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AnalyticsAdminService server but before it is returned to user code.

        We recommend only using this `post_get_data_sharing_settings_with_metadata`
        interceptor in new development instead of the `post_get_data_sharing_settings` interceptor.
        When both interceptors are used, this `post_get_data_sharing_settings_with_metadata` interceptor runs after the
        `post_get_data_sharing_settings` interceptor. The (possibly modified) response returned by
        `post_get_data_sharing_settings` will be passed to
        `post_get_data_sharing_settings_with_metadata`.
        """
        return response, metadata

    def pre_get_data_stream(
        self,
        request: analytics_admin.GetDataStreamRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        analytics_admin.GetDataStreamRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_data_stream

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AnalyticsAdminService server.
        """
        return request, metadata

    def post_get_data_stream(
        self, response: resources.DataStream
    ) -> resources.DataStream:
        """Post-rpc interceptor for get_data_stream

        DEPRECATED. Please use the `post_get_data_stream_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AnalyticsAdminService server but before
        it is returned to user code. This `post_get_data_stream` interceptor runs
        before the `post_get_data_stream_with_metadata` interceptor.
        """
        return response

    def post_get_data_stream_with_metadata(
        self,
        response: resources.DataStream,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[resources.DataStream, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_data_stream

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AnalyticsAdminService server but before it is returned to user code.

        We recommend only using this `post_get_data_stream_with_metadata`
        interceptor in new development instead of the `post_get_data_stream` interceptor.
        When both interceptors are used, this `post_get_data_stream_with_metadata` interceptor runs after the
        `post_get_data_stream` interceptor. The (possibly modified) response returned by
        `post_get_data_stream` will be passed to
        `post_get_data_stream_with_metadata`.
        """
        return response, metadata

    def pre_get_key_event(
        self,
        request: analytics_admin.GetKeyEventRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        analytics_admin.GetKeyEventRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_key_event

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AnalyticsAdminService server.
        """
        return request, metadata

    def post_get_key_event(self, response: resources.KeyEvent) -> resources.KeyEvent:
        """Post-rpc interceptor for get_key_event

        DEPRECATED. Please use the `post_get_key_event_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AnalyticsAdminService server but before
        it is returned to user code. This `post_get_key_event` interceptor runs
        before the `post_get_key_event_with_metadata` interceptor.
        """
        return response

    def post_get_key_event_with_metadata(
        self,
        response: resources.KeyEvent,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[resources.KeyEvent, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_key_event

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AnalyticsAdminService server but before it is returned to user code.

        We recommend only using this `post_get_key_event_with_metadata`
        interceptor in new development instead of the `post_get_key_event` interceptor.
        When both interceptors are used, this `post_get_key_event_with_metadata` interceptor runs after the
        `post_get_key_event` interceptor. The (possibly modified) response returned by
        `post_get_key_event` will be passed to
        `post_get_key_event_with_metadata`.
        """
        return response, metadata

    def pre_get_measurement_protocol_secret(
        self,
        request: analytics_admin.GetMeasurementProtocolSecretRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        analytics_admin.GetMeasurementProtocolSecretRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_measurement_protocol_secret

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AnalyticsAdminService server.
        """
        return request, metadata

    def post_get_measurement_protocol_secret(
        self, response: resources.MeasurementProtocolSecret
    ) -> resources.MeasurementProtocolSecret:
        """Post-rpc interceptor for get_measurement_protocol_secret

        DEPRECATED. Please use the `post_get_measurement_protocol_secret_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AnalyticsAdminService server but before
        it is returned to user code. This `post_get_measurement_protocol_secret` interceptor runs
        before the `post_get_measurement_protocol_secret_with_metadata` interceptor.
        """
        return response

    def post_get_measurement_protocol_secret_with_metadata(
        self,
        response: resources.MeasurementProtocolSecret,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        resources.MeasurementProtocolSecret, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for get_measurement_protocol_secret

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AnalyticsAdminService server but before it is returned to user code.

        We recommend only using this `post_get_measurement_protocol_secret_with_metadata`
        interceptor in new development instead of the `post_get_measurement_protocol_secret` interceptor.
        When both interceptors are used, this `post_get_measurement_protocol_secret_with_metadata` interceptor runs after the
        `post_get_measurement_protocol_secret` interceptor. The (possibly modified) response returned by
        `post_get_measurement_protocol_secret` will be passed to
        `post_get_measurement_protocol_secret_with_metadata`.
        """
        return response, metadata

    def pre_get_property(
        self,
        request: analytics_admin.GetPropertyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        analytics_admin.GetPropertyRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_property

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AnalyticsAdminService server.
        """
        return request, metadata

    def post_get_property(self, response: resources.Property) -> resources.Property:
        """Post-rpc interceptor for get_property

        DEPRECATED. Please use the `post_get_property_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AnalyticsAdminService server but before
        it is returned to user code. This `post_get_property` interceptor runs
        before the `post_get_property_with_metadata` interceptor.
        """
        return response

    def post_get_property_with_metadata(
        self,
        response: resources.Property,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[resources.Property, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_property

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AnalyticsAdminService server but before it is returned to user code.

        We recommend only using this `post_get_property_with_metadata`
        interceptor in new development instead of the `post_get_property` interceptor.
        When both interceptors are used, this `post_get_property_with_metadata` interceptor runs after the
        `post_get_property` interceptor. The (possibly modified) response returned by
        `post_get_property` will be passed to
        `post_get_property_with_metadata`.
        """
        return response, metadata

    def pre_list_accounts(
        self,
        request: analytics_admin.ListAccountsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        analytics_admin.ListAccountsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_accounts

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AnalyticsAdminService server.
        """
        return request, metadata

    def post_list_accounts(
        self, response: analytics_admin.ListAccountsResponse
    ) -> analytics_admin.ListAccountsResponse:
        """Post-rpc interceptor for list_accounts

        DEPRECATED. Please use the `post_list_accounts_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AnalyticsAdminService server but before
        it is returned to user code. This `post_list_accounts` interceptor runs
        before the `post_list_accounts_with_metadata` interceptor.
        """
        return response

    def post_list_accounts_with_metadata(
        self,
        response: analytics_admin.ListAccountsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        analytics_admin.ListAccountsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_accounts

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AnalyticsAdminService server but before it is returned to user code.

        We recommend only using this `post_list_accounts_with_metadata`
        interceptor in new development instead of the `post_list_accounts` interceptor.
        When both interceptors are used, this `post_list_accounts_with_metadata` interceptor runs after the
        `post_list_accounts` interceptor. The (possibly modified) response returned by
        `post_list_accounts` will be passed to
        `post_list_accounts_with_metadata`.
        """
        return response, metadata

    def pre_list_account_summaries(
        self,
        request: analytics_admin.ListAccountSummariesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        analytics_admin.ListAccountSummariesRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_account_summaries

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AnalyticsAdminService server.
        """
        return request, metadata

    def post_list_account_summaries(
        self, response: analytics_admin.ListAccountSummariesResponse
    ) -> analytics_admin.ListAccountSummariesResponse:
        """Post-rpc interceptor for list_account_summaries

        DEPRECATED. Please use the `post_list_account_summaries_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AnalyticsAdminService server but before
        it is returned to user code. This `post_list_account_summaries` interceptor runs
        before the `post_list_account_summaries_with_metadata` interceptor.
        """
        return response

    def post_list_account_summaries_with_metadata(
        self,
        response: analytics_admin.ListAccountSummariesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        analytics_admin.ListAccountSummariesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_account_summaries

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AnalyticsAdminService server but before it is returned to user code.

        We recommend only using this `post_list_account_summaries_with_metadata`
        interceptor in new development instead of the `post_list_account_summaries` interceptor.
        When both interceptors are used, this `post_list_account_summaries_with_metadata` interceptor runs after the
        `post_list_account_summaries` interceptor. The (possibly modified) response returned by
        `post_list_account_summaries` will be passed to
        `post_list_account_summaries_with_metadata`.
        """
        return response, metadata

    def pre_list_conversion_events(
        self,
        request: analytics_admin.ListConversionEventsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        analytics_admin.ListConversionEventsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_conversion_events

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AnalyticsAdminService server.
        """
        return request, metadata

    def post_list_conversion_events(
        self, response: analytics_admin.ListConversionEventsResponse
    ) -> analytics_admin.ListConversionEventsResponse:
        """Post-rpc interceptor for list_conversion_events

        DEPRECATED. Please use the `post_list_conversion_events_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AnalyticsAdminService server but before
        it is returned to user code. This `post_list_conversion_events` interceptor runs
        before the `post_list_conversion_events_with_metadata` interceptor.
        """
        return response

    def post_list_conversion_events_with_metadata(
        self,
        response: analytics_admin.ListConversionEventsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        analytics_admin.ListConversionEventsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_conversion_events

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AnalyticsAdminService server but before it is returned to user code.

        We recommend only using this `post_list_conversion_events_with_metadata`
        interceptor in new development instead of the `post_list_conversion_events` interceptor.
        When both interceptors are used, this `post_list_conversion_events_with_metadata` interceptor runs after the
        `post_list_conversion_events` interceptor. The (possibly modified) response returned by
        `post_list_conversion_events` will be passed to
        `post_list_conversion_events_with_metadata`.
        """
        return response, metadata

    def pre_list_custom_dimensions(
        self,
        request: analytics_admin.ListCustomDimensionsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        analytics_admin.ListCustomDimensionsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_custom_dimensions

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AnalyticsAdminService server.
        """
        return request, metadata

    def post_list_custom_dimensions(
        self, response: analytics_admin.ListCustomDimensionsResponse
    ) -> analytics_admin.ListCustomDimensionsResponse:
        """Post-rpc interceptor for list_custom_dimensions

        DEPRECATED. Please use the `post_list_custom_dimensions_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AnalyticsAdminService server but before
        it is returned to user code. This `post_list_custom_dimensions` interceptor runs
        before the `post_list_custom_dimensions_with_metadata` interceptor.
        """
        return response

    def post_list_custom_dimensions_with_metadata(
        self,
        response: analytics_admin.ListCustomDimensionsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        analytics_admin.ListCustomDimensionsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_custom_dimensions

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AnalyticsAdminService server but before it is returned to user code.

        We recommend only using this `post_list_custom_dimensions_with_metadata`
        interceptor in new development instead of the `post_list_custom_dimensions` interceptor.
        When both interceptors are used, this `post_list_custom_dimensions_with_metadata` interceptor runs after the
        `post_list_custom_dimensions` interceptor. The (possibly modified) response returned by
        `post_list_custom_dimensions` will be passed to
        `post_list_custom_dimensions_with_metadata`.
        """
        return response, metadata

    def pre_list_custom_metrics(
        self,
        request: analytics_admin.ListCustomMetricsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        analytics_admin.ListCustomMetricsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_custom_metrics

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AnalyticsAdminService server.
        """
        return request, metadata

    def post_list_custom_metrics(
        self, response: analytics_admin.ListCustomMetricsResponse
    ) -> analytics_admin.ListCustomMetricsResponse:
        """Post-rpc interceptor for list_custom_metrics

        DEPRECATED. Please use the `post_list_custom_metrics_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AnalyticsAdminService server but before
        it is returned to user code. This `post_list_custom_metrics` interceptor runs
        before the `post_list_custom_metrics_with_metadata` interceptor.
        """
        return response

    def post_list_custom_metrics_with_metadata(
        self,
        response: analytics_admin.ListCustomMetricsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        analytics_admin.ListCustomMetricsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_custom_metrics

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AnalyticsAdminService server but before it is returned to user code.

        We recommend only using this `post_list_custom_metrics_with_metadata`
        interceptor in new development instead of the `post_list_custom_metrics` interceptor.
        When both interceptors are used, this `post_list_custom_metrics_with_metadata` interceptor runs after the
        `post_list_custom_metrics` interceptor. The (possibly modified) response returned by
        `post_list_custom_metrics` will be passed to
        `post_list_custom_metrics_with_metadata`.
        """
        return response, metadata

    def pre_list_data_streams(
        self,
        request: analytics_admin.ListDataStreamsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        analytics_admin.ListDataStreamsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_data_streams

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AnalyticsAdminService server.
        """
        return request, metadata

    def post_list_data_streams(
        self, response: analytics_admin.ListDataStreamsResponse
    ) -> analytics_admin.ListDataStreamsResponse:
        """Post-rpc interceptor for list_data_streams

        DEPRECATED. Please use the `post_list_data_streams_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AnalyticsAdminService server but before
        it is returned to user code. This `post_list_data_streams` interceptor runs
        before the `post_list_data_streams_with_metadata` interceptor.
        """
        return response

    def post_list_data_streams_with_metadata(
        self,
        response: analytics_admin.ListDataStreamsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        analytics_admin.ListDataStreamsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_data_streams

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AnalyticsAdminService server but before it is returned to user code.

        We recommend only using this `post_list_data_streams_with_metadata`
        interceptor in new development instead of the `post_list_data_streams` interceptor.
        When both interceptors are used, this `post_list_data_streams_with_metadata` interceptor runs after the
        `post_list_data_streams` interceptor. The (possibly modified) response returned by
        `post_list_data_streams` will be passed to
        `post_list_data_streams_with_metadata`.
        """
        return response, metadata

    def pre_list_firebase_links(
        self,
        request: analytics_admin.ListFirebaseLinksRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        analytics_admin.ListFirebaseLinksRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_firebase_links

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AnalyticsAdminService server.
        """
        return request, metadata

    def post_list_firebase_links(
        self, response: analytics_admin.ListFirebaseLinksResponse
    ) -> analytics_admin.ListFirebaseLinksResponse:
        """Post-rpc interceptor for list_firebase_links

        DEPRECATED. Please use the `post_list_firebase_links_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AnalyticsAdminService server but before
        it is returned to user code. This `post_list_firebase_links` interceptor runs
        before the `post_list_firebase_links_with_metadata` interceptor.
        """
        return response

    def post_list_firebase_links_with_metadata(
        self,
        response: analytics_admin.ListFirebaseLinksResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        analytics_admin.ListFirebaseLinksResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_firebase_links

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AnalyticsAdminService server but before it is returned to user code.

        We recommend only using this `post_list_firebase_links_with_metadata`
        interceptor in new development instead of the `post_list_firebase_links` interceptor.
        When both interceptors are used, this `post_list_firebase_links_with_metadata` interceptor runs after the
        `post_list_firebase_links` interceptor. The (possibly modified) response returned by
        `post_list_firebase_links` will be passed to
        `post_list_firebase_links_with_metadata`.
        """
        return response, metadata

    def pre_list_google_ads_links(
        self,
        request: analytics_admin.ListGoogleAdsLinksRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        analytics_admin.ListGoogleAdsLinksRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_google_ads_links

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AnalyticsAdminService server.
        """
        return request, metadata

    def post_list_google_ads_links(
        self, response: analytics_admin.ListGoogleAdsLinksResponse
    ) -> analytics_admin.ListGoogleAdsLinksResponse:
        """Post-rpc interceptor for list_google_ads_links

        DEPRECATED. Please use the `post_list_google_ads_links_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AnalyticsAdminService server but before
        it is returned to user code. This `post_list_google_ads_links` interceptor runs
        before the `post_list_google_ads_links_with_metadata` interceptor.
        """
        return response

    def post_list_google_ads_links_with_metadata(
        self,
        response: analytics_admin.ListGoogleAdsLinksResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        analytics_admin.ListGoogleAdsLinksResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_google_ads_links

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AnalyticsAdminService server but before it is returned to user code.

        We recommend only using this `post_list_google_ads_links_with_metadata`
        interceptor in new development instead of the `post_list_google_ads_links` interceptor.
        When both interceptors are used, this `post_list_google_ads_links_with_metadata` interceptor runs after the
        `post_list_google_ads_links` interceptor. The (possibly modified) response returned by
        `post_list_google_ads_links` will be passed to
        `post_list_google_ads_links_with_metadata`.
        """
        return response, metadata

    def pre_list_key_events(
        self,
        request: analytics_admin.ListKeyEventsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        analytics_admin.ListKeyEventsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_key_events

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AnalyticsAdminService server.
        """
        return request, metadata

    def post_list_key_events(
        self, response: analytics_admin.ListKeyEventsResponse
    ) -> analytics_admin.ListKeyEventsResponse:
        """Post-rpc interceptor for list_key_events

        DEPRECATED. Please use the `post_list_key_events_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AnalyticsAdminService server but before
        it is returned to user code. This `post_list_key_events` interceptor runs
        before the `post_list_key_events_with_metadata` interceptor.
        """
        return response

    def post_list_key_events_with_metadata(
        self,
        response: analytics_admin.ListKeyEventsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        analytics_admin.ListKeyEventsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_key_events

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AnalyticsAdminService server but before it is returned to user code.

        We recommend only using this `post_list_key_events_with_metadata`
        interceptor in new development instead of the `post_list_key_events` interceptor.
        When both interceptors are used, this `post_list_key_events_with_metadata` interceptor runs after the
        `post_list_key_events` interceptor. The (possibly modified) response returned by
        `post_list_key_events` will be passed to
        `post_list_key_events_with_metadata`.
        """
        return response, metadata

    def pre_list_measurement_protocol_secrets(
        self,
        request: analytics_admin.ListMeasurementProtocolSecretsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        analytics_admin.ListMeasurementProtocolSecretsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_measurement_protocol_secrets

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AnalyticsAdminService server.
        """
        return request, metadata

    def post_list_measurement_protocol_secrets(
        self, response: analytics_admin.ListMeasurementProtocolSecretsResponse
    ) -> analytics_admin.ListMeasurementProtocolSecretsResponse:
        """Post-rpc interceptor for list_measurement_protocol_secrets

        DEPRECATED. Please use the `post_list_measurement_protocol_secrets_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AnalyticsAdminService server but before
        it is returned to user code. This `post_list_measurement_protocol_secrets` interceptor runs
        before the `post_list_measurement_protocol_secrets_with_metadata` interceptor.
        """
        return response

    def post_list_measurement_protocol_secrets_with_metadata(
        self,
        response: analytics_admin.ListMeasurementProtocolSecretsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        analytics_admin.ListMeasurementProtocolSecretsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_measurement_protocol_secrets

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AnalyticsAdminService server but before it is returned to user code.

        We recommend only using this `post_list_measurement_protocol_secrets_with_metadata`
        interceptor in new development instead of the `post_list_measurement_protocol_secrets` interceptor.
        When both interceptors are used, this `post_list_measurement_protocol_secrets_with_metadata` interceptor runs after the
        `post_list_measurement_protocol_secrets` interceptor. The (possibly modified) response returned by
        `post_list_measurement_protocol_secrets` will be passed to
        `post_list_measurement_protocol_secrets_with_metadata`.
        """
        return response, metadata

    def pre_list_properties(
        self,
        request: analytics_admin.ListPropertiesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        analytics_admin.ListPropertiesRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_properties

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AnalyticsAdminService server.
        """
        return request, metadata

    def post_list_properties(
        self, response: analytics_admin.ListPropertiesResponse
    ) -> analytics_admin.ListPropertiesResponse:
        """Post-rpc interceptor for list_properties

        DEPRECATED. Please use the `post_list_properties_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AnalyticsAdminService server but before
        it is returned to user code. This `post_list_properties` interceptor runs
        before the `post_list_properties_with_metadata` interceptor.
        """
        return response

    def post_list_properties_with_metadata(
        self,
        response: analytics_admin.ListPropertiesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        analytics_admin.ListPropertiesResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_properties

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AnalyticsAdminService server but before it is returned to user code.

        We recommend only using this `post_list_properties_with_metadata`
        interceptor in new development instead of the `post_list_properties` interceptor.
        When both interceptors are used, this `post_list_properties_with_metadata` interceptor runs after the
        `post_list_properties` interceptor. The (possibly modified) response returned by
        `post_list_properties` will be passed to
        `post_list_properties_with_metadata`.
        """
        return response, metadata

    def pre_provision_account_ticket(
        self,
        request: analytics_admin.ProvisionAccountTicketRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        analytics_admin.ProvisionAccountTicketRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for provision_account_ticket

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AnalyticsAdminService server.
        """
        return request, metadata

    def post_provision_account_ticket(
        self, response: analytics_admin.ProvisionAccountTicketResponse
    ) -> analytics_admin.ProvisionAccountTicketResponse:
        """Post-rpc interceptor for provision_account_ticket

        DEPRECATED. Please use the `post_provision_account_ticket_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AnalyticsAdminService server but before
        it is returned to user code. This `post_provision_account_ticket` interceptor runs
        before the `post_provision_account_ticket_with_metadata` interceptor.
        """
        return response

    def post_provision_account_ticket_with_metadata(
        self,
        response: analytics_admin.ProvisionAccountTicketResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        analytics_admin.ProvisionAccountTicketResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for provision_account_ticket

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AnalyticsAdminService server but before it is returned to user code.

        We recommend only using this `post_provision_account_ticket_with_metadata`
        interceptor in new development instead of the `post_provision_account_ticket` interceptor.
        When both interceptors are used, this `post_provision_account_ticket_with_metadata` interceptor runs after the
        `post_provision_account_ticket` interceptor. The (possibly modified) response returned by
        `post_provision_account_ticket` will be passed to
        `post_provision_account_ticket_with_metadata`.
        """
        return response, metadata

    def pre_run_access_report(
        self,
        request: analytics_admin.RunAccessReportRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        analytics_admin.RunAccessReportRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for run_access_report

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AnalyticsAdminService server.
        """
        return request, metadata

    def post_run_access_report(
        self, response: analytics_admin.RunAccessReportResponse
    ) -> analytics_admin.RunAccessReportResponse:
        """Post-rpc interceptor for run_access_report

        DEPRECATED. Please use the `post_run_access_report_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AnalyticsAdminService server but before
        it is returned to user code. This `post_run_access_report` interceptor runs
        before the `post_run_access_report_with_metadata` interceptor.
        """
        return response

    def post_run_access_report_with_metadata(
        self,
        response: analytics_admin.RunAccessReportResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        analytics_admin.RunAccessReportResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for run_access_report

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AnalyticsAdminService server but before it is returned to user code.

        We recommend only using this `post_run_access_report_with_metadata`
        interceptor in new development instead of the `post_run_access_report` interceptor.
        When both interceptors are used, this `post_run_access_report_with_metadata` interceptor runs after the
        `post_run_access_report` interceptor. The (possibly modified) response returned by
        `post_run_access_report` will be passed to
        `post_run_access_report_with_metadata`.
        """
        return response, metadata

    def pre_search_change_history_events(
        self,
        request: analytics_admin.SearchChangeHistoryEventsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        analytics_admin.SearchChangeHistoryEventsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for search_change_history_events

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AnalyticsAdminService server.
        """
        return request, metadata

    def post_search_change_history_events(
        self, response: analytics_admin.SearchChangeHistoryEventsResponse
    ) -> analytics_admin.SearchChangeHistoryEventsResponse:
        """Post-rpc interceptor for search_change_history_events

        DEPRECATED. Please use the `post_search_change_history_events_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AnalyticsAdminService server but before
        it is returned to user code. This `post_search_change_history_events` interceptor runs
        before the `post_search_change_history_events_with_metadata` interceptor.
        """
        return response

    def post_search_change_history_events_with_metadata(
        self,
        response: analytics_admin.SearchChangeHistoryEventsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        analytics_admin.SearchChangeHistoryEventsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for search_change_history_events

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AnalyticsAdminService server but before it is returned to user code.

        We recommend only using this `post_search_change_history_events_with_metadata`
        interceptor in new development instead of the `post_search_change_history_events` interceptor.
        When both interceptors are used, this `post_search_change_history_events_with_metadata` interceptor runs after the
        `post_search_change_history_events` interceptor. The (possibly modified) response returned by
        `post_search_change_history_events` will be passed to
        `post_search_change_history_events_with_metadata`.
        """
        return response, metadata

    def pre_update_account(
        self,
        request: analytics_admin.UpdateAccountRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        analytics_admin.UpdateAccountRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_account

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AnalyticsAdminService server.
        """
        return request, metadata

    def post_update_account(self, response: resources.Account) -> resources.Account:
        """Post-rpc interceptor for update_account

        DEPRECATED. Please use the `post_update_account_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AnalyticsAdminService server but before
        it is returned to user code. This `post_update_account` interceptor runs
        before the `post_update_account_with_metadata` interceptor.
        """
        return response

    def post_update_account_with_metadata(
        self,
        response: resources.Account,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[resources.Account, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_account

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AnalyticsAdminService server but before it is returned to user code.

        We recommend only using this `post_update_account_with_metadata`
        interceptor in new development instead of the `post_update_account` interceptor.
        When both interceptors are used, this `post_update_account_with_metadata` interceptor runs after the
        `post_update_account` interceptor. The (possibly modified) response returned by
        `post_update_account` will be passed to
        `post_update_account_with_metadata`.
        """
        return response, metadata

    def pre_update_conversion_event(
        self,
        request: analytics_admin.UpdateConversionEventRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        analytics_admin.UpdateConversionEventRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_conversion_event

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AnalyticsAdminService server.
        """
        return request, metadata

    def post_update_conversion_event(
        self, response: resources.ConversionEvent
    ) -> resources.ConversionEvent:
        """Post-rpc interceptor for update_conversion_event

        DEPRECATED. Please use the `post_update_conversion_event_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AnalyticsAdminService server but before
        it is returned to user code. This `post_update_conversion_event` interceptor runs
        before the `post_update_conversion_event_with_metadata` interceptor.
        """
        return response

    def post_update_conversion_event_with_metadata(
        self,
        response: resources.ConversionEvent,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[resources.ConversionEvent, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_conversion_event

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AnalyticsAdminService server but before it is returned to user code.

        We recommend only using this `post_update_conversion_event_with_metadata`
        interceptor in new development instead of the `post_update_conversion_event` interceptor.
        When both interceptors are used, this `post_update_conversion_event_with_metadata` interceptor runs after the
        `post_update_conversion_event` interceptor. The (possibly modified) response returned by
        `post_update_conversion_event` will be passed to
        `post_update_conversion_event_with_metadata`.
        """
        return response, metadata

    def pre_update_custom_dimension(
        self,
        request: analytics_admin.UpdateCustomDimensionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        analytics_admin.UpdateCustomDimensionRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_custom_dimension

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AnalyticsAdminService server.
        """
        return request, metadata

    def post_update_custom_dimension(
        self, response: resources.CustomDimension
    ) -> resources.CustomDimension:
        """Post-rpc interceptor for update_custom_dimension

        DEPRECATED. Please use the `post_update_custom_dimension_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AnalyticsAdminService server but before
        it is returned to user code. This `post_update_custom_dimension` interceptor runs
        before the `post_update_custom_dimension_with_metadata` interceptor.
        """
        return response

    def post_update_custom_dimension_with_metadata(
        self,
        response: resources.CustomDimension,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[resources.CustomDimension, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_custom_dimension

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AnalyticsAdminService server but before it is returned to user code.

        We recommend only using this `post_update_custom_dimension_with_metadata`
        interceptor in new development instead of the `post_update_custom_dimension` interceptor.
        When both interceptors are used, this `post_update_custom_dimension_with_metadata` interceptor runs after the
        `post_update_custom_dimension` interceptor. The (possibly modified) response returned by
        `post_update_custom_dimension` will be passed to
        `post_update_custom_dimension_with_metadata`.
        """
        return response, metadata

    def pre_update_custom_metric(
        self,
        request: analytics_admin.UpdateCustomMetricRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        analytics_admin.UpdateCustomMetricRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_custom_metric

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AnalyticsAdminService server.
        """
        return request, metadata

    def post_update_custom_metric(
        self, response: resources.CustomMetric
    ) -> resources.CustomMetric:
        """Post-rpc interceptor for update_custom_metric

        DEPRECATED. Please use the `post_update_custom_metric_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AnalyticsAdminService server but before
        it is returned to user code. This `post_update_custom_metric` interceptor runs
        before the `post_update_custom_metric_with_metadata` interceptor.
        """
        return response

    def post_update_custom_metric_with_metadata(
        self,
        response: resources.CustomMetric,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[resources.CustomMetric, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_custom_metric

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AnalyticsAdminService server but before it is returned to user code.

        We recommend only using this `post_update_custom_metric_with_metadata`
        interceptor in new development instead of the `post_update_custom_metric` interceptor.
        When both interceptors are used, this `post_update_custom_metric_with_metadata` interceptor runs after the
        `post_update_custom_metric` interceptor. The (possibly modified) response returned by
        `post_update_custom_metric` will be passed to
        `post_update_custom_metric_with_metadata`.
        """
        return response, metadata

    def pre_update_data_retention_settings(
        self,
        request: analytics_admin.UpdateDataRetentionSettingsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        analytics_admin.UpdateDataRetentionSettingsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_data_retention_settings

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AnalyticsAdminService server.
        """
        return request, metadata

    def post_update_data_retention_settings(
        self, response: resources.DataRetentionSettings
    ) -> resources.DataRetentionSettings:
        """Post-rpc interceptor for update_data_retention_settings

        DEPRECATED. Please use the `post_update_data_retention_settings_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AnalyticsAdminService server but before
        it is returned to user code. This `post_update_data_retention_settings` interceptor runs
        before the `post_update_data_retention_settings_with_metadata` interceptor.
        """
        return response

    def post_update_data_retention_settings_with_metadata(
        self,
        response: resources.DataRetentionSettings,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        resources.DataRetentionSettings, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for update_data_retention_settings

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AnalyticsAdminService server but before it is returned to user code.

        We recommend only using this `post_update_data_retention_settings_with_metadata`
        interceptor in new development instead of the `post_update_data_retention_settings` interceptor.
        When both interceptors are used, this `post_update_data_retention_settings_with_metadata` interceptor runs after the
        `post_update_data_retention_settings` interceptor. The (possibly modified) response returned by
        `post_update_data_retention_settings` will be passed to
        `post_update_data_retention_settings_with_metadata`.
        """
        return response, metadata

    def pre_update_data_stream(
        self,
        request: analytics_admin.UpdateDataStreamRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        analytics_admin.UpdateDataStreamRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_data_stream

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AnalyticsAdminService server.
        """
        return request, metadata

    def post_update_data_stream(
        self, response: resources.DataStream
    ) -> resources.DataStream:
        """Post-rpc interceptor for update_data_stream

        DEPRECATED. Please use the `post_update_data_stream_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AnalyticsAdminService server but before
        it is returned to user code. This `post_update_data_stream` interceptor runs
        before the `post_update_data_stream_with_metadata` interceptor.
        """
        return response

    def post_update_data_stream_with_metadata(
        self,
        response: resources.DataStream,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[resources.DataStream, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_data_stream

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AnalyticsAdminService server but before it is returned to user code.

        We recommend only using this `post_update_data_stream_with_metadata`
        interceptor in new development instead of the `post_update_data_stream` interceptor.
        When both interceptors are used, this `post_update_data_stream_with_metadata` interceptor runs after the
        `post_update_data_stream` interceptor. The (possibly modified) response returned by
        `post_update_data_stream` will be passed to
        `post_update_data_stream_with_metadata`.
        """
        return response, metadata

    def pre_update_google_ads_link(
        self,
        request: analytics_admin.UpdateGoogleAdsLinkRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        analytics_admin.UpdateGoogleAdsLinkRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_google_ads_link

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AnalyticsAdminService server.
        """
        return request, metadata

    def post_update_google_ads_link(
        self, response: resources.GoogleAdsLink
    ) -> resources.GoogleAdsLink:
        """Post-rpc interceptor for update_google_ads_link

        DEPRECATED. Please use the `post_update_google_ads_link_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AnalyticsAdminService server but before
        it is returned to user code. This `post_update_google_ads_link` interceptor runs
        before the `post_update_google_ads_link_with_metadata` interceptor.
        """
        return response

    def post_update_google_ads_link_with_metadata(
        self,
        response: resources.GoogleAdsLink,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[resources.GoogleAdsLink, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_google_ads_link

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AnalyticsAdminService server but before it is returned to user code.

        We recommend only using this `post_update_google_ads_link_with_metadata`
        interceptor in new development instead of the `post_update_google_ads_link` interceptor.
        When both interceptors are used, this `post_update_google_ads_link_with_metadata` interceptor runs after the
        `post_update_google_ads_link` interceptor. The (possibly modified) response returned by
        `post_update_google_ads_link` will be passed to
        `post_update_google_ads_link_with_metadata`.
        """
        return response, metadata

    def pre_update_key_event(
        self,
        request: analytics_admin.UpdateKeyEventRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        analytics_admin.UpdateKeyEventRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_key_event

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AnalyticsAdminService server.
        """
        return request, metadata

    def post_update_key_event(self, response: resources.KeyEvent) -> resources.KeyEvent:
        """Post-rpc interceptor for update_key_event

        DEPRECATED. Please use the `post_update_key_event_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AnalyticsAdminService server but before
        it is returned to user code. This `post_update_key_event` interceptor runs
        before the `post_update_key_event_with_metadata` interceptor.
        """
        return response

    def post_update_key_event_with_metadata(
        self,
        response: resources.KeyEvent,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[resources.KeyEvent, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_key_event

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AnalyticsAdminService server but before it is returned to user code.

        We recommend only using this `post_update_key_event_with_metadata`
        interceptor in new development instead of the `post_update_key_event` interceptor.
        When both interceptors are used, this `post_update_key_event_with_metadata` interceptor runs after the
        `post_update_key_event` interceptor. The (possibly modified) response returned by
        `post_update_key_event` will be passed to
        `post_update_key_event_with_metadata`.
        """
        return response, metadata

    def pre_update_measurement_protocol_secret(
        self,
        request: analytics_admin.UpdateMeasurementProtocolSecretRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        analytics_admin.UpdateMeasurementProtocolSecretRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_measurement_protocol_secret

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AnalyticsAdminService server.
        """
        return request, metadata

    def post_update_measurement_protocol_secret(
        self, response: resources.MeasurementProtocolSecret
    ) -> resources.MeasurementProtocolSecret:
        """Post-rpc interceptor for update_measurement_protocol_secret

        DEPRECATED. Please use the `post_update_measurement_protocol_secret_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AnalyticsAdminService server but before
        it is returned to user code. This `post_update_measurement_protocol_secret` interceptor runs
        before the `post_update_measurement_protocol_secret_with_metadata` interceptor.
        """
        return response

    def post_update_measurement_protocol_secret_with_metadata(
        self,
        response: resources.MeasurementProtocolSecret,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        resources.MeasurementProtocolSecret, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for update_measurement_protocol_secret

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AnalyticsAdminService server but before it is returned to user code.

        We recommend only using this `post_update_measurement_protocol_secret_with_metadata`
        interceptor in new development instead of the `post_update_measurement_protocol_secret` interceptor.
        When both interceptors are used, this `post_update_measurement_protocol_secret_with_metadata` interceptor runs after the
        `post_update_measurement_protocol_secret` interceptor. The (possibly modified) response returned by
        `post_update_measurement_protocol_secret` will be passed to
        `post_update_measurement_protocol_secret_with_metadata`.
        """
        return response, metadata

    def pre_update_property(
        self,
        request: analytics_admin.UpdatePropertyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        analytics_admin.UpdatePropertyRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_property

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AnalyticsAdminService server.
        """
        return request, metadata

    def post_update_property(self, response: resources.Property) -> resources.Property:
        """Post-rpc interceptor for update_property

        DEPRECATED. Please use the `post_update_property_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AnalyticsAdminService server but before
        it is returned to user code. This `post_update_property` interceptor runs
        before the `post_update_property_with_metadata` interceptor.
        """
        return response

    def post_update_property_with_metadata(
        self,
        response: resources.Property,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[resources.Property, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_property

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AnalyticsAdminService server but before it is returned to user code.

        We recommend only using this `post_update_property_with_metadata`
        interceptor in new development instead of the `post_update_property` interceptor.
        When both interceptors are used, this `post_update_property_with_metadata` interceptor runs after the
        `post_update_property` interceptor. The (possibly modified) response returned by
        `post_update_property` will be passed to
        `post_update_property_with_metadata`.
        """
        return response, metadata


@dataclasses.dataclass
class AnalyticsAdminServiceRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: AnalyticsAdminServiceRestInterceptor


class AnalyticsAdminServiceRestTransport(_BaseAnalyticsAdminServiceRestTransport):
    """REST backend synchronous transport for AnalyticsAdminService.

    Service Interface for the Google Analytics Admin API.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "analyticsadmin.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[AnalyticsAdminServiceRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'analyticsadmin.googleapis.com').
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
            interceptor (Optional[AnalyticsAdminServiceRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or AnalyticsAdminServiceRestInterceptor()
        self._prep_wrapped_messages(client_info)

    class _AcknowledgeUserDataCollection(
        _BaseAnalyticsAdminServiceRestTransport._BaseAcknowledgeUserDataCollection,
        AnalyticsAdminServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "AnalyticsAdminServiceRestTransport.AcknowledgeUserDataCollection"
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
            request: analytics_admin.AcknowledgeUserDataCollectionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> analytics_admin.AcknowledgeUserDataCollectionResponse:
            r"""Call the acknowledge user data
            collection method over HTTP.

                Args:
                    request (~.analytics_admin.AcknowledgeUserDataCollectionRequest):
                        The request object. Request message for
                    AcknowledgeUserDataCollection RPC.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.analytics_admin.AcknowledgeUserDataCollectionResponse:
                        Response message for
                    AcknowledgeUserDataCollection RPC.

            """

            http_options = _BaseAnalyticsAdminServiceRestTransport._BaseAcknowledgeUserDataCollection._get_http_options()
            request, metadata = self._interceptor.pre_acknowledge_user_data_collection(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAnalyticsAdminServiceRestTransport._BaseAcknowledgeUserDataCollection,
                    "_BaseAcknowledgeUserDataCollection__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.analytics.admin_v1beta.AnalyticsAdminServiceClient.AcknowledgeUserDataCollection",
                    extra={
                        "serviceName": "google.analytics.admin.v1beta.AnalyticsAdminService",
                        "rpcName": "AcknowledgeUserDataCollection",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AnalyticsAdminServiceRestTransport._AcknowledgeUserDataCollection._get_response(
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
            resp = analytics_admin.AcknowledgeUserDataCollectionResponse()
            pb_resp = analytics_admin.AcknowledgeUserDataCollectionResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_acknowledge_user_data_collection(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_acknowledge_user_data_collection_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        analytics_admin.AcknowledgeUserDataCollectionResponse.to_json(
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
                    "Received response for google.analytics.admin_v1beta.AnalyticsAdminServiceClient.acknowledge_user_data_collection",
                    extra={
                        "serviceName": "google.analytics.admin.v1beta.AnalyticsAdminService",
                        "rpcName": "AcknowledgeUserDataCollection",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ArchiveCustomDimension(
        _BaseAnalyticsAdminServiceRestTransport._BaseArchiveCustomDimension,
        AnalyticsAdminServiceRestStub,
    ):
        def __hash__(self):
            return hash("AnalyticsAdminServiceRestTransport.ArchiveCustomDimension")

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
            request: analytics_admin.ArchiveCustomDimensionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the archive custom dimension method over HTTP.

            Args:
                request (~.analytics_admin.ArchiveCustomDimensionRequest):
                    The request object. Request message for
                ArchiveCustomDimension RPC.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = _BaseAnalyticsAdminServiceRestTransport._BaseArchiveCustomDimension._get_http_options()
            request, metadata = self._interceptor.pre_archive_custom_dimension(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAnalyticsAdminServiceRestTransport._BaseArchiveCustomDimension,
                    "_BaseArchiveCustomDimension__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.analytics.admin_v1beta.AnalyticsAdminServiceClient.ArchiveCustomDimension",
                    extra={
                        "serviceName": "google.analytics.admin.v1beta.AnalyticsAdminService",
                        "rpcName": "ArchiveCustomDimension",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AnalyticsAdminServiceRestTransport._ArchiveCustomDimension._get_response(
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

    class _ArchiveCustomMetric(
        _BaseAnalyticsAdminServiceRestTransport._BaseArchiveCustomMetric,
        AnalyticsAdminServiceRestStub,
    ):
        def __hash__(self):
            return hash("AnalyticsAdminServiceRestTransport.ArchiveCustomMetric")

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
            request: analytics_admin.ArchiveCustomMetricRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the archive custom metric method over HTTP.

            Args:
                request (~.analytics_admin.ArchiveCustomMetricRequest):
                    The request object. Request message for
                ArchiveCustomMetric RPC.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = _BaseAnalyticsAdminServiceRestTransport._BaseArchiveCustomMetric._get_http_options()
            request, metadata = self._interceptor.pre_archive_custom_metric(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAnalyticsAdminServiceRestTransport._BaseArchiveCustomMetric,
                    "_BaseArchiveCustomMetric__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.analytics.admin_v1beta.AnalyticsAdminServiceClient.ArchiveCustomMetric",
                    extra={
                        "serviceName": "google.analytics.admin.v1beta.AnalyticsAdminService",
                        "rpcName": "ArchiveCustomMetric",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                AnalyticsAdminServiceRestTransport._ArchiveCustomMetric._get_response(
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

    class _CreateConversionEvent(
        _BaseAnalyticsAdminServiceRestTransport._BaseCreateConversionEvent,
        AnalyticsAdminServiceRestStub,
    ):
        def __hash__(self):
            return hash("AnalyticsAdminServiceRestTransport.CreateConversionEvent")

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
            request: analytics_admin.CreateConversionEventRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> resources.ConversionEvent:
            r"""Call the create conversion event method over HTTP.

            Args:
                request (~.analytics_admin.CreateConversionEventRequest):
                    The request object. Request message for
                CreateConversionEvent RPC
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.resources.ConversionEvent:
                    A conversion event in a Google
                Analytics property.

            """

            http_options = _BaseAnalyticsAdminServiceRestTransport._BaseCreateConversionEvent._get_http_options()
            request, metadata = self._interceptor.pre_create_conversion_event(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAnalyticsAdminServiceRestTransport._BaseCreateConversionEvent,
                    "_BaseCreateConversionEvent__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.analytics.admin_v1beta.AnalyticsAdminServiceClient.CreateConversionEvent",
                    extra={
                        "serviceName": "google.analytics.admin.v1beta.AnalyticsAdminService",
                        "rpcName": "CreateConversionEvent",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                AnalyticsAdminServiceRestTransport._CreateConversionEvent._get_response(
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
            resp = resources.ConversionEvent()
            pb_resp = resources.ConversionEvent.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_conversion_event(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_conversion_event_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = resources.ConversionEvent.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.analytics.admin_v1beta.AnalyticsAdminServiceClient.create_conversion_event",
                    extra={
                        "serviceName": "google.analytics.admin.v1beta.AnalyticsAdminService",
                        "rpcName": "CreateConversionEvent",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateCustomDimension(
        _BaseAnalyticsAdminServiceRestTransport._BaseCreateCustomDimension,
        AnalyticsAdminServiceRestStub,
    ):
        def __hash__(self):
            return hash("AnalyticsAdminServiceRestTransport.CreateCustomDimension")

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
            request: analytics_admin.CreateCustomDimensionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> resources.CustomDimension:
            r"""Call the create custom dimension method over HTTP.

            Args:
                request (~.analytics_admin.CreateCustomDimensionRequest):
                    The request object. Request message for
                CreateCustomDimension RPC.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.resources.CustomDimension:
                    A definition for a CustomDimension.
            """

            http_options = _BaseAnalyticsAdminServiceRestTransport._BaseCreateCustomDimension._get_http_options()
            request, metadata = self._interceptor.pre_create_custom_dimension(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAnalyticsAdminServiceRestTransport._BaseCreateCustomDimension,
                    "_BaseCreateCustomDimension__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.analytics.admin_v1beta.AnalyticsAdminServiceClient.CreateCustomDimension",
                    extra={
                        "serviceName": "google.analytics.admin.v1beta.AnalyticsAdminService",
                        "rpcName": "CreateCustomDimension",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                AnalyticsAdminServiceRestTransport._CreateCustomDimension._get_response(
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
            resp = resources.CustomDimension()
            pb_resp = resources.CustomDimension.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_custom_dimension(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_custom_dimension_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = resources.CustomDimension.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.analytics.admin_v1beta.AnalyticsAdminServiceClient.create_custom_dimension",
                    extra={
                        "serviceName": "google.analytics.admin.v1beta.AnalyticsAdminService",
                        "rpcName": "CreateCustomDimension",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateCustomMetric(
        _BaseAnalyticsAdminServiceRestTransport._BaseCreateCustomMetric,
        AnalyticsAdminServiceRestStub,
    ):
        def __hash__(self):
            return hash("AnalyticsAdminServiceRestTransport.CreateCustomMetric")

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
            request: analytics_admin.CreateCustomMetricRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> resources.CustomMetric:
            r"""Call the create custom metric method over HTTP.

            Args:
                request (~.analytics_admin.CreateCustomMetricRequest):
                    The request object. Request message for
                CreateCustomMetric RPC.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.resources.CustomMetric:
                    A definition for a custom metric.
            """

            http_options = _BaseAnalyticsAdminServiceRestTransport._BaseCreateCustomMetric._get_http_options()
            request, metadata = self._interceptor.pre_create_custom_metric(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAnalyticsAdminServiceRestTransport._BaseCreateCustomMetric,
                    "_BaseCreateCustomMetric__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.analytics.admin_v1beta.AnalyticsAdminServiceClient.CreateCustomMetric",
                    extra={
                        "serviceName": "google.analytics.admin.v1beta.AnalyticsAdminService",
                        "rpcName": "CreateCustomMetric",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                AnalyticsAdminServiceRestTransport._CreateCustomMetric._get_response(
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
            resp = resources.CustomMetric()
            pb_resp = resources.CustomMetric.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_custom_metric(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_custom_metric_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = resources.CustomMetric.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.analytics.admin_v1beta.AnalyticsAdminServiceClient.create_custom_metric",
                    extra={
                        "serviceName": "google.analytics.admin.v1beta.AnalyticsAdminService",
                        "rpcName": "CreateCustomMetric",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateDataStream(
        _BaseAnalyticsAdminServiceRestTransport._BaseCreateDataStream,
        AnalyticsAdminServiceRestStub,
    ):
        def __hash__(self):
            return hash("AnalyticsAdminServiceRestTransport.CreateDataStream")

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
            request: analytics_admin.CreateDataStreamRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> resources.DataStream:
            r"""Call the create data stream method over HTTP.

            Args:
                request (~.analytics_admin.CreateDataStreamRequest):
                    The request object. Request message for CreateDataStream
                RPC.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.resources.DataStream:
                    A resource message representing a
                data stream.

            """

            http_options = _BaseAnalyticsAdminServiceRestTransport._BaseCreateDataStream._get_http_options()
            request, metadata = self._interceptor.pre_create_data_stream(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAnalyticsAdminServiceRestTransport._BaseCreateDataStream,
                    "_BaseCreateDataStream__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.analytics.admin_v1beta.AnalyticsAdminServiceClient.CreateDataStream",
                    extra={
                        "serviceName": "google.analytics.admin.v1beta.AnalyticsAdminService",
                        "rpcName": "CreateDataStream",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                AnalyticsAdminServiceRestTransport._CreateDataStream._get_response(
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
            resp = resources.DataStream()
            pb_resp = resources.DataStream.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_data_stream(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_data_stream_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = resources.DataStream.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.analytics.admin_v1beta.AnalyticsAdminServiceClient.create_data_stream",
                    extra={
                        "serviceName": "google.analytics.admin.v1beta.AnalyticsAdminService",
                        "rpcName": "CreateDataStream",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateFirebaseLink(
        _BaseAnalyticsAdminServiceRestTransport._BaseCreateFirebaseLink,
        AnalyticsAdminServiceRestStub,
    ):
        def __hash__(self):
            return hash("AnalyticsAdminServiceRestTransport.CreateFirebaseLink")

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
            request: analytics_admin.CreateFirebaseLinkRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> resources.FirebaseLink:
            r"""Call the create firebase link method over HTTP.

            Args:
                request (~.analytics_admin.CreateFirebaseLinkRequest):
                    The request object. Request message for
                CreateFirebaseLink RPC
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.resources.FirebaseLink:
                    A link between a Google Analytics
                property and a Firebase project.

            """

            http_options = _BaseAnalyticsAdminServiceRestTransport._BaseCreateFirebaseLink._get_http_options()
            request, metadata = self._interceptor.pre_create_firebase_link(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAnalyticsAdminServiceRestTransport._BaseCreateFirebaseLink,
                    "_BaseCreateFirebaseLink__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.analytics.admin_v1beta.AnalyticsAdminServiceClient.CreateFirebaseLink",
                    extra={
                        "serviceName": "google.analytics.admin.v1beta.AnalyticsAdminService",
                        "rpcName": "CreateFirebaseLink",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                AnalyticsAdminServiceRestTransport._CreateFirebaseLink._get_response(
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
            resp = resources.FirebaseLink()
            pb_resp = resources.FirebaseLink.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_firebase_link(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_firebase_link_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = resources.FirebaseLink.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.analytics.admin_v1beta.AnalyticsAdminServiceClient.create_firebase_link",
                    extra={
                        "serviceName": "google.analytics.admin.v1beta.AnalyticsAdminService",
                        "rpcName": "CreateFirebaseLink",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateGoogleAdsLink(
        _BaseAnalyticsAdminServiceRestTransport._BaseCreateGoogleAdsLink,
        AnalyticsAdminServiceRestStub,
    ):
        def __hash__(self):
            return hash("AnalyticsAdminServiceRestTransport.CreateGoogleAdsLink")

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
            request: analytics_admin.CreateGoogleAdsLinkRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> resources.GoogleAdsLink:
            r"""Call the create google ads link method over HTTP.

            Args:
                request (~.analytics_admin.CreateGoogleAdsLinkRequest):
                    The request object. Request message for
                CreateGoogleAdsLink RPC
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.resources.GoogleAdsLink:
                    A link between a Google Analytics
                property and a Google Ads account.

            """

            http_options = _BaseAnalyticsAdminServiceRestTransport._BaseCreateGoogleAdsLink._get_http_options()
            request, metadata = self._interceptor.pre_create_google_ads_link(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAnalyticsAdminServiceRestTransport._BaseCreateGoogleAdsLink,
                    "_BaseCreateGoogleAdsLink__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.analytics.admin_v1beta.AnalyticsAdminServiceClient.CreateGoogleAdsLink",
                    extra={
                        "serviceName": "google.analytics.admin.v1beta.AnalyticsAdminService",
                        "rpcName": "CreateGoogleAdsLink",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                AnalyticsAdminServiceRestTransport._CreateGoogleAdsLink._get_response(
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
            resp = resources.GoogleAdsLink()
            pb_resp = resources.GoogleAdsLink.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_google_ads_link(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_google_ads_link_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = resources.GoogleAdsLink.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.analytics.admin_v1beta.AnalyticsAdminServiceClient.create_google_ads_link",
                    extra={
                        "serviceName": "google.analytics.admin.v1beta.AnalyticsAdminService",
                        "rpcName": "CreateGoogleAdsLink",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateKeyEvent(
        _BaseAnalyticsAdminServiceRestTransport._BaseCreateKeyEvent,
        AnalyticsAdminServiceRestStub,
    ):
        def __hash__(self):
            return hash("AnalyticsAdminServiceRestTransport.CreateKeyEvent")

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
            request: analytics_admin.CreateKeyEventRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> resources.KeyEvent:
            r"""Call the create key event method over HTTP.

            Args:
                request (~.analytics_admin.CreateKeyEventRequest):
                    The request object. Request message for CreateKeyEvent
                RPC
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.resources.KeyEvent:
                    A key event in a Google Analytics
                property.

            """

            http_options = _BaseAnalyticsAdminServiceRestTransport._BaseCreateKeyEvent._get_http_options()
            request, metadata = self._interceptor.pre_create_key_event(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAnalyticsAdminServiceRestTransport._BaseCreateKeyEvent,
                    "_BaseCreateKeyEvent__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.analytics.admin_v1beta.AnalyticsAdminServiceClient.CreateKeyEvent",
                    extra={
                        "serviceName": "google.analytics.admin.v1beta.AnalyticsAdminService",
                        "rpcName": "CreateKeyEvent",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AnalyticsAdminServiceRestTransport._CreateKeyEvent._get_response(
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
            resp = resources.KeyEvent()
            pb_resp = resources.KeyEvent.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_key_event(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_key_event_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = resources.KeyEvent.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.analytics.admin_v1beta.AnalyticsAdminServiceClient.create_key_event",
                    extra={
                        "serviceName": "google.analytics.admin.v1beta.AnalyticsAdminService",
                        "rpcName": "CreateKeyEvent",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateMeasurementProtocolSecret(
        _BaseAnalyticsAdminServiceRestTransport._BaseCreateMeasurementProtocolSecret,
        AnalyticsAdminServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "AnalyticsAdminServiceRestTransport.CreateMeasurementProtocolSecret"
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
            request: analytics_admin.CreateMeasurementProtocolSecretRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> resources.MeasurementProtocolSecret:
            r"""Call the create measurement
            protocol secret method over HTTP.

                Args:
                    request (~.analytics_admin.CreateMeasurementProtocolSecretRequest):
                        The request object. Request message for
                    CreateMeasurementProtocolSecret RPC
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.resources.MeasurementProtocolSecret:
                        A secret value used for sending hits
                    to Measurement Protocol.

            """

            http_options = _BaseAnalyticsAdminServiceRestTransport._BaseCreateMeasurementProtocolSecret._get_http_options()
            request, metadata = (
                self._interceptor.pre_create_measurement_protocol_secret(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAnalyticsAdminServiceRestTransport._BaseCreateMeasurementProtocolSecret,
                    "_BaseCreateMeasurementProtocolSecret__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.analytics.admin_v1beta.AnalyticsAdminServiceClient.CreateMeasurementProtocolSecret",
                    extra={
                        "serviceName": "google.analytics.admin.v1beta.AnalyticsAdminService",
                        "rpcName": "CreateMeasurementProtocolSecret",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AnalyticsAdminServiceRestTransport._CreateMeasurementProtocolSecret._get_response(
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
            resp = resources.MeasurementProtocolSecret()
            pb_resp = resources.MeasurementProtocolSecret.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_measurement_protocol_secret(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_create_measurement_protocol_secret_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = resources.MeasurementProtocolSecret.to_json(
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
                    "Received response for google.analytics.admin_v1beta.AnalyticsAdminServiceClient.create_measurement_protocol_secret",
                    extra={
                        "serviceName": "google.analytics.admin.v1beta.AnalyticsAdminService",
                        "rpcName": "CreateMeasurementProtocolSecret",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateProperty(
        _BaseAnalyticsAdminServiceRestTransport._BaseCreateProperty,
        AnalyticsAdminServiceRestStub,
    ):
        def __hash__(self):
            return hash("AnalyticsAdminServiceRestTransport.CreateProperty")

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
            request: analytics_admin.CreatePropertyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> resources.Property:
            r"""Call the create property method over HTTP.

            Args:
                request (~.analytics_admin.CreatePropertyRequest):
                    The request object. Request message for CreateProperty
                RPC.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.resources.Property:
                    A resource message representing a
                Google Analytics property.

            """

            http_options = _BaseAnalyticsAdminServiceRestTransport._BaseCreateProperty._get_http_options()
            request, metadata = self._interceptor.pre_create_property(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAnalyticsAdminServiceRestTransport._BaseCreateProperty,
                    "_BaseCreateProperty__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.analytics.admin_v1beta.AnalyticsAdminServiceClient.CreateProperty",
                    extra={
                        "serviceName": "google.analytics.admin.v1beta.AnalyticsAdminService",
                        "rpcName": "CreateProperty",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AnalyticsAdminServiceRestTransport._CreateProperty._get_response(
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
            resp = resources.Property()
            pb_resp = resources.Property.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_property(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_property_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = resources.Property.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.analytics.admin_v1beta.AnalyticsAdminServiceClient.create_property",
                    extra={
                        "serviceName": "google.analytics.admin.v1beta.AnalyticsAdminService",
                        "rpcName": "CreateProperty",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteAccount(
        _BaseAnalyticsAdminServiceRestTransport._BaseDeleteAccount,
        AnalyticsAdminServiceRestStub,
    ):
        def __hash__(self):
            return hash("AnalyticsAdminServiceRestTransport.DeleteAccount")

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
            request: analytics_admin.DeleteAccountRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete account method over HTTP.

            Args:
                request (~.analytics_admin.DeleteAccountRequest):
                    The request object. Request message for DeleteAccount
                RPC.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = _BaseAnalyticsAdminServiceRestTransport._BaseDeleteAccount._get_http_options()
            request, metadata = self._interceptor.pre_delete_account(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAnalyticsAdminServiceRestTransport._BaseDeleteAccount,
                    "_BaseDeleteAccount__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.analytics.admin_v1beta.AnalyticsAdminServiceClient.DeleteAccount",
                    extra={
                        "serviceName": "google.analytics.admin.v1beta.AnalyticsAdminService",
                        "rpcName": "DeleteAccount",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AnalyticsAdminServiceRestTransport._DeleteAccount._get_response(
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

    class _DeleteConversionEvent(
        _BaseAnalyticsAdminServiceRestTransport._BaseDeleteConversionEvent,
        AnalyticsAdminServiceRestStub,
    ):
        def __hash__(self):
            return hash("AnalyticsAdminServiceRestTransport.DeleteConversionEvent")

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
            request: analytics_admin.DeleteConversionEventRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete conversion event method over HTTP.

            Args:
                request (~.analytics_admin.DeleteConversionEventRequest):
                    The request object. Request message for
                DeleteConversionEvent RPC
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = _BaseAnalyticsAdminServiceRestTransport._BaseDeleteConversionEvent._get_http_options()
            request, metadata = self._interceptor.pre_delete_conversion_event(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAnalyticsAdminServiceRestTransport._BaseDeleteConversionEvent,
                    "_BaseDeleteConversionEvent__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.analytics.admin_v1beta.AnalyticsAdminServiceClient.DeleteConversionEvent",
                    extra={
                        "serviceName": "google.analytics.admin.v1beta.AnalyticsAdminService",
                        "rpcName": "DeleteConversionEvent",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                AnalyticsAdminServiceRestTransport._DeleteConversionEvent._get_response(
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

    class _DeleteDataStream(
        _BaseAnalyticsAdminServiceRestTransport._BaseDeleteDataStream,
        AnalyticsAdminServiceRestStub,
    ):
        def __hash__(self):
            return hash("AnalyticsAdminServiceRestTransport.DeleteDataStream")

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
            request: analytics_admin.DeleteDataStreamRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete data stream method over HTTP.

            Args:
                request (~.analytics_admin.DeleteDataStreamRequest):
                    The request object. Request message for DeleteDataStream
                RPC.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = _BaseAnalyticsAdminServiceRestTransport._BaseDeleteDataStream._get_http_options()
            request, metadata = self._interceptor.pre_delete_data_stream(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAnalyticsAdminServiceRestTransport._BaseDeleteDataStream,
                    "_BaseDeleteDataStream__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.analytics.admin_v1beta.AnalyticsAdminServiceClient.DeleteDataStream",
                    extra={
                        "serviceName": "google.analytics.admin.v1beta.AnalyticsAdminService",
                        "rpcName": "DeleteDataStream",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                AnalyticsAdminServiceRestTransport._DeleteDataStream._get_response(
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

    class _DeleteFirebaseLink(
        _BaseAnalyticsAdminServiceRestTransport._BaseDeleteFirebaseLink,
        AnalyticsAdminServiceRestStub,
    ):
        def __hash__(self):
            return hash("AnalyticsAdminServiceRestTransport.DeleteFirebaseLink")

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
            request: analytics_admin.DeleteFirebaseLinkRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete firebase link method over HTTP.

            Args:
                request (~.analytics_admin.DeleteFirebaseLinkRequest):
                    The request object. Request message for
                DeleteFirebaseLink RPC
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = _BaseAnalyticsAdminServiceRestTransport._BaseDeleteFirebaseLink._get_http_options()
            request, metadata = self._interceptor.pre_delete_firebase_link(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAnalyticsAdminServiceRestTransport._BaseDeleteFirebaseLink,
                    "_BaseDeleteFirebaseLink__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.analytics.admin_v1beta.AnalyticsAdminServiceClient.DeleteFirebaseLink",
                    extra={
                        "serviceName": "google.analytics.admin.v1beta.AnalyticsAdminService",
                        "rpcName": "DeleteFirebaseLink",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                AnalyticsAdminServiceRestTransport._DeleteFirebaseLink._get_response(
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

    class _DeleteGoogleAdsLink(
        _BaseAnalyticsAdminServiceRestTransport._BaseDeleteGoogleAdsLink,
        AnalyticsAdminServiceRestStub,
    ):
        def __hash__(self):
            return hash("AnalyticsAdminServiceRestTransport.DeleteGoogleAdsLink")

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
            request: analytics_admin.DeleteGoogleAdsLinkRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete google ads link method over HTTP.

            Args:
                request (~.analytics_admin.DeleteGoogleAdsLinkRequest):
                    The request object. Request message for
                DeleteGoogleAdsLink RPC.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = _BaseAnalyticsAdminServiceRestTransport._BaseDeleteGoogleAdsLink._get_http_options()
            request, metadata = self._interceptor.pre_delete_google_ads_link(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAnalyticsAdminServiceRestTransport._BaseDeleteGoogleAdsLink,
                    "_BaseDeleteGoogleAdsLink__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.analytics.admin_v1beta.AnalyticsAdminServiceClient.DeleteGoogleAdsLink",
                    extra={
                        "serviceName": "google.analytics.admin.v1beta.AnalyticsAdminService",
                        "rpcName": "DeleteGoogleAdsLink",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                AnalyticsAdminServiceRestTransport._DeleteGoogleAdsLink._get_response(
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

    class _DeleteKeyEvent(
        _BaseAnalyticsAdminServiceRestTransport._BaseDeleteKeyEvent,
        AnalyticsAdminServiceRestStub,
    ):
        def __hash__(self):
            return hash("AnalyticsAdminServiceRestTransport.DeleteKeyEvent")

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
            request: analytics_admin.DeleteKeyEventRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete key event method over HTTP.

            Args:
                request (~.analytics_admin.DeleteKeyEventRequest):
                    The request object. Request message for DeleteKeyEvent
                RPC
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = _BaseAnalyticsAdminServiceRestTransport._BaseDeleteKeyEvent._get_http_options()
            request, metadata = self._interceptor.pre_delete_key_event(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAnalyticsAdminServiceRestTransport._BaseDeleteKeyEvent,
                    "_BaseDeleteKeyEvent__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.analytics.admin_v1beta.AnalyticsAdminServiceClient.DeleteKeyEvent",
                    extra={
                        "serviceName": "google.analytics.admin.v1beta.AnalyticsAdminService",
                        "rpcName": "DeleteKeyEvent",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AnalyticsAdminServiceRestTransport._DeleteKeyEvent._get_response(
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

    class _DeleteMeasurementProtocolSecret(
        _BaseAnalyticsAdminServiceRestTransport._BaseDeleteMeasurementProtocolSecret,
        AnalyticsAdminServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "AnalyticsAdminServiceRestTransport.DeleteMeasurementProtocolSecret"
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
            request: analytics_admin.DeleteMeasurementProtocolSecretRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete measurement
            protocol secret method over HTTP.

                Args:
                    request (~.analytics_admin.DeleteMeasurementProtocolSecretRequest):
                        The request object. Request message for
                    DeleteMeasurementProtocolSecret RPC
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.
            """

            http_options = _BaseAnalyticsAdminServiceRestTransport._BaseDeleteMeasurementProtocolSecret._get_http_options()
            request, metadata = (
                self._interceptor.pre_delete_measurement_protocol_secret(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAnalyticsAdminServiceRestTransport._BaseDeleteMeasurementProtocolSecret,
                    "_BaseDeleteMeasurementProtocolSecret__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.analytics.admin_v1beta.AnalyticsAdminServiceClient.DeleteMeasurementProtocolSecret",
                    extra={
                        "serviceName": "google.analytics.admin.v1beta.AnalyticsAdminService",
                        "rpcName": "DeleteMeasurementProtocolSecret",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AnalyticsAdminServiceRestTransport._DeleteMeasurementProtocolSecret._get_response(
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

    class _DeleteProperty(
        _BaseAnalyticsAdminServiceRestTransport._BaseDeleteProperty,
        AnalyticsAdminServiceRestStub,
    ):
        def __hash__(self):
            return hash("AnalyticsAdminServiceRestTransport.DeleteProperty")

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
            request: analytics_admin.DeletePropertyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> resources.Property:
            r"""Call the delete property method over HTTP.

            Args:
                request (~.analytics_admin.DeletePropertyRequest):
                    The request object. Request message for DeleteProperty
                RPC.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.resources.Property:
                    A resource message representing a
                Google Analytics property.

            """

            http_options = _BaseAnalyticsAdminServiceRestTransport._BaseDeleteProperty._get_http_options()
            request, metadata = self._interceptor.pre_delete_property(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAnalyticsAdminServiceRestTransport._BaseDeleteProperty,
                    "_BaseDeleteProperty__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.analytics.admin_v1beta.AnalyticsAdminServiceClient.DeleteProperty",
                    extra={
                        "serviceName": "google.analytics.admin.v1beta.AnalyticsAdminService",
                        "rpcName": "DeleteProperty",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AnalyticsAdminServiceRestTransport._DeleteProperty._get_response(
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
            resp = resources.Property()
            pb_resp = resources.Property.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_delete_property(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_property_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = resources.Property.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.analytics.admin_v1beta.AnalyticsAdminServiceClient.delete_property",
                    extra={
                        "serviceName": "google.analytics.admin.v1beta.AnalyticsAdminService",
                        "rpcName": "DeleteProperty",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetAccount(
        _BaseAnalyticsAdminServiceRestTransport._BaseGetAccount,
        AnalyticsAdminServiceRestStub,
    ):
        def __hash__(self):
            return hash("AnalyticsAdminServiceRestTransport.GetAccount")

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
            request: analytics_admin.GetAccountRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> resources.Account:
            r"""Call the get account method over HTTP.

            Args:
                request (~.analytics_admin.GetAccountRequest):
                    The request object. Request message for GetAccount RPC.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.resources.Account:
                    A resource message representing a
                Google Analytics account.

            """

            http_options = _BaseAnalyticsAdminServiceRestTransport._BaseGetAccount._get_http_options()
            request, metadata = self._interceptor.pre_get_account(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAnalyticsAdminServiceRestTransport._BaseGetAccount,
                    "_BaseGetAccount__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.analytics.admin_v1beta.AnalyticsAdminServiceClient.GetAccount",
                    extra={
                        "serviceName": "google.analytics.admin.v1beta.AnalyticsAdminService",
                        "rpcName": "GetAccount",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AnalyticsAdminServiceRestTransport._GetAccount._get_response(
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
            resp = resources.Account()
            pb_resp = resources.Account.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_account(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_account_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = resources.Account.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.analytics.admin_v1beta.AnalyticsAdminServiceClient.get_account",
                    extra={
                        "serviceName": "google.analytics.admin.v1beta.AnalyticsAdminService",
                        "rpcName": "GetAccount",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetConversionEvent(
        _BaseAnalyticsAdminServiceRestTransport._BaseGetConversionEvent,
        AnalyticsAdminServiceRestStub,
    ):
        def __hash__(self):
            return hash("AnalyticsAdminServiceRestTransport.GetConversionEvent")

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
            request: analytics_admin.GetConversionEventRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> resources.ConversionEvent:
            r"""Call the get conversion event method over HTTP.

            Args:
                request (~.analytics_admin.GetConversionEventRequest):
                    The request object. Request message for
                GetConversionEvent RPC
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.resources.ConversionEvent:
                    A conversion event in a Google
                Analytics property.

            """

            http_options = _BaseAnalyticsAdminServiceRestTransport._BaseGetConversionEvent._get_http_options()
            request, metadata = self._interceptor.pre_get_conversion_event(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAnalyticsAdminServiceRestTransport._BaseGetConversionEvent,
                    "_BaseGetConversionEvent__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.analytics.admin_v1beta.AnalyticsAdminServiceClient.GetConversionEvent",
                    extra={
                        "serviceName": "google.analytics.admin.v1beta.AnalyticsAdminService",
                        "rpcName": "GetConversionEvent",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                AnalyticsAdminServiceRestTransport._GetConversionEvent._get_response(
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
            resp = resources.ConversionEvent()
            pb_resp = resources.ConversionEvent.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_conversion_event(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_conversion_event_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = resources.ConversionEvent.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.analytics.admin_v1beta.AnalyticsAdminServiceClient.get_conversion_event",
                    extra={
                        "serviceName": "google.analytics.admin.v1beta.AnalyticsAdminService",
                        "rpcName": "GetConversionEvent",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetCustomDimension(
        _BaseAnalyticsAdminServiceRestTransport._BaseGetCustomDimension,
        AnalyticsAdminServiceRestStub,
    ):
        def __hash__(self):
            return hash("AnalyticsAdminServiceRestTransport.GetCustomDimension")

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
            request: analytics_admin.GetCustomDimensionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> resources.CustomDimension:
            r"""Call the get custom dimension method over HTTP.

            Args:
                request (~.analytics_admin.GetCustomDimensionRequest):
                    The request object. Request message for
                GetCustomDimension RPC.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.resources.CustomDimension:
                    A definition for a CustomDimension.
            """

            http_options = _BaseAnalyticsAdminServiceRestTransport._BaseGetCustomDimension._get_http_options()
            request, metadata = self._interceptor.pre_get_custom_dimension(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAnalyticsAdminServiceRestTransport._BaseGetCustomDimension,
                    "_BaseGetCustomDimension__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.analytics.admin_v1beta.AnalyticsAdminServiceClient.GetCustomDimension",
                    extra={
                        "serviceName": "google.analytics.admin.v1beta.AnalyticsAdminService",
                        "rpcName": "GetCustomDimension",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                AnalyticsAdminServiceRestTransport._GetCustomDimension._get_response(
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
            resp = resources.CustomDimension()
            pb_resp = resources.CustomDimension.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_custom_dimension(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_custom_dimension_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = resources.CustomDimension.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.analytics.admin_v1beta.AnalyticsAdminServiceClient.get_custom_dimension",
                    extra={
                        "serviceName": "google.analytics.admin.v1beta.AnalyticsAdminService",
                        "rpcName": "GetCustomDimension",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetCustomMetric(
        _BaseAnalyticsAdminServiceRestTransport._BaseGetCustomMetric,
        AnalyticsAdminServiceRestStub,
    ):
        def __hash__(self):
            return hash("AnalyticsAdminServiceRestTransport.GetCustomMetric")

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
            request: analytics_admin.GetCustomMetricRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> resources.CustomMetric:
            r"""Call the get custom metric method over HTTP.

            Args:
                request (~.analytics_admin.GetCustomMetricRequest):
                    The request object. Request message for GetCustomMetric
                RPC.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.resources.CustomMetric:
                    A definition for a custom metric.
            """

            http_options = _BaseAnalyticsAdminServiceRestTransport._BaseGetCustomMetric._get_http_options()
            request, metadata = self._interceptor.pre_get_custom_metric(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAnalyticsAdminServiceRestTransport._BaseGetCustomMetric,
                    "_BaseGetCustomMetric__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.analytics.admin_v1beta.AnalyticsAdminServiceClient.GetCustomMetric",
                    extra={
                        "serviceName": "google.analytics.admin.v1beta.AnalyticsAdminService",
                        "rpcName": "GetCustomMetric",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                AnalyticsAdminServiceRestTransport._GetCustomMetric._get_response(
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
            resp = resources.CustomMetric()
            pb_resp = resources.CustomMetric.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_custom_metric(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_custom_metric_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = resources.CustomMetric.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.analytics.admin_v1beta.AnalyticsAdminServiceClient.get_custom_metric",
                    extra={
                        "serviceName": "google.analytics.admin.v1beta.AnalyticsAdminService",
                        "rpcName": "GetCustomMetric",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetDataRetentionSettings(
        _BaseAnalyticsAdminServiceRestTransport._BaseGetDataRetentionSettings,
        AnalyticsAdminServiceRestStub,
    ):
        def __hash__(self):
            return hash("AnalyticsAdminServiceRestTransport.GetDataRetentionSettings")

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
            request: analytics_admin.GetDataRetentionSettingsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> resources.DataRetentionSettings:
            r"""Call the get data retention
            settings method over HTTP.

                Args:
                    request (~.analytics_admin.GetDataRetentionSettingsRequest):
                        The request object. Request message for
                    GetDataRetentionSettings RPC.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.resources.DataRetentionSettings:
                        Settings values for data retention.
                    This is a singleton resource.

            """

            http_options = _BaseAnalyticsAdminServiceRestTransport._BaseGetDataRetentionSettings._get_http_options()
            request, metadata = self._interceptor.pre_get_data_retention_settings(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAnalyticsAdminServiceRestTransport._BaseGetDataRetentionSettings,
                    "_BaseGetDataRetentionSettings__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.analytics.admin_v1beta.AnalyticsAdminServiceClient.GetDataRetentionSettings",
                    extra={
                        "serviceName": "google.analytics.admin.v1beta.AnalyticsAdminService",
                        "rpcName": "GetDataRetentionSettings",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AnalyticsAdminServiceRestTransport._GetDataRetentionSettings._get_response(
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
            resp = resources.DataRetentionSettings()
            pb_resp = resources.DataRetentionSettings.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_data_retention_settings(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_data_retention_settings_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = resources.DataRetentionSettings.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.analytics.admin_v1beta.AnalyticsAdminServiceClient.get_data_retention_settings",
                    extra={
                        "serviceName": "google.analytics.admin.v1beta.AnalyticsAdminService",
                        "rpcName": "GetDataRetentionSettings",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetDataSharingSettings(
        _BaseAnalyticsAdminServiceRestTransport._BaseGetDataSharingSettings,
        AnalyticsAdminServiceRestStub,
    ):
        def __hash__(self):
            return hash("AnalyticsAdminServiceRestTransport.GetDataSharingSettings")

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
            request: analytics_admin.GetDataSharingSettingsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> resources.DataSharingSettings:
            r"""Call the get data sharing settings method over HTTP.

            Args:
                request (~.analytics_admin.GetDataSharingSettingsRequest):
                    The request object. Request message for
                GetDataSharingSettings RPC.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.resources.DataSharingSettings:
                    A resource message representing data
                sharing settings of a Google Analytics
                account.

            """

            http_options = _BaseAnalyticsAdminServiceRestTransport._BaseGetDataSharingSettings._get_http_options()
            request, metadata = self._interceptor.pre_get_data_sharing_settings(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAnalyticsAdminServiceRestTransport._BaseGetDataSharingSettings,
                    "_BaseGetDataSharingSettings__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.analytics.admin_v1beta.AnalyticsAdminServiceClient.GetDataSharingSettings",
                    extra={
                        "serviceName": "google.analytics.admin.v1beta.AnalyticsAdminService",
                        "rpcName": "GetDataSharingSettings",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AnalyticsAdminServiceRestTransport._GetDataSharingSettings._get_response(
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
            resp = resources.DataSharingSettings()
            pb_resp = resources.DataSharingSettings.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_data_sharing_settings(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_data_sharing_settings_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = resources.DataSharingSettings.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.analytics.admin_v1beta.AnalyticsAdminServiceClient.get_data_sharing_settings",
                    extra={
                        "serviceName": "google.analytics.admin.v1beta.AnalyticsAdminService",
                        "rpcName": "GetDataSharingSettings",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetDataStream(
        _BaseAnalyticsAdminServiceRestTransport._BaseGetDataStream,
        AnalyticsAdminServiceRestStub,
    ):
        def __hash__(self):
            return hash("AnalyticsAdminServiceRestTransport.GetDataStream")

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
            request: analytics_admin.GetDataStreamRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> resources.DataStream:
            r"""Call the get data stream method over HTTP.

            Args:
                request (~.analytics_admin.GetDataStreamRequest):
                    The request object. Request message for GetDataStream
                RPC.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.resources.DataStream:
                    A resource message representing a
                data stream.

            """

            http_options = _BaseAnalyticsAdminServiceRestTransport._BaseGetDataStream._get_http_options()
            request, metadata = self._interceptor.pre_get_data_stream(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAnalyticsAdminServiceRestTransport._BaseGetDataStream,
                    "_BaseGetDataStream__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.analytics.admin_v1beta.AnalyticsAdminServiceClient.GetDataStream",
                    extra={
                        "serviceName": "google.analytics.admin.v1beta.AnalyticsAdminService",
                        "rpcName": "GetDataStream",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AnalyticsAdminServiceRestTransport._GetDataStream._get_response(
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
            resp = resources.DataStream()
            pb_resp = resources.DataStream.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_data_stream(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_data_stream_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = resources.DataStream.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.analytics.admin_v1beta.AnalyticsAdminServiceClient.get_data_stream",
                    extra={
                        "serviceName": "google.analytics.admin.v1beta.AnalyticsAdminService",
                        "rpcName": "GetDataStream",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetKeyEvent(
        _BaseAnalyticsAdminServiceRestTransport._BaseGetKeyEvent,
        AnalyticsAdminServiceRestStub,
    ):
        def __hash__(self):
            return hash("AnalyticsAdminServiceRestTransport.GetKeyEvent")

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
            request: analytics_admin.GetKeyEventRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> resources.KeyEvent:
            r"""Call the get key event method over HTTP.

            Args:
                request (~.analytics_admin.GetKeyEventRequest):
                    The request object. Request message for GetKeyEvent RPC
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.resources.KeyEvent:
                    A key event in a Google Analytics
                property.

            """

            http_options = _BaseAnalyticsAdminServiceRestTransport._BaseGetKeyEvent._get_http_options()
            request, metadata = self._interceptor.pre_get_key_event(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAnalyticsAdminServiceRestTransport._BaseGetKeyEvent,
                    "_BaseGetKeyEvent__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.analytics.admin_v1beta.AnalyticsAdminServiceClient.GetKeyEvent",
                    extra={
                        "serviceName": "google.analytics.admin.v1beta.AnalyticsAdminService",
                        "rpcName": "GetKeyEvent",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AnalyticsAdminServiceRestTransport._GetKeyEvent._get_response(
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
            resp = resources.KeyEvent()
            pb_resp = resources.KeyEvent.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_key_event(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_key_event_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = resources.KeyEvent.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.analytics.admin_v1beta.AnalyticsAdminServiceClient.get_key_event",
                    extra={
                        "serviceName": "google.analytics.admin.v1beta.AnalyticsAdminService",
                        "rpcName": "GetKeyEvent",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetMeasurementProtocolSecret(
        _BaseAnalyticsAdminServiceRestTransport._BaseGetMeasurementProtocolSecret,
        AnalyticsAdminServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "AnalyticsAdminServiceRestTransport.GetMeasurementProtocolSecret"
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
            request: analytics_admin.GetMeasurementProtocolSecretRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> resources.MeasurementProtocolSecret:
            r"""Call the get measurement protocol
            secret method over HTTP.

                Args:
                    request (~.analytics_admin.GetMeasurementProtocolSecretRequest):
                        The request object. Request message for
                    GetMeasurementProtocolSecret RPC.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.resources.MeasurementProtocolSecret:
                        A secret value used for sending hits
                    to Measurement Protocol.

            """

            http_options = _BaseAnalyticsAdminServiceRestTransport._BaseGetMeasurementProtocolSecret._get_http_options()
            request, metadata = self._interceptor.pre_get_measurement_protocol_secret(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAnalyticsAdminServiceRestTransport._BaseGetMeasurementProtocolSecret,
                    "_BaseGetMeasurementProtocolSecret__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.analytics.admin_v1beta.AnalyticsAdminServiceClient.GetMeasurementProtocolSecret",
                    extra={
                        "serviceName": "google.analytics.admin.v1beta.AnalyticsAdminService",
                        "rpcName": "GetMeasurementProtocolSecret",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AnalyticsAdminServiceRestTransport._GetMeasurementProtocolSecret._get_response(
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
            resp = resources.MeasurementProtocolSecret()
            pb_resp = resources.MeasurementProtocolSecret.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_measurement_protocol_secret(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_get_measurement_protocol_secret_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = resources.MeasurementProtocolSecret.to_json(
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
                    "Received response for google.analytics.admin_v1beta.AnalyticsAdminServiceClient.get_measurement_protocol_secret",
                    extra={
                        "serviceName": "google.analytics.admin.v1beta.AnalyticsAdminService",
                        "rpcName": "GetMeasurementProtocolSecret",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetProperty(
        _BaseAnalyticsAdminServiceRestTransport._BaseGetProperty,
        AnalyticsAdminServiceRestStub,
    ):
        def __hash__(self):
            return hash("AnalyticsAdminServiceRestTransport.GetProperty")

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
            request: analytics_admin.GetPropertyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> resources.Property:
            r"""Call the get property method over HTTP.

            Args:
                request (~.analytics_admin.GetPropertyRequest):
                    The request object. Request message for GetProperty RPC.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.resources.Property:
                    A resource message representing a
                Google Analytics property.

            """

            http_options = _BaseAnalyticsAdminServiceRestTransport._BaseGetProperty._get_http_options()
            request, metadata = self._interceptor.pre_get_property(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAnalyticsAdminServiceRestTransport._BaseGetProperty,
                    "_BaseGetProperty__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.analytics.admin_v1beta.AnalyticsAdminServiceClient.GetProperty",
                    extra={
                        "serviceName": "google.analytics.admin.v1beta.AnalyticsAdminService",
                        "rpcName": "GetProperty",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AnalyticsAdminServiceRestTransport._GetProperty._get_response(
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
            resp = resources.Property()
            pb_resp = resources.Property.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_property(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_property_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = resources.Property.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.analytics.admin_v1beta.AnalyticsAdminServiceClient.get_property",
                    extra={
                        "serviceName": "google.analytics.admin.v1beta.AnalyticsAdminService",
                        "rpcName": "GetProperty",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListAccounts(
        _BaseAnalyticsAdminServiceRestTransport._BaseListAccounts,
        AnalyticsAdminServiceRestStub,
    ):
        def __hash__(self):
            return hash("AnalyticsAdminServiceRestTransport.ListAccounts")

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
            request: analytics_admin.ListAccountsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> analytics_admin.ListAccountsResponse:
            r"""Call the list accounts method over HTTP.

            Args:
                request (~.analytics_admin.ListAccountsRequest):
                    The request object. Request message for ListAccounts RPC.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.analytics_admin.ListAccountsResponse:
                    Request message for ListAccounts RPC.
            """

            http_options = _BaseAnalyticsAdminServiceRestTransport._BaseListAccounts._get_http_options()
            request, metadata = self._interceptor.pre_list_accounts(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAnalyticsAdminServiceRestTransport._BaseListAccounts,
                    "_BaseListAccounts__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.analytics.admin_v1beta.AnalyticsAdminServiceClient.ListAccounts",
                    extra={
                        "serviceName": "google.analytics.admin.v1beta.AnalyticsAdminService",
                        "rpcName": "ListAccounts",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AnalyticsAdminServiceRestTransport._ListAccounts._get_response(
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
            resp = analytics_admin.ListAccountsResponse()
            pb_resp = analytics_admin.ListAccountsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_accounts(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_accounts_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = analytics_admin.ListAccountsResponse.to_json(
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
                    "Received response for google.analytics.admin_v1beta.AnalyticsAdminServiceClient.list_accounts",
                    extra={
                        "serviceName": "google.analytics.admin.v1beta.AnalyticsAdminService",
                        "rpcName": "ListAccounts",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListAccountSummaries(
        _BaseAnalyticsAdminServiceRestTransport._BaseListAccountSummaries,
        AnalyticsAdminServiceRestStub,
    ):
        def __hash__(self):
            return hash("AnalyticsAdminServiceRestTransport.ListAccountSummaries")

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
            request: analytics_admin.ListAccountSummariesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> analytics_admin.ListAccountSummariesResponse:
            r"""Call the list account summaries method over HTTP.

            Args:
                request (~.analytics_admin.ListAccountSummariesRequest):
                    The request object. Request message for
                ListAccountSummaries RPC.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.analytics_admin.ListAccountSummariesResponse:
                    Response message for
                ListAccountSummaries RPC.

            """

            http_options = _BaseAnalyticsAdminServiceRestTransport._BaseListAccountSummaries._get_http_options()
            request, metadata = self._interceptor.pre_list_account_summaries(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAnalyticsAdminServiceRestTransport._BaseListAccountSummaries,
                    "_BaseListAccountSummaries__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.analytics.admin_v1beta.AnalyticsAdminServiceClient.ListAccountSummaries",
                    extra={
                        "serviceName": "google.analytics.admin.v1beta.AnalyticsAdminService",
                        "rpcName": "ListAccountSummaries",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                AnalyticsAdminServiceRestTransport._ListAccountSummaries._get_response(
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
            resp = analytics_admin.ListAccountSummariesResponse()
            pb_resp = analytics_admin.ListAccountSummariesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_account_summaries(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_account_summaries_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        analytics_admin.ListAccountSummariesResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.analytics.admin_v1beta.AnalyticsAdminServiceClient.list_account_summaries",
                    extra={
                        "serviceName": "google.analytics.admin.v1beta.AnalyticsAdminService",
                        "rpcName": "ListAccountSummaries",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListConversionEvents(
        _BaseAnalyticsAdminServiceRestTransport._BaseListConversionEvents,
        AnalyticsAdminServiceRestStub,
    ):
        def __hash__(self):
            return hash("AnalyticsAdminServiceRestTransport.ListConversionEvents")

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
            request: analytics_admin.ListConversionEventsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> analytics_admin.ListConversionEventsResponse:
            r"""Call the list conversion events method over HTTP.

            Args:
                request (~.analytics_admin.ListConversionEventsRequest):
                    The request object. Request message for
                ListConversionEvents RPC
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.analytics_admin.ListConversionEventsResponse:
                    Response message for
                ListConversionEvents RPC.

            """

            http_options = _BaseAnalyticsAdminServiceRestTransport._BaseListConversionEvents._get_http_options()
            request, metadata = self._interceptor.pre_list_conversion_events(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAnalyticsAdminServiceRestTransport._BaseListConversionEvents,
                    "_BaseListConversionEvents__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.analytics.admin_v1beta.AnalyticsAdminServiceClient.ListConversionEvents",
                    extra={
                        "serviceName": "google.analytics.admin.v1beta.AnalyticsAdminService",
                        "rpcName": "ListConversionEvents",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                AnalyticsAdminServiceRestTransport._ListConversionEvents._get_response(
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
            resp = analytics_admin.ListConversionEventsResponse()
            pb_resp = analytics_admin.ListConversionEventsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_conversion_events(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_conversion_events_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        analytics_admin.ListConversionEventsResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.analytics.admin_v1beta.AnalyticsAdminServiceClient.list_conversion_events",
                    extra={
                        "serviceName": "google.analytics.admin.v1beta.AnalyticsAdminService",
                        "rpcName": "ListConversionEvents",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListCustomDimensions(
        _BaseAnalyticsAdminServiceRestTransport._BaseListCustomDimensions,
        AnalyticsAdminServiceRestStub,
    ):
        def __hash__(self):
            return hash("AnalyticsAdminServiceRestTransport.ListCustomDimensions")

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
            request: analytics_admin.ListCustomDimensionsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> analytics_admin.ListCustomDimensionsResponse:
            r"""Call the list custom dimensions method over HTTP.

            Args:
                request (~.analytics_admin.ListCustomDimensionsRequest):
                    The request object. Request message for
                ListCustomDimensions RPC.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.analytics_admin.ListCustomDimensionsResponse:
                    Response message for
                ListCustomDimensions RPC.

            """

            http_options = _BaseAnalyticsAdminServiceRestTransport._BaseListCustomDimensions._get_http_options()
            request, metadata = self._interceptor.pre_list_custom_dimensions(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAnalyticsAdminServiceRestTransport._BaseListCustomDimensions,
                    "_BaseListCustomDimensions__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.analytics.admin_v1beta.AnalyticsAdminServiceClient.ListCustomDimensions",
                    extra={
                        "serviceName": "google.analytics.admin.v1beta.AnalyticsAdminService",
                        "rpcName": "ListCustomDimensions",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                AnalyticsAdminServiceRestTransport._ListCustomDimensions._get_response(
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
            resp = analytics_admin.ListCustomDimensionsResponse()
            pb_resp = analytics_admin.ListCustomDimensionsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_custom_dimensions(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_custom_dimensions_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        analytics_admin.ListCustomDimensionsResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.analytics.admin_v1beta.AnalyticsAdminServiceClient.list_custom_dimensions",
                    extra={
                        "serviceName": "google.analytics.admin.v1beta.AnalyticsAdminService",
                        "rpcName": "ListCustomDimensions",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListCustomMetrics(
        _BaseAnalyticsAdminServiceRestTransport._BaseListCustomMetrics,
        AnalyticsAdminServiceRestStub,
    ):
        def __hash__(self):
            return hash("AnalyticsAdminServiceRestTransport.ListCustomMetrics")

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
            request: analytics_admin.ListCustomMetricsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> analytics_admin.ListCustomMetricsResponse:
            r"""Call the list custom metrics method over HTTP.

            Args:
                request (~.analytics_admin.ListCustomMetricsRequest):
                    The request object. Request message for ListCustomMetrics
                RPC.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.analytics_admin.ListCustomMetricsResponse:
                    Response message for
                ListCustomMetrics RPC.

            """

            http_options = _BaseAnalyticsAdminServiceRestTransport._BaseListCustomMetrics._get_http_options()
            request, metadata = self._interceptor.pre_list_custom_metrics(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAnalyticsAdminServiceRestTransport._BaseListCustomMetrics,
                    "_BaseListCustomMetrics__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.analytics.admin_v1beta.AnalyticsAdminServiceClient.ListCustomMetrics",
                    extra={
                        "serviceName": "google.analytics.admin.v1beta.AnalyticsAdminService",
                        "rpcName": "ListCustomMetrics",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                AnalyticsAdminServiceRestTransport._ListCustomMetrics._get_response(
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
            resp = analytics_admin.ListCustomMetricsResponse()
            pb_resp = analytics_admin.ListCustomMetricsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_custom_metrics(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_custom_metrics_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        analytics_admin.ListCustomMetricsResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.analytics.admin_v1beta.AnalyticsAdminServiceClient.list_custom_metrics",
                    extra={
                        "serviceName": "google.analytics.admin.v1beta.AnalyticsAdminService",
                        "rpcName": "ListCustomMetrics",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListDataStreams(
        _BaseAnalyticsAdminServiceRestTransport._BaseListDataStreams,
        AnalyticsAdminServiceRestStub,
    ):
        def __hash__(self):
            return hash("AnalyticsAdminServiceRestTransport.ListDataStreams")

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
            request: analytics_admin.ListDataStreamsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> analytics_admin.ListDataStreamsResponse:
            r"""Call the list data streams method over HTTP.

            Args:
                request (~.analytics_admin.ListDataStreamsRequest):
                    The request object. Request message for ListDataStreams
                RPC.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.analytics_admin.ListDataStreamsResponse:
                    Response message for ListDataStreams
                RPC.

            """

            http_options = _BaseAnalyticsAdminServiceRestTransport._BaseListDataStreams._get_http_options()
            request, metadata = self._interceptor.pre_list_data_streams(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAnalyticsAdminServiceRestTransport._BaseListDataStreams,
                    "_BaseListDataStreams__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.analytics.admin_v1beta.AnalyticsAdminServiceClient.ListDataStreams",
                    extra={
                        "serviceName": "google.analytics.admin.v1beta.AnalyticsAdminService",
                        "rpcName": "ListDataStreams",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                AnalyticsAdminServiceRestTransport._ListDataStreams._get_response(
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
            resp = analytics_admin.ListDataStreamsResponse()
            pb_resp = analytics_admin.ListDataStreamsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_data_streams(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_data_streams_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = analytics_admin.ListDataStreamsResponse.to_json(
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
                    "Received response for google.analytics.admin_v1beta.AnalyticsAdminServiceClient.list_data_streams",
                    extra={
                        "serviceName": "google.analytics.admin.v1beta.AnalyticsAdminService",
                        "rpcName": "ListDataStreams",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListFirebaseLinks(
        _BaseAnalyticsAdminServiceRestTransport._BaseListFirebaseLinks,
        AnalyticsAdminServiceRestStub,
    ):
        def __hash__(self):
            return hash("AnalyticsAdminServiceRestTransport.ListFirebaseLinks")

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
            request: analytics_admin.ListFirebaseLinksRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> analytics_admin.ListFirebaseLinksResponse:
            r"""Call the list firebase links method over HTTP.

            Args:
                request (~.analytics_admin.ListFirebaseLinksRequest):
                    The request object. Request message for ListFirebaseLinks
                RPC
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.analytics_admin.ListFirebaseLinksResponse:
                    Response message for
                ListFirebaseLinks RPC

            """

            http_options = _BaseAnalyticsAdminServiceRestTransport._BaseListFirebaseLinks._get_http_options()
            request, metadata = self._interceptor.pre_list_firebase_links(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAnalyticsAdminServiceRestTransport._BaseListFirebaseLinks,
                    "_BaseListFirebaseLinks__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.analytics.admin_v1beta.AnalyticsAdminServiceClient.ListFirebaseLinks",
                    extra={
                        "serviceName": "google.analytics.admin.v1beta.AnalyticsAdminService",
                        "rpcName": "ListFirebaseLinks",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                AnalyticsAdminServiceRestTransport._ListFirebaseLinks._get_response(
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
            resp = analytics_admin.ListFirebaseLinksResponse()
            pb_resp = analytics_admin.ListFirebaseLinksResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_firebase_links(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_firebase_links_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        analytics_admin.ListFirebaseLinksResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.analytics.admin_v1beta.AnalyticsAdminServiceClient.list_firebase_links",
                    extra={
                        "serviceName": "google.analytics.admin.v1beta.AnalyticsAdminService",
                        "rpcName": "ListFirebaseLinks",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListGoogleAdsLinks(
        _BaseAnalyticsAdminServiceRestTransport._BaseListGoogleAdsLinks,
        AnalyticsAdminServiceRestStub,
    ):
        def __hash__(self):
            return hash("AnalyticsAdminServiceRestTransport.ListGoogleAdsLinks")

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
            request: analytics_admin.ListGoogleAdsLinksRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> analytics_admin.ListGoogleAdsLinksResponse:
            r"""Call the list google ads links method over HTTP.

            Args:
                request (~.analytics_admin.ListGoogleAdsLinksRequest):
                    The request object. Request message for
                ListGoogleAdsLinks RPC.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.analytics_admin.ListGoogleAdsLinksResponse:
                    Response message for
                ListGoogleAdsLinks RPC.

            """

            http_options = _BaseAnalyticsAdminServiceRestTransport._BaseListGoogleAdsLinks._get_http_options()
            request, metadata = self._interceptor.pre_list_google_ads_links(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAnalyticsAdminServiceRestTransport._BaseListGoogleAdsLinks,
                    "_BaseListGoogleAdsLinks__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.analytics.admin_v1beta.AnalyticsAdminServiceClient.ListGoogleAdsLinks",
                    extra={
                        "serviceName": "google.analytics.admin.v1beta.AnalyticsAdminService",
                        "rpcName": "ListGoogleAdsLinks",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                AnalyticsAdminServiceRestTransport._ListGoogleAdsLinks._get_response(
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
            resp = analytics_admin.ListGoogleAdsLinksResponse()
            pb_resp = analytics_admin.ListGoogleAdsLinksResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_google_ads_links(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_google_ads_links_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        analytics_admin.ListGoogleAdsLinksResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.analytics.admin_v1beta.AnalyticsAdminServiceClient.list_google_ads_links",
                    extra={
                        "serviceName": "google.analytics.admin.v1beta.AnalyticsAdminService",
                        "rpcName": "ListGoogleAdsLinks",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListKeyEvents(
        _BaseAnalyticsAdminServiceRestTransport._BaseListKeyEvents,
        AnalyticsAdminServiceRestStub,
    ):
        def __hash__(self):
            return hash("AnalyticsAdminServiceRestTransport.ListKeyEvents")

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
            request: analytics_admin.ListKeyEventsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> analytics_admin.ListKeyEventsResponse:
            r"""Call the list key events method over HTTP.

            Args:
                request (~.analytics_admin.ListKeyEventsRequest):
                    The request object. Request message for ListKeyEvents RPC
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.analytics_admin.ListKeyEventsResponse:
                    Response message for ListKeyEvents
                RPC.

            """

            http_options = _BaseAnalyticsAdminServiceRestTransport._BaseListKeyEvents._get_http_options()
            request, metadata = self._interceptor.pre_list_key_events(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAnalyticsAdminServiceRestTransport._BaseListKeyEvents,
                    "_BaseListKeyEvents__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.analytics.admin_v1beta.AnalyticsAdminServiceClient.ListKeyEvents",
                    extra={
                        "serviceName": "google.analytics.admin.v1beta.AnalyticsAdminService",
                        "rpcName": "ListKeyEvents",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AnalyticsAdminServiceRestTransport._ListKeyEvents._get_response(
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
            resp = analytics_admin.ListKeyEventsResponse()
            pb_resp = analytics_admin.ListKeyEventsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_key_events(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_key_events_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = analytics_admin.ListKeyEventsResponse.to_json(
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
                    "Received response for google.analytics.admin_v1beta.AnalyticsAdminServiceClient.list_key_events",
                    extra={
                        "serviceName": "google.analytics.admin.v1beta.AnalyticsAdminService",
                        "rpcName": "ListKeyEvents",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListMeasurementProtocolSecrets(
        _BaseAnalyticsAdminServiceRestTransport._BaseListMeasurementProtocolSecrets,
        AnalyticsAdminServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "AnalyticsAdminServiceRestTransport.ListMeasurementProtocolSecrets"
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
            request: analytics_admin.ListMeasurementProtocolSecretsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> analytics_admin.ListMeasurementProtocolSecretsResponse:
            r"""Call the list measurement protocol
            secrets method over HTTP.

                Args:
                    request (~.analytics_admin.ListMeasurementProtocolSecretsRequest):
                        The request object. Request message for
                    ListMeasurementProtocolSecret RPC
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.analytics_admin.ListMeasurementProtocolSecretsResponse:
                        Response message for
                    ListMeasurementProtocolSecret RPC

            """

            http_options = _BaseAnalyticsAdminServiceRestTransport._BaseListMeasurementProtocolSecrets._get_http_options()
            request, metadata = self._interceptor.pre_list_measurement_protocol_secrets(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAnalyticsAdminServiceRestTransport._BaseListMeasurementProtocolSecrets,
                    "_BaseListMeasurementProtocolSecrets__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.analytics.admin_v1beta.AnalyticsAdminServiceClient.ListMeasurementProtocolSecrets",
                    extra={
                        "serviceName": "google.analytics.admin.v1beta.AnalyticsAdminService",
                        "rpcName": "ListMeasurementProtocolSecrets",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AnalyticsAdminServiceRestTransport._ListMeasurementProtocolSecrets._get_response(
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
            resp = analytics_admin.ListMeasurementProtocolSecretsResponse()
            pb_resp = analytics_admin.ListMeasurementProtocolSecretsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_measurement_protocol_secrets(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_list_measurement_protocol_secrets_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        analytics_admin.ListMeasurementProtocolSecretsResponse.to_json(
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
                    "Received response for google.analytics.admin_v1beta.AnalyticsAdminServiceClient.list_measurement_protocol_secrets",
                    extra={
                        "serviceName": "google.analytics.admin.v1beta.AnalyticsAdminService",
                        "rpcName": "ListMeasurementProtocolSecrets",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListProperties(
        _BaseAnalyticsAdminServiceRestTransport._BaseListProperties,
        AnalyticsAdminServiceRestStub,
    ):
        def __hash__(self):
            return hash("AnalyticsAdminServiceRestTransport.ListProperties")

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
            request: analytics_admin.ListPropertiesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> analytics_admin.ListPropertiesResponse:
            r"""Call the list properties method over HTTP.

            Args:
                request (~.analytics_admin.ListPropertiesRequest):
                    The request object. Request message for ListProperties
                RPC.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.analytics_admin.ListPropertiesResponse:
                    Response message for ListProperties
                RPC.

            """

            http_options = _BaseAnalyticsAdminServiceRestTransport._BaseListProperties._get_http_options()
            request, metadata = self._interceptor.pre_list_properties(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAnalyticsAdminServiceRestTransport._BaseListProperties,
                    "_BaseListProperties__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.analytics.admin_v1beta.AnalyticsAdminServiceClient.ListProperties",
                    extra={
                        "serviceName": "google.analytics.admin.v1beta.AnalyticsAdminService",
                        "rpcName": "ListProperties",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AnalyticsAdminServiceRestTransport._ListProperties._get_response(
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
            resp = analytics_admin.ListPropertiesResponse()
            pb_resp = analytics_admin.ListPropertiesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_properties(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_properties_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = analytics_admin.ListPropertiesResponse.to_json(
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
                    "Received response for google.analytics.admin_v1beta.AnalyticsAdminServiceClient.list_properties",
                    extra={
                        "serviceName": "google.analytics.admin.v1beta.AnalyticsAdminService",
                        "rpcName": "ListProperties",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ProvisionAccountTicket(
        _BaseAnalyticsAdminServiceRestTransport._BaseProvisionAccountTicket,
        AnalyticsAdminServiceRestStub,
    ):
        def __hash__(self):
            return hash("AnalyticsAdminServiceRestTransport.ProvisionAccountTicket")

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
            request: analytics_admin.ProvisionAccountTicketRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> analytics_admin.ProvisionAccountTicketResponse:
            r"""Call the provision account ticket method over HTTP.

            Args:
                request (~.analytics_admin.ProvisionAccountTicketRequest):
                    The request object. Request message for
                ProvisionAccountTicket RPC.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.analytics_admin.ProvisionAccountTicketResponse:
                    Response message for
                ProvisionAccountTicket RPC.

            """

            http_options = _BaseAnalyticsAdminServiceRestTransport._BaseProvisionAccountTicket._get_http_options()
            request, metadata = self._interceptor.pre_provision_account_ticket(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAnalyticsAdminServiceRestTransport._BaseProvisionAccountTicket,
                    "_BaseProvisionAccountTicket__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.analytics.admin_v1beta.AnalyticsAdminServiceClient.ProvisionAccountTicket",
                    extra={
                        "serviceName": "google.analytics.admin.v1beta.AnalyticsAdminService",
                        "rpcName": "ProvisionAccountTicket",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AnalyticsAdminServiceRestTransport._ProvisionAccountTicket._get_response(
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
            resp = analytics_admin.ProvisionAccountTicketResponse()
            pb_resp = analytics_admin.ProvisionAccountTicketResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_provision_account_ticket(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_provision_account_ticket_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        analytics_admin.ProvisionAccountTicketResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.analytics.admin_v1beta.AnalyticsAdminServiceClient.provision_account_ticket",
                    extra={
                        "serviceName": "google.analytics.admin.v1beta.AnalyticsAdminService",
                        "rpcName": "ProvisionAccountTicket",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _RunAccessReport(
        _BaseAnalyticsAdminServiceRestTransport._BaseRunAccessReport,
        AnalyticsAdminServiceRestStub,
    ):
        def __hash__(self):
            return hash("AnalyticsAdminServiceRestTransport.RunAccessReport")

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
            request: analytics_admin.RunAccessReportRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> analytics_admin.RunAccessReportResponse:
            r"""Call the run access report method over HTTP.

            Args:
                request (~.analytics_admin.RunAccessReportRequest):
                    The request object. The request for a Data Access Record
                Report.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.analytics_admin.RunAccessReportResponse:
                    The customized Data Access Record
                Report response.

            """

            http_options = _BaseAnalyticsAdminServiceRestTransport._BaseRunAccessReport._get_http_options()
            request, metadata = self._interceptor.pre_run_access_report(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAnalyticsAdminServiceRestTransport._BaseRunAccessReport,
                    "_BaseRunAccessReport__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.analytics.admin_v1beta.AnalyticsAdminServiceClient.RunAccessReport",
                    extra={
                        "serviceName": "google.analytics.admin.v1beta.AnalyticsAdminService",
                        "rpcName": "RunAccessReport",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                AnalyticsAdminServiceRestTransport._RunAccessReport._get_response(
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
            resp = analytics_admin.RunAccessReportResponse()
            pb_resp = analytics_admin.RunAccessReportResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_run_access_report(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_run_access_report_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = analytics_admin.RunAccessReportResponse.to_json(
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
                    "Received response for google.analytics.admin_v1beta.AnalyticsAdminServiceClient.run_access_report",
                    extra={
                        "serviceName": "google.analytics.admin.v1beta.AnalyticsAdminService",
                        "rpcName": "RunAccessReport",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _SearchChangeHistoryEvents(
        _BaseAnalyticsAdminServiceRestTransport._BaseSearchChangeHistoryEvents,
        AnalyticsAdminServiceRestStub,
    ):
        def __hash__(self):
            return hash("AnalyticsAdminServiceRestTransport.SearchChangeHistoryEvents")

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
            request: analytics_admin.SearchChangeHistoryEventsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> analytics_admin.SearchChangeHistoryEventsResponse:
            r"""Call the search change history
            events method over HTTP.

                Args:
                    request (~.analytics_admin.SearchChangeHistoryEventsRequest):
                        The request object. Request message for
                    SearchChangeHistoryEvents RPC.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.analytics_admin.SearchChangeHistoryEventsResponse:
                        Response message for SearchAccounts
                    RPC.

            """

            http_options = _BaseAnalyticsAdminServiceRestTransport._BaseSearchChangeHistoryEvents._get_http_options()
            request, metadata = self._interceptor.pre_search_change_history_events(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAnalyticsAdminServiceRestTransport._BaseSearchChangeHistoryEvents,
                    "_BaseSearchChangeHistoryEvents__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.analytics.admin_v1beta.AnalyticsAdminServiceClient.SearchChangeHistoryEvents",
                    extra={
                        "serviceName": "google.analytics.admin.v1beta.AnalyticsAdminService",
                        "rpcName": "SearchChangeHistoryEvents",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AnalyticsAdminServiceRestTransport._SearchChangeHistoryEvents._get_response(
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
            resp = analytics_admin.SearchChangeHistoryEventsResponse()
            pb_resp = analytics_admin.SearchChangeHistoryEventsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_search_change_history_events(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_search_change_history_events_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        analytics_admin.SearchChangeHistoryEventsResponse.to_json(
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
                    "Received response for google.analytics.admin_v1beta.AnalyticsAdminServiceClient.search_change_history_events",
                    extra={
                        "serviceName": "google.analytics.admin.v1beta.AnalyticsAdminService",
                        "rpcName": "SearchChangeHistoryEvents",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateAccount(
        _BaseAnalyticsAdminServiceRestTransport._BaseUpdateAccount,
        AnalyticsAdminServiceRestStub,
    ):
        def __hash__(self):
            return hash("AnalyticsAdminServiceRestTransport.UpdateAccount")

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
            request: analytics_admin.UpdateAccountRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> resources.Account:
            r"""Call the update account method over HTTP.

            Args:
                request (~.analytics_admin.UpdateAccountRequest):
                    The request object. Request message for UpdateAccount
                RPC.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.resources.Account:
                    A resource message representing a
                Google Analytics account.

            """

            http_options = _BaseAnalyticsAdminServiceRestTransport._BaseUpdateAccount._get_http_options()
            request, metadata = self._interceptor.pre_update_account(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAnalyticsAdminServiceRestTransport._BaseUpdateAccount,
                    "_BaseUpdateAccount__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.analytics.admin_v1beta.AnalyticsAdminServiceClient.UpdateAccount",
                    extra={
                        "serviceName": "google.analytics.admin.v1beta.AnalyticsAdminService",
                        "rpcName": "UpdateAccount",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AnalyticsAdminServiceRestTransport._UpdateAccount._get_response(
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
            resp = resources.Account()
            pb_resp = resources.Account.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_account(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_account_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = resources.Account.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.analytics.admin_v1beta.AnalyticsAdminServiceClient.update_account",
                    extra={
                        "serviceName": "google.analytics.admin.v1beta.AnalyticsAdminService",
                        "rpcName": "UpdateAccount",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateConversionEvent(
        _BaseAnalyticsAdminServiceRestTransport._BaseUpdateConversionEvent,
        AnalyticsAdminServiceRestStub,
    ):
        def __hash__(self):
            return hash("AnalyticsAdminServiceRestTransport.UpdateConversionEvent")

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
            request: analytics_admin.UpdateConversionEventRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> resources.ConversionEvent:
            r"""Call the update conversion event method over HTTP.

            Args:
                request (~.analytics_admin.UpdateConversionEventRequest):
                    The request object. Request message for
                UpdateConversionEvent RPC
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.resources.ConversionEvent:
                    A conversion event in a Google
                Analytics property.

            """

            http_options = _BaseAnalyticsAdminServiceRestTransport._BaseUpdateConversionEvent._get_http_options()
            request, metadata = self._interceptor.pre_update_conversion_event(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAnalyticsAdminServiceRestTransport._BaseUpdateConversionEvent,
                    "_BaseUpdateConversionEvent__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.analytics.admin_v1beta.AnalyticsAdminServiceClient.UpdateConversionEvent",
                    extra={
                        "serviceName": "google.analytics.admin.v1beta.AnalyticsAdminService",
                        "rpcName": "UpdateConversionEvent",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                AnalyticsAdminServiceRestTransport._UpdateConversionEvent._get_response(
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
            resp = resources.ConversionEvent()
            pb_resp = resources.ConversionEvent.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_conversion_event(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_conversion_event_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = resources.ConversionEvent.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.analytics.admin_v1beta.AnalyticsAdminServiceClient.update_conversion_event",
                    extra={
                        "serviceName": "google.analytics.admin.v1beta.AnalyticsAdminService",
                        "rpcName": "UpdateConversionEvent",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateCustomDimension(
        _BaseAnalyticsAdminServiceRestTransport._BaseUpdateCustomDimension,
        AnalyticsAdminServiceRestStub,
    ):
        def __hash__(self):
            return hash("AnalyticsAdminServiceRestTransport.UpdateCustomDimension")

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
            request: analytics_admin.UpdateCustomDimensionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> resources.CustomDimension:
            r"""Call the update custom dimension method over HTTP.

            Args:
                request (~.analytics_admin.UpdateCustomDimensionRequest):
                    The request object. Request message for
                UpdateCustomDimension RPC.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.resources.CustomDimension:
                    A definition for a CustomDimension.
            """

            http_options = _BaseAnalyticsAdminServiceRestTransport._BaseUpdateCustomDimension._get_http_options()
            request, metadata = self._interceptor.pre_update_custom_dimension(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAnalyticsAdminServiceRestTransport._BaseUpdateCustomDimension,
                    "_BaseUpdateCustomDimension__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.analytics.admin_v1beta.AnalyticsAdminServiceClient.UpdateCustomDimension",
                    extra={
                        "serviceName": "google.analytics.admin.v1beta.AnalyticsAdminService",
                        "rpcName": "UpdateCustomDimension",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                AnalyticsAdminServiceRestTransport._UpdateCustomDimension._get_response(
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
            resp = resources.CustomDimension()
            pb_resp = resources.CustomDimension.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_custom_dimension(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_custom_dimension_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = resources.CustomDimension.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.analytics.admin_v1beta.AnalyticsAdminServiceClient.update_custom_dimension",
                    extra={
                        "serviceName": "google.analytics.admin.v1beta.AnalyticsAdminService",
                        "rpcName": "UpdateCustomDimension",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateCustomMetric(
        _BaseAnalyticsAdminServiceRestTransport._BaseUpdateCustomMetric,
        AnalyticsAdminServiceRestStub,
    ):
        def __hash__(self):
            return hash("AnalyticsAdminServiceRestTransport.UpdateCustomMetric")

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
            request: analytics_admin.UpdateCustomMetricRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> resources.CustomMetric:
            r"""Call the update custom metric method over HTTP.

            Args:
                request (~.analytics_admin.UpdateCustomMetricRequest):
                    The request object. Request message for
                UpdateCustomMetric RPC.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.resources.CustomMetric:
                    A definition for a custom metric.
            """

            http_options = _BaseAnalyticsAdminServiceRestTransport._BaseUpdateCustomMetric._get_http_options()
            request, metadata = self._interceptor.pre_update_custom_metric(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAnalyticsAdminServiceRestTransport._BaseUpdateCustomMetric,
                    "_BaseUpdateCustomMetric__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.analytics.admin_v1beta.AnalyticsAdminServiceClient.UpdateCustomMetric",
                    extra={
                        "serviceName": "google.analytics.admin.v1beta.AnalyticsAdminService",
                        "rpcName": "UpdateCustomMetric",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                AnalyticsAdminServiceRestTransport._UpdateCustomMetric._get_response(
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
            resp = resources.CustomMetric()
            pb_resp = resources.CustomMetric.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_custom_metric(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_custom_metric_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = resources.CustomMetric.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.analytics.admin_v1beta.AnalyticsAdminServiceClient.update_custom_metric",
                    extra={
                        "serviceName": "google.analytics.admin.v1beta.AnalyticsAdminService",
                        "rpcName": "UpdateCustomMetric",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateDataRetentionSettings(
        _BaseAnalyticsAdminServiceRestTransport._BaseUpdateDataRetentionSettings,
        AnalyticsAdminServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "AnalyticsAdminServiceRestTransport.UpdateDataRetentionSettings"
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
            request: analytics_admin.UpdateDataRetentionSettingsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> resources.DataRetentionSettings:
            r"""Call the update data retention
            settings method over HTTP.

                Args:
                    request (~.analytics_admin.UpdateDataRetentionSettingsRequest):
                        The request object. Request message for
                    UpdateDataRetentionSettings RPC.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.resources.DataRetentionSettings:
                        Settings values for data retention.
                    This is a singleton resource.

            """

            http_options = _BaseAnalyticsAdminServiceRestTransport._BaseUpdateDataRetentionSettings._get_http_options()
            request, metadata = self._interceptor.pre_update_data_retention_settings(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAnalyticsAdminServiceRestTransport._BaseUpdateDataRetentionSettings,
                    "_BaseUpdateDataRetentionSettings__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.analytics.admin_v1beta.AnalyticsAdminServiceClient.UpdateDataRetentionSettings",
                    extra={
                        "serviceName": "google.analytics.admin.v1beta.AnalyticsAdminService",
                        "rpcName": "UpdateDataRetentionSettings",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AnalyticsAdminServiceRestTransport._UpdateDataRetentionSettings._get_response(
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
            resp = resources.DataRetentionSettings()
            pb_resp = resources.DataRetentionSettings.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_data_retention_settings(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_update_data_retention_settings_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = resources.DataRetentionSettings.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.analytics.admin_v1beta.AnalyticsAdminServiceClient.update_data_retention_settings",
                    extra={
                        "serviceName": "google.analytics.admin.v1beta.AnalyticsAdminService",
                        "rpcName": "UpdateDataRetentionSettings",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateDataStream(
        _BaseAnalyticsAdminServiceRestTransport._BaseUpdateDataStream,
        AnalyticsAdminServiceRestStub,
    ):
        def __hash__(self):
            return hash("AnalyticsAdminServiceRestTransport.UpdateDataStream")

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
            request: analytics_admin.UpdateDataStreamRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> resources.DataStream:
            r"""Call the update data stream method over HTTP.

            Args:
                request (~.analytics_admin.UpdateDataStreamRequest):
                    The request object. Request message for UpdateDataStream
                RPC.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.resources.DataStream:
                    A resource message representing a
                data stream.

            """

            http_options = _BaseAnalyticsAdminServiceRestTransport._BaseUpdateDataStream._get_http_options()
            request, metadata = self._interceptor.pre_update_data_stream(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAnalyticsAdminServiceRestTransport._BaseUpdateDataStream,
                    "_BaseUpdateDataStream__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.analytics.admin_v1beta.AnalyticsAdminServiceClient.UpdateDataStream",
                    extra={
                        "serviceName": "google.analytics.admin.v1beta.AnalyticsAdminService",
                        "rpcName": "UpdateDataStream",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                AnalyticsAdminServiceRestTransport._UpdateDataStream._get_response(
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
            resp = resources.DataStream()
            pb_resp = resources.DataStream.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_data_stream(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_data_stream_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = resources.DataStream.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.analytics.admin_v1beta.AnalyticsAdminServiceClient.update_data_stream",
                    extra={
                        "serviceName": "google.analytics.admin.v1beta.AnalyticsAdminService",
                        "rpcName": "UpdateDataStream",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateGoogleAdsLink(
        _BaseAnalyticsAdminServiceRestTransport._BaseUpdateGoogleAdsLink,
        AnalyticsAdminServiceRestStub,
    ):
        def __hash__(self):
            return hash("AnalyticsAdminServiceRestTransport.UpdateGoogleAdsLink")

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
            request: analytics_admin.UpdateGoogleAdsLinkRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> resources.GoogleAdsLink:
            r"""Call the update google ads link method over HTTP.

            Args:
                request (~.analytics_admin.UpdateGoogleAdsLinkRequest):
                    The request object. Request message for
                UpdateGoogleAdsLink RPC
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.resources.GoogleAdsLink:
                    A link between a Google Analytics
                property and a Google Ads account.

            """

            http_options = _BaseAnalyticsAdminServiceRestTransport._BaseUpdateGoogleAdsLink._get_http_options()
            request, metadata = self._interceptor.pre_update_google_ads_link(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAnalyticsAdminServiceRestTransport._BaseUpdateGoogleAdsLink,
                    "_BaseUpdateGoogleAdsLink__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.analytics.admin_v1beta.AnalyticsAdminServiceClient.UpdateGoogleAdsLink",
                    extra={
                        "serviceName": "google.analytics.admin.v1beta.AnalyticsAdminService",
                        "rpcName": "UpdateGoogleAdsLink",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                AnalyticsAdminServiceRestTransport._UpdateGoogleAdsLink._get_response(
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
            resp = resources.GoogleAdsLink()
            pb_resp = resources.GoogleAdsLink.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_google_ads_link(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_google_ads_link_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = resources.GoogleAdsLink.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.analytics.admin_v1beta.AnalyticsAdminServiceClient.update_google_ads_link",
                    extra={
                        "serviceName": "google.analytics.admin.v1beta.AnalyticsAdminService",
                        "rpcName": "UpdateGoogleAdsLink",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateKeyEvent(
        _BaseAnalyticsAdminServiceRestTransport._BaseUpdateKeyEvent,
        AnalyticsAdminServiceRestStub,
    ):
        def __hash__(self):
            return hash("AnalyticsAdminServiceRestTransport.UpdateKeyEvent")

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
            request: analytics_admin.UpdateKeyEventRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> resources.KeyEvent:
            r"""Call the update key event method over HTTP.

            Args:
                request (~.analytics_admin.UpdateKeyEventRequest):
                    The request object. Request message for UpdateKeyEvent
                RPC
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.resources.KeyEvent:
                    A key event in a Google Analytics
                property.

            """

            http_options = _BaseAnalyticsAdminServiceRestTransport._BaseUpdateKeyEvent._get_http_options()
            request, metadata = self._interceptor.pre_update_key_event(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAnalyticsAdminServiceRestTransport._BaseUpdateKeyEvent,
                    "_BaseUpdateKeyEvent__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.analytics.admin_v1beta.AnalyticsAdminServiceClient.UpdateKeyEvent",
                    extra={
                        "serviceName": "google.analytics.admin.v1beta.AnalyticsAdminService",
                        "rpcName": "UpdateKeyEvent",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AnalyticsAdminServiceRestTransport._UpdateKeyEvent._get_response(
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
            resp = resources.KeyEvent()
            pb_resp = resources.KeyEvent.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_key_event(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_key_event_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = resources.KeyEvent.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.analytics.admin_v1beta.AnalyticsAdminServiceClient.update_key_event",
                    extra={
                        "serviceName": "google.analytics.admin.v1beta.AnalyticsAdminService",
                        "rpcName": "UpdateKeyEvent",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateMeasurementProtocolSecret(
        _BaseAnalyticsAdminServiceRestTransport._BaseUpdateMeasurementProtocolSecret,
        AnalyticsAdminServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "AnalyticsAdminServiceRestTransport.UpdateMeasurementProtocolSecret"
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
            request: analytics_admin.UpdateMeasurementProtocolSecretRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> resources.MeasurementProtocolSecret:
            r"""Call the update measurement
            protocol secret method over HTTP.

                Args:
                    request (~.analytics_admin.UpdateMeasurementProtocolSecretRequest):
                        The request object. Request message for
                    UpdateMeasurementProtocolSecret RPC
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.resources.MeasurementProtocolSecret:
                        A secret value used for sending hits
                    to Measurement Protocol.

            """

            http_options = _BaseAnalyticsAdminServiceRestTransport._BaseUpdateMeasurementProtocolSecret._get_http_options()
            request, metadata = (
                self._interceptor.pre_update_measurement_protocol_secret(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAnalyticsAdminServiceRestTransport._BaseUpdateMeasurementProtocolSecret,
                    "_BaseUpdateMeasurementProtocolSecret__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.analytics.admin_v1beta.AnalyticsAdminServiceClient.UpdateMeasurementProtocolSecret",
                    extra={
                        "serviceName": "google.analytics.admin.v1beta.AnalyticsAdminService",
                        "rpcName": "UpdateMeasurementProtocolSecret",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AnalyticsAdminServiceRestTransport._UpdateMeasurementProtocolSecret._get_response(
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
            resp = resources.MeasurementProtocolSecret()
            pb_resp = resources.MeasurementProtocolSecret.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_measurement_protocol_secret(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_update_measurement_protocol_secret_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = resources.MeasurementProtocolSecret.to_json(
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
                    "Received response for google.analytics.admin_v1beta.AnalyticsAdminServiceClient.update_measurement_protocol_secret",
                    extra={
                        "serviceName": "google.analytics.admin.v1beta.AnalyticsAdminService",
                        "rpcName": "UpdateMeasurementProtocolSecret",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateProperty(
        _BaseAnalyticsAdminServiceRestTransport._BaseUpdateProperty,
        AnalyticsAdminServiceRestStub,
    ):
        def __hash__(self):
            return hash("AnalyticsAdminServiceRestTransport.UpdateProperty")

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
            request: analytics_admin.UpdatePropertyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> resources.Property:
            r"""Call the update property method over HTTP.

            Args:
                request (~.analytics_admin.UpdatePropertyRequest):
                    The request object. Request message for UpdateProperty
                RPC.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.resources.Property:
                    A resource message representing a
                Google Analytics property.

            """

            http_options = _BaseAnalyticsAdminServiceRestTransport._BaseUpdateProperty._get_http_options()
            request, metadata = self._interceptor.pre_update_property(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAnalyticsAdminServiceRestTransport._BaseUpdateProperty,
                    "_BaseUpdateProperty__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.analytics.admin_v1beta.AnalyticsAdminServiceClient.UpdateProperty",
                    extra={
                        "serviceName": "google.analytics.admin.v1beta.AnalyticsAdminService",
                        "rpcName": "UpdateProperty",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AnalyticsAdminServiceRestTransport._UpdateProperty._get_response(
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
            resp = resources.Property()
            pb_resp = resources.Property.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_property(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_property_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = resources.Property.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.analytics.admin_v1beta.AnalyticsAdminServiceClient.update_property",
                    extra={
                        "serviceName": "google.analytics.admin.v1beta.AnalyticsAdminService",
                        "rpcName": "UpdateProperty",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def acknowledge_user_data_collection(
        self,
    ) -> Callable[
        [analytics_admin.AcknowledgeUserDataCollectionRequest],
        analytics_admin.AcknowledgeUserDataCollectionResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._AcknowledgeUserDataCollection(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def archive_custom_dimension(
        self,
    ) -> Callable[[analytics_admin.ArchiveCustomDimensionRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ArchiveCustomDimension(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def archive_custom_metric(
        self,
    ) -> Callable[[analytics_admin.ArchiveCustomMetricRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ArchiveCustomMetric(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_conversion_event(
        self,
    ) -> Callable[
        [analytics_admin.CreateConversionEventRequest], resources.ConversionEvent
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateConversionEvent(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_custom_dimension(
        self,
    ) -> Callable[
        [analytics_admin.CreateCustomDimensionRequest], resources.CustomDimension
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateCustomDimension(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_custom_metric(
        self,
    ) -> Callable[[analytics_admin.CreateCustomMetricRequest], resources.CustomMetric]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateCustomMetric(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_data_stream(
        self,
    ) -> Callable[[analytics_admin.CreateDataStreamRequest], resources.DataStream]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateDataStream(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_firebase_link(
        self,
    ) -> Callable[[analytics_admin.CreateFirebaseLinkRequest], resources.FirebaseLink]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateFirebaseLink(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_google_ads_link(
        self,
    ) -> Callable[
        [analytics_admin.CreateGoogleAdsLinkRequest], resources.GoogleAdsLink
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateGoogleAdsLink(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_key_event(
        self,
    ) -> Callable[[analytics_admin.CreateKeyEventRequest], resources.KeyEvent]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateKeyEvent(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_measurement_protocol_secret(
        self,
    ) -> Callable[
        [analytics_admin.CreateMeasurementProtocolSecretRequest],
        resources.MeasurementProtocolSecret,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateMeasurementProtocolSecret(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def create_property(
        self,
    ) -> Callable[[analytics_admin.CreatePropertyRequest], resources.Property]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateProperty(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_account(
        self,
    ) -> Callable[[analytics_admin.DeleteAccountRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteAccount(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_conversion_event(
        self,
    ) -> Callable[[analytics_admin.DeleteConversionEventRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteConversionEvent(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_data_stream(
        self,
    ) -> Callable[[analytics_admin.DeleteDataStreamRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteDataStream(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_firebase_link(
        self,
    ) -> Callable[[analytics_admin.DeleteFirebaseLinkRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteFirebaseLink(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_google_ads_link(
        self,
    ) -> Callable[[analytics_admin.DeleteGoogleAdsLinkRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteGoogleAdsLink(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_key_event(
        self,
    ) -> Callable[[analytics_admin.DeleteKeyEventRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteKeyEvent(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_measurement_protocol_secret(
        self,
    ) -> Callable[
        [analytics_admin.DeleteMeasurementProtocolSecretRequest], empty_pb2.Empty
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteMeasurementProtocolSecret(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def delete_property(
        self,
    ) -> Callable[[analytics_admin.DeletePropertyRequest], resources.Property]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteProperty(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_account(
        self,
    ) -> Callable[[analytics_admin.GetAccountRequest], resources.Account]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetAccount(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_conversion_event(
        self,
    ) -> Callable[
        [analytics_admin.GetConversionEventRequest], resources.ConversionEvent
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetConversionEvent(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_custom_dimension(
        self,
    ) -> Callable[
        [analytics_admin.GetCustomDimensionRequest], resources.CustomDimension
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetCustomDimension(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_custom_metric(
        self,
    ) -> Callable[[analytics_admin.GetCustomMetricRequest], resources.CustomMetric]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetCustomMetric(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_data_retention_settings(
        self,
    ) -> Callable[
        [analytics_admin.GetDataRetentionSettingsRequest],
        resources.DataRetentionSettings,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetDataRetentionSettings(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def get_data_sharing_settings(
        self,
    ) -> Callable[
        [analytics_admin.GetDataSharingSettingsRequest], resources.DataSharingSettings
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetDataSharingSettings(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def get_data_stream(
        self,
    ) -> Callable[[analytics_admin.GetDataStreamRequest], resources.DataStream]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetDataStream(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_key_event(
        self,
    ) -> Callable[[analytics_admin.GetKeyEventRequest], resources.KeyEvent]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetKeyEvent(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_measurement_protocol_secret(
        self,
    ) -> Callable[
        [analytics_admin.GetMeasurementProtocolSecretRequest],
        resources.MeasurementProtocolSecret,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetMeasurementProtocolSecret(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def get_property(
        self,
    ) -> Callable[[analytics_admin.GetPropertyRequest], resources.Property]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetProperty(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_accounts(
        self,
    ) -> Callable[
        [analytics_admin.ListAccountsRequest], analytics_admin.ListAccountsResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListAccounts(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_account_summaries(
        self,
    ) -> Callable[
        [analytics_admin.ListAccountSummariesRequest],
        analytics_admin.ListAccountSummariesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListAccountSummaries(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_conversion_events(
        self,
    ) -> Callable[
        [analytics_admin.ListConversionEventsRequest],
        analytics_admin.ListConversionEventsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListConversionEvents(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_custom_dimensions(
        self,
    ) -> Callable[
        [analytics_admin.ListCustomDimensionsRequest],
        analytics_admin.ListCustomDimensionsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListCustomDimensions(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_custom_metrics(
        self,
    ) -> Callable[
        [analytics_admin.ListCustomMetricsRequest],
        analytics_admin.ListCustomMetricsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListCustomMetrics(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_data_streams(
        self,
    ) -> Callable[
        [analytics_admin.ListDataStreamsRequest],
        analytics_admin.ListDataStreamsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListDataStreams(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_firebase_links(
        self,
    ) -> Callable[
        [analytics_admin.ListFirebaseLinksRequest],
        analytics_admin.ListFirebaseLinksResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListFirebaseLinks(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_google_ads_links(
        self,
    ) -> Callable[
        [analytics_admin.ListGoogleAdsLinksRequest],
        analytics_admin.ListGoogleAdsLinksResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListGoogleAdsLinks(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_key_events(
        self,
    ) -> Callable[
        [analytics_admin.ListKeyEventsRequest], analytics_admin.ListKeyEventsResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListKeyEvents(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_measurement_protocol_secrets(
        self,
    ) -> Callable[
        [analytics_admin.ListMeasurementProtocolSecretsRequest],
        analytics_admin.ListMeasurementProtocolSecretsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListMeasurementProtocolSecrets(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def list_properties(
        self,
    ) -> Callable[
        [analytics_admin.ListPropertiesRequest], analytics_admin.ListPropertiesResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListProperties(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def provision_account_ticket(
        self,
    ) -> Callable[
        [analytics_admin.ProvisionAccountTicketRequest],
        analytics_admin.ProvisionAccountTicketResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ProvisionAccountTicket(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def run_access_report(
        self,
    ) -> Callable[
        [analytics_admin.RunAccessReportRequest],
        analytics_admin.RunAccessReportResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._RunAccessReport(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def search_change_history_events(
        self,
    ) -> Callable[
        [analytics_admin.SearchChangeHistoryEventsRequest],
        analytics_admin.SearchChangeHistoryEventsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._SearchChangeHistoryEvents(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def update_account(
        self,
    ) -> Callable[[analytics_admin.UpdateAccountRequest], resources.Account]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateAccount(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_conversion_event(
        self,
    ) -> Callable[
        [analytics_admin.UpdateConversionEventRequest], resources.ConversionEvent
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateConversionEvent(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_custom_dimension(
        self,
    ) -> Callable[
        [analytics_admin.UpdateCustomDimensionRequest], resources.CustomDimension
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateCustomDimension(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_custom_metric(
        self,
    ) -> Callable[[analytics_admin.UpdateCustomMetricRequest], resources.CustomMetric]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateCustomMetric(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_data_retention_settings(
        self,
    ) -> Callable[
        [analytics_admin.UpdateDataRetentionSettingsRequest],
        resources.DataRetentionSettings,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateDataRetentionSettings(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def update_data_stream(
        self,
    ) -> Callable[[analytics_admin.UpdateDataStreamRequest], resources.DataStream]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateDataStream(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_google_ads_link(
        self,
    ) -> Callable[
        [analytics_admin.UpdateGoogleAdsLinkRequest], resources.GoogleAdsLink
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateGoogleAdsLink(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_key_event(
        self,
    ) -> Callable[[analytics_admin.UpdateKeyEventRequest], resources.KeyEvent]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateKeyEvent(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_measurement_protocol_secret(
        self,
    ) -> Callable[
        [analytics_admin.UpdateMeasurementProtocolSecretRequest],
        resources.MeasurementProtocolSecret,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateMeasurementProtocolSecret(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def update_property(
        self,
    ) -> Callable[[analytics_admin.UpdatePropertyRequest], resources.Property]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateProperty(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def kind(self) -> str:
        return "rest"

    def close(self):
        self._session.close()


__all__ = ("AnalyticsAdminServiceRestTransport",)
