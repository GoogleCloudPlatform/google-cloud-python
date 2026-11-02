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

from google.cloud.ces_v1beta._compat import transcode_request
from google.cloud.ces_v1beta.types import evaluation, evaluation_service
from google.cloud.ces_v1beta.types import evaluation as gcc_evaluation

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseEvaluationServiceRestTransport

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


class EvaluationServiceRestInterceptor:
    """Interceptor for EvaluationService.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the EvaluationServiceRestTransport.

    .. code-block:: python
        class MyCustomEvaluationServiceInterceptor(EvaluationServiceRestInterceptor):
            def pre_create_evaluation(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_evaluation(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_evaluation_dataset(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_evaluation_dataset(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_evaluation_expectation(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_evaluation_expectation(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_scheduled_evaluation_run(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_scheduled_evaluation_run(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_evaluation(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_delete_evaluation_dataset(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_delete_evaluation_expectation(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_delete_evaluation_result(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_delete_evaluation_run(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_evaluation_run(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_scheduled_evaluation_run(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_export_evaluation_results(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_export_evaluation_results(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_export_evaluation_runs(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_export_evaluation_runs(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_export_evaluations(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_export_evaluations(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_generate_evaluation(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_generate_evaluation(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_evaluation(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_evaluation(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_evaluation_dataset(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_evaluation_dataset(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_evaluation_expectation(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_evaluation_expectation(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_evaluation_result(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_evaluation_result(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_evaluation_run(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_evaluation_run(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_scheduled_evaluation_run(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_scheduled_evaluation_run(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_import_evaluations(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_import_evaluations(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_evaluation_datasets(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_evaluation_datasets(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_evaluation_expectations(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_evaluation_expectations(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_evaluation_results(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_evaluation_results(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_evaluation_runs(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_evaluation_runs(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_evaluations(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_evaluations(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_scheduled_evaluation_runs(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_scheduled_evaluation_runs(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_run_evaluation(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_run_evaluation(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_run_evaluation_result_metrics(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_run_evaluation_result_metrics(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_test_persona_voice(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_test_persona_voice(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_evaluation(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_evaluation(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_evaluation_dataset(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_evaluation_dataset(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_evaluation_expectation(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_evaluation_expectation(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_scheduled_evaluation_run(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_scheduled_evaluation_run(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_upload_evaluation_audio(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_upload_evaluation_audio(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = EvaluationServiceRestTransport(interceptor=MyCustomEvaluationServiceInterceptor())
        client = EvaluationServiceClient(transport=transport)


    """

    def pre_create_evaluation(
        self,
        request: evaluation_service.CreateEvaluationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        evaluation_service.CreateEvaluationRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_evaluation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the EvaluationService server.
        """
        return request, metadata

    def post_create_evaluation(
        self, response: gcc_evaluation.Evaluation
    ) -> gcc_evaluation.Evaluation:
        """Post-rpc interceptor for create_evaluation

        DEPRECATED. Please use the `post_create_evaluation_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the EvaluationService server but before
        it is returned to user code. This `post_create_evaluation` interceptor runs
        before the `post_create_evaluation_with_metadata` interceptor.
        """
        return response

    def post_create_evaluation_with_metadata(
        self,
        response: gcc_evaluation.Evaluation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[gcc_evaluation.Evaluation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_evaluation

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the EvaluationService server but before it is returned to user code.

        We recommend only using this `post_create_evaluation_with_metadata`
        interceptor in new development instead of the `post_create_evaluation` interceptor.
        When both interceptors are used, this `post_create_evaluation_with_metadata` interceptor runs after the
        `post_create_evaluation` interceptor. The (possibly modified) response returned by
        `post_create_evaluation` will be passed to
        `post_create_evaluation_with_metadata`.
        """
        return response, metadata

    def pre_create_evaluation_dataset(
        self,
        request: evaluation_service.CreateEvaluationDatasetRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        evaluation_service.CreateEvaluationDatasetRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_evaluation_dataset

        Override in a subclass to manipulate the request or metadata
        before they are sent to the EvaluationService server.
        """
        return request, metadata

    def post_create_evaluation_dataset(
        self, response: evaluation.EvaluationDataset
    ) -> evaluation.EvaluationDataset:
        """Post-rpc interceptor for create_evaluation_dataset

        DEPRECATED. Please use the `post_create_evaluation_dataset_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the EvaluationService server but before
        it is returned to user code. This `post_create_evaluation_dataset` interceptor runs
        before the `post_create_evaluation_dataset_with_metadata` interceptor.
        """
        return response

    def post_create_evaluation_dataset_with_metadata(
        self,
        response: evaluation.EvaluationDataset,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[evaluation.EvaluationDataset, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_evaluation_dataset

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the EvaluationService server but before it is returned to user code.

        We recommend only using this `post_create_evaluation_dataset_with_metadata`
        interceptor in new development instead of the `post_create_evaluation_dataset` interceptor.
        When both interceptors are used, this `post_create_evaluation_dataset_with_metadata` interceptor runs after the
        `post_create_evaluation_dataset` interceptor. The (possibly modified) response returned by
        `post_create_evaluation_dataset` will be passed to
        `post_create_evaluation_dataset_with_metadata`.
        """
        return response, metadata

    def pre_create_evaluation_expectation(
        self,
        request: evaluation_service.CreateEvaluationExpectationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        evaluation_service.CreateEvaluationExpectationRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_evaluation_expectation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the EvaluationService server.
        """
        return request, metadata

    def post_create_evaluation_expectation(
        self, response: evaluation.EvaluationExpectation
    ) -> evaluation.EvaluationExpectation:
        """Post-rpc interceptor for create_evaluation_expectation

        DEPRECATED. Please use the `post_create_evaluation_expectation_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the EvaluationService server but before
        it is returned to user code. This `post_create_evaluation_expectation` interceptor runs
        before the `post_create_evaluation_expectation_with_metadata` interceptor.
        """
        return response

    def post_create_evaluation_expectation_with_metadata(
        self,
        response: evaluation.EvaluationExpectation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        evaluation.EvaluationExpectation, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for create_evaluation_expectation

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the EvaluationService server but before it is returned to user code.

        We recommend only using this `post_create_evaluation_expectation_with_metadata`
        interceptor in new development instead of the `post_create_evaluation_expectation` interceptor.
        When both interceptors are used, this `post_create_evaluation_expectation_with_metadata` interceptor runs after the
        `post_create_evaluation_expectation` interceptor. The (possibly modified) response returned by
        `post_create_evaluation_expectation` will be passed to
        `post_create_evaluation_expectation_with_metadata`.
        """
        return response, metadata

    def pre_create_scheduled_evaluation_run(
        self,
        request: evaluation_service.CreateScheduledEvaluationRunRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        evaluation_service.CreateScheduledEvaluationRunRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_scheduled_evaluation_run

        Override in a subclass to manipulate the request or metadata
        before they are sent to the EvaluationService server.
        """
        return request, metadata

    def post_create_scheduled_evaluation_run(
        self, response: evaluation.ScheduledEvaluationRun
    ) -> evaluation.ScheduledEvaluationRun:
        """Post-rpc interceptor for create_scheduled_evaluation_run

        DEPRECATED. Please use the `post_create_scheduled_evaluation_run_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the EvaluationService server but before
        it is returned to user code. This `post_create_scheduled_evaluation_run` interceptor runs
        before the `post_create_scheduled_evaluation_run_with_metadata` interceptor.
        """
        return response

    def post_create_scheduled_evaluation_run_with_metadata(
        self,
        response: evaluation.ScheduledEvaluationRun,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        evaluation.ScheduledEvaluationRun, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for create_scheduled_evaluation_run

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the EvaluationService server but before it is returned to user code.

        We recommend only using this `post_create_scheduled_evaluation_run_with_metadata`
        interceptor in new development instead of the `post_create_scheduled_evaluation_run` interceptor.
        When both interceptors are used, this `post_create_scheduled_evaluation_run_with_metadata` interceptor runs after the
        `post_create_scheduled_evaluation_run` interceptor. The (possibly modified) response returned by
        `post_create_scheduled_evaluation_run` will be passed to
        `post_create_scheduled_evaluation_run_with_metadata`.
        """
        return response, metadata

    def pre_delete_evaluation(
        self,
        request: evaluation_service.DeleteEvaluationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        evaluation_service.DeleteEvaluationRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_evaluation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the EvaluationService server.
        """
        return request, metadata

    def pre_delete_evaluation_dataset(
        self,
        request: evaluation_service.DeleteEvaluationDatasetRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        evaluation_service.DeleteEvaluationDatasetRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_evaluation_dataset

        Override in a subclass to manipulate the request or metadata
        before they are sent to the EvaluationService server.
        """
        return request, metadata

    def pre_delete_evaluation_expectation(
        self,
        request: evaluation_service.DeleteEvaluationExpectationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        evaluation_service.DeleteEvaluationExpectationRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_evaluation_expectation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the EvaluationService server.
        """
        return request, metadata

    def pre_delete_evaluation_result(
        self,
        request: evaluation_service.DeleteEvaluationResultRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        evaluation_service.DeleteEvaluationResultRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_evaluation_result

        Override in a subclass to manipulate the request or metadata
        before they are sent to the EvaluationService server.
        """
        return request, metadata

    def pre_delete_evaluation_run(
        self,
        request: evaluation_service.DeleteEvaluationRunRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        evaluation_service.DeleteEvaluationRunRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_evaluation_run

        Override in a subclass to manipulate the request or metadata
        before they are sent to the EvaluationService server.
        """
        return request, metadata

    def post_delete_evaluation_run(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_evaluation_run

        DEPRECATED. Please use the `post_delete_evaluation_run_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the EvaluationService server but before
        it is returned to user code. This `post_delete_evaluation_run` interceptor runs
        before the `post_delete_evaluation_run_with_metadata` interceptor.
        """
        return response

    def post_delete_evaluation_run_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_evaluation_run

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the EvaluationService server but before it is returned to user code.

        We recommend only using this `post_delete_evaluation_run_with_metadata`
        interceptor in new development instead of the `post_delete_evaluation_run` interceptor.
        When both interceptors are used, this `post_delete_evaluation_run_with_metadata` interceptor runs after the
        `post_delete_evaluation_run` interceptor. The (possibly modified) response returned by
        `post_delete_evaluation_run` will be passed to
        `post_delete_evaluation_run_with_metadata`.
        """
        return response, metadata

    def pre_delete_scheduled_evaluation_run(
        self,
        request: evaluation_service.DeleteScheduledEvaluationRunRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        evaluation_service.DeleteScheduledEvaluationRunRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_scheduled_evaluation_run

        Override in a subclass to manipulate the request or metadata
        before they are sent to the EvaluationService server.
        """
        return request, metadata

    def pre_export_evaluation_results(
        self,
        request: evaluation_service.ExportEvaluationResultsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        evaluation_service.ExportEvaluationResultsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for export_evaluation_results

        Override in a subclass to manipulate the request or metadata
        before they are sent to the EvaluationService server.
        """
        return request, metadata

    def post_export_evaluation_results(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for export_evaluation_results

        DEPRECATED. Please use the `post_export_evaluation_results_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the EvaluationService server but before
        it is returned to user code. This `post_export_evaluation_results` interceptor runs
        before the `post_export_evaluation_results_with_metadata` interceptor.
        """
        return response

    def post_export_evaluation_results_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for export_evaluation_results

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the EvaluationService server but before it is returned to user code.

        We recommend only using this `post_export_evaluation_results_with_metadata`
        interceptor in new development instead of the `post_export_evaluation_results` interceptor.
        When both interceptors are used, this `post_export_evaluation_results_with_metadata` interceptor runs after the
        `post_export_evaluation_results` interceptor. The (possibly modified) response returned by
        `post_export_evaluation_results` will be passed to
        `post_export_evaluation_results_with_metadata`.
        """
        return response, metadata

    def pre_export_evaluation_runs(
        self,
        request: evaluation_service.ExportEvaluationRunsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        evaluation_service.ExportEvaluationRunsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for export_evaluation_runs

        Override in a subclass to manipulate the request or metadata
        before they are sent to the EvaluationService server.
        """
        return request, metadata

    def post_export_evaluation_runs(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for export_evaluation_runs

        DEPRECATED. Please use the `post_export_evaluation_runs_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the EvaluationService server but before
        it is returned to user code. This `post_export_evaluation_runs` interceptor runs
        before the `post_export_evaluation_runs_with_metadata` interceptor.
        """
        return response

    def post_export_evaluation_runs_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for export_evaluation_runs

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the EvaluationService server but before it is returned to user code.

        We recommend only using this `post_export_evaluation_runs_with_metadata`
        interceptor in new development instead of the `post_export_evaluation_runs` interceptor.
        When both interceptors are used, this `post_export_evaluation_runs_with_metadata` interceptor runs after the
        `post_export_evaluation_runs` interceptor. The (possibly modified) response returned by
        `post_export_evaluation_runs` will be passed to
        `post_export_evaluation_runs_with_metadata`.
        """
        return response, metadata

    def pre_export_evaluations(
        self,
        request: evaluation_service.ExportEvaluationsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        evaluation_service.ExportEvaluationsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for export_evaluations

        Override in a subclass to manipulate the request or metadata
        before they are sent to the EvaluationService server.
        """
        return request, metadata

    def post_export_evaluations(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for export_evaluations

        DEPRECATED. Please use the `post_export_evaluations_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the EvaluationService server but before
        it is returned to user code. This `post_export_evaluations` interceptor runs
        before the `post_export_evaluations_with_metadata` interceptor.
        """
        return response

    def post_export_evaluations_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for export_evaluations

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the EvaluationService server but before it is returned to user code.

        We recommend only using this `post_export_evaluations_with_metadata`
        interceptor in new development instead of the `post_export_evaluations` interceptor.
        When both interceptors are used, this `post_export_evaluations_with_metadata` interceptor runs after the
        `post_export_evaluations` interceptor. The (possibly modified) response returned by
        `post_export_evaluations` will be passed to
        `post_export_evaluations_with_metadata`.
        """
        return response, metadata

    def pre_generate_evaluation(
        self,
        request: evaluation_service.GenerateEvaluationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        evaluation_service.GenerateEvaluationRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for generate_evaluation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the EvaluationService server.
        """
        return request, metadata

    def post_generate_evaluation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for generate_evaluation

        DEPRECATED. Please use the `post_generate_evaluation_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the EvaluationService server but before
        it is returned to user code. This `post_generate_evaluation` interceptor runs
        before the `post_generate_evaluation_with_metadata` interceptor.
        """
        return response

    def post_generate_evaluation_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for generate_evaluation

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the EvaluationService server but before it is returned to user code.

        We recommend only using this `post_generate_evaluation_with_metadata`
        interceptor in new development instead of the `post_generate_evaluation` interceptor.
        When both interceptors are used, this `post_generate_evaluation_with_metadata` interceptor runs after the
        `post_generate_evaluation` interceptor. The (possibly modified) response returned by
        `post_generate_evaluation` will be passed to
        `post_generate_evaluation_with_metadata`.
        """
        return response, metadata

    def pre_get_evaluation(
        self,
        request: evaluation_service.GetEvaluationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        evaluation_service.GetEvaluationRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_evaluation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the EvaluationService server.
        """
        return request, metadata

    def post_get_evaluation(
        self, response: evaluation.Evaluation
    ) -> evaluation.Evaluation:
        """Post-rpc interceptor for get_evaluation

        DEPRECATED. Please use the `post_get_evaluation_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the EvaluationService server but before
        it is returned to user code. This `post_get_evaluation` interceptor runs
        before the `post_get_evaluation_with_metadata` interceptor.
        """
        return response

    def post_get_evaluation_with_metadata(
        self,
        response: evaluation.Evaluation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[evaluation.Evaluation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_evaluation

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the EvaluationService server but before it is returned to user code.

        We recommend only using this `post_get_evaluation_with_metadata`
        interceptor in new development instead of the `post_get_evaluation` interceptor.
        When both interceptors are used, this `post_get_evaluation_with_metadata` interceptor runs after the
        `post_get_evaluation` interceptor. The (possibly modified) response returned by
        `post_get_evaluation` will be passed to
        `post_get_evaluation_with_metadata`.
        """
        return response, metadata

    def pre_get_evaluation_dataset(
        self,
        request: evaluation_service.GetEvaluationDatasetRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        evaluation_service.GetEvaluationDatasetRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_evaluation_dataset

        Override in a subclass to manipulate the request or metadata
        before they are sent to the EvaluationService server.
        """
        return request, metadata

    def post_get_evaluation_dataset(
        self, response: evaluation.EvaluationDataset
    ) -> evaluation.EvaluationDataset:
        """Post-rpc interceptor for get_evaluation_dataset

        DEPRECATED. Please use the `post_get_evaluation_dataset_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the EvaluationService server but before
        it is returned to user code. This `post_get_evaluation_dataset` interceptor runs
        before the `post_get_evaluation_dataset_with_metadata` interceptor.
        """
        return response

    def post_get_evaluation_dataset_with_metadata(
        self,
        response: evaluation.EvaluationDataset,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[evaluation.EvaluationDataset, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_evaluation_dataset

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the EvaluationService server but before it is returned to user code.

        We recommend only using this `post_get_evaluation_dataset_with_metadata`
        interceptor in new development instead of the `post_get_evaluation_dataset` interceptor.
        When both interceptors are used, this `post_get_evaluation_dataset_with_metadata` interceptor runs after the
        `post_get_evaluation_dataset` interceptor. The (possibly modified) response returned by
        `post_get_evaluation_dataset` will be passed to
        `post_get_evaluation_dataset_with_metadata`.
        """
        return response, metadata

    def pre_get_evaluation_expectation(
        self,
        request: evaluation_service.GetEvaluationExpectationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        evaluation_service.GetEvaluationExpectationRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_evaluation_expectation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the EvaluationService server.
        """
        return request, metadata

    def post_get_evaluation_expectation(
        self, response: evaluation.EvaluationExpectation
    ) -> evaluation.EvaluationExpectation:
        """Post-rpc interceptor for get_evaluation_expectation

        DEPRECATED. Please use the `post_get_evaluation_expectation_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the EvaluationService server but before
        it is returned to user code. This `post_get_evaluation_expectation` interceptor runs
        before the `post_get_evaluation_expectation_with_metadata` interceptor.
        """
        return response

    def post_get_evaluation_expectation_with_metadata(
        self,
        response: evaluation.EvaluationExpectation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        evaluation.EvaluationExpectation, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for get_evaluation_expectation

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the EvaluationService server but before it is returned to user code.

        We recommend only using this `post_get_evaluation_expectation_with_metadata`
        interceptor in new development instead of the `post_get_evaluation_expectation` interceptor.
        When both interceptors are used, this `post_get_evaluation_expectation_with_metadata` interceptor runs after the
        `post_get_evaluation_expectation` interceptor. The (possibly modified) response returned by
        `post_get_evaluation_expectation` will be passed to
        `post_get_evaluation_expectation_with_metadata`.
        """
        return response, metadata

    def pre_get_evaluation_result(
        self,
        request: evaluation_service.GetEvaluationResultRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        evaluation_service.GetEvaluationResultRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_evaluation_result

        Override in a subclass to manipulate the request or metadata
        before they are sent to the EvaluationService server.
        """
        return request, metadata

    def post_get_evaluation_result(
        self, response: evaluation.EvaluationResult
    ) -> evaluation.EvaluationResult:
        """Post-rpc interceptor for get_evaluation_result

        DEPRECATED. Please use the `post_get_evaluation_result_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the EvaluationService server but before
        it is returned to user code. This `post_get_evaluation_result` interceptor runs
        before the `post_get_evaluation_result_with_metadata` interceptor.
        """
        return response

    def post_get_evaluation_result_with_metadata(
        self,
        response: evaluation.EvaluationResult,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[evaluation.EvaluationResult, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_evaluation_result

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the EvaluationService server but before it is returned to user code.

        We recommend only using this `post_get_evaluation_result_with_metadata`
        interceptor in new development instead of the `post_get_evaluation_result` interceptor.
        When both interceptors are used, this `post_get_evaluation_result_with_metadata` interceptor runs after the
        `post_get_evaluation_result` interceptor. The (possibly modified) response returned by
        `post_get_evaluation_result` will be passed to
        `post_get_evaluation_result_with_metadata`.
        """
        return response, metadata

    def pre_get_evaluation_run(
        self,
        request: evaluation_service.GetEvaluationRunRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        evaluation_service.GetEvaluationRunRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_evaluation_run

        Override in a subclass to manipulate the request or metadata
        before they are sent to the EvaluationService server.
        """
        return request, metadata

    def post_get_evaluation_run(
        self, response: evaluation.EvaluationRun
    ) -> evaluation.EvaluationRun:
        """Post-rpc interceptor for get_evaluation_run

        DEPRECATED. Please use the `post_get_evaluation_run_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the EvaluationService server but before
        it is returned to user code. This `post_get_evaluation_run` interceptor runs
        before the `post_get_evaluation_run_with_metadata` interceptor.
        """
        return response

    def post_get_evaluation_run_with_metadata(
        self,
        response: evaluation.EvaluationRun,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[evaluation.EvaluationRun, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_evaluation_run

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the EvaluationService server but before it is returned to user code.

        We recommend only using this `post_get_evaluation_run_with_metadata`
        interceptor in new development instead of the `post_get_evaluation_run` interceptor.
        When both interceptors are used, this `post_get_evaluation_run_with_metadata` interceptor runs after the
        `post_get_evaluation_run` interceptor. The (possibly modified) response returned by
        `post_get_evaluation_run` will be passed to
        `post_get_evaluation_run_with_metadata`.
        """
        return response, metadata

    def pre_get_scheduled_evaluation_run(
        self,
        request: evaluation_service.GetScheduledEvaluationRunRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        evaluation_service.GetScheduledEvaluationRunRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_scheduled_evaluation_run

        Override in a subclass to manipulate the request or metadata
        before they are sent to the EvaluationService server.
        """
        return request, metadata

    def post_get_scheduled_evaluation_run(
        self, response: evaluation.ScheduledEvaluationRun
    ) -> evaluation.ScheduledEvaluationRun:
        """Post-rpc interceptor for get_scheduled_evaluation_run

        DEPRECATED. Please use the `post_get_scheduled_evaluation_run_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the EvaluationService server but before
        it is returned to user code. This `post_get_scheduled_evaluation_run` interceptor runs
        before the `post_get_scheduled_evaluation_run_with_metadata` interceptor.
        """
        return response

    def post_get_scheduled_evaluation_run_with_metadata(
        self,
        response: evaluation.ScheduledEvaluationRun,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        evaluation.ScheduledEvaluationRun, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for get_scheduled_evaluation_run

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the EvaluationService server but before it is returned to user code.

        We recommend only using this `post_get_scheduled_evaluation_run_with_metadata`
        interceptor in new development instead of the `post_get_scheduled_evaluation_run` interceptor.
        When both interceptors are used, this `post_get_scheduled_evaluation_run_with_metadata` interceptor runs after the
        `post_get_scheduled_evaluation_run` interceptor. The (possibly modified) response returned by
        `post_get_scheduled_evaluation_run` will be passed to
        `post_get_scheduled_evaluation_run_with_metadata`.
        """
        return response, metadata

    def pre_import_evaluations(
        self,
        request: evaluation_service.ImportEvaluationsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        evaluation_service.ImportEvaluationsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for import_evaluations

        Override in a subclass to manipulate the request or metadata
        before they are sent to the EvaluationService server.
        """
        return request, metadata

    def post_import_evaluations(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for import_evaluations

        DEPRECATED. Please use the `post_import_evaluations_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the EvaluationService server but before
        it is returned to user code. This `post_import_evaluations` interceptor runs
        before the `post_import_evaluations_with_metadata` interceptor.
        """
        return response

    def post_import_evaluations_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for import_evaluations

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the EvaluationService server but before it is returned to user code.

        We recommend only using this `post_import_evaluations_with_metadata`
        interceptor in new development instead of the `post_import_evaluations` interceptor.
        When both interceptors are used, this `post_import_evaluations_with_metadata` interceptor runs after the
        `post_import_evaluations` interceptor. The (possibly modified) response returned by
        `post_import_evaluations` will be passed to
        `post_import_evaluations_with_metadata`.
        """
        return response, metadata

    def pre_list_evaluation_datasets(
        self,
        request: evaluation_service.ListEvaluationDatasetsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        evaluation_service.ListEvaluationDatasetsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_evaluation_datasets

        Override in a subclass to manipulate the request or metadata
        before they are sent to the EvaluationService server.
        """
        return request, metadata

    def post_list_evaluation_datasets(
        self, response: evaluation_service.ListEvaluationDatasetsResponse
    ) -> evaluation_service.ListEvaluationDatasetsResponse:
        """Post-rpc interceptor for list_evaluation_datasets

        DEPRECATED. Please use the `post_list_evaluation_datasets_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the EvaluationService server but before
        it is returned to user code. This `post_list_evaluation_datasets` interceptor runs
        before the `post_list_evaluation_datasets_with_metadata` interceptor.
        """
        return response

    def post_list_evaluation_datasets_with_metadata(
        self,
        response: evaluation_service.ListEvaluationDatasetsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        evaluation_service.ListEvaluationDatasetsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_evaluation_datasets

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the EvaluationService server but before it is returned to user code.

        We recommend only using this `post_list_evaluation_datasets_with_metadata`
        interceptor in new development instead of the `post_list_evaluation_datasets` interceptor.
        When both interceptors are used, this `post_list_evaluation_datasets_with_metadata` interceptor runs after the
        `post_list_evaluation_datasets` interceptor. The (possibly modified) response returned by
        `post_list_evaluation_datasets` will be passed to
        `post_list_evaluation_datasets_with_metadata`.
        """
        return response, metadata

    def pre_list_evaluation_expectations(
        self,
        request: evaluation_service.ListEvaluationExpectationsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        evaluation_service.ListEvaluationExpectationsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_evaluation_expectations

        Override in a subclass to manipulate the request or metadata
        before they are sent to the EvaluationService server.
        """
        return request, metadata

    def post_list_evaluation_expectations(
        self, response: evaluation_service.ListEvaluationExpectationsResponse
    ) -> evaluation_service.ListEvaluationExpectationsResponse:
        """Post-rpc interceptor for list_evaluation_expectations

        DEPRECATED. Please use the `post_list_evaluation_expectations_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the EvaluationService server but before
        it is returned to user code. This `post_list_evaluation_expectations` interceptor runs
        before the `post_list_evaluation_expectations_with_metadata` interceptor.
        """
        return response

    def post_list_evaluation_expectations_with_metadata(
        self,
        response: evaluation_service.ListEvaluationExpectationsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        evaluation_service.ListEvaluationExpectationsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_evaluation_expectations

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the EvaluationService server but before it is returned to user code.

        We recommend only using this `post_list_evaluation_expectations_with_metadata`
        interceptor in new development instead of the `post_list_evaluation_expectations` interceptor.
        When both interceptors are used, this `post_list_evaluation_expectations_with_metadata` interceptor runs after the
        `post_list_evaluation_expectations` interceptor. The (possibly modified) response returned by
        `post_list_evaluation_expectations` will be passed to
        `post_list_evaluation_expectations_with_metadata`.
        """
        return response, metadata

    def pre_list_evaluation_results(
        self,
        request: evaluation_service.ListEvaluationResultsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        evaluation_service.ListEvaluationResultsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_evaluation_results

        Override in a subclass to manipulate the request or metadata
        before they are sent to the EvaluationService server.
        """
        return request, metadata

    def post_list_evaluation_results(
        self, response: evaluation_service.ListEvaluationResultsResponse
    ) -> evaluation_service.ListEvaluationResultsResponse:
        """Post-rpc interceptor for list_evaluation_results

        DEPRECATED. Please use the `post_list_evaluation_results_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the EvaluationService server but before
        it is returned to user code. This `post_list_evaluation_results` interceptor runs
        before the `post_list_evaluation_results_with_metadata` interceptor.
        """
        return response

    def post_list_evaluation_results_with_metadata(
        self,
        response: evaluation_service.ListEvaluationResultsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        evaluation_service.ListEvaluationResultsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_evaluation_results

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the EvaluationService server but before it is returned to user code.

        We recommend only using this `post_list_evaluation_results_with_metadata`
        interceptor in new development instead of the `post_list_evaluation_results` interceptor.
        When both interceptors are used, this `post_list_evaluation_results_with_metadata` interceptor runs after the
        `post_list_evaluation_results` interceptor. The (possibly modified) response returned by
        `post_list_evaluation_results` will be passed to
        `post_list_evaluation_results_with_metadata`.
        """
        return response, metadata

    def pre_list_evaluation_runs(
        self,
        request: evaluation_service.ListEvaluationRunsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        evaluation_service.ListEvaluationRunsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_evaluation_runs

        Override in a subclass to manipulate the request or metadata
        before they are sent to the EvaluationService server.
        """
        return request, metadata

    def post_list_evaluation_runs(
        self, response: evaluation_service.ListEvaluationRunsResponse
    ) -> evaluation_service.ListEvaluationRunsResponse:
        """Post-rpc interceptor for list_evaluation_runs

        DEPRECATED. Please use the `post_list_evaluation_runs_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the EvaluationService server but before
        it is returned to user code. This `post_list_evaluation_runs` interceptor runs
        before the `post_list_evaluation_runs_with_metadata` interceptor.
        """
        return response

    def post_list_evaluation_runs_with_metadata(
        self,
        response: evaluation_service.ListEvaluationRunsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        evaluation_service.ListEvaluationRunsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_evaluation_runs

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the EvaluationService server but before it is returned to user code.

        We recommend only using this `post_list_evaluation_runs_with_metadata`
        interceptor in new development instead of the `post_list_evaluation_runs` interceptor.
        When both interceptors are used, this `post_list_evaluation_runs_with_metadata` interceptor runs after the
        `post_list_evaluation_runs` interceptor. The (possibly modified) response returned by
        `post_list_evaluation_runs` will be passed to
        `post_list_evaluation_runs_with_metadata`.
        """
        return response, metadata

    def pre_list_evaluations(
        self,
        request: evaluation_service.ListEvaluationsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        evaluation_service.ListEvaluationsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_evaluations

        Override in a subclass to manipulate the request or metadata
        before they are sent to the EvaluationService server.
        """
        return request, metadata

    def post_list_evaluations(
        self, response: evaluation_service.ListEvaluationsResponse
    ) -> evaluation_service.ListEvaluationsResponse:
        """Post-rpc interceptor for list_evaluations

        DEPRECATED. Please use the `post_list_evaluations_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the EvaluationService server but before
        it is returned to user code. This `post_list_evaluations` interceptor runs
        before the `post_list_evaluations_with_metadata` interceptor.
        """
        return response

    def post_list_evaluations_with_metadata(
        self,
        response: evaluation_service.ListEvaluationsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        evaluation_service.ListEvaluationsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_evaluations

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the EvaluationService server but before it is returned to user code.

        We recommend only using this `post_list_evaluations_with_metadata`
        interceptor in new development instead of the `post_list_evaluations` interceptor.
        When both interceptors are used, this `post_list_evaluations_with_metadata` interceptor runs after the
        `post_list_evaluations` interceptor. The (possibly modified) response returned by
        `post_list_evaluations` will be passed to
        `post_list_evaluations_with_metadata`.
        """
        return response, metadata

    def pre_list_scheduled_evaluation_runs(
        self,
        request: evaluation_service.ListScheduledEvaluationRunsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        evaluation_service.ListScheduledEvaluationRunsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_scheduled_evaluation_runs

        Override in a subclass to manipulate the request or metadata
        before they are sent to the EvaluationService server.
        """
        return request, metadata

    def post_list_scheduled_evaluation_runs(
        self, response: evaluation_service.ListScheduledEvaluationRunsResponse
    ) -> evaluation_service.ListScheduledEvaluationRunsResponse:
        """Post-rpc interceptor for list_scheduled_evaluation_runs

        DEPRECATED. Please use the `post_list_scheduled_evaluation_runs_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the EvaluationService server but before
        it is returned to user code. This `post_list_scheduled_evaluation_runs` interceptor runs
        before the `post_list_scheduled_evaluation_runs_with_metadata` interceptor.
        """
        return response

    def post_list_scheduled_evaluation_runs_with_metadata(
        self,
        response: evaluation_service.ListScheduledEvaluationRunsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        evaluation_service.ListScheduledEvaluationRunsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_scheduled_evaluation_runs

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the EvaluationService server but before it is returned to user code.

        We recommend only using this `post_list_scheduled_evaluation_runs_with_metadata`
        interceptor in new development instead of the `post_list_scheduled_evaluation_runs` interceptor.
        When both interceptors are used, this `post_list_scheduled_evaluation_runs_with_metadata` interceptor runs after the
        `post_list_scheduled_evaluation_runs` interceptor. The (possibly modified) response returned by
        `post_list_scheduled_evaluation_runs` will be passed to
        `post_list_scheduled_evaluation_runs_with_metadata`.
        """
        return response, metadata

    def pre_run_evaluation(
        self,
        request: evaluation.RunEvaluationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        evaluation.RunEvaluationRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for run_evaluation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the EvaluationService server.
        """
        return request, metadata

    def post_run_evaluation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for run_evaluation

        DEPRECATED. Please use the `post_run_evaluation_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the EvaluationService server but before
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
        is returned by the EvaluationService server but before it is returned to user code.

        We recommend only using this `post_run_evaluation_with_metadata`
        interceptor in new development instead of the `post_run_evaluation` interceptor.
        When both interceptors are used, this `post_run_evaluation_with_metadata` interceptor runs after the
        `post_run_evaluation` interceptor. The (possibly modified) response returned by
        `post_run_evaluation` will be passed to
        `post_run_evaluation_with_metadata`.
        """
        return response, metadata

    def pre_run_evaluation_result_metrics(
        self,
        request: evaluation_service.RunEvaluationResultMetricsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        evaluation_service.RunEvaluationResultMetricsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for run_evaluation_result_metrics

        Override in a subclass to manipulate the request or metadata
        before they are sent to the EvaluationService server.
        """
        return request, metadata

    def post_run_evaluation_result_metrics(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for run_evaluation_result_metrics

        DEPRECATED. Please use the `post_run_evaluation_result_metrics_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the EvaluationService server but before
        it is returned to user code. This `post_run_evaluation_result_metrics` interceptor runs
        before the `post_run_evaluation_result_metrics_with_metadata` interceptor.
        """
        return response

    def post_run_evaluation_result_metrics_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for run_evaluation_result_metrics

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the EvaluationService server but before it is returned to user code.

        We recommend only using this `post_run_evaluation_result_metrics_with_metadata`
        interceptor in new development instead of the `post_run_evaluation_result_metrics` interceptor.
        When both interceptors are used, this `post_run_evaluation_result_metrics_with_metadata` interceptor runs after the
        `post_run_evaluation_result_metrics` interceptor. The (possibly modified) response returned by
        `post_run_evaluation_result_metrics` will be passed to
        `post_run_evaluation_result_metrics_with_metadata`.
        """
        return response, metadata

    def pre_test_persona_voice(
        self,
        request: evaluation_service.TestPersonaVoiceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        evaluation_service.TestPersonaVoiceRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for test_persona_voice

        Override in a subclass to manipulate the request or metadata
        before they are sent to the EvaluationService server.
        """
        return request, metadata

    def post_test_persona_voice(
        self, response: evaluation_service.TestPersonaVoiceResponse
    ) -> evaluation_service.TestPersonaVoiceResponse:
        """Post-rpc interceptor for test_persona_voice

        DEPRECATED. Please use the `post_test_persona_voice_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the EvaluationService server but before
        it is returned to user code. This `post_test_persona_voice` interceptor runs
        before the `post_test_persona_voice_with_metadata` interceptor.
        """
        return response

    def post_test_persona_voice_with_metadata(
        self,
        response: evaluation_service.TestPersonaVoiceResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        evaluation_service.TestPersonaVoiceResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for test_persona_voice

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the EvaluationService server but before it is returned to user code.

        We recommend only using this `post_test_persona_voice_with_metadata`
        interceptor in new development instead of the `post_test_persona_voice` interceptor.
        When both interceptors are used, this `post_test_persona_voice_with_metadata` interceptor runs after the
        `post_test_persona_voice` interceptor. The (possibly modified) response returned by
        `post_test_persona_voice` will be passed to
        `post_test_persona_voice_with_metadata`.
        """
        return response, metadata

    def pre_update_evaluation(
        self,
        request: evaluation_service.UpdateEvaluationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        evaluation_service.UpdateEvaluationRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_evaluation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the EvaluationService server.
        """
        return request, metadata

    def post_update_evaluation(
        self, response: gcc_evaluation.Evaluation
    ) -> gcc_evaluation.Evaluation:
        """Post-rpc interceptor for update_evaluation

        DEPRECATED. Please use the `post_update_evaluation_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the EvaluationService server but before
        it is returned to user code. This `post_update_evaluation` interceptor runs
        before the `post_update_evaluation_with_metadata` interceptor.
        """
        return response

    def post_update_evaluation_with_metadata(
        self,
        response: gcc_evaluation.Evaluation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[gcc_evaluation.Evaluation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_evaluation

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the EvaluationService server but before it is returned to user code.

        We recommend only using this `post_update_evaluation_with_metadata`
        interceptor in new development instead of the `post_update_evaluation` interceptor.
        When both interceptors are used, this `post_update_evaluation_with_metadata` interceptor runs after the
        `post_update_evaluation` interceptor. The (possibly modified) response returned by
        `post_update_evaluation` will be passed to
        `post_update_evaluation_with_metadata`.
        """
        return response, metadata

    def pre_update_evaluation_dataset(
        self,
        request: evaluation_service.UpdateEvaluationDatasetRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        evaluation_service.UpdateEvaluationDatasetRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_evaluation_dataset

        Override in a subclass to manipulate the request or metadata
        before they are sent to the EvaluationService server.
        """
        return request, metadata

    def post_update_evaluation_dataset(
        self, response: evaluation.EvaluationDataset
    ) -> evaluation.EvaluationDataset:
        """Post-rpc interceptor for update_evaluation_dataset

        DEPRECATED. Please use the `post_update_evaluation_dataset_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the EvaluationService server but before
        it is returned to user code. This `post_update_evaluation_dataset` interceptor runs
        before the `post_update_evaluation_dataset_with_metadata` interceptor.
        """
        return response

    def post_update_evaluation_dataset_with_metadata(
        self,
        response: evaluation.EvaluationDataset,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[evaluation.EvaluationDataset, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_evaluation_dataset

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the EvaluationService server but before it is returned to user code.

        We recommend only using this `post_update_evaluation_dataset_with_metadata`
        interceptor in new development instead of the `post_update_evaluation_dataset` interceptor.
        When both interceptors are used, this `post_update_evaluation_dataset_with_metadata` interceptor runs after the
        `post_update_evaluation_dataset` interceptor. The (possibly modified) response returned by
        `post_update_evaluation_dataset` will be passed to
        `post_update_evaluation_dataset_with_metadata`.
        """
        return response, metadata

    def pre_update_evaluation_expectation(
        self,
        request: evaluation_service.UpdateEvaluationExpectationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        evaluation_service.UpdateEvaluationExpectationRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_evaluation_expectation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the EvaluationService server.
        """
        return request, metadata

    def post_update_evaluation_expectation(
        self, response: evaluation.EvaluationExpectation
    ) -> evaluation.EvaluationExpectation:
        """Post-rpc interceptor for update_evaluation_expectation

        DEPRECATED. Please use the `post_update_evaluation_expectation_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the EvaluationService server but before
        it is returned to user code. This `post_update_evaluation_expectation` interceptor runs
        before the `post_update_evaluation_expectation_with_metadata` interceptor.
        """
        return response

    def post_update_evaluation_expectation_with_metadata(
        self,
        response: evaluation.EvaluationExpectation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        evaluation.EvaluationExpectation, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for update_evaluation_expectation

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the EvaluationService server but before it is returned to user code.

        We recommend only using this `post_update_evaluation_expectation_with_metadata`
        interceptor in new development instead of the `post_update_evaluation_expectation` interceptor.
        When both interceptors are used, this `post_update_evaluation_expectation_with_metadata` interceptor runs after the
        `post_update_evaluation_expectation` interceptor. The (possibly modified) response returned by
        `post_update_evaluation_expectation` will be passed to
        `post_update_evaluation_expectation_with_metadata`.
        """
        return response, metadata

    def pre_update_scheduled_evaluation_run(
        self,
        request: evaluation_service.UpdateScheduledEvaluationRunRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        evaluation_service.UpdateScheduledEvaluationRunRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_scheduled_evaluation_run

        Override in a subclass to manipulate the request or metadata
        before they are sent to the EvaluationService server.
        """
        return request, metadata

    def post_update_scheduled_evaluation_run(
        self, response: evaluation.ScheduledEvaluationRun
    ) -> evaluation.ScheduledEvaluationRun:
        """Post-rpc interceptor for update_scheduled_evaluation_run

        DEPRECATED. Please use the `post_update_scheduled_evaluation_run_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the EvaluationService server but before
        it is returned to user code. This `post_update_scheduled_evaluation_run` interceptor runs
        before the `post_update_scheduled_evaluation_run_with_metadata` interceptor.
        """
        return response

    def post_update_scheduled_evaluation_run_with_metadata(
        self,
        response: evaluation.ScheduledEvaluationRun,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        evaluation.ScheduledEvaluationRun, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for update_scheduled_evaluation_run

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the EvaluationService server but before it is returned to user code.

        We recommend only using this `post_update_scheduled_evaluation_run_with_metadata`
        interceptor in new development instead of the `post_update_scheduled_evaluation_run` interceptor.
        When both interceptors are used, this `post_update_scheduled_evaluation_run_with_metadata` interceptor runs after the
        `post_update_scheduled_evaluation_run` interceptor. The (possibly modified) response returned by
        `post_update_scheduled_evaluation_run` will be passed to
        `post_update_scheduled_evaluation_run_with_metadata`.
        """
        return response, metadata

    def pre_upload_evaluation_audio(
        self,
        request: evaluation_service.UploadEvaluationAudioRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        evaluation_service.UploadEvaluationAudioRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for upload_evaluation_audio

        Override in a subclass to manipulate the request or metadata
        before they are sent to the EvaluationService server.
        """
        return request, metadata

    def post_upload_evaluation_audio(
        self, response: evaluation_service.UploadEvaluationAudioResponse
    ) -> evaluation_service.UploadEvaluationAudioResponse:
        """Post-rpc interceptor for upload_evaluation_audio

        DEPRECATED. Please use the `post_upload_evaluation_audio_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the EvaluationService server but before
        it is returned to user code. This `post_upload_evaluation_audio` interceptor runs
        before the `post_upload_evaluation_audio_with_metadata` interceptor.
        """
        return response

    def post_upload_evaluation_audio_with_metadata(
        self,
        response: evaluation_service.UploadEvaluationAudioResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        evaluation_service.UploadEvaluationAudioResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for upload_evaluation_audio

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the EvaluationService server but before it is returned to user code.

        We recommend only using this `post_upload_evaluation_audio_with_metadata`
        interceptor in new development instead of the `post_upload_evaluation_audio` interceptor.
        When both interceptors are used, this `post_upload_evaluation_audio_with_metadata` interceptor runs after the
        `post_upload_evaluation_audio` interceptor. The (possibly modified) response returned by
        `post_upload_evaluation_audio` will be passed to
        `post_upload_evaluation_audio_with_metadata`.
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
        before they are sent to the EvaluationService server.
        """
        return request, metadata

    def post_get_location(
        self, response: locations_pb2.Location
    ) -> locations_pb2.Location:
        """Post-rpc interceptor for get_location

        Override in a subclass to manipulate the response
        after it is returned by the EvaluationService server but before
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
        before they are sent to the EvaluationService server.
        """
        return request, metadata

    def post_list_locations(
        self, response: locations_pb2.ListLocationsResponse
    ) -> locations_pb2.ListLocationsResponse:
        """Post-rpc interceptor for list_locations

        Override in a subclass to manipulate the response
        after it is returned by the EvaluationService server but before
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
        before they are sent to the EvaluationService server.
        """
        return request, metadata

    def post_cancel_operation(self, response: None) -> None:
        """Post-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the response
        after it is returned by the EvaluationService server but before
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
        before they are sent to the EvaluationService server.
        """
        return request, metadata

    def post_delete_operation(self, response: None) -> None:
        """Post-rpc interceptor for delete_operation

        Override in a subclass to manipulate the response
        after it is returned by the EvaluationService server but before
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
        before they are sent to the EvaluationService server.
        """
        return request, metadata

    def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the EvaluationService server but before
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
        before they are sent to the EvaluationService server.
        """
        return request, metadata

    def post_list_operations(
        self, response: operations_pb2.ListOperationsResponse
    ) -> operations_pb2.ListOperationsResponse:
        """Post-rpc interceptor for list_operations

        Override in a subclass to manipulate the response
        after it is returned by the EvaluationService server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class EvaluationServiceRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: EvaluationServiceRestInterceptor


class EvaluationServiceRestTransport(_BaseEvaluationServiceRestTransport):
    """REST backend synchronous transport for EvaluationService.

    EvaluationService exposes methods to perform evaluation for
    the CES app.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "ces.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[EvaluationServiceRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'ces.googleapis.com').
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
            interceptor (Optional[EvaluationServiceRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or EvaluationServiceRestInterceptor()
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
                        "uri": "/v1beta/{name=projects/*/locations/*/operations/*}:cancel",
                        "body": "*",
                    },
                ],
                "google.longrunning.Operations.DeleteOperation": [
                    {
                        "method": "delete",
                        "uri": "/v1beta/{name=projects/*/locations/*/operations/*}",
                    },
                ],
                "google.longrunning.Operations.GetOperation": [
                    {
                        "method": "get",
                        "uri": "/v1beta/{name=projects/*/locations/*/operations/*}",
                    },
                ],
                "google.longrunning.Operations.ListOperations": [
                    {
                        "method": "get",
                        "uri": "/v1beta/{name=projects/*/locations/*}/operations",
                    },
                ],
            }

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

    class _CreateEvaluation(
        _BaseEvaluationServiceRestTransport._BaseCreateEvaluation,
        EvaluationServiceRestStub,
    ):
        def __hash__(self):
            return hash("EvaluationServiceRestTransport.CreateEvaluation")

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
            request: evaluation_service.CreateEvaluationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gcc_evaluation.Evaluation:
            r"""Call the create evaluation method over HTTP.

            Args:
                request (~.evaluation_service.CreateEvaluationRequest):
                    The request object. Request message for
                [EvaluationService.CreateEvaluation][google.cloud.ces.v1beta.EvaluationService.CreateEvaluation].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.gcc_evaluation.Evaluation:
                    An evaluation represents all of the
                information needed to simulate and
                evaluate an agent.

            """

            http_options = _BaseEvaluationServiceRestTransport._BaseCreateEvaluation._get_http_options()
            request, metadata = self._interceptor.pre_create_evaluation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEvaluationServiceRestTransport._BaseCreateEvaluation,
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
                    f"Sending request for google.cloud.ces_v1beta.EvaluationServiceClient.CreateEvaluation",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.EvaluationService",
                        "rpcName": "CreateEvaluation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = EvaluationServiceRestTransport._CreateEvaluation._get_response(
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
            resp = gcc_evaluation.Evaluation()
            pb_resp = gcc_evaluation.Evaluation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_evaluation(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_evaluation_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = gcc_evaluation.Evaluation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.ces_v1beta.EvaluationServiceClient.create_evaluation",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.EvaluationService",
                        "rpcName": "CreateEvaluation",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateEvaluationDataset(
        _BaseEvaluationServiceRestTransport._BaseCreateEvaluationDataset,
        EvaluationServiceRestStub,
    ):
        def __hash__(self):
            return hash("EvaluationServiceRestTransport.CreateEvaluationDataset")

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
            request: evaluation_service.CreateEvaluationDatasetRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> evaluation.EvaluationDataset:
            r"""Call the create evaluation dataset method over HTTP.

            Args:
                request (~.evaluation_service.CreateEvaluationDatasetRequest):
                    The request object. Request message for
                [EvaluationService.CreateEvaluationDataset][google.cloud.ces.v1beta.EvaluationService.CreateEvaluationDataset].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.evaluation.EvaluationDataset:
                    An evaluation dataset represents a
                set of evaluations that are grouped
                together basaed on shared tags.

            """

            http_options = _BaseEvaluationServiceRestTransport._BaseCreateEvaluationDataset._get_http_options()
            request, metadata = self._interceptor.pre_create_evaluation_dataset(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEvaluationServiceRestTransport._BaseCreateEvaluationDataset,
                    "_BaseCreateEvaluationDataset__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.ces_v1beta.EvaluationServiceClient.CreateEvaluationDataset",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.EvaluationService",
                        "rpcName": "CreateEvaluationDataset",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                EvaluationServiceRestTransport._CreateEvaluationDataset._get_response(
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
            resp = evaluation.EvaluationDataset()
            pb_resp = evaluation.EvaluationDataset.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_evaluation_dataset(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_evaluation_dataset_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = evaluation.EvaluationDataset.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.ces_v1beta.EvaluationServiceClient.create_evaluation_dataset",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.EvaluationService",
                        "rpcName": "CreateEvaluationDataset",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateEvaluationExpectation(
        _BaseEvaluationServiceRestTransport._BaseCreateEvaluationExpectation,
        EvaluationServiceRestStub,
    ):
        def __hash__(self):
            return hash("EvaluationServiceRestTransport.CreateEvaluationExpectation")

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
            request: evaluation_service.CreateEvaluationExpectationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> evaluation.EvaluationExpectation:
            r"""Call the create evaluation
            expectation method over HTTP.

                Args:
                    request (~.evaluation_service.CreateEvaluationExpectationRequest):
                        The request object. Request message for
                    [EvaluationService.CreateEvaluationExpectation][google.cloud.ces.v1beta.EvaluationService.CreateEvaluationExpectation].
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.evaluation.EvaluationExpectation:
                        An evaluation expectation represents
                    a specific criteria to evaluate against.

            """

            http_options = _BaseEvaluationServiceRestTransport._BaseCreateEvaluationExpectation._get_http_options()
            request, metadata = self._interceptor.pre_create_evaluation_expectation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEvaluationServiceRestTransport._BaseCreateEvaluationExpectation,
                    "_BaseCreateEvaluationExpectation__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.ces_v1beta.EvaluationServiceClient.CreateEvaluationExpectation",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.EvaluationService",
                        "rpcName": "CreateEvaluationExpectation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = EvaluationServiceRestTransport._CreateEvaluationExpectation._get_response(
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
            resp = evaluation.EvaluationExpectation()
            pb_resp = evaluation.EvaluationExpectation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_evaluation_expectation(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_create_evaluation_expectation_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = evaluation.EvaluationExpectation.to_json(
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
                    "Received response for google.cloud.ces_v1beta.EvaluationServiceClient.create_evaluation_expectation",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.EvaluationService",
                        "rpcName": "CreateEvaluationExpectation",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateScheduledEvaluationRun(
        _BaseEvaluationServiceRestTransport._BaseCreateScheduledEvaluationRun,
        EvaluationServiceRestStub,
    ):
        def __hash__(self):
            return hash("EvaluationServiceRestTransport.CreateScheduledEvaluationRun")

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
            request: evaluation_service.CreateScheduledEvaluationRunRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> evaluation.ScheduledEvaluationRun:
            r"""Call the create scheduled
            evaluation run method over HTTP.

                Args:
                    request (~.evaluation_service.CreateScheduledEvaluationRunRequest):
                        The request object. Request message for
                    [EvaluationService.CreateScheduledEvaluationRun][google.cloud.ces.v1beta.EvaluationService.CreateScheduledEvaluationRun].
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.evaluation.ScheduledEvaluationRun:
                        Represents a scheduled evaluation run
                    configuration.

            """

            http_options = _BaseEvaluationServiceRestTransport._BaseCreateScheduledEvaluationRun._get_http_options()
            request, metadata = self._interceptor.pre_create_scheduled_evaluation_run(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEvaluationServiceRestTransport._BaseCreateScheduledEvaluationRun,
                    "_BaseCreateScheduledEvaluationRun__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.ces_v1beta.EvaluationServiceClient.CreateScheduledEvaluationRun",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.EvaluationService",
                        "rpcName": "CreateScheduledEvaluationRun",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = EvaluationServiceRestTransport._CreateScheduledEvaluationRun._get_response(
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
            resp = evaluation.ScheduledEvaluationRun()
            pb_resp = evaluation.ScheduledEvaluationRun.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_scheduled_evaluation_run(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_create_scheduled_evaluation_run_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = evaluation.ScheduledEvaluationRun.to_json(
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
                    "Received response for google.cloud.ces_v1beta.EvaluationServiceClient.create_scheduled_evaluation_run",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.EvaluationService",
                        "rpcName": "CreateScheduledEvaluationRun",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteEvaluation(
        _BaseEvaluationServiceRestTransport._BaseDeleteEvaluation,
        EvaluationServiceRestStub,
    ):
        def __hash__(self):
            return hash("EvaluationServiceRestTransport.DeleteEvaluation")

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
            request: evaluation_service.DeleteEvaluationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete evaluation method over HTTP.

            Args:
                request (~.evaluation_service.DeleteEvaluationRequest):
                    The request object. Request message for
                [EvaluationService.DeleteEvaluation][google.cloud.ces.v1beta.EvaluationService.DeleteEvaluation].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = _BaseEvaluationServiceRestTransport._BaseDeleteEvaluation._get_http_options()
            request, metadata = self._interceptor.pre_delete_evaluation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEvaluationServiceRestTransport._BaseDeleteEvaluation,
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
                    f"Sending request for google.cloud.ces_v1beta.EvaluationServiceClient.DeleteEvaluation",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.EvaluationService",
                        "rpcName": "DeleteEvaluation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = EvaluationServiceRestTransport._DeleteEvaluation._get_response(
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

    class _DeleteEvaluationDataset(
        _BaseEvaluationServiceRestTransport._BaseDeleteEvaluationDataset,
        EvaluationServiceRestStub,
    ):
        def __hash__(self):
            return hash("EvaluationServiceRestTransport.DeleteEvaluationDataset")

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
            request: evaluation_service.DeleteEvaluationDatasetRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete evaluation dataset method over HTTP.

            Args:
                request (~.evaluation_service.DeleteEvaluationDatasetRequest):
                    The request object. Request message for
                [EvaluationService.DeleteEvaluationDataset][google.cloud.ces.v1beta.EvaluationService.DeleteEvaluationDataset].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = _BaseEvaluationServiceRestTransport._BaseDeleteEvaluationDataset._get_http_options()
            request, metadata = self._interceptor.pre_delete_evaluation_dataset(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEvaluationServiceRestTransport._BaseDeleteEvaluationDataset,
                    "_BaseDeleteEvaluationDataset__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.ces_v1beta.EvaluationServiceClient.DeleteEvaluationDataset",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.EvaluationService",
                        "rpcName": "DeleteEvaluationDataset",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                EvaluationServiceRestTransport._DeleteEvaluationDataset._get_response(
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

    class _DeleteEvaluationExpectation(
        _BaseEvaluationServiceRestTransport._BaseDeleteEvaluationExpectation,
        EvaluationServiceRestStub,
    ):
        def __hash__(self):
            return hash("EvaluationServiceRestTransport.DeleteEvaluationExpectation")

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
            request: evaluation_service.DeleteEvaluationExpectationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete evaluation
            expectation method over HTTP.

                Args:
                    request (~.evaluation_service.DeleteEvaluationExpectationRequest):
                        The request object. Request message for
                    [EvaluationService.DeleteEvaluationExpectation][google.cloud.ces.v1beta.EvaluationService.DeleteEvaluationExpectation].
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.
            """

            http_options = _BaseEvaluationServiceRestTransport._BaseDeleteEvaluationExpectation._get_http_options()
            request, metadata = self._interceptor.pre_delete_evaluation_expectation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEvaluationServiceRestTransport._BaseDeleteEvaluationExpectation,
                    "_BaseDeleteEvaluationExpectation__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.ces_v1beta.EvaluationServiceClient.DeleteEvaluationExpectation",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.EvaluationService",
                        "rpcName": "DeleteEvaluationExpectation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = EvaluationServiceRestTransport._DeleteEvaluationExpectation._get_response(
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

    class _DeleteEvaluationResult(
        _BaseEvaluationServiceRestTransport._BaseDeleteEvaluationResult,
        EvaluationServiceRestStub,
    ):
        def __hash__(self):
            return hash("EvaluationServiceRestTransport.DeleteEvaluationResult")

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
            request: evaluation_service.DeleteEvaluationResultRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete evaluation result method over HTTP.

            Args:
                request (~.evaluation_service.DeleteEvaluationResultRequest):
                    The request object. Request message for
                [EvaluationService.DeleteEvaluationResult][google.cloud.ces.v1beta.EvaluationService.DeleteEvaluationResult].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = _BaseEvaluationServiceRestTransport._BaseDeleteEvaluationResult._get_http_options()
            request, metadata = self._interceptor.pre_delete_evaluation_result(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEvaluationServiceRestTransport._BaseDeleteEvaluationResult,
                    "_BaseDeleteEvaluationResult__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.ces_v1beta.EvaluationServiceClient.DeleteEvaluationResult",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.EvaluationService",
                        "rpcName": "DeleteEvaluationResult",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                EvaluationServiceRestTransport._DeleteEvaluationResult._get_response(
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

    class _DeleteEvaluationRun(
        _BaseEvaluationServiceRestTransport._BaseDeleteEvaluationRun,
        EvaluationServiceRestStub,
    ):
        def __hash__(self):
            return hash("EvaluationServiceRestTransport.DeleteEvaluationRun")

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
            request: evaluation_service.DeleteEvaluationRunRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete evaluation run method over HTTP.

            Args:
                request (~.evaluation_service.DeleteEvaluationRunRequest):
                    The request object. Request message for
                [EvaluationService.DeleteEvaluationRun][google.cloud.ces.v1beta.EvaluationService.DeleteEvaluationRun].
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

            http_options = _BaseEvaluationServiceRestTransport._BaseDeleteEvaluationRun._get_http_options()
            request, metadata = self._interceptor.pre_delete_evaluation_run(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEvaluationServiceRestTransport._BaseDeleteEvaluationRun,
                    "_BaseDeleteEvaluationRun__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.ces_v1beta.EvaluationServiceClient.DeleteEvaluationRun",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.EvaluationService",
                        "rpcName": "DeleteEvaluationRun",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                EvaluationServiceRestTransport._DeleteEvaluationRun._get_response(
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
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_delete_evaluation_run(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_evaluation_run_with_metadata(
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
                    "Received response for google.cloud.ces_v1beta.EvaluationServiceClient.delete_evaluation_run",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.EvaluationService",
                        "rpcName": "DeleteEvaluationRun",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteScheduledEvaluationRun(
        _BaseEvaluationServiceRestTransport._BaseDeleteScheduledEvaluationRun,
        EvaluationServiceRestStub,
    ):
        def __hash__(self):
            return hash("EvaluationServiceRestTransport.DeleteScheduledEvaluationRun")

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
            request: evaluation_service.DeleteScheduledEvaluationRunRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete scheduled
            evaluation run method over HTTP.

                Args:
                    request (~.evaluation_service.DeleteScheduledEvaluationRunRequest):
                        The request object. Request message for
                    [EvaluationService.DeleteScheduledEvaluationRun][google.cloud.ces.v1beta.EvaluationService.DeleteScheduledEvaluationRun].
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.
            """

            http_options = _BaseEvaluationServiceRestTransport._BaseDeleteScheduledEvaluationRun._get_http_options()
            request, metadata = self._interceptor.pre_delete_scheduled_evaluation_run(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEvaluationServiceRestTransport._BaseDeleteScheduledEvaluationRun,
                    "_BaseDeleteScheduledEvaluationRun__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.ces_v1beta.EvaluationServiceClient.DeleteScheduledEvaluationRun",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.EvaluationService",
                        "rpcName": "DeleteScheduledEvaluationRun",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = EvaluationServiceRestTransport._DeleteScheduledEvaluationRun._get_response(
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

    class _ExportEvaluationResults(
        _BaseEvaluationServiceRestTransport._BaseExportEvaluationResults,
        EvaluationServiceRestStub,
    ):
        def __hash__(self):
            return hash("EvaluationServiceRestTransport.ExportEvaluationResults")

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
            request: evaluation_service.ExportEvaluationResultsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the export evaluation results method over HTTP.

            Args:
                request (~.evaluation_service.ExportEvaluationResultsRequest):
                    The request object. Request message for
                [EvaluationService.ExportEvaluationResults][google.cloud.ces.v1beta.EvaluationService.ExportEvaluationResults].
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

            http_options = _BaseEvaluationServiceRestTransport._BaseExportEvaluationResults._get_http_options()
            request, metadata = self._interceptor.pre_export_evaluation_results(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEvaluationServiceRestTransport._BaseExportEvaluationResults,
                    "_BaseExportEvaluationResults__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.ces_v1beta.EvaluationServiceClient.ExportEvaluationResults",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.EvaluationService",
                        "rpcName": "ExportEvaluationResults",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                EvaluationServiceRestTransport._ExportEvaluationResults._get_response(
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

            resp = self._interceptor.post_export_evaluation_results(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_export_evaluation_results_with_metadata(
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
                    "Received response for google.cloud.ces_v1beta.EvaluationServiceClient.export_evaluation_results",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.EvaluationService",
                        "rpcName": "ExportEvaluationResults",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ExportEvaluationRuns(
        _BaseEvaluationServiceRestTransport._BaseExportEvaluationRuns,
        EvaluationServiceRestStub,
    ):
        def __hash__(self):
            return hash("EvaluationServiceRestTransport.ExportEvaluationRuns")

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
            request: evaluation_service.ExportEvaluationRunsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the export evaluation runs method over HTTP.

            Args:
                request (~.evaluation_service.ExportEvaluationRunsRequest):
                    The request object. Request message for
                [EvaluationService.ExportEvaluationRuns][google.cloud.ces.v1beta.EvaluationService.ExportEvaluationRuns].
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

            http_options = _BaseEvaluationServiceRestTransport._BaseExportEvaluationRuns._get_http_options()
            request, metadata = self._interceptor.pre_export_evaluation_runs(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEvaluationServiceRestTransport._BaseExportEvaluationRuns,
                    "_BaseExportEvaluationRuns__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.ces_v1beta.EvaluationServiceClient.ExportEvaluationRuns",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.EvaluationService",
                        "rpcName": "ExportEvaluationRuns",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                EvaluationServiceRestTransport._ExportEvaluationRuns._get_response(
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

            resp = self._interceptor.post_export_evaluation_runs(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_export_evaluation_runs_with_metadata(
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
                    "Received response for google.cloud.ces_v1beta.EvaluationServiceClient.export_evaluation_runs",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.EvaluationService",
                        "rpcName": "ExportEvaluationRuns",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ExportEvaluations(
        _BaseEvaluationServiceRestTransport._BaseExportEvaluations,
        EvaluationServiceRestStub,
    ):
        def __hash__(self):
            return hash("EvaluationServiceRestTransport.ExportEvaluations")

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
            request: evaluation_service.ExportEvaluationsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the export evaluations method over HTTP.

            Args:
                request (~.evaluation_service.ExportEvaluationsRequest):
                    The request object. Request message for
                [EvaluationService.ExportEvaluations][google.cloud.ces.v1beta.EvaluationService.ExportEvaluations].
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

            http_options = _BaseEvaluationServiceRestTransport._BaseExportEvaluations._get_http_options()
            request, metadata = self._interceptor.pre_export_evaluations(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEvaluationServiceRestTransport._BaseExportEvaluations,
                    "_BaseExportEvaluations__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.ces_v1beta.EvaluationServiceClient.ExportEvaluations",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.EvaluationService",
                        "rpcName": "ExportEvaluations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = EvaluationServiceRestTransport._ExportEvaluations._get_response(
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

            resp = self._interceptor.post_export_evaluations(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_export_evaluations_with_metadata(
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
                    "Received response for google.cloud.ces_v1beta.EvaluationServiceClient.export_evaluations",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.EvaluationService",
                        "rpcName": "ExportEvaluations",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GenerateEvaluation(
        _BaseEvaluationServiceRestTransport._BaseGenerateEvaluation,
        EvaluationServiceRestStub,
    ):
        def __hash__(self):
            return hash("EvaluationServiceRestTransport.GenerateEvaluation")

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
            request: evaluation_service.GenerateEvaluationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the generate evaluation method over HTTP.

            Args:
                request (~.evaluation_service.GenerateEvaluationRequest):
                    The request object. Request message for
                [EvaluationService.GenerateEvaluation][google.cloud.ces.v1beta.EvaluationService.GenerateEvaluation].
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

            http_options = _BaseEvaluationServiceRestTransport._BaseGenerateEvaluation._get_http_options()
            request, metadata = self._interceptor.pre_generate_evaluation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEvaluationServiceRestTransport._BaseGenerateEvaluation,
                    "_BaseGenerateEvaluation__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.ces_v1beta.EvaluationServiceClient.GenerateEvaluation",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.EvaluationService",
                        "rpcName": "GenerateEvaluation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = EvaluationServiceRestTransport._GenerateEvaluation._get_response(
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

            resp = self._interceptor.post_generate_evaluation(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_generate_evaluation_with_metadata(
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
                    "Received response for google.cloud.ces_v1beta.EvaluationServiceClient.generate_evaluation",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.EvaluationService",
                        "rpcName": "GenerateEvaluation",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetEvaluation(
        _BaseEvaluationServiceRestTransport._BaseGetEvaluation,
        EvaluationServiceRestStub,
    ):
        def __hash__(self):
            return hash("EvaluationServiceRestTransport.GetEvaluation")

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
            request: evaluation_service.GetEvaluationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> evaluation.Evaluation:
            r"""Call the get evaluation method over HTTP.

            Args:
                request (~.evaluation_service.GetEvaluationRequest):
                    The request object. Request message for
                [EvaluationService.GetEvaluation][google.cloud.ces.v1beta.EvaluationService.GetEvaluation].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.evaluation.Evaluation:
                    An evaluation represents all of the
                information needed to simulate and
                evaluate an agent.

            """

            http_options = _BaseEvaluationServiceRestTransport._BaseGetEvaluation._get_http_options()
            request, metadata = self._interceptor.pre_get_evaluation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEvaluationServiceRestTransport._BaseGetEvaluation,
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
                    f"Sending request for google.cloud.ces_v1beta.EvaluationServiceClient.GetEvaluation",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.EvaluationService",
                        "rpcName": "GetEvaluation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = EvaluationServiceRestTransport._GetEvaluation._get_response(
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
            resp = evaluation.Evaluation()
            pb_resp = evaluation.Evaluation.pb(resp)

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
                    response_payload = evaluation.Evaluation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.ces_v1beta.EvaluationServiceClient.get_evaluation",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.EvaluationService",
                        "rpcName": "GetEvaluation",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetEvaluationDataset(
        _BaseEvaluationServiceRestTransport._BaseGetEvaluationDataset,
        EvaluationServiceRestStub,
    ):
        def __hash__(self):
            return hash("EvaluationServiceRestTransport.GetEvaluationDataset")

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
            request: evaluation_service.GetEvaluationDatasetRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> evaluation.EvaluationDataset:
            r"""Call the get evaluation dataset method over HTTP.

            Args:
                request (~.evaluation_service.GetEvaluationDatasetRequest):
                    The request object. Request message for
                [EvaluationService.GetEvaluationDataset][google.cloud.ces.v1beta.EvaluationService.GetEvaluationDataset].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.evaluation.EvaluationDataset:
                    An evaluation dataset represents a
                set of evaluations that are grouped
                together basaed on shared tags.

            """

            http_options = _BaseEvaluationServiceRestTransport._BaseGetEvaluationDataset._get_http_options()
            request, metadata = self._interceptor.pre_get_evaluation_dataset(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEvaluationServiceRestTransport._BaseGetEvaluationDataset,
                    "_BaseGetEvaluationDataset__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.ces_v1beta.EvaluationServiceClient.GetEvaluationDataset",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.EvaluationService",
                        "rpcName": "GetEvaluationDataset",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                EvaluationServiceRestTransport._GetEvaluationDataset._get_response(
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
            resp = evaluation.EvaluationDataset()
            pb_resp = evaluation.EvaluationDataset.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_evaluation_dataset(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_evaluation_dataset_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = evaluation.EvaluationDataset.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.ces_v1beta.EvaluationServiceClient.get_evaluation_dataset",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.EvaluationService",
                        "rpcName": "GetEvaluationDataset",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetEvaluationExpectation(
        _BaseEvaluationServiceRestTransport._BaseGetEvaluationExpectation,
        EvaluationServiceRestStub,
    ):
        def __hash__(self):
            return hash("EvaluationServiceRestTransport.GetEvaluationExpectation")

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
            request: evaluation_service.GetEvaluationExpectationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> evaluation.EvaluationExpectation:
            r"""Call the get evaluation
            expectation method over HTTP.

                Args:
                    request (~.evaluation_service.GetEvaluationExpectationRequest):
                        The request object. Request message for
                    [EvaluationService.GetEvaluationExpectation][google.cloud.ces.v1beta.EvaluationService.GetEvaluationExpectation].
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.evaluation.EvaluationExpectation:
                        An evaluation expectation represents
                    a specific criteria to evaluate against.

            """

            http_options = _BaseEvaluationServiceRestTransport._BaseGetEvaluationExpectation._get_http_options()
            request, metadata = self._interceptor.pre_get_evaluation_expectation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEvaluationServiceRestTransport._BaseGetEvaluationExpectation,
                    "_BaseGetEvaluationExpectation__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.ces_v1beta.EvaluationServiceClient.GetEvaluationExpectation",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.EvaluationService",
                        "rpcName": "GetEvaluationExpectation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                EvaluationServiceRestTransport._GetEvaluationExpectation._get_response(
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
            resp = evaluation.EvaluationExpectation()
            pb_resp = evaluation.EvaluationExpectation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_evaluation_expectation(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_evaluation_expectation_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = evaluation.EvaluationExpectation.to_json(
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
                    "Received response for google.cloud.ces_v1beta.EvaluationServiceClient.get_evaluation_expectation",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.EvaluationService",
                        "rpcName": "GetEvaluationExpectation",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetEvaluationResult(
        _BaseEvaluationServiceRestTransport._BaseGetEvaluationResult,
        EvaluationServiceRestStub,
    ):
        def __hash__(self):
            return hash("EvaluationServiceRestTransport.GetEvaluationResult")

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
            request: evaluation_service.GetEvaluationResultRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> evaluation.EvaluationResult:
            r"""Call the get evaluation result method over HTTP.

            Args:
                request (~.evaluation_service.GetEvaluationResultRequest):
                    The request object. Request message for
                [EvaluationService.GetEvaluationResult][google.cloud.ces.v1beta.EvaluationService.GetEvaluationResult].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.evaluation.EvaluationResult:
                    An evaluation result represents the
                output of running an Evaluation.

            """

            http_options = _BaseEvaluationServiceRestTransport._BaseGetEvaluationResult._get_http_options()
            request, metadata = self._interceptor.pre_get_evaluation_result(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEvaluationServiceRestTransport._BaseGetEvaluationResult,
                    "_BaseGetEvaluationResult__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.ces_v1beta.EvaluationServiceClient.GetEvaluationResult",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.EvaluationService",
                        "rpcName": "GetEvaluationResult",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                EvaluationServiceRestTransport._GetEvaluationResult._get_response(
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
            resp = evaluation.EvaluationResult()
            pb_resp = evaluation.EvaluationResult.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_evaluation_result(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_evaluation_result_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = evaluation.EvaluationResult.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.ces_v1beta.EvaluationServiceClient.get_evaluation_result",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.EvaluationService",
                        "rpcName": "GetEvaluationResult",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetEvaluationRun(
        _BaseEvaluationServiceRestTransport._BaseGetEvaluationRun,
        EvaluationServiceRestStub,
    ):
        def __hash__(self):
            return hash("EvaluationServiceRestTransport.GetEvaluationRun")

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
            request: evaluation_service.GetEvaluationRunRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> evaluation.EvaluationRun:
            r"""Call the get evaluation run method over HTTP.

            Args:
                request (~.evaluation_service.GetEvaluationRunRequest):
                    The request object. Request message for
                [EvaluationService.GetEvaluationRun][google.cloud.ces.v1beta.EvaluationService.GetEvaluationRun].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.evaluation.EvaluationRun:
                    An evaluation run represents an all
                the evaluation results from an
                evaluation execution.

            """

            http_options = _BaseEvaluationServiceRestTransport._BaseGetEvaluationRun._get_http_options()
            request, metadata = self._interceptor.pre_get_evaluation_run(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEvaluationServiceRestTransport._BaseGetEvaluationRun,
                    "_BaseGetEvaluationRun__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.ces_v1beta.EvaluationServiceClient.GetEvaluationRun",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.EvaluationService",
                        "rpcName": "GetEvaluationRun",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = EvaluationServiceRestTransport._GetEvaluationRun._get_response(
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
            resp = evaluation.EvaluationRun()
            pb_resp = evaluation.EvaluationRun.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_evaluation_run(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_evaluation_run_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = evaluation.EvaluationRun.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.ces_v1beta.EvaluationServiceClient.get_evaluation_run",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.EvaluationService",
                        "rpcName": "GetEvaluationRun",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetScheduledEvaluationRun(
        _BaseEvaluationServiceRestTransport._BaseGetScheduledEvaluationRun,
        EvaluationServiceRestStub,
    ):
        def __hash__(self):
            return hash("EvaluationServiceRestTransport.GetScheduledEvaluationRun")

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
            request: evaluation_service.GetScheduledEvaluationRunRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> evaluation.ScheduledEvaluationRun:
            r"""Call the get scheduled evaluation
            run method over HTTP.

                Args:
                    request (~.evaluation_service.GetScheduledEvaluationRunRequest):
                        The request object. Request message for
                    [EvaluationService.GetScheduledEvaluationRun][google.cloud.ces.v1beta.EvaluationService.GetScheduledEvaluationRun].
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.evaluation.ScheduledEvaluationRun:
                        Represents a scheduled evaluation run
                    configuration.

            """

            http_options = _BaseEvaluationServiceRestTransport._BaseGetScheduledEvaluationRun._get_http_options()
            request, metadata = self._interceptor.pre_get_scheduled_evaluation_run(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEvaluationServiceRestTransport._BaseGetScheduledEvaluationRun,
                    "_BaseGetScheduledEvaluationRun__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.ces_v1beta.EvaluationServiceClient.GetScheduledEvaluationRun",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.EvaluationService",
                        "rpcName": "GetScheduledEvaluationRun",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                EvaluationServiceRestTransport._GetScheduledEvaluationRun._get_response(
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
            resp = evaluation.ScheduledEvaluationRun()
            pb_resp = evaluation.ScheduledEvaluationRun.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_scheduled_evaluation_run(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_scheduled_evaluation_run_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = evaluation.ScheduledEvaluationRun.to_json(
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
                    "Received response for google.cloud.ces_v1beta.EvaluationServiceClient.get_scheduled_evaluation_run",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.EvaluationService",
                        "rpcName": "GetScheduledEvaluationRun",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ImportEvaluations(
        _BaseEvaluationServiceRestTransport._BaseImportEvaluations,
        EvaluationServiceRestStub,
    ):
        def __hash__(self):
            return hash("EvaluationServiceRestTransport.ImportEvaluations")

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
            request: evaluation_service.ImportEvaluationsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the import evaluations method over HTTP.

            Args:
                request (~.evaluation_service.ImportEvaluationsRequest):
                    The request object. Request message for
                [EvaluationService.ImportEvaluations][google.cloud.ces.v1beta.EvaluationService.ImportEvaluations].
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

            http_options = _BaseEvaluationServiceRestTransport._BaseImportEvaluations._get_http_options()
            request, metadata = self._interceptor.pre_import_evaluations(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEvaluationServiceRestTransport._BaseImportEvaluations,
                    "_BaseImportEvaluations__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.ces_v1beta.EvaluationServiceClient.ImportEvaluations",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.EvaluationService",
                        "rpcName": "ImportEvaluations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = EvaluationServiceRestTransport._ImportEvaluations._get_response(
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

            resp = self._interceptor.post_import_evaluations(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_import_evaluations_with_metadata(
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
                    "Received response for google.cloud.ces_v1beta.EvaluationServiceClient.import_evaluations",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.EvaluationService",
                        "rpcName": "ImportEvaluations",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListEvaluationDatasets(
        _BaseEvaluationServiceRestTransport._BaseListEvaluationDatasets,
        EvaluationServiceRestStub,
    ):
        def __hash__(self):
            return hash("EvaluationServiceRestTransport.ListEvaluationDatasets")

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
            request: evaluation_service.ListEvaluationDatasetsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> evaluation_service.ListEvaluationDatasetsResponse:
            r"""Call the list evaluation datasets method over HTTP.

            Args:
                request (~.evaluation_service.ListEvaluationDatasetsRequest):
                    The request object. Request message for
                [EvaluationService.ListEvaluationDatasets][google.cloud.ces.v1beta.EvaluationService.ListEvaluationDatasets].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.evaluation_service.ListEvaluationDatasetsResponse:
                    Response message for
                [EvaluationService.ListEvaluationDatasets][google.cloud.ces.v1beta.EvaluationService.ListEvaluationDatasets].

            """

            http_options = _BaseEvaluationServiceRestTransport._BaseListEvaluationDatasets._get_http_options()
            request, metadata = self._interceptor.pre_list_evaluation_datasets(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEvaluationServiceRestTransport._BaseListEvaluationDatasets,
                    "_BaseListEvaluationDatasets__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.ces_v1beta.EvaluationServiceClient.ListEvaluationDatasets",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.EvaluationService",
                        "rpcName": "ListEvaluationDatasets",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                EvaluationServiceRestTransport._ListEvaluationDatasets._get_response(
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
            resp = evaluation_service.ListEvaluationDatasetsResponse()
            pb_resp = evaluation_service.ListEvaluationDatasetsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_evaluation_datasets(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_evaluation_datasets_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        evaluation_service.ListEvaluationDatasetsResponse.to_json(
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
                    "Received response for google.cloud.ces_v1beta.EvaluationServiceClient.list_evaluation_datasets",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.EvaluationService",
                        "rpcName": "ListEvaluationDatasets",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListEvaluationExpectations(
        _BaseEvaluationServiceRestTransport._BaseListEvaluationExpectations,
        EvaluationServiceRestStub,
    ):
        def __hash__(self):
            return hash("EvaluationServiceRestTransport.ListEvaluationExpectations")

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
            request: evaluation_service.ListEvaluationExpectationsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> evaluation_service.ListEvaluationExpectationsResponse:
            r"""Call the list evaluation
            expectations method over HTTP.

                Args:
                    request (~.evaluation_service.ListEvaluationExpectationsRequest):
                        The request object. Request message for
                    [EvaluationService.ListEvaluationExpectations][google.cloud.ces.v1beta.EvaluationService.ListEvaluationExpectations].
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.evaluation_service.ListEvaluationExpectationsResponse:
                        Response message for
                    [EvaluationService.ListEvaluationExpectations][google.cloud.ces.v1beta.EvaluationService.ListEvaluationExpectations].

            """

            http_options = _BaseEvaluationServiceRestTransport._BaseListEvaluationExpectations._get_http_options()
            request, metadata = self._interceptor.pre_list_evaluation_expectations(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEvaluationServiceRestTransport._BaseListEvaluationExpectations,
                    "_BaseListEvaluationExpectations__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.ces_v1beta.EvaluationServiceClient.ListEvaluationExpectations",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.EvaluationService",
                        "rpcName": "ListEvaluationExpectations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = EvaluationServiceRestTransport._ListEvaluationExpectations._get_response(
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
            resp = evaluation_service.ListEvaluationExpectationsResponse()
            pb_resp = evaluation_service.ListEvaluationExpectationsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_evaluation_expectations(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_evaluation_expectations_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        evaluation_service.ListEvaluationExpectationsResponse.to_json(
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
                    "Received response for google.cloud.ces_v1beta.EvaluationServiceClient.list_evaluation_expectations",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.EvaluationService",
                        "rpcName": "ListEvaluationExpectations",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListEvaluationResults(
        _BaseEvaluationServiceRestTransport._BaseListEvaluationResults,
        EvaluationServiceRestStub,
    ):
        def __hash__(self):
            return hash("EvaluationServiceRestTransport.ListEvaluationResults")

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
            request: evaluation_service.ListEvaluationResultsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> evaluation_service.ListEvaluationResultsResponse:
            r"""Call the list evaluation results method over HTTP.

            Args:
                request (~.evaluation_service.ListEvaluationResultsRequest):
                    The request object. Request message for
                [EvaluationService.ListEvaluationResults][google.cloud.ces.v1beta.EvaluationService.ListEvaluationResults].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.evaluation_service.ListEvaluationResultsResponse:
                    Response message for
                [EvaluationService.ListEvaluationResults][google.cloud.ces.v1beta.EvaluationService.ListEvaluationResults].

            """

            http_options = _BaseEvaluationServiceRestTransport._BaseListEvaluationResults._get_http_options()
            request, metadata = self._interceptor.pre_list_evaluation_results(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEvaluationServiceRestTransport._BaseListEvaluationResults,
                    "_BaseListEvaluationResults__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.ces_v1beta.EvaluationServiceClient.ListEvaluationResults",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.EvaluationService",
                        "rpcName": "ListEvaluationResults",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                EvaluationServiceRestTransport._ListEvaluationResults._get_response(
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
            resp = evaluation_service.ListEvaluationResultsResponse()
            pb_resp = evaluation_service.ListEvaluationResultsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_evaluation_results(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_evaluation_results_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        evaluation_service.ListEvaluationResultsResponse.to_json(
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
                    "Received response for google.cloud.ces_v1beta.EvaluationServiceClient.list_evaluation_results",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.EvaluationService",
                        "rpcName": "ListEvaluationResults",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListEvaluationRuns(
        _BaseEvaluationServiceRestTransport._BaseListEvaluationRuns,
        EvaluationServiceRestStub,
    ):
        def __hash__(self):
            return hash("EvaluationServiceRestTransport.ListEvaluationRuns")

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
            request: evaluation_service.ListEvaluationRunsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> evaluation_service.ListEvaluationRunsResponse:
            r"""Call the list evaluation runs method over HTTP.

            Args:
                request (~.evaluation_service.ListEvaluationRunsRequest):
                    The request object. Request message for
                [EvaluationService.ListEvaluationRuns][google.cloud.ces.v1beta.EvaluationService.ListEvaluationRuns].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.evaluation_service.ListEvaluationRunsResponse:
                    Response message for
                [EvaluationService.ListEvaluationRuns][google.cloud.ces.v1beta.EvaluationService.ListEvaluationRuns].

            """

            http_options = _BaseEvaluationServiceRestTransport._BaseListEvaluationRuns._get_http_options()
            request, metadata = self._interceptor.pre_list_evaluation_runs(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEvaluationServiceRestTransport._BaseListEvaluationRuns,
                    "_BaseListEvaluationRuns__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.ces_v1beta.EvaluationServiceClient.ListEvaluationRuns",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.EvaluationService",
                        "rpcName": "ListEvaluationRuns",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = EvaluationServiceRestTransport._ListEvaluationRuns._get_response(
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
            resp = evaluation_service.ListEvaluationRunsResponse()
            pb_resp = evaluation_service.ListEvaluationRunsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_evaluation_runs(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_evaluation_runs_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        evaluation_service.ListEvaluationRunsResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.ces_v1beta.EvaluationServiceClient.list_evaluation_runs",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.EvaluationService",
                        "rpcName": "ListEvaluationRuns",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListEvaluations(
        _BaseEvaluationServiceRestTransport._BaseListEvaluations,
        EvaluationServiceRestStub,
    ):
        def __hash__(self):
            return hash("EvaluationServiceRestTransport.ListEvaluations")

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
            request: evaluation_service.ListEvaluationsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> evaluation_service.ListEvaluationsResponse:
            r"""Call the list evaluations method over HTTP.

            Args:
                request (~.evaluation_service.ListEvaluationsRequest):
                    The request object. Request message for
                [EvaluationService.ListEvaluations][google.cloud.ces.v1beta.EvaluationService.ListEvaluations].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.evaluation_service.ListEvaluationsResponse:
                    Response message for
                [EvaluationService.ListEvaluations][google.cloud.ces.v1beta.EvaluationService.ListEvaluations].

            """

            http_options = _BaseEvaluationServiceRestTransport._BaseListEvaluations._get_http_options()
            request, metadata = self._interceptor.pre_list_evaluations(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEvaluationServiceRestTransport._BaseListEvaluations,
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
                    f"Sending request for google.cloud.ces_v1beta.EvaluationServiceClient.ListEvaluations",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.EvaluationService",
                        "rpcName": "ListEvaluations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = EvaluationServiceRestTransport._ListEvaluations._get_response(
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
            resp = evaluation_service.ListEvaluationsResponse()
            pb_resp = evaluation_service.ListEvaluationsResponse.pb(resp)

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
                    response_payload = (
                        evaluation_service.ListEvaluationsResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.ces_v1beta.EvaluationServiceClient.list_evaluations",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.EvaluationService",
                        "rpcName": "ListEvaluations",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListScheduledEvaluationRuns(
        _BaseEvaluationServiceRestTransport._BaseListScheduledEvaluationRuns,
        EvaluationServiceRestStub,
    ):
        def __hash__(self):
            return hash("EvaluationServiceRestTransport.ListScheduledEvaluationRuns")

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
            request: evaluation_service.ListScheduledEvaluationRunsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> evaluation_service.ListScheduledEvaluationRunsResponse:
            r"""Call the list scheduled evaluation
            runs method over HTTP.

                Args:
                    request (~.evaluation_service.ListScheduledEvaluationRunsRequest):
                        The request object. Request message for
                    [EvaluationService.ListScheduledEvaluationRuns][google.cloud.ces.v1beta.EvaluationService.ListScheduledEvaluationRuns].
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.evaluation_service.ListScheduledEvaluationRunsResponse:
                        Response message for
                    [EvaluationService.ListScheduledEvaluationRuns][google.cloud.ces.v1beta.EvaluationService.ListScheduledEvaluationRuns].

            """

            http_options = _BaseEvaluationServiceRestTransport._BaseListScheduledEvaluationRuns._get_http_options()
            request, metadata = self._interceptor.pre_list_scheduled_evaluation_runs(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEvaluationServiceRestTransport._BaseListScheduledEvaluationRuns,
                    "_BaseListScheduledEvaluationRuns__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.ces_v1beta.EvaluationServiceClient.ListScheduledEvaluationRuns",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.EvaluationService",
                        "rpcName": "ListScheduledEvaluationRuns",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = EvaluationServiceRestTransport._ListScheduledEvaluationRuns._get_response(
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
            resp = evaluation_service.ListScheduledEvaluationRunsResponse()
            pb_resp = evaluation_service.ListScheduledEvaluationRunsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_scheduled_evaluation_runs(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_list_scheduled_evaluation_runs_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        evaluation_service.ListScheduledEvaluationRunsResponse.to_json(
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
                    "Received response for google.cloud.ces_v1beta.EvaluationServiceClient.list_scheduled_evaluation_runs",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.EvaluationService",
                        "rpcName": "ListScheduledEvaluationRuns",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _RunEvaluation(
        _BaseEvaluationServiceRestTransport._BaseRunEvaluation,
        EvaluationServiceRestStub,
    ):
        def __hash__(self):
            return hash("EvaluationServiceRestTransport.RunEvaluation")

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
            request: evaluation.RunEvaluationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the run evaluation method over HTTP.

            Args:
                request (~.evaluation.RunEvaluationRequest):
                    The request object. Request message for
                [EvaluationService.RunEvaluation][google.cloud.ces.v1beta.EvaluationService.RunEvaluation].
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

            http_options = _BaseEvaluationServiceRestTransport._BaseRunEvaluation._get_http_options()
            request, metadata = self._interceptor.pre_run_evaluation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEvaluationServiceRestTransport._BaseRunEvaluation,
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
                    f"Sending request for google.cloud.ces_v1beta.EvaluationServiceClient.RunEvaluation",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.EvaluationService",
                        "rpcName": "RunEvaluation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = EvaluationServiceRestTransport._RunEvaluation._get_response(
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
                    "Received response for google.cloud.ces_v1beta.EvaluationServiceClient.run_evaluation",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.EvaluationService",
                        "rpcName": "RunEvaluation",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _RunEvaluationResultMetrics(
        _BaseEvaluationServiceRestTransport._BaseRunEvaluationResultMetrics,
        EvaluationServiceRestStub,
    ):
        def __hash__(self):
            return hash("EvaluationServiceRestTransport.RunEvaluationResultMetrics")

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
            request: evaluation_service.RunEvaluationResultMetricsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the run evaluation result
            metrics method over HTTP.

                Args:
                    request (~.evaluation_service.RunEvaluationResultMetricsRequest):
                        The request object. Request message for
                    [EvaluationService.RunEvaluationResultMetrics][google.cloud.ces.v1beta.EvaluationService.RunEvaluationResultMetrics].
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

            http_options = _BaseEvaluationServiceRestTransport._BaseRunEvaluationResultMetrics._get_http_options()
            request, metadata = self._interceptor.pre_run_evaluation_result_metrics(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEvaluationServiceRestTransport._BaseRunEvaluationResultMetrics,
                    "_BaseRunEvaluationResultMetrics__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.ces_v1beta.EvaluationServiceClient.RunEvaluationResultMetrics",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.EvaluationService",
                        "rpcName": "RunEvaluationResultMetrics",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = EvaluationServiceRestTransport._RunEvaluationResultMetrics._get_response(
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

            resp = self._interceptor.post_run_evaluation_result_metrics(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_run_evaluation_result_metrics_with_metadata(
                    resp, response_metadata
                )
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
                    "Received response for google.cloud.ces_v1beta.EvaluationServiceClient.run_evaluation_result_metrics",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.EvaluationService",
                        "rpcName": "RunEvaluationResultMetrics",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _TestPersonaVoice(
        _BaseEvaluationServiceRestTransport._BaseTestPersonaVoice,
        EvaluationServiceRestStub,
    ):
        def __hash__(self):
            return hash("EvaluationServiceRestTransport.TestPersonaVoice")

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
            request: evaluation_service.TestPersonaVoiceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> evaluation_service.TestPersonaVoiceResponse:
            r"""Call the test persona voice method over HTTP.

            Args:
                request (~.evaluation_service.TestPersonaVoiceRequest):
                    The request object. Request message for
                [EvaluationService.TestPersonaVoice][google.cloud.ces.v1beta.EvaluationService.TestPersonaVoice].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.evaluation_service.TestPersonaVoiceResponse:
                    Response message for
                [EvaluationService.TestPersonaVoice][google.cloud.ces.v1beta.EvaluationService.TestPersonaVoice].

            """

            http_options = _BaseEvaluationServiceRestTransport._BaseTestPersonaVoice._get_http_options()
            request, metadata = self._interceptor.pre_test_persona_voice(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEvaluationServiceRestTransport._BaseTestPersonaVoice,
                    "_BaseTestPersonaVoice__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.ces_v1beta.EvaluationServiceClient.TestPersonaVoice",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.EvaluationService",
                        "rpcName": "TestPersonaVoice",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = EvaluationServiceRestTransport._TestPersonaVoice._get_response(
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
            resp = evaluation_service.TestPersonaVoiceResponse()
            pb_resp = evaluation_service.TestPersonaVoiceResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_test_persona_voice(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_test_persona_voice_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        evaluation_service.TestPersonaVoiceResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.ces_v1beta.EvaluationServiceClient.test_persona_voice",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.EvaluationService",
                        "rpcName": "TestPersonaVoice",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateEvaluation(
        _BaseEvaluationServiceRestTransport._BaseUpdateEvaluation,
        EvaluationServiceRestStub,
    ):
        def __hash__(self):
            return hash("EvaluationServiceRestTransport.UpdateEvaluation")

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
            request: evaluation_service.UpdateEvaluationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gcc_evaluation.Evaluation:
            r"""Call the update evaluation method over HTTP.

            Args:
                request (~.evaluation_service.UpdateEvaluationRequest):
                    The request object. Request message for
                [EvaluationService.UpdateEvaluation][google.cloud.ces.v1beta.EvaluationService.UpdateEvaluation].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.gcc_evaluation.Evaluation:
                    An evaluation represents all of the
                information needed to simulate and
                evaluate an agent.

            """

            http_options = _BaseEvaluationServiceRestTransport._BaseUpdateEvaluation._get_http_options()
            request, metadata = self._interceptor.pre_update_evaluation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEvaluationServiceRestTransport._BaseUpdateEvaluation,
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
                    f"Sending request for google.cloud.ces_v1beta.EvaluationServiceClient.UpdateEvaluation",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.EvaluationService",
                        "rpcName": "UpdateEvaluation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = EvaluationServiceRestTransport._UpdateEvaluation._get_response(
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
            resp = gcc_evaluation.Evaluation()
            pb_resp = gcc_evaluation.Evaluation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_evaluation(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_evaluation_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = gcc_evaluation.Evaluation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.ces_v1beta.EvaluationServiceClient.update_evaluation",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.EvaluationService",
                        "rpcName": "UpdateEvaluation",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateEvaluationDataset(
        _BaseEvaluationServiceRestTransport._BaseUpdateEvaluationDataset,
        EvaluationServiceRestStub,
    ):
        def __hash__(self):
            return hash("EvaluationServiceRestTransport.UpdateEvaluationDataset")

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
            request: evaluation_service.UpdateEvaluationDatasetRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> evaluation.EvaluationDataset:
            r"""Call the update evaluation dataset method over HTTP.

            Args:
                request (~.evaluation_service.UpdateEvaluationDatasetRequest):
                    The request object. Request message for
                [EvaluationService.UpdateEvaluationDataset][google.cloud.ces.v1beta.EvaluationService.UpdateEvaluationDataset].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.evaluation.EvaluationDataset:
                    An evaluation dataset represents a
                set of evaluations that are grouped
                together basaed on shared tags.

            """

            http_options = _BaseEvaluationServiceRestTransport._BaseUpdateEvaluationDataset._get_http_options()
            request, metadata = self._interceptor.pre_update_evaluation_dataset(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEvaluationServiceRestTransport._BaseUpdateEvaluationDataset,
                    "_BaseUpdateEvaluationDataset__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.ces_v1beta.EvaluationServiceClient.UpdateEvaluationDataset",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.EvaluationService",
                        "rpcName": "UpdateEvaluationDataset",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                EvaluationServiceRestTransport._UpdateEvaluationDataset._get_response(
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
            resp = evaluation.EvaluationDataset()
            pb_resp = evaluation.EvaluationDataset.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_evaluation_dataset(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_evaluation_dataset_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = evaluation.EvaluationDataset.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.ces_v1beta.EvaluationServiceClient.update_evaluation_dataset",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.EvaluationService",
                        "rpcName": "UpdateEvaluationDataset",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateEvaluationExpectation(
        _BaseEvaluationServiceRestTransport._BaseUpdateEvaluationExpectation,
        EvaluationServiceRestStub,
    ):
        def __hash__(self):
            return hash("EvaluationServiceRestTransport.UpdateEvaluationExpectation")

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
            request: evaluation_service.UpdateEvaluationExpectationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> evaluation.EvaluationExpectation:
            r"""Call the update evaluation
            expectation method over HTTP.

                Args:
                    request (~.evaluation_service.UpdateEvaluationExpectationRequest):
                        The request object. Request message for
                    [EvaluationService.UpdateEvaluationExpectation][google.cloud.ces.v1beta.EvaluationService.UpdateEvaluationExpectation].
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.evaluation.EvaluationExpectation:
                        An evaluation expectation represents
                    a specific criteria to evaluate against.

            """

            http_options = _BaseEvaluationServiceRestTransport._BaseUpdateEvaluationExpectation._get_http_options()
            request, metadata = self._interceptor.pre_update_evaluation_expectation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEvaluationServiceRestTransport._BaseUpdateEvaluationExpectation,
                    "_BaseUpdateEvaluationExpectation__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.ces_v1beta.EvaluationServiceClient.UpdateEvaluationExpectation",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.EvaluationService",
                        "rpcName": "UpdateEvaluationExpectation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = EvaluationServiceRestTransport._UpdateEvaluationExpectation._get_response(
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
            resp = evaluation.EvaluationExpectation()
            pb_resp = evaluation.EvaluationExpectation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_evaluation_expectation(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_update_evaluation_expectation_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = evaluation.EvaluationExpectation.to_json(
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
                    "Received response for google.cloud.ces_v1beta.EvaluationServiceClient.update_evaluation_expectation",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.EvaluationService",
                        "rpcName": "UpdateEvaluationExpectation",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateScheduledEvaluationRun(
        _BaseEvaluationServiceRestTransport._BaseUpdateScheduledEvaluationRun,
        EvaluationServiceRestStub,
    ):
        def __hash__(self):
            return hash("EvaluationServiceRestTransport.UpdateScheduledEvaluationRun")

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
            request: evaluation_service.UpdateScheduledEvaluationRunRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> evaluation.ScheduledEvaluationRun:
            r"""Call the update scheduled
            evaluation run method over HTTP.

                Args:
                    request (~.evaluation_service.UpdateScheduledEvaluationRunRequest):
                        The request object. Request message for
                    [EvaluationService.UpdateScheduledEvaluationRun][google.cloud.ces.v1beta.EvaluationService.UpdateScheduledEvaluationRun].
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.evaluation.ScheduledEvaluationRun:
                        Represents a scheduled evaluation run
                    configuration.

            """

            http_options = _BaseEvaluationServiceRestTransport._BaseUpdateScheduledEvaluationRun._get_http_options()
            request, metadata = self._interceptor.pre_update_scheduled_evaluation_run(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEvaluationServiceRestTransport._BaseUpdateScheduledEvaluationRun,
                    "_BaseUpdateScheduledEvaluationRun__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.ces_v1beta.EvaluationServiceClient.UpdateScheduledEvaluationRun",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.EvaluationService",
                        "rpcName": "UpdateScheduledEvaluationRun",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = EvaluationServiceRestTransport._UpdateScheduledEvaluationRun._get_response(
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
            resp = evaluation.ScheduledEvaluationRun()
            pb_resp = evaluation.ScheduledEvaluationRun.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_scheduled_evaluation_run(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_update_scheduled_evaluation_run_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = evaluation.ScheduledEvaluationRun.to_json(
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
                    "Received response for google.cloud.ces_v1beta.EvaluationServiceClient.update_scheduled_evaluation_run",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.EvaluationService",
                        "rpcName": "UpdateScheduledEvaluationRun",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UploadEvaluationAudio(
        _BaseEvaluationServiceRestTransport._BaseUploadEvaluationAudio,
        EvaluationServiceRestStub,
    ):
        def __hash__(self):
            return hash("EvaluationServiceRestTransport.UploadEvaluationAudio")

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
            request: evaluation_service.UploadEvaluationAudioRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> evaluation_service.UploadEvaluationAudioResponse:
            r"""Call the upload evaluation audio method over HTTP.

            Args:
                request (~.evaluation_service.UploadEvaluationAudioRequest):
                    The request object. Request message for
                [EvaluationService.UploadEvaluationAudio][google.cloud.ces.v1beta.EvaluationService.UploadEvaluationAudio].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.evaluation_service.UploadEvaluationAudioResponse:
                    Response message for
                [EvaluationService.UploadEvaluationAudio][google.cloud.ces.v1beta.EvaluationService.UploadEvaluationAudio].

            """

            http_options = _BaseEvaluationServiceRestTransport._BaseUploadEvaluationAudio._get_http_options()
            request, metadata = self._interceptor.pre_upload_evaluation_audio(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEvaluationServiceRestTransport._BaseUploadEvaluationAudio,
                    "_BaseUploadEvaluationAudio__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.ces_v1beta.EvaluationServiceClient.UploadEvaluationAudio",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.EvaluationService",
                        "rpcName": "UploadEvaluationAudio",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                EvaluationServiceRestTransport._UploadEvaluationAudio._get_response(
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
            resp = evaluation_service.UploadEvaluationAudioResponse()
            pb_resp = evaluation_service.UploadEvaluationAudioResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_upload_evaluation_audio(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_upload_evaluation_audio_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        evaluation_service.UploadEvaluationAudioResponse.to_json(
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
                    "Received response for google.cloud.ces_v1beta.EvaluationServiceClient.upload_evaluation_audio",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.EvaluationService",
                        "rpcName": "UploadEvaluationAudio",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def create_evaluation(
        self,
    ) -> Callable[
        [evaluation_service.CreateEvaluationRequest], gcc_evaluation.Evaluation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateEvaluation(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_evaluation_dataset(
        self,
    ) -> Callable[
        [evaluation_service.CreateEvaluationDatasetRequest],
        evaluation.EvaluationDataset,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateEvaluationDataset(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def create_evaluation_expectation(
        self,
    ) -> Callable[
        [evaluation_service.CreateEvaluationExpectationRequest],
        evaluation.EvaluationExpectation,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateEvaluationExpectation(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def create_scheduled_evaluation_run(
        self,
    ) -> Callable[
        [evaluation_service.CreateScheduledEvaluationRunRequest],
        evaluation.ScheduledEvaluationRun,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateScheduledEvaluationRun(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def delete_evaluation(
        self,
    ) -> Callable[[evaluation_service.DeleteEvaluationRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteEvaluation(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_evaluation_dataset(
        self,
    ) -> Callable[[evaluation_service.DeleteEvaluationDatasetRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteEvaluationDataset(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def delete_evaluation_expectation(
        self,
    ) -> Callable[
        [evaluation_service.DeleteEvaluationExpectationRequest], empty_pb2.Empty
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteEvaluationExpectation(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def delete_evaluation_result(
        self,
    ) -> Callable[[evaluation_service.DeleteEvaluationResultRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteEvaluationResult(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def delete_evaluation_run(
        self,
    ) -> Callable[
        [evaluation_service.DeleteEvaluationRunRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteEvaluationRun(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_scheduled_evaluation_run(
        self,
    ) -> Callable[
        [evaluation_service.DeleteScheduledEvaluationRunRequest], empty_pb2.Empty
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteScheduledEvaluationRun(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def export_evaluation_results(
        self,
    ) -> Callable[
        [evaluation_service.ExportEvaluationResultsRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ExportEvaluationResults(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def export_evaluation_runs(
        self,
    ) -> Callable[
        [evaluation_service.ExportEvaluationRunsRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ExportEvaluationRuns(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def export_evaluations(
        self,
    ) -> Callable[
        [evaluation_service.ExportEvaluationsRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ExportEvaluations(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def generate_evaluation(
        self,
    ) -> Callable[
        [evaluation_service.GenerateEvaluationRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GenerateEvaluation(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_evaluation(
        self,
    ) -> Callable[[evaluation_service.GetEvaluationRequest], evaluation.Evaluation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetEvaluation(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_evaluation_dataset(
        self,
    ) -> Callable[
        [evaluation_service.GetEvaluationDatasetRequest], evaluation.EvaluationDataset
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetEvaluationDataset(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_evaluation_expectation(
        self,
    ) -> Callable[
        [evaluation_service.GetEvaluationExpectationRequest],
        evaluation.EvaluationExpectation,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetEvaluationExpectation(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def get_evaluation_result(
        self,
    ) -> Callable[
        [evaluation_service.GetEvaluationResultRequest], evaluation.EvaluationResult
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetEvaluationResult(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_evaluation_run(
        self,
    ) -> Callable[
        [evaluation_service.GetEvaluationRunRequest], evaluation.EvaluationRun
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetEvaluationRun(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_scheduled_evaluation_run(
        self,
    ) -> Callable[
        [evaluation_service.GetScheduledEvaluationRunRequest],
        evaluation.ScheduledEvaluationRun,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetScheduledEvaluationRun(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def import_evaluations(
        self,
    ) -> Callable[
        [evaluation_service.ImportEvaluationsRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ImportEvaluations(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_evaluation_datasets(
        self,
    ) -> Callable[
        [evaluation_service.ListEvaluationDatasetsRequest],
        evaluation_service.ListEvaluationDatasetsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListEvaluationDatasets(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def list_evaluation_expectations(
        self,
    ) -> Callable[
        [evaluation_service.ListEvaluationExpectationsRequest],
        evaluation_service.ListEvaluationExpectationsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListEvaluationExpectations(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def list_evaluation_results(
        self,
    ) -> Callable[
        [evaluation_service.ListEvaluationResultsRequest],
        evaluation_service.ListEvaluationResultsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListEvaluationResults(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_evaluation_runs(
        self,
    ) -> Callable[
        [evaluation_service.ListEvaluationRunsRequest],
        evaluation_service.ListEvaluationRunsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListEvaluationRuns(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_evaluations(
        self,
    ) -> Callable[
        [evaluation_service.ListEvaluationsRequest],
        evaluation_service.ListEvaluationsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListEvaluations(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_scheduled_evaluation_runs(
        self,
    ) -> Callable[
        [evaluation_service.ListScheduledEvaluationRunsRequest],
        evaluation_service.ListScheduledEvaluationRunsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListScheduledEvaluationRuns(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def run_evaluation(
        self,
    ) -> Callable[[evaluation.RunEvaluationRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._RunEvaluation(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def run_evaluation_result_metrics(
        self,
    ) -> Callable[
        [evaluation_service.RunEvaluationResultMetricsRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._RunEvaluationResultMetrics(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def test_persona_voice(
        self,
    ) -> Callable[
        [evaluation_service.TestPersonaVoiceRequest],
        evaluation_service.TestPersonaVoiceResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._TestPersonaVoice(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_evaluation(
        self,
    ) -> Callable[
        [evaluation_service.UpdateEvaluationRequest], gcc_evaluation.Evaluation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateEvaluation(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_evaluation_dataset(
        self,
    ) -> Callable[
        [evaluation_service.UpdateEvaluationDatasetRequest],
        evaluation.EvaluationDataset,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateEvaluationDataset(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def update_evaluation_expectation(
        self,
    ) -> Callable[
        [evaluation_service.UpdateEvaluationExpectationRequest],
        evaluation.EvaluationExpectation,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateEvaluationExpectation(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def update_scheduled_evaluation_run(
        self,
    ) -> Callable[
        [evaluation_service.UpdateScheduledEvaluationRunRequest],
        evaluation.ScheduledEvaluationRun,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateScheduledEvaluationRun(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def upload_evaluation_audio(
        self,
    ) -> Callable[
        [evaluation_service.UploadEvaluationAudioRequest],
        evaluation_service.UploadEvaluationAudioResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UploadEvaluationAudio(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_location(self):
        return self._GetLocation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetLocation(
        _BaseEvaluationServiceRestTransport._BaseGetLocation, EvaluationServiceRestStub
    ):
        def __hash__(self):
            return hash("EvaluationServiceRestTransport.GetLocation")

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
                _BaseEvaluationServiceRestTransport._BaseGetLocation._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_location(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEvaluationServiceRestTransport._BaseGetLocation,
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
                    f"Sending request for google.cloud.ces_v1beta.EvaluationServiceClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.EvaluationService",
                        "rpcName": "GetLocation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = EvaluationServiceRestTransport._GetLocation._get_response(
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
                    "Received response for google.cloud.ces_v1beta.EvaluationServiceAsyncClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.EvaluationService",
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
        _BaseEvaluationServiceRestTransport._BaseListLocations,
        EvaluationServiceRestStub,
    ):
        def __hash__(self):
            return hash("EvaluationServiceRestTransport.ListLocations")

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

            http_options = _BaseEvaluationServiceRestTransport._BaseListLocations._get_http_options()
            request, metadata = self._interceptor.pre_list_locations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEvaluationServiceRestTransport._BaseListLocations,
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
                    f"Sending request for google.cloud.ces_v1beta.EvaluationServiceClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.EvaluationService",
                        "rpcName": "ListLocations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = EvaluationServiceRestTransport._ListLocations._get_response(
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
                    "Received response for google.cloud.ces_v1beta.EvaluationServiceAsyncClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.EvaluationService",
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
        _BaseEvaluationServiceRestTransport._BaseCancelOperation,
        EvaluationServiceRestStub,
    ):
        def __hash__(self):
            return hash("EvaluationServiceRestTransport.CancelOperation")

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

            http_options = _BaseEvaluationServiceRestTransport._BaseCancelOperation._get_http_options()
            request, metadata = self._interceptor.pre_cancel_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEvaluationServiceRestTransport._BaseCancelOperation,
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
                    f"Sending request for google.cloud.ces_v1beta.EvaluationServiceClient.CancelOperation",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.EvaluationService",
                        "rpcName": "CancelOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = EvaluationServiceRestTransport._CancelOperation._get_response(
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
        _BaseEvaluationServiceRestTransport._BaseDeleteOperation,
        EvaluationServiceRestStub,
    ):
        def __hash__(self):
            return hash("EvaluationServiceRestTransport.DeleteOperation")

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

            http_options = _BaseEvaluationServiceRestTransport._BaseDeleteOperation._get_http_options()
            request, metadata = self._interceptor.pre_delete_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEvaluationServiceRestTransport._BaseDeleteOperation,
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
                    f"Sending request for google.cloud.ces_v1beta.EvaluationServiceClient.DeleteOperation",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.EvaluationService",
                        "rpcName": "DeleteOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = EvaluationServiceRestTransport._DeleteOperation._get_response(
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
        _BaseEvaluationServiceRestTransport._BaseGetOperation, EvaluationServiceRestStub
    ):
        def __hash__(self):
            return hash("EvaluationServiceRestTransport.GetOperation")

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

            http_options = _BaseEvaluationServiceRestTransport._BaseGetOperation._get_http_options()
            request, metadata = self._interceptor.pre_get_operation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEvaluationServiceRestTransport._BaseGetOperation,
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
                    f"Sending request for google.cloud.ces_v1beta.EvaluationServiceClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.EvaluationService",
                        "rpcName": "GetOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = EvaluationServiceRestTransport._GetOperation._get_response(
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
                    "Received response for google.cloud.ces_v1beta.EvaluationServiceAsyncClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.EvaluationService",
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
        _BaseEvaluationServiceRestTransport._BaseListOperations,
        EvaluationServiceRestStub,
    ):
        def __hash__(self):
            return hash("EvaluationServiceRestTransport.ListOperations")

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

            http_options = _BaseEvaluationServiceRestTransport._BaseListOperations._get_http_options()
            request, metadata = self._interceptor.pre_list_operations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEvaluationServiceRestTransport._BaseListOperations,
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
                    f"Sending request for google.cloud.ces_v1beta.EvaluationServiceClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.EvaluationService",
                        "rpcName": "ListOperations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = EvaluationServiceRestTransport._ListOperations._get_response(
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
                    "Received response for google.cloud.ces_v1beta.EvaluationServiceAsyncClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.EvaluationService",
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


__all__ = ("EvaluationServiceRestTransport",)
