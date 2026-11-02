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

from google.analytics.data_v1beta._compat import transcode_request
from google.analytics.data_v1beta.types import analytics_data_api

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseBetaAnalyticsDataRestTransport

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


class BetaAnalyticsDataRestInterceptor:
    """Interceptor for BetaAnalyticsData.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the BetaAnalyticsDataRestTransport.

    .. code-block:: python
        class MyCustomBetaAnalyticsDataInterceptor(BetaAnalyticsDataRestInterceptor):
            def pre_batch_run_pivot_reports(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_run_pivot_reports(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_batch_run_reports(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_run_reports(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_check_compatibility(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_check_compatibility(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_audience_export(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_audience_export(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_audience_export(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_audience_export(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_metadata(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_metadata(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_audience_exports(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_audience_exports(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_query_audience_export(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_query_audience_export(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_run_pivot_report(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_run_pivot_report(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_run_realtime_report(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_run_realtime_report(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_run_report(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_run_report(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = BetaAnalyticsDataRestTransport(interceptor=MyCustomBetaAnalyticsDataInterceptor())
        client = BetaAnalyticsDataClient(transport=transport)


    """

    def pre_batch_run_pivot_reports(
        self,
        request: analytics_data_api.BatchRunPivotReportsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        analytics_data_api.BatchRunPivotReportsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_run_pivot_reports

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BetaAnalyticsData server.
        """
        return request, metadata

    def post_batch_run_pivot_reports(
        self, response: analytics_data_api.BatchRunPivotReportsResponse
    ) -> analytics_data_api.BatchRunPivotReportsResponse:
        """Post-rpc interceptor for batch_run_pivot_reports

        DEPRECATED. Please use the `post_batch_run_pivot_reports_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BetaAnalyticsData server but before
        it is returned to user code. This `post_batch_run_pivot_reports` interceptor runs
        before the `post_batch_run_pivot_reports_with_metadata` interceptor.
        """
        return response

    def post_batch_run_pivot_reports_with_metadata(
        self,
        response: analytics_data_api.BatchRunPivotReportsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        analytics_data_api.BatchRunPivotReportsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_run_pivot_reports

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BetaAnalyticsData server but before it is returned to user code.

        We recommend only using this `post_batch_run_pivot_reports_with_metadata`
        interceptor in new development instead of the `post_batch_run_pivot_reports` interceptor.
        When both interceptors are used, this `post_batch_run_pivot_reports_with_metadata` interceptor runs after the
        `post_batch_run_pivot_reports` interceptor. The (possibly modified) response returned by
        `post_batch_run_pivot_reports` will be passed to
        `post_batch_run_pivot_reports_with_metadata`.
        """
        return response, metadata

    def pre_batch_run_reports(
        self,
        request: analytics_data_api.BatchRunReportsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        analytics_data_api.BatchRunReportsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_run_reports

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BetaAnalyticsData server.
        """
        return request, metadata

    def post_batch_run_reports(
        self, response: analytics_data_api.BatchRunReportsResponse
    ) -> analytics_data_api.BatchRunReportsResponse:
        """Post-rpc interceptor for batch_run_reports

        DEPRECATED. Please use the `post_batch_run_reports_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BetaAnalyticsData server but before
        it is returned to user code. This `post_batch_run_reports` interceptor runs
        before the `post_batch_run_reports_with_metadata` interceptor.
        """
        return response

    def post_batch_run_reports_with_metadata(
        self,
        response: analytics_data_api.BatchRunReportsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        analytics_data_api.BatchRunReportsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_run_reports

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BetaAnalyticsData server but before it is returned to user code.

        We recommend only using this `post_batch_run_reports_with_metadata`
        interceptor in new development instead of the `post_batch_run_reports` interceptor.
        When both interceptors are used, this `post_batch_run_reports_with_metadata` interceptor runs after the
        `post_batch_run_reports` interceptor. The (possibly modified) response returned by
        `post_batch_run_reports` will be passed to
        `post_batch_run_reports_with_metadata`.
        """
        return response, metadata

    def pre_check_compatibility(
        self,
        request: analytics_data_api.CheckCompatibilityRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        analytics_data_api.CheckCompatibilityRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for check_compatibility

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BetaAnalyticsData server.
        """
        return request, metadata

    def post_check_compatibility(
        self, response: analytics_data_api.CheckCompatibilityResponse
    ) -> analytics_data_api.CheckCompatibilityResponse:
        """Post-rpc interceptor for check_compatibility

        DEPRECATED. Please use the `post_check_compatibility_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BetaAnalyticsData server but before
        it is returned to user code. This `post_check_compatibility` interceptor runs
        before the `post_check_compatibility_with_metadata` interceptor.
        """
        return response

    def post_check_compatibility_with_metadata(
        self,
        response: analytics_data_api.CheckCompatibilityResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        analytics_data_api.CheckCompatibilityResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for check_compatibility

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BetaAnalyticsData server but before it is returned to user code.

        We recommend only using this `post_check_compatibility_with_metadata`
        interceptor in new development instead of the `post_check_compatibility` interceptor.
        When both interceptors are used, this `post_check_compatibility_with_metadata` interceptor runs after the
        `post_check_compatibility` interceptor. The (possibly modified) response returned by
        `post_check_compatibility` will be passed to
        `post_check_compatibility_with_metadata`.
        """
        return response, metadata

    def pre_create_audience_export(
        self,
        request: analytics_data_api.CreateAudienceExportRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        analytics_data_api.CreateAudienceExportRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_audience_export

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BetaAnalyticsData server.
        """
        return request, metadata

    def post_create_audience_export(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_audience_export

        DEPRECATED. Please use the `post_create_audience_export_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BetaAnalyticsData server but before
        it is returned to user code. This `post_create_audience_export` interceptor runs
        before the `post_create_audience_export_with_metadata` interceptor.
        """
        return response

    def post_create_audience_export_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_audience_export

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BetaAnalyticsData server but before it is returned to user code.

        We recommend only using this `post_create_audience_export_with_metadata`
        interceptor in new development instead of the `post_create_audience_export` interceptor.
        When both interceptors are used, this `post_create_audience_export_with_metadata` interceptor runs after the
        `post_create_audience_export` interceptor. The (possibly modified) response returned by
        `post_create_audience_export` will be passed to
        `post_create_audience_export_with_metadata`.
        """
        return response, metadata

    def pre_get_audience_export(
        self,
        request: analytics_data_api.GetAudienceExportRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        analytics_data_api.GetAudienceExportRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_audience_export

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BetaAnalyticsData server.
        """
        return request, metadata

    def post_get_audience_export(
        self, response: analytics_data_api.AudienceExport
    ) -> analytics_data_api.AudienceExport:
        """Post-rpc interceptor for get_audience_export

        DEPRECATED. Please use the `post_get_audience_export_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BetaAnalyticsData server but before
        it is returned to user code. This `post_get_audience_export` interceptor runs
        before the `post_get_audience_export_with_metadata` interceptor.
        """
        return response

    def post_get_audience_export_with_metadata(
        self,
        response: analytics_data_api.AudienceExport,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        analytics_data_api.AudienceExport, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for get_audience_export

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BetaAnalyticsData server but before it is returned to user code.

        We recommend only using this `post_get_audience_export_with_metadata`
        interceptor in new development instead of the `post_get_audience_export` interceptor.
        When both interceptors are used, this `post_get_audience_export_with_metadata` interceptor runs after the
        `post_get_audience_export` interceptor. The (possibly modified) response returned by
        `post_get_audience_export` will be passed to
        `post_get_audience_export_with_metadata`.
        """
        return response, metadata

    def pre_get_metadata(
        self,
        request: analytics_data_api.GetMetadataRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        analytics_data_api.GetMetadataRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_metadata

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BetaAnalyticsData server.
        """
        return request, metadata

    def post_get_metadata(
        self, response: analytics_data_api.Metadata
    ) -> analytics_data_api.Metadata:
        """Post-rpc interceptor for get_metadata

        DEPRECATED. Please use the `post_get_metadata_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BetaAnalyticsData server but before
        it is returned to user code. This `post_get_metadata` interceptor runs
        before the `post_get_metadata_with_metadata` interceptor.
        """
        return response

    def post_get_metadata_with_metadata(
        self,
        response: analytics_data_api.Metadata,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[analytics_data_api.Metadata, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_metadata

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BetaAnalyticsData server but before it is returned to user code.

        We recommend only using this `post_get_metadata_with_metadata`
        interceptor in new development instead of the `post_get_metadata` interceptor.
        When both interceptors are used, this `post_get_metadata_with_metadata` interceptor runs after the
        `post_get_metadata` interceptor. The (possibly modified) response returned by
        `post_get_metadata` will be passed to
        `post_get_metadata_with_metadata`.
        """
        return response, metadata

    def pre_list_audience_exports(
        self,
        request: analytics_data_api.ListAudienceExportsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        analytics_data_api.ListAudienceExportsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_audience_exports

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BetaAnalyticsData server.
        """
        return request, metadata

    def post_list_audience_exports(
        self, response: analytics_data_api.ListAudienceExportsResponse
    ) -> analytics_data_api.ListAudienceExportsResponse:
        """Post-rpc interceptor for list_audience_exports

        DEPRECATED. Please use the `post_list_audience_exports_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BetaAnalyticsData server but before
        it is returned to user code. This `post_list_audience_exports` interceptor runs
        before the `post_list_audience_exports_with_metadata` interceptor.
        """
        return response

    def post_list_audience_exports_with_metadata(
        self,
        response: analytics_data_api.ListAudienceExportsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        analytics_data_api.ListAudienceExportsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_audience_exports

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BetaAnalyticsData server but before it is returned to user code.

        We recommend only using this `post_list_audience_exports_with_metadata`
        interceptor in new development instead of the `post_list_audience_exports` interceptor.
        When both interceptors are used, this `post_list_audience_exports_with_metadata` interceptor runs after the
        `post_list_audience_exports` interceptor. The (possibly modified) response returned by
        `post_list_audience_exports` will be passed to
        `post_list_audience_exports_with_metadata`.
        """
        return response, metadata

    def pre_query_audience_export(
        self,
        request: analytics_data_api.QueryAudienceExportRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        analytics_data_api.QueryAudienceExportRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for query_audience_export

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BetaAnalyticsData server.
        """
        return request, metadata

    def post_query_audience_export(
        self, response: analytics_data_api.QueryAudienceExportResponse
    ) -> analytics_data_api.QueryAudienceExportResponse:
        """Post-rpc interceptor for query_audience_export

        DEPRECATED. Please use the `post_query_audience_export_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BetaAnalyticsData server but before
        it is returned to user code. This `post_query_audience_export` interceptor runs
        before the `post_query_audience_export_with_metadata` interceptor.
        """
        return response

    def post_query_audience_export_with_metadata(
        self,
        response: analytics_data_api.QueryAudienceExportResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        analytics_data_api.QueryAudienceExportResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for query_audience_export

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BetaAnalyticsData server but before it is returned to user code.

        We recommend only using this `post_query_audience_export_with_metadata`
        interceptor in new development instead of the `post_query_audience_export` interceptor.
        When both interceptors are used, this `post_query_audience_export_with_metadata` interceptor runs after the
        `post_query_audience_export` interceptor. The (possibly modified) response returned by
        `post_query_audience_export` will be passed to
        `post_query_audience_export_with_metadata`.
        """
        return response, metadata

    def pre_run_pivot_report(
        self,
        request: analytics_data_api.RunPivotReportRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        analytics_data_api.RunPivotReportRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for run_pivot_report

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BetaAnalyticsData server.
        """
        return request, metadata

    def post_run_pivot_report(
        self, response: analytics_data_api.RunPivotReportResponse
    ) -> analytics_data_api.RunPivotReportResponse:
        """Post-rpc interceptor for run_pivot_report

        DEPRECATED. Please use the `post_run_pivot_report_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BetaAnalyticsData server but before
        it is returned to user code. This `post_run_pivot_report` interceptor runs
        before the `post_run_pivot_report_with_metadata` interceptor.
        """
        return response

    def post_run_pivot_report_with_metadata(
        self,
        response: analytics_data_api.RunPivotReportResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        analytics_data_api.RunPivotReportResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for run_pivot_report

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BetaAnalyticsData server but before it is returned to user code.

        We recommend only using this `post_run_pivot_report_with_metadata`
        interceptor in new development instead of the `post_run_pivot_report` interceptor.
        When both interceptors are used, this `post_run_pivot_report_with_metadata` interceptor runs after the
        `post_run_pivot_report` interceptor. The (possibly modified) response returned by
        `post_run_pivot_report` will be passed to
        `post_run_pivot_report_with_metadata`.
        """
        return response, metadata

    def pre_run_realtime_report(
        self,
        request: analytics_data_api.RunRealtimeReportRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        analytics_data_api.RunRealtimeReportRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for run_realtime_report

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BetaAnalyticsData server.
        """
        return request, metadata

    def post_run_realtime_report(
        self, response: analytics_data_api.RunRealtimeReportResponse
    ) -> analytics_data_api.RunRealtimeReportResponse:
        """Post-rpc interceptor for run_realtime_report

        DEPRECATED. Please use the `post_run_realtime_report_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BetaAnalyticsData server but before
        it is returned to user code. This `post_run_realtime_report` interceptor runs
        before the `post_run_realtime_report_with_metadata` interceptor.
        """
        return response

    def post_run_realtime_report_with_metadata(
        self,
        response: analytics_data_api.RunRealtimeReportResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        analytics_data_api.RunRealtimeReportResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for run_realtime_report

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BetaAnalyticsData server but before it is returned to user code.

        We recommend only using this `post_run_realtime_report_with_metadata`
        interceptor in new development instead of the `post_run_realtime_report` interceptor.
        When both interceptors are used, this `post_run_realtime_report_with_metadata` interceptor runs after the
        `post_run_realtime_report` interceptor. The (possibly modified) response returned by
        `post_run_realtime_report` will be passed to
        `post_run_realtime_report_with_metadata`.
        """
        return response, metadata

    def pre_run_report(
        self,
        request: analytics_data_api.RunReportRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        analytics_data_api.RunReportRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for run_report

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BetaAnalyticsData server.
        """
        return request, metadata

    def post_run_report(
        self, response: analytics_data_api.RunReportResponse
    ) -> analytics_data_api.RunReportResponse:
        """Post-rpc interceptor for run_report

        DEPRECATED. Please use the `post_run_report_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BetaAnalyticsData server but before
        it is returned to user code. This `post_run_report` interceptor runs
        before the `post_run_report_with_metadata` interceptor.
        """
        return response

    def post_run_report_with_metadata(
        self,
        response: analytics_data_api.RunReportResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        analytics_data_api.RunReportResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for run_report

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BetaAnalyticsData server but before it is returned to user code.

        We recommend only using this `post_run_report_with_metadata`
        interceptor in new development instead of the `post_run_report` interceptor.
        When both interceptors are used, this `post_run_report_with_metadata` interceptor runs after the
        `post_run_report` interceptor. The (possibly modified) response returned by
        `post_run_report` will be passed to
        `post_run_report_with_metadata`.
        """
        return response, metadata


@dataclasses.dataclass
class BetaAnalyticsDataRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: BetaAnalyticsDataRestInterceptor


class BetaAnalyticsDataRestTransport(_BaseBetaAnalyticsDataRestTransport):
    """REST backend synchronous transport for BetaAnalyticsData.

    Google Analytics reporting data service.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "analyticsdata.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[BetaAnalyticsDataRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'analyticsdata.googleapis.com').
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
            interceptor (Optional[BetaAnalyticsDataRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or BetaAnalyticsDataRestInterceptor()
        self._prep_wrapped_messages(client_info)

    @property
    def operations_client(self) -> operations_v1.AbstractOperationsClient:
        """Create the client designed to process long-running operations.

        This property caches on the instance; repeated calls return the same
        client.
        """
        # Only create a new client if we do not already have one.
        if self._operations_client is None:
            http_options: Dict[str, List[Dict[str, str]]] = {}

            rest_transport = operations_v1.OperationsRestTransport(
                host=self._host,
                # use the credentials which are saved
                credentials=self._credentials,
                scopes=self._scopes,
                http_options=http_options,
                path_prefix="v1beta",
            )

            self._operations_client = operations_v1.AbstractOperationsClient(
                transport=rest_transport
            )

        # Return the client from cache.
        return self._operations_client

    class _BatchRunPivotReports(
        _BaseBetaAnalyticsDataRestTransport._BaseBatchRunPivotReports,
        BetaAnalyticsDataRestStub,
    ):
        def __hash__(self):
            return hash("BetaAnalyticsDataRestTransport.BatchRunPivotReports")

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
            request: analytics_data_api.BatchRunPivotReportsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> analytics_data_api.BatchRunPivotReportsResponse:
            r"""Call the batch run pivot reports method over HTTP.

            Args:
                request (~.analytics_data_api.BatchRunPivotReportsRequest):
                    The request object. The batch request containing multiple
                pivot report requests.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.analytics_data_api.BatchRunPivotReportsResponse:
                    The batch response containing
                multiple pivot reports.

            """

            http_options = _BaseBetaAnalyticsDataRestTransport._BaseBatchRunPivotReports._get_http_options()
            request, metadata = self._interceptor.pre_batch_run_pivot_reports(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBetaAnalyticsDataRestTransport._BaseBatchRunPivotReports,
                    "_BaseBatchRunPivotReports__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.analytics.data_v1beta.BetaAnalyticsDataClient.BatchRunPivotReports",
                    extra={
                        "serviceName": "google.analytics.data.v1beta.BetaAnalyticsData",
                        "rpcName": "BatchRunPivotReports",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                BetaAnalyticsDataRestTransport._BatchRunPivotReports._get_response(
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
            resp = analytics_data_api.BatchRunPivotReportsResponse()
            pb_resp = analytics_data_api.BatchRunPivotReportsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_run_pivot_reports(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_batch_run_pivot_reports_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        analytics_data_api.BatchRunPivotReportsResponse.to_json(
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
                    "Received response for google.analytics.data_v1beta.BetaAnalyticsDataClient.batch_run_pivot_reports",
                    extra={
                        "serviceName": "google.analytics.data.v1beta.BetaAnalyticsData",
                        "rpcName": "BatchRunPivotReports",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BatchRunReports(
        _BaseBetaAnalyticsDataRestTransport._BaseBatchRunReports,
        BetaAnalyticsDataRestStub,
    ):
        def __hash__(self):
            return hash("BetaAnalyticsDataRestTransport.BatchRunReports")

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
            request: analytics_data_api.BatchRunReportsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> analytics_data_api.BatchRunReportsResponse:
            r"""Call the batch run reports method over HTTP.

            Args:
                request (~.analytics_data_api.BatchRunReportsRequest):
                    The request object. The batch request containing multiple
                report requests.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.analytics_data_api.BatchRunReportsResponse:
                    The batch response containing
                multiple reports.

            """

            http_options = _BaseBetaAnalyticsDataRestTransport._BaseBatchRunReports._get_http_options()
            request, metadata = self._interceptor.pre_batch_run_reports(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBetaAnalyticsDataRestTransport._BaseBatchRunReports,
                    "_BaseBatchRunReports__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.analytics.data_v1beta.BetaAnalyticsDataClient.BatchRunReports",
                    extra={
                        "serviceName": "google.analytics.data.v1beta.BetaAnalyticsData",
                        "rpcName": "BatchRunReports",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BetaAnalyticsDataRestTransport._BatchRunReports._get_response(
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
            resp = analytics_data_api.BatchRunReportsResponse()
            pb_resp = analytics_data_api.BatchRunReportsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_run_reports(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_batch_run_reports_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        analytics_data_api.BatchRunReportsResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.analytics.data_v1beta.BetaAnalyticsDataClient.batch_run_reports",
                    extra={
                        "serviceName": "google.analytics.data.v1beta.BetaAnalyticsData",
                        "rpcName": "BatchRunReports",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CheckCompatibility(
        _BaseBetaAnalyticsDataRestTransport._BaseCheckCompatibility,
        BetaAnalyticsDataRestStub,
    ):
        def __hash__(self):
            return hash("BetaAnalyticsDataRestTransport.CheckCompatibility")

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
            request: analytics_data_api.CheckCompatibilityRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> analytics_data_api.CheckCompatibilityResponse:
            r"""Call the check compatibility method over HTTP.

            Args:
                request (~.analytics_data_api.CheckCompatibilityRequest):
                    The request object. The request for compatibility information for a report's
                dimensions and metrics. Check compatibility provides a
                preview of the compatibility of a report; fields shared
                with the ``runReport`` request should be the same values
                as in your ``runReport`` request.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.analytics_data_api.CheckCompatibilityResponse:
                    The compatibility response with the
                compatibility of each dimension &
                metric.

            """

            http_options = _BaseBetaAnalyticsDataRestTransport._BaseCheckCompatibility._get_http_options()
            request, metadata = self._interceptor.pre_check_compatibility(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBetaAnalyticsDataRestTransport._BaseCheckCompatibility,
                    "_BaseCheckCompatibility__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.analytics.data_v1beta.BetaAnalyticsDataClient.CheckCompatibility",
                    extra={
                        "serviceName": "google.analytics.data.v1beta.BetaAnalyticsData",
                        "rpcName": "CheckCompatibility",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BetaAnalyticsDataRestTransport._CheckCompatibility._get_response(
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
            resp = analytics_data_api.CheckCompatibilityResponse()
            pb_resp = analytics_data_api.CheckCompatibilityResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_check_compatibility(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_check_compatibility_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        analytics_data_api.CheckCompatibilityResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.analytics.data_v1beta.BetaAnalyticsDataClient.check_compatibility",
                    extra={
                        "serviceName": "google.analytics.data.v1beta.BetaAnalyticsData",
                        "rpcName": "CheckCompatibility",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateAudienceExport(
        _BaseBetaAnalyticsDataRestTransport._BaseCreateAudienceExport,
        BetaAnalyticsDataRestStub,
    ):
        def __hash__(self):
            return hash("BetaAnalyticsDataRestTransport.CreateAudienceExport")

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
            request: analytics_data_api.CreateAudienceExportRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create audience export method over HTTP.

            Args:
                request (~.analytics_data_api.CreateAudienceExportRequest):
                    The request object. A request to create a new audience
                export.
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

            http_options = _BaseBetaAnalyticsDataRestTransport._BaseCreateAudienceExport._get_http_options()
            request, metadata = self._interceptor.pre_create_audience_export(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBetaAnalyticsDataRestTransport._BaseCreateAudienceExport,
                    "_BaseCreateAudienceExport__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.analytics.data_v1beta.BetaAnalyticsDataClient.CreateAudienceExport",
                    extra={
                        "serviceName": "google.analytics.data.v1beta.BetaAnalyticsData",
                        "rpcName": "CreateAudienceExport",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                BetaAnalyticsDataRestTransport._CreateAudienceExport._get_response(
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

            resp = self._interceptor.post_create_audience_export(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_audience_export_with_metadata(
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
                    "Received response for google.analytics.data_v1beta.BetaAnalyticsDataClient.create_audience_export",
                    extra={
                        "serviceName": "google.analytics.data.v1beta.BetaAnalyticsData",
                        "rpcName": "CreateAudienceExport",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetAudienceExport(
        _BaseBetaAnalyticsDataRestTransport._BaseGetAudienceExport,
        BetaAnalyticsDataRestStub,
    ):
        def __hash__(self):
            return hash("BetaAnalyticsDataRestTransport.GetAudienceExport")

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
            request: analytics_data_api.GetAudienceExportRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> analytics_data_api.AudienceExport:
            r"""Call the get audience export method over HTTP.

            Args:
                request (~.analytics_data_api.GetAudienceExportRequest):
                    The request object. A request to retrieve configuration
                metadata about a specific audience
                export.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.analytics_data_api.AudienceExport:
                    An audience export is a list of users
                in an audience at the time of the list's
                creation. One audience may have multiple
                audience exports created for different
                days.

            """

            http_options = _BaseBetaAnalyticsDataRestTransport._BaseGetAudienceExport._get_http_options()
            request, metadata = self._interceptor.pre_get_audience_export(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBetaAnalyticsDataRestTransport._BaseGetAudienceExport,
                    "_BaseGetAudienceExport__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.analytics.data_v1beta.BetaAnalyticsDataClient.GetAudienceExport",
                    extra={
                        "serviceName": "google.analytics.data.v1beta.BetaAnalyticsData",
                        "rpcName": "GetAudienceExport",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BetaAnalyticsDataRestTransport._GetAudienceExport._get_response(
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
            resp = analytics_data_api.AudienceExport()
            pb_resp = analytics_data_api.AudienceExport.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_audience_export(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_audience_export_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = analytics_data_api.AudienceExport.to_json(
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
                    "Received response for google.analytics.data_v1beta.BetaAnalyticsDataClient.get_audience_export",
                    extra={
                        "serviceName": "google.analytics.data.v1beta.BetaAnalyticsData",
                        "rpcName": "GetAudienceExport",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetMetadata(
        _BaseBetaAnalyticsDataRestTransport._BaseGetMetadata, BetaAnalyticsDataRestStub
    ):
        def __hash__(self):
            return hash("BetaAnalyticsDataRestTransport.GetMetadata")

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
            request: analytics_data_api.GetMetadataRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> analytics_data_api.Metadata:
            r"""Call the get metadata method over HTTP.

            Args:
                request (~.analytics_data_api.GetMetadataRequest):
                    The request object. Request for a property's dimension
                and metric metadata.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.analytics_data_api.Metadata:
                    The dimensions, metrics and
                comparisons currently accepted in
                reporting methods.

            """

            http_options = (
                _BaseBetaAnalyticsDataRestTransport._BaseGetMetadata._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_metadata(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBetaAnalyticsDataRestTransport._BaseGetMetadata,
                    "_BaseGetMetadata__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.analytics.data_v1beta.BetaAnalyticsDataClient.GetMetadata",
                    extra={
                        "serviceName": "google.analytics.data.v1beta.BetaAnalyticsData",
                        "rpcName": "GetMetadata",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BetaAnalyticsDataRestTransport._GetMetadata._get_response(
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
            resp = analytics_data_api.Metadata()
            pb_resp = analytics_data_api.Metadata.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_metadata(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_metadata_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = analytics_data_api.Metadata.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.analytics.data_v1beta.BetaAnalyticsDataClient.get_metadata",
                    extra={
                        "serviceName": "google.analytics.data.v1beta.BetaAnalyticsData",
                        "rpcName": "GetMetadata",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListAudienceExports(
        _BaseBetaAnalyticsDataRestTransport._BaseListAudienceExports,
        BetaAnalyticsDataRestStub,
    ):
        def __hash__(self):
            return hash("BetaAnalyticsDataRestTransport.ListAudienceExports")

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
            request: analytics_data_api.ListAudienceExportsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> analytics_data_api.ListAudienceExportsResponse:
            r"""Call the list audience exports method over HTTP.

            Args:
                request (~.analytics_data_api.ListAudienceExportsRequest):
                    The request object. A request to list all audience
                exports for a property.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.analytics_data_api.ListAudienceExportsResponse:
                    A list of all audience exports for a
                property.

            """

            http_options = _BaseBetaAnalyticsDataRestTransport._BaseListAudienceExports._get_http_options()
            request, metadata = self._interceptor.pre_list_audience_exports(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBetaAnalyticsDataRestTransport._BaseListAudienceExports,
                    "_BaseListAudienceExports__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.analytics.data_v1beta.BetaAnalyticsDataClient.ListAudienceExports",
                    extra={
                        "serviceName": "google.analytics.data.v1beta.BetaAnalyticsData",
                        "rpcName": "ListAudienceExports",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                BetaAnalyticsDataRestTransport._ListAudienceExports._get_response(
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
            resp = analytics_data_api.ListAudienceExportsResponse()
            pb_resp = analytics_data_api.ListAudienceExportsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_audience_exports(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_audience_exports_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        analytics_data_api.ListAudienceExportsResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.analytics.data_v1beta.BetaAnalyticsDataClient.list_audience_exports",
                    extra={
                        "serviceName": "google.analytics.data.v1beta.BetaAnalyticsData",
                        "rpcName": "ListAudienceExports",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _QueryAudienceExport(
        _BaseBetaAnalyticsDataRestTransport._BaseQueryAudienceExport,
        BetaAnalyticsDataRestStub,
    ):
        def __hash__(self):
            return hash("BetaAnalyticsDataRestTransport.QueryAudienceExport")

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
            request: analytics_data_api.QueryAudienceExportRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> analytics_data_api.QueryAudienceExportResponse:
            r"""Call the query audience export method over HTTP.

            Args:
                request (~.analytics_data_api.QueryAudienceExportRequest):
                    The request object. A request to list users in an
                audience export.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.analytics_data_api.QueryAudienceExportResponse:
                    A list of users in an audience
                export.

            """

            http_options = _BaseBetaAnalyticsDataRestTransport._BaseQueryAudienceExport._get_http_options()
            request, metadata = self._interceptor.pre_query_audience_export(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBetaAnalyticsDataRestTransport._BaseQueryAudienceExport,
                    "_BaseQueryAudienceExport__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.analytics.data_v1beta.BetaAnalyticsDataClient.QueryAudienceExport",
                    extra={
                        "serviceName": "google.analytics.data.v1beta.BetaAnalyticsData",
                        "rpcName": "QueryAudienceExport",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                BetaAnalyticsDataRestTransport._QueryAudienceExport._get_response(
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
            resp = analytics_data_api.QueryAudienceExportResponse()
            pb_resp = analytics_data_api.QueryAudienceExportResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_query_audience_export(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_query_audience_export_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        analytics_data_api.QueryAudienceExportResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.analytics.data_v1beta.BetaAnalyticsDataClient.query_audience_export",
                    extra={
                        "serviceName": "google.analytics.data.v1beta.BetaAnalyticsData",
                        "rpcName": "QueryAudienceExport",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _RunPivotReport(
        _BaseBetaAnalyticsDataRestTransport._BaseRunPivotReport,
        BetaAnalyticsDataRestStub,
    ):
        def __hash__(self):
            return hash("BetaAnalyticsDataRestTransport.RunPivotReport")

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
            request: analytics_data_api.RunPivotReportRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> analytics_data_api.RunPivotReportResponse:
            r"""Call the run pivot report method over HTTP.

            Args:
                request (~.analytics_data_api.RunPivotReportRequest):
                    The request object. The request to generate a pivot
                report.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.analytics_data_api.RunPivotReportResponse:
                    The response pivot report table
                corresponding to a pivot request.

            """

            http_options = _BaseBetaAnalyticsDataRestTransport._BaseRunPivotReport._get_http_options()
            request, metadata = self._interceptor.pre_run_pivot_report(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBetaAnalyticsDataRestTransport._BaseRunPivotReport,
                    "_BaseRunPivotReport__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.analytics.data_v1beta.BetaAnalyticsDataClient.RunPivotReport",
                    extra={
                        "serviceName": "google.analytics.data.v1beta.BetaAnalyticsData",
                        "rpcName": "RunPivotReport",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BetaAnalyticsDataRestTransport._RunPivotReport._get_response(
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
            resp = analytics_data_api.RunPivotReportResponse()
            pb_resp = analytics_data_api.RunPivotReportResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_run_pivot_report(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_run_pivot_report_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        analytics_data_api.RunPivotReportResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.analytics.data_v1beta.BetaAnalyticsDataClient.run_pivot_report",
                    extra={
                        "serviceName": "google.analytics.data.v1beta.BetaAnalyticsData",
                        "rpcName": "RunPivotReport",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _RunRealtimeReport(
        _BaseBetaAnalyticsDataRestTransport._BaseRunRealtimeReport,
        BetaAnalyticsDataRestStub,
    ):
        def __hash__(self):
            return hash("BetaAnalyticsDataRestTransport.RunRealtimeReport")

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
            request: analytics_data_api.RunRealtimeReportRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> analytics_data_api.RunRealtimeReportResponse:
            r"""Call the run realtime report method over HTTP.

            Args:
                request (~.analytics_data_api.RunRealtimeReportRequest):
                    The request object. The request to generate a realtime
                report.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.analytics_data_api.RunRealtimeReportResponse:
                    The response realtime report table
                corresponding to a request.

            """

            http_options = _BaseBetaAnalyticsDataRestTransport._BaseRunRealtimeReport._get_http_options()
            request, metadata = self._interceptor.pre_run_realtime_report(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBetaAnalyticsDataRestTransport._BaseRunRealtimeReport,
                    "_BaseRunRealtimeReport__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.analytics.data_v1beta.BetaAnalyticsDataClient.RunRealtimeReport",
                    extra={
                        "serviceName": "google.analytics.data.v1beta.BetaAnalyticsData",
                        "rpcName": "RunRealtimeReport",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BetaAnalyticsDataRestTransport._RunRealtimeReport._get_response(
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
            resp = analytics_data_api.RunRealtimeReportResponse()
            pb_resp = analytics_data_api.RunRealtimeReportResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_run_realtime_report(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_run_realtime_report_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        analytics_data_api.RunRealtimeReportResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.analytics.data_v1beta.BetaAnalyticsDataClient.run_realtime_report",
                    extra={
                        "serviceName": "google.analytics.data.v1beta.BetaAnalyticsData",
                        "rpcName": "RunRealtimeReport",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _RunReport(
        _BaseBetaAnalyticsDataRestTransport._BaseRunReport, BetaAnalyticsDataRestStub
    ):
        def __hash__(self):
            return hash("BetaAnalyticsDataRestTransport.RunReport")

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
            request: analytics_data_api.RunReportRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> analytics_data_api.RunReportResponse:
            r"""Call the run report method over HTTP.

            Args:
                request (~.analytics_data_api.RunReportRequest):
                    The request object. The request to generate a report.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.analytics_data_api.RunReportResponse:
                    The response report table
                corresponding to a request.

            """

            http_options = (
                _BaseBetaAnalyticsDataRestTransport._BaseRunReport._get_http_options()
            )
            request, metadata = self._interceptor.pre_run_report(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBetaAnalyticsDataRestTransport._BaseRunReport,
                    "_BaseRunReport__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.analytics.data_v1beta.BetaAnalyticsDataClient.RunReport",
                    extra={
                        "serviceName": "google.analytics.data.v1beta.BetaAnalyticsData",
                        "rpcName": "RunReport",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BetaAnalyticsDataRestTransport._RunReport._get_response(
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
            resp = analytics_data_api.RunReportResponse()
            pb_resp = analytics_data_api.RunReportResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_run_report(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_run_report_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = analytics_data_api.RunReportResponse.to_json(
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
                    "Received response for google.analytics.data_v1beta.BetaAnalyticsDataClient.run_report",
                    extra={
                        "serviceName": "google.analytics.data.v1beta.BetaAnalyticsData",
                        "rpcName": "RunReport",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def batch_run_pivot_reports(
        self,
    ) -> Callable[
        [analytics_data_api.BatchRunPivotReportsRequest],
        analytics_data_api.BatchRunPivotReportsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchRunPivotReports(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def batch_run_reports(
        self,
    ) -> Callable[
        [analytics_data_api.BatchRunReportsRequest],
        analytics_data_api.BatchRunReportsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchRunReports(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def check_compatibility(
        self,
    ) -> Callable[
        [analytics_data_api.CheckCompatibilityRequest],
        analytics_data_api.CheckCompatibilityResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CheckCompatibility(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_audience_export(
        self,
    ) -> Callable[
        [analytics_data_api.CreateAudienceExportRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateAudienceExport(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_audience_export(
        self,
    ) -> Callable[
        [analytics_data_api.GetAudienceExportRequest], analytics_data_api.AudienceExport
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetAudienceExport(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_metadata(
        self,
    ) -> Callable[[analytics_data_api.GetMetadataRequest], analytics_data_api.Metadata]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetMetadata(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_audience_exports(
        self,
    ) -> Callable[
        [analytics_data_api.ListAudienceExportsRequest],
        analytics_data_api.ListAudienceExportsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListAudienceExports(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def query_audience_export(
        self,
    ) -> Callable[
        [analytics_data_api.QueryAudienceExportRequest],
        analytics_data_api.QueryAudienceExportResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._QueryAudienceExport(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def run_pivot_report(
        self,
    ) -> Callable[
        [analytics_data_api.RunPivotReportRequest],
        analytics_data_api.RunPivotReportResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._RunPivotReport(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def run_realtime_report(
        self,
    ) -> Callable[
        [analytics_data_api.RunRealtimeReportRequest],
        analytics_data_api.RunRealtimeReportResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._RunRealtimeReport(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def run_report(
        self,
    ) -> Callable[
        [analytics_data_api.RunReportRequest], analytics_data_api.RunReportResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._RunReport(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def kind(self) -> str:
        return "rest"

    def close(self):
        self._session.close()


__all__ = ("BetaAnalyticsDataRestTransport",)
