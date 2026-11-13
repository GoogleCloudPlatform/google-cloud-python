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

from google.cloud.websecurityscanner_v1alpha._compat import transcode_request
from google.cloud.websecurityscanner_v1alpha.types import (
    finding,
    scan_config,
    scan_run,
    web_security_scanner,
)
from google.cloud.websecurityscanner_v1alpha.types import scan_config as gcw_scan_config

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseWebSecurityScannerRestTransport

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


class WebSecurityScannerRestInterceptor:
    """Interceptor for WebSecurityScanner.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the WebSecurityScannerRestTransport.

    .. code-block:: python
        class MyCustomWebSecurityScannerInterceptor(WebSecurityScannerRestInterceptor):
            def pre_create_scan_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_scan_config(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_scan_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_get_finding(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_finding(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_scan_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_scan_config(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_scan_run(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_scan_run(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_crawled_urls(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_crawled_urls(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_findings(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_findings(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_finding_type_stats(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_finding_type_stats(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_scan_configs(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_scan_configs(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_scan_runs(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_scan_runs(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_start_scan_run(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_start_scan_run(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_stop_scan_run(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_stop_scan_run(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_scan_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_scan_config(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = WebSecurityScannerRestTransport(interceptor=MyCustomWebSecurityScannerInterceptor())
        client = WebSecurityScannerClient(transport=transport)


    """

    def pre_create_scan_config(
        self,
        request: web_security_scanner.CreateScanConfigRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        web_security_scanner.CreateScanConfigRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_scan_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the WebSecurityScanner server.
        """
        return request, metadata

    def post_create_scan_config(
        self, response: gcw_scan_config.ScanConfig
    ) -> gcw_scan_config.ScanConfig:
        """Post-rpc interceptor for create_scan_config

        DEPRECATED. Please use the `post_create_scan_config_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the WebSecurityScanner server but before
        it is returned to user code. This `post_create_scan_config` interceptor runs
        before the `post_create_scan_config_with_metadata` interceptor.
        """
        return response

    def post_create_scan_config_with_metadata(
        self,
        response: gcw_scan_config.ScanConfig,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[gcw_scan_config.ScanConfig, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_scan_config

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the WebSecurityScanner server but before it is returned to user code.

        We recommend only using this `post_create_scan_config_with_metadata`
        interceptor in new development instead of the `post_create_scan_config` interceptor.
        When both interceptors are used, this `post_create_scan_config_with_metadata` interceptor runs after the
        `post_create_scan_config` interceptor. The (possibly modified) response returned by
        `post_create_scan_config` will be passed to
        `post_create_scan_config_with_metadata`.
        """
        return response, metadata

    def pre_delete_scan_config(
        self,
        request: web_security_scanner.DeleteScanConfigRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        web_security_scanner.DeleteScanConfigRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_scan_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the WebSecurityScanner server.
        """
        return request, metadata

    def pre_get_finding(
        self,
        request: web_security_scanner.GetFindingRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        web_security_scanner.GetFindingRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_finding

        Override in a subclass to manipulate the request or metadata
        before they are sent to the WebSecurityScanner server.
        """
        return request, metadata

    def post_get_finding(self, response: finding.Finding) -> finding.Finding:
        """Post-rpc interceptor for get_finding

        DEPRECATED. Please use the `post_get_finding_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the WebSecurityScanner server but before
        it is returned to user code. This `post_get_finding` interceptor runs
        before the `post_get_finding_with_metadata` interceptor.
        """
        return response

    def post_get_finding_with_metadata(
        self,
        response: finding.Finding,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[finding.Finding, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_finding

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the WebSecurityScanner server but before it is returned to user code.

        We recommend only using this `post_get_finding_with_metadata`
        interceptor in new development instead of the `post_get_finding` interceptor.
        When both interceptors are used, this `post_get_finding_with_metadata` interceptor runs after the
        `post_get_finding` interceptor. The (possibly modified) response returned by
        `post_get_finding` will be passed to
        `post_get_finding_with_metadata`.
        """
        return response, metadata

    def pre_get_scan_config(
        self,
        request: web_security_scanner.GetScanConfigRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        web_security_scanner.GetScanConfigRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_scan_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the WebSecurityScanner server.
        """
        return request, metadata

    def post_get_scan_config(
        self, response: scan_config.ScanConfig
    ) -> scan_config.ScanConfig:
        """Post-rpc interceptor for get_scan_config

        DEPRECATED. Please use the `post_get_scan_config_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the WebSecurityScanner server but before
        it is returned to user code. This `post_get_scan_config` interceptor runs
        before the `post_get_scan_config_with_metadata` interceptor.
        """
        return response

    def post_get_scan_config_with_metadata(
        self,
        response: scan_config.ScanConfig,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[scan_config.ScanConfig, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_scan_config

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the WebSecurityScanner server but before it is returned to user code.

        We recommend only using this `post_get_scan_config_with_metadata`
        interceptor in new development instead of the `post_get_scan_config` interceptor.
        When both interceptors are used, this `post_get_scan_config_with_metadata` interceptor runs after the
        `post_get_scan_config` interceptor. The (possibly modified) response returned by
        `post_get_scan_config` will be passed to
        `post_get_scan_config_with_metadata`.
        """
        return response, metadata

    def pre_get_scan_run(
        self,
        request: web_security_scanner.GetScanRunRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        web_security_scanner.GetScanRunRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_scan_run

        Override in a subclass to manipulate the request or metadata
        before they are sent to the WebSecurityScanner server.
        """
        return request, metadata

    def post_get_scan_run(self, response: scan_run.ScanRun) -> scan_run.ScanRun:
        """Post-rpc interceptor for get_scan_run

        DEPRECATED. Please use the `post_get_scan_run_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the WebSecurityScanner server but before
        it is returned to user code. This `post_get_scan_run` interceptor runs
        before the `post_get_scan_run_with_metadata` interceptor.
        """
        return response

    def post_get_scan_run_with_metadata(
        self,
        response: scan_run.ScanRun,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[scan_run.ScanRun, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_scan_run

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the WebSecurityScanner server but before it is returned to user code.

        We recommend only using this `post_get_scan_run_with_metadata`
        interceptor in new development instead of the `post_get_scan_run` interceptor.
        When both interceptors are used, this `post_get_scan_run_with_metadata` interceptor runs after the
        `post_get_scan_run` interceptor. The (possibly modified) response returned by
        `post_get_scan_run` will be passed to
        `post_get_scan_run_with_metadata`.
        """
        return response, metadata

    def pre_list_crawled_urls(
        self,
        request: web_security_scanner.ListCrawledUrlsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        web_security_scanner.ListCrawledUrlsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_crawled_urls

        Override in a subclass to manipulate the request or metadata
        before they are sent to the WebSecurityScanner server.
        """
        return request, metadata

    def post_list_crawled_urls(
        self, response: web_security_scanner.ListCrawledUrlsResponse
    ) -> web_security_scanner.ListCrawledUrlsResponse:
        """Post-rpc interceptor for list_crawled_urls

        DEPRECATED. Please use the `post_list_crawled_urls_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the WebSecurityScanner server but before
        it is returned to user code. This `post_list_crawled_urls` interceptor runs
        before the `post_list_crawled_urls_with_metadata` interceptor.
        """
        return response

    def post_list_crawled_urls_with_metadata(
        self,
        response: web_security_scanner.ListCrawledUrlsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        web_security_scanner.ListCrawledUrlsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_crawled_urls

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the WebSecurityScanner server but before it is returned to user code.

        We recommend only using this `post_list_crawled_urls_with_metadata`
        interceptor in new development instead of the `post_list_crawled_urls` interceptor.
        When both interceptors are used, this `post_list_crawled_urls_with_metadata` interceptor runs after the
        `post_list_crawled_urls` interceptor. The (possibly modified) response returned by
        `post_list_crawled_urls` will be passed to
        `post_list_crawled_urls_with_metadata`.
        """
        return response, metadata

    def pre_list_findings(
        self,
        request: web_security_scanner.ListFindingsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        web_security_scanner.ListFindingsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_findings

        Override in a subclass to manipulate the request or metadata
        before they are sent to the WebSecurityScanner server.
        """
        return request, metadata

    def post_list_findings(
        self, response: web_security_scanner.ListFindingsResponse
    ) -> web_security_scanner.ListFindingsResponse:
        """Post-rpc interceptor for list_findings

        DEPRECATED. Please use the `post_list_findings_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the WebSecurityScanner server but before
        it is returned to user code. This `post_list_findings` interceptor runs
        before the `post_list_findings_with_metadata` interceptor.
        """
        return response

    def post_list_findings_with_metadata(
        self,
        response: web_security_scanner.ListFindingsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        web_security_scanner.ListFindingsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_findings

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the WebSecurityScanner server but before it is returned to user code.

        We recommend only using this `post_list_findings_with_metadata`
        interceptor in new development instead of the `post_list_findings` interceptor.
        When both interceptors are used, this `post_list_findings_with_metadata` interceptor runs after the
        `post_list_findings` interceptor. The (possibly modified) response returned by
        `post_list_findings` will be passed to
        `post_list_findings_with_metadata`.
        """
        return response, metadata

    def pre_list_finding_type_stats(
        self,
        request: web_security_scanner.ListFindingTypeStatsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        web_security_scanner.ListFindingTypeStatsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_finding_type_stats

        Override in a subclass to manipulate the request or metadata
        before they are sent to the WebSecurityScanner server.
        """
        return request, metadata

    def post_list_finding_type_stats(
        self, response: web_security_scanner.ListFindingTypeStatsResponse
    ) -> web_security_scanner.ListFindingTypeStatsResponse:
        """Post-rpc interceptor for list_finding_type_stats

        DEPRECATED. Please use the `post_list_finding_type_stats_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the WebSecurityScanner server but before
        it is returned to user code. This `post_list_finding_type_stats` interceptor runs
        before the `post_list_finding_type_stats_with_metadata` interceptor.
        """
        return response

    def post_list_finding_type_stats_with_metadata(
        self,
        response: web_security_scanner.ListFindingTypeStatsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        web_security_scanner.ListFindingTypeStatsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_finding_type_stats

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the WebSecurityScanner server but before it is returned to user code.

        We recommend only using this `post_list_finding_type_stats_with_metadata`
        interceptor in new development instead of the `post_list_finding_type_stats` interceptor.
        When both interceptors are used, this `post_list_finding_type_stats_with_metadata` interceptor runs after the
        `post_list_finding_type_stats` interceptor. The (possibly modified) response returned by
        `post_list_finding_type_stats` will be passed to
        `post_list_finding_type_stats_with_metadata`.
        """
        return response, metadata

    def pre_list_scan_configs(
        self,
        request: web_security_scanner.ListScanConfigsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        web_security_scanner.ListScanConfigsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_scan_configs

        Override in a subclass to manipulate the request or metadata
        before they are sent to the WebSecurityScanner server.
        """
        return request, metadata

    def post_list_scan_configs(
        self, response: web_security_scanner.ListScanConfigsResponse
    ) -> web_security_scanner.ListScanConfigsResponse:
        """Post-rpc interceptor for list_scan_configs

        DEPRECATED. Please use the `post_list_scan_configs_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the WebSecurityScanner server but before
        it is returned to user code. This `post_list_scan_configs` interceptor runs
        before the `post_list_scan_configs_with_metadata` interceptor.
        """
        return response

    def post_list_scan_configs_with_metadata(
        self,
        response: web_security_scanner.ListScanConfigsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        web_security_scanner.ListScanConfigsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_scan_configs

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the WebSecurityScanner server but before it is returned to user code.

        We recommend only using this `post_list_scan_configs_with_metadata`
        interceptor in new development instead of the `post_list_scan_configs` interceptor.
        When both interceptors are used, this `post_list_scan_configs_with_metadata` interceptor runs after the
        `post_list_scan_configs` interceptor. The (possibly modified) response returned by
        `post_list_scan_configs` will be passed to
        `post_list_scan_configs_with_metadata`.
        """
        return response, metadata

    def pre_list_scan_runs(
        self,
        request: web_security_scanner.ListScanRunsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        web_security_scanner.ListScanRunsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_scan_runs

        Override in a subclass to manipulate the request or metadata
        before they are sent to the WebSecurityScanner server.
        """
        return request, metadata

    def post_list_scan_runs(
        self, response: web_security_scanner.ListScanRunsResponse
    ) -> web_security_scanner.ListScanRunsResponse:
        """Post-rpc interceptor for list_scan_runs

        DEPRECATED. Please use the `post_list_scan_runs_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the WebSecurityScanner server but before
        it is returned to user code. This `post_list_scan_runs` interceptor runs
        before the `post_list_scan_runs_with_metadata` interceptor.
        """
        return response

    def post_list_scan_runs_with_metadata(
        self,
        response: web_security_scanner.ListScanRunsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        web_security_scanner.ListScanRunsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_scan_runs

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the WebSecurityScanner server but before it is returned to user code.

        We recommend only using this `post_list_scan_runs_with_metadata`
        interceptor in new development instead of the `post_list_scan_runs` interceptor.
        When both interceptors are used, this `post_list_scan_runs_with_metadata` interceptor runs after the
        `post_list_scan_runs` interceptor. The (possibly modified) response returned by
        `post_list_scan_runs` will be passed to
        `post_list_scan_runs_with_metadata`.
        """
        return response, metadata

    def pre_start_scan_run(
        self,
        request: web_security_scanner.StartScanRunRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        web_security_scanner.StartScanRunRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for start_scan_run

        Override in a subclass to manipulate the request or metadata
        before they are sent to the WebSecurityScanner server.
        """
        return request, metadata

    def post_start_scan_run(self, response: scan_run.ScanRun) -> scan_run.ScanRun:
        """Post-rpc interceptor for start_scan_run

        DEPRECATED. Please use the `post_start_scan_run_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the WebSecurityScanner server but before
        it is returned to user code. This `post_start_scan_run` interceptor runs
        before the `post_start_scan_run_with_metadata` interceptor.
        """
        return response

    def post_start_scan_run_with_metadata(
        self,
        response: scan_run.ScanRun,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[scan_run.ScanRun, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for start_scan_run

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the WebSecurityScanner server but before it is returned to user code.

        We recommend only using this `post_start_scan_run_with_metadata`
        interceptor in new development instead of the `post_start_scan_run` interceptor.
        When both interceptors are used, this `post_start_scan_run_with_metadata` interceptor runs after the
        `post_start_scan_run` interceptor. The (possibly modified) response returned by
        `post_start_scan_run` will be passed to
        `post_start_scan_run_with_metadata`.
        """
        return response, metadata

    def pre_stop_scan_run(
        self,
        request: web_security_scanner.StopScanRunRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        web_security_scanner.StopScanRunRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for stop_scan_run

        Override in a subclass to manipulate the request or metadata
        before they are sent to the WebSecurityScanner server.
        """
        return request, metadata

    def post_stop_scan_run(self, response: scan_run.ScanRun) -> scan_run.ScanRun:
        """Post-rpc interceptor for stop_scan_run

        DEPRECATED. Please use the `post_stop_scan_run_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the WebSecurityScanner server but before
        it is returned to user code. This `post_stop_scan_run` interceptor runs
        before the `post_stop_scan_run_with_metadata` interceptor.
        """
        return response

    def post_stop_scan_run_with_metadata(
        self,
        response: scan_run.ScanRun,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[scan_run.ScanRun, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for stop_scan_run

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the WebSecurityScanner server but before it is returned to user code.

        We recommend only using this `post_stop_scan_run_with_metadata`
        interceptor in new development instead of the `post_stop_scan_run` interceptor.
        When both interceptors are used, this `post_stop_scan_run_with_metadata` interceptor runs after the
        `post_stop_scan_run` interceptor. The (possibly modified) response returned by
        `post_stop_scan_run` will be passed to
        `post_stop_scan_run_with_metadata`.
        """
        return response, metadata

    def pre_update_scan_config(
        self,
        request: web_security_scanner.UpdateScanConfigRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        web_security_scanner.UpdateScanConfigRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_scan_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the WebSecurityScanner server.
        """
        return request, metadata

    def post_update_scan_config(
        self, response: gcw_scan_config.ScanConfig
    ) -> gcw_scan_config.ScanConfig:
        """Post-rpc interceptor for update_scan_config

        DEPRECATED. Please use the `post_update_scan_config_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the WebSecurityScanner server but before
        it is returned to user code. This `post_update_scan_config` interceptor runs
        before the `post_update_scan_config_with_metadata` interceptor.
        """
        return response

    def post_update_scan_config_with_metadata(
        self,
        response: gcw_scan_config.ScanConfig,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[gcw_scan_config.ScanConfig, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_scan_config

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the WebSecurityScanner server but before it is returned to user code.

        We recommend only using this `post_update_scan_config_with_metadata`
        interceptor in new development instead of the `post_update_scan_config` interceptor.
        When both interceptors are used, this `post_update_scan_config_with_metadata` interceptor runs after the
        `post_update_scan_config` interceptor. The (possibly modified) response returned by
        `post_update_scan_config` will be passed to
        `post_update_scan_config_with_metadata`.
        """
        return response, metadata


@dataclasses.dataclass
class WebSecurityScannerRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: WebSecurityScannerRestInterceptor


class WebSecurityScannerRestTransport(_BaseWebSecurityScannerRestTransport):
    """REST backend synchronous transport for WebSecurityScanner.

    Cloud Web Security Scanner Service identifies security
    vulnerabilities in web applications hosted on Google Cloud
    Platform. It crawls your application, and attempts to exercise
    as many user inputs and event handlers as possible.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "websecurityscanner.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[WebSecurityScannerRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'websecurityscanner.googleapis.com').
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
            interceptor (Optional[WebSecurityScannerRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or WebSecurityScannerRestInterceptor()
        self._prep_wrapped_messages(client_info)

    class _CreateScanConfig(
        _BaseWebSecurityScannerRestTransport._BaseCreateScanConfig,
        WebSecurityScannerRestStub,
    ):
        def __hash__(self):
            return hash("WebSecurityScannerRestTransport.CreateScanConfig")

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
            request: web_security_scanner.CreateScanConfigRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gcw_scan_config.ScanConfig:
            r"""Call the create scan config method over HTTP.

            Args:
                request (~.web_security_scanner.CreateScanConfigRequest):
                    The request object. Request for the ``CreateScanConfig`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.gcw_scan_config.ScanConfig:
                    A ScanConfig resource contains the
                configurations to launch a scan. next
                id: 12

            """

            http_options = _BaseWebSecurityScannerRestTransport._BaseCreateScanConfig._get_http_options()
            request, metadata = self._interceptor.pre_create_scan_config(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseWebSecurityScannerRestTransport._BaseCreateScanConfig,
                    "_BaseCreateScanConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.websecurityscanner_v1alpha.WebSecurityScannerClient.CreateScanConfig",
                    extra={
                        "serviceName": "google.cloud.websecurityscanner.v1alpha.WebSecurityScanner",
                        "rpcName": "CreateScanConfig",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = WebSecurityScannerRestTransport._CreateScanConfig._get_response(
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
            resp = gcw_scan_config.ScanConfig()
            pb_resp = gcw_scan_config.ScanConfig.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_scan_config(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_scan_config_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = gcw_scan_config.ScanConfig.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.websecurityscanner_v1alpha.WebSecurityScannerClient.create_scan_config",
                    extra={
                        "serviceName": "google.cloud.websecurityscanner.v1alpha.WebSecurityScanner",
                        "rpcName": "CreateScanConfig",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteScanConfig(
        _BaseWebSecurityScannerRestTransport._BaseDeleteScanConfig,
        WebSecurityScannerRestStub,
    ):
        def __hash__(self):
            return hash("WebSecurityScannerRestTransport.DeleteScanConfig")

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
            request: web_security_scanner.DeleteScanConfigRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete scan config method over HTTP.

            Args:
                request (~.web_security_scanner.DeleteScanConfigRequest):
                    The request object. Request for the ``DeleteScanConfig`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = _BaseWebSecurityScannerRestTransport._BaseDeleteScanConfig._get_http_options()
            request, metadata = self._interceptor.pre_delete_scan_config(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseWebSecurityScannerRestTransport._BaseDeleteScanConfig,
                    "_BaseDeleteScanConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.websecurityscanner_v1alpha.WebSecurityScannerClient.DeleteScanConfig",
                    extra={
                        "serviceName": "google.cloud.websecurityscanner.v1alpha.WebSecurityScanner",
                        "rpcName": "DeleteScanConfig",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = WebSecurityScannerRestTransport._DeleteScanConfig._get_response(
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

    class _GetFinding(
        _BaseWebSecurityScannerRestTransport._BaseGetFinding, WebSecurityScannerRestStub
    ):
        def __hash__(self):
            return hash("WebSecurityScannerRestTransport.GetFinding")

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
            request: web_security_scanner.GetFindingRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> finding.Finding:
            r"""Call the get finding method over HTTP.

            Args:
                request (~.web_security_scanner.GetFindingRequest):
                    The request object. Request for the ``GetFinding`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.finding.Finding:
                    A Finding resource represents a
                vulnerability instance identified during
                a ScanRun.

            """

            http_options = (
                _BaseWebSecurityScannerRestTransport._BaseGetFinding._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_finding(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseWebSecurityScannerRestTransport._BaseGetFinding,
                    "_BaseGetFinding__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.websecurityscanner_v1alpha.WebSecurityScannerClient.GetFinding",
                    extra={
                        "serviceName": "google.cloud.websecurityscanner.v1alpha.WebSecurityScanner",
                        "rpcName": "GetFinding",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = WebSecurityScannerRestTransport._GetFinding._get_response(
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
            resp = finding.Finding()
            pb_resp = finding.Finding.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_finding(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_finding_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = finding.Finding.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.websecurityscanner_v1alpha.WebSecurityScannerClient.get_finding",
                    extra={
                        "serviceName": "google.cloud.websecurityscanner.v1alpha.WebSecurityScanner",
                        "rpcName": "GetFinding",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetScanConfig(
        _BaseWebSecurityScannerRestTransport._BaseGetScanConfig,
        WebSecurityScannerRestStub,
    ):
        def __hash__(self):
            return hash("WebSecurityScannerRestTransport.GetScanConfig")

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
            request: web_security_scanner.GetScanConfigRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> scan_config.ScanConfig:
            r"""Call the get scan config method over HTTP.

            Args:
                request (~.web_security_scanner.GetScanConfigRequest):
                    The request object. Request for the ``GetScanConfig`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.scan_config.ScanConfig:
                    A ScanConfig resource contains the
                configurations to launch a scan. next
                id: 12

            """

            http_options = _BaseWebSecurityScannerRestTransport._BaseGetScanConfig._get_http_options()
            request, metadata = self._interceptor.pre_get_scan_config(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseWebSecurityScannerRestTransport._BaseGetScanConfig,
                    "_BaseGetScanConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.websecurityscanner_v1alpha.WebSecurityScannerClient.GetScanConfig",
                    extra={
                        "serviceName": "google.cloud.websecurityscanner.v1alpha.WebSecurityScanner",
                        "rpcName": "GetScanConfig",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = WebSecurityScannerRestTransport._GetScanConfig._get_response(
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
            resp = scan_config.ScanConfig()
            pb_resp = scan_config.ScanConfig.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_scan_config(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_scan_config_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = scan_config.ScanConfig.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.websecurityscanner_v1alpha.WebSecurityScannerClient.get_scan_config",
                    extra={
                        "serviceName": "google.cloud.websecurityscanner.v1alpha.WebSecurityScanner",
                        "rpcName": "GetScanConfig",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetScanRun(
        _BaseWebSecurityScannerRestTransport._BaseGetScanRun, WebSecurityScannerRestStub
    ):
        def __hash__(self):
            return hash("WebSecurityScannerRestTransport.GetScanRun")

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
            request: web_security_scanner.GetScanRunRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> scan_run.ScanRun:
            r"""Call the get scan run method over HTTP.

            Args:
                request (~.web_security_scanner.GetScanRunRequest):
                    The request object. Request for the ``GetScanRun`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.scan_run.ScanRun:
                    A ScanRun is a output-only resource
                representing an actual run of the scan.

            """

            http_options = (
                _BaseWebSecurityScannerRestTransport._BaseGetScanRun._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_scan_run(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseWebSecurityScannerRestTransport._BaseGetScanRun,
                    "_BaseGetScanRun__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.websecurityscanner_v1alpha.WebSecurityScannerClient.GetScanRun",
                    extra={
                        "serviceName": "google.cloud.websecurityscanner.v1alpha.WebSecurityScanner",
                        "rpcName": "GetScanRun",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = WebSecurityScannerRestTransport._GetScanRun._get_response(
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
            resp = scan_run.ScanRun()
            pb_resp = scan_run.ScanRun.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_scan_run(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_scan_run_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = scan_run.ScanRun.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.websecurityscanner_v1alpha.WebSecurityScannerClient.get_scan_run",
                    extra={
                        "serviceName": "google.cloud.websecurityscanner.v1alpha.WebSecurityScanner",
                        "rpcName": "GetScanRun",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListCrawledUrls(
        _BaseWebSecurityScannerRestTransport._BaseListCrawledUrls,
        WebSecurityScannerRestStub,
    ):
        def __hash__(self):
            return hash("WebSecurityScannerRestTransport.ListCrawledUrls")

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
            request: web_security_scanner.ListCrawledUrlsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> web_security_scanner.ListCrawledUrlsResponse:
            r"""Call the list crawled urls method over HTTP.

            Args:
                request (~.web_security_scanner.ListCrawledUrlsRequest):
                    The request object. Request for the ``ListCrawledUrls`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.web_security_scanner.ListCrawledUrlsResponse:
                    Response for the ``ListCrawledUrls`` method.
            """

            http_options = _BaseWebSecurityScannerRestTransport._BaseListCrawledUrls._get_http_options()
            request, metadata = self._interceptor.pre_list_crawled_urls(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseWebSecurityScannerRestTransport._BaseListCrawledUrls,
                    "_BaseListCrawledUrls__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.websecurityscanner_v1alpha.WebSecurityScannerClient.ListCrawledUrls",
                    extra={
                        "serviceName": "google.cloud.websecurityscanner.v1alpha.WebSecurityScanner",
                        "rpcName": "ListCrawledUrls",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = WebSecurityScannerRestTransport._ListCrawledUrls._get_response(
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
            resp = web_security_scanner.ListCrawledUrlsResponse()
            pb_resp = web_security_scanner.ListCrawledUrlsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_crawled_urls(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_crawled_urls_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        web_security_scanner.ListCrawledUrlsResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.websecurityscanner_v1alpha.WebSecurityScannerClient.list_crawled_urls",
                    extra={
                        "serviceName": "google.cloud.websecurityscanner.v1alpha.WebSecurityScanner",
                        "rpcName": "ListCrawledUrls",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListFindings(
        _BaseWebSecurityScannerRestTransport._BaseListFindings,
        WebSecurityScannerRestStub,
    ):
        def __hash__(self):
            return hash("WebSecurityScannerRestTransport.ListFindings")

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
            request: web_security_scanner.ListFindingsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> web_security_scanner.ListFindingsResponse:
            r"""Call the list findings method over HTTP.

            Args:
                request (~.web_security_scanner.ListFindingsRequest):
                    The request object. Request for the ``ListFindings`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.web_security_scanner.ListFindingsResponse:
                    Response for the ``ListFindings`` method.
            """

            http_options = _BaseWebSecurityScannerRestTransport._BaseListFindings._get_http_options()
            request, metadata = self._interceptor.pre_list_findings(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseWebSecurityScannerRestTransport._BaseListFindings,
                    "_BaseListFindings__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.websecurityscanner_v1alpha.WebSecurityScannerClient.ListFindings",
                    extra={
                        "serviceName": "google.cloud.websecurityscanner.v1alpha.WebSecurityScanner",
                        "rpcName": "ListFindings",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = WebSecurityScannerRestTransport._ListFindings._get_response(
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
            resp = web_security_scanner.ListFindingsResponse()
            pb_resp = web_security_scanner.ListFindingsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_findings(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_findings_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        web_security_scanner.ListFindingsResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.websecurityscanner_v1alpha.WebSecurityScannerClient.list_findings",
                    extra={
                        "serviceName": "google.cloud.websecurityscanner.v1alpha.WebSecurityScanner",
                        "rpcName": "ListFindings",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListFindingTypeStats(
        _BaseWebSecurityScannerRestTransport._BaseListFindingTypeStats,
        WebSecurityScannerRestStub,
    ):
        def __hash__(self):
            return hash("WebSecurityScannerRestTransport.ListFindingTypeStats")

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
            request: web_security_scanner.ListFindingTypeStatsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> web_security_scanner.ListFindingTypeStatsResponse:
            r"""Call the list finding type stats method over HTTP.

            Args:
                request (~.web_security_scanner.ListFindingTypeStatsRequest):
                    The request object. Request for the ``ListFindingTypeStats`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.web_security_scanner.ListFindingTypeStatsResponse:
                    Response for the ``ListFindingTypeStats`` method.
            """

            http_options = _BaseWebSecurityScannerRestTransport._BaseListFindingTypeStats._get_http_options()
            request, metadata = self._interceptor.pre_list_finding_type_stats(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseWebSecurityScannerRestTransport._BaseListFindingTypeStats,
                    "_BaseListFindingTypeStats__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.websecurityscanner_v1alpha.WebSecurityScannerClient.ListFindingTypeStats",
                    extra={
                        "serviceName": "google.cloud.websecurityscanner.v1alpha.WebSecurityScanner",
                        "rpcName": "ListFindingTypeStats",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                WebSecurityScannerRestTransport._ListFindingTypeStats._get_response(
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
            resp = web_security_scanner.ListFindingTypeStatsResponse()
            pb_resp = web_security_scanner.ListFindingTypeStatsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_finding_type_stats(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_finding_type_stats_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        web_security_scanner.ListFindingTypeStatsResponse.to_json(
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
                    "Received response for google.cloud.websecurityscanner_v1alpha.WebSecurityScannerClient.list_finding_type_stats",
                    extra={
                        "serviceName": "google.cloud.websecurityscanner.v1alpha.WebSecurityScanner",
                        "rpcName": "ListFindingTypeStats",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListScanConfigs(
        _BaseWebSecurityScannerRestTransport._BaseListScanConfigs,
        WebSecurityScannerRestStub,
    ):
        def __hash__(self):
            return hash("WebSecurityScannerRestTransport.ListScanConfigs")

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
            request: web_security_scanner.ListScanConfigsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> web_security_scanner.ListScanConfigsResponse:
            r"""Call the list scan configs method over HTTP.

            Args:
                request (~.web_security_scanner.ListScanConfigsRequest):
                    The request object. Request for the ``ListScanConfigs`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.web_security_scanner.ListScanConfigsResponse:
                    Response for the ``ListScanConfigs`` method.
            """

            http_options = _BaseWebSecurityScannerRestTransport._BaseListScanConfigs._get_http_options()
            request, metadata = self._interceptor.pre_list_scan_configs(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseWebSecurityScannerRestTransport._BaseListScanConfigs,
                    "_BaseListScanConfigs__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.websecurityscanner_v1alpha.WebSecurityScannerClient.ListScanConfigs",
                    extra={
                        "serviceName": "google.cloud.websecurityscanner.v1alpha.WebSecurityScanner",
                        "rpcName": "ListScanConfigs",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = WebSecurityScannerRestTransport._ListScanConfigs._get_response(
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
            resp = web_security_scanner.ListScanConfigsResponse()
            pb_resp = web_security_scanner.ListScanConfigsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_scan_configs(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_scan_configs_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        web_security_scanner.ListScanConfigsResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.websecurityscanner_v1alpha.WebSecurityScannerClient.list_scan_configs",
                    extra={
                        "serviceName": "google.cloud.websecurityscanner.v1alpha.WebSecurityScanner",
                        "rpcName": "ListScanConfigs",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListScanRuns(
        _BaseWebSecurityScannerRestTransport._BaseListScanRuns,
        WebSecurityScannerRestStub,
    ):
        def __hash__(self):
            return hash("WebSecurityScannerRestTransport.ListScanRuns")

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
            request: web_security_scanner.ListScanRunsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> web_security_scanner.ListScanRunsResponse:
            r"""Call the list scan runs method over HTTP.

            Args:
                request (~.web_security_scanner.ListScanRunsRequest):
                    The request object. Request for the ``ListScanRuns`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.web_security_scanner.ListScanRunsResponse:
                    Response for the ``ListScanRuns`` method.
            """

            http_options = _BaseWebSecurityScannerRestTransport._BaseListScanRuns._get_http_options()
            request, metadata = self._interceptor.pre_list_scan_runs(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseWebSecurityScannerRestTransport._BaseListScanRuns,
                    "_BaseListScanRuns__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.websecurityscanner_v1alpha.WebSecurityScannerClient.ListScanRuns",
                    extra={
                        "serviceName": "google.cloud.websecurityscanner.v1alpha.WebSecurityScanner",
                        "rpcName": "ListScanRuns",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = WebSecurityScannerRestTransport._ListScanRuns._get_response(
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
            resp = web_security_scanner.ListScanRunsResponse()
            pb_resp = web_security_scanner.ListScanRunsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_scan_runs(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_scan_runs_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        web_security_scanner.ListScanRunsResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.websecurityscanner_v1alpha.WebSecurityScannerClient.list_scan_runs",
                    extra={
                        "serviceName": "google.cloud.websecurityscanner.v1alpha.WebSecurityScanner",
                        "rpcName": "ListScanRuns",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _StartScanRun(
        _BaseWebSecurityScannerRestTransport._BaseStartScanRun,
        WebSecurityScannerRestStub,
    ):
        def __hash__(self):
            return hash("WebSecurityScannerRestTransport.StartScanRun")

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
            request: web_security_scanner.StartScanRunRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> scan_run.ScanRun:
            r"""Call the start scan run method over HTTP.

            Args:
                request (~.web_security_scanner.StartScanRunRequest):
                    The request object. Request for the ``StartScanRun`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.scan_run.ScanRun:
                    A ScanRun is a output-only resource
                representing an actual run of the scan.

            """

            http_options = _BaseWebSecurityScannerRestTransport._BaseStartScanRun._get_http_options()
            request, metadata = self._interceptor.pre_start_scan_run(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseWebSecurityScannerRestTransport._BaseStartScanRun,
                    "_BaseStartScanRun__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.websecurityscanner_v1alpha.WebSecurityScannerClient.StartScanRun",
                    extra={
                        "serviceName": "google.cloud.websecurityscanner.v1alpha.WebSecurityScanner",
                        "rpcName": "StartScanRun",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = WebSecurityScannerRestTransport._StartScanRun._get_response(
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
            resp = scan_run.ScanRun()
            pb_resp = scan_run.ScanRun.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_start_scan_run(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_start_scan_run_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = scan_run.ScanRun.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.websecurityscanner_v1alpha.WebSecurityScannerClient.start_scan_run",
                    extra={
                        "serviceName": "google.cloud.websecurityscanner.v1alpha.WebSecurityScanner",
                        "rpcName": "StartScanRun",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _StopScanRun(
        _BaseWebSecurityScannerRestTransport._BaseStopScanRun,
        WebSecurityScannerRestStub,
    ):
        def __hash__(self):
            return hash("WebSecurityScannerRestTransport.StopScanRun")

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
            request: web_security_scanner.StopScanRunRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> scan_run.ScanRun:
            r"""Call the stop scan run method over HTTP.

            Args:
                request (~.web_security_scanner.StopScanRunRequest):
                    The request object. Request for the ``StopScanRun`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.scan_run.ScanRun:
                    A ScanRun is a output-only resource
                representing an actual run of the scan.

            """

            http_options = _BaseWebSecurityScannerRestTransport._BaseStopScanRun._get_http_options()
            request, metadata = self._interceptor.pre_stop_scan_run(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseWebSecurityScannerRestTransport._BaseStopScanRun,
                    "_BaseStopScanRun__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.websecurityscanner_v1alpha.WebSecurityScannerClient.StopScanRun",
                    extra={
                        "serviceName": "google.cloud.websecurityscanner.v1alpha.WebSecurityScanner",
                        "rpcName": "StopScanRun",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = WebSecurityScannerRestTransport._StopScanRun._get_response(
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
            resp = scan_run.ScanRun()
            pb_resp = scan_run.ScanRun.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_stop_scan_run(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_stop_scan_run_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = scan_run.ScanRun.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.websecurityscanner_v1alpha.WebSecurityScannerClient.stop_scan_run",
                    extra={
                        "serviceName": "google.cloud.websecurityscanner.v1alpha.WebSecurityScanner",
                        "rpcName": "StopScanRun",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateScanConfig(
        _BaseWebSecurityScannerRestTransport._BaseUpdateScanConfig,
        WebSecurityScannerRestStub,
    ):
        def __hash__(self):
            return hash("WebSecurityScannerRestTransport.UpdateScanConfig")

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
            request: web_security_scanner.UpdateScanConfigRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gcw_scan_config.ScanConfig:
            r"""Call the update scan config method over HTTP.

            Args:
                request (~.web_security_scanner.UpdateScanConfigRequest):
                    The request object. Request for the ``UpdateScanConfigRequest`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.gcw_scan_config.ScanConfig:
                    A ScanConfig resource contains the
                configurations to launch a scan. next
                id: 12

            """

            http_options = _BaseWebSecurityScannerRestTransport._BaseUpdateScanConfig._get_http_options()
            request, metadata = self._interceptor.pre_update_scan_config(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseWebSecurityScannerRestTransport._BaseUpdateScanConfig,
                    "_BaseUpdateScanConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.websecurityscanner_v1alpha.WebSecurityScannerClient.UpdateScanConfig",
                    extra={
                        "serviceName": "google.cloud.websecurityscanner.v1alpha.WebSecurityScanner",
                        "rpcName": "UpdateScanConfig",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = WebSecurityScannerRestTransport._UpdateScanConfig._get_response(
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
            resp = gcw_scan_config.ScanConfig()
            pb_resp = gcw_scan_config.ScanConfig.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_scan_config(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_scan_config_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = gcw_scan_config.ScanConfig.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.websecurityscanner_v1alpha.WebSecurityScannerClient.update_scan_config",
                    extra={
                        "serviceName": "google.cloud.websecurityscanner.v1alpha.WebSecurityScanner",
                        "rpcName": "UpdateScanConfig",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def create_scan_config(
        self,
    ) -> Callable[
        [web_security_scanner.CreateScanConfigRequest], gcw_scan_config.ScanConfig
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateScanConfig(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_scan_config(
        self,
    ) -> Callable[[web_security_scanner.DeleteScanConfigRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteScanConfig(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_finding(
        self,
    ) -> Callable[[web_security_scanner.GetFindingRequest], finding.Finding]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetFinding(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_scan_config(
        self,
    ) -> Callable[[web_security_scanner.GetScanConfigRequest], scan_config.ScanConfig]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetScanConfig(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_scan_run(
        self,
    ) -> Callable[[web_security_scanner.GetScanRunRequest], scan_run.ScanRun]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetScanRun(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_crawled_urls(
        self,
    ) -> Callable[
        [web_security_scanner.ListCrawledUrlsRequest],
        web_security_scanner.ListCrawledUrlsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListCrawledUrls(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_findings(
        self,
    ) -> Callable[
        [web_security_scanner.ListFindingsRequest],
        web_security_scanner.ListFindingsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListFindings(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_finding_type_stats(
        self,
    ) -> Callable[
        [web_security_scanner.ListFindingTypeStatsRequest],
        web_security_scanner.ListFindingTypeStatsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListFindingTypeStats(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_scan_configs(
        self,
    ) -> Callable[
        [web_security_scanner.ListScanConfigsRequest],
        web_security_scanner.ListScanConfigsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListScanConfigs(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_scan_runs(
        self,
    ) -> Callable[
        [web_security_scanner.ListScanRunsRequest],
        web_security_scanner.ListScanRunsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListScanRuns(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def start_scan_run(
        self,
    ) -> Callable[[web_security_scanner.StartScanRunRequest], scan_run.ScanRun]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._StartScanRun(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def stop_scan_run(
        self,
    ) -> Callable[[web_security_scanner.StopScanRunRequest], scan_run.ScanRun]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._StopScanRun(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_scan_config(
        self,
    ) -> Callable[
        [web_security_scanner.UpdateScanConfigRequest], gcw_scan_config.ScanConfig
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateScanConfig(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def kind(self) -> str:
        return "rest"

    def close(self):
        self._session.close()


__all__ = ("WebSecurityScannerRestTransport",)
