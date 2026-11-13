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
from google.cloud.location import locations_pb2  # type: ignore
from google.iam.v1 import (
    iam_policy_pb2,  # type: ignore
    policy_pb2,  # type: ignore
)
from google.longrunning import operations_pb2  # type: ignore
from google.protobuf import json_format
from requests import __version__ as requests_version

from google.cloud.visionai_v1._compat import transcode_request
from google.cloud.visionai_v1.types import lva_resources, lva_service

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseLiveVideoAnalyticsRestTransport

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


class LiveVideoAnalyticsRestInterceptor:
    """Interceptor for LiveVideoAnalytics.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the LiveVideoAnalyticsRestTransport.

    .. code-block:: python
        class MyCustomLiveVideoAnalyticsInterceptor(LiveVideoAnalyticsRestInterceptor):
            def pre_batch_run_process(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_run_process(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_analysis(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_analysis(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_operator(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_operator(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_process(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_process(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_analysis(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_analysis(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_operator(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_operator(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_process(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_process(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_analysis(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_analysis(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_operator(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_operator(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_process(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_process(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_analyses(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_analyses(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_operators(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_operators(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_processes(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_processes(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_public_operators(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_public_operators(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_resolve_operator_info(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_resolve_operator_info(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_analysis(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_analysis(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_operator(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_operator(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_process(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_process(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = LiveVideoAnalyticsRestTransport(interceptor=MyCustomLiveVideoAnalyticsInterceptor())
        client = LiveVideoAnalyticsClient(transport=transport)


    """

    def pre_batch_run_process(
        self,
        request: lva_service.BatchRunProcessRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        lva_service.BatchRunProcessRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for batch_run_process

        Override in a subclass to manipulate the request or metadata
        before they are sent to the LiveVideoAnalytics server.
        """
        return request, metadata

    def post_batch_run_process(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for batch_run_process

        DEPRECATED. Please use the `post_batch_run_process_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the LiveVideoAnalytics server but before
        it is returned to user code. This `post_batch_run_process` interceptor runs
        before the `post_batch_run_process_with_metadata` interceptor.
        """
        return response

    def post_batch_run_process_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for batch_run_process

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the LiveVideoAnalytics server but before it is returned to user code.

        We recommend only using this `post_batch_run_process_with_metadata`
        interceptor in new development instead of the `post_batch_run_process` interceptor.
        When both interceptors are used, this `post_batch_run_process_with_metadata` interceptor runs after the
        `post_batch_run_process` interceptor. The (possibly modified) response returned by
        `post_batch_run_process` will be passed to
        `post_batch_run_process_with_metadata`.
        """
        return response, metadata

    def pre_create_analysis(
        self,
        request: lva_service.CreateAnalysisRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        lva_service.CreateAnalysisRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_analysis

        Override in a subclass to manipulate the request or metadata
        before they are sent to the LiveVideoAnalytics server.
        """
        return request, metadata

    def post_create_analysis(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_analysis

        DEPRECATED. Please use the `post_create_analysis_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the LiveVideoAnalytics server but before
        it is returned to user code. This `post_create_analysis` interceptor runs
        before the `post_create_analysis_with_metadata` interceptor.
        """
        return response

    def post_create_analysis_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_analysis

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the LiveVideoAnalytics server but before it is returned to user code.

        We recommend only using this `post_create_analysis_with_metadata`
        interceptor in new development instead of the `post_create_analysis` interceptor.
        When both interceptors are used, this `post_create_analysis_with_metadata` interceptor runs after the
        `post_create_analysis` interceptor. The (possibly modified) response returned by
        `post_create_analysis` will be passed to
        `post_create_analysis_with_metadata`.
        """
        return response, metadata

    def pre_create_operator(
        self,
        request: lva_service.CreateOperatorRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        lva_service.CreateOperatorRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_operator

        Override in a subclass to manipulate the request or metadata
        before they are sent to the LiveVideoAnalytics server.
        """
        return request, metadata

    def post_create_operator(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_operator

        DEPRECATED. Please use the `post_create_operator_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the LiveVideoAnalytics server but before
        it is returned to user code. This `post_create_operator` interceptor runs
        before the `post_create_operator_with_metadata` interceptor.
        """
        return response

    def post_create_operator_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_operator

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the LiveVideoAnalytics server but before it is returned to user code.

        We recommend only using this `post_create_operator_with_metadata`
        interceptor in new development instead of the `post_create_operator` interceptor.
        When both interceptors are used, this `post_create_operator_with_metadata` interceptor runs after the
        `post_create_operator` interceptor. The (possibly modified) response returned by
        `post_create_operator` will be passed to
        `post_create_operator_with_metadata`.
        """
        return response, metadata

    def pre_create_process(
        self,
        request: lva_service.CreateProcessRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        lva_service.CreateProcessRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_process

        Override in a subclass to manipulate the request or metadata
        before they are sent to the LiveVideoAnalytics server.
        """
        return request, metadata

    def post_create_process(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_process

        DEPRECATED. Please use the `post_create_process_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the LiveVideoAnalytics server but before
        it is returned to user code. This `post_create_process` interceptor runs
        before the `post_create_process_with_metadata` interceptor.
        """
        return response

    def post_create_process_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_process

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the LiveVideoAnalytics server but before it is returned to user code.

        We recommend only using this `post_create_process_with_metadata`
        interceptor in new development instead of the `post_create_process` interceptor.
        When both interceptors are used, this `post_create_process_with_metadata` interceptor runs after the
        `post_create_process` interceptor. The (possibly modified) response returned by
        `post_create_process` will be passed to
        `post_create_process_with_metadata`.
        """
        return response, metadata

    def pre_delete_analysis(
        self,
        request: lva_service.DeleteAnalysisRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        lva_service.DeleteAnalysisRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_analysis

        Override in a subclass to manipulate the request or metadata
        before they are sent to the LiveVideoAnalytics server.
        """
        return request, metadata

    def post_delete_analysis(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_analysis

        DEPRECATED. Please use the `post_delete_analysis_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the LiveVideoAnalytics server but before
        it is returned to user code. This `post_delete_analysis` interceptor runs
        before the `post_delete_analysis_with_metadata` interceptor.
        """
        return response

    def post_delete_analysis_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_analysis

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the LiveVideoAnalytics server but before it is returned to user code.

        We recommend only using this `post_delete_analysis_with_metadata`
        interceptor in new development instead of the `post_delete_analysis` interceptor.
        When both interceptors are used, this `post_delete_analysis_with_metadata` interceptor runs after the
        `post_delete_analysis` interceptor. The (possibly modified) response returned by
        `post_delete_analysis` will be passed to
        `post_delete_analysis_with_metadata`.
        """
        return response, metadata

    def pre_delete_operator(
        self,
        request: lva_service.DeleteOperatorRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        lva_service.DeleteOperatorRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_operator

        Override in a subclass to manipulate the request or metadata
        before they are sent to the LiveVideoAnalytics server.
        """
        return request, metadata

    def post_delete_operator(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_operator

        DEPRECATED. Please use the `post_delete_operator_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the LiveVideoAnalytics server but before
        it is returned to user code. This `post_delete_operator` interceptor runs
        before the `post_delete_operator_with_metadata` interceptor.
        """
        return response

    def post_delete_operator_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_operator

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the LiveVideoAnalytics server but before it is returned to user code.

        We recommend only using this `post_delete_operator_with_metadata`
        interceptor in new development instead of the `post_delete_operator` interceptor.
        When both interceptors are used, this `post_delete_operator_with_metadata` interceptor runs after the
        `post_delete_operator` interceptor. The (possibly modified) response returned by
        `post_delete_operator` will be passed to
        `post_delete_operator_with_metadata`.
        """
        return response, metadata

    def pre_delete_process(
        self,
        request: lva_service.DeleteProcessRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        lva_service.DeleteProcessRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_process

        Override in a subclass to manipulate the request or metadata
        before they are sent to the LiveVideoAnalytics server.
        """
        return request, metadata

    def post_delete_process(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_process

        DEPRECATED. Please use the `post_delete_process_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the LiveVideoAnalytics server but before
        it is returned to user code. This `post_delete_process` interceptor runs
        before the `post_delete_process_with_metadata` interceptor.
        """
        return response

    def post_delete_process_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_process

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the LiveVideoAnalytics server but before it is returned to user code.

        We recommend only using this `post_delete_process_with_metadata`
        interceptor in new development instead of the `post_delete_process` interceptor.
        When both interceptors are used, this `post_delete_process_with_metadata` interceptor runs after the
        `post_delete_process` interceptor. The (possibly modified) response returned by
        `post_delete_process` will be passed to
        `post_delete_process_with_metadata`.
        """
        return response, metadata

    def pre_get_analysis(
        self,
        request: lva_service.GetAnalysisRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[lva_service.GetAnalysisRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_analysis

        Override in a subclass to manipulate the request or metadata
        before they are sent to the LiveVideoAnalytics server.
        """
        return request, metadata

    def post_get_analysis(
        self, response: lva_resources.Analysis
    ) -> lva_resources.Analysis:
        """Post-rpc interceptor for get_analysis

        DEPRECATED. Please use the `post_get_analysis_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the LiveVideoAnalytics server but before
        it is returned to user code. This `post_get_analysis` interceptor runs
        before the `post_get_analysis_with_metadata` interceptor.
        """
        return response

    def post_get_analysis_with_metadata(
        self,
        response: lva_resources.Analysis,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[lva_resources.Analysis, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_analysis

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the LiveVideoAnalytics server but before it is returned to user code.

        We recommend only using this `post_get_analysis_with_metadata`
        interceptor in new development instead of the `post_get_analysis` interceptor.
        When both interceptors are used, this `post_get_analysis_with_metadata` interceptor runs after the
        `post_get_analysis` interceptor. The (possibly modified) response returned by
        `post_get_analysis` will be passed to
        `post_get_analysis_with_metadata`.
        """
        return response, metadata

    def pre_get_operator(
        self,
        request: lva_service.GetOperatorRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[lva_service.GetOperatorRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_operator

        Override in a subclass to manipulate the request or metadata
        before they are sent to the LiveVideoAnalytics server.
        """
        return request, metadata

    def post_get_operator(
        self, response: lva_resources.Operator
    ) -> lva_resources.Operator:
        """Post-rpc interceptor for get_operator

        DEPRECATED. Please use the `post_get_operator_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the LiveVideoAnalytics server but before
        it is returned to user code. This `post_get_operator` interceptor runs
        before the `post_get_operator_with_metadata` interceptor.
        """
        return response

    def post_get_operator_with_metadata(
        self,
        response: lva_resources.Operator,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[lva_resources.Operator, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_operator

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the LiveVideoAnalytics server but before it is returned to user code.

        We recommend only using this `post_get_operator_with_metadata`
        interceptor in new development instead of the `post_get_operator` interceptor.
        When both interceptors are used, this `post_get_operator_with_metadata` interceptor runs after the
        `post_get_operator` interceptor. The (possibly modified) response returned by
        `post_get_operator` will be passed to
        `post_get_operator_with_metadata`.
        """
        return response, metadata

    def pre_get_process(
        self,
        request: lva_service.GetProcessRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[lva_service.GetProcessRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_process

        Override in a subclass to manipulate the request or metadata
        before they are sent to the LiveVideoAnalytics server.
        """
        return request, metadata

    def post_get_process(
        self, response: lva_resources.Process
    ) -> lva_resources.Process:
        """Post-rpc interceptor for get_process

        DEPRECATED. Please use the `post_get_process_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the LiveVideoAnalytics server but before
        it is returned to user code. This `post_get_process` interceptor runs
        before the `post_get_process_with_metadata` interceptor.
        """
        return response

    def post_get_process_with_metadata(
        self,
        response: lva_resources.Process,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[lva_resources.Process, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_process

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the LiveVideoAnalytics server but before it is returned to user code.

        We recommend only using this `post_get_process_with_metadata`
        interceptor in new development instead of the `post_get_process` interceptor.
        When both interceptors are used, this `post_get_process_with_metadata` interceptor runs after the
        `post_get_process` interceptor. The (possibly modified) response returned by
        `post_get_process` will be passed to
        `post_get_process_with_metadata`.
        """
        return response, metadata

    def pre_list_analyses(
        self,
        request: lva_service.ListAnalysesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        lva_service.ListAnalysesRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_analyses

        Override in a subclass to manipulate the request or metadata
        before they are sent to the LiveVideoAnalytics server.
        """
        return request, metadata

    def post_list_analyses(
        self, response: lva_service.ListAnalysesResponse
    ) -> lva_service.ListAnalysesResponse:
        """Post-rpc interceptor for list_analyses

        DEPRECATED. Please use the `post_list_analyses_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the LiveVideoAnalytics server but before
        it is returned to user code. This `post_list_analyses` interceptor runs
        before the `post_list_analyses_with_metadata` interceptor.
        """
        return response

    def post_list_analyses_with_metadata(
        self,
        response: lva_service.ListAnalysesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        lva_service.ListAnalysesResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_analyses

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the LiveVideoAnalytics server but before it is returned to user code.

        We recommend only using this `post_list_analyses_with_metadata`
        interceptor in new development instead of the `post_list_analyses` interceptor.
        When both interceptors are used, this `post_list_analyses_with_metadata` interceptor runs after the
        `post_list_analyses` interceptor. The (possibly modified) response returned by
        `post_list_analyses` will be passed to
        `post_list_analyses_with_metadata`.
        """
        return response, metadata

    def pre_list_operators(
        self,
        request: lva_service.ListOperatorsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        lva_service.ListOperatorsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_operators

        Override in a subclass to manipulate the request or metadata
        before they are sent to the LiveVideoAnalytics server.
        """
        return request, metadata

    def post_list_operators(
        self, response: lva_service.ListOperatorsResponse
    ) -> lva_service.ListOperatorsResponse:
        """Post-rpc interceptor for list_operators

        DEPRECATED. Please use the `post_list_operators_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the LiveVideoAnalytics server but before
        it is returned to user code. This `post_list_operators` interceptor runs
        before the `post_list_operators_with_metadata` interceptor.
        """
        return response

    def post_list_operators_with_metadata(
        self,
        response: lva_service.ListOperatorsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        lva_service.ListOperatorsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_operators

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the LiveVideoAnalytics server but before it is returned to user code.

        We recommend only using this `post_list_operators_with_metadata`
        interceptor in new development instead of the `post_list_operators` interceptor.
        When both interceptors are used, this `post_list_operators_with_metadata` interceptor runs after the
        `post_list_operators` interceptor. The (possibly modified) response returned by
        `post_list_operators` will be passed to
        `post_list_operators_with_metadata`.
        """
        return response, metadata

    def pre_list_processes(
        self,
        request: lva_service.ListProcessesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        lva_service.ListProcessesRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_processes

        Override in a subclass to manipulate the request or metadata
        before they are sent to the LiveVideoAnalytics server.
        """
        return request, metadata

    def post_list_processes(
        self, response: lva_service.ListProcessesResponse
    ) -> lva_service.ListProcessesResponse:
        """Post-rpc interceptor for list_processes

        DEPRECATED. Please use the `post_list_processes_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the LiveVideoAnalytics server but before
        it is returned to user code. This `post_list_processes` interceptor runs
        before the `post_list_processes_with_metadata` interceptor.
        """
        return response

    def post_list_processes_with_metadata(
        self,
        response: lva_service.ListProcessesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        lva_service.ListProcessesResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_processes

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the LiveVideoAnalytics server but before it is returned to user code.

        We recommend only using this `post_list_processes_with_metadata`
        interceptor in new development instead of the `post_list_processes` interceptor.
        When both interceptors are used, this `post_list_processes_with_metadata` interceptor runs after the
        `post_list_processes` interceptor. The (possibly modified) response returned by
        `post_list_processes` will be passed to
        `post_list_processes_with_metadata`.
        """
        return response, metadata

    def pre_list_public_operators(
        self,
        request: lva_service.ListPublicOperatorsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        lva_service.ListPublicOperatorsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_public_operators

        Override in a subclass to manipulate the request or metadata
        before they are sent to the LiveVideoAnalytics server.
        """
        return request, metadata

    def post_list_public_operators(
        self, response: lva_service.ListPublicOperatorsResponse
    ) -> lva_service.ListPublicOperatorsResponse:
        """Post-rpc interceptor for list_public_operators

        DEPRECATED. Please use the `post_list_public_operators_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the LiveVideoAnalytics server but before
        it is returned to user code. This `post_list_public_operators` interceptor runs
        before the `post_list_public_operators_with_metadata` interceptor.
        """
        return response

    def post_list_public_operators_with_metadata(
        self,
        response: lva_service.ListPublicOperatorsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        lva_service.ListPublicOperatorsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_public_operators

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the LiveVideoAnalytics server but before it is returned to user code.

        We recommend only using this `post_list_public_operators_with_metadata`
        interceptor in new development instead of the `post_list_public_operators` interceptor.
        When both interceptors are used, this `post_list_public_operators_with_metadata` interceptor runs after the
        `post_list_public_operators` interceptor. The (possibly modified) response returned by
        `post_list_public_operators` will be passed to
        `post_list_public_operators_with_metadata`.
        """
        return response, metadata

    def pre_resolve_operator_info(
        self,
        request: lva_service.ResolveOperatorInfoRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        lva_service.ResolveOperatorInfoRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for resolve_operator_info

        Override in a subclass to manipulate the request or metadata
        before they are sent to the LiveVideoAnalytics server.
        """
        return request, metadata

    def post_resolve_operator_info(
        self, response: lva_service.ResolveOperatorInfoResponse
    ) -> lva_service.ResolveOperatorInfoResponse:
        """Post-rpc interceptor for resolve_operator_info

        DEPRECATED. Please use the `post_resolve_operator_info_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the LiveVideoAnalytics server but before
        it is returned to user code. This `post_resolve_operator_info` interceptor runs
        before the `post_resolve_operator_info_with_metadata` interceptor.
        """
        return response

    def post_resolve_operator_info_with_metadata(
        self,
        response: lva_service.ResolveOperatorInfoResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        lva_service.ResolveOperatorInfoResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for resolve_operator_info

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the LiveVideoAnalytics server but before it is returned to user code.

        We recommend only using this `post_resolve_operator_info_with_metadata`
        interceptor in new development instead of the `post_resolve_operator_info` interceptor.
        When both interceptors are used, this `post_resolve_operator_info_with_metadata` interceptor runs after the
        `post_resolve_operator_info` interceptor. The (possibly modified) response returned by
        `post_resolve_operator_info` will be passed to
        `post_resolve_operator_info_with_metadata`.
        """
        return response, metadata

    def pre_update_analysis(
        self,
        request: lva_service.UpdateAnalysisRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        lva_service.UpdateAnalysisRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_analysis

        Override in a subclass to manipulate the request or metadata
        before they are sent to the LiveVideoAnalytics server.
        """
        return request, metadata

    def post_update_analysis(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_analysis

        DEPRECATED. Please use the `post_update_analysis_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the LiveVideoAnalytics server but before
        it is returned to user code. This `post_update_analysis` interceptor runs
        before the `post_update_analysis_with_metadata` interceptor.
        """
        return response

    def post_update_analysis_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_analysis

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the LiveVideoAnalytics server but before it is returned to user code.

        We recommend only using this `post_update_analysis_with_metadata`
        interceptor in new development instead of the `post_update_analysis` interceptor.
        When both interceptors are used, this `post_update_analysis_with_metadata` interceptor runs after the
        `post_update_analysis` interceptor. The (possibly modified) response returned by
        `post_update_analysis` will be passed to
        `post_update_analysis_with_metadata`.
        """
        return response, metadata

    def pre_update_operator(
        self,
        request: lva_service.UpdateOperatorRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        lva_service.UpdateOperatorRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_operator

        Override in a subclass to manipulate the request or metadata
        before they are sent to the LiveVideoAnalytics server.
        """
        return request, metadata

    def post_update_operator(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_operator

        DEPRECATED. Please use the `post_update_operator_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the LiveVideoAnalytics server but before
        it is returned to user code. This `post_update_operator` interceptor runs
        before the `post_update_operator_with_metadata` interceptor.
        """
        return response

    def post_update_operator_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_operator

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the LiveVideoAnalytics server but before it is returned to user code.

        We recommend only using this `post_update_operator_with_metadata`
        interceptor in new development instead of the `post_update_operator` interceptor.
        When both interceptors are used, this `post_update_operator_with_metadata` interceptor runs after the
        `post_update_operator` interceptor. The (possibly modified) response returned by
        `post_update_operator` will be passed to
        `post_update_operator_with_metadata`.
        """
        return response, metadata

    def pre_update_process(
        self,
        request: lva_service.UpdateProcessRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        lva_service.UpdateProcessRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_process

        Override in a subclass to manipulate the request or metadata
        before they are sent to the LiveVideoAnalytics server.
        """
        return request, metadata

    def post_update_process(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_process

        DEPRECATED. Please use the `post_update_process_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the LiveVideoAnalytics server but before
        it is returned to user code. This `post_update_process` interceptor runs
        before the `post_update_process_with_metadata` interceptor.
        """
        return response

    def post_update_process_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_process

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the LiveVideoAnalytics server but before it is returned to user code.

        We recommend only using this `post_update_process_with_metadata`
        interceptor in new development instead of the `post_update_process` interceptor.
        When both interceptors are used, this `post_update_process_with_metadata` interceptor runs after the
        `post_update_process` interceptor. The (possibly modified) response returned by
        `post_update_process` will be passed to
        `post_update_process_with_metadata`.
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
        before they are sent to the LiveVideoAnalytics server.
        """
        return request, metadata

    def post_get_location(
        self, response: locations_pb2.Location
    ) -> locations_pb2.Location:
        """Post-rpc interceptor for get_location

        Override in a subclass to manipulate the response
        after it is returned by the LiveVideoAnalytics server but before
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
        before they are sent to the LiveVideoAnalytics server.
        """
        return request, metadata

    def post_list_locations(
        self, response: locations_pb2.ListLocationsResponse
    ) -> locations_pb2.ListLocationsResponse:
        """Post-rpc interceptor for list_locations

        Override in a subclass to manipulate the response
        after it is returned by the LiveVideoAnalytics server but before
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
        before they are sent to the LiveVideoAnalytics server.
        """
        return request, metadata

    def post_cancel_operation(self, response: None) -> None:
        """Post-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the response
        after it is returned by the LiveVideoAnalytics server but before
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
        before they are sent to the LiveVideoAnalytics server.
        """
        return request, metadata

    def post_delete_operation(self, response: None) -> None:
        """Post-rpc interceptor for delete_operation

        Override in a subclass to manipulate the response
        after it is returned by the LiveVideoAnalytics server but before
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
        before they are sent to the LiveVideoAnalytics server.
        """
        return request, metadata

    def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the LiveVideoAnalytics server but before
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
        before they are sent to the LiveVideoAnalytics server.
        """
        return request, metadata

    def post_list_operations(
        self, response: operations_pb2.ListOperationsResponse
    ) -> operations_pb2.ListOperationsResponse:
        """Post-rpc interceptor for list_operations

        Override in a subclass to manipulate the response
        after it is returned by the LiveVideoAnalytics server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class LiveVideoAnalyticsRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: LiveVideoAnalyticsRestInterceptor


class LiveVideoAnalyticsRestTransport(_BaseLiveVideoAnalyticsRestTransport):
    """REST backend synchronous transport for LiveVideoAnalytics.

    Service describing handlers for resources. The service
    enables clients to run Live Video Analytics (LVA) on the
    streaming inputs.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "visionai.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[LiveVideoAnalyticsRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'visionai.googleapis.com').
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
            interceptor (Optional[LiveVideoAnalyticsRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or LiveVideoAnalyticsRestInterceptor()
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
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/warehouseOperations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/corpora/*/assets/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/corpora/*/collections/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/corpora/*/imageIndexes/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/corpora/*/indexes/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/corpora/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/indexEndpoints/*/operations/*}",
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

    class _BatchRunProcess(
        _BaseLiveVideoAnalyticsRestTransport._BaseBatchRunProcess,
        LiveVideoAnalyticsRestStub,
    ):
        def __hash__(self):
            return hash("LiveVideoAnalyticsRestTransport.BatchRunProcess")

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
            request: lva_service.BatchRunProcessRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the batch run process method over HTTP.

            Args:
                request (~.lva_service.BatchRunProcessRequest):
                    The request object. Request message for running the
                processes in a batch.
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

            http_options = _BaseLiveVideoAnalyticsRestTransport._BaseBatchRunProcess._get_http_options()
            request, metadata = self._interceptor.pre_batch_run_process(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLiveVideoAnalyticsRestTransport._BaseBatchRunProcess,
                    "_BaseBatchRunProcess__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.visionai_v1.LiveVideoAnalyticsClient.BatchRunProcess",
                    extra={
                        "serviceName": "google.cloud.visionai.v1.LiveVideoAnalytics",
                        "rpcName": "BatchRunProcess",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LiveVideoAnalyticsRestTransport._BatchRunProcess._get_response(
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

            resp = self._interceptor.post_batch_run_process(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_batch_run_process_with_metadata(
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
                    "Received response for google.cloud.visionai_v1.LiveVideoAnalyticsClient.batch_run_process",
                    extra={
                        "serviceName": "google.cloud.visionai.v1.LiveVideoAnalytics",
                        "rpcName": "BatchRunProcess",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateAnalysis(
        _BaseLiveVideoAnalyticsRestTransport._BaseCreateAnalysis,
        LiveVideoAnalyticsRestStub,
    ):
        def __hash__(self):
            return hash("LiveVideoAnalyticsRestTransport.CreateAnalysis")

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
            request: lva_service.CreateAnalysisRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create analysis method over HTTP.

            Args:
                request (~.lva_service.CreateAnalysisRequest):
                    The request object. Message for creating an Analysis.
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

            http_options = _BaseLiveVideoAnalyticsRestTransport._BaseCreateAnalysis._get_http_options()
            request, metadata = self._interceptor.pre_create_analysis(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLiveVideoAnalyticsRestTransport._BaseCreateAnalysis,
                    "_BaseCreateAnalysis__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.visionai_v1.LiveVideoAnalyticsClient.CreateAnalysis",
                    extra={
                        "serviceName": "google.cloud.visionai.v1.LiveVideoAnalytics",
                        "rpcName": "CreateAnalysis",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LiveVideoAnalyticsRestTransport._CreateAnalysis._get_response(
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

            resp = self._interceptor.post_create_analysis(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_analysis_with_metadata(
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
                    "Received response for google.cloud.visionai_v1.LiveVideoAnalyticsClient.create_analysis",
                    extra={
                        "serviceName": "google.cloud.visionai.v1.LiveVideoAnalytics",
                        "rpcName": "CreateAnalysis",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateOperator(
        _BaseLiveVideoAnalyticsRestTransport._BaseCreateOperator,
        LiveVideoAnalyticsRestStub,
    ):
        def __hash__(self):
            return hash("LiveVideoAnalyticsRestTransport.CreateOperator")

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
            request: lva_service.CreateOperatorRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create operator method over HTTP.

            Args:
                request (~.lva_service.CreateOperatorRequest):
                    The request object. Message for creating a Operator.
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

            http_options = _BaseLiveVideoAnalyticsRestTransport._BaseCreateOperator._get_http_options()
            request, metadata = self._interceptor.pre_create_operator(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLiveVideoAnalyticsRestTransport._BaseCreateOperator,
                    "_BaseCreateOperator__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.visionai_v1.LiveVideoAnalyticsClient.CreateOperator",
                    extra={
                        "serviceName": "google.cloud.visionai.v1.LiveVideoAnalytics",
                        "rpcName": "CreateOperator",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LiveVideoAnalyticsRestTransport._CreateOperator._get_response(
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

            resp = self._interceptor.post_create_operator(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_operator_with_metadata(
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
                    "Received response for google.cloud.visionai_v1.LiveVideoAnalyticsClient.create_operator",
                    extra={
                        "serviceName": "google.cloud.visionai.v1.LiveVideoAnalytics",
                        "rpcName": "CreateOperator",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateProcess(
        _BaseLiveVideoAnalyticsRestTransport._BaseCreateProcess,
        LiveVideoAnalyticsRestStub,
    ):
        def __hash__(self):
            return hash("LiveVideoAnalyticsRestTransport.CreateProcess")

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
            request: lva_service.CreateProcessRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create process method over HTTP.

            Args:
                request (~.lva_service.CreateProcessRequest):
                    The request object. Message for creating a Process.
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

            http_options = _BaseLiveVideoAnalyticsRestTransport._BaseCreateProcess._get_http_options()
            request, metadata = self._interceptor.pre_create_process(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLiveVideoAnalyticsRestTransport._BaseCreateProcess,
                    "_BaseCreateProcess__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.visionai_v1.LiveVideoAnalyticsClient.CreateProcess",
                    extra={
                        "serviceName": "google.cloud.visionai.v1.LiveVideoAnalytics",
                        "rpcName": "CreateProcess",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LiveVideoAnalyticsRestTransport._CreateProcess._get_response(
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

            resp = self._interceptor.post_create_process(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_process_with_metadata(
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
                    "Received response for google.cloud.visionai_v1.LiveVideoAnalyticsClient.create_process",
                    extra={
                        "serviceName": "google.cloud.visionai.v1.LiveVideoAnalytics",
                        "rpcName": "CreateProcess",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteAnalysis(
        _BaseLiveVideoAnalyticsRestTransport._BaseDeleteAnalysis,
        LiveVideoAnalyticsRestStub,
    ):
        def __hash__(self):
            return hash("LiveVideoAnalyticsRestTransport.DeleteAnalysis")

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
            request: lva_service.DeleteAnalysisRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete analysis method over HTTP.

            Args:
                request (~.lva_service.DeleteAnalysisRequest):
                    The request object. Message for deleting an Analysis.
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

            http_options = _BaseLiveVideoAnalyticsRestTransport._BaseDeleteAnalysis._get_http_options()
            request, metadata = self._interceptor.pre_delete_analysis(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLiveVideoAnalyticsRestTransport._BaseDeleteAnalysis,
                    "_BaseDeleteAnalysis__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.visionai_v1.LiveVideoAnalyticsClient.DeleteAnalysis",
                    extra={
                        "serviceName": "google.cloud.visionai.v1.LiveVideoAnalytics",
                        "rpcName": "DeleteAnalysis",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LiveVideoAnalyticsRestTransport._DeleteAnalysis._get_response(
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

            resp = self._interceptor.post_delete_analysis(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_analysis_with_metadata(
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
                    "Received response for google.cloud.visionai_v1.LiveVideoAnalyticsClient.delete_analysis",
                    extra={
                        "serviceName": "google.cloud.visionai.v1.LiveVideoAnalytics",
                        "rpcName": "DeleteAnalysis",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteOperator(
        _BaseLiveVideoAnalyticsRestTransport._BaseDeleteOperator,
        LiveVideoAnalyticsRestStub,
    ):
        def __hash__(self):
            return hash("LiveVideoAnalyticsRestTransport.DeleteOperator")

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
            request: lva_service.DeleteOperatorRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete operator method over HTTP.

            Args:
                request (~.lva_service.DeleteOperatorRequest):
                    The request object. Message for deleting a Operator
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

            http_options = _BaseLiveVideoAnalyticsRestTransport._BaseDeleteOperator._get_http_options()
            request, metadata = self._interceptor.pre_delete_operator(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLiveVideoAnalyticsRestTransport._BaseDeleteOperator,
                    "_BaseDeleteOperator__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.visionai_v1.LiveVideoAnalyticsClient.DeleteOperator",
                    extra={
                        "serviceName": "google.cloud.visionai.v1.LiveVideoAnalytics",
                        "rpcName": "DeleteOperator",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LiveVideoAnalyticsRestTransport._DeleteOperator._get_response(
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

            resp = self._interceptor.post_delete_operator(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_operator_with_metadata(
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
                    "Received response for google.cloud.visionai_v1.LiveVideoAnalyticsClient.delete_operator",
                    extra={
                        "serviceName": "google.cloud.visionai.v1.LiveVideoAnalytics",
                        "rpcName": "DeleteOperator",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteProcess(
        _BaseLiveVideoAnalyticsRestTransport._BaseDeleteProcess,
        LiveVideoAnalyticsRestStub,
    ):
        def __hash__(self):
            return hash("LiveVideoAnalyticsRestTransport.DeleteProcess")

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
            request: lva_service.DeleteProcessRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete process method over HTTP.

            Args:
                request (~.lva_service.DeleteProcessRequest):
                    The request object. Message for deleting a Process.
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

            http_options = _BaseLiveVideoAnalyticsRestTransport._BaseDeleteProcess._get_http_options()
            request, metadata = self._interceptor.pre_delete_process(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLiveVideoAnalyticsRestTransport._BaseDeleteProcess,
                    "_BaseDeleteProcess__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.visionai_v1.LiveVideoAnalyticsClient.DeleteProcess",
                    extra={
                        "serviceName": "google.cloud.visionai.v1.LiveVideoAnalytics",
                        "rpcName": "DeleteProcess",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LiveVideoAnalyticsRestTransport._DeleteProcess._get_response(
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

            resp = self._interceptor.post_delete_process(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_process_with_metadata(
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
                    "Received response for google.cloud.visionai_v1.LiveVideoAnalyticsClient.delete_process",
                    extra={
                        "serviceName": "google.cloud.visionai.v1.LiveVideoAnalytics",
                        "rpcName": "DeleteProcess",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetAnalysis(
        _BaseLiveVideoAnalyticsRestTransport._BaseGetAnalysis,
        LiveVideoAnalyticsRestStub,
    ):
        def __hash__(self):
            return hash("LiveVideoAnalyticsRestTransport.GetAnalysis")

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
            request: lva_service.GetAnalysisRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> lva_resources.Analysis:
            r"""Call the get analysis method over HTTP.

            Args:
                request (~.lva_service.GetAnalysisRequest):
                    The request object. Message for getting an Analysis.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.lva_resources.Analysis:
                    Message describing the Analysis
                object.

            """

            http_options = _BaseLiveVideoAnalyticsRestTransport._BaseGetAnalysis._get_http_options()
            request, metadata = self._interceptor.pre_get_analysis(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLiveVideoAnalyticsRestTransport._BaseGetAnalysis,
                    "_BaseGetAnalysis__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.visionai_v1.LiveVideoAnalyticsClient.GetAnalysis",
                    extra={
                        "serviceName": "google.cloud.visionai.v1.LiveVideoAnalytics",
                        "rpcName": "GetAnalysis",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LiveVideoAnalyticsRestTransport._GetAnalysis._get_response(
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
            resp = lva_resources.Analysis()
            pb_resp = lva_resources.Analysis.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_analysis(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_analysis_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = lva_resources.Analysis.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.visionai_v1.LiveVideoAnalyticsClient.get_analysis",
                    extra={
                        "serviceName": "google.cloud.visionai.v1.LiveVideoAnalytics",
                        "rpcName": "GetAnalysis",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetOperator(
        _BaseLiveVideoAnalyticsRestTransport._BaseGetOperator,
        LiveVideoAnalyticsRestStub,
    ):
        def __hash__(self):
            return hash("LiveVideoAnalyticsRestTransport.GetOperator")

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
            request: lva_service.GetOperatorRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> lva_resources.Operator:
            r"""Call the get operator method over HTTP.

            Args:
                request (~.lva_service.GetOperatorRequest):
                    The request object. Message for getting a Operator.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.lva_resources.Operator:
                    Message describing the Operator
                object.

            """

            http_options = _BaseLiveVideoAnalyticsRestTransport._BaseGetOperator._get_http_options()
            request, metadata = self._interceptor.pre_get_operator(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLiveVideoAnalyticsRestTransport._BaseGetOperator,
                    "_BaseGetOperator__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.visionai_v1.LiveVideoAnalyticsClient.GetOperator",
                    extra={
                        "serviceName": "google.cloud.visionai.v1.LiveVideoAnalytics",
                        "rpcName": "GetOperator",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LiveVideoAnalyticsRestTransport._GetOperator._get_response(
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
            resp = lva_resources.Operator()
            pb_resp = lva_resources.Operator.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_operator(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_operator_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = lva_resources.Operator.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.visionai_v1.LiveVideoAnalyticsClient.get_operator",
                    extra={
                        "serviceName": "google.cloud.visionai.v1.LiveVideoAnalytics",
                        "rpcName": "GetOperator",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetProcess(
        _BaseLiveVideoAnalyticsRestTransport._BaseGetProcess, LiveVideoAnalyticsRestStub
    ):
        def __hash__(self):
            return hash("LiveVideoAnalyticsRestTransport.GetProcess")

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
            request: lva_service.GetProcessRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> lva_resources.Process:
            r"""Call the get process method over HTTP.

            Args:
                request (~.lva_service.GetProcessRequest):
                    The request object. Message for getting a Process.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.lva_resources.Process:
                    Message describing the Process
                object.

            """

            http_options = (
                _BaseLiveVideoAnalyticsRestTransport._BaseGetProcess._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_process(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLiveVideoAnalyticsRestTransport._BaseGetProcess,
                    "_BaseGetProcess__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.visionai_v1.LiveVideoAnalyticsClient.GetProcess",
                    extra={
                        "serviceName": "google.cloud.visionai.v1.LiveVideoAnalytics",
                        "rpcName": "GetProcess",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LiveVideoAnalyticsRestTransport._GetProcess._get_response(
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
            resp = lva_resources.Process()
            pb_resp = lva_resources.Process.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_process(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_process_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = lva_resources.Process.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.visionai_v1.LiveVideoAnalyticsClient.get_process",
                    extra={
                        "serviceName": "google.cloud.visionai.v1.LiveVideoAnalytics",
                        "rpcName": "GetProcess",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListAnalyses(
        _BaseLiveVideoAnalyticsRestTransport._BaseListAnalyses,
        LiveVideoAnalyticsRestStub,
    ):
        def __hash__(self):
            return hash("LiveVideoAnalyticsRestTransport.ListAnalyses")

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
            request: lva_service.ListAnalysesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> lva_service.ListAnalysesResponse:
            r"""Call the list analyses method over HTTP.

            Args:
                request (~.lva_service.ListAnalysesRequest):
                    The request object. Message for requesting list of
                Analyses
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.lva_service.ListAnalysesResponse:
                    Message for response to listing
                Analyses

            """

            http_options = _BaseLiveVideoAnalyticsRestTransport._BaseListAnalyses._get_http_options()
            request, metadata = self._interceptor.pre_list_analyses(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLiveVideoAnalyticsRestTransport._BaseListAnalyses,
                    "_BaseListAnalyses__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.visionai_v1.LiveVideoAnalyticsClient.ListAnalyses",
                    extra={
                        "serviceName": "google.cloud.visionai.v1.LiveVideoAnalytics",
                        "rpcName": "ListAnalyses",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LiveVideoAnalyticsRestTransport._ListAnalyses._get_response(
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
            resp = lva_service.ListAnalysesResponse()
            pb_resp = lva_service.ListAnalysesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_analyses(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_analyses_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = lva_service.ListAnalysesResponse.to_json(
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
                    "Received response for google.cloud.visionai_v1.LiveVideoAnalyticsClient.list_analyses",
                    extra={
                        "serviceName": "google.cloud.visionai.v1.LiveVideoAnalytics",
                        "rpcName": "ListAnalyses",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListOperators(
        _BaseLiveVideoAnalyticsRestTransport._BaseListOperators,
        LiveVideoAnalyticsRestStub,
    ):
        def __hash__(self):
            return hash("LiveVideoAnalyticsRestTransport.ListOperators")

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
            request: lva_service.ListOperatorsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> lva_service.ListOperatorsResponse:
            r"""Call the list operators method over HTTP.

            Args:
                request (~.lva_service.ListOperatorsRequest):
                    The request object. Message for requesting list of
                Operators.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.lva_service.ListOperatorsResponse:
                    Message for response to listing
                Operators.

            """

            http_options = _BaseLiveVideoAnalyticsRestTransport._BaseListOperators._get_http_options()
            request, metadata = self._interceptor.pre_list_operators(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLiveVideoAnalyticsRestTransport._BaseListOperators,
                    "_BaseListOperators__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.visionai_v1.LiveVideoAnalyticsClient.ListOperators",
                    extra={
                        "serviceName": "google.cloud.visionai.v1.LiveVideoAnalytics",
                        "rpcName": "ListOperators",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LiveVideoAnalyticsRestTransport._ListOperators._get_response(
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
            resp = lva_service.ListOperatorsResponse()
            pb_resp = lva_service.ListOperatorsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_operators(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_operators_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = lva_service.ListOperatorsResponse.to_json(
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
                    "Received response for google.cloud.visionai_v1.LiveVideoAnalyticsClient.list_operators",
                    extra={
                        "serviceName": "google.cloud.visionai.v1.LiveVideoAnalytics",
                        "rpcName": "ListOperators",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListProcesses(
        _BaseLiveVideoAnalyticsRestTransport._BaseListProcesses,
        LiveVideoAnalyticsRestStub,
    ):
        def __hash__(self):
            return hash("LiveVideoAnalyticsRestTransport.ListProcesses")

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
            request: lva_service.ListProcessesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> lva_service.ListProcessesResponse:
            r"""Call the list processes method over HTTP.

            Args:
                request (~.lva_service.ListProcessesRequest):
                    The request object. Message for requesting list of
                Processes.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.lva_service.ListProcessesResponse:
                    Message for response to listing
                Processes.

            """

            http_options = _BaseLiveVideoAnalyticsRestTransport._BaseListProcesses._get_http_options()
            request, metadata = self._interceptor.pre_list_processes(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLiveVideoAnalyticsRestTransport._BaseListProcesses,
                    "_BaseListProcesses__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.visionai_v1.LiveVideoAnalyticsClient.ListProcesses",
                    extra={
                        "serviceName": "google.cloud.visionai.v1.LiveVideoAnalytics",
                        "rpcName": "ListProcesses",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LiveVideoAnalyticsRestTransport._ListProcesses._get_response(
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
            resp = lva_service.ListProcessesResponse()
            pb_resp = lva_service.ListProcessesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_processes(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_processes_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = lva_service.ListProcessesResponse.to_json(
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
                    "Received response for google.cloud.visionai_v1.LiveVideoAnalyticsClient.list_processes",
                    extra={
                        "serviceName": "google.cloud.visionai.v1.LiveVideoAnalytics",
                        "rpcName": "ListProcesses",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListPublicOperators(
        _BaseLiveVideoAnalyticsRestTransport._BaseListPublicOperators,
        LiveVideoAnalyticsRestStub,
    ):
        def __hash__(self):
            return hash("LiveVideoAnalyticsRestTransport.ListPublicOperators")

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
            request: lva_service.ListPublicOperatorsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> lva_service.ListPublicOperatorsResponse:
            r"""Call the list public operators method over HTTP.

            Args:
                request (~.lva_service.ListPublicOperatorsRequest):
                    The request object. Request message of
                ListPublicOperatorsRequest API.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.lva_service.ListPublicOperatorsResponse:
                    Response message of
                ListPublicOperators API.

            """

            http_options = _BaseLiveVideoAnalyticsRestTransport._BaseListPublicOperators._get_http_options()
            request, metadata = self._interceptor.pre_list_public_operators(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLiveVideoAnalyticsRestTransport._BaseListPublicOperators,
                    "_BaseListPublicOperators__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.visionai_v1.LiveVideoAnalyticsClient.ListPublicOperators",
                    extra={
                        "serviceName": "google.cloud.visionai.v1.LiveVideoAnalytics",
                        "rpcName": "ListPublicOperators",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                LiveVideoAnalyticsRestTransport._ListPublicOperators._get_response(
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
            resp = lva_service.ListPublicOperatorsResponse()
            pb_resp = lva_service.ListPublicOperatorsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_public_operators(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_public_operators_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = lva_service.ListPublicOperatorsResponse.to_json(
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
                    "Received response for google.cloud.visionai_v1.LiveVideoAnalyticsClient.list_public_operators",
                    extra={
                        "serviceName": "google.cloud.visionai.v1.LiveVideoAnalytics",
                        "rpcName": "ListPublicOperators",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ResolveOperatorInfo(
        _BaseLiveVideoAnalyticsRestTransport._BaseResolveOperatorInfo,
        LiveVideoAnalyticsRestStub,
    ):
        def __hash__(self):
            return hash("LiveVideoAnalyticsRestTransport.ResolveOperatorInfo")

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
            request: lva_service.ResolveOperatorInfoRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> lva_service.ResolveOperatorInfoResponse:
            r"""Call the resolve operator info method over HTTP.

            Args:
                request (~.lva_service.ResolveOperatorInfoRequest):
                    The request object. Request message for querying operator
                info.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.lva_service.ResolveOperatorInfoResponse:
                    Response message of
                ResolveOperatorInfo API.

            """

            http_options = _BaseLiveVideoAnalyticsRestTransport._BaseResolveOperatorInfo._get_http_options()
            request, metadata = self._interceptor.pre_resolve_operator_info(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLiveVideoAnalyticsRestTransport._BaseResolveOperatorInfo,
                    "_BaseResolveOperatorInfo__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.visionai_v1.LiveVideoAnalyticsClient.ResolveOperatorInfo",
                    extra={
                        "serviceName": "google.cloud.visionai.v1.LiveVideoAnalytics",
                        "rpcName": "ResolveOperatorInfo",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                LiveVideoAnalyticsRestTransport._ResolveOperatorInfo._get_response(
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
            resp = lva_service.ResolveOperatorInfoResponse()
            pb_resp = lva_service.ResolveOperatorInfoResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_resolve_operator_info(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_resolve_operator_info_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = lva_service.ResolveOperatorInfoResponse.to_json(
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
                    "Received response for google.cloud.visionai_v1.LiveVideoAnalyticsClient.resolve_operator_info",
                    extra={
                        "serviceName": "google.cloud.visionai.v1.LiveVideoAnalytics",
                        "rpcName": "ResolveOperatorInfo",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateAnalysis(
        _BaseLiveVideoAnalyticsRestTransport._BaseUpdateAnalysis,
        LiveVideoAnalyticsRestStub,
    ):
        def __hash__(self):
            return hash("LiveVideoAnalyticsRestTransport.UpdateAnalysis")

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
            request: lva_service.UpdateAnalysisRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update analysis method over HTTP.

            Args:
                request (~.lva_service.UpdateAnalysisRequest):
                    The request object. Message for updating an Analysis.
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

            http_options = _BaseLiveVideoAnalyticsRestTransport._BaseUpdateAnalysis._get_http_options()
            request, metadata = self._interceptor.pre_update_analysis(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLiveVideoAnalyticsRestTransport._BaseUpdateAnalysis,
                    "_BaseUpdateAnalysis__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.visionai_v1.LiveVideoAnalyticsClient.UpdateAnalysis",
                    extra={
                        "serviceName": "google.cloud.visionai.v1.LiveVideoAnalytics",
                        "rpcName": "UpdateAnalysis",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LiveVideoAnalyticsRestTransport._UpdateAnalysis._get_response(
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

            resp = self._interceptor.post_update_analysis(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_analysis_with_metadata(
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
                    "Received response for google.cloud.visionai_v1.LiveVideoAnalyticsClient.update_analysis",
                    extra={
                        "serviceName": "google.cloud.visionai.v1.LiveVideoAnalytics",
                        "rpcName": "UpdateAnalysis",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateOperator(
        _BaseLiveVideoAnalyticsRestTransport._BaseUpdateOperator,
        LiveVideoAnalyticsRestStub,
    ):
        def __hash__(self):
            return hash("LiveVideoAnalyticsRestTransport.UpdateOperator")

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
            request: lva_service.UpdateOperatorRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update operator method over HTTP.

            Args:
                request (~.lva_service.UpdateOperatorRequest):
                    The request object. Message for updating a Operator.
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

            http_options = _BaseLiveVideoAnalyticsRestTransport._BaseUpdateOperator._get_http_options()
            request, metadata = self._interceptor.pre_update_operator(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLiveVideoAnalyticsRestTransport._BaseUpdateOperator,
                    "_BaseUpdateOperator__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.visionai_v1.LiveVideoAnalyticsClient.UpdateOperator",
                    extra={
                        "serviceName": "google.cloud.visionai.v1.LiveVideoAnalytics",
                        "rpcName": "UpdateOperator",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LiveVideoAnalyticsRestTransport._UpdateOperator._get_response(
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

            resp = self._interceptor.post_update_operator(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_operator_with_metadata(
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
                    "Received response for google.cloud.visionai_v1.LiveVideoAnalyticsClient.update_operator",
                    extra={
                        "serviceName": "google.cloud.visionai.v1.LiveVideoAnalytics",
                        "rpcName": "UpdateOperator",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateProcess(
        _BaseLiveVideoAnalyticsRestTransport._BaseUpdateProcess,
        LiveVideoAnalyticsRestStub,
    ):
        def __hash__(self):
            return hash("LiveVideoAnalyticsRestTransport.UpdateProcess")

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
            request: lva_service.UpdateProcessRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update process method over HTTP.

            Args:
                request (~.lva_service.UpdateProcessRequest):
                    The request object. Message for updating a Process.
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

            http_options = _BaseLiveVideoAnalyticsRestTransport._BaseUpdateProcess._get_http_options()
            request, metadata = self._interceptor.pre_update_process(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLiveVideoAnalyticsRestTransport._BaseUpdateProcess,
                    "_BaseUpdateProcess__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.visionai_v1.LiveVideoAnalyticsClient.UpdateProcess",
                    extra={
                        "serviceName": "google.cloud.visionai.v1.LiveVideoAnalytics",
                        "rpcName": "UpdateProcess",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LiveVideoAnalyticsRestTransport._UpdateProcess._get_response(
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

            resp = self._interceptor.post_update_process(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_process_with_metadata(
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
                    "Received response for google.cloud.visionai_v1.LiveVideoAnalyticsClient.update_process",
                    extra={
                        "serviceName": "google.cloud.visionai.v1.LiveVideoAnalytics",
                        "rpcName": "UpdateProcess",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def batch_run_process(
        self,
    ) -> Callable[[lva_service.BatchRunProcessRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchRunProcess(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_analysis(
        self,
    ) -> Callable[[lva_service.CreateAnalysisRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateAnalysis(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_operator(
        self,
    ) -> Callable[[lva_service.CreateOperatorRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateOperator(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_process(
        self,
    ) -> Callable[[lva_service.CreateProcessRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateProcess(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_analysis(
        self,
    ) -> Callable[[lva_service.DeleteAnalysisRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteAnalysis(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_operator(
        self,
    ) -> Callable[[lva_service.DeleteOperatorRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteOperator(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_process(
        self,
    ) -> Callable[[lva_service.DeleteProcessRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteProcess(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_analysis(
        self,
    ) -> Callable[[lva_service.GetAnalysisRequest], lva_resources.Analysis]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetAnalysis(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_operator(
        self,
    ) -> Callable[[lva_service.GetOperatorRequest], lva_resources.Operator]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetOperator(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_process(
        self,
    ) -> Callable[[lva_service.GetProcessRequest], lva_resources.Process]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetProcess(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_analyses(
        self,
    ) -> Callable[[lva_service.ListAnalysesRequest], lva_service.ListAnalysesResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListAnalyses(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_operators(
        self,
    ) -> Callable[
        [lva_service.ListOperatorsRequest], lva_service.ListOperatorsResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListOperators(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_processes(
        self,
    ) -> Callable[
        [lva_service.ListProcessesRequest], lva_service.ListProcessesResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListProcesses(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_public_operators(
        self,
    ) -> Callable[
        [lva_service.ListPublicOperatorsRequest],
        lva_service.ListPublicOperatorsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListPublicOperators(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def resolve_operator_info(
        self,
    ) -> Callable[
        [lva_service.ResolveOperatorInfoRequest],
        lva_service.ResolveOperatorInfoResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ResolveOperatorInfo(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_analysis(
        self,
    ) -> Callable[[lva_service.UpdateAnalysisRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateAnalysis(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_operator(
        self,
    ) -> Callable[[lva_service.UpdateOperatorRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateOperator(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_process(
        self,
    ) -> Callable[[lva_service.UpdateProcessRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateProcess(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_location(self):
        return self._GetLocation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetLocation(
        _BaseLiveVideoAnalyticsRestTransport._BaseGetLocation,
        LiveVideoAnalyticsRestStub,
    ):
        def __hash__(self):
            return hash("LiveVideoAnalyticsRestTransport.GetLocation")

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

            http_options = _BaseLiveVideoAnalyticsRestTransport._BaseGetLocation._get_http_options()
            request, metadata = self._interceptor.pre_get_location(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLiveVideoAnalyticsRestTransport._BaseGetLocation,
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
                    f"Sending request for google.cloud.visionai_v1.LiveVideoAnalyticsClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.visionai.v1.LiveVideoAnalytics",
                        "rpcName": "GetLocation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LiveVideoAnalyticsRestTransport._GetLocation._get_response(
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
                    "Received response for google.cloud.visionai_v1.LiveVideoAnalyticsAsyncClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.visionai.v1.LiveVideoAnalytics",
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
        _BaseLiveVideoAnalyticsRestTransport._BaseListLocations,
        LiveVideoAnalyticsRestStub,
    ):
        def __hash__(self):
            return hash("LiveVideoAnalyticsRestTransport.ListLocations")

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

            http_options = _BaseLiveVideoAnalyticsRestTransport._BaseListLocations._get_http_options()
            request, metadata = self._interceptor.pre_list_locations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLiveVideoAnalyticsRestTransport._BaseListLocations,
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
                    f"Sending request for google.cloud.visionai_v1.LiveVideoAnalyticsClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.visionai.v1.LiveVideoAnalytics",
                        "rpcName": "ListLocations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LiveVideoAnalyticsRestTransport._ListLocations._get_response(
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
                    "Received response for google.cloud.visionai_v1.LiveVideoAnalyticsAsyncClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.visionai.v1.LiveVideoAnalytics",
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
        _BaseLiveVideoAnalyticsRestTransport._BaseCancelOperation,
        LiveVideoAnalyticsRestStub,
    ):
        def __hash__(self):
            return hash("LiveVideoAnalyticsRestTransport.CancelOperation")

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

            http_options = _BaseLiveVideoAnalyticsRestTransport._BaseCancelOperation._get_http_options()
            request, metadata = self._interceptor.pre_cancel_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLiveVideoAnalyticsRestTransport._BaseCancelOperation,
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
                    f"Sending request for google.cloud.visionai_v1.LiveVideoAnalyticsClient.CancelOperation",
                    extra={
                        "serviceName": "google.cloud.visionai.v1.LiveVideoAnalytics",
                        "rpcName": "CancelOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LiveVideoAnalyticsRestTransport._CancelOperation._get_response(
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
        _BaseLiveVideoAnalyticsRestTransport._BaseDeleteOperation,
        LiveVideoAnalyticsRestStub,
    ):
        def __hash__(self):
            return hash("LiveVideoAnalyticsRestTransport.DeleteOperation")

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

            http_options = _BaseLiveVideoAnalyticsRestTransport._BaseDeleteOperation._get_http_options()
            request, metadata = self._interceptor.pre_delete_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLiveVideoAnalyticsRestTransport._BaseDeleteOperation,
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
                    f"Sending request for google.cloud.visionai_v1.LiveVideoAnalyticsClient.DeleteOperation",
                    extra={
                        "serviceName": "google.cloud.visionai.v1.LiveVideoAnalytics",
                        "rpcName": "DeleteOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LiveVideoAnalyticsRestTransport._DeleteOperation._get_response(
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
        _BaseLiveVideoAnalyticsRestTransport._BaseGetOperation,
        LiveVideoAnalyticsRestStub,
    ):
        def __hash__(self):
            return hash("LiveVideoAnalyticsRestTransport.GetOperation")

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

            http_options = _BaseLiveVideoAnalyticsRestTransport._BaseGetOperation._get_http_options()
            request, metadata = self._interceptor.pre_get_operation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLiveVideoAnalyticsRestTransport._BaseGetOperation,
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
                    f"Sending request for google.cloud.visionai_v1.LiveVideoAnalyticsClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.visionai.v1.LiveVideoAnalytics",
                        "rpcName": "GetOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LiveVideoAnalyticsRestTransport._GetOperation._get_response(
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
                    "Received response for google.cloud.visionai_v1.LiveVideoAnalyticsAsyncClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.visionai.v1.LiveVideoAnalytics",
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
        _BaseLiveVideoAnalyticsRestTransport._BaseListOperations,
        LiveVideoAnalyticsRestStub,
    ):
        def __hash__(self):
            return hash("LiveVideoAnalyticsRestTransport.ListOperations")

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

            http_options = _BaseLiveVideoAnalyticsRestTransport._BaseListOperations._get_http_options()
            request, metadata = self._interceptor.pre_list_operations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLiveVideoAnalyticsRestTransport._BaseListOperations,
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
                    f"Sending request for google.cloud.visionai_v1.LiveVideoAnalyticsClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.visionai.v1.LiveVideoAnalytics",
                        "rpcName": "ListOperations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LiveVideoAnalyticsRestTransport._ListOperations._get_response(
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
                    "Received response for google.cloud.visionai_v1.LiveVideoAnalyticsAsyncClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.visionai.v1.LiveVideoAnalytics",
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


__all__ = ("LiveVideoAnalyticsRestTransport",)
