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
from google.cloud.location import locations_pb2  # type: ignore
from google.protobuf import json_format
from requests import __version__ as requests_version

from google.cloud.bigquery_datatransfer_v1._compat import transcode_request
from google.cloud.bigquery_datatransfer_v1.types import datatransfer, transfer

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseDataTransferServiceRestTransport

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


class DataTransferServiceRestInterceptor:
    """Interceptor for DataTransferService.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the DataTransferServiceRestTransport.

    .. code-block:: python
        class MyCustomDataTransferServiceInterceptor(DataTransferServiceRestInterceptor):
            def pre_check_valid_creds(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_check_valid_creds(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_transfer_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_transfer_config(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_transfer_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_delete_transfer_run(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_enroll_data_sources(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_get_data_source(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_data_source(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_transfer_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_transfer_config(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_transfer_run(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_transfer_run(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_data_sources(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_data_sources(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_transfer_configs(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_transfer_configs(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_transfer_logs(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_transfer_logs(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_transfer_runs(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_transfer_runs(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_schedule_transfer_runs(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_schedule_transfer_runs(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_start_manual_transfer_runs(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_start_manual_transfer_runs(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_unenroll_data_sources(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_update_transfer_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_transfer_config(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = DataTransferServiceRestTransport(interceptor=MyCustomDataTransferServiceInterceptor())
        client = DataTransferServiceClient(transport=transport)


    """

    def pre_check_valid_creds(
        self,
        request: datatransfer.CheckValidCredsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        datatransfer.CheckValidCredsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for check_valid_creds

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DataTransferService server.
        """
        return request, metadata

    def post_check_valid_creds(
        self, response: datatransfer.CheckValidCredsResponse
    ) -> datatransfer.CheckValidCredsResponse:
        """Post-rpc interceptor for check_valid_creds

        DEPRECATED. Please use the `post_check_valid_creds_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DataTransferService server but before
        it is returned to user code. This `post_check_valid_creds` interceptor runs
        before the `post_check_valid_creds_with_metadata` interceptor.
        """
        return response

    def post_check_valid_creds_with_metadata(
        self,
        response: datatransfer.CheckValidCredsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        datatransfer.CheckValidCredsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for check_valid_creds

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DataTransferService server but before it is returned to user code.

        We recommend only using this `post_check_valid_creds_with_metadata`
        interceptor in new development instead of the `post_check_valid_creds` interceptor.
        When both interceptors are used, this `post_check_valid_creds_with_metadata` interceptor runs after the
        `post_check_valid_creds` interceptor. The (possibly modified) response returned by
        `post_check_valid_creds` will be passed to
        `post_check_valid_creds_with_metadata`.
        """
        return response, metadata

    def pre_create_transfer_config(
        self,
        request: datatransfer.CreateTransferConfigRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        datatransfer.CreateTransferConfigRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_transfer_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DataTransferService server.
        """
        return request, metadata

    def post_create_transfer_config(
        self, response: transfer.TransferConfig
    ) -> transfer.TransferConfig:
        """Post-rpc interceptor for create_transfer_config

        DEPRECATED. Please use the `post_create_transfer_config_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DataTransferService server but before
        it is returned to user code. This `post_create_transfer_config` interceptor runs
        before the `post_create_transfer_config_with_metadata` interceptor.
        """
        return response

    def post_create_transfer_config_with_metadata(
        self,
        response: transfer.TransferConfig,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[transfer.TransferConfig, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_transfer_config

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DataTransferService server but before it is returned to user code.

        We recommend only using this `post_create_transfer_config_with_metadata`
        interceptor in new development instead of the `post_create_transfer_config` interceptor.
        When both interceptors are used, this `post_create_transfer_config_with_metadata` interceptor runs after the
        `post_create_transfer_config` interceptor. The (possibly modified) response returned by
        `post_create_transfer_config` will be passed to
        `post_create_transfer_config_with_metadata`.
        """
        return response, metadata

    def pre_delete_transfer_config(
        self,
        request: datatransfer.DeleteTransferConfigRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        datatransfer.DeleteTransferConfigRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_transfer_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DataTransferService server.
        """
        return request, metadata

    def pre_delete_transfer_run(
        self,
        request: datatransfer.DeleteTransferRunRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        datatransfer.DeleteTransferRunRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_transfer_run

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DataTransferService server.
        """
        return request, metadata

    def pre_enroll_data_sources(
        self,
        request: datatransfer.EnrollDataSourcesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        datatransfer.EnrollDataSourcesRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for enroll_data_sources

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DataTransferService server.
        """
        return request, metadata

    def pre_get_data_source(
        self,
        request: datatransfer.GetDataSourceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        datatransfer.GetDataSourceRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_data_source

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DataTransferService server.
        """
        return request, metadata

    def post_get_data_source(
        self, response: datatransfer.DataSource
    ) -> datatransfer.DataSource:
        """Post-rpc interceptor for get_data_source

        DEPRECATED. Please use the `post_get_data_source_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DataTransferService server but before
        it is returned to user code. This `post_get_data_source` interceptor runs
        before the `post_get_data_source_with_metadata` interceptor.
        """
        return response

    def post_get_data_source_with_metadata(
        self,
        response: datatransfer.DataSource,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[datatransfer.DataSource, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_data_source

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DataTransferService server but before it is returned to user code.

        We recommend only using this `post_get_data_source_with_metadata`
        interceptor in new development instead of the `post_get_data_source` interceptor.
        When both interceptors are used, this `post_get_data_source_with_metadata` interceptor runs after the
        `post_get_data_source` interceptor. The (possibly modified) response returned by
        `post_get_data_source` will be passed to
        `post_get_data_source_with_metadata`.
        """
        return response, metadata

    def pre_get_transfer_config(
        self,
        request: datatransfer.GetTransferConfigRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        datatransfer.GetTransferConfigRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_transfer_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DataTransferService server.
        """
        return request, metadata

    def post_get_transfer_config(
        self, response: transfer.TransferConfig
    ) -> transfer.TransferConfig:
        """Post-rpc interceptor for get_transfer_config

        DEPRECATED. Please use the `post_get_transfer_config_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DataTransferService server but before
        it is returned to user code. This `post_get_transfer_config` interceptor runs
        before the `post_get_transfer_config_with_metadata` interceptor.
        """
        return response

    def post_get_transfer_config_with_metadata(
        self,
        response: transfer.TransferConfig,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[transfer.TransferConfig, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_transfer_config

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DataTransferService server but before it is returned to user code.

        We recommend only using this `post_get_transfer_config_with_metadata`
        interceptor in new development instead of the `post_get_transfer_config` interceptor.
        When both interceptors are used, this `post_get_transfer_config_with_metadata` interceptor runs after the
        `post_get_transfer_config` interceptor. The (possibly modified) response returned by
        `post_get_transfer_config` will be passed to
        `post_get_transfer_config_with_metadata`.
        """
        return response, metadata

    def pre_get_transfer_run(
        self,
        request: datatransfer.GetTransferRunRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        datatransfer.GetTransferRunRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_transfer_run

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DataTransferService server.
        """
        return request, metadata

    def post_get_transfer_run(
        self, response: transfer.TransferRun
    ) -> transfer.TransferRun:
        """Post-rpc interceptor for get_transfer_run

        DEPRECATED. Please use the `post_get_transfer_run_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DataTransferService server but before
        it is returned to user code. This `post_get_transfer_run` interceptor runs
        before the `post_get_transfer_run_with_metadata` interceptor.
        """
        return response

    def post_get_transfer_run_with_metadata(
        self,
        response: transfer.TransferRun,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[transfer.TransferRun, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_transfer_run

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DataTransferService server but before it is returned to user code.

        We recommend only using this `post_get_transfer_run_with_metadata`
        interceptor in new development instead of the `post_get_transfer_run` interceptor.
        When both interceptors are used, this `post_get_transfer_run_with_metadata` interceptor runs after the
        `post_get_transfer_run` interceptor. The (possibly modified) response returned by
        `post_get_transfer_run` will be passed to
        `post_get_transfer_run_with_metadata`.
        """
        return response, metadata

    def pre_list_data_sources(
        self,
        request: datatransfer.ListDataSourcesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        datatransfer.ListDataSourcesRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_data_sources

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DataTransferService server.
        """
        return request, metadata

    def post_list_data_sources(
        self, response: datatransfer.ListDataSourcesResponse
    ) -> datatransfer.ListDataSourcesResponse:
        """Post-rpc interceptor for list_data_sources

        DEPRECATED. Please use the `post_list_data_sources_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DataTransferService server but before
        it is returned to user code. This `post_list_data_sources` interceptor runs
        before the `post_list_data_sources_with_metadata` interceptor.
        """
        return response

    def post_list_data_sources_with_metadata(
        self,
        response: datatransfer.ListDataSourcesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        datatransfer.ListDataSourcesResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_data_sources

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DataTransferService server but before it is returned to user code.

        We recommend only using this `post_list_data_sources_with_metadata`
        interceptor in new development instead of the `post_list_data_sources` interceptor.
        When both interceptors are used, this `post_list_data_sources_with_metadata` interceptor runs after the
        `post_list_data_sources` interceptor. The (possibly modified) response returned by
        `post_list_data_sources` will be passed to
        `post_list_data_sources_with_metadata`.
        """
        return response, metadata

    def pre_list_transfer_configs(
        self,
        request: datatransfer.ListTransferConfigsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        datatransfer.ListTransferConfigsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_transfer_configs

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DataTransferService server.
        """
        return request, metadata

    def post_list_transfer_configs(
        self, response: datatransfer.ListTransferConfigsResponse
    ) -> datatransfer.ListTransferConfigsResponse:
        """Post-rpc interceptor for list_transfer_configs

        DEPRECATED. Please use the `post_list_transfer_configs_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DataTransferService server but before
        it is returned to user code. This `post_list_transfer_configs` interceptor runs
        before the `post_list_transfer_configs_with_metadata` interceptor.
        """
        return response

    def post_list_transfer_configs_with_metadata(
        self,
        response: datatransfer.ListTransferConfigsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        datatransfer.ListTransferConfigsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_transfer_configs

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DataTransferService server but before it is returned to user code.

        We recommend only using this `post_list_transfer_configs_with_metadata`
        interceptor in new development instead of the `post_list_transfer_configs` interceptor.
        When both interceptors are used, this `post_list_transfer_configs_with_metadata` interceptor runs after the
        `post_list_transfer_configs` interceptor. The (possibly modified) response returned by
        `post_list_transfer_configs` will be passed to
        `post_list_transfer_configs_with_metadata`.
        """
        return response, metadata

    def pre_list_transfer_logs(
        self,
        request: datatransfer.ListTransferLogsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        datatransfer.ListTransferLogsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_transfer_logs

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DataTransferService server.
        """
        return request, metadata

    def post_list_transfer_logs(
        self, response: datatransfer.ListTransferLogsResponse
    ) -> datatransfer.ListTransferLogsResponse:
        """Post-rpc interceptor for list_transfer_logs

        DEPRECATED. Please use the `post_list_transfer_logs_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DataTransferService server but before
        it is returned to user code. This `post_list_transfer_logs` interceptor runs
        before the `post_list_transfer_logs_with_metadata` interceptor.
        """
        return response

    def post_list_transfer_logs_with_metadata(
        self,
        response: datatransfer.ListTransferLogsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        datatransfer.ListTransferLogsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_transfer_logs

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DataTransferService server but before it is returned to user code.

        We recommend only using this `post_list_transfer_logs_with_metadata`
        interceptor in new development instead of the `post_list_transfer_logs` interceptor.
        When both interceptors are used, this `post_list_transfer_logs_with_metadata` interceptor runs after the
        `post_list_transfer_logs` interceptor. The (possibly modified) response returned by
        `post_list_transfer_logs` will be passed to
        `post_list_transfer_logs_with_metadata`.
        """
        return response, metadata

    def pre_list_transfer_runs(
        self,
        request: datatransfer.ListTransferRunsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        datatransfer.ListTransferRunsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_transfer_runs

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DataTransferService server.
        """
        return request, metadata

    def post_list_transfer_runs(
        self, response: datatransfer.ListTransferRunsResponse
    ) -> datatransfer.ListTransferRunsResponse:
        """Post-rpc interceptor for list_transfer_runs

        DEPRECATED. Please use the `post_list_transfer_runs_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DataTransferService server but before
        it is returned to user code. This `post_list_transfer_runs` interceptor runs
        before the `post_list_transfer_runs_with_metadata` interceptor.
        """
        return response

    def post_list_transfer_runs_with_metadata(
        self,
        response: datatransfer.ListTransferRunsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        datatransfer.ListTransferRunsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_transfer_runs

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DataTransferService server but before it is returned to user code.

        We recommend only using this `post_list_transfer_runs_with_metadata`
        interceptor in new development instead of the `post_list_transfer_runs` interceptor.
        When both interceptors are used, this `post_list_transfer_runs_with_metadata` interceptor runs after the
        `post_list_transfer_runs` interceptor. The (possibly modified) response returned by
        `post_list_transfer_runs` will be passed to
        `post_list_transfer_runs_with_metadata`.
        """
        return response, metadata

    def pre_schedule_transfer_runs(
        self,
        request: datatransfer.ScheduleTransferRunsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        datatransfer.ScheduleTransferRunsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for schedule_transfer_runs

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DataTransferService server.
        """
        return request, metadata

    def post_schedule_transfer_runs(
        self, response: datatransfer.ScheduleTransferRunsResponse
    ) -> datatransfer.ScheduleTransferRunsResponse:
        """Post-rpc interceptor for schedule_transfer_runs

        DEPRECATED. Please use the `post_schedule_transfer_runs_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DataTransferService server but before
        it is returned to user code. This `post_schedule_transfer_runs` interceptor runs
        before the `post_schedule_transfer_runs_with_metadata` interceptor.
        """
        return response

    def post_schedule_transfer_runs_with_metadata(
        self,
        response: datatransfer.ScheduleTransferRunsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        datatransfer.ScheduleTransferRunsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for schedule_transfer_runs

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DataTransferService server but before it is returned to user code.

        We recommend only using this `post_schedule_transfer_runs_with_metadata`
        interceptor in new development instead of the `post_schedule_transfer_runs` interceptor.
        When both interceptors are used, this `post_schedule_transfer_runs_with_metadata` interceptor runs after the
        `post_schedule_transfer_runs` interceptor. The (possibly modified) response returned by
        `post_schedule_transfer_runs` will be passed to
        `post_schedule_transfer_runs_with_metadata`.
        """
        return response, metadata

    def pre_start_manual_transfer_runs(
        self,
        request: datatransfer.StartManualTransferRunsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        datatransfer.StartManualTransferRunsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for start_manual_transfer_runs

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DataTransferService server.
        """
        return request, metadata

    def post_start_manual_transfer_runs(
        self, response: datatransfer.StartManualTransferRunsResponse
    ) -> datatransfer.StartManualTransferRunsResponse:
        """Post-rpc interceptor for start_manual_transfer_runs

        DEPRECATED. Please use the `post_start_manual_transfer_runs_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DataTransferService server but before
        it is returned to user code. This `post_start_manual_transfer_runs` interceptor runs
        before the `post_start_manual_transfer_runs_with_metadata` interceptor.
        """
        return response

    def post_start_manual_transfer_runs_with_metadata(
        self,
        response: datatransfer.StartManualTransferRunsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        datatransfer.StartManualTransferRunsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for start_manual_transfer_runs

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DataTransferService server but before it is returned to user code.

        We recommend only using this `post_start_manual_transfer_runs_with_metadata`
        interceptor in new development instead of the `post_start_manual_transfer_runs` interceptor.
        When both interceptors are used, this `post_start_manual_transfer_runs_with_metadata` interceptor runs after the
        `post_start_manual_transfer_runs` interceptor. The (possibly modified) response returned by
        `post_start_manual_transfer_runs` will be passed to
        `post_start_manual_transfer_runs_with_metadata`.
        """
        return response, metadata

    def pre_unenroll_data_sources(
        self,
        request: datatransfer.UnenrollDataSourcesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        datatransfer.UnenrollDataSourcesRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for unenroll_data_sources

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DataTransferService server.
        """
        return request, metadata

    def pre_update_transfer_config(
        self,
        request: datatransfer.UpdateTransferConfigRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        datatransfer.UpdateTransferConfigRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_transfer_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DataTransferService server.
        """
        return request, metadata

    def post_update_transfer_config(
        self, response: transfer.TransferConfig
    ) -> transfer.TransferConfig:
        """Post-rpc interceptor for update_transfer_config

        DEPRECATED. Please use the `post_update_transfer_config_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DataTransferService server but before
        it is returned to user code. This `post_update_transfer_config` interceptor runs
        before the `post_update_transfer_config_with_metadata` interceptor.
        """
        return response

    def post_update_transfer_config_with_metadata(
        self,
        response: transfer.TransferConfig,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[transfer.TransferConfig, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_transfer_config

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DataTransferService server but before it is returned to user code.

        We recommend only using this `post_update_transfer_config_with_metadata`
        interceptor in new development instead of the `post_update_transfer_config` interceptor.
        When both interceptors are used, this `post_update_transfer_config_with_metadata` interceptor runs after the
        `post_update_transfer_config` interceptor. The (possibly modified) response returned by
        `post_update_transfer_config` will be passed to
        `post_update_transfer_config_with_metadata`.
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
        before they are sent to the DataTransferService server.
        """
        return request, metadata

    def post_get_location(
        self, response: locations_pb2.Location
    ) -> locations_pb2.Location:
        """Post-rpc interceptor for get_location

        Override in a subclass to manipulate the response
        after it is returned by the DataTransferService server but before
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
        before they are sent to the DataTransferService server.
        """
        return request, metadata

    def post_list_locations(
        self, response: locations_pb2.ListLocationsResponse
    ) -> locations_pb2.ListLocationsResponse:
        """Post-rpc interceptor for list_locations

        Override in a subclass to manipulate the response
        after it is returned by the DataTransferService server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class DataTransferServiceRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: DataTransferServiceRestInterceptor


class DataTransferServiceRestTransport(_BaseDataTransferServiceRestTransport):
    """REST backend synchronous transport for DataTransferService.

    This API allows users to manage their data transfers into
    BigQuery.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "bigquerydatatransfer.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[DataTransferServiceRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'bigquerydatatransfer.googleapis.com').
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
            interceptor (Optional[DataTransferServiceRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or DataTransferServiceRestInterceptor()
        self._prep_wrapped_messages(client_info)

    class _CheckValidCreds(
        _BaseDataTransferServiceRestTransport._BaseCheckValidCreds,
        DataTransferServiceRestStub,
    ):
        def __hash__(self):
            return hash("DataTransferServiceRestTransport.CheckValidCreds")

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
            request: datatransfer.CheckValidCredsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> datatransfer.CheckValidCredsResponse:
            r"""Call the check valid creds method over HTTP.

            Args:
                request (~.datatransfer.CheckValidCredsRequest):
                    The request object. A request to determine whether the
                user has valid credentials. This method
                is used to limit the number of OAuth
                popups in the user interface. The user
                id is inferred from the API call
                context. If the data source has the
                Google+ authorization type, this method
                returns false, as it cannot be
                determined whether the credentials are
                already valid merely based on the user
                id.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.datatransfer.CheckValidCredsResponse:
                    A response indicating whether the
                credentials exist and are valid.

            """

            http_options = _BaseDataTransferServiceRestTransport._BaseCheckValidCreds._get_http_options()
            request, metadata = self._interceptor.pre_check_valid_creds(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataTransferServiceRestTransport._BaseCheckValidCreds,
                    "_BaseCheckValidCreds__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.bigquery.datatransfer_v1.DataTransferServiceClient.CheckValidCreds",
                    extra={
                        "serviceName": "google.cloud.bigquery.datatransfer.v1.DataTransferService",
                        "rpcName": "CheckValidCreds",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DataTransferServiceRestTransport._CheckValidCreds._get_response(
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
            resp = datatransfer.CheckValidCredsResponse()
            pb_resp = datatransfer.CheckValidCredsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_check_valid_creds(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_check_valid_creds_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = datatransfer.CheckValidCredsResponse.to_json(
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
                    "Received response for google.cloud.bigquery.datatransfer_v1.DataTransferServiceClient.check_valid_creds",
                    extra={
                        "serviceName": "google.cloud.bigquery.datatransfer.v1.DataTransferService",
                        "rpcName": "CheckValidCreds",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateTransferConfig(
        _BaseDataTransferServiceRestTransport._BaseCreateTransferConfig,
        DataTransferServiceRestStub,
    ):
        def __hash__(self):
            return hash("DataTransferServiceRestTransport.CreateTransferConfig")

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
            request: datatransfer.CreateTransferConfigRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> transfer.TransferConfig:
            r"""Call the create transfer config method over HTTP.

            Args:
                request (~.datatransfer.CreateTransferConfigRequest):
                    The request object. A request to create a data transfer configuration. If
                new credentials are needed for this transfer
                configuration, authorization info must be provided. If
                authorization info is provided, the transfer
                configuration will be associated with the user id
                corresponding to the authorization info. Otherwise, the
                transfer configuration will be associated with the
                calling user.

                When using a cross project service account for creating
                a transfer config, you must enable cross project service
                account usage. For more information, see `Disable
                attachment of service accounts to resources in other
                projects <https://cloud.google.com/resource-manager/docs/organization-policy/restricting-service-accounts#disable_cross_project_service_accounts>`__.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.transfer.TransferConfig:
                    Represents a data transfer configuration. A transfer
                configuration contains all metadata needed to perform a
                data transfer. For example, ``destination_dataset_id``
                specifies where data should be stored. When a new
                transfer configuration is created, the specified
                ``destination_dataset_id`` is created when needed and
                shared with the appropriate data source service account.

            """

            http_options = _BaseDataTransferServiceRestTransport._BaseCreateTransferConfig._get_http_options()
            request, metadata = self._interceptor.pre_create_transfer_config(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataTransferServiceRestTransport._BaseCreateTransferConfig,
                    "_BaseCreateTransferConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.bigquery.datatransfer_v1.DataTransferServiceClient.CreateTransferConfig",
                    extra={
                        "serviceName": "google.cloud.bigquery.datatransfer.v1.DataTransferService",
                        "rpcName": "CreateTransferConfig",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                DataTransferServiceRestTransport._CreateTransferConfig._get_response(
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
            resp = transfer.TransferConfig()
            pb_resp = transfer.TransferConfig.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_transfer_config(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_transfer_config_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = transfer.TransferConfig.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.bigquery.datatransfer_v1.DataTransferServiceClient.create_transfer_config",
                    extra={
                        "serviceName": "google.cloud.bigquery.datatransfer.v1.DataTransferService",
                        "rpcName": "CreateTransferConfig",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteTransferConfig(
        _BaseDataTransferServiceRestTransport._BaseDeleteTransferConfig,
        DataTransferServiceRestStub,
    ):
        def __hash__(self):
            return hash("DataTransferServiceRestTransport.DeleteTransferConfig")

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
            request: datatransfer.DeleteTransferConfigRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete transfer config method over HTTP.

            Args:
                request (~.datatransfer.DeleteTransferConfigRequest):
                    The request object. A request to delete data transfer
                information. All associated transfer
                runs and log messages will be deleted as
                well.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = _BaseDataTransferServiceRestTransport._BaseDeleteTransferConfig._get_http_options()
            request, metadata = self._interceptor.pre_delete_transfer_config(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataTransferServiceRestTransport._BaseDeleteTransferConfig,
                    "_BaseDeleteTransferConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.bigquery.datatransfer_v1.DataTransferServiceClient.DeleteTransferConfig",
                    extra={
                        "serviceName": "google.cloud.bigquery.datatransfer.v1.DataTransferService",
                        "rpcName": "DeleteTransferConfig",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                DataTransferServiceRestTransport._DeleteTransferConfig._get_response(
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

    class _DeleteTransferRun(
        _BaseDataTransferServiceRestTransport._BaseDeleteTransferRun,
        DataTransferServiceRestStub,
    ):
        def __hash__(self):
            return hash("DataTransferServiceRestTransport.DeleteTransferRun")

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
            request: datatransfer.DeleteTransferRunRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete transfer run method over HTTP.

            Args:
                request (~.datatransfer.DeleteTransferRunRequest):
                    The request object. A request to delete data transfer run
                information.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = _BaseDataTransferServiceRestTransport._BaseDeleteTransferRun._get_http_options()
            request, metadata = self._interceptor.pre_delete_transfer_run(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataTransferServiceRestTransport._BaseDeleteTransferRun,
                    "_BaseDeleteTransferRun__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.bigquery.datatransfer_v1.DataTransferServiceClient.DeleteTransferRun",
                    extra={
                        "serviceName": "google.cloud.bigquery.datatransfer.v1.DataTransferService",
                        "rpcName": "DeleteTransferRun",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                DataTransferServiceRestTransport._DeleteTransferRun._get_response(
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

    class _EnrollDataSources(
        _BaseDataTransferServiceRestTransport._BaseEnrollDataSources,
        DataTransferServiceRestStub,
    ):
        def __hash__(self):
            return hash("DataTransferServiceRestTransport.EnrollDataSources")

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
            request: datatransfer.EnrollDataSourcesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the enroll data sources method over HTTP.

            Args:
                request (~.datatransfer.EnrollDataSourcesRequest):
                    The request object. A request to enroll a set of data sources so they are
                visible in the BigQuery UI's ``Transfer`` tab.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = _BaseDataTransferServiceRestTransport._BaseEnrollDataSources._get_http_options()
            request, metadata = self._interceptor.pre_enroll_data_sources(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataTransferServiceRestTransport._BaseEnrollDataSources,
                    "_BaseEnrollDataSources__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.bigquery.datatransfer_v1.DataTransferServiceClient.EnrollDataSources",
                    extra={
                        "serviceName": "google.cloud.bigquery.datatransfer.v1.DataTransferService",
                        "rpcName": "EnrollDataSources",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                DataTransferServiceRestTransport._EnrollDataSources._get_response(
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

    class _GetDataSource(
        _BaseDataTransferServiceRestTransport._BaseGetDataSource,
        DataTransferServiceRestStub,
    ):
        def __hash__(self):
            return hash("DataTransferServiceRestTransport.GetDataSource")

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
            request: datatransfer.GetDataSourceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> datatransfer.DataSource:
            r"""Call the get data source method over HTTP.

            Args:
                request (~.datatransfer.GetDataSourceRequest):
                    The request object. A request to get data source info.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.datatransfer.DataSource:
                    Defines the properties and custom
                parameters for a data source.

            """

            http_options = _BaseDataTransferServiceRestTransport._BaseGetDataSource._get_http_options()
            request, metadata = self._interceptor.pre_get_data_source(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataTransferServiceRestTransport._BaseGetDataSource,
                    "_BaseGetDataSource__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.bigquery.datatransfer_v1.DataTransferServiceClient.GetDataSource",
                    extra={
                        "serviceName": "google.cloud.bigquery.datatransfer.v1.DataTransferService",
                        "rpcName": "GetDataSource",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DataTransferServiceRestTransport._GetDataSource._get_response(
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
            resp = datatransfer.DataSource()
            pb_resp = datatransfer.DataSource.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_data_source(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_data_source_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = datatransfer.DataSource.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.bigquery.datatransfer_v1.DataTransferServiceClient.get_data_source",
                    extra={
                        "serviceName": "google.cloud.bigquery.datatransfer.v1.DataTransferService",
                        "rpcName": "GetDataSource",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetTransferConfig(
        _BaseDataTransferServiceRestTransport._BaseGetTransferConfig,
        DataTransferServiceRestStub,
    ):
        def __hash__(self):
            return hash("DataTransferServiceRestTransport.GetTransferConfig")

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
            request: datatransfer.GetTransferConfigRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> transfer.TransferConfig:
            r"""Call the get transfer config method over HTTP.

            Args:
                request (~.datatransfer.GetTransferConfigRequest):
                    The request object. A request to get data transfer
                information.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.transfer.TransferConfig:
                    Represents a data transfer configuration. A transfer
                configuration contains all metadata needed to perform a
                data transfer. For example, ``destination_dataset_id``
                specifies where data should be stored. When a new
                transfer configuration is created, the specified
                ``destination_dataset_id`` is created when needed and
                shared with the appropriate data source service account.

            """

            http_options = _BaseDataTransferServiceRestTransport._BaseGetTransferConfig._get_http_options()
            request, metadata = self._interceptor.pre_get_transfer_config(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataTransferServiceRestTransport._BaseGetTransferConfig,
                    "_BaseGetTransferConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.bigquery.datatransfer_v1.DataTransferServiceClient.GetTransferConfig",
                    extra={
                        "serviceName": "google.cloud.bigquery.datatransfer.v1.DataTransferService",
                        "rpcName": "GetTransferConfig",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                DataTransferServiceRestTransport._GetTransferConfig._get_response(
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
            resp = transfer.TransferConfig()
            pb_resp = transfer.TransferConfig.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_transfer_config(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_transfer_config_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = transfer.TransferConfig.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.bigquery.datatransfer_v1.DataTransferServiceClient.get_transfer_config",
                    extra={
                        "serviceName": "google.cloud.bigquery.datatransfer.v1.DataTransferService",
                        "rpcName": "GetTransferConfig",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetTransferRun(
        _BaseDataTransferServiceRestTransport._BaseGetTransferRun,
        DataTransferServiceRestStub,
    ):
        def __hash__(self):
            return hash("DataTransferServiceRestTransport.GetTransferRun")

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
            request: datatransfer.GetTransferRunRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> transfer.TransferRun:
            r"""Call the get transfer run method over HTTP.

            Args:
                request (~.datatransfer.GetTransferRunRequest):
                    The request object. A request to get data transfer run
                information.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.transfer.TransferRun:
                    Represents a data transfer run.
            """

            http_options = _BaseDataTransferServiceRestTransport._BaseGetTransferRun._get_http_options()
            request, metadata = self._interceptor.pre_get_transfer_run(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataTransferServiceRestTransport._BaseGetTransferRun,
                    "_BaseGetTransferRun__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.bigquery.datatransfer_v1.DataTransferServiceClient.GetTransferRun",
                    extra={
                        "serviceName": "google.cloud.bigquery.datatransfer.v1.DataTransferService",
                        "rpcName": "GetTransferRun",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DataTransferServiceRestTransport._GetTransferRun._get_response(
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
            resp = transfer.TransferRun()
            pb_resp = transfer.TransferRun.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_transfer_run(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_transfer_run_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = transfer.TransferRun.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.bigquery.datatransfer_v1.DataTransferServiceClient.get_transfer_run",
                    extra={
                        "serviceName": "google.cloud.bigquery.datatransfer.v1.DataTransferService",
                        "rpcName": "GetTransferRun",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListDataSources(
        _BaseDataTransferServiceRestTransport._BaseListDataSources,
        DataTransferServiceRestStub,
    ):
        def __hash__(self):
            return hash("DataTransferServiceRestTransport.ListDataSources")

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
            request: datatransfer.ListDataSourcesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> datatransfer.ListDataSourcesResponse:
            r"""Call the list data sources method over HTTP.

            Args:
                request (~.datatransfer.ListDataSourcesRequest):
                    The request object. Request to list supported data
                sources and their data transfer
                settings.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.datatransfer.ListDataSourcesResponse:
                    Returns list of supported data
                sources and their metadata.

            """

            http_options = _BaseDataTransferServiceRestTransport._BaseListDataSources._get_http_options()
            request, metadata = self._interceptor.pre_list_data_sources(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataTransferServiceRestTransport._BaseListDataSources,
                    "_BaseListDataSources__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.bigquery.datatransfer_v1.DataTransferServiceClient.ListDataSources",
                    extra={
                        "serviceName": "google.cloud.bigquery.datatransfer.v1.DataTransferService",
                        "rpcName": "ListDataSources",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DataTransferServiceRestTransport._ListDataSources._get_response(
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
            resp = datatransfer.ListDataSourcesResponse()
            pb_resp = datatransfer.ListDataSourcesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_data_sources(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_data_sources_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = datatransfer.ListDataSourcesResponse.to_json(
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
                    "Received response for google.cloud.bigquery.datatransfer_v1.DataTransferServiceClient.list_data_sources",
                    extra={
                        "serviceName": "google.cloud.bigquery.datatransfer.v1.DataTransferService",
                        "rpcName": "ListDataSources",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListTransferConfigs(
        _BaseDataTransferServiceRestTransport._BaseListTransferConfigs,
        DataTransferServiceRestStub,
    ):
        def __hash__(self):
            return hash("DataTransferServiceRestTransport.ListTransferConfigs")

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
            request: datatransfer.ListTransferConfigsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> datatransfer.ListTransferConfigsResponse:
            r"""Call the list transfer configs method over HTTP.

            Args:
                request (~.datatransfer.ListTransferConfigsRequest):
                    The request object. A request to list data transfers
                configured for a BigQuery project.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.datatransfer.ListTransferConfigsResponse:
                    The returned list of pipelines in the
                project.

            """

            http_options = _BaseDataTransferServiceRestTransport._BaseListTransferConfigs._get_http_options()
            request, metadata = self._interceptor.pre_list_transfer_configs(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataTransferServiceRestTransport._BaseListTransferConfigs,
                    "_BaseListTransferConfigs__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.bigquery.datatransfer_v1.DataTransferServiceClient.ListTransferConfigs",
                    extra={
                        "serviceName": "google.cloud.bigquery.datatransfer.v1.DataTransferService",
                        "rpcName": "ListTransferConfigs",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                DataTransferServiceRestTransport._ListTransferConfigs._get_response(
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
            resp = datatransfer.ListTransferConfigsResponse()
            pb_resp = datatransfer.ListTransferConfigsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_transfer_configs(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_transfer_configs_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = datatransfer.ListTransferConfigsResponse.to_json(
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
                    "Received response for google.cloud.bigquery.datatransfer_v1.DataTransferServiceClient.list_transfer_configs",
                    extra={
                        "serviceName": "google.cloud.bigquery.datatransfer.v1.DataTransferService",
                        "rpcName": "ListTransferConfigs",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListTransferLogs(
        _BaseDataTransferServiceRestTransport._BaseListTransferLogs,
        DataTransferServiceRestStub,
    ):
        def __hash__(self):
            return hash("DataTransferServiceRestTransport.ListTransferLogs")

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
            request: datatransfer.ListTransferLogsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> datatransfer.ListTransferLogsResponse:
            r"""Call the list transfer logs method over HTTP.

            Args:
                request (~.datatransfer.ListTransferLogsRequest):
                    The request object. A request to get user facing log
                messages associated with data transfer
                run.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.datatransfer.ListTransferLogsResponse:
                    The returned list transfer run
                messages.

            """

            http_options = _BaseDataTransferServiceRestTransport._BaseListTransferLogs._get_http_options()
            request, metadata = self._interceptor.pre_list_transfer_logs(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataTransferServiceRestTransport._BaseListTransferLogs,
                    "_BaseListTransferLogs__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.bigquery.datatransfer_v1.DataTransferServiceClient.ListTransferLogs",
                    extra={
                        "serviceName": "google.cloud.bigquery.datatransfer.v1.DataTransferService",
                        "rpcName": "ListTransferLogs",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DataTransferServiceRestTransport._ListTransferLogs._get_response(
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
            resp = datatransfer.ListTransferLogsResponse()
            pb_resp = datatransfer.ListTransferLogsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_transfer_logs(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_transfer_logs_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = datatransfer.ListTransferLogsResponse.to_json(
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
                    "Received response for google.cloud.bigquery.datatransfer_v1.DataTransferServiceClient.list_transfer_logs",
                    extra={
                        "serviceName": "google.cloud.bigquery.datatransfer.v1.DataTransferService",
                        "rpcName": "ListTransferLogs",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListTransferRuns(
        _BaseDataTransferServiceRestTransport._BaseListTransferRuns,
        DataTransferServiceRestStub,
    ):
        def __hash__(self):
            return hash("DataTransferServiceRestTransport.ListTransferRuns")

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
            request: datatransfer.ListTransferRunsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> datatransfer.ListTransferRunsResponse:
            r"""Call the list transfer runs method over HTTP.

            Args:
                request (~.datatransfer.ListTransferRunsRequest):
                    The request object. A request to list data transfer runs.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.datatransfer.ListTransferRunsResponse:
                    The returned list of pipelines in the
                project.

            """

            http_options = _BaseDataTransferServiceRestTransport._BaseListTransferRuns._get_http_options()
            request, metadata = self._interceptor.pre_list_transfer_runs(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataTransferServiceRestTransport._BaseListTransferRuns,
                    "_BaseListTransferRuns__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.bigquery.datatransfer_v1.DataTransferServiceClient.ListTransferRuns",
                    extra={
                        "serviceName": "google.cloud.bigquery.datatransfer.v1.DataTransferService",
                        "rpcName": "ListTransferRuns",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DataTransferServiceRestTransport._ListTransferRuns._get_response(
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
            resp = datatransfer.ListTransferRunsResponse()
            pb_resp = datatransfer.ListTransferRunsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_transfer_runs(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_transfer_runs_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = datatransfer.ListTransferRunsResponse.to_json(
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
                    "Received response for google.cloud.bigquery.datatransfer_v1.DataTransferServiceClient.list_transfer_runs",
                    extra={
                        "serviceName": "google.cloud.bigquery.datatransfer.v1.DataTransferService",
                        "rpcName": "ListTransferRuns",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ScheduleTransferRuns(
        _BaseDataTransferServiceRestTransport._BaseScheduleTransferRuns,
        DataTransferServiceRestStub,
    ):
        def __hash__(self):
            return hash("DataTransferServiceRestTransport.ScheduleTransferRuns")

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
            request: datatransfer.ScheduleTransferRunsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> datatransfer.ScheduleTransferRunsResponse:
            r"""Call the schedule transfer runs method over HTTP.

            Args:
                request (~.datatransfer.ScheduleTransferRunsRequest):
                    The request object. A request to schedule transfer runs
                for a time range.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.datatransfer.ScheduleTransferRunsResponse:
                    A response to schedule transfer runs
                for a time range.

            """

            http_options = _BaseDataTransferServiceRestTransport._BaseScheduleTransferRuns._get_http_options()
            request, metadata = self._interceptor.pre_schedule_transfer_runs(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataTransferServiceRestTransport._BaseScheduleTransferRuns,
                    "_BaseScheduleTransferRuns__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.bigquery.datatransfer_v1.DataTransferServiceClient.ScheduleTransferRuns",
                    extra={
                        "serviceName": "google.cloud.bigquery.datatransfer.v1.DataTransferService",
                        "rpcName": "ScheduleTransferRuns",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                DataTransferServiceRestTransport._ScheduleTransferRuns._get_response(
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
            resp = datatransfer.ScheduleTransferRunsResponse()
            pb_resp = datatransfer.ScheduleTransferRunsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_schedule_transfer_runs(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_schedule_transfer_runs_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        datatransfer.ScheduleTransferRunsResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.bigquery.datatransfer_v1.DataTransferServiceClient.schedule_transfer_runs",
                    extra={
                        "serviceName": "google.cloud.bigquery.datatransfer.v1.DataTransferService",
                        "rpcName": "ScheduleTransferRuns",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _StartManualTransferRuns(
        _BaseDataTransferServiceRestTransport._BaseStartManualTransferRuns,
        DataTransferServiceRestStub,
    ):
        def __hash__(self):
            return hash("DataTransferServiceRestTransport.StartManualTransferRuns")

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
            request: datatransfer.StartManualTransferRunsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> datatransfer.StartManualTransferRunsResponse:
            r"""Call the start manual transfer
            runs method over HTTP.

                Args:
                    request (~.datatransfer.StartManualTransferRunsRequest):
                        The request object. A request to start manual transfer
                    runs.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.datatransfer.StartManualTransferRunsResponse:
                        A response to start manual transfer
                    runs.

            """

            http_options = _BaseDataTransferServiceRestTransport._BaseStartManualTransferRuns._get_http_options()
            request, metadata = self._interceptor.pre_start_manual_transfer_runs(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataTransferServiceRestTransport._BaseStartManualTransferRuns,
                    "_BaseStartManualTransferRuns__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.bigquery.datatransfer_v1.DataTransferServiceClient.StartManualTransferRuns",
                    extra={
                        "serviceName": "google.cloud.bigquery.datatransfer.v1.DataTransferService",
                        "rpcName": "StartManualTransferRuns",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                DataTransferServiceRestTransport._StartManualTransferRuns._get_response(
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
            resp = datatransfer.StartManualTransferRunsResponse()
            pb_resp = datatransfer.StartManualTransferRunsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_start_manual_transfer_runs(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_start_manual_transfer_runs_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        datatransfer.StartManualTransferRunsResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.bigquery.datatransfer_v1.DataTransferServiceClient.start_manual_transfer_runs",
                    extra={
                        "serviceName": "google.cloud.bigquery.datatransfer.v1.DataTransferService",
                        "rpcName": "StartManualTransferRuns",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UnenrollDataSources(
        _BaseDataTransferServiceRestTransport._BaseUnenrollDataSources,
        DataTransferServiceRestStub,
    ):
        def __hash__(self):
            return hash("DataTransferServiceRestTransport.UnenrollDataSources")

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
            request: datatransfer.UnenrollDataSourcesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the unenroll data sources method over HTTP.

            Args:
                request (~.datatransfer.UnenrollDataSourcesRequest):
                    The request object. A request to unenroll a set of data sources so they are
                no longer visible in the BigQuery UI's ``Transfer`` tab.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = _BaseDataTransferServiceRestTransport._BaseUnenrollDataSources._get_http_options()
            request, metadata = self._interceptor.pre_unenroll_data_sources(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataTransferServiceRestTransport._BaseUnenrollDataSources,
                    "_BaseUnenrollDataSources__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.bigquery.datatransfer_v1.DataTransferServiceClient.UnenrollDataSources",
                    extra={
                        "serviceName": "google.cloud.bigquery.datatransfer.v1.DataTransferService",
                        "rpcName": "UnenrollDataSources",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                DataTransferServiceRestTransport._UnenrollDataSources._get_response(
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

    class _UpdateTransferConfig(
        _BaseDataTransferServiceRestTransport._BaseUpdateTransferConfig,
        DataTransferServiceRestStub,
    ):
        def __hash__(self):
            return hash("DataTransferServiceRestTransport.UpdateTransferConfig")

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
            request: datatransfer.UpdateTransferConfigRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> transfer.TransferConfig:
            r"""Call the update transfer config method over HTTP.

            Args:
                request (~.datatransfer.UpdateTransferConfigRequest):
                    The request object. A request to update a transfer configuration. To update
                the user id of the transfer configuration, authorization
                info needs to be provided.

                When using a cross project service account for updating
                a transfer config, you must enable cross project service
                account usage. For more information, see `Disable
                attachment of service accounts to resources in other
                projects <https://cloud.google.com/resource-manager/docs/organization-policy/restricting-service-accounts#disable_cross_project_service_accounts>`__.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.transfer.TransferConfig:
                    Represents a data transfer configuration. A transfer
                configuration contains all metadata needed to perform a
                data transfer. For example, ``destination_dataset_id``
                specifies where data should be stored. When a new
                transfer configuration is created, the specified
                ``destination_dataset_id`` is created when needed and
                shared with the appropriate data source service account.

            """

            http_options = _BaseDataTransferServiceRestTransport._BaseUpdateTransferConfig._get_http_options()
            request, metadata = self._interceptor.pre_update_transfer_config(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataTransferServiceRestTransport._BaseUpdateTransferConfig,
                    "_BaseUpdateTransferConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.bigquery.datatransfer_v1.DataTransferServiceClient.UpdateTransferConfig",
                    extra={
                        "serviceName": "google.cloud.bigquery.datatransfer.v1.DataTransferService",
                        "rpcName": "UpdateTransferConfig",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                DataTransferServiceRestTransport._UpdateTransferConfig._get_response(
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
            resp = transfer.TransferConfig()
            pb_resp = transfer.TransferConfig.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_transfer_config(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_transfer_config_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = transfer.TransferConfig.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.bigquery.datatransfer_v1.DataTransferServiceClient.update_transfer_config",
                    extra={
                        "serviceName": "google.cloud.bigquery.datatransfer.v1.DataTransferService",
                        "rpcName": "UpdateTransferConfig",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def check_valid_creds(
        self,
    ) -> Callable[
        [datatransfer.CheckValidCredsRequest], datatransfer.CheckValidCredsResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CheckValidCreds(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_transfer_config(
        self,
    ) -> Callable[[datatransfer.CreateTransferConfigRequest], transfer.TransferConfig]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateTransferConfig(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_transfer_config(
        self,
    ) -> Callable[[datatransfer.DeleteTransferConfigRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteTransferConfig(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_transfer_run(
        self,
    ) -> Callable[[datatransfer.DeleteTransferRunRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteTransferRun(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def enroll_data_sources(
        self,
    ) -> Callable[[datatransfer.EnrollDataSourcesRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._EnrollDataSources(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_data_source(
        self,
    ) -> Callable[[datatransfer.GetDataSourceRequest], datatransfer.DataSource]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetDataSource(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_transfer_config(
        self,
    ) -> Callable[[datatransfer.GetTransferConfigRequest], transfer.TransferConfig]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetTransferConfig(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_transfer_run(
        self,
    ) -> Callable[[datatransfer.GetTransferRunRequest], transfer.TransferRun]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetTransferRun(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_data_sources(
        self,
    ) -> Callable[
        [datatransfer.ListDataSourcesRequest], datatransfer.ListDataSourcesResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListDataSources(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_transfer_configs(
        self,
    ) -> Callable[
        [datatransfer.ListTransferConfigsRequest],
        datatransfer.ListTransferConfigsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListTransferConfigs(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_transfer_logs(
        self,
    ) -> Callable[
        [datatransfer.ListTransferLogsRequest], datatransfer.ListTransferLogsResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListTransferLogs(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_transfer_runs(
        self,
    ) -> Callable[
        [datatransfer.ListTransferRunsRequest], datatransfer.ListTransferRunsResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListTransferRuns(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def schedule_transfer_runs(
        self,
    ) -> Callable[
        [datatransfer.ScheduleTransferRunsRequest],
        datatransfer.ScheduleTransferRunsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ScheduleTransferRuns(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def start_manual_transfer_runs(
        self,
    ) -> Callable[
        [datatransfer.StartManualTransferRunsRequest],
        datatransfer.StartManualTransferRunsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._StartManualTransferRuns(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def unenroll_data_sources(
        self,
    ) -> Callable[[datatransfer.UnenrollDataSourcesRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UnenrollDataSources(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_transfer_config(
        self,
    ) -> Callable[[datatransfer.UpdateTransferConfigRequest], transfer.TransferConfig]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateTransferConfig(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_location(self):
        return self._GetLocation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetLocation(
        _BaseDataTransferServiceRestTransport._BaseGetLocation,
        DataTransferServiceRestStub,
    ):
        def __hash__(self):
            return hash("DataTransferServiceRestTransport.GetLocation")

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

            http_options = _BaseDataTransferServiceRestTransport._BaseGetLocation._get_http_options()
            request, metadata = self._interceptor.pre_get_location(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataTransferServiceRestTransport._BaseGetLocation,
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
                    f"Sending request for google.cloud.bigquery.datatransfer_v1.DataTransferServiceClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.bigquery.datatransfer.v1.DataTransferService",
                        "rpcName": "GetLocation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DataTransferServiceRestTransport._GetLocation._get_response(
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
                    "Received response for google.cloud.bigquery.datatransfer_v1.DataTransferServiceAsyncClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.bigquery.datatransfer.v1.DataTransferService",
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
        _BaseDataTransferServiceRestTransport._BaseListLocations,
        DataTransferServiceRestStub,
    ):
        def __hash__(self):
            return hash("DataTransferServiceRestTransport.ListLocations")

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

            http_options = _BaseDataTransferServiceRestTransport._BaseListLocations._get_http_options()
            request, metadata = self._interceptor.pre_list_locations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataTransferServiceRestTransport._BaseListLocations,
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
                    f"Sending request for google.cloud.bigquery.datatransfer_v1.DataTransferServiceClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.bigquery.datatransfer.v1.DataTransferService",
                        "rpcName": "ListLocations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DataTransferServiceRestTransport._ListLocations._get_response(
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
                    "Received response for google.cloud.bigquery.datatransfer_v1.DataTransferServiceAsyncClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.bigquery.datatransfer.v1.DataTransferService",
                        "rpcName": "ListLocations",
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


__all__ = ("DataTransferServiceRestTransport",)
