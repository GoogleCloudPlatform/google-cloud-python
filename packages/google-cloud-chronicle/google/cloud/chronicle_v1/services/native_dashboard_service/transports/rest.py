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

from google.cloud.chronicle_v1._compat import transcode_request
from google.cloud.chronicle_v1.types import native_dashboard
from google.cloud.chronicle_v1.types import native_dashboard as gcc_native_dashboard

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseNativeDashboardServiceRestTransport

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


class NativeDashboardServiceRestInterceptor:
    """Interceptor for NativeDashboardService.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the NativeDashboardServiceRestTransport.

    .. code-block:: python
        class MyCustomNativeDashboardServiceInterceptor(NativeDashboardServiceRestInterceptor):
            def pre_add_chart(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_add_chart(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_native_dashboard(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_native_dashboard(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_native_dashboard(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_duplicate_chart(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_duplicate_chart(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_duplicate_native_dashboard(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_duplicate_native_dashboard(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_edit_chart(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_edit_chart(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_export_native_dashboards(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_export_native_dashboards(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_native_dashboard(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_native_dashboard(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_import_native_dashboards(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_import_native_dashboards(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_native_dashboards(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_native_dashboards(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_remove_chart(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_remove_chart(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_native_dashboard(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_native_dashboard(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = NativeDashboardServiceRestTransport(interceptor=MyCustomNativeDashboardServiceInterceptor())
        client = NativeDashboardServiceClient(transport=transport)


    """

    def pre_add_chart(
        self,
        request: native_dashboard.AddChartRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        native_dashboard.AddChartRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for add_chart

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NativeDashboardService server.
        """
        return request, metadata

    def post_add_chart(
        self, response: native_dashboard.AddChartResponse
    ) -> native_dashboard.AddChartResponse:
        """Post-rpc interceptor for add_chart

        DEPRECATED. Please use the `post_add_chart_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NativeDashboardService server but before
        it is returned to user code. This `post_add_chart` interceptor runs
        before the `post_add_chart_with_metadata` interceptor.
        """
        return response

    def post_add_chart_with_metadata(
        self,
        response: native_dashboard.AddChartResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        native_dashboard.AddChartResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for add_chart

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NativeDashboardService server but before it is returned to user code.

        We recommend only using this `post_add_chart_with_metadata`
        interceptor in new development instead of the `post_add_chart` interceptor.
        When both interceptors are used, this `post_add_chart_with_metadata` interceptor runs after the
        `post_add_chart` interceptor. The (possibly modified) response returned by
        `post_add_chart` will be passed to
        `post_add_chart_with_metadata`.
        """
        return response, metadata

    def pre_create_native_dashboard(
        self,
        request: gcc_native_dashboard.CreateNativeDashboardRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gcc_native_dashboard.CreateNativeDashboardRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_native_dashboard

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NativeDashboardService server.
        """
        return request, metadata

    def post_create_native_dashboard(
        self, response: gcc_native_dashboard.NativeDashboard
    ) -> gcc_native_dashboard.NativeDashboard:
        """Post-rpc interceptor for create_native_dashboard

        DEPRECATED. Please use the `post_create_native_dashboard_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NativeDashboardService server but before
        it is returned to user code. This `post_create_native_dashboard` interceptor runs
        before the `post_create_native_dashboard_with_metadata` interceptor.
        """
        return response

    def post_create_native_dashboard_with_metadata(
        self,
        response: gcc_native_dashboard.NativeDashboard,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gcc_native_dashboard.NativeDashboard, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for create_native_dashboard

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NativeDashboardService server but before it is returned to user code.

        We recommend only using this `post_create_native_dashboard_with_metadata`
        interceptor in new development instead of the `post_create_native_dashboard` interceptor.
        When both interceptors are used, this `post_create_native_dashboard_with_metadata` interceptor runs after the
        `post_create_native_dashboard` interceptor. The (possibly modified) response returned by
        `post_create_native_dashboard` will be passed to
        `post_create_native_dashboard_with_metadata`.
        """
        return response, metadata

    def pre_delete_native_dashboard(
        self,
        request: native_dashboard.DeleteNativeDashboardRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        native_dashboard.DeleteNativeDashboardRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_native_dashboard

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NativeDashboardService server.
        """
        return request, metadata

    def pre_duplicate_chart(
        self,
        request: native_dashboard.DuplicateChartRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        native_dashboard.DuplicateChartRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for duplicate_chart

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NativeDashboardService server.
        """
        return request, metadata

    def post_duplicate_chart(
        self, response: native_dashboard.DuplicateChartResponse
    ) -> native_dashboard.DuplicateChartResponse:
        """Post-rpc interceptor for duplicate_chart

        DEPRECATED. Please use the `post_duplicate_chart_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NativeDashboardService server but before
        it is returned to user code. This `post_duplicate_chart` interceptor runs
        before the `post_duplicate_chart_with_metadata` interceptor.
        """
        return response

    def post_duplicate_chart_with_metadata(
        self,
        response: native_dashboard.DuplicateChartResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        native_dashboard.DuplicateChartResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for duplicate_chart

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NativeDashboardService server but before it is returned to user code.

        We recommend only using this `post_duplicate_chart_with_metadata`
        interceptor in new development instead of the `post_duplicate_chart` interceptor.
        When both interceptors are used, this `post_duplicate_chart_with_metadata` interceptor runs after the
        `post_duplicate_chart` interceptor. The (possibly modified) response returned by
        `post_duplicate_chart` will be passed to
        `post_duplicate_chart_with_metadata`.
        """
        return response, metadata

    def pre_duplicate_native_dashboard(
        self,
        request: gcc_native_dashboard.DuplicateNativeDashboardRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gcc_native_dashboard.DuplicateNativeDashboardRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for duplicate_native_dashboard

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NativeDashboardService server.
        """
        return request, metadata

    def post_duplicate_native_dashboard(
        self, response: gcc_native_dashboard.NativeDashboard
    ) -> gcc_native_dashboard.NativeDashboard:
        """Post-rpc interceptor for duplicate_native_dashboard

        DEPRECATED. Please use the `post_duplicate_native_dashboard_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NativeDashboardService server but before
        it is returned to user code. This `post_duplicate_native_dashboard` interceptor runs
        before the `post_duplicate_native_dashboard_with_metadata` interceptor.
        """
        return response

    def post_duplicate_native_dashboard_with_metadata(
        self,
        response: gcc_native_dashboard.NativeDashboard,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gcc_native_dashboard.NativeDashboard, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for duplicate_native_dashboard

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NativeDashboardService server but before it is returned to user code.

        We recommend only using this `post_duplicate_native_dashboard_with_metadata`
        interceptor in new development instead of the `post_duplicate_native_dashboard` interceptor.
        When both interceptors are used, this `post_duplicate_native_dashboard_with_metadata` interceptor runs after the
        `post_duplicate_native_dashboard` interceptor. The (possibly modified) response returned by
        `post_duplicate_native_dashboard` will be passed to
        `post_duplicate_native_dashboard_with_metadata`.
        """
        return response, metadata

    def pre_edit_chart(
        self,
        request: native_dashboard.EditChartRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        native_dashboard.EditChartRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for edit_chart

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NativeDashboardService server.
        """
        return request, metadata

    def post_edit_chart(
        self, response: native_dashboard.EditChartResponse
    ) -> native_dashboard.EditChartResponse:
        """Post-rpc interceptor for edit_chart

        DEPRECATED. Please use the `post_edit_chart_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NativeDashboardService server but before
        it is returned to user code. This `post_edit_chart` interceptor runs
        before the `post_edit_chart_with_metadata` interceptor.
        """
        return response

    def post_edit_chart_with_metadata(
        self,
        response: native_dashboard.EditChartResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        native_dashboard.EditChartResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for edit_chart

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NativeDashboardService server but before it is returned to user code.

        We recommend only using this `post_edit_chart_with_metadata`
        interceptor in new development instead of the `post_edit_chart` interceptor.
        When both interceptors are used, this `post_edit_chart_with_metadata` interceptor runs after the
        `post_edit_chart` interceptor. The (possibly modified) response returned by
        `post_edit_chart` will be passed to
        `post_edit_chart_with_metadata`.
        """
        return response, metadata

    def pre_export_native_dashboards(
        self,
        request: native_dashboard.ExportNativeDashboardsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        native_dashboard.ExportNativeDashboardsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for export_native_dashboards

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NativeDashboardService server.
        """
        return request, metadata

    def post_export_native_dashboards(
        self, response: native_dashboard.ExportNativeDashboardsResponse
    ) -> native_dashboard.ExportNativeDashboardsResponse:
        """Post-rpc interceptor for export_native_dashboards

        DEPRECATED. Please use the `post_export_native_dashboards_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NativeDashboardService server but before
        it is returned to user code. This `post_export_native_dashboards` interceptor runs
        before the `post_export_native_dashboards_with_metadata` interceptor.
        """
        return response

    def post_export_native_dashboards_with_metadata(
        self,
        response: native_dashboard.ExportNativeDashboardsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        native_dashboard.ExportNativeDashboardsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for export_native_dashboards

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NativeDashboardService server but before it is returned to user code.

        We recommend only using this `post_export_native_dashboards_with_metadata`
        interceptor in new development instead of the `post_export_native_dashboards` interceptor.
        When both interceptors are used, this `post_export_native_dashboards_with_metadata` interceptor runs after the
        `post_export_native_dashboards` interceptor. The (possibly modified) response returned by
        `post_export_native_dashboards` will be passed to
        `post_export_native_dashboards_with_metadata`.
        """
        return response, metadata

    def pre_get_native_dashboard(
        self,
        request: native_dashboard.GetNativeDashboardRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        native_dashboard.GetNativeDashboardRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_native_dashboard

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NativeDashboardService server.
        """
        return request, metadata

    def post_get_native_dashboard(
        self, response: native_dashboard.NativeDashboard
    ) -> native_dashboard.NativeDashboard:
        """Post-rpc interceptor for get_native_dashboard

        DEPRECATED. Please use the `post_get_native_dashboard_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NativeDashboardService server but before
        it is returned to user code. This `post_get_native_dashboard` interceptor runs
        before the `post_get_native_dashboard_with_metadata` interceptor.
        """
        return response

    def post_get_native_dashboard_with_metadata(
        self,
        response: native_dashboard.NativeDashboard,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        native_dashboard.NativeDashboard, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for get_native_dashboard

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NativeDashboardService server but before it is returned to user code.

        We recommend only using this `post_get_native_dashboard_with_metadata`
        interceptor in new development instead of the `post_get_native_dashboard` interceptor.
        When both interceptors are used, this `post_get_native_dashboard_with_metadata` interceptor runs after the
        `post_get_native_dashboard` interceptor. The (possibly modified) response returned by
        `post_get_native_dashboard` will be passed to
        `post_get_native_dashboard_with_metadata`.
        """
        return response, metadata

    def pre_import_native_dashboards(
        self,
        request: native_dashboard.ImportNativeDashboardsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        native_dashboard.ImportNativeDashboardsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for import_native_dashboards

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NativeDashboardService server.
        """
        return request, metadata

    def post_import_native_dashboards(
        self, response: native_dashboard.ImportNativeDashboardsResponse
    ) -> native_dashboard.ImportNativeDashboardsResponse:
        """Post-rpc interceptor for import_native_dashboards

        DEPRECATED. Please use the `post_import_native_dashboards_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NativeDashboardService server but before
        it is returned to user code. This `post_import_native_dashboards` interceptor runs
        before the `post_import_native_dashboards_with_metadata` interceptor.
        """
        return response

    def post_import_native_dashboards_with_metadata(
        self,
        response: native_dashboard.ImportNativeDashboardsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        native_dashboard.ImportNativeDashboardsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for import_native_dashboards

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NativeDashboardService server but before it is returned to user code.

        We recommend only using this `post_import_native_dashboards_with_metadata`
        interceptor in new development instead of the `post_import_native_dashboards` interceptor.
        When both interceptors are used, this `post_import_native_dashboards_with_metadata` interceptor runs after the
        `post_import_native_dashboards` interceptor. The (possibly modified) response returned by
        `post_import_native_dashboards` will be passed to
        `post_import_native_dashboards_with_metadata`.
        """
        return response, metadata

    def pre_list_native_dashboards(
        self,
        request: native_dashboard.ListNativeDashboardsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        native_dashboard.ListNativeDashboardsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_native_dashboards

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NativeDashboardService server.
        """
        return request, metadata

    def post_list_native_dashboards(
        self, response: native_dashboard.ListNativeDashboardsResponse
    ) -> native_dashboard.ListNativeDashboardsResponse:
        """Post-rpc interceptor for list_native_dashboards

        DEPRECATED. Please use the `post_list_native_dashboards_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NativeDashboardService server but before
        it is returned to user code. This `post_list_native_dashboards` interceptor runs
        before the `post_list_native_dashboards_with_metadata` interceptor.
        """
        return response

    def post_list_native_dashboards_with_metadata(
        self,
        response: native_dashboard.ListNativeDashboardsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        native_dashboard.ListNativeDashboardsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_native_dashboards

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NativeDashboardService server but before it is returned to user code.

        We recommend only using this `post_list_native_dashboards_with_metadata`
        interceptor in new development instead of the `post_list_native_dashboards` interceptor.
        When both interceptors are used, this `post_list_native_dashboards_with_metadata` interceptor runs after the
        `post_list_native_dashboards` interceptor. The (possibly modified) response returned by
        `post_list_native_dashboards` will be passed to
        `post_list_native_dashboards_with_metadata`.
        """
        return response, metadata

    def pre_remove_chart(
        self,
        request: native_dashboard.RemoveChartRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        native_dashboard.RemoveChartRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for remove_chart

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NativeDashboardService server.
        """
        return request, metadata

    def post_remove_chart(
        self, response: native_dashboard.NativeDashboard
    ) -> native_dashboard.NativeDashboard:
        """Post-rpc interceptor for remove_chart

        DEPRECATED. Please use the `post_remove_chart_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NativeDashboardService server but before
        it is returned to user code. This `post_remove_chart` interceptor runs
        before the `post_remove_chart_with_metadata` interceptor.
        """
        return response

    def post_remove_chart_with_metadata(
        self,
        response: native_dashboard.NativeDashboard,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        native_dashboard.NativeDashboard, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for remove_chart

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NativeDashboardService server but before it is returned to user code.

        We recommend only using this `post_remove_chart_with_metadata`
        interceptor in new development instead of the `post_remove_chart` interceptor.
        When both interceptors are used, this `post_remove_chart_with_metadata` interceptor runs after the
        `post_remove_chart` interceptor. The (possibly modified) response returned by
        `post_remove_chart` will be passed to
        `post_remove_chart_with_metadata`.
        """
        return response, metadata

    def pre_update_native_dashboard(
        self,
        request: gcc_native_dashboard.UpdateNativeDashboardRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gcc_native_dashboard.UpdateNativeDashboardRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_native_dashboard

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NativeDashboardService server.
        """
        return request, metadata

    def post_update_native_dashboard(
        self, response: gcc_native_dashboard.NativeDashboard
    ) -> gcc_native_dashboard.NativeDashboard:
        """Post-rpc interceptor for update_native_dashboard

        DEPRECATED. Please use the `post_update_native_dashboard_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NativeDashboardService server but before
        it is returned to user code. This `post_update_native_dashboard` interceptor runs
        before the `post_update_native_dashboard_with_metadata` interceptor.
        """
        return response

    def post_update_native_dashboard_with_metadata(
        self,
        response: gcc_native_dashboard.NativeDashboard,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gcc_native_dashboard.NativeDashboard, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for update_native_dashboard

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NativeDashboardService server but before it is returned to user code.

        We recommend only using this `post_update_native_dashboard_with_metadata`
        interceptor in new development instead of the `post_update_native_dashboard` interceptor.
        When both interceptors are used, this `post_update_native_dashboard_with_metadata` interceptor runs after the
        `post_update_native_dashboard` interceptor. The (possibly modified) response returned by
        `post_update_native_dashboard` will be passed to
        `post_update_native_dashboard_with_metadata`.
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
        before they are sent to the NativeDashboardService server.
        """
        return request, metadata

    def post_cancel_operation(self, response: None) -> None:
        """Post-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the response
        after it is returned by the NativeDashboardService server but before
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
        before they are sent to the NativeDashboardService server.
        """
        return request, metadata

    def post_delete_operation(self, response: None) -> None:
        """Post-rpc interceptor for delete_operation

        Override in a subclass to manipulate the response
        after it is returned by the NativeDashboardService server but before
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
        before they are sent to the NativeDashboardService server.
        """
        return request, metadata

    def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the NativeDashboardService server but before
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
        before they are sent to the NativeDashboardService server.
        """
        return request, metadata

    def post_list_operations(
        self, response: operations_pb2.ListOperationsResponse
    ) -> operations_pb2.ListOperationsResponse:
        """Post-rpc interceptor for list_operations

        Override in a subclass to manipulate the response
        after it is returned by the NativeDashboardService server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class NativeDashboardServiceRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: NativeDashboardServiceRestInterceptor


class NativeDashboardServiceRestTransport(_BaseNativeDashboardServiceRestTransport):
    """REST backend synchronous transport for NativeDashboardService.

    A service providing functionality for managing native
    dashboards.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "chronicle.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[NativeDashboardServiceRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'chronicle.googleapis.com').
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
            interceptor (Optional[NativeDashboardServiceRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or NativeDashboardServiceRestInterceptor()
        self._prep_wrapped_messages(client_info)

    class _AddChart(
        _BaseNativeDashboardServiceRestTransport._BaseAddChart,
        NativeDashboardServiceRestStub,
    ):
        def __hash__(self):
            return hash("NativeDashboardServiceRestTransport.AddChart")

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
            request: native_dashboard.AddChartRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> native_dashboard.AddChartResponse:
            r"""Call the add chart method over HTTP.

            Args:
                request (~.native_dashboard.AddChartRequest):
                    The request object. Request message to add chart in a
                dashboard.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.native_dashboard.AddChartResponse:
                    Response message for adding chart in
                a dashboard.

            """

            http_options = _BaseNativeDashboardServiceRestTransport._BaseAddChart._get_http_options()
            request, metadata = self._interceptor.pre_add_chart(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNativeDashboardServiceRestTransport._BaseAddChart,
                    "_BaseAddChart__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.chronicle_v1.NativeDashboardServiceClient.AddChart",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.NativeDashboardService",
                        "rpcName": "AddChart",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NativeDashboardServiceRestTransport._AddChart._get_response(
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
            resp = native_dashboard.AddChartResponse()
            pb_resp = native_dashboard.AddChartResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_add_chart(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_add_chart_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = native_dashboard.AddChartResponse.to_json(
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
                    "Received response for google.cloud.chronicle_v1.NativeDashboardServiceClient.add_chart",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.NativeDashboardService",
                        "rpcName": "AddChart",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateNativeDashboard(
        _BaseNativeDashboardServiceRestTransport._BaseCreateNativeDashboard,
        NativeDashboardServiceRestStub,
    ):
        def __hash__(self):
            return hash("NativeDashboardServiceRestTransport.CreateNativeDashboard")

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
            request: gcc_native_dashboard.CreateNativeDashboardRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gcc_native_dashboard.NativeDashboard:
            r"""Call the create native dashboard method over HTTP.

            Args:
                request (~.gcc_native_dashboard.CreateNativeDashboardRequest):
                    The request object. Request message to create a
                dashboard.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.gcc_native_dashboard.NativeDashboard:
                    NativeDashboard resource.
            """

            http_options = _BaseNativeDashboardServiceRestTransport._BaseCreateNativeDashboard._get_http_options()
            request, metadata = self._interceptor.pre_create_native_dashboard(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNativeDashboardServiceRestTransport._BaseCreateNativeDashboard,
                    "_BaseCreateNativeDashboard__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.chronicle_v1.NativeDashboardServiceClient.CreateNativeDashboard",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.NativeDashboardService",
                        "rpcName": "CreateNativeDashboard",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NativeDashboardServiceRestTransport._CreateNativeDashboard._get_response(
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
            resp = gcc_native_dashboard.NativeDashboard()
            pb_resp = gcc_native_dashboard.NativeDashboard.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_native_dashboard(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_native_dashboard_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = gcc_native_dashboard.NativeDashboard.to_json(
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
                    "Received response for google.cloud.chronicle_v1.NativeDashboardServiceClient.create_native_dashboard",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.NativeDashboardService",
                        "rpcName": "CreateNativeDashboard",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteNativeDashboard(
        _BaseNativeDashboardServiceRestTransport._BaseDeleteNativeDashboard,
        NativeDashboardServiceRestStub,
    ):
        def __hash__(self):
            return hash("NativeDashboardServiceRestTransport.DeleteNativeDashboard")

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
            request: native_dashboard.DeleteNativeDashboardRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete native dashboard method over HTTP.

            Args:
                request (~.native_dashboard.DeleteNativeDashboardRequest):
                    The request object. Request message to delete a
                dashboard.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = _BaseNativeDashboardServiceRestTransport._BaseDeleteNativeDashboard._get_http_options()
            request, metadata = self._interceptor.pre_delete_native_dashboard(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNativeDashboardServiceRestTransport._BaseDeleteNativeDashboard,
                    "_BaseDeleteNativeDashboard__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.chronicle_v1.NativeDashboardServiceClient.DeleteNativeDashboard",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.NativeDashboardService",
                        "rpcName": "DeleteNativeDashboard",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NativeDashboardServiceRestTransport._DeleteNativeDashboard._get_response(
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

    class _DuplicateChart(
        _BaseNativeDashboardServiceRestTransport._BaseDuplicateChart,
        NativeDashboardServiceRestStub,
    ):
        def __hash__(self):
            return hash("NativeDashboardServiceRestTransport.DuplicateChart")

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
            request: native_dashboard.DuplicateChartRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> native_dashboard.DuplicateChartResponse:
            r"""Call the duplicate chart method over HTTP.

            Args:
                request (~.native_dashboard.DuplicateChartRequest):
                    The request object. Request message to duplicate chart in
                a dashboard.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.native_dashboard.DuplicateChartResponse:
                    Response message for duplicating
                chart in a dashboard.

            """

            http_options = _BaseNativeDashboardServiceRestTransport._BaseDuplicateChart._get_http_options()
            request, metadata = self._interceptor.pre_duplicate_chart(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNativeDashboardServiceRestTransport._BaseDuplicateChart,
                    "_BaseDuplicateChart__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.chronicle_v1.NativeDashboardServiceClient.DuplicateChart",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.NativeDashboardService",
                        "rpcName": "DuplicateChart",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                NativeDashboardServiceRestTransport._DuplicateChart._get_response(
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
            resp = native_dashboard.DuplicateChartResponse()
            pb_resp = native_dashboard.DuplicateChartResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_duplicate_chart(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_duplicate_chart_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = native_dashboard.DuplicateChartResponse.to_json(
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
                    "Received response for google.cloud.chronicle_v1.NativeDashboardServiceClient.duplicate_chart",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.NativeDashboardService",
                        "rpcName": "DuplicateChart",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DuplicateNativeDashboard(
        _BaseNativeDashboardServiceRestTransport._BaseDuplicateNativeDashboard,
        NativeDashboardServiceRestStub,
    ):
        def __hash__(self):
            return hash("NativeDashboardServiceRestTransport.DuplicateNativeDashboard")

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
            request: gcc_native_dashboard.DuplicateNativeDashboardRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gcc_native_dashboard.NativeDashboard:
            r"""Call the duplicate native
            dashboard method over HTTP.

                Args:
                    request (~.gcc_native_dashboard.DuplicateNativeDashboardRequest):
                        The request object. Request message to duplicate a
                    dashboard.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.gcc_native_dashboard.NativeDashboard:
                        NativeDashboard resource.
            """

            http_options = _BaseNativeDashboardServiceRestTransport._BaseDuplicateNativeDashboard._get_http_options()
            request, metadata = self._interceptor.pre_duplicate_native_dashboard(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNativeDashboardServiceRestTransport._BaseDuplicateNativeDashboard,
                    "_BaseDuplicateNativeDashboard__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.chronicle_v1.NativeDashboardServiceClient.DuplicateNativeDashboard",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.NativeDashboardService",
                        "rpcName": "DuplicateNativeDashboard",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NativeDashboardServiceRestTransport._DuplicateNativeDashboard._get_response(
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
            resp = gcc_native_dashboard.NativeDashboard()
            pb_resp = gcc_native_dashboard.NativeDashboard.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_duplicate_native_dashboard(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_duplicate_native_dashboard_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = gcc_native_dashboard.NativeDashboard.to_json(
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
                    "Received response for google.cloud.chronicle_v1.NativeDashboardServiceClient.duplicate_native_dashboard",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.NativeDashboardService",
                        "rpcName": "DuplicateNativeDashboard",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _EditChart(
        _BaseNativeDashboardServiceRestTransport._BaseEditChart,
        NativeDashboardServiceRestStub,
    ):
        def __hash__(self):
            return hash("NativeDashboardServiceRestTransport.EditChart")

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
            request: native_dashboard.EditChartRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> native_dashboard.EditChartResponse:
            r"""Call the edit chart method over HTTP.

            Args:
                request (~.native_dashboard.EditChartRequest):
                    The request object. Request message to edit chart in a
                dashboard.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.native_dashboard.EditChartResponse:
                    Response message for editing chart in
                a dashboard.

            """

            http_options = _BaseNativeDashboardServiceRestTransport._BaseEditChart._get_http_options()
            request, metadata = self._interceptor.pre_edit_chart(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNativeDashboardServiceRestTransport._BaseEditChart,
                    "_BaseEditChart__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.chronicle_v1.NativeDashboardServiceClient.EditChart",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.NativeDashboardService",
                        "rpcName": "EditChart",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NativeDashboardServiceRestTransport._EditChart._get_response(
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
            resp = native_dashboard.EditChartResponse()
            pb_resp = native_dashboard.EditChartResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_edit_chart(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_edit_chart_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = native_dashboard.EditChartResponse.to_json(
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
                    "Received response for google.cloud.chronicle_v1.NativeDashboardServiceClient.edit_chart",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.NativeDashboardService",
                        "rpcName": "EditChart",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ExportNativeDashboards(
        _BaseNativeDashboardServiceRestTransport._BaseExportNativeDashboards,
        NativeDashboardServiceRestStub,
    ):
        def __hash__(self):
            return hash("NativeDashboardServiceRestTransport.ExportNativeDashboards")

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
            request: native_dashboard.ExportNativeDashboardsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> native_dashboard.ExportNativeDashboardsResponse:
            r"""Call the export native dashboards method over HTTP.

            Args:
                request (~.native_dashboard.ExportNativeDashboardsRequest):
                    The request object. Request message to export list of
                dashboard.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.native_dashboard.ExportNativeDashboardsResponse:
                    Response message for exporting a
                dashboard.

            """

            http_options = _BaseNativeDashboardServiceRestTransport._BaseExportNativeDashboards._get_http_options()
            request, metadata = self._interceptor.pre_export_native_dashboards(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNativeDashboardServiceRestTransport._BaseExportNativeDashboards,
                    "_BaseExportNativeDashboards__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.chronicle_v1.NativeDashboardServiceClient.ExportNativeDashboards",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.NativeDashboardService",
                        "rpcName": "ExportNativeDashboards",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NativeDashboardServiceRestTransport._ExportNativeDashboards._get_response(
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
            resp = native_dashboard.ExportNativeDashboardsResponse()
            pb_resp = native_dashboard.ExportNativeDashboardsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_export_native_dashboards(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_export_native_dashboards_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        native_dashboard.ExportNativeDashboardsResponse.to_json(
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
                    "Received response for google.cloud.chronicle_v1.NativeDashboardServiceClient.export_native_dashboards",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.NativeDashboardService",
                        "rpcName": "ExportNativeDashboards",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetNativeDashboard(
        _BaseNativeDashboardServiceRestTransport._BaseGetNativeDashboard,
        NativeDashboardServiceRestStub,
    ):
        def __hash__(self):
            return hash("NativeDashboardServiceRestTransport.GetNativeDashboard")

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
            request: native_dashboard.GetNativeDashboardRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> native_dashboard.NativeDashboard:
            r"""Call the get native dashboard method over HTTP.

            Args:
                request (~.native_dashboard.GetNativeDashboardRequest):
                    The request object. Request message to get a dashboard.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.native_dashboard.NativeDashboard:
                    NativeDashboard resource.
            """

            http_options = _BaseNativeDashboardServiceRestTransport._BaseGetNativeDashboard._get_http_options()
            request, metadata = self._interceptor.pre_get_native_dashboard(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNativeDashboardServiceRestTransport._BaseGetNativeDashboard,
                    "_BaseGetNativeDashboard__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.chronicle_v1.NativeDashboardServiceClient.GetNativeDashboard",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.NativeDashboardService",
                        "rpcName": "GetNativeDashboard",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                NativeDashboardServiceRestTransport._GetNativeDashboard._get_response(
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
            resp = native_dashboard.NativeDashboard()
            pb_resp = native_dashboard.NativeDashboard.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_native_dashboard(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_native_dashboard_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = native_dashboard.NativeDashboard.to_json(
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
                    "Received response for google.cloud.chronicle_v1.NativeDashboardServiceClient.get_native_dashboard",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.NativeDashboardService",
                        "rpcName": "GetNativeDashboard",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ImportNativeDashboards(
        _BaseNativeDashboardServiceRestTransport._BaseImportNativeDashboards,
        NativeDashboardServiceRestStub,
    ):
        def __hash__(self):
            return hash("NativeDashboardServiceRestTransport.ImportNativeDashboards")

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
            request: native_dashboard.ImportNativeDashboardsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> native_dashboard.ImportNativeDashboardsResponse:
            r"""Call the import native dashboards method over HTTP.

            Args:
                request (~.native_dashboard.ImportNativeDashboardsRequest):
                    The request object. Request message to import dashboards.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.native_dashboard.ImportNativeDashboardsResponse:
                    Response message for importing
                dashboards.

            """

            http_options = _BaseNativeDashboardServiceRestTransport._BaseImportNativeDashboards._get_http_options()
            request, metadata = self._interceptor.pre_import_native_dashboards(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNativeDashboardServiceRestTransport._BaseImportNativeDashboards,
                    "_BaseImportNativeDashboards__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.chronicle_v1.NativeDashboardServiceClient.ImportNativeDashboards",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.NativeDashboardService",
                        "rpcName": "ImportNativeDashboards",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NativeDashboardServiceRestTransport._ImportNativeDashboards._get_response(
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
            resp = native_dashboard.ImportNativeDashboardsResponse()
            pb_resp = native_dashboard.ImportNativeDashboardsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_import_native_dashboards(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_import_native_dashboards_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        native_dashboard.ImportNativeDashboardsResponse.to_json(
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
                    "Received response for google.cloud.chronicle_v1.NativeDashboardServiceClient.import_native_dashboards",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.NativeDashboardService",
                        "rpcName": "ImportNativeDashboards",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListNativeDashboards(
        _BaseNativeDashboardServiceRestTransport._BaseListNativeDashboards,
        NativeDashboardServiceRestStub,
    ):
        def __hash__(self):
            return hash("NativeDashboardServiceRestTransport.ListNativeDashboards")

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
            request: native_dashboard.ListNativeDashboardsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> native_dashboard.ListNativeDashboardsResponse:
            r"""Call the list native dashboards method over HTTP.

            Args:
                request (~.native_dashboard.ListNativeDashboardsRequest):
                    The request object. Request message to list dashboards.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.native_dashboard.ListNativeDashboardsResponse:
                    Response message for listing
                dashboards.

            """

            http_options = _BaseNativeDashboardServiceRestTransport._BaseListNativeDashboards._get_http_options()
            request, metadata = self._interceptor.pre_list_native_dashboards(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNativeDashboardServiceRestTransport._BaseListNativeDashboards,
                    "_BaseListNativeDashboards__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.chronicle_v1.NativeDashboardServiceClient.ListNativeDashboards",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.NativeDashboardService",
                        "rpcName": "ListNativeDashboards",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                NativeDashboardServiceRestTransport._ListNativeDashboards._get_response(
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
            resp = native_dashboard.ListNativeDashboardsResponse()
            pb_resp = native_dashboard.ListNativeDashboardsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_native_dashboards(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_native_dashboards_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        native_dashboard.ListNativeDashboardsResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.chronicle_v1.NativeDashboardServiceClient.list_native_dashboards",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.NativeDashboardService",
                        "rpcName": "ListNativeDashboards",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _RemoveChart(
        _BaseNativeDashboardServiceRestTransport._BaseRemoveChart,
        NativeDashboardServiceRestStub,
    ):
        def __hash__(self):
            return hash("NativeDashboardServiceRestTransport.RemoveChart")

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
            request: native_dashboard.RemoveChartRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> native_dashboard.NativeDashboard:
            r"""Call the remove chart method over HTTP.

            Args:
                request (~.native_dashboard.RemoveChartRequest):
                    The request object. Request message to remove chart from
                a dashboard.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.native_dashboard.NativeDashboard:
                    NativeDashboard resource.
            """

            http_options = _BaseNativeDashboardServiceRestTransport._BaseRemoveChart._get_http_options()
            request, metadata = self._interceptor.pre_remove_chart(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNativeDashboardServiceRestTransport._BaseRemoveChart,
                    "_BaseRemoveChart__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.chronicle_v1.NativeDashboardServiceClient.RemoveChart",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.NativeDashboardService",
                        "rpcName": "RemoveChart",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NativeDashboardServiceRestTransport._RemoveChart._get_response(
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
            resp = native_dashboard.NativeDashboard()
            pb_resp = native_dashboard.NativeDashboard.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_remove_chart(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_remove_chart_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = native_dashboard.NativeDashboard.to_json(
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
                    "Received response for google.cloud.chronicle_v1.NativeDashboardServiceClient.remove_chart",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.NativeDashboardService",
                        "rpcName": "RemoveChart",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateNativeDashboard(
        _BaseNativeDashboardServiceRestTransport._BaseUpdateNativeDashboard,
        NativeDashboardServiceRestStub,
    ):
        def __hash__(self):
            return hash("NativeDashboardServiceRestTransport.UpdateNativeDashboard")

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
            request: gcc_native_dashboard.UpdateNativeDashboardRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gcc_native_dashboard.NativeDashboard:
            r"""Call the update native dashboard method over HTTP.

            Args:
                request (~.gcc_native_dashboard.UpdateNativeDashboardRequest):
                    The request object. Request message to update a
                dashboard.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.gcc_native_dashboard.NativeDashboard:
                    NativeDashboard resource.
            """

            http_options = _BaseNativeDashboardServiceRestTransport._BaseUpdateNativeDashboard._get_http_options()
            request, metadata = self._interceptor.pre_update_native_dashboard(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNativeDashboardServiceRestTransport._BaseUpdateNativeDashboard,
                    "_BaseUpdateNativeDashboard__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.chronicle_v1.NativeDashboardServiceClient.UpdateNativeDashboard",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.NativeDashboardService",
                        "rpcName": "UpdateNativeDashboard",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NativeDashboardServiceRestTransport._UpdateNativeDashboard._get_response(
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
            resp = gcc_native_dashboard.NativeDashboard()
            pb_resp = gcc_native_dashboard.NativeDashboard.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_native_dashboard(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_native_dashboard_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = gcc_native_dashboard.NativeDashboard.to_json(
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
                    "Received response for google.cloud.chronicle_v1.NativeDashboardServiceClient.update_native_dashboard",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.NativeDashboardService",
                        "rpcName": "UpdateNativeDashboard",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def add_chart(
        self,
    ) -> Callable[
        [native_dashboard.AddChartRequest], native_dashboard.AddChartResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._AddChart(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_native_dashboard(
        self,
    ) -> Callable[
        [gcc_native_dashboard.CreateNativeDashboardRequest],
        gcc_native_dashboard.NativeDashboard,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateNativeDashboard(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_native_dashboard(
        self,
    ) -> Callable[[native_dashboard.DeleteNativeDashboardRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteNativeDashboard(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def duplicate_chart(
        self,
    ) -> Callable[
        [native_dashboard.DuplicateChartRequest],
        native_dashboard.DuplicateChartResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DuplicateChart(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def duplicate_native_dashboard(
        self,
    ) -> Callable[
        [gcc_native_dashboard.DuplicateNativeDashboardRequest],
        gcc_native_dashboard.NativeDashboard,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DuplicateNativeDashboard(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def edit_chart(
        self,
    ) -> Callable[
        [native_dashboard.EditChartRequest], native_dashboard.EditChartResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._EditChart(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def export_native_dashboards(
        self,
    ) -> Callable[
        [native_dashboard.ExportNativeDashboardsRequest],
        native_dashboard.ExportNativeDashboardsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ExportNativeDashboards(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def get_native_dashboard(
        self,
    ) -> Callable[
        [native_dashboard.GetNativeDashboardRequest], native_dashboard.NativeDashboard
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetNativeDashboard(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def import_native_dashboards(
        self,
    ) -> Callable[
        [native_dashboard.ImportNativeDashboardsRequest],
        native_dashboard.ImportNativeDashboardsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ImportNativeDashboards(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def list_native_dashboards(
        self,
    ) -> Callable[
        [native_dashboard.ListNativeDashboardsRequest],
        native_dashboard.ListNativeDashboardsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListNativeDashboards(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def remove_chart(
        self,
    ) -> Callable[
        [native_dashboard.RemoveChartRequest], native_dashboard.NativeDashboard
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._RemoveChart(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_native_dashboard(
        self,
    ) -> Callable[
        [gcc_native_dashboard.UpdateNativeDashboardRequest],
        gcc_native_dashboard.NativeDashboard,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateNativeDashboard(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def cancel_operation(self):
        return self._CancelOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _CancelOperation(
        _BaseNativeDashboardServiceRestTransport._BaseCancelOperation,
        NativeDashboardServiceRestStub,
    ):
        def __hash__(self):
            return hash("NativeDashboardServiceRestTransport.CancelOperation")

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

            http_options = _BaseNativeDashboardServiceRestTransport._BaseCancelOperation._get_http_options()
            request, metadata = self._interceptor.pre_cancel_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNativeDashboardServiceRestTransport._BaseCancelOperation,
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
                    f"Sending request for google.cloud.chronicle_v1.NativeDashboardServiceClient.CancelOperation",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.NativeDashboardService",
                        "rpcName": "CancelOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                NativeDashboardServiceRestTransport._CancelOperation._get_response(
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

            return self._interceptor.post_cancel_operation(None)

    @property
    def delete_operation(self):
        return self._DeleteOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _DeleteOperation(
        _BaseNativeDashboardServiceRestTransport._BaseDeleteOperation,
        NativeDashboardServiceRestStub,
    ):
        def __hash__(self):
            return hash("NativeDashboardServiceRestTransport.DeleteOperation")

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

            http_options = _BaseNativeDashboardServiceRestTransport._BaseDeleteOperation._get_http_options()
            request, metadata = self._interceptor.pre_delete_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNativeDashboardServiceRestTransport._BaseDeleteOperation,
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
                    f"Sending request for google.cloud.chronicle_v1.NativeDashboardServiceClient.DeleteOperation",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.NativeDashboardService",
                        "rpcName": "DeleteOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                NativeDashboardServiceRestTransport._DeleteOperation._get_response(
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

            return self._interceptor.post_delete_operation(None)

    @property
    def get_operation(self):
        return self._GetOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetOperation(
        _BaseNativeDashboardServiceRestTransport._BaseGetOperation,
        NativeDashboardServiceRestStub,
    ):
        def __hash__(self):
            return hash("NativeDashboardServiceRestTransport.GetOperation")

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

            http_options = _BaseNativeDashboardServiceRestTransport._BaseGetOperation._get_http_options()
            request, metadata = self._interceptor.pre_get_operation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNativeDashboardServiceRestTransport._BaseGetOperation,
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
                    f"Sending request for google.cloud.chronicle_v1.NativeDashboardServiceClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.NativeDashboardService",
                        "rpcName": "GetOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NativeDashboardServiceRestTransport._GetOperation._get_response(
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
                    "Received response for google.cloud.chronicle_v1.NativeDashboardServiceAsyncClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.NativeDashboardService",
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
        _BaseNativeDashboardServiceRestTransport._BaseListOperations,
        NativeDashboardServiceRestStub,
    ):
        def __hash__(self):
            return hash("NativeDashboardServiceRestTransport.ListOperations")

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

            http_options = _BaseNativeDashboardServiceRestTransport._BaseListOperations._get_http_options()
            request, metadata = self._interceptor.pre_list_operations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNativeDashboardServiceRestTransport._BaseListOperations,
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
                    f"Sending request for google.cloud.chronicle_v1.NativeDashboardServiceClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.NativeDashboardService",
                        "rpcName": "ListOperations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                NativeDashboardServiceRestTransport._ListOperations._get_response(
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
                    "Received response for google.cloud.chronicle_v1.NativeDashboardServiceAsyncClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.NativeDashboardService",
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


__all__ = ("NativeDashboardServiceRestTransport",)
