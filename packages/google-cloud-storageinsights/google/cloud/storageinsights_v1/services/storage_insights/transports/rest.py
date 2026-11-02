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
from google.api_core import gapic_v1, operations_v1, rest_helpers, rest_streaming
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.auth.transport.requests import AuthorizedSession  # type: ignore
from google.cloud.location import locations_pb2  # type: ignore
from google.longrunning import operations_pb2  # type: ignore
from google.protobuf import json_format
from requests import __version__ as requests_version

from google.cloud.storageinsights_v1._compat import transcode_request
from google.cloud.storageinsights_v1.types import storageinsights

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseStorageInsightsRestTransport

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


class StorageInsightsRestInterceptor:
    """Interceptor for StorageInsights.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the StorageInsightsRestTransport.

    .. code-block:: python
        class MyCustomStorageInsightsInterceptor(StorageInsightsRestInterceptor):
            def pre_create_dataset_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_dataset_config(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_report_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_report_config(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_dataset_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_dataset_config(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_report_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_get_dataset_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_dataset_config(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_report_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_report_config(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_report_detail(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_report_detail(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_link_dataset(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_link_dataset(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_dataset_configs(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_dataset_configs(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_report_configs(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_report_configs(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_report_details(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_report_details(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_unlink_dataset(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_unlink_dataset(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_dataset_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_dataset_config(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_report_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_report_config(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = StorageInsightsRestTransport(interceptor=MyCustomStorageInsightsInterceptor())
        client = StorageInsightsClient(transport=transport)


    """

    def pre_create_dataset_config(
        self,
        request: storageinsights.CreateDatasetConfigRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        storageinsights.CreateDatasetConfigRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_dataset_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the StorageInsights server.
        """
        return request, metadata

    def post_create_dataset_config(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_dataset_config

        DEPRECATED. Please use the `post_create_dataset_config_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the StorageInsights server but before
        it is returned to user code. This `post_create_dataset_config` interceptor runs
        before the `post_create_dataset_config_with_metadata` interceptor.
        """
        return response

    def post_create_dataset_config_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_dataset_config

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the StorageInsights server but before it is returned to user code.

        We recommend only using this `post_create_dataset_config_with_metadata`
        interceptor in new development instead of the `post_create_dataset_config` interceptor.
        When both interceptors are used, this `post_create_dataset_config_with_metadata` interceptor runs after the
        `post_create_dataset_config` interceptor. The (possibly modified) response returned by
        `post_create_dataset_config` will be passed to
        `post_create_dataset_config_with_metadata`.
        """
        return response, metadata

    def pre_create_report_config(
        self,
        request: storageinsights.CreateReportConfigRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        storageinsights.CreateReportConfigRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_report_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the StorageInsights server.
        """
        return request, metadata

    def post_create_report_config(
        self, response: storageinsights.ReportConfig
    ) -> storageinsights.ReportConfig:
        """Post-rpc interceptor for create_report_config

        DEPRECATED. Please use the `post_create_report_config_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the StorageInsights server but before
        it is returned to user code. This `post_create_report_config` interceptor runs
        before the `post_create_report_config_with_metadata` interceptor.
        """
        return response

    def post_create_report_config_with_metadata(
        self,
        response: storageinsights.ReportConfig,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[storageinsights.ReportConfig, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_report_config

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the StorageInsights server but before it is returned to user code.

        We recommend only using this `post_create_report_config_with_metadata`
        interceptor in new development instead of the `post_create_report_config` interceptor.
        When both interceptors are used, this `post_create_report_config_with_metadata` interceptor runs after the
        `post_create_report_config` interceptor. The (possibly modified) response returned by
        `post_create_report_config` will be passed to
        `post_create_report_config_with_metadata`.
        """
        return response, metadata

    def pre_delete_dataset_config(
        self,
        request: storageinsights.DeleteDatasetConfigRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        storageinsights.DeleteDatasetConfigRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_dataset_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the StorageInsights server.
        """
        return request, metadata

    def post_delete_dataset_config(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_dataset_config

        DEPRECATED. Please use the `post_delete_dataset_config_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the StorageInsights server but before
        it is returned to user code. This `post_delete_dataset_config` interceptor runs
        before the `post_delete_dataset_config_with_metadata` interceptor.
        """
        return response

    def post_delete_dataset_config_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_dataset_config

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the StorageInsights server but before it is returned to user code.

        We recommend only using this `post_delete_dataset_config_with_metadata`
        interceptor in new development instead of the `post_delete_dataset_config` interceptor.
        When both interceptors are used, this `post_delete_dataset_config_with_metadata` interceptor runs after the
        `post_delete_dataset_config` interceptor. The (possibly modified) response returned by
        `post_delete_dataset_config` will be passed to
        `post_delete_dataset_config_with_metadata`.
        """
        return response, metadata

    def pre_delete_report_config(
        self,
        request: storageinsights.DeleteReportConfigRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        storageinsights.DeleteReportConfigRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_report_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the StorageInsights server.
        """
        return request, metadata

    def pre_get_dataset_config(
        self,
        request: storageinsights.GetDatasetConfigRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        storageinsights.GetDatasetConfigRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_dataset_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the StorageInsights server.
        """
        return request, metadata

    def post_get_dataset_config(
        self, response: storageinsights.DatasetConfig
    ) -> storageinsights.DatasetConfig:
        """Post-rpc interceptor for get_dataset_config

        DEPRECATED. Please use the `post_get_dataset_config_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the StorageInsights server but before
        it is returned to user code. This `post_get_dataset_config` interceptor runs
        before the `post_get_dataset_config_with_metadata` interceptor.
        """
        return response

    def post_get_dataset_config_with_metadata(
        self,
        response: storageinsights.DatasetConfig,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[storageinsights.DatasetConfig, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_dataset_config

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the StorageInsights server but before it is returned to user code.

        We recommend only using this `post_get_dataset_config_with_metadata`
        interceptor in new development instead of the `post_get_dataset_config` interceptor.
        When both interceptors are used, this `post_get_dataset_config_with_metadata` interceptor runs after the
        `post_get_dataset_config` interceptor. The (possibly modified) response returned by
        `post_get_dataset_config` will be passed to
        `post_get_dataset_config_with_metadata`.
        """
        return response, metadata

    def pre_get_report_config(
        self,
        request: storageinsights.GetReportConfigRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        storageinsights.GetReportConfigRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_report_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the StorageInsights server.
        """
        return request, metadata

    def post_get_report_config(
        self, response: storageinsights.ReportConfig
    ) -> storageinsights.ReportConfig:
        """Post-rpc interceptor for get_report_config

        DEPRECATED. Please use the `post_get_report_config_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the StorageInsights server but before
        it is returned to user code. This `post_get_report_config` interceptor runs
        before the `post_get_report_config_with_metadata` interceptor.
        """
        return response

    def post_get_report_config_with_metadata(
        self,
        response: storageinsights.ReportConfig,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[storageinsights.ReportConfig, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_report_config

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the StorageInsights server but before it is returned to user code.

        We recommend only using this `post_get_report_config_with_metadata`
        interceptor in new development instead of the `post_get_report_config` interceptor.
        When both interceptors are used, this `post_get_report_config_with_metadata` interceptor runs after the
        `post_get_report_config` interceptor. The (possibly modified) response returned by
        `post_get_report_config` will be passed to
        `post_get_report_config_with_metadata`.
        """
        return response, metadata

    def pre_get_report_detail(
        self,
        request: storageinsights.GetReportDetailRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        storageinsights.GetReportDetailRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_report_detail

        Override in a subclass to manipulate the request or metadata
        before they are sent to the StorageInsights server.
        """
        return request, metadata

    def post_get_report_detail(
        self, response: storageinsights.ReportDetail
    ) -> storageinsights.ReportDetail:
        """Post-rpc interceptor for get_report_detail

        DEPRECATED. Please use the `post_get_report_detail_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the StorageInsights server but before
        it is returned to user code. This `post_get_report_detail` interceptor runs
        before the `post_get_report_detail_with_metadata` interceptor.
        """
        return response

    def post_get_report_detail_with_metadata(
        self,
        response: storageinsights.ReportDetail,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[storageinsights.ReportDetail, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_report_detail

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the StorageInsights server but before it is returned to user code.

        We recommend only using this `post_get_report_detail_with_metadata`
        interceptor in new development instead of the `post_get_report_detail` interceptor.
        When both interceptors are used, this `post_get_report_detail_with_metadata` interceptor runs after the
        `post_get_report_detail` interceptor. The (possibly modified) response returned by
        `post_get_report_detail` will be passed to
        `post_get_report_detail_with_metadata`.
        """
        return response, metadata

    def pre_link_dataset(
        self,
        request: storageinsights.LinkDatasetRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        storageinsights.LinkDatasetRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for link_dataset

        Override in a subclass to manipulate the request or metadata
        before they are sent to the StorageInsights server.
        """
        return request, metadata

    def post_link_dataset(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for link_dataset

        DEPRECATED. Please use the `post_link_dataset_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the StorageInsights server but before
        it is returned to user code. This `post_link_dataset` interceptor runs
        before the `post_link_dataset_with_metadata` interceptor.
        """
        return response

    def post_link_dataset_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for link_dataset

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the StorageInsights server but before it is returned to user code.

        We recommend only using this `post_link_dataset_with_metadata`
        interceptor in new development instead of the `post_link_dataset` interceptor.
        When both interceptors are used, this `post_link_dataset_with_metadata` interceptor runs after the
        `post_link_dataset` interceptor. The (possibly modified) response returned by
        `post_link_dataset` will be passed to
        `post_link_dataset_with_metadata`.
        """
        return response, metadata

    def pre_list_dataset_configs(
        self,
        request: storageinsights.ListDatasetConfigsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        storageinsights.ListDatasetConfigsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_dataset_configs

        Override in a subclass to manipulate the request or metadata
        before they are sent to the StorageInsights server.
        """
        return request, metadata

    def post_list_dataset_configs(
        self, response: storageinsights.ListDatasetConfigsResponse
    ) -> storageinsights.ListDatasetConfigsResponse:
        """Post-rpc interceptor for list_dataset_configs

        DEPRECATED. Please use the `post_list_dataset_configs_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the StorageInsights server but before
        it is returned to user code. This `post_list_dataset_configs` interceptor runs
        before the `post_list_dataset_configs_with_metadata` interceptor.
        """
        return response

    def post_list_dataset_configs_with_metadata(
        self,
        response: storageinsights.ListDatasetConfigsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        storageinsights.ListDatasetConfigsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_dataset_configs

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the StorageInsights server but before it is returned to user code.

        We recommend only using this `post_list_dataset_configs_with_metadata`
        interceptor in new development instead of the `post_list_dataset_configs` interceptor.
        When both interceptors are used, this `post_list_dataset_configs_with_metadata` interceptor runs after the
        `post_list_dataset_configs` interceptor. The (possibly modified) response returned by
        `post_list_dataset_configs` will be passed to
        `post_list_dataset_configs_with_metadata`.
        """
        return response, metadata

    def pre_list_report_configs(
        self,
        request: storageinsights.ListReportConfigsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        storageinsights.ListReportConfigsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_report_configs

        Override in a subclass to manipulate the request or metadata
        before they are sent to the StorageInsights server.
        """
        return request, metadata

    def post_list_report_configs(
        self, response: storageinsights.ListReportConfigsResponse
    ) -> storageinsights.ListReportConfigsResponse:
        """Post-rpc interceptor for list_report_configs

        DEPRECATED. Please use the `post_list_report_configs_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the StorageInsights server but before
        it is returned to user code. This `post_list_report_configs` interceptor runs
        before the `post_list_report_configs_with_metadata` interceptor.
        """
        return response

    def post_list_report_configs_with_metadata(
        self,
        response: storageinsights.ListReportConfigsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        storageinsights.ListReportConfigsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_report_configs

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the StorageInsights server but before it is returned to user code.

        We recommend only using this `post_list_report_configs_with_metadata`
        interceptor in new development instead of the `post_list_report_configs` interceptor.
        When both interceptors are used, this `post_list_report_configs_with_metadata` interceptor runs after the
        `post_list_report_configs` interceptor. The (possibly modified) response returned by
        `post_list_report_configs` will be passed to
        `post_list_report_configs_with_metadata`.
        """
        return response, metadata

    def pre_list_report_details(
        self,
        request: storageinsights.ListReportDetailsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        storageinsights.ListReportDetailsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_report_details

        Override in a subclass to manipulate the request or metadata
        before they are sent to the StorageInsights server.
        """
        return request, metadata

    def post_list_report_details(
        self, response: storageinsights.ListReportDetailsResponse
    ) -> storageinsights.ListReportDetailsResponse:
        """Post-rpc interceptor for list_report_details

        DEPRECATED. Please use the `post_list_report_details_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the StorageInsights server but before
        it is returned to user code. This `post_list_report_details` interceptor runs
        before the `post_list_report_details_with_metadata` interceptor.
        """
        return response

    def post_list_report_details_with_metadata(
        self,
        response: storageinsights.ListReportDetailsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        storageinsights.ListReportDetailsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_report_details

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the StorageInsights server but before it is returned to user code.

        We recommend only using this `post_list_report_details_with_metadata`
        interceptor in new development instead of the `post_list_report_details` interceptor.
        When both interceptors are used, this `post_list_report_details_with_metadata` interceptor runs after the
        `post_list_report_details` interceptor. The (possibly modified) response returned by
        `post_list_report_details` will be passed to
        `post_list_report_details_with_metadata`.
        """
        return response, metadata

    def pre_unlink_dataset(
        self,
        request: storageinsights.UnlinkDatasetRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        storageinsights.UnlinkDatasetRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for unlink_dataset

        Override in a subclass to manipulate the request or metadata
        before they are sent to the StorageInsights server.
        """
        return request, metadata

    def post_unlink_dataset(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for unlink_dataset

        DEPRECATED. Please use the `post_unlink_dataset_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the StorageInsights server but before
        it is returned to user code. This `post_unlink_dataset` interceptor runs
        before the `post_unlink_dataset_with_metadata` interceptor.
        """
        return response

    def post_unlink_dataset_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for unlink_dataset

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the StorageInsights server but before it is returned to user code.

        We recommend only using this `post_unlink_dataset_with_metadata`
        interceptor in new development instead of the `post_unlink_dataset` interceptor.
        When both interceptors are used, this `post_unlink_dataset_with_metadata` interceptor runs after the
        `post_unlink_dataset` interceptor. The (possibly modified) response returned by
        `post_unlink_dataset` will be passed to
        `post_unlink_dataset_with_metadata`.
        """
        return response, metadata

    def pre_update_dataset_config(
        self,
        request: storageinsights.UpdateDatasetConfigRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        storageinsights.UpdateDatasetConfigRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_dataset_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the StorageInsights server.
        """
        return request, metadata

    def post_update_dataset_config(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_dataset_config

        DEPRECATED. Please use the `post_update_dataset_config_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the StorageInsights server but before
        it is returned to user code. This `post_update_dataset_config` interceptor runs
        before the `post_update_dataset_config_with_metadata` interceptor.
        """
        return response

    def post_update_dataset_config_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_dataset_config

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the StorageInsights server but before it is returned to user code.

        We recommend only using this `post_update_dataset_config_with_metadata`
        interceptor in new development instead of the `post_update_dataset_config` interceptor.
        When both interceptors are used, this `post_update_dataset_config_with_metadata` interceptor runs after the
        `post_update_dataset_config` interceptor. The (possibly modified) response returned by
        `post_update_dataset_config` will be passed to
        `post_update_dataset_config_with_metadata`.
        """
        return response, metadata

    def pre_update_report_config(
        self,
        request: storageinsights.UpdateReportConfigRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        storageinsights.UpdateReportConfigRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_report_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the StorageInsights server.
        """
        return request, metadata

    def post_update_report_config(
        self, response: storageinsights.ReportConfig
    ) -> storageinsights.ReportConfig:
        """Post-rpc interceptor for update_report_config

        DEPRECATED. Please use the `post_update_report_config_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the StorageInsights server but before
        it is returned to user code. This `post_update_report_config` interceptor runs
        before the `post_update_report_config_with_metadata` interceptor.
        """
        return response

    def post_update_report_config_with_metadata(
        self,
        response: storageinsights.ReportConfig,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[storageinsights.ReportConfig, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_report_config

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the StorageInsights server but before it is returned to user code.

        We recommend only using this `post_update_report_config_with_metadata`
        interceptor in new development instead of the `post_update_report_config` interceptor.
        When both interceptors are used, this `post_update_report_config_with_metadata` interceptor runs after the
        `post_update_report_config` interceptor. The (possibly modified) response returned by
        `post_update_report_config` will be passed to
        `post_update_report_config_with_metadata`.
        """
        return response, metadata

    def pre_get_location(
        self,
        request: locations_pb2.GetLocationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        locations_pb2.GetLocationRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_location

        Override in a subclass to manipulate the request or metadata
        before they are sent to the StorageInsights server.
        """
        return request, metadata

    def post_get_location(
        self, response: locations_pb2.Location
    ) -> locations_pb2.Location:
        """Post-rpc interceptor for get_location

        Override in a subclass to manipulate the response
        after it is returned by the StorageInsights server but before
        it is returned to user code.
        """
        return response

    def pre_list_locations(
        self,
        request: locations_pb2.ListLocationsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        locations_pb2.ListLocationsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_locations

        Override in a subclass to manipulate the request or metadata
        before they are sent to the StorageInsights server.
        """
        return request, metadata

    def post_list_locations(
        self, response: locations_pb2.ListLocationsResponse
    ) -> locations_pb2.ListLocationsResponse:
        """Post-rpc interceptor for list_locations

        Override in a subclass to manipulate the response
        after it is returned by the StorageInsights server but before
        it is returned to user code.
        """
        return response

    def pre_cancel_operation(
        self,
        request: operations_pb2.CancelOperationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        operations_pb2.CancelOperationRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the StorageInsights server.
        """
        return request, metadata

    def post_cancel_operation(self, response: None) -> None:
        """Post-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the response
        after it is returned by the StorageInsights server but before
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
        before they are sent to the StorageInsights server.
        """
        return request, metadata

    def post_delete_operation(self, response: None) -> None:
        """Post-rpc interceptor for delete_operation

        Override in a subclass to manipulate the response
        after it is returned by the StorageInsights server but before
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
        before they are sent to the StorageInsights server.
        """
        return request, metadata

    def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the StorageInsights server but before
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
        before they are sent to the StorageInsights server.
        """
        return request, metadata

    def post_list_operations(
        self, response: operations_pb2.ListOperationsResponse
    ) -> operations_pb2.ListOperationsResponse:
        """Post-rpc interceptor for list_operations

        Override in a subclass to manipulate the response
        after it is returned by the StorageInsights server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class StorageInsightsRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: StorageInsightsRestInterceptor


class StorageInsightsRestTransport(_BaseStorageInsightsRestTransport):
    """REST backend synchronous transport for StorageInsights.

    Service describing handlers for resources

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "storageinsights.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[StorageInsightsRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'storageinsights.googleapis.com').
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
            interceptor (Optional[StorageInsightsRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or StorageInsightsRestInterceptor()
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

    class _CreateDatasetConfig(
        _BaseStorageInsightsRestTransport._BaseCreateDatasetConfig,
        StorageInsightsRestStub,
    ):
        def __hash__(self):
            return hash("StorageInsightsRestTransport.CreateDatasetConfig")

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
            request: storageinsights.CreateDatasetConfigRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create dataset config method over HTTP.

            Args:
                request (~.storageinsights.CreateDatasetConfigRequest):
                    The request object. Request message for
                [``CreateDatasetConfig``][google.cloud.storageinsights.v1.StorageInsights.CreateDatasetConfig]
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

            http_options = _BaseStorageInsightsRestTransport._BaseCreateDatasetConfig._get_http_options()
            request, metadata = self._interceptor.pre_create_dataset_config(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseStorageInsightsRestTransport._BaseCreateDatasetConfig,
                    "_BaseCreateDatasetConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.storageinsights_v1.StorageInsightsClient.CreateDatasetConfig",
                    extra={
                        "serviceName": "google.cloud.storageinsights.v1.StorageInsights",
                        "rpcName": "CreateDatasetConfig",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = StorageInsightsRestTransport._CreateDatasetConfig._get_response(
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

            resp = self._interceptor.post_create_dataset_config(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_dataset_config_with_metadata(
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
                    "Received response for google.cloud.storageinsights_v1.StorageInsightsClient.create_dataset_config",
                    extra={
                        "serviceName": "google.cloud.storageinsights.v1.StorageInsights",
                        "rpcName": "CreateDatasetConfig",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateReportConfig(
        _BaseStorageInsightsRestTransport._BaseCreateReportConfig,
        StorageInsightsRestStub,
    ):
        def __hash__(self):
            return hash("StorageInsightsRestTransport.CreateReportConfig")

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
            request: storageinsights.CreateReportConfigRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> storageinsights.ReportConfig:
            r"""Call the create report config method over HTTP.

            Args:
                request (~.storageinsights.CreateReportConfigRequest):
                    The request object. Message for creating a ReportConfig
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.storageinsights.ReportConfig:
                    Message describing ReportConfig
                object. ReportConfig is the
                configuration to generate reports. See
                https://cloud.google.com/storage/docs/insights/using-inventory-reports#create-config-rest
                for more details on how to set various
                fields. Next ID: 12

            """

            http_options = _BaseStorageInsightsRestTransport._BaseCreateReportConfig._get_http_options()
            request, metadata = self._interceptor.pre_create_report_config(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseStorageInsightsRestTransport._BaseCreateReportConfig,
                    "_BaseCreateReportConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.storageinsights_v1.StorageInsightsClient.CreateReportConfig",
                    extra={
                        "serviceName": "google.cloud.storageinsights.v1.StorageInsights",
                        "rpcName": "CreateReportConfig",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = StorageInsightsRestTransport._CreateReportConfig._get_response(
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
            resp = storageinsights.ReportConfig()
            pb_resp = storageinsights.ReportConfig.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_report_config(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_report_config_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = storageinsights.ReportConfig.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.storageinsights_v1.StorageInsightsClient.create_report_config",
                    extra={
                        "serviceName": "google.cloud.storageinsights.v1.StorageInsights",
                        "rpcName": "CreateReportConfig",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteDatasetConfig(
        _BaseStorageInsightsRestTransport._BaseDeleteDatasetConfig,
        StorageInsightsRestStub,
    ):
        def __hash__(self):
            return hash("StorageInsightsRestTransport.DeleteDatasetConfig")

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
            request: storageinsights.DeleteDatasetConfigRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete dataset config method over HTTP.

            Args:
                request (~.storageinsights.DeleteDatasetConfigRequest):
                    The request object. Request message for
                [``DeleteDatasetConfig``][google.cloud.storageinsights.v1.StorageInsights.DeleteDatasetConfig]
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

            http_options = _BaseStorageInsightsRestTransport._BaseDeleteDatasetConfig._get_http_options()
            request, metadata = self._interceptor.pre_delete_dataset_config(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseStorageInsightsRestTransport._BaseDeleteDatasetConfig,
                    "_BaseDeleteDatasetConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.storageinsights_v1.StorageInsightsClient.DeleteDatasetConfig",
                    extra={
                        "serviceName": "google.cloud.storageinsights.v1.StorageInsights",
                        "rpcName": "DeleteDatasetConfig",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = StorageInsightsRestTransport._DeleteDatasetConfig._get_response(
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

            resp = self._interceptor.post_delete_dataset_config(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_dataset_config_with_metadata(
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
                    "Received response for google.cloud.storageinsights_v1.StorageInsightsClient.delete_dataset_config",
                    extra={
                        "serviceName": "google.cloud.storageinsights.v1.StorageInsights",
                        "rpcName": "DeleteDatasetConfig",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteReportConfig(
        _BaseStorageInsightsRestTransport._BaseDeleteReportConfig,
        StorageInsightsRestStub,
    ):
        def __hash__(self):
            return hash("StorageInsightsRestTransport.DeleteReportConfig")

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
            request: storageinsights.DeleteReportConfigRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete report config method over HTTP.

            Args:
                request (~.storageinsights.DeleteReportConfigRequest):
                    The request object. Message for deleting a ReportConfig
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = _BaseStorageInsightsRestTransport._BaseDeleteReportConfig._get_http_options()
            request, metadata = self._interceptor.pre_delete_report_config(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseStorageInsightsRestTransport._BaseDeleteReportConfig,
                    "_BaseDeleteReportConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.storageinsights_v1.StorageInsightsClient.DeleteReportConfig",
                    extra={
                        "serviceName": "google.cloud.storageinsights.v1.StorageInsights",
                        "rpcName": "DeleteReportConfig",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = StorageInsightsRestTransport._DeleteReportConfig._get_response(
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

    class _GetDatasetConfig(
        _BaseStorageInsightsRestTransport._BaseGetDatasetConfig, StorageInsightsRestStub
    ):
        def __hash__(self):
            return hash("StorageInsightsRestTransport.GetDatasetConfig")

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
            request: storageinsights.GetDatasetConfigRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> storageinsights.DatasetConfig:
            r"""Call the get dataset config method over HTTP.

            Args:
                request (~.storageinsights.GetDatasetConfigRequest):
                    The request object. Request message for
                [``GetDatasetConfig``][google.cloud.storageinsights.v1.StorageInsights.GetDatasetConfig]
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.storageinsights.DatasetConfig:
                    Message describing the dataset configuration properties.
                For more information, see `Dataset configuration
                properties <https://cloud.google.com/storage/docs/insights/datasets#dataset-config>`__.

            """

            http_options = _BaseStorageInsightsRestTransport._BaseGetDatasetConfig._get_http_options()
            request, metadata = self._interceptor.pre_get_dataset_config(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseStorageInsightsRestTransport._BaseGetDatasetConfig,
                    "_BaseGetDatasetConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.storageinsights_v1.StorageInsightsClient.GetDatasetConfig",
                    extra={
                        "serviceName": "google.cloud.storageinsights.v1.StorageInsights",
                        "rpcName": "GetDatasetConfig",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = StorageInsightsRestTransport._GetDatasetConfig._get_response(
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
            resp = storageinsights.DatasetConfig()
            pb_resp = storageinsights.DatasetConfig.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_dataset_config(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_dataset_config_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = storageinsights.DatasetConfig.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.storageinsights_v1.StorageInsightsClient.get_dataset_config",
                    extra={
                        "serviceName": "google.cloud.storageinsights.v1.StorageInsights",
                        "rpcName": "GetDatasetConfig",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetReportConfig(
        _BaseStorageInsightsRestTransport._BaseGetReportConfig, StorageInsightsRestStub
    ):
        def __hash__(self):
            return hash("StorageInsightsRestTransport.GetReportConfig")

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
            request: storageinsights.GetReportConfigRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> storageinsights.ReportConfig:
            r"""Call the get report config method over HTTP.

            Args:
                request (~.storageinsights.GetReportConfigRequest):
                    The request object. Message for getting a ReportConfig
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.storageinsights.ReportConfig:
                    Message describing ReportConfig
                object. ReportConfig is the
                configuration to generate reports. See
                https://cloud.google.com/storage/docs/insights/using-inventory-reports#create-config-rest
                for more details on how to set various
                fields. Next ID: 12

            """

            http_options = _BaseStorageInsightsRestTransport._BaseGetReportConfig._get_http_options()
            request, metadata = self._interceptor.pre_get_report_config(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseStorageInsightsRestTransport._BaseGetReportConfig,
                    "_BaseGetReportConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.storageinsights_v1.StorageInsightsClient.GetReportConfig",
                    extra={
                        "serviceName": "google.cloud.storageinsights.v1.StorageInsights",
                        "rpcName": "GetReportConfig",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = StorageInsightsRestTransport._GetReportConfig._get_response(
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
            resp = storageinsights.ReportConfig()
            pb_resp = storageinsights.ReportConfig.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_report_config(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_report_config_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = storageinsights.ReportConfig.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.storageinsights_v1.StorageInsightsClient.get_report_config",
                    extra={
                        "serviceName": "google.cloud.storageinsights.v1.StorageInsights",
                        "rpcName": "GetReportConfig",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetReportDetail(
        _BaseStorageInsightsRestTransport._BaseGetReportDetail, StorageInsightsRestStub
    ):
        def __hash__(self):
            return hash("StorageInsightsRestTransport.GetReportDetail")

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
            request: storageinsights.GetReportDetailRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> storageinsights.ReportDetail:
            r"""Call the get report detail method over HTTP.

            Args:
                request (~.storageinsights.GetReportDetailRequest):
                    The request object. Message for getting a ReportDetail
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.storageinsights.ReportDetail:
                    Message describing ReportDetail
                object. ReportDetail represents metadata
                of generated reports for a ReportConfig.
                Next ID: 10

            """

            http_options = _BaseStorageInsightsRestTransport._BaseGetReportDetail._get_http_options()
            request, metadata = self._interceptor.pre_get_report_detail(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseStorageInsightsRestTransport._BaseGetReportDetail,
                    "_BaseGetReportDetail__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.storageinsights_v1.StorageInsightsClient.GetReportDetail",
                    extra={
                        "serviceName": "google.cloud.storageinsights.v1.StorageInsights",
                        "rpcName": "GetReportDetail",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = StorageInsightsRestTransport._GetReportDetail._get_response(
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
            resp = storageinsights.ReportDetail()
            pb_resp = storageinsights.ReportDetail.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_report_detail(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_report_detail_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = storageinsights.ReportDetail.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.storageinsights_v1.StorageInsightsClient.get_report_detail",
                    extra={
                        "serviceName": "google.cloud.storageinsights.v1.StorageInsights",
                        "rpcName": "GetReportDetail",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _LinkDataset(
        _BaseStorageInsightsRestTransport._BaseLinkDataset, StorageInsightsRestStub
    ):
        def __hash__(self):
            return hash("StorageInsightsRestTransport.LinkDataset")

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
            request: storageinsights.LinkDatasetRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the link dataset method over HTTP.

            Args:
                request (~.storageinsights.LinkDatasetRequest):
                    The request object. Request message for
                [``LinkDataset``][google.cloud.storageinsights.v1.StorageInsights.LinkDataset]
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

            http_options = (
                _BaseStorageInsightsRestTransport._BaseLinkDataset._get_http_options()
            )
            request, metadata = self._interceptor.pre_link_dataset(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseStorageInsightsRestTransport._BaseLinkDataset,
                    "_BaseLinkDataset__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.storageinsights_v1.StorageInsightsClient.LinkDataset",
                    extra={
                        "serviceName": "google.cloud.storageinsights.v1.StorageInsights",
                        "rpcName": "LinkDataset",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = StorageInsightsRestTransport._LinkDataset._get_response(
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

            resp = self._interceptor.post_link_dataset(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_link_dataset_with_metadata(
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
                    "Received response for google.cloud.storageinsights_v1.StorageInsightsClient.link_dataset",
                    extra={
                        "serviceName": "google.cloud.storageinsights.v1.StorageInsights",
                        "rpcName": "LinkDataset",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListDatasetConfigs(
        _BaseStorageInsightsRestTransport._BaseListDatasetConfigs,
        StorageInsightsRestStub,
    ):
        def __hash__(self):
            return hash("StorageInsightsRestTransport.ListDatasetConfigs")

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
            request: storageinsights.ListDatasetConfigsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> storageinsights.ListDatasetConfigsResponse:
            r"""Call the list dataset configs method over HTTP.

            Args:
                request (~.storageinsights.ListDatasetConfigsRequest):
                    The request object. Request message for
                [``ListDatasetConfigs``][google.cloud.storageinsights.v1.StorageInsights.ListDatasetConfigs]
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.storageinsights.ListDatasetConfigsResponse:
                    Response message for
                [``ListDatasetConfigs``][google.cloud.storageinsights.v1.StorageInsights.ListDatasetConfigs]

            """

            http_options = _BaseStorageInsightsRestTransport._BaseListDatasetConfigs._get_http_options()
            request, metadata = self._interceptor.pre_list_dataset_configs(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseStorageInsightsRestTransport._BaseListDatasetConfigs,
                    "_BaseListDatasetConfigs__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.storageinsights_v1.StorageInsightsClient.ListDatasetConfigs",
                    extra={
                        "serviceName": "google.cloud.storageinsights.v1.StorageInsights",
                        "rpcName": "ListDatasetConfigs",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = StorageInsightsRestTransport._ListDatasetConfigs._get_response(
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
            resp = storageinsights.ListDatasetConfigsResponse()
            pb_resp = storageinsights.ListDatasetConfigsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_dataset_configs(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_dataset_configs_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        storageinsights.ListDatasetConfigsResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.storageinsights_v1.StorageInsightsClient.list_dataset_configs",
                    extra={
                        "serviceName": "google.cloud.storageinsights.v1.StorageInsights",
                        "rpcName": "ListDatasetConfigs",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListReportConfigs(
        _BaseStorageInsightsRestTransport._BaseListReportConfigs,
        StorageInsightsRestStub,
    ):
        def __hash__(self):
            return hash("StorageInsightsRestTransport.ListReportConfigs")

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
            request: storageinsights.ListReportConfigsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> storageinsights.ListReportConfigsResponse:
            r"""Call the list report configs method over HTTP.

            Args:
                request (~.storageinsights.ListReportConfigsRequest):
                    The request object. Request message for
                [``ListReportConfigs``][google.cloud.storageinsights.v1.StorageInsights.ListReportConfigs]
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.storageinsights.ListReportConfigsResponse:
                    Message for response to listing
                ReportConfigs

            """

            http_options = _BaseStorageInsightsRestTransport._BaseListReportConfigs._get_http_options()
            request, metadata = self._interceptor.pre_list_report_configs(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseStorageInsightsRestTransport._BaseListReportConfigs,
                    "_BaseListReportConfigs__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.storageinsights_v1.StorageInsightsClient.ListReportConfigs",
                    extra={
                        "serviceName": "google.cloud.storageinsights.v1.StorageInsights",
                        "rpcName": "ListReportConfigs",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = StorageInsightsRestTransport._ListReportConfigs._get_response(
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
            resp = storageinsights.ListReportConfigsResponse()
            pb_resp = storageinsights.ListReportConfigsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_report_configs(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_report_configs_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        storageinsights.ListReportConfigsResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.storageinsights_v1.StorageInsightsClient.list_report_configs",
                    extra={
                        "serviceName": "google.cloud.storageinsights.v1.StorageInsights",
                        "rpcName": "ListReportConfigs",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListReportDetails(
        _BaseStorageInsightsRestTransport._BaseListReportDetails,
        StorageInsightsRestStub,
    ):
        def __hash__(self):
            return hash("StorageInsightsRestTransport.ListReportDetails")

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
            request: storageinsights.ListReportDetailsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> storageinsights.ListReportDetailsResponse:
            r"""Call the list report details method over HTTP.

            Args:
                request (~.storageinsights.ListReportDetailsRequest):
                    The request object. Message for requesting list of
                ReportDetails
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.storageinsights.ListReportDetailsResponse:
                    Message for response to listing
                ReportDetails

            """

            http_options = _BaseStorageInsightsRestTransport._BaseListReportDetails._get_http_options()
            request, metadata = self._interceptor.pre_list_report_details(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseStorageInsightsRestTransport._BaseListReportDetails,
                    "_BaseListReportDetails__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.storageinsights_v1.StorageInsightsClient.ListReportDetails",
                    extra={
                        "serviceName": "google.cloud.storageinsights.v1.StorageInsights",
                        "rpcName": "ListReportDetails",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = StorageInsightsRestTransport._ListReportDetails._get_response(
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
            resp = storageinsights.ListReportDetailsResponse()
            pb_resp = storageinsights.ListReportDetailsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_report_details(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_report_details_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        storageinsights.ListReportDetailsResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.storageinsights_v1.StorageInsightsClient.list_report_details",
                    extra={
                        "serviceName": "google.cloud.storageinsights.v1.StorageInsights",
                        "rpcName": "ListReportDetails",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UnlinkDataset(
        _BaseStorageInsightsRestTransport._BaseUnlinkDataset, StorageInsightsRestStub
    ):
        def __hash__(self):
            return hash("StorageInsightsRestTransport.UnlinkDataset")

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
            request: storageinsights.UnlinkDatasetRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the unlink dataset method over HTTP.

            Args:
                request (~.storageinsights.UnlinkDatasetRequest):
                    The request object. Request message for
                [``UnlinkDataset``][google.cloud.storageinsights.v1.StorageInsights.UnlinkDataset]
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

            http_options = (
                _BaseStorageInsightsRestTransport._BaseUnlinkDataset._get_http_options()
            )
            request, metadata = self._interceptor.pre_unlink_dataset(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseStorageInsightsRestTransport._BaseUnlinkDataset,
                    "_BaseUnlinkDataset__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.storageinsights_v1.StorageInsightsClient.UnlinkDataset",
                    extra={
                        "serviceName": "google.cloud.storageinsights.v1.StorageInsights",
                        "rpcName": "UnlinkDataset",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = StorageInsightsRestTransport._UnlinkDataset._get_response(
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

            resp = self._interceptor.post_unlink_dataset(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_unlink_dataset_with_metadata(
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
                    "Received response for google.cloud.storageinsights_v1.StorageInsightsClient.unlink_dataset",
                    extra={
                        "serviceName": "google.cloud.storageinsights.v1.StorageInsights",
                        "rpcName": "UnlinkDataset",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateDatasetConfig(
        _BaseStorageInsightsRestTransport._BaseUpdateDatasetConfig,
        StorageInsightsRestStub,
    ):
        def __hash__(self):
            return hash("StorageInsightsRestTransport.UpdateDatasetConfig")

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
            request: storageinsights.UpdateDatasetConfigRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update dataset config method over HTTP.

            Args:
                request (~.storageinsights.UpdateDatasetConfigRequest):
                    The request object. Request message for
                [``UpdateDatasetConfig``][google.cloud.storageinsights.v1.StorageInsights.UpdateDatasetConfig]
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

            http_options = _BaseStorageInsightsRestTransport._BaseUpdateDatasetConfig._get_http_options()
            request, metadata = self._interceptor.pre_update_dataset_config(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseStorageInsightsRestTransport._BaseUpdateDatasetConfig,
                    "_BaseUpdateDatasetConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.storageinsights_v1.StorageInsightsClient.UpdateDatasetConfig",
                    extra={
                        "serviceName": "google.cloud.storageinsights.v1.StorageInsights",
                        "rpcName": "UpdateDatasetConfig",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = StorageInsightsRestTransport._UpdateDatasetConfig._get_response(
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

            resp = self._interceptor.post_update_dataset_config(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_dataset_config_with_metadata(
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
                    "Received response for google.cloud.storageinsights_v1.StorageInsightsClient.update_dataset_config",
                    extra={
                        "serviceName": "google.cloud.storageinsights.v1.StorageInsights",
                        "rpcName": "UpdateDatasetConfig",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateReportConfig(
        _BaseStorageInsightsRestTransport._BaseUpdateReportConfig,
        StorageInsightsRestStub,
    ):
        def __hash__(self):
            return hash("StorageInsightsRestTransport.UpdateReportConfig")

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
            request: storageinsights.UpdateReportConfigRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> storageinsights.ReportConfig:
            r"""Call the update report config method over HTTP.

            Args:
                request (~.storageinsights.UpdateReportConfigRequest):
                    The request object. Message for updating a ReportConfig
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.storageinsights.ReportConfig:
                    Message describing ReportConfig
                object. ReportConfig is the
                configuration to generate reports. See
                https://cloud.google.com/storage/docs/insights/using-inventory-reports#create-config-rest
                for more details on how to set various
                fields. Next ID: 12

            """

            http_options = _BaseStorageInsightsRestTransport._BaseUpdateReportConfig._get_http_options()
            request, metadata = self._interceptor.pre_update_report_config(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseStorageInsightsRestTransport._BaseUpdateReportConfig,
                    "_BaseUpdateReportConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.storageinsights_v1.StorageInsightsClient.UpdateReportConfig",
                    extra={
                        "serviceName": "google.cloud.storageinsights.v1.StorageInsights",
                        "rpcName": "UpdateReportConfig",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = StorageInsightsRestTransport._UpdateReportConfig._get_response(
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
            resp = storageinsights.ReportConfig()
            pb_resp = storageinsights.ReportConfig.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_report_config(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_report_config_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = storageinsights.ReportConfig.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.storageinsights_v1.StorageInsightsClient.update_report_config",
                    extra={
                        "serviceName": "google.cloud.storageinsights.v1.StorageInsights",
                        "rpcName": "UpdateReportConfig",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def create_dataset_config(
        self,
    ) -> Callable[
        [storageinsights.CreateDatasetConfigRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateDatasetConfig(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_report_config(
        self,
    ) -> Callable[
        [storageinsights.CreateReportConfigRequest], storageinsights.ReportConfig
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateReportConfig(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_dataset_config(
        self,
    ) -> Callable[
        [storageinsights.DeleteDatasetConfigRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteDatasetConfig(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_report_config(
        self,
    ) -> Callable[[storageinsights.DeleteReportConfigRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteReportConfig(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_dataset_config(
        self,
    ) -> Callable[
        [storageinsights.GetDatasetConfigRequest], storageinsights.DatasetConfig
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetDatasetConfig(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_report_config(
        self,
    ) -> Callable[
        [storageinsights.GetReportConfigRequest], storageinsights.ReportConfig
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetReportConfig(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_report_detail(
        self,
    ) -> Callable[
        [storageinsights.GetReportDetailRequest], storageinsights.ReportDetail
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetReportDetail(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def link_dataset(
        self,
    ) -> Callable[[storageinsights.LinkDatasetRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._LinkDataset(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_dataset_configs(
        self,
    ) -> Callable[
        [storageinsights.ListDatasetConfigsRequest],
        storageinsights.ListDatasetConfigsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListDatasetConfigs(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_report_configs(
        self,
    ) -> Callable[
        [storageinsights.ListReportConfigsRequest],
        storageinsights.ListReportConfigsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListReportConfigs(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_report_details(
        self,
    ) -> Callable[
        [storageinsights.ListReportDetailsRequest],
        storageinsights.ListReportDetailsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListReportDetails(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def unlink_dataset(
        self,
    ) -> Callable[[storageinsights.UnlinkDatasetRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UnlinkDataset(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_dataset_config(
        self,
    ) -> Callable[
        [storageinsights.UpdateDatasetConfigRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateDatasetConfig(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_report_config(
        self,
    ) -> Callable[
        [storageinsights.UpdateReportConfigRequest], storageinsights.ReportConfig
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateReportConfig(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_location(self):
        return self._GetLocation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetLocation(
        _BaseStorageInsightsRestTransport._BaseGetLocation, StorageInsightsRestStub
    ):
        def __hash__(self):
            return hash("StorageInsightsRestTransport.GetLocation")

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
            request: locations_pb2.GetLocationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> locations_pb2.Location:
            r"""Call the get location method over HTTP.

            Args:
                request (locations_pb2.GetLocationRequest):
                    The request object for GetLocation method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                locations_pb2.Location: Response from GetLocation method.
            """

            http_options = (
                _BaseStorageInsightsRestTransport._BaseGetLocation._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_location(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseStorageInsightsRestTransport._BaseGetLocation,
                    "_BaseGetLocation__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.storageinsights_v1.StorageInsightsClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.storageinsights.v1.StorageInsights",
                        "rpcName": "GetLocation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = StorageInsightsRestTransport._GetLocation._get_response(
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
            resp = locations_pb2.Location()
            resp = json_format.Parse(content, resp)
            resp = self._interceptor.post_get_location(resp)
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
                    "Received response for google.cloud.storageinsights_v1.StorageInsightsAsyncClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.storageinsights.v1.StorageInsights",
                        "rpcName": "GetLocation",
                        "httpResponse": http_response,
                        "metadata": http_response["headers"],
                    },
                )
            return resp

    @property
    def list_locations(self):
        return self._ListLocations(self._session, self._host, self._interceptor)  # type: ignore

    class _ListLocations(
        _BaseStorageInsightsRestTransport._BaseListLocations, StorageInsightsRestStub
    ):
        def __hash__(self):
            return hash("StorageInsightsRestTransport.ListLocations")

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
            request: locations_pb2.ListLocationsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> locations_pb2.ListLocationsResponse:
            r"""Call the list locations method over HTTP.

            Args:
                request (locations_pb2.ListLocationsRequest):
                    The request object for ListLocations method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                locations_pb2.ListLocationsResponse: Response from ListLocations method.
            """

            http_options = (
                _BaseStorageInsightsRestTransport._BaseListLocations._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_locations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseStorageInsightsRestTransport._BaseListLocations,
                    "_BaseListLocations__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.storageinsights_v1.StorageInsightsClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.storageinsights.v1.StorageInsights",
                        "rpcName": "ListLocations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = StorageInsightsRestTransport._ListLocations._get_response(
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
            resp = locations_pb2.ListLocationsResponse()
            resp = json_format.Parse(content, resp)
            resp = self._interceptor.post_list_locations(resp)
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
                    "Received response for google.cloud.storageinsights_v1.StorageInsightsAsyncClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.storageinsights.v1.StorageInsights",
                        "rpcName": "ListLocations",
                        "httpResponse": http_response,
                        "metadata": http_response["headers"],
                    },
                )
            return resp

    @property
    def cancel_operation(self):
        return self._CancelOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _CancelOperation(
        _BaseStorageInsightsRestTransport._BaseCancelOperation, StorageInsightsRestStub
    ):
        def __hash__(self):
            return hash("StorageInsightsRestTransport.CancelOperation")

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

            http_options = _BaseStorageInsightsRestTransport._BaseCancelOperation._get_http_options()
            request, metadata = self._interceptor.pre_cancel_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseStorageInsightsRestTransport._BaseCancelOperation,
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
                    f"Sending request for google.cloud.storageinsights_v1.StorageInsightsClient.CancelOperation",
                    extra={
                        "serviceName": "google.cloud.storageinsights.v1.StorageInsights",
                        "rpcName": "CancelOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = StorageInsightsRestTransport._CancelOperation._get_response(
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
        _BaseStorageInsightsRestTransport._BaseDeleteOperation, StorageInsightsRestStub
    ):
        def __hash__(self):
            return hash("StorageInsightsRestTransport.DeleteOperation")

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

            http_options = _BaseStorageInsightsRestTransport._BaseDeleteOperation._get_http_options()
            request, metadata = self._interceptor.pre_delete_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseStorageInsightsRestTransport._BaseDeleteOperation,
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
                    f"Sending request for google.cloud.storageinsights_v1.StorageInsightsClient.DeleteOperation",
                    extra={
                        "serviceName": "google.cloud.storageinsights.v1.StorageInsights",
                        "rpcName": "DeleteOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = StorageInsightsRestTransport._DeleteOperation._get_response(
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
        _BaseStorageInsightsRestTransport._BaseGetOperation, StorageInsightsRestStub
    ):
        def __hash__(self):
            return hash("StorageInsightsRestTransport.GetOperation")

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
                _BaseStorageInsightsRestTransport._BaseGetOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_operation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseStorageInsightsRestTransport._BaseGetOperation,
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
                    f"Sending request for google.cloud.storageinsights_v1.StorageInsightsClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.storageinsights.v1.StorageInsights",
                        "rpcName": "GetOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = StorageInsightsRestTransport._GetOperation._get_response(
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
                    "Received response for google.cloud.storageinsights_v1.StorageInsightsAsyncClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.storageinsights.v1.StorageInsights",
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
        _BaseStorageInsightsRestTransport._BaseListOperations, StorageInsightsRestStub
    ):
        def __hash__(self):
            return hash("StorageInsightsRestTransport.ListOperations")

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

            http_options = _BaseStorageInsightsRestTransport._BaseListOperations._get_http_options()
            request, metadata = self._interceptor.pre_list_operations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseStorageInsightsRestTransport._BaseListOperations,
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
                    f"Sending request for google.cloud.storageinsights_v1.StorageInsightsClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.storageinsights.v1.StorageInsights",
                        "rpcName": "ListOperations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = StorageInsightsRestTransport._ListOperations._get_response(
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
                    "Received response for google.cloud.storageinsights_v1.StorageInsightsAsyncClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.storageinsights.v1.StorageInsights",
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


__all__ = ("StorageInsightsRestTransport",)
