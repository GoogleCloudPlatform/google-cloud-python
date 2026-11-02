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

from google.cloud.dialogflowcx_v3beta1._compat import transcode_request
from google.cloud.dialogflowcx_v3beta1.types import test_case
from google.cloud.dialogflowcx_v3beta1.types import test_case as gcdc_test_case

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseTestCasesRestTransport

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


class TestCasesRestInterceptor:
    """Interceptor for TestCases.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the TestCasesRestTransport.

    .. code-block:: python
        class MyCustomTestCasesInterceptor(TestCasesRestInterceptor):
            def pre_batch_delete_test_cases(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_batch_run_test_cases(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_run_test_cases(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_calculate_coverage(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_calculate_coverage(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_test_case(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_test_case(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_export_test_cases(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_export_test_cases(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_test_case(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_test_case(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_test_case_result(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_test_case_result(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_import_test_cases(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_import_test_cases(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_test_case_results(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_test_case_results(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_test_cases(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_test_cases(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_run_test_case(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_run_test_case(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_test_case(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_test_case(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = TestCasesRestTransport(interceptor=MyCustomTestCasesInterceptor())
        client = TestCasesClient(transport=transport)


    """

    def pre_batch_delete_test_cases(
        self,
        request: test_case.BatchDeleteTestCasesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        test_case.BatchDeleteTestCasesRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for batch_delete_test_cases

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TestCases server.
        """
        return request, metadata

    def pre_batch_run_test_cases(
        self,
        request: test_case.BatchRunTestCasesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        test_case.BatchRunTestCasesRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for batch_run_test_cases

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TestCases server.
        """
        return request, metadata

    def post_batch_run_test_cases(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for batch_run_test_cases

        DEPRECATED. Please use the `post_batch_run_test_cases_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the TestCases server but before
        it is returned to user code. This `post_batch_run_test_cases` interceptor runs
        before the `post_batch_run_test_cases_with_metadata` interceptor.
        """
        return response

    def post_batch_run_test_cases_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for batch_run_test_cases

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the TestCases server but before it is returned to user code.

        We recommend only using this `post_batch_run_test_cases_with_metadata`
        interceptor in new development instead of the `post_batch_run_test_cases` interceptor.
        When both interceptors are used, this `post_batch_run_test_cases_with_metadata` interceptor runs after the
        `post_batch_run_test_cases` interceptor. The (possibly modified) response returned by
        `post_batch_run_test_cases` will be passed to
        `post_batch_run_test_cases_with_metadata`.
        """
        return response, metadata

    def pre_calculate_coverage(
        self,
        request: test_case.CalculateCoverageRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        test_case.CalculateCoverageRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for calculate_coverage

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TestCases server.
        """
        return request, metadata

    def post_calculate_coverage(
        self, response: test_case.CalculateCoverageResponse
    ) -> test_case.CalculateCoverageResponse:
        """Post-rpc interceptor for calculate_coverage

        DEPRECATED. Please use the `post_calculate_coverage_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the TestCases server but before
        it is returned to user code. This `post_calculate_coverage` interceptor runs
        before the `post_calculate_coverage_with_metadata` interceptor.
        """
        return response

    def post_calculate_coverage_with_metadata(
        self,
        response: test_case.CalculateCoverageResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        test_case.CalculateCoverageResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for calculate_coverage

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the TestCases server but before it is returned to user code.

        We recommend only using this `post_calculate_coverage_with_metadata`
        interceptor in new development instead of the `post_calculate_coverage` interceptor.
        When both interceptors are used, this `post_calculate_coverage_with_metadata` interceptor runs after the
        `post_calculate_coverage` interceptor. The (possibly modified) response returned by
        `post_calculate_coverage` will be passed to
        `post_calculate_coverage_with_metadata`.
        """
        return response, metadata

    def pre_create_test_case(
        self,
        request: gcdc_test_case.CreateTestCaseRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gcdc_test_case.CreateTestCaseRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_test_case

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TestCases server.
        """
        return request, metadata

    def post_create_test_case(
        self, response: gcdc_test_case.TestCase
    ) -> gcdc_test_case.TestCase:
        """Post-rpc interceptor for create_test_case

        DEPRECATED. Please use the `post_create_test_case_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the TestCases server but before
        it is returned to user code. This `post_create_test_case` interceptor runs
        before the `post_create_test_case_with_metadata` interceptor.
        """
        return response

    def post_create_test_case_with_metadata(
        self,
        response: gcdc_test_case.TestCase,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[gcdc_test_case.TestCase, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_test_case

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the TestCases server but before it is returned to user code.

        We recommend only using this `post_create_test_case_with_metadata`
        interceptor in new development instead of the `post_create_test_case` interceptor.
        When both interceptors are used, this `post_create_test_case_with_metadata` interceptor runs after the
        `post_create_test_case` interceptor. The (possibly modified) response returned by
        `post_create_test_case` will be passed to
        `post_create_test_case_with_metadata`.
        """
        return response, metadata

    def pre_export_test_cases(
        self,
        request: test_case.ExportTestCasesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        test_case.ExportTestCasesRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for export_test_cases

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TestCases server.
        """
        return request, metadata

    def post_export_test_cases(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for export_test_cases

        DEPRECATED. Please use the `post_export_test_cases_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the TestCases server but before
        it is returned to user code. This `post_export_test_cases` interceptor runs
        before the `post_export_test_cases_with_metadata` interceptor.
        """
        return response

    def post_export_test_cases_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for export_test_cases

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the TestCases server but before it is returned to user code.

        We recommend only using this `post_export_test_cases_with_metadata`
        interceptor in new development instead of the `post_export_test_cases` interceptor.
        When both interceptors are used, this `post_export_test_cases_with_metadata` interceptor runs after the
        `post_export_test_cases` interceptor. The (possibly modified) response returned by
        `post_export_test_cases` will be passed to
        `post_export_test_cases_with_metadata`.
        """
        return response, metadata

    def pre_get_test_case(
        self,
        request: test_case.GetTestCaseRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[test_case.GetTestCaseRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_test_case

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TestCases server.
        """
        return request, metadata

    def post_get_test_case(self, response: test_case.TestCase) -> test_case.TestCase:
        """Post-rpc interceptor for get_test_case

        DEPRECATED. Please use the `post_get_test_case_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the TestCases server but before
        it is returned to user code. This `post_get_test_case` interceptor runs
        before the `post_get_test_case_with_metadata` interceptor.
        """
        return response

    def post_get_test_case_with_metadata(
        self,
        response: test_case.TestCase,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[test_case.TestCase, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_test_case

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the TestCases server but before it is returned to user code.

        We recommend only using this `post_get_test_case_with_metadata`
        interceptor in new development instead of the `post_get_test_case` interceptor.
        When both interceptors are used, this `post_get_test_case_with_metadata` interceptor runs after the
        `post_get_test_case` interceptor. The (possibly modified) response returned by
        `post_get_test_case` will be passed to
        `post_get_test_case_with_metadata`.
        """
        return response, metadata

    def pre_get_test_case_result(
        self,
        request: test_case.GetTestCaseResultRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        test_case.GetTestCaseResultRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_test_case_result

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TestCases server.
        """
        return request, metadata

    def post_get_test_case_result(
        self, response: test_case.TestCaseResult
    ) -> test_case.TestCaseResult:
        """Post-rpc interceptor for get_test_case_result

        DEPRECATED. Please use the `post_get_test_case_result_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the TestCases server but before
        it is returned to user code. This `post_get_test_case_result` interceptor runs
        before the `post_get_test_case_result_with_metadata` interceptor.
        """
        return response

    def post_get_test_case_result_with_metadata(
        self,
        response: test_case.TestCaseResult,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[test_case.TestCaseResult, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_test_case_result

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the TestCases server but before it is returned to user code.

        We recommend only using this `post_get_test_case_result_with_metadata`
        interceptor in new development instead of the `post_get_test_case_result` interceptor.
        When both interceptors are used, this `post_get_test_case_result_with_metadata` interceptor runs after the
        `post_get_test_case_result` interceptor. The (possibly modified) response returned by
        `post_get_test_case_result` will be passed to
        `post_get_test_case_result_with_metadata`.
        """
        return response, metadata

    def pre_import_test_cases(
        self,
        request: test_case.ImportTestCasesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        test_case.ImportTestCasesRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for import_test_cases

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TestCases server.
        """
        return request, metadata

    def post_import_test_cases(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for import_test_cases

        DEPRECATED. Please use the `post_import_test_cases_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the TestCases server but before
        it is returned to user code. This `post_import_test_cases` interceptor runs
        before the `post_import_test_cases_with_metadata` interceptor.
        """
        return response

    def post_import_test_cases_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for import_test_cases

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the TestCases server but before it is returned to user code.

        We recommend only using this `post_import_test_cases_with_metadata`
        interceptor in new development instead of the `post_import_test_cases` interceptor.
        When both interceptors are used, this `post_import_test_cases_with_metadata` interceptor runs after the
        `post_import_test_cases` interceptor. The (possibly modified) response returned by
        `post_import_test_cases` will be passed to
        `post_import_test_cases_with_metadata`.
        """
        return response, metadata

    def pre_list_test_case_results(
        self,
        request: test_case.ListTestCaseResultsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        test_case.ListTestCaseResultsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_test_case_results

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TestCases server.
        """
        return request, metadata

    def post_list_test_case_results(
        self, response: test_case.ListTestCaseResultsResponse
    ) -> test_case.ListTestCaseResultsResponse:
        """Post-rpc interceptor for list_test_case_results

        DEPRECATED. Please use the `post_list_test_case_results_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the TestCases server but before
        it is returned to user code. This `post_list_test_case_results` interceptor runs
        before the `post_list_test_case_results_with_metadata` interceptor.
        """
        return response

    def post_list_test_case_results_with_metadata(
        self,
        response: test_case.ListTestCaseResultsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        test_case.ListTestCaseResultsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_test_case_results

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the TestCases server but before it is returned to user code.

        We recommend only using this `post_list_test_case_results_with_metadata`
        interceptor in new development instead of the `post_list_test_case_results` interceptor.
        When both interceptors are used, this `post_list_test_case_results_with_metadata` interceptor runs after the
        `post_list_test_case_results` interceptor. The (possibly modified) response returned by
        `post_list_test_case_results` will be passed to
        `post_list_test_case_results_with_metadata`.
        """
        return response, metadata

    def pre_list_test_cases(
        self,
        request: test_case.ListTestCasesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[test_case.ListTestCasesRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for list_test_cases

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TestCases server.
        """
        return request, metadata

    def post_list_test_cases(
        self, response: test_case.ListTestCasesResponse
    ) -> test_case.ListTestCasesResponse:
        """Post-rpc interceptor for list_test_cases

        DEPRECATED. Please use the `post_list_test_cases_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the TestCases server but before
        it is returned to user code. This `post_list_test_cases` interceptor runs
        before the `post_list_test_cases_with_metadata` interceptor.
        """
        return response

    def post_list_test_cases_with_metadata(
        self,
        response: test_case.ListTestCasesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        test_case.ListTestCasesResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_test_cases

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the TestCases server but before it is returned to user code.

        We recommend only using this `post_list_test_cases_with_metadata`
        interceptor in new development instead of the `post_list_test_cases` interceptor.
        When both interceptors are used, this `post_list_test_cases_with_metadata` interceptor runs after the
        `post_list_test_cases` interceptor. The (possibly modified) response returned by
        `post_list_test_cases` will be passed to
        `post_list_test_cases_with_metadata`.
        """
        return response, metadata

    def pre_run_test_case(
        self,
        request: test_case.RunTestCaseRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[test_case.RunTestCaseRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for run_test_case

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TestCases server.
        """
        return request, metadata

    def post_run_test_case(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for run_test_case

        DEPRECATED. Please use the `post_run_test_case_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the TestCases server but before
        it is returned to user code. This `post_run_test_case` interceptor runs
        before the `post_run_test_case_with_metadata` interceptor.
        """
        return response

    def post_run_test_case_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for run_test_case

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the TestCases server but before it is returned to user code.

        We recommend only using this `post_run_test_case_with_metadata`
        interceptor in new development instead of the `post_run_test_case` interceptor.
        When both interceptors are used, this `post_run_test_case_with_metadata` interceptor runs after the
        `post_run_test_case` interceptor. The (possibly modified) response returned by
        `post_run_test_case` will be passed to
        `post_run_test_case_with_metadata`.
        """
        return response, metadata

    def pre_update_test_case(
        self,
        request: gcdc_test_case.UpdateTestCaseRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gcdc_test_case.UpdateTestCaseRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_test_case

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TestCases server.
        """
        return request, metadata

    def post_update_test_case(
        self, response: gcdc_test_case.TestCase
    ) -> gcdc_test_case.TestCase:
        """Post-rpc interceptor for update_test_case

        DEPRECATED. Please use the `post_update_test_case_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the TestCases server but before
        it is returned to user code. This `post_update_test_case` interceptor runs
        before the `post_update_test_case_with_metadata` interceptor.
        """
        return response

    def post_update_test_case_with_metadata(
        self,
        response: gcdc_test_case.TestCase,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[gcdc_test_case.TestCase, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_test_case

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the TestCases server but before it is returned to user code.

        We recommend only using this `post_update_test_case_with_metadata`
        interceptor in new development instead of the `post_update_test_case` interceptor.
        When both interceptors are used, this `post_update_test_case_with_metadata` interceptor runs after the
        `post_update_test_case` interceptor. The (possibly modified) response returned by
        `post_update_test_case` will be passed to
        `post_update_test_case_with_metadata`.
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
        before they are sent to the TestCases server.
        """
        return request, metadata

    def post_get_location(
        self, response: locations_pb2.Location
    ) -> locations_pb2.Location:
        """Post-rpc interceptor for get_location

        Override in a subclass to manipulate the response
        after it is returned by the TestCases server but before
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
        before they are sent to the TestCases server.
        """
        return request, metadata

    def post_list_locations(
        self, response: locations_pb2.ListLocationsResponse
    ) -> locations_pb2.ListLocationsResponse:
        """Post-rpc interceptor for list_locations

        Override in a subclass to manipulate the response
        after it is returned by the TestCases server but before
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
        before they are sent to the TestCases server.
        """
        return request, metadata

    def post_cancel_operation(self, response: None) -> None:
        """Post-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the response
        after it is returned by the TestCases server but before
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
        before they are sent to the TestCases server.
        """
        return request, metadata

    def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the TestCases server but before
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
        before they are sent to the TestCases server.
        """
        return request, metadata

    def post_list_operations(
        self, response: operations_pb2.ListOperationsResponse
    ) -> operations_pb2.ListOperationsResponse:
        """Post-rpc interceptor for list_operations

        Override in a subclass to manipulate the response
        after it is returned by the TestCases server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class TestCasesRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: TestCasesRestInterceptor


class TestCasesRestTransport(_BaseTestCasesRestTransport):
    """REST backend synchronous transport for TestCases.

    Service for managing [Test
    Cases][google.cloud.dialogflow.cx.v3beta1.TestCase] and [Test Case
    Results][google.cloud.dialogflow.cx.v3beta1.TestCaseResult].

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "dialogflow.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[TestCasesRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'dialogflow.googleapis.com').
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
            interceptor (Optional[TestCasesRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or TestCasesRestInterceptor()
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
                        "uri": "/v3beta1/{name=projects/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v3beta1/{name=projects/*/locations/*/operations/*}:cancel",
                    },
                ],
                "google.longrunning.Operations.GetOperation": [
                    {
                        "method": "get",
                        "uri": "/v3beta1/{name=projects/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v3beta1/{name=projects/*/locations/*/operations/*}",
                    },
                ],
                "google.longrunning.Operations.ListOperations": [
                    {
                        "method": "get",
                        "uri": "/v3beta1/{name=projects/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v3beta1/{name=projects/*/locations/*}/operations",
                    },
                ],
            }

            rest_transport = operations_v1.OperationsRestTransport(
                host=self._host,
                # use the credentials which are saved
                credentials=self._credentials,
                scopes=self._scopes,
                http_options=http_options,
                path_prefix="v3beta1",
            )

            self._operations_client = operations_v1.AbstractOperationsClient(
                transport=rest_transport
            )

        # Return the client from cache.
        return self._operations_client

    class _BatchDeleteTestCases(
        _BaseTestCasesRestTransport._BaseBatchDeleteTestCases, TestCasesRestStub
    ):
        def __hash__(self):
            return hash("TestCasesRestTransport.BatchDeleteTestCases")

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
            request: test_case.BatchDeleteTestCasesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the batch delete test cases method over HTTP.

            Args:
                request (~.test_case.BatchDeleteTestCasesRequest):
                    The request object. The request message for
                [TestCases.BatchDeleteTestCases][google.cloud.dialogflow.cx.v3beta1.TestCases.BatchDeleteTestCases].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = _BaseTestCasesRestTransport._BaseBatchDeleteTestCases._get_http_options()
            request, metadata = self._interceptor.pre_batch_delete_test_cases(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseTestCasesRestTransport._BaseBatchDeleteTestCases,
                    "_BaseBatchDeleteTestCases__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.dialogflow.cx_v3beta1.TestCasesClient.BatchDeleteTestCases",
                    extra={
                        "serviceName": "google.cloud.dialogflow.cx.v3beta1.TestCases",
                        "rpcName": "BatchDeleteTestCases",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = TestCasesRestTransport._BatchDeleteTestCases._get_response(
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

    class _BatchRunTestCases(
        _BaseTestCasesRestTransport._BaseBatchRunTestCases, TestCasesRestStub
    ):
        def __hash__(self):
            return hash("TestCasesRestTransport.BatchRunTestCases")

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
            request: test_case.BatchRunTestCasesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the batch run test cases method over HTTP.

            Args:
                request (~.test_case.BatchRunTestCasesRequest):
                    The request object. The request message for
                [TestCases.BatchRunTestCases][google.cloud.dialogflow.cx.v3beta1.TestCases.BatchRunTestCases].
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
                _BaseTestCasesRestTransport._BaseBatchRunTestCases._get_http_options()
            )
            request, metadata = self._interceptor.pre_batch_run_test_cases(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseTestCasesRestTransport._BaseBatchRunTestCases,
                    "_BaseBatchRunTestCases__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.dialogflow.cx_v3beta1.TestCasesClient.BatchRunTestCases",
                    extra={
                        "serviceName": "google.cloud.dialogflow.cx.v3beta1.TestCases",
                        "rpcName": "BatchRunTestCases",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = TestCasesRestTransport._BatchRunTestCases._get_response(
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

            resp = self._interceptor.post_batch_run_test_cases(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_batch_run_test_cases_with_metadata(
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
                    "Received response for google.cloud.dialogflow.cx_v3beta1.TestCasesClient.batch_run_test_cases",
                    extra={
                        "serviceName": "google.cloud.dialogflow.cx.v3beta1.TestCases",
                        "rpcName": "BatchRunTestCases",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CalculateCoverage(
        _BaseTestCasesRestTransport._BaseCalculateCoverage, TestCasesRestStub
    ):
        def __hash__(self):
            return hash("TestCasesRestTransport.CalculateCoverage")

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
            request: test_case.CalculateCoverageRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> test_case.CalculateCoverageResponse:
            r"""Call the calculate coverage method over HTTP.

            Args:
                request (~.test_case.CalculateCoverageRequest):
                    The request object. The request message for
                [TestCases.CalculateCoverage][google.cloud.dialogflow.cx.v3beta1.TestCases.CalculateCoverage].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.test_case.CalculateCoverageResponse:
                    The response message for
                [TestCases.CalculateCoverage][google.cloud.dialogflow.cx.v3beta1.TestCases.CalculateCoverage].

            """

            http_options = (
                _BaseTestCasesRestTransport._BaseCalculateCoverage._get_http_options()
            )
            request, metadata = self._interceptor.pre_calculate_coverage(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseTestCasesRestTransport._BaseCalculateCoverage,
                    "_BaseCalculateCoverage__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.dialogflow.cx_v3beta1.TestCasesClient.CalculateCoverage",
                    extra={
                        "serviceName": "google.cloud.dialogflow.cx.v3beta1.TestCases",
                        "rpcName": "CalculateCoverage",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = TestCasesRestTransport._CalculateCoverage._get_response(
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
            resp = test_case.CalculateCoverageResponse()
            pb_resp = test_case.CalculateCoverageResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_calculate_coverage(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_calculate_coverage_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = test_case.CalculateCoverageResponse.to_json(
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
                    "Received response for google.cloud.dialogflow.cx_v3beta1.TestCasesClient.calculate_coverage",
                    extra={
                        "serviceName": "google.cloud.dialogflow.cx.v3beta1.TestCases",
                        "rpcName": "CalculateCoverage",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateTestCase(
        _BaseTestCasesRestTransport._BaseCreateTestCase, TestCasesRestStub
    ):
        def __hash__(self):
            return hash("TestCasesRestTransport.CreateTestCase")

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
            request: gcdc_test_case.CreateTestCaseRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gcdc_test_case.TestCase:
            r"""Call the create test case method over HTTP.

            Args:
                request (~.gcdc_test_case.CreateTestCaseRequest):
                    The request object. The request message for
                [TestCases.CreateTestCase][google.cloud.dialogflow.cx.v3beta1.TestCases.CreateTestCase].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.gcdc_test_case.TestCase:
                    Represents a test case.
            """

            http_options = (
                _BaseTestCasesRestTransport._BaseCreateTestCase._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_test_case(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseTestCasesRestTransport._BaseCreateTestCase,
                    "_BaseCreateTestCase__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.dialogflow.cx_v3beta1.TestCasesClient.CreateTestCase",
                    extra={
                        "serviceName": "google.cloud.dialogflow.cx.v3beta1.TestCases",
                        "rpcName": "CreateTestCase",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = TestCasesRestTransport._CreateTestCase._get_response(
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
            resp = gcdc_test_case.TestCase()
            pb_resp = gcdc_test_case.TestCase.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_test_case(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_test_case_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = gcdc_test_case.TestCase.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.dialogflow.cx_v3beta1.TestCasesClient.create_test_case",
                    extra={
                        "serviceName": "google.cloud.dialogflow.cx.v3beta1.TestCases",
                        "rpcName": "CreateTestCase",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ExportTestCases(
        _BaseTestCasesRestTransport._BaseExportTestCases, TestCasesRestStub
    ):
        def __hash__(self):
            return hash("TestCasesRestTransport.ExportTestCases")

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
            request: test_case.ExportTestCasesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the export test cases method over HTTP.

            Args:
                request (~.test_case.ExportTestCasesRequest):
                    The request object. The request message for
                [TestCases.ExportTestCases][google.cloud.dialogflow.cx.v3beta1.TestCases.ExportTestCases].
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
                _BaseTestCasesRestTransport._BaseExportTestCases._get_http_options()
            )
            request, metadata = self._interceptor.pre_export_test_cases(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseTestCasesRestTransport._BaseExportTestCases,
                    "_BaseExportTestCases__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.dialogflow.cx_v3beta1.TestCasesClient.ExportTestCases",
                    extra={
                        "serviceName": "google.cloud.dialogflow.cx.v3beta1.TestCases",
                        "rpcName": "ExportTestCases",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = TestCasesRestTransport._ExportTestCases._get_response(
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

            resp = self._interceptor.post_export_test_cases(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_export_test_cases_with_metadata(
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
                    "Received response for google.cloud.dialogflow.cx_v3beta1.TestCasesClient.export_test_cases",
                    extra={
                        "serviceName": "google.cloud.dialogflow.cx.v3beta1.TestCases",
                        "rpcName": "ExportTestCases",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetTestCase(_BaseTestCasesRestTransport._BaseGetTestCase, TestCasesRestStub):
        def __hash__(self):
            return hash("TestCasesRestTransport.GetTestCase")

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
            request: test_case.GetTestCaseRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> test_case.TestCase:
            r"""Call the get test case method over HTTP.

            Args:
                request (~.test_case.GetTestCaseRequest):
                    The request object. The request message for
                [TestCases.GetTestCase][google.cloud.dialogflow.cx.v3beta1.TestCases.GetTestCase].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.test_case.TestCase:
                    Represents a test case.
            """

            http_options = (
                _BaseTestCasesRestTransport._BaseGetTestCase._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_test_case(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseTestCasesRestTransport._BaseGetTestCase,
                    "_BaseGetTestCase__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.dialogflow.cx_v3beta1.TestCasesClient.GetTestCase",
                    extra={
                        "serviceName": "google.cloud.dialogflow.cx.v3beta1.TestCases",
                        "rpcName": "GetTestCase",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = TestCasesRestTransport._GetTestCase._get_response(
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
            resp = test_case.TestCase()
            pb_resp = test_case.TestCase.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_test_case(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_test_case_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = test_case.TestCase.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.dialogflow.cx_v3beta1.TestCasesClient.get_test_case",
                    extra={
                        "serviceName": "google.cloud.dialogflow.cx.v3beta1.TestCases",
                        "rpcName": "GetTestCase",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetTestCaseResult(
        _BaseTestCasesRestTransport._BaseGetTestCaseResult, TestCasesRestStub
    ):
        def __hash__(self):
            return hash("TestCasesRestTransport.GetTestCaseResult")

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
            request: test_case.GetTestCaseResultRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> test_case.TestCaseResult:
            r"""Call the get test case result method over HTTP.

            Args:
                request (~.test_case.GetTestCaseResultRequest):
                    The request object. The request message for
                [TestCases.GetTestCaseResult][google.cloud.dialogflow.cx.v3beta1.TestCases.GetTestCaseResult].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.test_case.TestCaseResult:
                    Represents a result from running a
                test case in an agent environment.

            """

            http_options = (
                _BaseTestCasesRestTransport._BaseGetTestCaseResult._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_test_case_result(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseTestCasesRestTransport._BaseGetTestCaseResult,
                    "_BaseGetTestCaseResult__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.dialogflow.cx_v3beta1.TestCasesClient.GetTestCaseResult",
                    extra={
                        "serviceName": "google.cloud.dialogflow.cx.v3beta1.TestCases",
                        "rpcName": "GetTestCaseResult",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = TestCasesRestTransport._GetTestCaseResult._get_response(
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
            resp = test_case.TestCaseResult()
            pb_resp = test_case.TestCaseResult.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_test_case_result(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_test_case_result_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = test_case.TestCaseResult.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.dialogflow.cx_v3beta1.TestCasesClient.get_test_case_result",
                    extra={
                        "serviceName": "google.cloud.dialogflow.cx.v3beta1.TestCases",
                        "rpcName": "GetTestCaseResult",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ImportTestCases(
        _BaseTestCasesRestTransport._BaseImportTestCases, TestCasesRestStub
    ):
        def __hash__(self):
            return hash("TestCasesRestTransport.ImportTestCases")

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
            request: test_case.ImportTestCasesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the import test cases method over HTTP.

            Args:
                request (~.test_case.ImportTestCasesRequest):
                    The request object. The request message for
                [TestCases.ImportTestCases][google.cloud.dialogflow.cx.v3beta1.TestCases.ImportTestCases].
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
                _BaseTestCasesRestTransport._BaseImportTestCases._get_http_options()
            )
            request, metadata = self._interceptor.pre_import_test_cases(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseTestCasesRestTransport._BaseImportTestCases,
                    "_BaseImportTestCases__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.dialogflow.cx_v3beta1.TestCasesClient.ImportTestCases",
                    extra={
                        "serviceName": "google.cloud.dialogflow.cx.v3beta1.TestCases",
                        "rpcName": "ImportTestCases",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = TestCasesRestTransport._ImportTestCases._get_response(
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

            resp = self._interceptor.post_import_test_cases(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_import_test_cases_with_metadata(
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
                    "Received response for google.cloud.dialogflow.cx_v3beta1.TestCasesClient.import_test_cases",
                    extra={
                        "serviceName": "google.cloud.dialogflow.cx.v3beta1.TestCases",
                        "rpcName": "ImportTestCases",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListTestCaseResults(
        _BaseTestCasesRestTransport._BaseListTestCaseResults, TestCasesRestStub
    ):
        def __hash__(self):
            return hash("TestCasesRestTransport.ListTestCaseResults")

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
            request: test_case.ListTestCaseResultsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> test_case.ListTestCaseResultsResponse:
            r"""Call the list test case results method over HTTP.

            Args:
                request (~.test_case.ListTestCaseResultsRequest):
                    The request object. The request message for
                [TestCases.ListTestCaseResults][google.cloud.dialogflow.cx.v3beta1.TestCases.ListTestCaseResults].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.test_case.ListTestCaseResultsResponse:
                    The response message for
                [TestCases.ListTestCaseResults][google.cloud.dialogflow.cx.v3beta1.TestCases.ListTestCaseResults].

            """

            http_options = (
                _BaseTestCasesRestTransport._BaseListTestCaseResults._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_test_case_results(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseTestCasesRestTransport._BaseListTestCaseResults,
                    "_BaseListTestCaseResults__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.dialogflow.cx_v3beta1.TestCasesClient.ListTestCaseResults",
                    extra={
                        "serviceName": "google.cloud.dialogflow.cx.v3beta1.TestCases",
                        "rpcName": "ListTestCaseResults",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = TestCasesRestTransport._ListTestCaseResults._get_response(
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
            resp = test_case.ListTestCaseResultsResponse()
            pb_resp = test_case.ListTestCaseResultsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_test_case_results(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_test_case_results_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = test_case.ListTestCaseResultsResponse.to_json(
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
                    "Received response for google.cloud.dialogflow.cx_v3beta1.TestCasesClient.list_test_case_results",
                    extra={
                        "serviceName": "google.cloud.dialogflow.cx.v3beta1.TestCases",
                        "rpcName": "ListTestCaseResults",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListTestCases(
        _BaseTestCasesRestTransport._BaseListTestCases, TestCasesRestStub
    ):
        def __hash__(self):
            return hash("TestCasesRestTransport.ListTestCases")

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
            request: test_case.ListTestCasesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> test_case.ListTestCasesResponse:
            r"""Call the list test cases method over HTTP.

            Args:
                request (~.test_case.ListTestCasesRequest):
                    The request object. The request message for
                [TestCases.ListTestCases][google.cloud.dialogflow.cx.v3beta1.TestCases.ListTestCases].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.test_case.ListTestCasesResponse:
                    The response message for
                [TestCases.ListTestCases][google.cloud.dialogflow.cx.v3beta1.TestCases.ListTestCases].

            """

            http_options = (
                _BaseTestCasesRestTransport._BaseListTestCases._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_test_cases(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseTestCasesRestTransport._BaseListTestCases,
                    "_BaseListTestCases__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.dialogflow.cx_v3beta1.TestCasesClient.ListTestCases",
                    extra={
                        "serviceName": "google.cloud.dialogflow.cx.v3beta1.TestCases",
                        "rpcName": "ListTestCases",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = TestCasesRestTransport._ListTestCases._get_response(
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
            resp = test_case.ListTestCasesResponse()
            pb_resp = test_case.ListTestCasesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_test_cases(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_test_cases_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = test_case.ListTestCasesResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.dialogflow.cx_v3beta1.TestCasesClient.list_test_cases",
                    extra={
                        "serviceName": "google.cloud.dialogflow.cx.v3beta1.TestCases",
                        "rpcName": "ListTestCases",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _RunTestCase(_BaseTestCasesRestTransport._BaseRunTestCase, TestCasesRestStub):
        def __hash__(self):
            return hash("TestCasesRestTransport.RunTestCase")

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
            request: test_case.RunTestCaseRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the run test case method over HTTP.

            Args:
                request (~.test_case.RunTestCaseRequest):
                    The request object. The request message for
                [TestCases.RunTestCase][google.cloud.dialogflow.cx.v3beta1.TestCases.RunTestCase].
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
                _BaseTestCasesRestTransport._BaseRunTestCase._get_http_options()
            )
            request, metadata = self._interceptor.pre_run_test_case(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseTestCasesRestTransport._BaseRunTestCase,
                    "_BaseRunTestCase__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.dialogflow.cx_v3beta1.TestCasesClient.RunTestCase",
                    extra={
                        "serviceName": "google.cloud.dialogflow.cx.v3beta1.TestCases",
                        "rpcName": "RunTestCase",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = TestCasesRestTransport._RunTestCase._get_response(
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

            resp = self._interceptor.post_run_test_case(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_run_test_case_with_metadata(
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
                    "Received response for google.cloud.dialogflow.cx_v3beta1.TestCasesClient.run_test_case",
                    extra={
                        "serviceName": "google.cloud.dialogflow.cx.v3beta1.TestCases",
                        "rpcName": "RunTestCase",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateTestCase(
        _BaseTestCasesRestTransport._BaseUpdateTestCase, TestCasesRestStub
    ):
        def __hash__(self):
            return hash("TestCasesRestTransport.UpdateTestCase")

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
            request: gcdc_test_case.UpdateTestCaseRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gcdc_test_case.TestCase:
            r"""Call the update test case method over HTTP.

            Args:
                request (~.gcdc_test_case.UpdateTestCaseRequest):
                    The request object. The request message for
                [TestCases.UpdateTestCase][google.cloud.dialogflow.cx.v3beta1.TestCases.UpdateTestCase].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.gcdc_test_case.TestCase:
                    Represents a test case.
            """

            http_options = (
                _BaseTestCasesRestTransport._BaseUpdateTestCase._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_test_case(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseTestCasesRestTransport._BaseUpdateTestCase,
                    "_BaseUpdateTestCase__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.dialogflow.cx_v3beta1.TestCasesClient.UpdateTestCase",
                    extra={
                        "serviceName": "google.cloud.dialogflow.cx.v3beta1.TestCases",
                        "rpcName": "UpdateTestCase",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = TestCasesRestTransport._UpdateTestCase._get_response(
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
            resp = gcdc_test_case.TestCase()
            pb_resp = gcdc_test_case.TestCase.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_test_case(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_test_case_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = gcdc_test_case.TestCase.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.dialogflow.cx_v3beta1.TestCasesClient.update_test_case",
                    extra={
                        "serviceName": "google.cloud.dialogflow.cx.v3beta1.TestCases",
                        "rpcName": "UpdateTestCase",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def batch_delete_test_cases(
        self,
    ) -> Callable[[test_case.BatchDeleteTestCasesRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchDeleteTestCases(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def batch_run_test_cases(
        self,
    ) -> Callable[[test_case.BatchRunTestCasesRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchRunTestCases(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def calculate_coverage(
        self,
    ) -> Callable[
        [test_case.CalculateCoverageRequest], test_case.CalculateCoverageResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CalculateCoverage(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_test_case(
        self,
    ) -> Callable[[gcdc_test_case.CreateTestCaseRequest], gcdc_test_case.TestCase]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateTestCase(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def export_test_cases(
        self,
    ) -> Callable[[test_case.ExportTestCasesRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ExportTestCases(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_test_case(
        self,
    ) -> Callable[[test_case.GetTestCaseRequest], test_case.TestCase]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetTestCase(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_test_case_result(
        self,
    ) -> Callable[[test_case.GetTestCaseResultRequest], test_case.TestCaseResult]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetTestCaseResult(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def import_test_cases(
        self,
    ) -> Callable[[test_case.ImportTestCasesRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ImportTestCases(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_test_case_results(
        self,
    ) -> Callable[
        [test_case.ListTestCaseResultsRequest], test_case.ListTestCaseResultsResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListTestCaseResults(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_test_cases(
        self,
    ) -> Callable[[test_case.ListTestCasesRequest], test_case.ListTestCasesResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListTestCases(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def run_test_case(
        self,
    ) -> Callable[[test_case.RunTestCaseRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._RunTestCase(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_test_case(
        self,
    ) -> Callable[[gcdc_test_case.UpdateTestCaseRequest], gcdc_test_case.TestCase]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateTestCase(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_location(self):
        return self._GetLocation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetLocation(_BaseTestCasesRestTransport._BaseGetLocation, TestCasesRestStub):
        def __hash__(self):
            return hash("TestCasesRestTransport.GetLocation")

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
                _BaseTestCasesRestTransport._BaseGetLocation._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_location(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseTestCasesRestTransport._BaseGetLocation,
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
                    f"Sending request for google.cloud.dialogflow.cx_v3beta1.TestCasesClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.dialogflow.cx.v3beta1.TestCases",
                        "rpcName": "GetLocation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = TestCasesRestTransport._GetLocation._get_response(
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
                    "Received response for google.cloud.dialogflow.cx_v3beta1.TestCasesAsyncClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.dialogflow.cx.v3beta1.TestCases",
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
        _BaseTestCasesRestTransport._BaseListLocations, TestCasesRestStub
    ):
        def __hash__(self):
            return hash("TestCasesRestTransport.ListLocations")

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
                _BaseTestCasesRestTransport._BaseListLocations._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_locations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseTestCasesRestTransport._BaseListLocations,
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
                    f"Sending request for google.cloud.dialogflow.cx_v3beta1.TestCasesClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.dialogflow.cx.v3beta1.TestCases",
                        "rpcName": "ListLocations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = TestCasesRestTransport._ListLocations._get_response(
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
                    "Received response for google.cloud.dialogflow.cx_v3beta1.TestCasesAsyncClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.dialogflow.cx.v3beta1.TestCases",
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
        _BaseTestCasesRestTransport._BaseCancelOperation, TestCasesRestStub
    ):
        def __hash__(self):
            return hash("TestCasesRestTransport.CancelOperation")

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

            http_options = (
                _BaseTestCasesRestTransport._BaseCancelOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_cancel_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseTestCasesRestTransport._BaseCancelOperation,
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
                    f"Sending request for google.cloud.dialogflow.cx_v3beta1.TestCasesClient.CancelOperation",
                    extra={
                        "serviceName": "google.cloud.dialogflow.cx.v3beta1.TestCases",
                        "rpcName": "CancelOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = TestCasesRestTransport._CancelOperation._get_response(
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

            return self._interceptor.post_cancel_operation(None)

    @property
    def get_operation(self):
        return self._GetOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetOperation(
        _BaseTestCasesRestTransport._BaseGetOperation, TestCasesRestStub
    ):
        def __hash__(self):
            return hash("TestCasesRestTransport.GetOperation")

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
                _BaseTestCasesRestTransport._BaseGetOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_operation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseTestCasesRestTransport._BaseGetOperation,
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
                    f"Sending request for google.cloud.dialogflow.cx_v3beta1.TestCasesClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.dialogflow.cx.v3beta1.TestCases",
                        "rpcName": "GetOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = TestCasesRestTransport._GetOperation._get_response(
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
                    "Received response for google.cloud.dialogflow.cx_v3beta1.TestCasesAsyncClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.dialogflow.cx.v3beta1.TestCases",
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
        _BaseTestCasesRestTransport._BaseListOperations, TestCasesRestStub
    ):
        def __hash__(self):
            return hash("TestCasesRestTransport.ListOperations")

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

            http_options = (
                _BaseTestCasesRestTransport._BaseListOperations._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_operations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseTestCasesRestTransport._BaseListOperations,
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
                    f"Sending request for google.cloud.dialogflow.cx_v3beta1.TestCasesClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.dialogflow.cx.v3beta1.TestCases",
                        "rpcName": "ListOperations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = TestCasesRestTransport._ListOperations._get_response(
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
                    "Received response for google.cloud.dialogflow.cx_v3beta1.TestCasesAsyncClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.dialogflow.cx.v3beta1.TestCases",
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


__all__ = ("TestCasesRestTransport",)
