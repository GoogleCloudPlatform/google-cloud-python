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
from google.longrunning import operations_pb2  # type: ignore
from google.protobuf import json_format
from requests import __version__ as requests_version

from google.cloud.workloadmanager_v1._compat import transcode_request
from google.cloud.workloadmanager_v1.types import service

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseWorkloadManagerRestTransport

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


class WorkloadManagerRestInterceptor:
    """Interceptor for WorkloadManager.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the WorkloadManagerRestTransport.

    .. code-block:: python
        class MyCustomWorkloadManagerInterceptor(WorkloadManagerRestInterceptor):
            def pre_create_evaluation(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_evaluation(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_evaluation(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_evaluation(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_execution(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_execution(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_evaluation(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_evaluation(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_execution(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_execution(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_evaluations(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_evaluations(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_execution_results(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_execution_results(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_executions(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_executions(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_rules(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_rules(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_scanned_resources(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_scanned_resources(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_run_evaluation(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_run_evaluation(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_evaluation(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_evaluation(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = WorkloadManagerRestTransport(interceptor=MyCustomWorkloadManagerInterceptor())
        client = WorkloadManagerClient(transport=transport)


    """

    def pre_create_evaluation(
        self,
        request: service.CreateEvaluationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.CreateEvaluationRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_evaluation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the WorkloadManager server.
        """
        return request, metadata

    def post_create_evaluation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_evaluation

        DEPRECATED. Please use the `post_create_evaluation_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the WorkloadManager server but before
        it is returned to user code. This `post_create_evaluation` interceptor runs
        before the `post_create_evaluation_with_metadata` interceptor.
        """
        return response

    def post_create_evaluation_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_evaluation

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the WorkloadManager server but before it is returned to user code.

        We recommend only using this `post_create_evaluation_with_metadata`
        interceptor in new development instead of the `post_create_evaluation` interceptor.
        When both interceptors are used, this `post_create_evaluation_with_metadata` interceptor runs after the
        `post_create_evaluation` interceptor. The (possibly modified) response returned by
        `post_create_evaluation` will be passed to
        `post_create_evaluation_with_metadata`.
        """
        return response, metadata

    def pre_delete_evaluation(
        self,
        request: service.DeleteEvaluationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.DeleteEvaluationRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_evaluation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the WorkloadManager server.
        """
        return request, metadata

    def post_delete_evaluation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_evaluation

        DEPRECATED. Please use the `post_delete_evaluation_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the WorkloadManager server but before
        it is returned to user code. This `post_delete_evaluation` interceptor runs
        before the `post_delete_evaluation_with_metadata` interceptor.
        """
        return response

    def post_delete_evaluation_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_evaluation

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the WorkloadManager server but before it is returned to user code.

        We recommend only using this `post_delete_evaluation_with_metadata`
        interceptor in new development instead of the `post_delete_evaluation` interceptor.
        When both interceptors are used, this `post_delete_evaluation_with_metadata` interceptor runs after the
        `post_delete_evaluation` interceptor. The (possibly modified) response returned by
        `post_delete_evaluation` will be passed to
        `post_delete_evaluation_with_metadata`.
        """
        return response, metadata

    def pre_delete_execution(
        self,
        request: service.DeleteExecutionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.DeleteExecutionRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for delete_execution

        Override in a subclass to manipulate the request or metadata
        before they are sent to the WorkloadManager server.
        """
        return request, metadata

    def post_delete_execution(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_execution

        DEPRECATED. Please use the `post_delete_execution_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the WorkloadManager server but before
        it is returned to user code. This `post_delete_execution` interceptor runs
        before the `post_delete_execution_with_metadata` interceptor.
        """
        return response

    def post_delete_execution_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_execution

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the WorkloadManager server but before it is returned to user code.

        We recommend only using this `post_delete_execution_with_metadata`
        interceptor in new development instead of the `post_delete_execution` interceptor.
        When both interceptors are used, this `post_delete_execution_with_metadata` interceptor runs after the
        `post_delete_execution` interceptor. The (possibly modified) response returned by
        `post_delete_execution` will be passed to
        `post_delete_execution_with_metadata`.
        """
        return response, metadata

    def pre_get_evaluation(
        self,
        request: service.GetEvaluationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.GetEvaluationRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_evaluation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the WorkloadManager server.
        """
        return request, metadata

    def post_get_evaluation(self, response: service.Evaluation) -> service.Evaluation:
        """Post-rpc interceptor for get_evaluation

        DEPRECATED. Please use the `post_get_evaluation_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the WorkloadManager server but before
        it is returned to user code. This `post_get_evaluation` interceptor runs
        before the `post_get_evaluation_with_metadata` interceptor.
        """
        return response

    def post_get_evaluation_with_metadata(
        self,
        response: service.Evaluation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.Evaluation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_evaluation

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the WorkloadManager server but before it is returned to user code.

        We recommend only using this `post_get_evaluation_with_metadata`
        interceptor in new development instead of the `post_get_evaluation` interceptor.
        When both interceptors are used, this `post_get_evaluation_with_metadata` interceptor runs after the
        `post_get_evaluation` interceptor. The (possibly modified) response returned by
        `post_get_evaluation` will be passed to
        `post_get_evaluation_with_metadata`.
        """
        return response, metadata

    def pre_get_execution(
        self,
        request: service.GetExecutionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.GetExecutionRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_execution

        Override in a subclass to manipulate the request or metadata
        before they are sent to the WorkloadManager server.
        """
        return request, metadata

    def post_get_execution(self, response: service.Execution) -> service.Execution:
        """Post-rpc interceptor for get_execution

        DEPRECATED. Please use the `post_get_execution_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the WorkloadManager server but before
        it is returned to user code. This `post_get_execution` interceptor runs
        before the `post_get_execution_with_metadata` interceptor.
        """
        return response

    def post_get_execution_with_metadata(
        self,
        response: service.Execution,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.Execution, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_execution

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the WorkloadManager server but before it is returned to user code.

        We recommend only using this `post_get_execution_with_metadata`
        interceptor in new development instead of the `post_get_execution` interceptor.
        When both interceptors are used, this `post_get_execution_with_metadata` interceptor runs after the
        `post_get_execution` interceptor. The (possibly modified) response returned by
        `post_get_execution` will be passed to
        `post_get_execution_with_metadata`.
        """
        return response, metadata

    def pre_list_evaluations(
        self,
        request: service.ListEvaluationsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.ListEvaluationsRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for list_evaluations

        Override in a subclass to manipulate the request or metadata
        before they are sent to the WorkloadManager server.
        """
        return request, metadata

    def post_list_evaluations(
        self, response: service.ListEvaluationsResponse
    ) -> service.ListEvaluationsResponse:
        """Post-rpc interceptor for list_evaluations

        DEPRECATED. Please use the `post_list_evaluations_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the WorkloadManager server but before
        it is returned to user code. This `post_list_evaluations` interceptor runs
        before the `post_list_evaluations_with_metadata` interceptor.
        """
        return response

    def post_list_evaluations_with_metadata(
        self,
        response: service.ListEvaluationsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.ListEvaluationsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_evaluations

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the WorkloadManager server but before it is returned to user code.

        We recommend only using this `post_list_evaluations_with_metadata`
        interceptor in new development instead of the `post_list_evaluations` interceptor.
        When both interceptors are used, this `post_list_evaluations_with_metadata` interceptor runs after the
        `post_list_evaluations` interceptor. The (possibly modified) response returned by
        `post_list_evaluations` will be passed to
        `post_list_evaluations_with_metadata`.
        """
        return response, metadata

    def pre_list_execution_results(
        self,
        request: service.ListExecutionResultsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.ListExecutionResultsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_execution_results

        Override in a subclass to manipulate the request or metadata
        before they are sent to the WorkloadManager server.
        """
        return request, metadata

    def post_list_execution_results(
        self, response: service.ListExecutionResultsResponse
    ) -> service.ListExecutionResultsResponse:
        """Post-rpc interceptor for list_execution_results

        DEPRECATED. Please use the `post_list_execution_results_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the WorkloadManager server but before
        it is returned to user code. This `post_list_execution_results` interceptor runs
        before the `post_list_execution_results_with_metadata` interceptor.
        """
        return response

    def post_list_execution_results_with_metadata(
        self,
        response: service.ListExecutionResultsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.ListExecutionResultsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_execution_results

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the WorkloadManager server but before it is returned to user code.

        We recommend only using this `post_list_execution_results_with_metadata`
        interceptor in new development instead of the `post_list_execution_results` interceptor.
        When both interceptors are used, this `post_list_execution_results_with_metadata` interceptor runs after the
        `post_list_execution_results` interceptor. The (possibly modified) response returned by
        `post_list_execution_results` will be passed to
        `post_list_execution_results_with_metadata`.
        """
        return response, metadata

    def pre_list_executions(
        self,
        request: service.ListExecutionsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.ListExecutionsRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for list_executions

        Override in a subclass to manipulate the request or metadata
        before they are sent to the WorkloadManager server.
        """
        return request, metadata

    def post_list_executions(
        self, response: service.ListExecutionsResponse
    ) -> service.ListExecutionsResponse:
        """Post-rpc interceptor for list_executions

        DEPRECATED. Please use the `post_list_executions_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the WorkloadManager server but before
        it is returned to user code. This `post_list_executions` interceptor runs
        before the `post_list_executions_with_metadata` interceptor.
        """
        return response

    def post_list_executions_with_metadata(
        self,
        response: service.ListExecutionsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.ListExecutionsResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for list_executions

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the WorkloadManager server but before it is returned to user code.

        We recommend only using this `post_list_executions_with_metadata`
        interceptor in new development instead of the `post_list_executions` interceptor.
        When both interceptors are used, this `post_list_executions_with_metadata` interceptor runs after the
        `post_list_executions` interceptor. The (possibly modified) response returned by
        `post_list_executions` will be passed to
        `post_list_executions_with_metadata`.
        """
        return response, metadata

    def pre_list_rules(
        self,
        request: service.ListRulesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.ListRulesRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for list_rules

        Override in a subclass to manipulate the request or metadata
        before they are sent to the WorkloadManager server.
        """
        return request, metadata

    def post_list_rules(
        self, response: service.ListRulesResponse
    ) -> service.ListRulesResponse:
        """Post-rpc interceptor for list_rules

        DEPRECATED. Please use the `post_list_rules_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the WorkloadManager server but before
        it is returned to user code. This `post_list_rules` interceptor runs
        before the `post_list_rules_with_metadata` interceptor.
        """
        return response

    def post_list_rules_with_metadata(
        self,
        response: service.ListRulesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.ListRulesResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for list_rules

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the WorkloadManager server but before it is returned to user code.

        We recommend only using this `post_list_rules_with_metadata`
        interceptor in new development instead of the `post_list_rules` interceptor.
        When both interceptors are used, this `post_list_rules_with_metadata` interceptor runs after the
        `post_list_rules` interceptor. The (possibly modified) response returned by
        `post_list_rules` will be passed to
        `post_list_rules_with_metadata`.
        """
        return response, metadata

    def pre_list_scanned_resources(
        self,
        request: service.ListScannedResourcesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.ListScannedResourcesRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_scanned_resources

        Override in a subclass to manipulate the request or metadata
        before they are sent to the WorkloadManager server.
        """
        return request, metadata

    def post_list_scanned_resources(
        self, response: service.ListScannedResourcesResponse
    ) -> service.ListScannedResourcesResponse:
        """Post-rpc interceptor for list_scanned_resources

        DEPRECATED. Please use the `post_list_scanned_resources_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the WorkloadManager server but before
        it is returned to user code. This `post_list_scanned_resources` interceptor runs
        before the `post_list_scanned_resources_with_metadata` interceptor.
        """
        return response

    def post_list_scanned_resources_with_metadata(
        self,
        response: service.ListScannedResourcesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.ListScannedResourcesResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_scanned_resources

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the WorkloadManager server but before it is returned to user code.

        We recommend only using this `post_list_scanned_resources_with_metadata`
        interceptor in new development instead of the `post_list_scanned_resources` interceptor.
        When both interceptors are used, this `post_list_scanned_resources_with_metadata` interceptor runs after the
        `post_list_scanned_resources` interceptor. The (possibly modified) response returned by
        `post_list_scanned_resources` will be passed to
        `post_list_scanned_resources_with_metadata`.
        """
        return response, metadata

    def pre_run_evaluation(
        self,
        request: service.RunEvaluationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.RunEvaluationRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for run_evaluation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the WorkloadManager server.
        """
        return request, metadata

    def post_run_evaluation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for run_evaluation

        DEPRECATED. Please use the `post_run_evaluation_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the WorkloadManager server but before
        it is returned to user code. This `post_run_evaluation` interceptor runs
        before the `post_run_evaluation_with_metadata` interceptor.
        """
        return response

    def post_run_evaluation_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for run_evaluation

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the WorkloadManager server but before it is returned to user code.

        We recommend only using this `post_run_evaluation_with_metadata`
        interceptor in new development instead of the `post_run_evaluation` interceptor.
        When both interceptors are used, this `post_run_evaluation_with_metadata` interceptor runs after the
        `post_run_evaluation` interceptor. The (possibly modified) response returned by
        `post_run_evaluation` will be passed to
        `post_run_evaluation_with_metadata`.
        """
        return response, metadata

    def pre_update_evaluation(
        self,
        request: service.UpdateEvaluationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.UpdateEvaluationRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_evaluation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the WorkloadManager server.
        """
        return request, metadata

    def post_update_evaluation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_evaluation

        DEPRECATED. Please use the `post_update_evaluation_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the WorkloadManager server but before
        it is returned to user code. This `post_update_evaluation` interceptor runs
        before the `post_update_evaluation_with_metadata` interceptor.
        """
        return response

    def post_update_evaluation_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_evaluation

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the WorkloadManager server but before it is returned to user code.

        We recommend only using this `post_update_evaluation_with_metadata`
        interceptor in new development instead of the `post_update_evaluation` interceptor.
        When both interceptors are used, this `post_update_evaluation_with_metadata` interceptor runs after the
        `post_update_evaluation` interceptor. The (possibly modified) response returned by
        `post_update_evaluation` will be passed to
        `post_update_evaluation_with_metadata`.
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
        before they are sent to the WorkloadManager server.
        """
        return request, metadata

    def post_get_location(
        self, response: locations_pb2.Location
    ) -> locations_pb2.Location:
        """Post-rpc interceptor for get_location

        Override in a subclass to manipulate the response
        after it is returned by the WorkloadManager server but before
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
        before they are sent to the WorkloadManager server.
        """
        return request, metadata

    def post_list_locations(
        self, response: locations_pb2.ListLocationsResponse
    ) -> locations_pb2.ListLocationsResponse:
        """Post-rpc interceptor for list_locations

        Override in a subclass to manipulate the response
        after it is returned by the WorkloadManager server but before
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
        before they are sent to the WorkloadManager server.
        """
        return request, metadata

    def post_cancel_operation(self, response: None) -> None:
        """Post-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the response
        after it is returned by the WorkloadManager server but before
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
        before they are sent to the WorkloadManager server.
        """
        return request, metadata

    def post_delete_operation(self, response: None) -> None:
        """Post-rpc interceptor for delete_operation

        Override in a subclass to manipulate the response
        after it is returned by the WorkloadManager server but before
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
        before they are sent to the WorkloadManager server.
        """
        return request, metadata

    def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the WorkloadManager server but before
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
        before they are sent to the WorkloadManager server.
        """
        return request, metadata

    def post_list_operations(
        self, response: operations_pb2.ListOperationsResponse
    ) -> operations_pb2.ListOperationsResponse:
        """Post-rpc interceptor for list_operations

        Override in a subclass to manipulate the response
        after it is returned by the WorkloadManager server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class WorkloadManagerRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: WorkloadManagerRestInterceptor


class WorkloadManagerRestTransport(_BaseWorkloadManagerRestTransport):
    """REST backend synchronous transport for WorkloadManager.

    The Workload Manager provides various tools to deploy,
    validate and observe your workloads running on Google Cloud.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "workloadmanager.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[WorkloadManagerRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'workloadmanager.googleapis.com').
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
            interceptor (Optional[WorkloadManagerRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or WorkloadManagerRestInterceptor()
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

    class _CreateEvaluation(
        _BaseWorkloadManagerRestTransport._BaseCreateEvaluation, WorkloadManagerRestStub
    ):
        def __hash__(self):
            return hash("WorkloadManagerRestTransport.CreateEvaluation")

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
            request: service.CreateEvaluationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create evaluation method over HTTP.

            Args:
                request (~.service.CreateEvaluationRequest):
                    The request object. Request message for the
                CreateEvaluation RPC.
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

            http_options = _BaseWorkloadManagerRestTransport._BaseCreateEvaluation._get_http_options()
            request, metadata = self._interceptor.pre_create_evaluation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseWorkloadManagerRestTransport._BaseCreateEvaluation,
                    "_BaseCreateEvaluation__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.workloadmanager_v1.WorkloadManagerClient.CreateEvaluation",
                    extra={
                        "serviceName": "google.cloud.workloadmanager.v1.WorkloadManager",
                        "rpcName": "CreateEvaluation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = WorkloadManagerRestTransport._CreateEvaluation._get_response(
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

            resp = self._interceptor.post_create_evaluation(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_evaluation_with_metadata(
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
                    "Received response for google.cloud.workloadmanager_v1.WorkloadManagerClient.create_evaluation",
                    extra={
                        "serviceName": "google.cloud.workloadmanager.v1.WorkloadManager",
                        "rpcName": "CreateEvaluation",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteEvaluation(
        _BaseWorkloadManagerRestTransport._BaseDeleteEvaluation, WorkloadManagerRestStub
    ):
        def __hash__(self):
            return hash("WorkloadManagerRestTransport.DeleteEvaluation")

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
            request: service.DeleteEvaluationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete evaluation method over HTTP.

            Args:
                request (~.service.DeleteEvaluationRequest):
                    The request object. Request message for the
                DeleteEvaluation RPC.
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

            http_options = _BaseWorkloadManagerRestTransport._BaseDeleteEvaluation._get_http_options()
            request, metadata = self._interceptor.pre_delete_evaluation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseWorkloadManagerRestTransport._BaseDeleteEvaluation,
                    "_BaseDeleteEvaluation__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.workloadmanager_v1.WorkloadManagerClient.DeleteEvaluation",
                    extra={
                        "serviceName": "google.cloud.workloadmanager.v1.WorkloadManager",
                        "rpcName": "DeleteEvaluation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = WorkloadManagerRestTransport._DeleteEvaluation._get_response(
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

            resp = self._interceptor.post_delete_evaluation(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_evaluation_with_metadata(
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
                    "Received response for google.cloud.workloadmanager_v1.WorkloadManagerClient.delete_evaluation",
                    extra={
                        "serviceName": "google.cloud.workloadmanager.v1.WorkloadManager",
                        "rpcName": "DeleteEvaluation",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteExecution(
        _BaseWorkloadManagerRestTransport._BaseDeleteExecution, WorkloadManagerRestStub
    ):
        def __hash__(self):
            return hash("WorkloadManagerRestTransport.DeleteExecution")

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
            request: service.DeleteExecutionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete execution method over HTTP.

            Args:
                request (~.service.DeleteExecutionRequest):
                    The request object. Request message for the
                DeleteExecution RPC.
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

            http_options = _BaseWorkloadManagerRestTransport._BaseDeleteExecution._get_http_options()
            request, metadata = self._interceptor.pre_delete_execution(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseWorkloadManagerRestTransport._BaseDeleteExecution,
                    "_BaseDeleteExecution__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.workloadmanager_v1.WorkloadManagerClient.DeleteExecution",
                    extra={
                        "serviceName": "google.cloud.workloadmanager.v1.WorkloadManager",
                        "rpcName": "DeleteExecution",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = WorkloadManagerRestTransport._DeleteExecution._get_response(
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

            resp = self._interceptor.post_delete_execution(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_execution_with_metadata(
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
                    "Received response for google.cloud.workloadmanager_v1.WorkloadManagerClient.delete_execution",
                    extra={
                        "serviceName": "google.cloud.workloadmanager.v1.WorkloadManager",
                        "rpcName": "DeleteExecution",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetEvaluation(
        _BaseWorkloadManagerRestTransport._BaseGetEvaluation, WorkloadManagerRestStub
    ):
        def __hash__(self):
            return hash("WorkloadManagerRestTransport.GetEvaluation")

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
            request: service.GetEvaluationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> service.Evaluation:
            r"""Call the get evaluation method over HTTP.

            Args:
                request (~.service.GetEvaluationRequest):
                    The request object. Request message for the GetEvaluation
                RPC.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.service.Evaluation:
                    Represents a Workload Manager
                Evaluation configuration. An Evaluation
                defines a set of rules to be validated
                against a scope of Cloud resources.

            """

            http_options = (
                _BaseWorkloadManagerRestTransport._BaseGetEvaluation._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_evaluation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseWorkloadManagerRestTransport._BaseGetEvaluation,
                    "_BaseGetEvaluation__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.workloadmanager_v1.WorkloadManagerClient.GetEvaluation",
                    extra={
                        "serviceName": "google.cloud.workloadmanager.v1.WorkloadManager",
                        "rpcName": "GetEvaluation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = WorkloadManagerRestTransport._GetEvaluation._get_response(
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
            resp = service.Evaluation()
            pb_resp = service.Evaluation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_evaluation(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_evaluation_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = service.Evaluation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.workloadmanager_v1.WorkloadManagerClient.get_evaluation",
                    extra={
                        "serviceName": "google.cloud.workloadmanager.v1.WorkloadManager",
                        "rpcName": "GetEvaluation",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetExecution(
        _BaseWorkloadManagerRestTransport._BaseGetExecution, WorkloadManagerRestStub
    ):
        def __hash__(self):
            return hash("WorkloadManagerRestTransport.GetExecution")

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
            request: service.GetExecutionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> service.Execution:
            r"""Call the get execution method over HTTP.

            Args:
                request (~.service.GetExecutionRequest):
                    The request object. Request message for the GetExecution
                RPC.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.service.Execution:
                    Execution that represents a single
                run of an Evaluation.

            """

            http_options = (
                _BaseWorkloadManagerRestTransport._BaseGetExecution._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_execution(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseWorkloadManagerRestTransport._BaseGetExecution,
                    "_BaseGetExecution__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.workloadmanager_v1.WorkloadManagerClient.GetExecution",
                    extra={
                        "serviceName": "google.cloud.workloadmanager.v1.WorkloadManager",
                        "rpcName": "GetExecution",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = WorkloadManagerRestTransport._GetExecution._get_response(
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
            resp = service.Execution()
            pb_resp = service.Execution.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_execution(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_execution_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = service.Execution.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.workloadmanager_v1.WorkloadManagerClient.get_execution",
                    extra={
                        "serviceName": "google.cloud.workloadmanager.v1.WorkloadManager",
                        "rpcName": "GetExecution",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListEvaluations(
        _BaseWorkloadManagerRestTransport._BaseListEvaluations, WorkloadManagerRestStub
    ):
        def __hash__(self):
            return hash("WorkloadManagerRestTransport.ListEvaluations")

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
            request: service.ListEvaluationsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> service.ListEvaluationsResponse:
            r"""Call the list evaluations method over HTTP.

            Args:
                request (~.service.ListEvaluationsRequest):
                    The request object. Request message for the
                ListEvaluations RPC.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.service.ListEvaluationsResponse:
                    Response message for the
                ListEvaluations RPC.

            """

            http_options = _BaseWorkloadManagerRestTransport._BaseListEvaluations._get_http_options()
            request, metadata = self._interceptor.pre_list_evaluations(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseWorkloadManagerRestTransport._BaseListEvaluations,
                    "_BaseListEvaluations__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.workloadmanager_v1.WorkloadManagerClient.ListEvaluations",
                    extra={
                        "serviceName": "google.cloud.workloadmanager.v1.WorkloadManager",
                        "rpcName": "ListEvaluations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = WorkloadManagerRestTransport._ListEvaluations._get_response(
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
            resp = service.ListEvaluationsResponse()
            pb_resp = service.ListEvaluationsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_evaluations(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_evaluations_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = service.ListEvaluationsResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.workloadmanager_v1.WorkloadManagerClient.list_evaluations",
                    extra={
                        "serviceName": "google.cloud.workloadmanager.v1.WorkloadManager",
                        "rpcName": "ListEvaluations",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListExecutionResults(
        _BaseWorkloadManagerRestTransport._BaseListExecutionResults,
        WorkloadManagerRestStub,
    ):
        def __hash__(self):
            return hash("WorkloadManagerRestTransport.ListExecutionResults")

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
            request: service.ListExecutionResultsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> service.ListExecutionResultsResponse:
            r"""Call the list execution results method over HTTP.

            Args:
                request (~.service.ListExecutionResultsRequest):
                    The request object. Request message for the
                ListExecutionResults RPC.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.service.ListExecutionResultsResponse:
                    Response message for the
                ListExecutionResults RPC.

            """

            http_options = _BaseWorkloadManagerRestTransport._BaseListExecutionResults._get_http_options()
            request, metadata = self._interceptor.pre_list_execution_results(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseWorkloadManagerRestTransport._BaseListExecutionResults,
                    "_BaseListExecutionResults__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.workloadmanager_v1.WorkloadManagerClient.ListExecutionResults",
                    extra={
                        "serviceName": "google.cloud.workloadmanager.v1.WorkloadManager",
                        "rpcName": "ListExecutionResults",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = WorkloadManagerRestTransport._ListExecutionResults._get_response(
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
            resp = service.ListExecutionResultsResponse()
            pb_resp = service.ListExecutionResultsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_execution_results(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_execution_results_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = service.ListExecutionResultsResponse.to_json(
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
                    "Received response for google.cloud.workloadmanager_v1.WorkloadManagerClient.list_execution_results",
                    extra={
                        "serviceName": "google.cloud.workloadmanager.v1.WorkloadManager",
                        "rpcName": "ListExecutionResults",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListExecutions(
        _BaseWorkloadManagerRestTransport._BaseListExecutions, WorkloadManagerRestStub
    ):
        def __hash__(self):
            return hash("WorkloadManagerRestTransport.ListExecutions")

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
            request: service.ListExecutionsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> service.ListExecutionsResponse:
            r"""Call the list executions method over HTTP.

            Args:
                request (~.service.ListExecutionsRequest):
                    The request object. Request message for the
                ListExecutions RPC.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.service.ListExecutionsResponse:
                    Response message for the
                ListExecutions RPC.

            """

            http_options = _BaseWorkloadManagerRestTransport._BaseListExecutions._get_http_options()
            request, metadata = self._interceptor.pre_list_executions(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseWorkloadManagerRestTransport._BaseListExecutions,
                    "_BaseListExecutions__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.workloadmanager_v1.WorkloadManagerClient.ListExecutions",
                    extra={
                        "serviceName": "google.cloud.workloadmanager.v1.WorkloadManager",
                        "rpcName": "ListExecutions",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = WorkloadManagerRestTransport._ListExecutions._get_response(
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
            resp = service.ListExecutionsResponse()
            pb_resp = service.ListExecutionsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_executions(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_executions_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = service.ListExecutionsResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.workloadmanager_v1.WorkloadManagerClient.list_executions",
                    extra={
                        "serviceName": "google.cloud.workloadmanager.v1.WorkloadManager",
                        "rpcName": "ListExecutions",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListRules(
        _BaseWorkloadManagerRestTransport._BaseListRules, WorkloadManagerRestStub
    ):
        def __hash__(self):
            return hash("WorkloadManagerRestTransport.ListRules")

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
            request: service.ListRulesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> service.ListRulesResponse:
            r"""Call the list rules method over HTTP.

            Args:
                request (~.service.ListRulesRequest):
                    The request object. Request message for the ListRules
                RPC.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.service.ListRulesResponse:
                    Response message for the ListRules
                RPC.

            """

            http_options = (
                _BaseWorkloadManagerRestTransport._BaseListRules._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_rules(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseWorkloadManagerRestTransport._BaseListRules,
                    "_BaseListRules__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.workloadmanager_v1.WorkloadManagerClient.ListRules",
                    extra={
                        "serviceName": "google.cloud.workloadmanager.v1.WorkloadManager",
                        "rpcName": "ListRules",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = WorkloadManagerRestTransport._ListRules._get_response(
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
            resp = service.ListRulesResponse()
            pb_resp = service.ListRulesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_rules(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_rules_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = service.ListRulesResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.workloadmanager_v1.WorkloadManagerClient.list_rules",
                    extra={
                        "serviceName": "google.cloud.workloadmanager.v1.WorkloadManager",
                        "rpcName": "ListRules",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListScannedResources(
        _BaseWorkloadManagerRestTransport._BaseListScannedResources,
        WorkloadManagerRestStub,
    ):
        def __hash__(self):
            return hash("WorkloadManagerRestTransport.ListScannedResources")

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
            request: service.ListScannedResourcesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> service.ListScannedResourcesResponse:
            r"""Call the list scanned resources method over HTTP.

            Args:
                request (~.service.ListScannedResourcesRequest):
                    The request object. Request message for the
                ListScannedResources RPC.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.service.ListScannedResourcesResponse:
                    Response message for the
                ListScannedResources RPC.

            """

            http_options = _BaseWorkloadManagerRestTransport._BaseListScannedResources._get_http_options()
            request, metadata = self._interceptor.pre_list_scanned_resources(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseWorkloadManagerRestTransport._BaseListScannedResources,
                    "_BaseListScannedResources__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.workloadmanager_v1.WorkloadManagerClient.ListScannedResources",
                    extra={
                        "serviceName": "google.cloud.workloadmanager.v1.WorkloadManager",
                        "rpcName": "ListScannedResources",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = WorkloadManagerRestTransport._ListScannedResources._get_response(
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
            resp = service.ListScannedResourcesResponse()
            pb_resp = service.ListScannedResourcesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_scanned_resources(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_scanned_resources_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = service.ListScannedResourcesResponse.to_json(
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
                    "Received response for google.cloud.workloadmanager_v1.WorkloadManagerClient.list_scanned_resources",
                    extra={
                        "serviceName": "google.cloud.workloadmanager.v1.WorkloadManager",
                        "rpcName": "ListScannedResources",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _RunEvaluation(
        _BaseWorkloadManagerRestTransport._BaseRunEvaluation, WorkloadManagerRestStub
    ):
        def __hash__(self):
            return hash("WorkloadManagerRestTransport.RunEvaluation")

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
            request: service.RunEvaluationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the run evaluation method over HTTP.

            Args:
                request (~.service.RunEvaluationRequest):
                    The request object. Request message for the RunEvaluation
                RPC.
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
                _BaseWorkloadManagerRestTransport._BaseRunEvaluation._get_http_options()
            )
            request, metadata = self._interceptor.pre_run_evaluation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseWorkloadManagerRestTransport._BaseRunEvaluation,
                    "_BaseRunEvaluation__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.workloadmanager_v1.WorkloadManagerClient.RunEvaluation",
                    extra={
                        "serviceName": "google.cloud.workloadmanager.v1.WorkloadManager",
                        "rpcName": "RunEvaluation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = WorkloadManagerRestTransport._RunEvaluation._get_response(
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

            resp = self._interceptor.post_run_evaluation(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_run_evaluation_with_metadata(
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
                    "Received response for google.cloud.workloadmanager_v1.WorkloadManagerClient.run_evaluation",
                    extra={
                        "serviceName": "google.cloud.workloadmanager.v1.WorkloadManager",
                        "rpcName": "RunEvaluation",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateEvaluation(
        _BaseWorkloadManagerRestTransport._BaseUpdateEvaluation, WorkloadManagerRestStub
    ):
        def __hash__(self):
            return hash("WorkloadManagerRestTransport.UpdateEvaluation")

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
            request: service.UpdateEvaluationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update evaluation method over HTTP.

            Args:
                request (~.service.UpdateEvaluationRequest):
                    The request object. Request message for the
                UpdateEvaluation RPC.
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

            http_options = _BaseWorkloadManagerRestTransport._BaseUpdateEvaluation._get_http_options()
            request, metadata = self._interceptor.pre_update_evaluation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseWorkloadManagerRestTransport._BaseUpdateEvaluation,
                    "_BaseUpdateEvaluation__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.workloadmanager_v1.WorkloadManagerClient.UpdateEvaluation",
                    extra={
                        "serviceName": "google.cloud.workloadmanager.v1.WorkloadManager",
                        "rpcName": "UpdateEvaluation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = WorkloadManagerRestTransport._UpdateEvaluation._get_response(
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

            resp = self._interceptor.post_update_evaluation(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_evaluation_with_metadata(
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
                    "Received response for google.cloud.workloadmanager_v1.WorkloadManagerClient.update_evaluation",
                    extra={
                        "serviceName": "google.cloud.workloadmanager.v1.WorkloadManager",
                        "rpcName": "UpdateEvaluation",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def create_evaluation(
        self,
    ) -> Callable[[service.CreateEvaluationRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateEvaluation(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_evaluation(
        self,
    ) -> Callable[[service.DeleteEvaluationRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteEvaluation(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_execution(
        self,
    ) -> Callable[[service.DeleteExecutionRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteExecution(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_evaluation(
        self,
    ) -> Callable[[service.GetEvaluationRequest], service.Evaluation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetEvaluation(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_execution(
        self,
    ) -> Callable[[service.GetExecutionRequest], service.Execution]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetExecution(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_evaluations(
        self,
    ) -> Callable[[service.ListEvaluationsRequest], service.ListEvaluationsResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListEvaluations(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_execution_results(
        self,
    ) -> Callable[
        [service.ListExecutionResultsRequest], service.ListExecutionResultsResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListExecutionResults(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_executions(
        self,
    ) -> Callable[[service.ListExecutionsRequest], service.ListExecutionsResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListExecutions(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_rules(
        self,
    ) -> Callable[[service.ListRulesRequest], service.ListRulesResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListRules(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_scanned_resources(
        self,
    ) -> Callable[
        [service.ListScannedResourcesRequest], service.ListScannedResourcesResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListScannedResources(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def run_evaluation(
        self,
    ) -> Callable[[service.RunEvaluationRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._RunEvaluation(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_evaluation(
        self,
    ) -> Callable[[service.UpdateEvaluationRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateEvaluation(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_location(self):
        return self._GetLocation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetLocation(
        _BaseWorkloadManagerRestTransport._BaseGetLocation, WorkloadManagerRestStub
    ):
        def __hash__(self):
            return hash("WorkloadManagerRestTransport.GetLocation")

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
                _BaseWorkloadManagerRestTransport._BaseGetLocation._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_location(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseWorkloadManagerRestTransport._BaseGetLocation,
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
                    f"Sending request for google.cloud.workloadmanager_v1.WorkloadManagerClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.workloadmanager.v1.WorkloadManager",
                        "rpcName": "GetLocation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = WorkloadManagerRestTransport._GetLocation._get_response(
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
                    "Received response for google.cloud.workloadmanager_v1.WorkloadManagerAsyncClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.workloadmanager.v1.WorkloadManager",
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
        _BaseWorkloadManagerRestTransport._BaseListLocations, WorkloadManagerRestStub
    ):
        def __hash__(self):
            return hash("WorkloadManagerRestTransport.ListLocations")

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
                _BaseWorkloadManagerRestTransport._BaseListLocations._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_locations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseWorkloadManagerRestTransport._BaseListLocations,
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
                    f"Sending request for google.cloud.workloadmanager_v1.WorkloadManagerClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.workloadmanager.v1.WorkloadManager",
                        "rpcName": "ListLocations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = WorkloadManagerRestTransport._ListLocations._get_response(
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
                    "Received response for google.cloud.workloadmanager_v1.WorkloadManagerAsyncClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.workloadmanager.v1.WorkloadManager",
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
        _BaseWorkloadManagerRestTransport._BaseCancelOperation, WorkloadManagerRestStub
    ):
        def __hash__(self):
            return hash("WorkloadManagerRestTransport.CancelOperation")

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

            http_options = _BaseWorkloadManagerRestTransport._BaseCancelOperation._get_http_options()
            request, metadata = self._interceptor.pre_cancel_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseWorkloadManagerRestTransport._BaseCancelOperation,
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
                    f"Sending request for google.cloud.workloadmanager_v1.WorkloadManagerClient.CancelOperation",
                    extra={
                        "serviceName": "google.cloud.workloadmanager.v1.WorkloadManager",
                        "rpcName": "CancelOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = WorkloadManagerRestTransport._CancelOperation._get_response(
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
        _BaseWorkloadManagerRestTransport._BaseDeleteOperation, WorkloadManagerRestStub
    ):
        def __hash__(self):
            return hash("WorkloadManagerRestTransport.DeleteOperation")

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

            http_options = _BaseWorkloadManagerRestTransport._BaseDeleteOperation._get_http_options()
            request, metadata = self._interceptor.pre_delete_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseWorkloadManagerRestTransport._BaseDeleteOperation,
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
                    f"Sending request for google.cloud.workloadmanager_v1.WorkloadManagerClient.DeleteOperation",
                    extra={
                        "serviceName": "google.cloud.workloadmanager.v1.WorkloadManager",
                        "rpcName": "DeleteOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = WorkloadManagerRestTransport._DeleteOperation._get_response(
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
        _BaseWorkloadManagerRestTransport._BaseGetOperation, WorkloadManagerRestStub
    ):
        def __hash__(self):
            return hash("WorkloadManagerRestTransport.GetOperation")

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
                _BaseWorkloadManagerRestTransport._BaseGetOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_operation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseWorkloadManagerRestTransport._BaseGetOperation,
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
                    f"Sending request for google.cloud.workloadmanager_v1.WorkloadManagerClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.workloadmanager.v1.WorkloadManager",
                        "rpcName": "GetOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = WorkloadManagerRestTransport._GetOperation._get_response(
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
                    "Received response for google.cloud.workloadmanager_v1.WorkloadManagerAsyncClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.workloadmanager.v1.WorkloadManager",
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
        _BaseWorkloadManagerRestTransport._BaseListOperations, WorkloadManagerRestStub
    ):
        def __hash__(self):
            return hash("WorkloadManagerRestTransport.ListOperations")

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

            http_options = _BaseWorkloadManagerRestTransport._BaseListOperations._get_http_options()
            request, metadata = self._interceptor.pre_list_operations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseWorkloadManagerRestTransport._BaseListOperations,
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
                    f"Sending request for google.cloud.workloadmanager_v1.WorkloadManagerClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.workloadmanager.v1.WorkloadManager",
                        "rpcName": "ListOperations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = WorkloadManagerRestTransport._ListOperations._get_response(
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
                    "Received response for google.cloud.workloadmanager_v1.WorkloadManagerAsyncClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.workloadmanager.v1.WorkloadManager",
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


__all__ = ("WorkloadManagerRestTransport",)
